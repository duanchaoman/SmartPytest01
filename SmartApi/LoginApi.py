import base64
import json

import requests
from Config import config
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5 as Cipher_pksc1_v1_5



def login(userAccount,password):
    input_userAccount = userAccount
    publicKey_url = "http://" + config.setuip() + '/smartSecurityAPI/userLogin/getPublicKey?userAccount=' + str(input_userAccount)
    res = requests.get(url=publicKey_url).json()
    public = res.get('result')
    publicKey = '-----BEGIN PUBLIC KEY-----\n' + public + '\n-----END PUBLIC KEY-----'
    rsakey = RSA.importKey(publicKey)
    cipher = Cipher_pksc1_v1_5.new(rsakey)
    cipher_text = base64.b64encode(cipher.encrypt(password.encode()))
    password=cipher_text.decode()
    payload = json.dumps({
        "userAccount": userAccount,
        "password": password
    })
    login_headers={'Content-Type': 'application/json'}
    login_url = "http://" + config.setuip() +'/smartSecurityAPI/userLogin/login'
    res=requests.post(url=login_url, headers=login_headers, data=payload).json()
    token=res.get('result').get('token')
    guestCode=res.get('result').get('user').get('guestCode')
    departId = res.get('result').get('person').get('departId')
    headers = {'Content-Type': 'application/json','token':token,'guestCode':guestCode}
    return res,headers,departId


if __name__ == '__main__':
    login('5229455','Admin@123')