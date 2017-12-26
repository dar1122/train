
import select
from pprint import pprint

if __name__ == '__main__':

    from_station = input("请输入始发站：")
    to_station = input("请输入终点站：")
    go_date = input("请输入出发日期，格式为YYYY-MM-DD：")
    info = select.se(from_station,to_station,go_date)


    infos = "车次    出发站     目的地    出发时间    到达时间    消耗时间  座位情况：一等座   二等座   软卧   硬卧   硬座   无座\n"

    d = open('info.txt', 'w+', encoding='utf-8')
    d.writelines(infos)
    d.writelines(info)
    d.close()

    c = open('info.txt','r',encoding='utf-8')
    dar = c.readlines()
    for x in dar:
        print(x)
