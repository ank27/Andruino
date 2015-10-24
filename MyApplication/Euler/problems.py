__author__ = 'ankurkhandelwal'


def question1():
    x=[]
    y=0
    for i in range(1,1000):
        if i%3==0 or i%5==0:
            x.append(i)
            y+=i
    print(y)


def question2():
    result= []
    a,b=1,1
    sum=0
    while b < 4000000:
        result.append(b)
        a,b = b,a+b
    for counter, result_value in enumerate(result):
        if(result_value%2==0):
            sum+=result_value
    print sum


def question3():
    aray=[]
    n=8462696833
    for i in range(2, n):
        if(n%i==0):
            aray.append(i)
            n=n/i
    print aray[-1]


def question4():
    maxValue=0
    for i in range(999,100,-1):
        for j in range(i,100,-1):
            x=i*j
            if(str(x)[::-1]==str(x)):
               if(int(x)>int(maxValue)):
                   maxValue=x
    print(maxValue)


def find_gcd(a, b):
    while b>0:
        a%=b
        if(a==0):
            return b
        b%=a
    return a


def find_lcm(a,b):
    x=find_gcd(a,b)
    lcm=(a*b)/x
    return lcm


def is_prime(n):
    x=int(n**(0.5))
    if(n%2==0 and n>2):
        return False
    for i in range(3,x+1,2):
        if n%i==0:
            return False
    return True


def question5():
    lcm=1
    for i in range(2,20):
        lcm=find_lcm(lcm,i)
    print(lcm)


def question6(n):
    sum_of_squares=(n*(n+1)*((2*n)+1))/6
    sum_of_numbers= ((n*(n+1))/2)**2
    difference=sum_of_numbers-sum_of_squares
    print(difference)


def question7():
    index=0
    while index<100001:
        if(is_prime(index)):
            index+=1

def range_values():
    values=[]
    for r in range(1,10):
        values.append((r*(3*r-1))/2)
        values.append((r*(3*r+1))/2)
    return values


def alpha(n):
    values=[]
    flag=0
    for r in range(1,11):
        values.append((r*(3*r-1))/2)
        values.append((r*(3*r+1))/2)
    if n==0:
        return 1

    for index, i in enumerate(values):
        if i==n:
            flag=1
            return (-1)**index

    if(flag==0):
        return 0

def integer_partition(n):
    if n > 0:
        sum_ip = 0
        for k in range(1, n+1):
            sum_ip = sum_ip + ((-1)**(k+1))*(integer_partition(n - k*(3*k-1)/2) + integer_partition(n - k*(3*k+1)/2))
        return sum_ip
    elif n < 0:
        return 0
    if n == 0:
        return 1


def question78():
    for i in range(10,1000):
        x=integer_partition(i)
        if(x>1000000):
            if(x%1000000):
                print(x)


# question78()
print(integer_partition(100))