#1. Write a prorgram to calculate simple interest.
	# formula to calculate simple interest : PNR/100                     Output
  P=int(input("Principle amount: "))                                  #  Principle amount: 2000               
  T=float(input("Number of years: "))                                  #  Number of years: 1
  R=float(input("Rate of interest: "))                                 #  Rate of interest: 10
  SI=P *T *R/100                                                                
  print("Simple Interest =  ",round(SI,2))                            #   Simple Interest =  200.0

#2. Write a program to find sum and average of 3 values
  print("Enter the three numbers : ")                                  #Enter the three numbers :
  a,b,c = map(int,input().split())                                      #      11 16 20
  Sum=a+b+c                                                               
  average=(a+b+c)/3 
  print("Sum = ",Sum)                                                    #        Sum =  47
  print("Average = ",average)                                             #  Average = 15.666666666666666

#3. Write a program to perform the following task. The provided code stub reads two integers from STDIN,  and . Add code to print three lines where:  
#The first line contains the sum of the two numbers.
# The second line contains the difference of the two numbers (first - second).
# The third line contains the product of the two numbers.

'''Sample Input 0

3
2
Sample Output 0

5
1
6 '''

  print("Enter two numbers")                                              # Enter two numbers
  a=int(input())                                                           #           52
  b=int(input())                                                            #          24
  print(“Sum = “,a+b)                                                        #    Sum = 76
  print(“Difference = “,a-b)                                                #  Difference = 28 
  print(“Product = “,a*b)    

