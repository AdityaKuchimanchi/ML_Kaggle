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

