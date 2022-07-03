# Exercise 1: Write function named sum_to that accepts a single integer n, and returns the sum of the integers from 1 to n
# sum_to(6) #returns 21
# sum_to(10) #returns 55

# ----- My code -----
def sum_to(n):
  sum = 0
# loop from 1 to n
  for num in range(1, n + 1, 1):
      sum = sum + num
  print("Sum of first", n, "numbers is: ", sum)

sum_to(6)
sum_to(10)


# Exercise 2: Write a function called largest that takes a list of numbers as an argument and returns the largest number in that list
# largest([1, 2, 3, 4, 0]) #returns 4
# largest([10, 4, 2, 231, 91, 54]) # returns 231

# ----- My Code -----
def largest(list):
  print("The largest element is:", max(list))

largest([1, 2, 3, 4, 0])
largest([10, 4, 2, 231, 91, 54])





# 3. write a function named occurrences that takes two string elements as input and counts the number of occurrences of the second string inside the first string.
# occurrences('fleep floop', 'e')  #returns 2
# occurrences('fleep floop', 'p')  #returns 2
# occurrences('fleep floop', 'ee')  #returns 1
# occurrences('fleep floop', 'fe')  #returns 0

# ----- My code -----
def occurrences(phrase, letter):
  letter_count = phrase.count(letter)
  print(f"The count of {letter} is:", letter_count)

occurrences('fleep floop', 'e')
occurrences('fleep floop', 'p')
occurrences('fleep floop', 'ee')
occurrences('fleep floop', 'fe')



# 4. Write a function named product that takes an arbitrary number of numbers, multiplies them all together, and returns the product (review your notes on *args)
# product(-1, 4)      #returns -4
# product(2, 5, 5)    #returns 50
# product(4, 0.5, 5)  # returns 10.0

# ----- My Code -----

def product(*args):
  total = 1
  for x in args:
    total *= x
  return total
print(product(-1, 4))
print(product(2, 5, 5))
print(product(4, 0.5, 5))
