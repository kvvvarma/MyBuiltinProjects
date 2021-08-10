#Stopping station problem

# There are 12 intermediate stations between two places A and B. 
# Find the number of ways in which a train can be made to stop at 
# 4 of these intermediate stations so that no two stopping stations are consecutive?

# Examples –
# Test Case - 1


# Input  : n = 12, s = 4
# Output : 126

# Test Case - 2 

# Input  : n = 16, s = 5
# Output : 792

#stop station
def train_stopping_station(p, n):
    num = 1                         #--> Numerators                   
    dem = 1                         #--> Denomerators
    s = p
 # selecting specified position
    while p != 1:  
        dem *= p
        p-=1
        t = n - s + 1
        #dem = 24
        
    while t != (n-2 * s + 1):
        num *= t
        t-=1
        #num = 9, 72, 504, 3024  
    if (n - s + 1) >= s:
        #num = 3024
        #dem = 24
        return int(num/dem)
        #3024/24 = 126
    else:
        return -1


num = train_stopping_station(5, 16)
if num != -1:
 print(f"Stopping Stations Count is : {num}")
else:
 print("Not  Possible")
 
 
 #As per the Given test cases the program is executing..
 #As per the first test case the result is showing as 126 
 #As per the second test case the result is shwoing as 792