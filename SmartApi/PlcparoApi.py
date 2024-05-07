import requests
from Config import config
import json
from datetime import datetime

# 新增巡更路线
def addPlcparo():
    url = 'http://'+config.setuip()+'/smartSecurityAPI/patrol/path/save'
    headers = config.getuserinfo()
    pathNode = "[{\"id\":\"xgpoint3748\",\"type\":0,\"currentTreeId\":\"000\",\"url\":\"\",\"positionCode\":\"5223010030090300270020000000001000000000\",\"videoArr\":[],\"position\":{\"longitude\":104.91964972549191,\"latitude\":25.136245142355815,\"altitude\":65.6849678889957}},{\"id\":\"xgpoint0468\",\"type\":0,\"currentTreeId\":\"000\",\"url\":\"\",\"positionCode\":\"5223010030090300270020000000001000000000\",\"videoArr\":[],\"position\":{\"longitude\":104.919499419485,\"latitude\":25.136890583330715,\"altitude\":65.66221604181243}},{\"id\":\"xgpoint8076\",\"type\":0,\"currentTreeId\":\"000\",\"url\":\"\",\"positionCode\":\"5223010030090300270020000000001000000000\",\"videoArr\":[],\"position\":{\"longitude\":104.92004081159351,\"latitude\":25.13702465293982,\"altitude\":65.6669518570738}}]"
    data = json.dumps({
            "pathName": "日常巡更路线",
            "pathNode": pathNode
            })
    res = requests.post(url=url,headers=headers,data=data).json()
    return res

# 新增巡更任务
def addPlcdata():
    user_headers = config.getuserinfo()
    get_listurl = 'http://'+config.setuip()+'/smartSecurityAPI/patrol/path/list'
    get_listres = requests.get(url=get_listurl,headers=user_headers,params=None).json()
    result = get_listres.get('result')
    path = result[0]
    pathId = path.get('pathId')
    url = 'http://'+config.setuip()+'/smartSecurityAPI/patrol/task/save'
    data = json.dumps({
        "pathId": pathId,
        "taskName": "日常巡更任务",
        "departId": config.getdepartId(),
        "taskType": "0",
        "taskTimes": 1,
        "taskTime": 5
    })
    res = requests.post(url=url,headers=user_headers,data=data).json()
    return res

# 执行巡更任务
def plcimp():
    getlist_url = 'http://'+config.setuip()+'/smartSecurityAPI/patrol/task/getTodayPatrolTaskDetails?taskType=0'
    headers = config.getuserinfo()
    getlist_res = requests.get(url=getlist_url,headers=headers,params=None).json()
    result = getlist_res.get('result')
    result_0 = result[0]
    taskId = result_0.get('taskId')
    taskStartTime = datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S')
    taskEndTime = datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S')
    url = 'http://' + config.setuip() + '/smartSecurityAPI/patrol/rec/save'
    data = json.dumps({
        "recResult": 1,
        "recRemark": "",
        "taskId": taskId,
        "taskStartTime": taskStartTime,
        "taskEndTime": taskEndTime
    })
    res = requests.post(url=url, headers=headers, data=data).json()
    return res

# 添加定时巡更任务
def addtask():
    patrol_url = 'http://'+config.setuip()+'/smartSecurityAPI/patrol/path/list'
    headers = config.getuserinfo()
    patrol_res = requests.get(url=patrol_url, headers=headers, params=None).json()
    get_pathId = ((patrol_res.get('result'))[0]).get('pathId')
    task_url = 'http://' + config.setuip() + '/smartSecurityAPI/patrol/task/save'
    task_data = json.dumps(
        {
            "pathId": get_pathId,
            "taskName": "定时",
            "departId": config.getdepartId(),
            "taskType": "1",
            "taskTimes": 1,
            "taskTime": 5,
            "taskRange": "[{\"arr\":[\"00:00-23:59\"]},{\"arr\":[\"00:00-23:59\"]},{\"arr\":[\"00:00-23:59\"]},{\"arr\":[\"00:00-23:59\"]},{\"arr\":[\"00:00-23:59\"]},{\"arr\":[\"00:00-23:59\"]},{\"arr\":[\"00:00-23:59\"]}]"
        }
    )
    task_res = requests.post(url=task_url, headers=headers, data=task_data).json()
    return task_res

# 执行定时巡更任务
def dotimetask():
    TaskDetails_url = 'http://' + config.setuip() + '/smartSecurityAPI/patrol/task/getTodayPatrolTaskDetails?taskType=1'
    headers = config.getuserinfo()
    TaskDetails_res = requests.get(url=TaskDetails_url, headers=headers, params=None).json()
    taskID = ((TaskDetails_res.get('result'))[0]).get('taskId')
    url = 'http://' + config.setuip() + '/smartSecurityAPI/patrol/rec/save'
    this_startime = datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S')
    this_endtime = datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S')
    data = json.dumps(
        {
            "recResult": 1,
            "recRemark": "",
            "taskId": taskID,
            "taskStartTime": this_startime,
            "taskEndTime": this_endtime
        }
    )
    res = requests.post(url=url, headers=headers, data=data).json()
    return res

# 巡更日志
def plclog():
    taskStartTime = datetime.strftime(datetime.now(), '%Y-%m-%d')
    taskEndTime = datetime.strftime(datetime.now(), '%Y-%m-%d')
    url = 'http://'+config.setuip()+'/smartSecurityAPI/patrol/rec/list?taskStartTime='+taskStartTime+'+00:00:00&taskEndTime='+taskEndTime+'+23:59:59'
    headers = config.getuserinfo()
    res = requests.get(url=url,headers=headers,params=None).json()
    return res

# 统计分析
def plcstaana():
    beginDat = datetime.strftime(datetime.now(), '%Y-%m-%d')
    endDate = datetime.strftime(datetime.now(), '%Y-%m-%d')
    url = 'http://'+config.setuip()+'/smartSecurityAPI/patrol/path/pathStatistics?beginDate='+beginDat+'+00:00:00&endDate='+endDate+'+23:59:59'
    headers = config.getuserinfo()
    res = requests.get(url=url, headers=headers, params=None).json()
    return res

if __name__ == '__main__':
    print(plcstaana())