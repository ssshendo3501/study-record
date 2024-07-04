import openpyxl as xl
# ブックを作りシートを得る
book = xl.Workbook()
sheet = book.active

# A1,B1,C1,D1に同じ日時の値を指定 --- (*1)
import datetime
dt = datetime.datetime(
      year=2023, month=4, day=5,
      hour=11, minute=22, second=33)
sheet.append([dt, dt, dt, dt])

# 日付を「yyyy/mm/dd」で指定する --- (*2)
sheet["A1"].number_format = 'yyyy/mm/dd'

# 日付を「yyyy年mm月dd日」で指定する --- (*3)
sheet["B1"].number_format = 'yyyy年mm月dd日'

# 時間を「hh:mm:ss」で指定する --- (*4)
sheet["C1"].number_format = 'hh:mm:ss'

# 日付と時間を「mm/dd hh:mm:ss」で指定する --- (*5)
sheet["D1"].number_format = 'mm/dd hh:mm:ss'

# 保存
book.save("number_format_datetime.xlsx")



import openpyxl as xl
# ブックを作りシートを得る
book = xl.Workbook()
sheet = book.active

# A1,B1,C1に同じ日時の値を指定 --- (*1)
import datetime
dt = datetime.datetime(
      year=2023, month=4, day=5,
      hour=11, minute=22, second=33)
sheet.append([dt, dt, dt, dt])

sheet["A1"].number_format = '[$-411]yyyy/mm/dd dddd'
sheet["B1"].number_format = '[$-411]ggge年mm月'
sheet["C1"].number_format = '[$-411]gge年mm月'
sheet["D1"].number_format = 'dd/mmm/yyyy'

# 保存
book.save("number_format_datetime2.xlsx")
