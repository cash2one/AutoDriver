# coding=utf-8
__author__ = 'ggh'

from Tkinter import *
import tkFont
import ttk
import tkMessageBox
import os
# from PIL import ImageTk, Image


class MainWin():
    def __init__(self, case_data):
        self.root = Tk()
        self.root.title("AutoDriver")
        self.set_window_center(self.root, 570, 350)
        self.case_data = case_data
        self.current_folder = ''

        menubar = Menu(self.root)

        file_menu = Menu(menubar, tearoff=0)
        file_menu.add_command(label='新建测试任务', command=self.hello)
        file_menu.add_command(label='退出', command=self.hello)
        menubar.add_cascade(label='文件', menu=file_menu)

        history_menu = Menu(menubar, tearoff=0)
        history_menu.add_command(label='任务1', command=self.hello)
        history_menu.add_command(label='任务2', command=self.hello)
        # 所有结果列表都做为子菜单
        menubar.add_cascade(label='历史任务', menu=history_menu)
        self.root.config(menu=menubar)

        report_menu = Menu(menubar, tearoff=0)
        report_menu.add_command(label='发送', command=self.hello)
        report_menu.add_command(label='输出报告', command=self.hello)
        menubar.add_cascade(label='发送报告', menu=report_menu)

    def hello(self):
        print 'hello'

    def base_form(self, master):
        frame_form = Frame(master)
        label_task = Label(frame_form, text='任务名称：')
        label_task.grid(row=0, column=0, sticky='w', padx=0, pady=5)
        e = StringVar()
        e.set('input your text here')
        ipt_task = Entry(frame_form, text='0', width=55, textvariable=e)
        ipt_task.grid(row=0, column=1, sticky='w', columnspan=3, padx=0, pady=5)

        label_cases = Label(frame_form, text='选择用例：')
        label_cases.grid(row=1, column=0, sticky='w', padx=0, pady=5)
        ipt_cases = Entry(frame_form, text='0', width=55)
        ipt_cases.grid(row=1, column=1, sticky='w', pady=5, columnspan=3)
        btn_cases = Button(frame_form, text='选择', command=lambda: self.func())
        btn_cases.grid(row=1, column=4, sticky='w', pady=5)

        label_name = Label(frame_form, text='执行次数：')
        label_name.grid(row=2, column=0, sticky='w', padx=0, pady=5)
        ipt_name = Entry(frame_form, text='0')
        ipt_name.grid(row=2, column=1, sticky='w', padx=0, pady=5)

        label_creator = Label(frame_form, text='执行人：')
        label_creator.grid(row=2, column=2, sticky='w', padx=0, pady=5)
        ipt_creator = Entry(frame_form, text='0')
        ipt_creator.grid(row=2, column=3, sticky='w', padx=0, pady=5)

        # 按钮
        # frame_action = Frame(master)
        btn_start = Button(frame_form, text='执行用例', command=lambda: self.func())
        btn_start.grid(row=3, column=1, sticky='w', pady=5)
        btn_stop = Button(frame_form, text='停止用例')
        btn_stop.grid(row=3, column=2, sticky='w', pady=5)
        btn_report = Button(frame_form, text='输出报告')
        btn_report.grid(row=3, column=3, sticky='w', pady=5)

        frame_form.pack(fill=BOTH, expand=1, padx=20, pady=10)

        scrollbar = Scrollbar(master, orient=VERTICAL)
        listbox_status = Listbox(master, height=9, yscrollcommand=scrollbar.set, borderwidth=0)
        listbox_status.pack(side=LEFT, fill=BOTH, expand=1)
        scrollbar.config(command=self.yview)
        scrollbar.pack(side=RIGHT, fill=Y)
        # frame_list.pack(fill=BOTH, expand=1, padx=20, pady=0)

        # listbox_status = Listbox(frame_action, width=78, height=9, yscrollcommand=scrollbar.set)
        # scrollbar.configure(command=listbox_status.yview)
        # listbox_status.grid(row=2, column=0, sticky='wn', columnspan=4, padx=0, pady=5)

        listbox_status.insert(END, '测试结果信息')

    def func(self):
        self.top = Toplevel(self.root)
        self.set_window_center(self.top, 500, 400)

        frame1 = Frame(self.top, width=100)

        tree = ttk.Treeview(frame1)
        ysb = ttk.Scrollbar(frame1, orient='vertical', command=tree.yview)
        tree.configure(yscroll=ysb.set)
        tree.heading('#0', text='Path', anchor='w')

        root_node = tree.insert('', 'end', text='TestCase', open=True)
        self.process_directory(tree, root_node, PATH('../../testcase/'))

        tree.grid(row=0)
        ysb.grid(row=0, column=1, sticky=NS)  # pack(side=RIGHT, fill=Y)
        frame1.grid(row=0, column=0)

        frame2 = Frame(self.top, width=100)
        cnames = StringVar()
        # cnames.set(tuple(tnames))
        listbox = Listbox(frame2, listvariable=cnames, selectmode='extended')
        listbox.grid(row=0, column=0)

        frame2.grid(row=0, column=1)

        btn_select = Button(self.top, text='选择', command=lambda: self.select_node(tree, listbox))
        btn_select.grid(row=1, column=0)
        btn_del = Button(self.top, text='不选', command=lambda: self.del_box_item(listbox))
        btn_del.grid(row=1, column=1)
        btn_ok = Button(self.top, text='确定', command=lambda: self.select_ok(listbox))
        btn_ok.grid(row=1, column=2)


    def select_node(self, tree, box):
        # print tree.selection()
        sel_tup = tree.selection()
        for st in sel_tup:
            box.insert(END, tree.item(st)['text'])

    def del_box_item(self, box):
        indexs = box.curselection()
        for i in range(len(indexs)):
            print box.get(indexs[i])

    def select_ok(self, box):
        pass

    def process_directory(self, tree, parent, path):
        for p in os.listdir(path):
            abspath = os.path.join(path, p)
            isdir = os.path.isdir(abspath)
            oid = tree.insert(parent, 'end', text=p, open=False)
            if isdir:
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

    def layout_widget(self):
        frame1 = Frame()
        frame1.pack(fill=BOTH, expand=1)

        self.tag = StringVar()
        self.current_folder = '../../testcase/'
        values = find_folder(PATH(self.current_folder))
        cbox = ttk.Combobox(frame1, textvariable=self.tag, values=values, state='readonly')
        cbox.current(0)
        cbox.bind('<<ComboboxSelected>>', self.test_a)

        cbox.pack(side=LEFT)

        self.load_data_box(frame1)

        self.listbox_right = Listbox(frame1, width=30)
        self.listbox_right.pack(side=RIGHT, fill=Y)
        self.listbox_right.insert(END, 'gewgwe')

        button1 = Button(frame1, text="Move all", fg='blue', bg='yellow', command=self.move_all)
        button1.pack()
        button2 = Button(frame1, text="Move Right", fg='blue', bg='yellow', command=self.move_right)
        button2.pack()
        button3 = Button(frame1, text="Move Left", fg='blue', bg='yellow', command=self.move_left)
        button3.pack()

        frame2 = Frame()
        frame2.pack(fill=BOTH, expand=1)
        button = Button(frame2, text="OK", fg='blue', bg='yellow')
        button.pack(side=RIGHT, fill=Y)

    def move_all(self):
        tkMessageBox.showinfo('all', 'gwgweeewwe')

    def move_left(self):
        pass

    def move_right(self):
        # print self.listbox_left.selection_set(0,3)
        sel_tup = self.listbox_left.curselection()
        for st in sel_tup:
            self.listbox_right.insert(END, self.listbox_left.get(int(st)))
            self.listbox_left.delete(int(st))


    def set_window_center(self, parent, w, h):
        curWidth = w  # self.root.winfo_reqwidth() # get current width
        curHeight = h  # self.root.winfo_height() # get current height
        scnWidth, scnHeight = parent.maxsize()  # get screen width and height
        # now generate configuration information
        tmpcnf = '%dx%d+%d+%d' % (curWidth, curHeight,
                                  (scnWidth - curWidth) / 2, (scnHeight - curHeight) / 2)
        parent.geometry(tmpcnf)

    def createWidgets(self, parent):
        # self.tb = ttk.Notebook(parent, height=200, width=300)
        self.tree = ttk.Treeview(parent)
        ysb = ttk.Scrollbar(parent, orient='vertical', command=self.tree.yview)
        xsb = ttk.Scrollbar(parent, orient='horizontal', command=self.tree.xview)
        self.tree.configure(yscroll=ysb.set, xscroll=xsb.set)
        self.tree.heading('#0', text='Path', anchor='w')
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
        self.tree.grid(row=0, column=0, sticky='n')
        ysb.grid(row=0, column=1, sticky='ns')
        xsb.grid(row=1, column=0, sticky='ew')
        # self.tb.grid(row=0, column=2)
        # self.tb.grid(row=0, column=0, sticky=N)
        self.tree.bind('<<TreeviewSelect>>', self.func)

        # def process_directory(self, parent, path):
        # 遍历路径下的子目录
        # for p in path:
        # oid = self.tree.insert(parent, 'end', text=p, open=False)

        # def func(self, event):
        # # 返回对象为Tuple
        #     select = self.tree.selection()
        #     txt = self.tree.item(select[0])['text']
        #     # listb = Listbox(width=100)
        #     # self.tb.add(listb, text=self.tree.item(select[0])['text'])
        #     self.listbox_right.insert(END, txt)


        # select = select[0]
        # if select == 'I002':  # and self.lock1 == 0:
        # lable = Label(text='欢迎登陆！', fg='black')

        # self.tb.add(lable, text='首页')
        #self.lock1 = 1


    def show(self):
        self.base_form(self.root)
        # frame3 = Frame()
        # frame3.pack(fill=BOTH, expand=1)
        # self.createWidgets(frame3)
        # self.layout_widget()
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

    data_list = data.walk_testcase(PATH('../../testcase/'))
    f = PATH('../../testcase/Autobook/')

    m = MainWin(data_list)
    m.show()


