import random
import datetime

__author__ = 'ankurkhandelwal'


def fibo(n):
    result= []
    a,b=0,1
    while b<n:
        result.append(b)
        a,b=b,a+b
    return result


def randm(a,b):
    c=random.randint(a,b)
    return c



def save_to_file():
    values=[1,2,4,5,6,7]
    # get a object of file
    today=datetime.date.today()
    file_object=open('workfile.txt','w')
    file_object.write("%s \n" %today)
    for i in values:
        file_object.write("%s," % i)
    file_object.close()

    file_read=open('workfile.txt','r')
    f=file_read.readline(1)
    single_value=[]
    for value in f:
        single_value.append(value.split(',',1)[0])
        single_value=filter(None,single_value)
        print(single_value)
    max_value=max(single_value)
    print(max_value)

# save_to_file()

print fibo(1500)