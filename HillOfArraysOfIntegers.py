'''
Array of integers is a hill, if:

it is strictly increasing in the beginning; after that it is constant; after that it is strictly decreasing.
The first block (increasing) and the last block (decreasing) may be absent. It is allowed that both of this blocks are absent.
For example, the following three arrays are a hill: [5,7,11,11,2,1], [4,4,2], [7],
but the following three are not unimodal: [5,5,6,6,1], [1,2,1,2], [4,5,5,6].

Write a program that checks if an array is a hill.

Input Format

The first line contains integer n (1<=n<=100) — the number of elements in the array.

The second line contains n integers a1,a2,...,an (1<=ai<=1000) — the elements of the array.

Output Format

Print "yes" if the given array is a hill. Otherwise, print "no".

'''
list1 = [ ]
n = int(input("No.of elements: "))

for i in range(n):
    elt = int(input())
    list1.append(elt)

i = 1

if i < n:
    while i<n and list1[i] > list1[i-1]:
        i += 1
    while i<n and list1[i] == list1[i-1]:
        i += 1
    while i<n and list1[i] < list1[i-1]:
        i += 1
    print("Yes")
else:
    print("No")
