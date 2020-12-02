'''
2. 完成model定义后， 在app下创建一个service.py文件
   在此文件中写一个获取 用户交易表 中 指定时间段内 交易总额 最大 的 前三名 用户的 id，以及 交易总额是多少
   函数名根据描述自行创建，参数为指定时间段的起止时间，优先使用orm完成查询以及聚合，聚合可以查询官方文档，如果orm不能完成，可以书写一下SQL语句查询
'''

import MySQLdb
from django.http import HttpResponse

from payment.models import Trade

conn = MySQLdb.connect(
    host='localhost',    # mysql所在主机的ip
    port=3306, 		    # mysql的端口号
    user="root",         # mysql 用户名
    password="123456",   # mysql 的密码
    db="trade",          # 要使用的库名
    charset="utf8"      # 连接中使用的字符集
)
cursor = conn.cursor()


#   sql语句查询
def get_max(start_date, end_date):
    #   查询交易总额 最大 的 前三名 用户的 id，以及 交易总额是多少
    sql = 'select user_id, trade_amount from trade_db where trade_date between %s and %s order by trade_amount desc'
    cursor.execute(sql, [start_date, end_date])
    trades = cursor.fetchall()
    return f'交易总额最大的前三名的id是{trades[0].user_id}、{trades[1].user_id}、{trades[2].user_id}，' \
           f'他们各自的交易总额是{trades[0].trade_amount}、{trades[1].trade_amount}、{trades[2].trade_amount}'


#   运用orm机制查询
def get_trade_info(request):
    '''

    :param request:
    start_date: 开始时间
    end_date: 结束时间
    '''
    start_date = request.Get.get('start_date')
    end_date = request.Get.get('end_date')
    trades = Trade.objects.filter(trade_date__range=(start_date, end_date)).order_by('-trade_amount')
    #   交易前三名的用户
    user_id1 = trades[0].user_id
    trade_amount1 = trades[0].trade_amount
    user_id2 = trades[1].user_id
    trade_amount2 = trades[1].trade_amount
    user_id3 = trades[2].user_id
    trade_amount3 = trades[2].trade_amount
    return HttpResponse(f'交易额最大的前三名的用户id是{user_id1}、{user_id2}、{user_id3},交易额是{trade_amount1}、{trade_amount2}、{trade_amount3}')
