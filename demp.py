# patter1 

def patter1(n):
    for i in range(n):
        for j in range(n):
            print('*',end = '')
        print('')

# pattern 2

def patter2(n):
    for i in range(n):
        for j in range(i+1):
            print('*',end='')
        print('')

# pattern 3

def pattern3(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(j,end=' ')
        print('')


# pattern 4

def pattern4(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(i,end=' ')
        print('')
        
# pattern 5

def pattern5(n):
    for i in range(1,n+1):
        for j in range(n-i+1):
            print('*',end =' ')
        print('')
    
# pattern 6

def pattern6(n):
    for i in range(1,n+1):
        for j in range(n-i+1):
            print(j+1,end =' ')
        print('')

    
# pattern 7

def pattern7(n):
    for i in range(1,n+1):
        print(' '*(n-i),end='')
        for j in range((i*2)-1):
            print('*',end='')
        print(' '*(n-i))
        
# pattern 8

def pattern8(n):
    for i in range(n,0,-1):
        print(' '*(n-i),end='')
        for j in range((2*i)-1):
            print('*',end='')
        print(' '*(n-i))

# pattern 9

def pattern9(n):
    for i in range(1,(2*n)):
        stars = i
        if i>=n+1:
            stars = 2*n - i
        for j in range(stars):
            print('*',end=' ')
        print('')
      
# pattern 10

def pattern10(n):
    
    for i in range(1,n+1):
        if i%2==1: start = 1
        else: start = 0
        for j in range(i):
            print(start,end=' ')
            start = 1-start
        print('')

# pattern 11

def pattern11(n): 
    for i in range(1,n+1):
        # number
        for j in range(1,i+1):
            print(j,end='')
        # space
        for j in range(((2*n) - (2*i) )) :
            print(' ',end='')
        # reverse number
        for j in range(i,0,-1):
            print(j,end='')
        print('')


# pattern 12

def pattern12(n): 
    start = 1
    for i in range(n):
        for j in range(i+1):
            print(start,end=' ')
            start+=1
        print('')
            
# pattern 13

def pattern13(n): 
    for i in range(n):
        for j in range(i+1):
            print(chr(65+j),end='')
        print('')

# pattern 14

def pattern14(n): 
    for i in range(n,0,-1):
        for j in range(i):
            print(chr(65+j),end='')
        print('')

# pattern 15

def pattern15(n): 
    for i in range(n):
        for j in range(i+1):
            print(chr(65+i),end=' ')
        print('')

# pattern 16

def pattern16(n): 
    for i in range(1,n+1):
        # for space 
        for j in range(n-i):
            print(' ',end='')
        # for char
        char = 64
        for j in range((2*i) - 1):
            if i>j:
                char+=1
                print(chr(char),end='')
                
            else:
                char-=1
                print(chr(char),end='')
                
        # for space 
        for j in range(n-i):
            print(' ',end='')
        print('')
          
# pattern 17

def pattern17(n): 
    for i in range(1,n+1):
        char = 65+n-i
        for j in range(i):
            print(chr(char+j),end=' ')
        print('')

# pattern 18

def pattern18(n): 
    for i in range(n):
        # stars
        for j in range(n,i,-1):
            print('*',end='')
        # space
        for j in range(2*n-2*(n-i)):
            print(' ',end='')
        #stars
        for j in range(n,i,-1):
            print('*',end='')
            
        print('')
    for i in range(n):
        # stars
        for j in range(i+1):
            print('*',end='')
        # space
        for j in range(2*(n-i)-2):
            print(' ',end='')
        #stars
        for j in range(i+1):
            print('*',end='')
            
        print('')
        

# pattern 19

def pattern19(n): 
    for i in range(2*n):
        stars = i
        if i>((2*n)//2):
            stars = 2*n-i
            space +=2
        else:
            space = 2*(n-i)
        for j in range(stars):
            print('*',end='')
        for j in range(space):
            print(' ',end='')
        for j in range(stars):
            print('*',end='')
        print('')
        

# pattern 20

def pattern20(n): 
    for i in range(n):
        for j in range(n):
            if i==0 or j==0 or j==n-1 or i==n-1:
                print('*',end='')
            else:
                print(' ',end='')
        print('')
        
# pattern 21

def pattern21(n): 
    for i in range(2*n-1):
        for j in range(2*n-1):
            min_dist = min(i,j,2*n-2-i,2*n-2-j)
            print(n-min_dist,end='')
        print('')

def test(n):
    for i in range(2*n):
        # space
        if i>=2*n/2:
            space = i-n+1
            num = num-2
        else:
            space = n-i-1
            num = 2*i+1
        for j in range(space):
            print(' ',end='')
        # star
        char = 0
        for j in range(num):
            
            if j>num//2:
                char-=1
                print(char,end='')
                  
            else:
                char+=1
                print(char,end='')
               
        # space
        for j in range(space):
            print(' ',end='')
        
        print('')

t= int(input())
test(t)
