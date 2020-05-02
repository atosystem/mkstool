import requests
import json
import time
import urllib
import uuid
import os
import random
import getpass
import sys

from tabulate import tabulate

class MksTool_API():
    
    def __init__(self):
        self.BASE_URL = 'http://140.112.174.221:8080'
        self.login_data = {'user' : '', 'pass' : ''}
        self.IsLoginIn = False
        USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'

        self.session = requests.Session()
        self.session.headers = {'user-agent' : USER_AGENT}
    
    def login(self,username,password):

        # BASE_URL = 'http://140.112.174.221:8080'
        API_AUTH = '/api/checkauth'
        # LOGIN_URL = 'https://web2.cc.ntu.edu.tw/p/s/login2/p1.php'
        
        # req = session.get(FIRST_URL)

        self.login_data = {'user' : username, 'pass' : password}

        req_login = self.session.post(self.BASE_URL+API_AUTH,data=self.login_data,allow_redirects = True)
        ret = json.loads(req_login.text)
        # print(ret)
        if(ret['login']):
            self.IsLoginIn = True
            print(ret['message'])
            self.login_data['user'] = ret['student_id']
            return True
        else:
            print(ret['message'])
            return False
        # print(req_login.text)

        # if(req_login.text.find("Authentication Fail!") == -1):
        #     a = req_login.text.find('src="imgs/userlogin.png"')
        #     a = req_login.text.find('>',a)
        #     b = req_login.text.find('<',a)
        #     str1 = req_login.text[a+1:b]
        #     self.user=str1.split()[0]
        #     self.title = str1.split()[1]
        #     self.userID = username
        #     return True
        #     #print(str1.split()[0])
        # else :
        #     #print ("Wrong Username or Password")
        #     return False

    def ssh_profile_view(self):
        if(not self.IsLoginIn):
            print("not login yet")
            return
        API_AUTH = '/api/ssh/profile'
        req = self.session.post(self.BASE_URL+API_AUTH,allow_redirects = True)
        # print(req.text)
        return json.loads(req.text)

    def ssh_create(self):
        print("Create ssh account")
        
        print("Creating...")
        API_AUTH = '/api/ssh/add'

        req = self.session.post(self.BASE_URL+API_AUTH,data={'pass' : self.login_data['user']},allow_redirects = True)
        req = json.loads(req.text)
        if(req['status']=="success"):
            print(req['message'])
            # print("Account created")
            # print("Username:",self.login_data['user'])
            # print("Password:(default same with username)")
            # print("login: $ssh " + self.login_data['user'] + "@140.112.174.221")
        else:
            print("Fail")
            print(req['message'])
        return

    def ssh_rst_pass(self):
        print("Create ssh account")
        
        print("Reseting...")
        API_AUTH = '/api/ssh/reset_password'

        req = self.session.post(self.BASE_URL+API_AUTH,data={'pass' : self.login_data['user']},allow_redirects = True)
        req = json.loads(req.text)
        if(req['status']=="success"):
            print(req['message'])
            # print("Account created")
            # print("Username:",self.login_data['user'])
            # print("Password:(default same with username)")
            # print("login: $ssh " + self.login_data['user'] + "@140.112.174.221")
        else:
            print("Fail")
            print(req['message'])
        return

    def ssh_users_list(self):
        API_AUTH = '/api/ssh/users'
        req = self.session.post(self.BASE_URL+API_AUTH,allow_redirects = True)
        req = json.loads(req.text)
        if(req['status']=="success"):
            print(tabulate(req['data'], headers=['id', 'student_id','role','ssh','name','created']))
            # for u in req['data']:
            #     print(u)
            # print(req['data'])
            # print("Account created")
            # print("Username:",self.login_data['user'])
            # print("Password:(default same with username)")
            # print("login: $ssh " + self.login_data['user'] + "@140.112.174.221")
        else:
            print("Fail")
            print(req['message'])

    def ssh_users_change_role(self,r_id,n_role):
        API_AUTH = '/api/ssh/change_role'

        req = self.session.post(self.BASE_URL+API_AUTH,data={'new_role' : n_role,'row_id':r_id},allow_redirects = True)
        req = json.loads(req.text)

        if(req['status']=="success"):
            print(req['message'])
            # for u in req['data']:
            #     print(u)
            # print(req['data'])
            # print("Account created")
            # print("Username:",self.login_data['user'])
            # print("Password:(default same with username)")
            # print("login: $ssh " + self.login_data['user'] + "@140.112.174.221")
        else:
            print("Fail")
            print(req['message'])

# u=input('Username: ')
# p=getpass.getpass('Password: ')

# n = mkstool_api()
# result = n.login(u,p)
# n.ssh_profile_view()
# exit()
# # print()
# if(result):
#     print('登入成功')
#     print(n.user + n.userID)
# else:
#     print('登入錯誤')

