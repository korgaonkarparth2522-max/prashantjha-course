def findBiggestNumber(array): #------------------->O(1)
    firstvalue=array[0] #------------------------->O(1)
    for i in range(1,len(array)): #--------------->O(n)----->
        if array[i]>firstvalue: #----------------->O(1)----->O(n) #overall complexity is the O(n)
            firstvalue=array[i] #----------------->O(1)----->
    print(firstvalue) #--------------------------->O(1)
    
array=[2,4,5,6,7,1,9,3,4,5,6]
findBiggestNumber(array)