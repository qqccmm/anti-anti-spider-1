# coding=utf-8

"""
    重点违章

    update:
        2019-05-13: 进入四川官网，发现出现带计算的验证码
        分析js发现，请求里有token字段，仅仅是没有启用而已
        cookie 里的 tmri_csfr_token 也是由主页写入的
        然后发现 accessToken是由主页颁发
        !! 以上仍然不行
        这下录入 checkType试试
        !! 成功
        牛皮， checkType 竟然是写死的

        2019-05-14:
            测试重庆官网，可行
            北京官网，可行
            天津官网，可行
            河北官网，可行
            山西官网，可行
            内蒙官网，可行
            辽宁官网，可行
            吉林官网，可行
            黑龙江官网，可行
            上海官网，可行
            江苏官网，可行
            浙江官网，可行
            江西官网，可行
            福建官网，可行
            ** 山东官网，不可行
            河南官网，可行
            湖北官网，可行
            湖南官网，可行
            广东官网，可行
            广西官网，可行
            海南官网，可行
            贵州官网，可行
            云南官网，可行
            ** 西藏官网，不可行
            陕西官网，可行
            甘肃官网，可行
            ** 青海官网，不可行
            宁夏官网，可行
            新疆官网，可行
"""