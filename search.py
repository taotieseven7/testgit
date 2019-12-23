#二分查找
def search(num,l):
    
    left=0
    right=len(l)-1

    while left<=right and left>=0:
        mid=(left+right)//2
        if l[mid]==num:
            print("元素所在位置为：",mid)
            return
    
        elif l[mid]<num:
            left=mid+1

        else:
            right=mid-1

        

    print("未查找到该元素")

l=[2,4,5,7,9,12,14,14,17,19]
