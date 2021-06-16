'''
Rotate a given String in the specified direction by specified magnitude.
After each rotation make a note of the first character of the rotated String, After all rotation are performed the accumulated first character as noted previously will form another string, say FIRSTCHARSTRING.
Check If FIRSTCHARSTRING is an Anagram of any substring of the Original string.
If yes print "YES" otherwise "NO". Input
The first line contains the original string s. The second line contains a single integer q. The ith of the next q lines contains character d[i] denoting direction and integer r[i] denoting the magnitude.

Constraints
1 <= Length of original string <= 30
1<= q <= 10

Output
YES or NO

Example 1
Input
carrace
 3
 L 2
 R 2
 '''

string = input("Enter the string: ")
no_rotation = int(input("Enter the number of rotations: "))
rotation_list = []
print("Enter the rotation commands: ")
for _ in range(no_rotation):
    rotation_list.append(input().split())
firstcharstring = ""
for r_type,nor in rotation_list:
    nor = int(nor)
    if r_type == "L":
        firstcharstring += (string[nor:] + string[:nor])[0]
    elif r_type == "R":
        firstcharstring += (string[nor*-1:] + string[:len(string)-nor])[0]
        
substring_list = []
for index1 in range(1,len(string)+1):
    for index2 in range(index1,len(string)+1):
        if len(string[index1-1:index2]) == len(firstcharstring):
            substring_list.append(string[index1-1:index2])
            
for substring in substring_list:
    if sorted(firstcharstring) == sorted(substring):
        print("YES")
        break
    else:
        print("NO")
        break
