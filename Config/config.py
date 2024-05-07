from SmartApi import LoginApi


def setUserInfo():
    userAccount = '5229455'
    userPassword = 'Admin@123'
    return userAccount,userPassword

def setuip():
    uip = '192.168.1.253'
    return uip

def getuserinfo():
    userAccount = (setUserInfo())[0]
    userPassword = (setUserInfo())[1]
    res=LoginApi.login(userAccount,userPassword)
    headers=res[1]
    return headers

def getdepartId():
    userAccount = (setUserInfo())[0]
    userPassword = (setUserInfo())[1]
    res = LoginApi.login(userAccount, userPassword)
    departId = res[2]
    print(departId)
    return departId

if __name__ == '__main__':
    getdepartId()