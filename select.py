#coding=utf-8
import requests
import stations
import json


def se():
    allstations = stations.a

    allstations_1 = {v:k for k,v in allstations.items()}

    start = '北京'
    from_station = allstations.get(start)

    end = '上海'
    to_station = allstations.get(end)

    search_date = '2017-12-26'
    date = search_date


    url = "https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date={}&leftTicketDTO.from_station={}&leftTicketDTO.to_station={}&purpose_codes=ADULT".format(date,from_station,to_station)

    lists = []

    r = requests.get(url, verify=False)


    trains = r.json()['data']['result']

    for raw_train in trains:
        # 循环遍历每辆列车的信息
        data_list = raw_train.split('|')

        # 车次号码
        train_no = data_list[3]
        # 出发站
        from_station_code = data_list[6]
        from_station_name = allstations_1.get(from_station_code)

        # 终点站
        to_station_code = data_list[7]
        to_station_name = allstations_1.get(to_station_code)

        # 出发时间
        start_time = data_list[8]

        # 到达时间
        arrive_time = data_list[9]
        # 总耗时
        time_fucked_up = data_list[10]
        # 一等座
        first_class_seat = data_list[31] or '--'
        # 二等座
        second_class_seat = data_list[30] or '--'
        # 软卧
        soft_sleep = data_list[23] or '--'
        # 硬卧
        hard_sleep = data_list[28] or '--'
        # 硬座
        hard_seat = data_list[29] or '--'
        # 无座
        no_seat = data_list[26] or '--'

        list = ('车次:{}\n出发站:{}\n目的地:{}\n出发时间:{}\n到达时间:{}\n消耗时间:{}\n座位情况：\n 一等座：「{}」 \n二等座：「{}」\n软卧：「{}」\n硬卧：「{}」\n硬座：「{}」\n无座：「{}」\n\n'.format(train_no, from_station_name, to_station_name, start_time, arrive_time, time_fucked_up, first_class_seat,second_class_seat, soft_sleep, hard_sleep, hard_seat, no_seat))
        lists.append(list)
    return lists
a = se()

print(a)