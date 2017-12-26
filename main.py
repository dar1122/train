
import select
from pprint import pprint

if __name__ == '__main__':
    from_station = input("请输入始发站：")
    to_station = input("请输入终点站：")
    go_date = input("请输入出发日期，格式为YYYY-MM-DD：")
    info = select.se(from_station,to_station,go_date)

    d = open('info.txt', 'w+', encoding='utf-8')
    d.writelines(info)
    d.close()

    c = open('info.txt','r',encoding='utf-8')
    dar = c.readlines()
    for x in dar:
        print(x)
