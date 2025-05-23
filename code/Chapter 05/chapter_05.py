# -*- coding: utf-8 -*-
"""Chapter_05.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/github/nceder/qpb4e/blob/main/code/Chapter%2005/Chapter_05.ipynb

# 5 Lists, tuples, and sets

# 5.1 Lists are like arrays
"""

# This assigns a three-element list to x
x = [1, 2, 3]

# First element is a number, second is a string, third is another list.
x = [2, "two", [1, 2, 3]]
len(x)

"""### Quick Check: len()
What would len() return for each of the following: `[0]`; `[]`; `[[1, 3, [4, 5], 6], 7]`?
"""

len([0])

len([])

len([[1, 3, [4, 5], 6], 7])

"""## 5.2 List indices"""

x = ["first", "second", "third", "fourth"]
x[0]

x[2]

x[-2]

x = ["first", "second", "third", "fourth"]
x[1:-1]

x[0:3]

x[2:]

y = x[:]
y[0] = '1 st'
y

x

"""### Try This: list slices and indexes
Using what you know about the `len()` function and list slices, how would you combine the two to get the second half of a list when you don't know what size it is? Experiment in the Python shell to confirm that your solution works.
"""

# experiment with your code here

my_list = [1, 2, 3, 4, 5, 6]
last_half = my_list[len(my_list)//2:]
last_half

"""## 5.3 Modifying lists"""

x = [1, 2, 3, 4]
x[1] = "two"
x

x = [1, 2, 3, 4]
x[len(x):] = [5, 6, 7]              #A
x

x[:0] = [-1, 0]                     #B
x

x[1:-1] = []                        #C
x

x = [1, 2, 3]
x.append("four")
x

x = [1, 2, 3, 4]
y = [5, 6, 7]
x.append(y)
x

x = [1, 2, 3, 4]
y = [5, 6, 7]
x.extend(y)
x

x = [1, 2, 3]
x.insert(2, "hello")
x

x.insert(0, "start")
x

x = [1, 2, 3]
x.insert(-1, "hello")
x

x = ['a', 2, 'c', 7, 9, 11]
del x[1]
x

del x[:2]
x

x = [1, 2, 3, 4, 3, 5]
x.remove(3)
x

x.remove(3)
x

x.remove(3)

x = [1, 3, 5, 6, 7]
x.reverse()
x

"""### Try this: Modifying lists
Suppose that you have a list 10 items long. How might you move the last three items from the end of the list to the beginning, keeping them in the same order?

"""

# experiement here

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
my_list = my_list[-3:] + my_list[:-3]
my_list

"""## 5.4 Sorting lists"""

my_list = my_list[-3:] + my_list[:-3]
my_list

x = [3, 8, 4, 0, 2, 1]
x.sort()
x

x = [2, 4, 1, 3]
y = x[:]
y.sort()
y

x

x = ["Life", "Is", "Enchanting"]
x.sort()
x

x = [1, 2, 'hello', 3]
x.sort()

x = [[3, 5], [2, 9], [2, 3], [4, 1], [3, 2]]
x.sort()
x

def comp_num_of_chars(string1):
    return len(string1)
word_list = ['Python', 'is', 'better', 'than', 'C']
word_list.sort()
print(word_list)

word_list = ['Python', 'is', 'better', 'than', 'C']
word_list.sort(key=comp_num_of_chars)
print(word_list)

x = (4, 3, 1, 2)
y = sorted(x)
y

z = sorted(x, reverse=True)
z

"""### Try this: Sorting lists
Suppose that you have a list in which each element is in turn a list: `[[1, 2, 3], [2, 1, 3], [4, 0, 1]]`. If you wanted to sort this list by the second element in each list so that the result would be `[[4, 0, 1], [2, 1, 3], [1, 2, 3]]`, what function would you write to pass as the key value to the sort() method?
"""

# experiement here

the_list =  [[1, 2, 3], [2, 1, 3], [4, 0, 1]]
the_list.sort(key=lambda x: x[1])
the_list

"""or"""

the_list =  [[1, 2, 3], [2, 1, 3], [4, 0, 1]]
the_list.sort(key=lambda x: x[1])
the_list

"""## 5.5 Other list operations"""

3 in [1, 3, 4, 5]

3 not in [1, 3, 4, 5]

3 in ["one", "two", "three"]

3 not in ["one", "two", "three"]

z = [1, 2, 3] + [4, 5]
z

z = [None] * 4
z

z = [3, 1] * 2
z

min([3, 7, 0, -2, 11])

max([4, "Hello", [1, 2]])

x = [1, 3, "five", 7, -2]
x.index(7)

x.index(5)

x = [1, 2, 2, 3, 5, 2, 5]
x.count(2)

x.count(5)

x.count(4)

"""### Quick Check: List Operations
What would be the result of `len([[1,2]] * 3)`?

What are two differences between using the `in` operator and a list's `index()` method?

Which of the following will raise an exception?: `min(["a", "b”, "c"])`; `max([1, 2, "three"])`; `[1, 2, 3].count("one")`
"""

len([[1,2]] * 3)

"""What are two differences between using the `in` operator and a list's `index()` method?

* index gives position; in gives a true/false answer.
* index gives an error if an element isn’t in the list.
Which of the following raises an exception?
"""

min(["a", "b”, "c"])

max([1, 2, "three"])

[1, 2, 3].count("one")

"""### Try This: List operations
If you have a list x, write the code to safely remove an item if—and only if—that value is in the list.

Modify that code to remove the element only if the item occurs in the list more than once.

"""



x = [1, 2, 3, 4, 5, 4]
# change element to a value not in x to text counter case
element = 3
if element in x:
    x.remove(element)
x

x = [1, 2, 3, 4, 5, 4]
# change element to something other than 4 or a value not in x to text counter cases
element = 4
if x.count(element) > 1:
    x.remove(element)
x

"""## 5.6 Nested lists and deep copies"""

m = [[0, 1, 2], [10, 11, 12], [20, 21, 22]]
m[0]

m[0][1]

m[2]

m[2][2]

nested = [0]
original = [nested, 1]
original

nested[0] = 'zero'
original

original[0][0] = 0
nested

original

nested = [2]
original

original = [[0], 1]
shallow = original[:]
import copy
deep = copy.deepcopy(original)

shallow[1] = 2
shallow

original

shallow[0][0] = 'zero'
original

deep[0][0] = 5
deep

original

"""### Try This: List copies
Suppose that you have the following list: `x = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]` What code could you use to get a copy y of that list in which you could change the elements without the side effect of changing the contents of x?

"""



import copy
x = [1, 2, 3, 4, 5]
copy_x = copy.deepcopy(x)
copy_x

"""## 5.7 Tuples"""

x = ('a', 'b', 'c')
x[2]

x[1:]

len(x)

max(x)

min(x)

5 in x

5 not in x

x[2] = 'd'

x + x

2 * x

x[:]

x * 1

x + ()

x = 3
y = 4
(x + y)   # This line adds x and y.

(x + y,)  # Including a comma indicates that the parentheses denote a tuple.

()        # To create an empty tuple, use an empty pair of parentheses.

(one, two, three, four) =  (1, 2, 3, 4)
one

two

one, two, three, four = 1, 2, 3, 4

x = (1, 2, 3, 4)
a, b, *c = x
a, b, c

a, *b, c = x
a, b, c

*a, b, c = x
a, b, c

a, b, c, d, *e = x
a, b, c, d, e

[a, b] = [1, 2]
[c, d] = 3, 4
[e, f] = (5, 6)
(g, h) = 7, 8
i, j = [9, 10]
k, l = (11, 12)
a

[b, c, d]

(e, f, g)

h, i, j, k, l

list((1, 2, 3, 4))

tuple([1, 2, 3, 4])

list("Hello")

"""### Quick Check: Tuples
Explain why the following operations aren't legal for the tuple `x = (1, 2, 3, 4)`:

`x.append(1)`

`x[1] = "hello"`

`del x[2]`

All of these operations change the object in place, and tuples can't be changed.

If you had a tuple `x = (3, 1, 4, 2)`, how might you end up with x sorted?
"""



x = (3, 1, 4, 2)
x = tuple(sorted(x))
x

"""## 5.8 Sets"""

x = set([1, 2, 3, 1, 3, 5])    #A
x

x.add(6)              #C
x

x.remove(5)                    #D
x

1 in x        #E

4 in x        #E

y = set([1, 7, 8, 9])
x | y                #F

x & y                  #G

x ^ y                  #H

x = set([1, 2, 3, 1, 3, 5])
z = frozenset(x)
z

z.add(6)

x.add(z)
x

"""### Quick Check: Sets
If you were to construct a set from the following list, how many elements would the set have?: `[1, 2, 5, 1, 0, 2, 3, 1, 1, (1, 2, 3)]`

"""



"""Six unique elements: 1, 2, 5, 0, 3, and the tuple (1, 2, 3)
Lab 5: Examining a List

### Lab 5: Examining a List
In this lab, the task is to read a set of temperature data (the monthly high temperatures at Heathrow Airport for 1948 through 2016) from a file and then find some basic information: the highest and lowest temperatures, the mean (average) temperature, and the median temperature (the temperature in the middle if all the temperatures are sorted).

The temperature data is in the file lab_05.txt in the source code directory for this chapter. Because I haven't yet discussed reading files, here's the code to read the files into a list:
```
temperatures = []
with open('lab_05.txt') as infile:
     for row in infile:
        temperatures.append(float(row.strip()))
```
You should find the highest and lowest temperature, the average, and the median. You'll probably want to use the `min()`, `max()`, `sum()`, `len()`, and `sort()` functions/methods.
"""

temperatures = []

with open('lab_05.txt') as infile:
     for row in infile:
        temperatures.append(float(row.strip()))

max_temp = max(temperatures)
min_temp = min(temperatures)
mean_temp = sum(temperatures)/len(temperatures)
# we'll need to sort to get the median temp
temperatures.sort()
median_temp = temperatures[len(temperatures)//2]
print("max = {}".format(max_temp))
print("min = {}".format(min_temp))
print("mean = {}".format(mean_temp))
print("median = {}".format(median_temp))

# prompt: read a set of temperature data from a file lab05.txt and then find the
#         highest and lowest temperatures, the mean temperature, and the median temperature .

temperatures = []
with open('lab_05.txt') as infile:
     for row in infile:
        temperatures.append(float(row.strip()))

# Find the highest and lowest temperature
highest_temp = max(temperatures)
lowest_temp = min(temperatures)

# Find the mean temperature
mean_temp = sum(temperatures) / len(temperatures)

# Find the median temperature
temperatures.sort()
if len(temperatures) % 2 == 0:
    median_temp = (temperatures[len(temperatures) // 2] + temperatures[len(temperatures) // 2 - 1]) / 2
else:
    median_temp = temperatures[len(temperatures) // 2]

# Print the results
print("Highest temperature:", highest_temp)
print("Lowest temperature:", lowest_temp)
print("Mean temperature:", mean_temp)
print("Median temperature:", median_temp)

"""### Bonus
Determine how many unique temperatures are in the list.

"""



unique_temps = len(set(temperatures))

print("number of temps - {}".format(len(temperatures)))
print("number of unique temps - {}".format(unique_temps))

# prompt: Determine how many unique temperatures are in the list.

unique_temps = len(set(temperatures))

print("number of temps - {}".format(len(temperatures)))
print("number of unique temps - {}".format(unique_temps))