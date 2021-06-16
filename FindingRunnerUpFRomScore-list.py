'''
Using Functions & Methods:
Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given N scores. Store them in a list and find the score of the runner-up.

Sample Input 0

5
2 3 6 6 5
Sample Output 0
5
'''

print("Enter the number of participants: ")
if __name__ == '__main__':
    n = int(input())
    print("Enter the participants' scores: ")
    arr = map(int, input().split())
    print(sorted(list(set(arr)))[-2])


