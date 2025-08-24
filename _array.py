nums = list(map(int,input().split()))
# find the largest element in the array
from collections import defaultdict

def find_largest(nums):
    largest = nums[0]
    for num in nums:
        if num > largest:
            largest = num
    print(largest)
    
def second_smallest(nums):
    f_smallest = nums[0]
    s_smallest = float('inf')
    for i in range(1,len(nums)):
        if nums[i]<f_smallest:
            f_smallest,s_smallest = nums[i],f_smallest
        elif nums[i]<s_smallest:
            s_smallest = nums[i]
    print(s_smallest)



def second_largest(nums):
    first_l = nums[0]
    second_l = float('-inf')
    for i in range(1,len(nums)):
        if nums[i]>first_l:
            first_l,second_l = nums[i],first_l
        elif nums[i]!=first_l and nums[i]>second_l:
            second_l = nums[i]
    print(second_l)
        

def is_sorted(nums):
    for i in range(0,len(nums)-1):
        if nums[i]>nums[i+1]:
            return False        
    return True

def remove_duplicates(nums):
    unique_elements = set()
    for num in nums:
        unique_elements.add(num)
    
    index = 0
    for num in unique_elements:
        nums[index] = num
        index+=1
    print(nums,index)



def remove_duplicates_2(nums):
    i = 0
    for j in range(1,len(nums)):
        if nums[j]!=nums[i]:
            nums[i+1]= nums[j]
            i+=1
    print(nums,i)
            

def left_rotate_array_1(nums):
    temp = nums[0]
    for i in range(1,len(nums)):
        nums[i-1] = nums[i]
    nums[i] = temp
    print(nums)
    
def left_rotate_array_d(nums,d):
    if d>len(nums):
        d = d%len(nums)
    temp = []
    for i in range(0,d):
        temp.append(nums[i])
    for j in range(d,len(nums)):
        nums[j-d] = nums[j]
    # replace the temp at last 
    for i in range(len(nums)-d,len(nums)):
        nums[i] = temp[i-(len(nums)-d)]
    print(nums)
    
def reverse(nums,l,r):
    while l<r:
        nums[l],nums[r] = nums[r],nums[l]
        l+=1
        r-=1
    
def left_rotate_array_d_optimal(nums,d):
    if d>=len(nums):
        d = d%len(nums)
    reverse(nums,0,d-1)
    reverse(nums,d,len(nums)-1)
    reverse(nums,0,len(nums)-1)
    print(nums)
    
    
def move_zeros_brute(nums):
    temp = []
    for num in nums:
        if num != 0:
            temp.append(num)
    for i in range(0,len(nums)):
        if i < len(temp):
            nums[i] = temp[i]
        else:
            nums[i] = 0
    
    print(nums)
    

def move_zeros_optimal(nums):
    i = 0
    for j in range(1,len(nums)):
        if nums[i]==0 and nums[j]!=0:
            nums[i],nums[j] = nums[j],nums[i]
            i+=1
        elif nums[i]!=0:
            i+=1
    print(nums)

def linear_search_brute(nums,target):
    for i in range(0,len(nums)):
        if nums[i] == target:
            return i
    return -1

def sorted_union_brute(nums,nums2):
    list1 = []
    for num in nums:
        if num not in list1:
            list1.append(num)
    for num in nums2:
        if num not in list1:
            list1.append(num)
    return sorted(list1)

def sorted_union_optimal(nums,nums2):
    temp = []
    i = 0
    j = 0
    while (i<len(nums) and j<len(nums2)):
        if nums[i]<nums2[j]:
            if not temp or  temp[-1] != nums[i] :
                temp.append(nums[i])
            i+=1
        elif  nums2[j]<nums[i]:
            if not temp or temp[-1]!= nums2[j]:
                temp.append(nums2[j])
            j+=1
        elif nums[i]==nums2[j]:
            if not temp or temp[-1]!=nums[i]:
                temp.append(nums[i])
            i+=1
            j+=1   
    while i<len(nums):
        if temp[-1]!= nums[i]:
            temp.append(nums[i])
        i+=1
    while j<len(nums2):
        if temp[-1]!= nums2[j]:
            temp.append(nums2[j])
        j+=1
    
    print(temp)
    
