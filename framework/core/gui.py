# coding=utf-8
__author__ = 'ggh'

from Tkinter import *
import tkFont
import tkMessageBox
import os
from PIL import ImageTk, Image


def close_window(window):
    """give prompt when user close the window"""
    if tkMessageBox.askyesno("QUIT", "Close the Window(Yes/No)", icon="question"):
        window.destroy()


def manage_wifi(how, message_frame):
    """this function will open/close the wifi network accoring the arguments:
        how=1(open the network) how=2(close the network),
        message_frame(the frame which the message display"""

    open_wifi_cmd = "netsh wlan start hostednetwork"
    close_wifi_cmd = "netsh wlan stop hostednetwork"

    if how == 1:
        cmd = open_wifi_cmd
    else:
        cmd = close_wifi_cmd

    result = os.system(cmd)
    if result != 0:
        if how == 1:
            message_frame.listbox_insert("请检查无线网卡是否打开，设置是否正确")
        else:
            message_frame.listbox_insert("关闭WIFI失败！")
    else:
        if how == 1:
            message_frame.listbox_insert("WIFI已打开")
        else:
            message_frame.listbox_insert("WIFI已关闭")


class ShowMessageFrame():
    """will create a frame contanis a listbox and scrollbar"""

    def __init__(self):
        self.frame = Frame()
        self.message_ft = tkFont.Font(family="Arial", size=10)
        self.scrollbar = Scrollbar(self.frame, orient=VERTICAL)
        self.listbox = Listbox(self.frame, bg="white", selectbackground="blue",
                               selectmode="extended", font=self.message_ft, width=20)
        self.scrollbar.config(command=self.listbox.yview)
        self.scrollbar.pack(side=RIGHT, fill=Y)
        self.listbox.config(yscrollcommand=self.scrollbar.set)
        self.listbox.pack(side=LEFT, fill=BOTH, expand=1)

        self.listbox_insert("Welcome to WIFI!")

    def listbox_insert(self, args):
        self.listbox.insert(END, args)


class MyMenu():
    """Create the Menu for Window"""
    message_status = 1

    def __init__(self, root):

        self.menubar = Menu(root)
        self.optionmenu = Menu(self.menubar, tearoff=1)
        self.optionmenu.add_command(label='Show Message', command=lambda: self.show_messagebox(root))
        self.optionmenu.add_command(label='Hide Message', command=lambda: self.hide_messagebox(root))
        self.optionmenu.add_separator()
        self.optionmenu.add_command(label='Exit', command=lambda: close_window(root))
        self.menubar.add_cascade(label='Options', menu=self.optionmenu)

        self.helpmenu = Menu(self.menubar, tearoff=1)
        self.helpmenu.add_command(label='About', command=self.show_info)
        self.menubar.add_cascade(label='Help', menu=self.helpmenu)

        self.frame = ''

    def hide_messagebox(self, root):
        """will hide the message listbox and scrollbar"""
        if self.message_status == 1:
            self.frame = root.grid_slaves(2, 0)[0]
            root.grid_slaves(2, 0)[0].grid_remove()
            self.__class__.message_status = 0

    def show_messagebox(self, root):
        if self.message_status == 0 and self.frame != '':
            # print root.grid_slaves(2,0)

            self.frame.grid(row=2, columnspan=2, pady=5, sticky=S + N + E + W)
            self.__class__.message_status = 1
            self.frame = ''


    def show_info(self):
        """show the software info"""
        tkMessageBox.showinfo("About",
                              """
                    WIFI 热点助手
        ------------------------------------------
                version: 1.0
                author: Cullen
                Email:  wangyiyan402@163.com
        ------------------------------------------""")


class MyWindow():
    """ create the main window which include the image and two button(bounded the appropriate function"""

    def __init__(self):
        self.root = Tk()
        self.root.title("WIFI热点助手")

        self.root.update()  # update window ,must do
        curWidth = 900  # self.root.winfo_reqwidth() # get current width
        curHeight = 600  # self.root.winfo_height() # get current height
        scnWidth, scnHeight = self.root.maxsize()  # get screen width and height
        # now generate configuration information
        tmpcnf = '%dx%d+%d+%d' % (curWidth, curHeight,
                                  (scnWidth - curWidth) / 2, (scnHeight - curHeight) / 2)
        self.root.geometry(tmpcnf)

        # create menu
        my_menu = MyMenu(self.root)
        self.root.config(menu=my_menu.menubar)

        # font and image
        self.button_ft = tkFont.Font(family="Arial", size=10, weight=tkFont.BOLD)
        # self.image = Image.open("wifi.jpg")
        # self.bm = ImageTk.PhotoImage(self.image)
        #
        # self.label = Label(self.root, image=self.bm)
        # self.label.grid(row=0, columnspan=2)



        # create frame which include listbox and scrollbar
        message_frame = ShowMessageFrame()
        message_frame.frame.grid(row=2, columnspan=2, pady=5, sticky=S + N + E + W)
        # message_frame.frame.grid_forget()

        #create button
        self.open_button = Button(self.root, text="OPEN", font=self.button_ft, pady=10,
                                  width=10, borderwidth=2, bg="#F3E9CC", command=lambda: manage_wifi(1, message_frame))
        self.open_button.grid(row=1, column=0)

        self.close_button = Button(self.root, text="CLOSE", font=self.button_ft, pady=10,
                                   width=10, borderwidth=2, bg="#F3E9CC", command=lambda: manage_wifi(0, message_frame))
        self.close_button.grid(row=1, column=1)

        #prompt when user close the window
        self.root.protocol('WM_DELETE_WINDOW', lambda: close_window(self.root))
        self.root.mainloop()


class MainWin():
    def __init__(self):
        self.root = Tk()
        self.root.title("AutoDriver")
        self.set_window_center(900, 600)

    def layout_widget(self):
        frame1 = Frame()
        frame1.pack(fill=BOTH, expand=1)

        self.listbox_left = Listbox(frame1, width=30,selectmode = EXTENDED)
        self.listbox_left.pack(side=LEFT, fill=Y)
        for d in ['张三', '李四', '王五', '赵六', '前期', '无法', '问sass']:
            self.listbox_left.insert(END, d)

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
        pass

    def move_left(self):
        pass

    def move_right(self):
        #print self.listbox_left.selection_set(0,3)
        sel_tup= self.listbox_left.curselection()
        for st in sel_tup:
            self.listbox_right.insert(END,self.listbox_left.get(int(st)))
            self.listbox_left.delete(int(st))

    def set_window_center(self, w, h):
        curWidth = w  # self.root.winfo_reqwidth() # get current width
        curHeight = h  # self.root.winfo_height() # get current height
        scnWidth, scnHeight = self.root.maxsize()  # get screen width and height
        # now generate configuration information
        tmpcnf = '%dx%d+%d+%d' % (curWidth, curHeight,
                                  (scnWidth - curWidth) / 2, (scnHeight - curHeight) / 2)
        self.root.geometry(tmpcnf)

    def show(self):
        self.layout_widget()
        self.root.mainloop()


if __name__ == '__main__':
    # main()
    # my_window = MyWindow()
    m = MainWin()
    m.show()

