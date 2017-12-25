import re  
import urllib  
from urllib import request  
import requests
from bs4 import BeautifulSoup
from pprint import pprint  
url = 'https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.8955'  
req = urllib.request.Request(url)  
r = urllib.request.urlopen(req).read().decode('utf-8')  
#print (r)  
stations =re.findall(r'([\u4e00-\u9fa5]+)\|([A-Z]+)',r) #匹配中文和对应的英文  
stations = dict(stations)  
stations = dict(zip( stations.keys(),stations.values()))#将匹配的内容转化为字典  
pprint(stations)                                        #以列的形式打印出来  