def sorted_intersection_brute(nums,nums2):
    temp = [0]*len(nums2)
    intersection_array = []
    for i in range(0,len(nums)):
        for j in range(0,len(nums2)):
            if nums[i]==nums2[j] and temp[j]==0:
                intersection_array.append(nums2[j])
                temp[j] = 1
                break
            elif nums[i]<nums2[j]:
                break
    print(intersection_array)
    
def sorted_intersection_optimised(nums,nums2):
    i = 0
    j = 0
    intersection_array = []
    while (i<len(nums) and j<len(nums2)):
        if nums[i]==nums2[j]:
               intersection_array.append(nums[i])
               i+=1
               j+=1
        elif nums[i]> nums2[j]:
            j+=1
        else:
            i+=1
    print(intersection_array)
    
def missing_num_array_brute(nums):
    arr_sorted = sorted(nums)
    j = 0
    for i in range(arr_sorted[0],arr_sorted[-1]+1):
        if i != arr_sorted[j]:
            return i 
        j+=1
    return arr_sorted[-1]+1

def missing_num_array_optimised1(nums):
    hash = [0]*(len(nums)+1)
    for num in nums:
        hash[num]=1
    for i in range(0,len(nums)+1):
        if hash[i]==0:
            return i


def missing_num_array_optimised2(nums):
    n = len(nums)
    sum = n * (n+1)//2
    total = 0
    for num in nums:
        total+=num
    return abs(sum - total)

def missing_num_array_optimised3(nums):
    xor1 = 0
    xor2 = 0
    for i in range(0,len(nums)):
        xor1= xor1^nums[i]
        xor2 = xor2^(i+1)
    return abs(xor1-xor2)
    
        
# nums2 = list(map(int,input().split()))

def find_consequtive_ones(nums):
    max = 0
    current = 0
    for num in nums:
        if num==1:
            current+=1
        elif num==0:
            if current>max:
                max = current
                current = 0
    if current>max:
        max = current
    return max

def find_appears_once(nums):
    hash = {}
    for num in nums:
        if num not in hash:
            hash[num] = 1
        else:
            hash[num] +=1
    for key,value in hash.items():
        if value ==1:
            return key
    return -1

def find_appears_once_optimal(nums):
    l = 0
    r = 1
    while (r<len(nums)):
        if nums[l]!=nums[r]:
            return nums[l]
        else:
            l+=2
            r+=2
    return nums[-1]  # xor is more optimal

def max_sub_array(nums,m):
    max_sub_array = 0
    for i in range(0,len(nums)):
        for j in range(i,len(nums)):
            current = 0
            for k in range(i,j+1):
                current+=nums[k]
            if current == m:
                max_sub_array = max(max_sub_array,j-i+1)
    return max_sub_array
                
            
def max_sub_array_optimal(nums,k):
    r = 0
    l = 0
    max_sub = 0
    current = 0
    while(l<len(nums) and r<len(nums)):
        current+=nums[r]
        if current<=k:
            max_sub = max(r-l+1,max_sub)
            r+=1
        if current>k:
            current-=nums[l]
            l+=1
            if current<=k:
                max_sub = max(r-l+1,max_sub)
                r+=1
    return max_sub
                
def two_sum(nums,target):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]+nums[j]==target:
                return i,j
    return False


def two_sum_better(nums,target):
    hash = {}
    for i in range(len(nums)):
        if target-nums[i] in hash:
            return hash[target-nums[i]],i
        else:
            hash[nums[i]] = i
    return False 

def two_sum_optimal(nums,target):
    l = 0
    r = len(nums)-1
    while (l<r):
        if nums[l]+nums[r]>target:
            r-=1
        elif nums[l]+nums[r]<target:
            l+=1
        else:
            return l,r
    return False
    

