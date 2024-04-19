from Config import config
import requests

# 外来车辆
def foreigncar():
    url = 'http://'+config.setuip()+'/smartSecurityAPI/carInout?carNo=&beginDate=&endDate=&isOut=&currentPage=1&pageSize=10'
    headres = config.getuserinfo()
    res = requests.get(url=url,headers=headres,params=None).json()
    return res

# 外来人员
def foreignpeople():
    url ='http://' +config.setuip()+'/smartSecurityAPI/peopleInout?keyWord=&beginDate=&endDate=&currentPage=1'
    headres = config.getuserinfo()
    res = requests.get(url=url,headers=headres,params=None).json()
    return res

# 罪犯流动
def criminalInOut():
    url = 'http://'+config.setuip()+'/smartSecurityAPI/criminalInOut/getList?pageSize=10&currentPage=1'
    headres = config.getuserinfo()
    res = requests.get(url=url,headers=headres,params=None).json()
    return res

# 外来物资
def materials():
    url = 'http://'+config.setuip()+'/smartSecurityAPI/materials?zrmjName=&beginDate=&endDate=&wzmc=&currentPage=1&pageSize=10'
    headres = config.getuserinfo()
    res = requests.get(url=url,headers=headres,params=None).json()
    return res