'''
PRINT THE BELOW MENTIONED PATTERN FOR ANY "N" VALUE. WHERE "N" INDICATES NO.OF ROWS.

Input Format

A SINGLE INTEGER DENOTING N VALUE

Constraints

1<=N<=100

N is only odd

Output Format

PATTERN AS SHOWN IN SAMPLE TEST CASE

Sample Input 0

5
Sample Output 0

1   5
 2 4
  3
.
'''

print("Enter the value of N")
n=int(input())
if n % 2 != 0 and 1 <= n <= 100:
    for i in range(1, n//2 + 2):
        for j in range(1, n + 1):
            if j==i or j==n - i + 1:
                print(j, end="")
            else:
                print(" ",end="")
        print()
else:
    print("N not odd or greater than 100")
