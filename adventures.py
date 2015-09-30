#adventures in python

# codewars problem:
# Write a function that removes each 9 that it is in between 7s.
#
def seven_ate9(str_):
  leftSeven = False
  for i in range(len(str_)):
    if (str_[i] == '9'):
      if (str_[i-1] == '7' and str_[i+1] == '7'):
        del str[i]
        i -= 1
  return str_
# this was my first idea: iterate through the string and if we find a 9,
# check if its left and right neighbors are 7s and if they are delete the 9
# after it didnt work, I remembered that del only works on lists not strings
# so I looked online for some methods that could be run on strings and found
# string.replace(this,withThis)
# I decided to use it like str_.replace('797','77'). My idea was that this
# would automatically remove all of the 9s that were inbetween 7s... but it still
# didnt work. For example, consider 7979797. This should return 7777 but instead
# returned 77977. What happens is that python breaks up the string like this:
# 797 9 797 and replaces those 797s with 77s like so: 77 9 77. To fix this, I decided
# to just call replace twice which led me to my implementation that passed all the tests:
def seven_ate9(str_):
  return str_.replace('797','77').replace('797','77')
# This worked but it doesnt satisfy me because I believe that there is some way to craft
# a case that will break this code.
# The best implementation that I found was this one:
def seven_ate9(str_):
  while str_.find('797') != -1:
    str_ = str_.replace('797','77')
  return str_
# You can tell that this one will work no matter what because it will keep using str_.find
# to look for 797s and replace them as needed. In my opinion this is the safest implentation


# Create a function that returns the lowest product of 4 consecutive numbers in a given string of numbers.
# This should only work is the number has 4 digits of more. If not, return "Number is too small".
def lowest_product(input):
  if len(input) < 4:
    return "Number is too small"
  numList = [int(x) for x in list(input)]
  lowest = 1
  for i in numList[:4]:
    lowest *= i
  current = lowest
  if lowest == 0:
    return 0
  for i in range(4,len(numList)):
    if numList[i] == 0:
      return 0
    current *= numList[i]
    current //= numList[i-4]
    if current < lowest:
      lowest = current
  return lowest
# At first I believed that my implementation was pretty clever. I start with the product of
# the first four integers then iterate through the rest of the list. As I iterate, I multiply
# by the newest number encountered and divide by the oldest number in the list. This results
# in a new product of four numbers. If it is the smallest that I've seen so far, then I save
# it as the lowest. At the end of the iteration, I return the lowest. This strategy works as
# long as there are no zeros in the input since were dividing. To fix this, As soon as I encounter
# a zero, I return zero.
def lowest_product(input):
  s = map(int, str(input))
  if len(s) < 4:
    return "Number is too small"
  return min(map(lambda a,b,c,d : a * b * c * d, s[:-3], s[1:-2], s[2:-1], s[3:]))
# This was the highest rated solution for this problem. Its concise and clever but it iterates through
# the list four times and It is a bit harder to read. I still want to spend some time picking this one apart


# You have a sequence of positive numbers starting with 1, but one number is missing!
# Find out the missing number; if the sequence is not broken, you should return 0.
# Each sequence always increments by 1.
# In short: an invalid sequence must return 1, an already complete (or empty) sequence must return 0;
# otherwise return the missing element.
# Note that the sequence may be shuffled.
def find_missing_number(sequence):
  nums = [int(x) for x in sorted(sequence.split())]
  if len(nums) == 0:
    return 0
  if nums[0] != 1:
    return 1
  for i in range(len(nums)-1):
    if nums[i]+1 != nums[i+1]:
      return nums[i]+1
  return 0
# There were a lot of edge cases that I kept running into so in the end, my code didnt work
# This was the best solution that I found:
def find_missing_number(sequence):
  if not len(sequence): return 0
  sequence = [i for i in sequence.split() if i.isdigit()]
  if not len(sequence): return 1
  for i in range(1, max(map(int,sequence))):
    if str(i) not in sequence: return i
  return 0
# Make a program that takes a list of a random amount (but will always have atleast 1 number in)
# of numbers and returns the average, or mean, of the numbers.
# Also the program should return "Incorrect" if the value entered is a string.
def average(x):
    if type(x) != list:
        return "Incorrect"
    result = 0
    for i in x:
        result += i
    return result // len(x)
# This was my favorite solution
def average(xs):
    try:
        return sum(xs)/len(xs)
    except:
        return "Incorrect"
# I didnt know about sum() before this problem and I had never used python try catch blocks
# One big difference between python and javascript is that python throws exceptions where js
# will just return undefined or something so its smart to take advantage of those exceptions

#Make a program that takes a value (x) and returns "Bang" if the number is divisible by 3,
# "Boom" if it is divisible by 5, "BangBoom" if it divisible by 3 and 5,
# and "Miss" if it isn't divisible by any of them.
# Note: Your program should only return one value
def multiple(x):
    if x%15 == 0:
        return "BangBoom"
    if x%5 == 0:
        return "Boom"
    if x%3 == 0:
        return "Bang"
    return "Miss"
# Its just a variation of FizzBuzz
# This was the coolest solution
def multiple(x):
    return 'Bang' * (x % 3 == 0) + 'Boom' * (x % 5 == 0) or 'Miss'