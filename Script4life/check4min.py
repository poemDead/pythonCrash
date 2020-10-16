'''
简单的生成每天的打卡信息的脚本
'''
import datetime
import locale
import pyperclip

# 获取系统时间并本地化为日语
today = datetime.datetime.today()
locale.setlocale(locale.LC_TIME,'ja_JP.UTF-8')

# 分别存入变量
year = today.year
month = today.month
day = today.day
weekday = today.strftime('%a')

# 生成标题和打卡内容
title = f"{year}{month}{day}_閻敏_在宅勤務"
message = f"作業開始いたしました。\n{month}月{day}日（{weekday}）9:00-17:30予定\n"
message += f"\n「本日の作業予定」\n・SMJBtoB単体テストの実施\n\n12:00-13:00　昼休憩予定\n\n以上"

# 分两次录入剪切板
pyperclip.copy(title)
print('现在可以去复制标题了')
todo = input('（复制完成后，回车即可复制打卡信息）')
pyperclip.copy(message)
print('-------end---------')