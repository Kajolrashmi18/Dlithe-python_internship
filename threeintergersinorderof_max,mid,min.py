'''
Read three integers from the keyboard a,b,c and those values in the following order.

max > mid > min

Sample Input 
10 1 7

Sample Output
10 > 7 > 1
'''
print("Enter the three numbers")                                    
a,b,c = map(int,input().split())                                                
x=max(a,b,c)                                                                   
y=min(a,b,c)                                                                                      
z=(a+b+c)-x-y                                   
print(x,z,y,sep=" > ")  #print(max(a,b),((a+b+c)-a-b),min(a,b),sep=” > “)

