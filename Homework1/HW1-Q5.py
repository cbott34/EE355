# Given two sorted arrays arraynum1 and arraynums2 of size m and n respectively, 
# return the median of the two sorted arrays. You may code this in either Python or C, your choice. 
# arraynums1.length == m
# arraynums2.length == n
# 0 <= m <= 1000
# 0 <= n <= 1000
# 1 <= m + n <= 2000
# -106 <= arraynums1[i], arraynums2[i] <= 106
#
# Notes:
# 1) Although a complexity of O(Log(n+m)) is prefered, any correct algorithm with higher complexities, 
# would also receive a perfect point.
# 2) For coding questions such as this one, try to submit a test code or testbench or test plan 
# in addition to design code. It's a good practice to take testing seriously.
  
# This function returns median of sorted arrays arraynum1[] and arraynum2[]. 

def getMedian(arraynum1, arraynum2, n, m) :
  
    i = 0 # Current index of input array arraynum1[] 
    j = 0 # Current index of input array arraynum2[] 
    median1, median2 = -1, -1 
     
    # There are two cases, if n+m is odd, then the middle element of combined sorted array is median
    
    if((m + n) % 2 == 1) :    
        for count in range(((n + m) // 2) + 1) :        
            if(i != n and j != m) :
                if arraynum1[i] > arraynum2[j] :
                    median1 = arraynum2[j]
                    j += 1
                else :
                    median1 = arraynum1[i]
                    i += 1            
            elif(i < n) :            
                median1 = arraynum1[i]
                i += 1
           
            # for case when j<m, 
            else :            
                median1 = arraynum2[j]
                j += 1        
        return median1
      
    # Other case: Median will be average of the two middle elements of the combined sorted array
        for count in range(((n + m) // 2) + 1) :         
            median2 = median1
            if(i != n and j != m) :        
                if arraynum1[i] > arraynum2[j] :
                    median1 = arraynum2[j]
                    j += 1
                else :
                    median1 = arraynum1[i]
                    i += 1            
            elif(i < n) :            
                median1 = arraynum1[i]
                i += 1
              
            # for case when j<m, 
            else :            
                median1 = arraynum2[j]
                j += 1        
        return (median1 + median2)//2
  
# Driver code      

arraynum1 = []
x = int(input("Enter Size of First Sorted Array Followed Sorted Contents: "))
for i in range(0,x):
    entries = int(input())
    arraynum1.append(entries)

arraynum2 = []
x = int(input("Enter Size of Second Sorted Array Followed Sorted Contents: "))
for i in range(0,x):
    entries = int(input())
    arraynum2.append(entries)
  
n1 = len(arraynum1)
n2 = len(arraynum2)
print("Median of Combined Arrays : " + str((getMedian(arraynum1, arraynum2, n1, n2))))