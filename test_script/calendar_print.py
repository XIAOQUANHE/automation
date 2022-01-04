import calendar as c
'''
AttributeError: module 'calendar' has no attribute 'TextCalendar'
原因：文件名和模块名一致了，需要更改文件名
'''
def ask():
    try:
        year = int(input("请输入合法的年份：\n"))
    except Exception:
        while True:
            try:
                year = int('请输入合法的年份: \n')
            except Exception:
                continue
            else:
                break
    try:
        month = int(input("请输入合法的月份：\n"))
    except Exception:
        while True:
            try:
                month = int(input("请输入合法的月份：\n"))
            except Exception:
                continue
            else:
                break

    while not 0 < month < 13:
        month = int(input("请输入合法的月份：\n"))
    return year, month
def show(year, month):
    print("-----------{} 年 {} 月的日历--------".format(str(year),str(month)))
    print(c.TextCalendar().formatmonth(year,month,w=0, l=0))

def main():
    print("--------查询日历小程序--------")
    y,m = ask()
    show(y,m)

if __name__ == '__main__':
    main()