'''
Python program to remove Nth occurrence of the given word. Given a list of words in Python, the task is to remove the Nth occurrence of the given word in that list.

Examples:

Input: list - ["Python", "for", "developers", "professionals", "developers"]
       word = developers, N = 2
Output: list - ["Python", "for", "developers", "professionals"]

Input: list - ["can", "you",  "can", "a", "can" "?"]
       word = can, N = 1
Output: list - ["you",  "can", "a", "can" "?"]
'''

list1 = input().split()
word, N = input().split()
count = list1.count(word)

i = 0
index = -1

while count > 0:
    index = list1.index(word, index+1)
    i += 1
    if i == int(N):
        list1.pop(index)
        break
    count -= 1
print(list1)


