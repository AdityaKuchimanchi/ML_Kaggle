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
