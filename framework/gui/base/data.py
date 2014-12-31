# coding=utf-8
__author__ = 'guguohai@outlook.com'


class Data():
    '''
    这里禁止线程读写，只允许单步操作
    '''

    def __init__(self):
        self.not_logged='Admin'
        self.task_header = (
            u'编号', u'任务名称', u'任务类型', u'任务状态', u'优先级', u'执行人', u'创建人', u'创建时间', u'更新时间', u'执行时间', u'结束时间',u'备注')

        # self.task_header = (u'编号', u'任务名称', u'任务类型', u'任务状态', u'优先级', u'执行人', u'创建人', u'创建时间', u'执行时间')
        self.tasks = (
            {'row': (
                u'001', u'接口测试', u'自动化', u'未开始', u'普通', u'顾国海', u'顾国海', u'2014-07-02 17:35:00', u'2014-07-02 17:35:00',
                u'2014-07-02 17:35:00',
                u'2014-07-02 17:35:00','desc'), 'script': []},
            {'row': (
                u'002', u'app平台测试', u'自动化', u'未开始', u'高级', u'顾国海', u'顾国海', u'2014-08-02 17:35:00',
                u'2014-08-02 17:35:00', u'2014-08-02 17:35:00',
                u'2014-08-02 17:35:00','desc'),
             'script': []})
        self.task_row = 'row'
        self.task_script = 'script'
        self.task_type = (u'自动化', u'车机测试', u'App', u'Web平台', u'接口', u'性能测试')
        self.priority = (u'普通', u'中级', u'高级')
        self.task_state = (u'未开始', u'已开始', u'已取消', u'已结束')
        self.page_size = 20


    def get_task_row(self):
        return self.tasks['row']
