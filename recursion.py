# Recursion 

def recursion (i,n):
    if i>n:
        return 
    recursion(i+1,n)
    print(i)


def sum_n_numbers(n):
    if n==0:
        return 0
    return n+sum_n_numbers(n-1)

def factorial (n):
    if n==1 or n==0:
        return 1
    return n*factorial(n-1)
    
def reverse_two_pointer():
    _list = [1,2,3,4,5]
    left = 0
    right  = len(_list)-1
    for i in range(len(_list)):
        if(left>=right):
            break
        temp = _list[left]
        _list[left] = _list[right]
        _list[right] = temp
        left+=1
        right-=1
    print(_list)
    
def swap(arr,l,r):
    temp = arr[l]
    arr[l] = arr[r]
    arr[r] = temp

_list = [1,2,3,4,5]
def reverse_array(i,n):
    if i>=n//2:
        return 
    swap(_list,i,n-1)
    reverse_array(i+1,n-i-1)

def palindrome(i,string):
    if i>=len(string)/2:
        return True
    if string[i]!= string[len(string)-i-1]:
        return False
    else:
        return palindrome(i+1,string)

def fibo(n):
    if n==0 or n==1:
        return n
    last = fibo(n-2)
    first = fibo(n-1)
    return last+first  # 2^n exponential calls

def reverse_string(i,string):
    if i==len(string):
        return ''
    return reverse_string(i+1,string)+ string[i]

a = input()
print(reverse_string(0,a))
