"""""
name: Jialin Liu
id: 991318879
"""

import csv
import re

with open('input.csv','r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')

    pre_line = ""

    for row in reader:
        id = row[0]
        string = row[1]

        if (id == 'student'and (re.match(r'^\d{9}$',string))):
            pre_line = string
            print("yes")
        elif (id == 'password' and (re.match(r'^(?=.*[a-zA-z\d].*)[a-zA-Z\d!@#$%&*]{12,}$',string))):
            pre_line = string
            print("yes")
        elif(id == 'username' and (re.match(r'^.{3,20}$',string))):
            pre_line = string
            print("yes")
        elif(id == 'email' and (re.match(r'^\w+@[a-zA-Z_]+?\.[a-zA-Z]{3,20}$',string))):
            pre_line = string
            print("yes")
        elif (id == 'previous' and (re.match(pre_line,string))):
            print("yes")
        elif(id == 'phone' and (re.match(r'^[(]?[0-9]{3}[)]?[ ,-]?[0-9]{3}[ ,-]?[0-9]{4}$',string))):
            pre_line = string
            print("yes")
        elif(id == 'postal' and (re.match(r'^(?!.*[DFIOQU])[A-VXY][0-9][A-Z] ?[0-9][A-Z][0-9]$',string))):
            pre_line = string
            print("yes")
        elif(id == 'address' and (re.match(r'^\d{1,3}.?\d{0,3}\s[a-zA-Z]{2,30}\s[a-zA-Z]{2,15}.',string))):
            pre_line = string
            print("yes")
        elif(id == 'binary' and (re.match(r'[0-1]+',string))):
            pre_line = string
            print("yes")
        elif(id == 'bio' and (re.match(r'(?![a-zA-Z0-9]*<[a-z0-9]+[^>]*>(.+?)<\/[a-z0-9]+>)', string))):
            pre_line = string
            print("yes")
        else:
            pre_line = string
            print("no")