# coding=utf-8
__author__ = 'ggh'

from Tkinter import *
import tkFont,ttk,tkMessageBox
import os,time,shutil,webbrowser
from framework.core import data as gui_data
from framework.report import report
from framework.core import task as ta


class MainWin():
    def __init__(self):
        self.root = Tk()
        self.root.title("AutoDriver")
        self.set_window_center(self.root, 750, 500)
        # self.root.wm_state('zoomed')
        self.root.iconbitmap('./wp.ico')
        self.case_data = []
        self.current_folder = ''
        self.node_path = ()
        self.temp_node_path = ()
        self.task_index = 0

        menubar = Menu(self.root)

        file_menu = Menu(menubar, tearoff=0)
        file_menu.add_command(label='新建测试任务', command=self.new_task)
        file_menu.add_command(label='退出', command=self.hello)
        menubar.add_cascade(label='文件', menu=file_menu)

        help_menu = Menu(menubar, tearoff=0)
        help_menu.add_command(label='About', command=self.hello)
        menubar.add_cascade(label='Help', menu=help_menu)

        self.root.config(menu=menubar)

        self.result_folder = PATH('../../result/')
        if not os.path.exists(self.result_folder):
            os.mkdir(self.result_folder)


    def hello(self):
        print 'hello'

    def base_form(self, master):
        frame_left = Frame(master)
        self.task_box = Listbox(frame_left, width=24, selectmode=SINGLE, height=28)
        scrollbar = Scrollbar(frame_left, orient=VERTICAL, command=self.task_box.yview)
        self.task_box.configure(yscroll=scrollbar.set)
        self.task_box.bind('<ButtonRelease-1>', self.printList)

        self.task_box.grid(row=0, column=0, sticky=NS)
        scrollbar.grid(row=0, column=1, sticky=NS)
        frame_left.pack(side=LEFT, fill=BOTH, padx=10, pady=10)  # grid(row=0, column=0, sticky=NS, padx=10, pady=10)

        for f in os.listdir(PATH('../../result/')):
            self.task_box.insert(END, f.replace('.db',''))

        frame_form = Frame(master)
        label_task = Label(frame_form, text='任务名称：')
        label_task.grid(row=0, column=0, sticky='w', padx=0, pady=5)
        self.var_task_name = StringVar()
        self.ipt_task = Entry(frame_form, width=40, textvariable=self.var_task_name)
        self.ipt_task.grid(row=0, column=1, sticky='w', columnspan=3, padx=0, pady=5)

        label_cases = Label(frame_form, text='选择用例：')
        label_cases.grid(row=1, column=0, sticky='w', padx=0, pady=5)
        ipt_cases = Entry(frame_form, width=40)
        ipt_cases.grid(row=1, column=1, sticky='w', pady=5, columnspan=3)
        btn_cases = Button(frame_form, text='选择', command=lambda: self.dialog_case())
        btn_cases.grid(row=1, column=3, sticky=E, pady=5)

        label_name = Label(frame_form, text='执行次数：')
        label_name.grid(row=2, column=0, sticky='w', padx=0, pady=5)
        e_num = StringVar()
        e_num.set('1')
        ipt_num = Entry(frame_form, textvariable=e_num)
        ipt_num.grid(row=2, column=1, sticky='w', padx=0, pady=5)

        label_creator = Label(frame_form, text='执行人：')
        label_creator.grid(row=2, column=2, sticky='w', padx=0, pady=5)
        e_creator = StringVar()
        e_creator.set('testing')
        ipt_creator = Entry(frame_form, textvariable=e_creator)
        ipt_creator.grid(row=2, column=3, sticky='w', padx=0, pady=5)
        frame_form.pack(side=LEFT, fill=BOTH, padx=10, pady=10)  # grid(row=0, column=1, sticky=NW, pady=10)  #

        # 按钮
        frame_action = Frame(frame_form)
        btn_start = Button(frame_action, text='执行任务', command=self.run_task)
        btn_start.grid(row=0, column=0, sticky='w', padx=5, pady=20)
        btn_stop = Button(frame_action, text='停止任务', command=self.stop_task)
        btn_stop.grid(row=0, column=1, sticky='w', padx=5, pady=20)
        btn_report = Button(frame_action, text='输出报告',command=self.generate_report)
        btn_report.grid(row=0, column=2, sticky='w', padx=5, pady=20)
        btn_save = Button(frame_action, text='保存任务', command=self.save_task)
        btn_save.grid(row=0, column=3, sticky='w', padx=5, pady=20)
        btn_del = Button(frame_action, text='删除任务', command=self.del_task)
        btn_del.grid(row=0, column=4, sticky='w', padx=5, pady=20)

        frame_action.grid(row=3, column=0, columnspan=4)

        self.task_info(0)


    def new_task(self):
        _name = 'task%s' % str(time.time()).replace('.', '')
        self.task_box.insert(0, _name)
        self.task_box.selection_clear(0, self.task_box.size() - 1)

        db_path = os.path.join(self.result_folder, '%s.db' % _name)
        db = gui_data.generateData(db_path)
        db.init_table(gui_data.DRIVER_TABLES)
        db.close()

        self.task_info(0)

    def save_task(self):
        db_name = self.task_box.get(self.task_index)
        self.task_box.delete(self.task_index)
        self.task_box.insert(self.task_index, self.ipt_task.get())
        self.task_box.selection_set(self.task_index)

        tar = os.path.join(self.result_folder, '%s.db' % self.ipt_task.get())
        src = os.path.join(self.result_folder, '%s.db' % db_name)
        os.rename(src, tar)

    def del_task(self):
        try:
            index = self.task_box.curselection()[0]
            self.task_box.delete(index)
            size = self.task_box.size()
            if size == index:
                if size > 1:
                    self.task_info(index - 1)
                else:
                    self.task_info(0)
            else:
                self.task_info(index)
        except IndexError:
            pass

    def task_info(self, index):
        _name = self.task_box.get(index)
        self.var_task_name.set(_name)

        # self.var_task_name.set(_name)
        self.task_index = index
        self.task_box.selection_set(index)

    def printList(self, event):
        # print event.keycode
        try:
            index = self.task_box.curselection()[0]
            self.task_info(index)
        except IndexError:
            pass

    def run_task(self):
        self.root.iconify()
        self.run_state = Toplevel(self.root)
        self.run_state.attributes("-topmost", True)
        self.run_state.overrideredirect(True)

        curWidth = 500
        curHeight = 25
        scnWidth, scnHeight = self.run_state.maxsize()
        tmpcnf = '%dx%d+%d+%d' % (curWidth, curHeight,
                                  (scnWidth - curWidth) / 2, 0)
        self.run_state.geometry(tmpcnf)

        label = Label(self.run_state, text='任务运行中，当前：。。。')
        label.pack(side=LEFT, fill=BOTH)

        task_list = []
        for c in self.case_data:
            t = ta.Task(c)
            task_list.append(t)

        db_path = PATH('../../result/%s.db' %self.ipt_task.get())
        runner = ta.TestRunner(task_list, db_path, self)
        runner.start()

    def stop_task(self):
        try:
            self.run_state.destroy()
        except AttributeError:
            pass

    def generate_report(self):
        '''
        测试完成，生成静态html报告
        :return:
        '''

        result_path = PATH('../../result/%s' % self.ipt_task.get())
        #index_name = db_path.split(os.sep)[-1].replace('.db', '')

        # if os.path.exists(result_path):
        #     ret = QMessageBox.warning(self, u'报告已存在',
        #                               u"\n已有报告存在，是否确认删除后继续生成报告？",
        #                               QMessageBox.Yes | QMessageBox.Cancel)
        #     if ret == QMessageBox.Yes:
        #         shutil.rmtree(PATH('../result/%s' % index_name))
        #         time.sleep(2)
        #
        #         rp = report.Report(result_path+'.db', 25)
        #         rp.start()
        #         webbrowser.open(PATH('../result/%s/%s1.html' % (index_name, index_name)))
        #     elif ret == QMessageBox.Cancel:
        #         pass

        rp = report.Report(result_path+'.db', 25)
        rp.start()

    def dialog_case(self):
        self.top = Toplevel(self.root)
        self.set_window_center(self.top, 600, 400)

        frame1 = Frame(self.top, width=100)

        tree = ttk.Treeview(frame1, height=18)
        ysb = ttk.Scrollbar(frame1, orient='vertical', command=tree.yview)
        tree.configure(yscroll=ysb.set)
        tree.heading('#0', text='Path', anchor='w')
        tree.column("#0", minwidth=0, width=250, stretch=NO)

        root_node = tree.insert('', 'end', text='TestCase', open=True)
        self.process_directory(tree, root_node, PATH('../../testcase/'))

        tree.grid(row=0)
        ysb.grid(row=0, column=1, sticky=NS)  # pack(side=RIGHT, fill=Y)
        frame1.grid(row=0, column=0)

        frame_action = Frame(self.top)
        btn_select = Button(frame_action, text='>', command=lambda: self.select_node(tree, listbox))
        btn_select.grid(row=0, column=0)
        btn_del = Button(frame_action, text='<', command=lambda: self.del_box_item(listbox))
        btn_del.grid(row=1, column=0)
        frame_action.grid(row=0, column=1, padx=10)

        frame2 = Frame(self.top, width=100)
        cnames = StringVar()
        # cnames.set(tuple(tnames))
        listbox = Listbox(frame2, listvariable=cnames, selectmode='extended', width=35, height=20)
        listbox.grid(row=0, column=0)

        frame2.grid(row=0, column=2)

        btn_ok = Button(self.top, text='确定', command=lambda: self.select_ok(listbox))
        btn_ok.grid(row=1, column=1)
        btn_cancel = Button(self.top, text='取消', command=lambda: self.top.destroy())
        btn_cancel.grid(row=1, column=2)


    def get_node_path(self, tree, current_item):
        parent = tree.parent(current_item)
        if parent:
            self.node_path += (parent,)
            self.get_node_path(tree, parent)


    def select_node(self, tree, box):
        sel_tup = tree.selection()

        if len(self.temp_node_path) == 0:
            self.temp_node_path = self.node_path

        if cmp(self.temp_node_path, self.node_path) == 0:
            self.temp_node_path = self.node_path
            self.node_path = ()
            # 判断listbox是否清空

            for st in sel_tup:
                box.insert(END, tree.item(st)['text'])
        else:
            print self.temp_node_path, self.node_path


    def del_box_item(self, box):
        indexs = box.curselection()
        for i in range(len(indexs)):
            box.delete(i)
            # print box.get(indexs[i])

    def select_ok(self, box):
        print box.get(0, END)

    def process_directory(self, tree, parent, path):
        for p in os.listdir(path):
            abspath = os.path.join(path, p)
            isdir = os.path.isdir(abspath)

            if os.path.isfile(abspath):
                test = re.compile("^test_.*?.py$")  # , re.IGNORECASE)
                match = test.match(p)
                if match:
                    tree.insert(parent, 'end', text=p, open=False)

            if isdir:
                oid = tree.insert(parent, 'end', text=p, open=False)
                self.process_directory(tree, oid, abspath)

    def send_value(self):
        print 'fwefe'

    # def start_test(self):
    # self.set_window_center(600, 300)

    def yview(self, *args):
        pass
        # apply(self.b1.yview, args)
        # apply(self.b2.yview, args)

    def load_data_box(self, parent):
        self.listbox_left = Listbox(parent, width=30, selectmode=EXTENDED)
        self.listbox_left.pack(side=LEFT, fill=Y)
        if self.case_data != None:
            for d in self.case_data:
                self.listbox_left.insert(END, d)

    def test_a(self, val):
        tagval = self.tag.get()

        v = find_folder(PATH('../../testcase/%s' % tagval))
        print v

    # def layout_widget(self):
    # frame1 = Frame()
    # frame1.pack(fill=BOTH, expand=1)
    #
    # self.tag = StringVar()
    # self.current_folder = '../../testcase/'
    # values = find_folder(PATH(self.current_folder))
    # cbox = ttk.Combobox(frame1, textvariable=self.tag, values=values, state='readonly')
    # cbox.current(0)
    # cbox.bind('<<ComboboxSelected>>', self.test_a)
    #
    # cbox.pack(side=LEFT)
    #
    # self.load_data_box(frame1)
    #
    # self.listbox_right = Listbox(frame1, width=30)
    # self.listbox_right.pack(side=RIGHT, fill=Y)
    # self.listbox_right.insert(END, 'gewgwe')
    #
    # button1 = Button(frame1, text="Move all", fg='blue', bg='yellow', command=self.move_all)
    # button1.pack()
    #     button2 = Button(frame1, text="Move Right", fg='blue', bg='yellow', command=self.move_right)
    #     button2.pack()
    #     button3 = Button(frame1, text="Move Left", fg='blue', bg='yellow', command=self.move_left)
    #     button3.pack()
    #
    #     frame2 = Frame()
    #     frame2.pack(fill=BOTH, expand=1)
    #     button = Button(frame2, text="OK", fg='blue', bg='yellow')
    #     button.pack(side=RIGHT, fill=Y)
    #
    # def move_all(self):
    #     tkMessageBox.showinfo('all', 'gwgweeewwe')
    #
    # def move_left(self):
    #     pass
    #
    # def move_right(self):
    #     # print self.listbox_left.selection_set(0,3)
    #     sel_tup = self.listbox_left.curselection()
    #     for st in sel_tup:
    #         self.listbox_right.insert(END, self.listbox_left.get(int(st)))
    #         self.listbox_left.delete(int(st))


    def set_window_center(self, parent, w, h):
        curWidth = w  # self.root.winfo_reqwidth() # get current width
        curHeight = h  # self.root.winfo_height() # get current height
        scnWidth, scnHeight = parent.maxsize()  # get screen width and height
        # now generate configuration information
        tmpcnf = '%dx%d+%d+%d' % (curWidth, curHeight,
                                  (scnWidth - curWidth) / 2, (scnHeight - curHeight) / 2)
        parent.geometry(tmpcnf)

        # def createWidgets(self, parent):
        # self.tb = ttk.Notebook(parent, height=200, width=300)
        # self.tree = ttk.Treeview(parent)
        # ysb = ttk.Scrollbar(parent, orient='vertical', command=self.tree.yview)
        # xsb = ttk.Scrollbar(parent, orient='horizontal', command=self.tree.xview)
        # self.tree.configure(yscroll=ysb.set, xscroll=xsb.set)
        # self.tree.heading('#0', text='Path', anchor='w')
        # path = find_file_dir(PATH('../../testcase/'))
        #
        # root_node = self.tree.insert('', 'end', text='TestCase', open=True)
        #
        # _path = PATH('../../testcase/')
        # folders = []
        # files = []
        # all_f = []
        # dirs = os.listdir(_path)
        # for f in dirs:
        # all_f.append(f)
        # if os.path.isdir(os.path.join(_path, f)):
        # folders.append(f)
        # else:
        # files.append(f)
        #
        #
        # self.process_directory(root_node, path)
        # 构建一个grid
        # self.tree.grid(row=0, column=0, sticky='n')
        # ysb.grid(row=0, column=1, sticky='ns')
        # xsb.grid(row=1, column=0, sticky='ew')
        # self.tb.grid(row=0, column=2)
        # self.tb.grid(row=0, column=0, sticky=N)
        # self.tree.bind('<<TreeviewSelect>>', self.dialog_case)

        # def process_directory(self, parent, path):
        # 遍历路径下的子目录
        # for p in path:
        # oid = self.tree.insert(parent, 'end', text=p, open=False)

        # def func(self, event):
        # # 返回对象为Tuple
        # select = self.tree.selection()
        # txt = self.tree.item(select[0])['text']
        # # listb = Listbox(width=100)
        # # self.tb.add(listb, text=self.tree.item(select[0])['text'])
        # self.listbox_right.insert(END, txt)


        # select = select[0]
        # if select == 'I002':  # and self.lock1 == 0:
        # lable = Label(text='欢迎登陆！', fg='black')

        # self.tb.add(lable, text='首页')
        # self.lock1 = 1


    def show(self):
        self.base_form(self.root)
        self.root.mainloop()


PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


def find_folder(folder_path):
    for parent, dirnames, filenames in os.walk(folder_path):
        if len(dirnames) > 0:
            return dirnames


def find_file_dir(path, parent, tree):
    folders = []
    files = []
    all_f = []
    dirs = os.listdir(path)
    for f in dirs:
        all_f.append(f)
        if os.path.isdir(os.path.join(path, f)):
            folders.append(f)

        else:
            tree.insert(parent, 'end', text=f, open=False)
            files.append(f)
    return all_f


if __name__ == '__main__':
    import data

    #data_list = data.walk_testcase(PATH('../../testcase/'))
    f = PATH('../../testcase/Autobook/')

    m = MainWin()
    m.show()


