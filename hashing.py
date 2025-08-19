
nums = list(map(int, input().split()))



def selection_sort():
    
    def swap(i,min_idx):
        nums[i],nums[min_idx] = nums[min_idx],nums[i]
        
    for i in range(0,len(nums)-1):
        min_idx = i
        for j in range(i,len(nums)):
            if nums[j]<nums[min_idx]:
                min_idx = j
        swap(i,min_idx)
        
    for num in nums:
        print(num)
    
    
def bubble_sort():
    for i in range(len(nums),0,-1):
        did_swap = 0
        for j in range(0,i-1):
            if nums[j+1]<nums[j]:
                nums[j],nums[j+1] = nums[j+1],nums[j]
                did_swap = 1
        print(nums)
        if did_swap==0:
            break
        did_swap = 0
    
    for num in nums:
        print(num)


def insertion_sort():
    for i in range(0,len(nums)):
        j = i
        while(j>0 and nums[j-1]>nums[j]):
            nums[j-1],nums[j] = nums[j],nums[j-1]
            j-=1
        
    for num in nums:
        print(num)
        

def merge(nums,low,mid,high):
    temp = []
    left = low
    right = mid+1
    while(left<=mid and right<=high):
        if (nums[left]<nums[right]):
            temp.append(nums[left])
            left+=1
        else:
            temp.append(nums[right])
            right+=1
            
    while(left<=mid):
        temp.append(nums[left])
        left+=1
    while(right<=high):
        temp.append(nums[right])
        right+=1
        
    for i in range(low,high+1):
        nums[i] = temp[i-low]

def merge_sort(nums,low,high):
    if (low>=high): return 
    mid = (low+high)//2
    merge_sort(nums,low,mid)
    merge_sort(nums,mid+1,high)
    merge(nums,low,mid,high)
    

def partion(nums,low,high):
    pivot = low
    i = low
    j = high
    while (i<j):
        while (nums[i]<=nums[pivot] and i<high):
            i+=1
        while (nums[j]> nums[pivot] and j>low):
            j-=1
        if i<j:
            nums[i],nums[j] = nums[j],nums[i]
    nums[pivot],nums[j] = nums[j],nums[pivot]
    return j
            
    
def quick_sort(nums,low,high):
    if low<high:
        part_idx = partion(nums,low,high)
        quick_sort(nums,low,part_idx)
        quick_sort(nums,part_idx+1,high)

def bubble_rec(nums,len):
    if len==0:
        return 
    for i in range(0,len-1):
        if nums[i+1]<nums[i]:
            nums[i+1],nums[i] = nums[i],nums[i+1]
    bubble_rec(nums,len-1)

def insert_rec(nums,start):
    if start==len(nums):
        return 
    i = start
    while (i>0 and nums[i]< nums[i-1]):
        nums[i],nums[i-1] = nums[i-1],nums[i]
        i-=1
    
    insert_rec(nums,start+1)

insert_rec(nums,0)
print(nums)