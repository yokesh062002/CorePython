from pickle import *
name=open("varun.txt","rb")
while True:
    try:
        studentdata=load(name)
        print(studentdata)
    except EOFError as e:
        break