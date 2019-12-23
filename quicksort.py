def quick(l,left,right):
    i=left
    j=right
    
    if len(l)<=1 or i>=j:
       return 

    key=l[i]

    while i!=j:        
            
        while(l[j]>=key and j>i):
            print("$$$$$$$$$$")
            j=j-1

        while(l[i]<=key and j>i):
            i=i+1
        if i<j:
            temp=l[i]
            l[i]=l[j]
            l[j]=temp

    l[left]=l[i]
    l[i]=key
    
    quick(l,0,i-1)
    
    quick(l,i+1,right)
    print(l)


#最差时间复杂度O(N2),平均时间复杂度O（NlogN）   
l=[23,24,63,56]

#l=[13,2,56,24,8,7,9,23,63,13]


                
                
