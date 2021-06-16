'''
Read four integers from the keyboard a,b,c, d and those values in the following order.

max > mid1 > mid2 > min

Sample Input 
10 1 7 5

Sample Output
10 > 7 > 5 > 1
'''
print("Input four integers:")
nums = list(map(int, input().split()))
nums.sort()
nums.reverse()
print("After sorting the said Integers:")
print(*nums,sep = " > ")
