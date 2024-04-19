from Config import config
import requests

# 外来车辆
def foreigncar():
    url = 'http://'+config.setuip()+'/smartSecurityAPI/carInout?carNo=&beginDate=&endDate=&isOut=&currentPage=1&pageSize=10'
    headres = config.getuserinfo()
    res = requests.get(url=url,headers=headres,params=None).json()
    return res

1231231
