# coding: UTF-8
import time
import datetime
import calendar
from exercise.common import show_title

# time
show_title('日期和时间的处理')
ticks = time.time()
now=time.localtime(ticks)
print("当前时间戳为:", ticks,time.timezone)
print("当前时间元组：",now,time.tzname)
print("当前时间：",time.asctime(now),'CLock=',time.clock())
print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))

cal = calendar.month(2018, 3)
print("以下输出2016年1月份的日历:")
print(cal);

i = datetime.datetime.now()
print ("当前的日期和时间是 %s" % i)
print ("ISO格式的日期和时间是 %s" % i.isoformat() )
print ("当前的年份是 %s" %i.year)
print ("当前的月份是 %s" %i.month)
print ("当前的日期是  %s" %i.day)
print ("dd/mm/yyyy 格式是  %s/%s/%s" % (i.day, i.month, i.year) )
print ("当前小时是 %s" %i.hour)
print ("当前分钟是 %s" %i.minute)
print ("当前秒是  %s" %i.second)
print ("当前 %s" % i.strftime('%Y-%m-%d %H:%M:%S'))
d=datetime.datetime.strptime('2017-1-1 12:43:23','%Y-%m-%d %H:%M:%S')
print(d.date())