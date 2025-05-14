## practice continues here.

## Function With Return Value
## 1. Here one integer n is given. You need to 
## write the complete function returnValueFunction that takes n as a parameter 
## and uses the return keyword to return double the value of n

def return_value_function(n):
  return n*n

n=2
print(return_value_function(n))

## 2. This problem has no input. You need to write the function helloFunction that prints Hello
def return_default_value():
  return "Hello"

print(return_default_value())

## 3. Here two integers a and b are given. The given input and its values are passed as arguments to the function argumentFunction. 
## The argumentFunction is responsible to return (a+b). You need to write this function

def function_with_arguments(a,b):
  return a+b
a=b=3
print(function_with_arguments(a,b))

## 4. Given a number n, find the first digit of the number

def find_first_number(n):
  return str(n)[0]
n=458
print(find_first_number(n))

## 5. Print GFG n times without the loop
def printGfg(n):
    print(n)
    printGfg(n)
n="GFG"
printGfg(n)

## 6. Print numbers from 1 to n without the help of loops. 
## You only need to complete the function printNos() that takes n as a parameter and prints the number from 1 to n recursively
def print_recursive_num(n):
    print(*range(1,n+1))
n=10
print_recursive_num(n)

## 7. Fibonacci series up to Nth term
def fibonacci(n):
    if n<=0:
        return []
    elif n == 1:
        return [0]
    else:
        fib_list = [0,1]
        while len(fib_list)<=n:
            next_fib= fib_list[-1] + fib_list[-2]
            fib_list.append(next_fib)
    return fib_list
print(fibnocci(15))

## 8.Juggler Sequence
## Juggler Sequence is a series of integers in which the first term starts with a positive integer number a and the remaining terms 
## are generated from the immediate previous term using the below recurrence relation:
## Given a number n, find the Juggler Sequence for this number as the first term of the sequence until it becomes 1
import math as m
def juggler_seq(n):
    if n != 1:
        if n%2==0:
            n = int(m.sqrt(pow(n, 1)))
            print(n)
        else:
            n = int(m.sqrt(pow(n,3)))
            print(n)
        juggler_seq(n)
a = 9
print(a)
juggler_seq(a)

## 9. Power Of Numbers
## Given a number n, find the value of n raised to the power of its own reverse
import math as m
def pow_reverse(n):
    # print(n)
   b = str(n)[::-1]
   n = pow(n, int(b[-1]))
   print(n)
a = 3
pow_reverse(a)

## --------------------------------------------------------------------------------------------------------------------------- ##
##List Traversal
## You are given a list that contains integers. You need to print the elements of the list with a space between them.
lst = [54, 43, 2, 1, 5]

for i in lst:
    print(i, end=" ")

## Length of The List
## You are given a list that contains integers. You need to return the length of the list.
def length_list(n):
    return len(n)
print(length_list([54, 43, 2, 1, 5]))

## Sum The List
## You are given a list that contains integers. You need to return the sum of the list.
def sum_list(n):
    sum =0
    for i in n:
        sum += i
    return sum
print(sum_list([54, 43, 2, 1, 5]))

## Decrement List Values
## You are given a list that contains integers. You need to decrement each element of the list by 1 and return the list.
def minus_list(n):
    sum =0
    for i in n:
        sum = i-1
        print(sum)
minus_list([54, 43, 2, 1, 5])

## Append To List
## You are given three inputs a, b, c. You need to create a list and append a, b, c to the list and then return that list.
def append_lst(a,b,c):
    ip=[a,b,c]
    lst=[]
    lst.extend(ip)
    return lst
a = 1 
b = 2 
c = 3
print(append_lst(a,b,c))

## Less Than
## You are given a number k and a list arr that contains integers. You need to return list of numbers that are less than k.
def less_than(n,k):
    for i in n:
        if i < k:
            print(i)
lst=[54, 43, 2, 1, 5]
k=6
less_than(lst,k)

## Average
## You are given a list arr that contains integers. You need to return average of the non negative integers.
n = [5, 0, 0, 0] #[1, 2, 3] #[-12, 8, -7, 6, 12, -9, 14]
def avg_positive_num(n):
    avg_val = 0
    op = []
    for i in n:
        if i>0:
            op.append(i)
    avg_val = sum(op)/len(op)        
    return avg_val
print(avg_positive_num(n))

## Separate Even Odd
## You are given a list numbers that contains integers. You need to return two lists, one of even numbers and other of odd numbers.
lst=[54, 43, 2, 5, 14, 17, 18, 9]
def seperate_even_odd(n):
    even_lst=[]
    odd_lst=[]
    for i in n:
        if i%2==0:
            even_lst.append(i)
        else:
            odd_lst.append(i)
    return even_lst,odd_lst
print(seperate_even_odd(lst))
