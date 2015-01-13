# coding=utf-8
__author__ = 'guguohai@outlook.com'

common = [
    {
        'displayName': u'连接测试',
        'url': 'service/commonService/activeTest',
        'desc': '调用成功后，服务端将发送验证码短信，并根据手机号判断客户是否存在。如果客户已存在，将更新客户验证码信息，否则新增客户，并保存验证码。最小调用时间间隔见系统参数4.1.1。',
        'parameter':
            [
                {'name': 'phone', 'type': 'String', 'required': 'true', 'desc': '手机号。'}
            ]
    },
    {
        'displayName': u'获取资源文件',
        'url': 'service/commonService/getResourse',
        'desc': '登录客户，成功时返回个人信息、令牌号、未完成的订单列表。',
        'parameter':
            [
                {'name': 'phone', 'type': 'String', 'required': 'true', 'desc': '手机号。'},
                {'name': 'code', 'type': 'String', 'required': 'true', 'desc': '验证码，需MD5加密。'},
                {'name': 'versionNo', 'type': 'String', 'required': 'true', 'desc': 'APP版本号。'}
            ]
    }
]

customer = [
    {
        'displayName': u'获取验证码短信',
        'url': '/service/customerService/verifySms',
        'desc': '调用成功后，服务端将发送验证码短信，并根据手机号判断客户是否存在。如果客户已存在，将更新客户验证码信息，否则新增客户，并保存验证码。最小调用时间间隔见系统参数4.1.1。',
        'parameter':
            [
                {'name': 'phone', 'type': 'String', 'required': 'true', 'desc': '手机号。'}
            ]
    },
    {
        'displayName': u'客户登录',
        'url': 'service/customerService/login',
        'desc': '登录客户，成功时返回个人信息、令牌号、未完成的订单列表。',
        'parameter':
            [
                {'name': 'phone', 'type': 'String', 'required': 'true', 'desc': '手机号。'},
                {'name': 'code', 'type': 'String', 'required': 'true', 'desc': '验证码，需MD5加密。'},
                {'name': 'versionNo', 'type': 'String', 'required': 'true', 'desc': 'APP版本号。'}
            ]
    }
]

driver = [
    {
        'displayName': u'司机登录',
        'url': '/service/customerService/verifySms',
        'desc': '调用成功后，服务端将发送验证码短信，并根据手机号判断客户是否存在。如果客户已存在，将更新客户验证码信息，否则新增客户，并保存验证码。最小调用时间间隔见系统参数4.1.1。',
        'parameter':
            [
                {'name': 'phone', 'type': 'String', 'required': 'true', 'desc': '手机号。'}
            ]
    },
    {
        'displayName': u'司机登出',
        'url': 'service/customerService/login',
        'desc': '登录客户，成功时返回个人信息、令牌号、未完成的订单列表。',
        'parameter':
            [
                {'name': 'phone', 'type': 'String', 'required': 'true', 'desc': '手机号。'},
                {'name': 'code', 'type': 'String', 'required': 'true', 'desc': '验证码，需MD5加密。'},
                {'name': 'versionNo', 'type': 'String', 'required': 'true', 'desc': 'APP版本号。'}
            ]
    }
]

inf = [
    {'name': u'公共接口', 'api': common},
    {'name': u'用户端接口', 'api': customer},
    {'name': u'司机端接口', 'api': driver}
]