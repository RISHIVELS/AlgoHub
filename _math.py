def armstrong(n:int):
    am = 0
    quo =n
    while(quo>0):
        rem = quo%10
        am+=rem**3
        quo//=10
    if n ==am: 
        print(True)
    else:
        print(False)


def divisors(n):
    for i in range(1,n+1):
        if n%i==0:
            print(i)

import math 

def math_div(n):
    _list = []
    for i in range(1,int(math.sqrt(n)+1)):
        if n%i==0:
            _list.append(n)
        if n/i!=i:
            _list.append(n/i)
    _list.sort()
    for num in _list:
        print(int(num))
        
def check_for_prime(num):
    counter =0
    for i in range(1,int(math.sqrt(num)+1)):
        if num%i==0:
            counter+=1
            if num/i!=i:
                counter+=1
    if counter==2:
        print(True)
    else:
        print(False)
        

def find_gcd(num1,num2):
    while num1>1 and num2>1:
        if num1>num2:
            num1 = num1%num2
        else:
            num2 = num2%num1
    if num1==0 : return num2
    else: return num1

num1 = int(input())
num2 = int(input())
print(find_gcd(num1,num2))

