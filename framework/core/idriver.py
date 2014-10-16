# coding=utf-8
__author__ = 'Administrator'


from framework.core import the


def changeWork(isWorking):
    myself = the.android
    if the.i_driver['status'] != isWorking:
        myself.find_element_by_id('cn.com.pathbook.idriver.driver:id/tb_work_state').click()
        the.i_driver['status'] = isWorking


def license_type(val):
    license_types = {
        'lt_1':'大型客车','lt_2':'牵引车','lt_3':'城市公交车','lt_4':'中型客车',
        'lt_5':'大型货车','lt_6':'小型汽车','lt_7':'小型自动挡汽车','lt_8':'低速载货汽车',
        'lt_9':'三轮汽车','lt_10':'普通三轮摩托车','lt_11':'普通二轮摩托车','lt_12':'轻便摩托车',
        'lt_13':'其他'
    }
    return license_types['lt_'+str(val)]

def province(val):
    provinces = {
        'p_0':'全国','p_1':'北京','p_2':'天津','p_3':'上海','p_4':'重庆',
        'p_5':'河北','p_6':'山西','p_7':'辽宁','p_8':'吉林','p_9':'黑龙江',
        'p_10':'江苏','p_11':'浙江','p_12':'安徽','p_13':'福建','p_14':'江西',
        'p_15':'山东','p_16':'河南','p_17':'湖北','p_18':'湖南','p_19':'广东',
        'p_20':'海南','p_21':'四川','p_22':'贵州','p_23':'云南','p_24':'陕西',
        'p_25':'甘肃','p_26':'青海','p_27':'台湾','p_28':'西藏','p_29':'广西',
        'p_30':'内蒙古','p_31':'宁夏','p_32':'新疆','p_33':'香港','p_34':'澳门'
    }
    return provinces['p_'+str(val)]