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