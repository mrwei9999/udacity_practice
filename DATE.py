from datetime import datetime
a = input("輸入日期1:(ex:2000/01/01))")
b = input("輸入日期2:(ex:2000/01/01))")
x = datetime.strptime(a, '%Y/%m/%d')
y = datetime.strptime(b, '%Y/%m/%d')
z = x-y
print(abs(z.days),'天')
