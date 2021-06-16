'''
A little girl living in a village craves some rava idli even though she has had rava idli for the last 346514534 days in a row !! (Strange, you might think. But its normal down here)

At the idli shop there are two types of Rava Idli's available.

One goes for Rs.A per piece and the other goes for Rs.B per piece.
The girl has a total of K rupees.

What is the maximum number of rava idlis that she can have?

Note that she does not care about the type of idli she gets, she just wants to have as many rava idlis of any type as possible.

Input

The first line contains the number of test cases T
1 = T = 1000
Each test case contains three integers, A, B and K.
1 = A,B,K = 10^9
'''
print(“Enter the value of N”)
n=int(input())
for i in range (n):
    a,b,k=(map(int,input().split()))
    if a>=b:
        print(k//b)
    else:
        print(k//a)