def zero_one_two(nums):
    low = 0
    high = len(nums)-1
    mid = 0
    while (mid<=high):
        if nums[mid]==0:
            nums[mid],nums[low] = nums[low],nums[mid]
            low+=1
            mid+=1
        elif nums[mid]==1:
            mid+=1
        else:
            nums[mid],nums[high] = nums[high],nums[mid]
            high-=1
    print(nums)

def majority_element(nums):
    hash = {}
    high = float('-inf')
    freq = None
    for num in nums:
        if num not in hash:
            hash[num] = 1
        else:
            hash[num]+=1
    for key,value in hash.items():
        if value>high:
            high = value
            freq = key
    if high>len(nums)/2:
        return freq
    return -1

def majority_element_optimal(nums):
    left = 1
    current = nums[0]
    count = 1
    while (left <len(nums)):
        if nums[left]!=current and count==0:
            current = nums[left]
            count +=1
            left+=1
            
        elif nums[left]!=current and count>0:
            count-=1
            left+=1
            
        else:
            count+=1
            left+=1
    return current


def max_subarray_sum(nums):
    sum = float('-inf')
    for i in range(len(nums)):
        for j in range(i,len(nums)):
            count = 0
            for k in range(i,j+1):
                count+=nums[k]
            if count >sum:
                sum = count 
    return sum


def max_subarray_sum_better(nums):
    sum = 0
    for i in range(len(nums)):
        count = 0
        for j in range(i,len(nums)):
            count += nums[j]
            if count>sum:
                sum = count
    return sum

def max_subarray_sum_optimal(nums):
    max_subarray = float('-inf')
    curr = 0
    start = -1
    end = -1
    for index,num in enumerate(nums):
        if curr ==0:
            start = index
        curr+=num
        max_subarray = max(max_subarray,num,curr)
        if curr>max_subarray:
            end = index
        elif curr<0:
            curr = 0

    return max_subarray

def max_subarray_value(nums,target):
    max_subarray = 0
    for i in range(len(nums)):
        sum = 0
        for j in range(i,len(nums)):
            sum+=nums[j]
            if sum==target:
                max_subarray = max(max_subarray,j-i+1)
    return max_subarray

def max_subarray_value_optimal(nums,target):
    max_subarray_sum = float('-inf')
    curr = 0
    start = -1
    end = -1
    max_subarray = 0
    for index,num in enumerate(nums):
        if curr ==0:
            start = index
        curr+=num
        if curr>max_subarray_sum:
            end = index
            max_subarray_sum = max(max_subarray_sum,num,curr)
        if curr<0:
            curr = 0
        if max_subarray_sum == target:
            max_subarray = max(max_subarray,end-start+1)

    return max_subarray
            
        

def buy_and_sell(nums):
    profit = float('-inf')
    buy = 0
    sell = 0
    for i in range(len(nums)):
        buy = nums[i]
        for j in range(i,len(nums)):
            sell = nums[j]
            profit = max(profit,sell-buy)
    return profit


def buy_and_sell_optimal(nums):
    profit = 0
    minimum = nums[0]
    for i in range(1,len(nums)):
        profit = max(profit,nums[i]-minimum)
        minimum = min(minimum,nums[i])
        
    return profit

def arrange_pos_neg(nums):
    pos =  []
    neg = []
    for num in nums:
        if num>=0:
            pos.append(num)
        else:
            neg.append(num)
    for i in range(0,len(nums)//2):
        nums[i*2] = pos[i]
        nums[i*2+1] = neg[i]
        
    return nums

def arrange_pos_neg_better(nums):
    pos = 0
    neg = 1
    _array = [0]*len(nums)
    for num in nums:
        if num>=0:
            _array[pos] = num
            pos +=2
        else:
            _array[neg] = num
            neg+=2
    return _array

def gcdOfOddEvenSums(n) -> int:
        odd = n*n
        even = n*(n+1)
        while even:
            odd,even = even,odd%even
        return odd

print(gcdOfOddEvenSums(4))