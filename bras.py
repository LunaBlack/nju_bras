#!/usr/bin/env python
# -*- coding: UTF-8 -*-


import subprocess
import shlex
import time

try:
    print "import"
    import requests
    print "import end"
except ImportError:
    print "err"
    

# Fill in your account information inside the quotos
info1 = dict(username = '*******', password = '*******')
login_url = "http://p.nju.edu.cn/portal_io/login"
info = dict(action="login")
info.update(info1)


def login():
    
    try:
        response = requests.post(login_url, data=info)
        reply_code = response.json().get("reply_code")
        if reply_code == 1 or reply_code == 6:
            print "Hello, %s! Your login was successful!" % info.get("username")
        return reply_code
    
    except:
        return 000 # fail flag


def ping():
    flag = 0 # 初始化，0表示网络不畅通
    
    command_line1 = "ping www.baidu.com"
    command_line2 = "ping www.bilibili.com"
    command_line3 = "ping www.zhihu.com"
    args1 = shlex.split(command_line1)
    args2 = shlex.split(command_line2)
    args3 = shlex.split(command_line3)
    
    try:
        subprocess.check_call(args1, stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        print "Website baidu is there."
        flag = 1 # 网络通畅
        return flag
    
    except subprocess.CalledProcessError:
        try:
            subprocess.check_call(args2, stdout=subprocess.PIPE,stderr=subprocess.PIPE)
            print "Website bilibili is there."
            flag = 1 # 网络通畅
            return flag
        
        except subprocess.CalledProcessError:
            try:
                subprocess.check_call(args3, stdout=subprocess.PIPE,stderr=subprocess.PIPE)
                print "Website zhihu is there."
                flag = 1 # 网络通畅
                return flag

            except subprocess.CalledProcessError:
                print "Couldn't get a ping."
                return flag

            except:
                return flag

        except:
            return flag

    except:
        return flag


if __name__ == '__main__':
    
    print "start"

    while(1):
        try:
            ping_result = ping()
            if ping_result == 1: # 网络畅通
                print "Web unobstructed."
                pass
            
            else: # 网络不畅通
                print "Web obstructed."
                for i in range(3): 
                    login_reply_code = login()
                    if login_reply_code == 1 or login_reply_code == 6:
                        print "login successfully."
                        break
                    else:
                        if i < 2:
                            pass
                        else:
                            print "login unsuccessfully."

            print "sleep now"
            time.sleep(3600) # 一小时一次

        except:
            pass
                            

