# Exercise 1: Calculate the multiplication and sum of two numbers 
# Given two integer numbers, write a Python program to return their product only if the product is equal to or lower than 1000. Otherwise, return their sum.
'''
num1=20
num2=30
num1=40
num2=30

def multiplication_or_sum(n1,n2):
  if n1*n2<=1000:
    return n1*n2
  return n1+n2

print(multiplication_or_sum(num1,num2))
'''

#Exercise 2: Print the Sum of a Current Number and a Previous number
#Write Python code to iterate through the first 10 numbers and, in each iteration, print the sum of the current and previous number.
'''
def print_sum_and_prev(num):
  for n in range(num):
    prev = 0 if n-1<0 else n-1  
    sum = n+prev
    print(f"Current Number {n} Previous Number  {prev}  Sum:  {sum}")

print_sum_and_prev(10)
'''

#Exercise 3: Print characters present at an even index number
#Write a Python code to accept a string from the user and display characters present at an even index number.
#For example, str = "PYnative". so your code should display ‘P’, ‘n’, ‘t’, ‘v’.
'''
def print_only_even_index():
  str=input("please provide a string ")
  print("Orginal String is", str)
  print("Printing only even index chars")

  length = len(str)

  for i in range(0,length-1,2):
   print(f"Index: {i}, word: {str[i]}")


print_only_even_index()
'''

#Exercise 4: Remove first n characters from a string
#Write a Python code to remove characters from a string from 0 to n and return a new string.
'''
def remove_chars(word, n):
  word_size = len(word)

  if n>=word_size:
    return "To many characters to remove"
  
  print("Removing characters from a string")
  new_word = word[n:]
  return new_word

print(remove_chars("pynative", 4)) 
# output 'tive' first four characters are removed
print(remove_chars("pynative", 2)) 
# output 'native'
'''

#Exercise 5: Check if the first and last numbers of a list are the same
#Write a code to return True if the list’s first and last numbers are the same. If the numbers are different, return False.
'''
numbers = [10, 20, 30, 40, 10]
#numbers = [75, 65, 35, 75, 30]

def is_first_and_last_identical(list):
  is_identical = True if list[0] == list[len(list)-1] else False
  return is_identical

print(is_first_and_last_identical(numbers))
'''


