# This file contain string notes and example
# String : Sequence of characters with single/double quotes
# In python char data type is not there ,even single char is considered as string only

# To define multiple line string literal ,then we should use triple quotes
# For ex: Print "'" single quote in your string statement
"""--------------------------------------------------------------------------------------------------- """
# 1st way :
"""s = 'This is ' symbol'
print(s)"""
# output : ERROR!
# Traceback (most recent call last):
#   File "<main.py>", line 1
#     s = 'This is ' symbol'
#                          ^
# SyntaxError: unterminated string literal (detected at line 1)

# 2nd way
"""
To print "'" single quote within single quotes only
s = 'This is \' symbol' 
print(s) """
# OUTPUT:This is ' symbol

# 3rd way:

"""
To print "'" single quote within single quotes only
s = '''This is ' symbol'''
print(s) """
# OUTPUT:This is ' symbol
"""--------------------------------------------------------------------------------------------------- """
# For ex 2:

# 1st way:
# Expected string - This "Python" is a very easy to 'learn'
"""s = "This \"Python\" is very easy to \'learn\'"
print(s)"""
# output :  This "Python" is a very easy to 'learn'

# 2nd way:Use triple double quotes
# s = """This "Python" is very easy to 'learn'"""
# print(s)
# output :  This "Python" is a very easy to 'learn'

"""--------------------------------------------------------------------------------------------------- """

# Accessing the char in string:
# there are ways : Using index or using slice
# ex : s = "Kavya"
# s[0] = K
# s[-1] = a
# s[100] = "Index out of range
"""-------------------------------------------------------------------------------------------------"""
# ex2:
# To print positive index and negative index
"""s = input("Enter some string ")
# -5 -4 -3 -2 -1
# K a v y a
# 0 1 2 3 4
i = 0
for ch in s:
    print ("For char {} the positive index is {} and the negative index is {} ".format (ch,i,i-len(s)))
    # i prints positive index
    # i-len(s) print negative index
    i+=1
"""
"""----------------------------------------------------------------------------------------------------------------"""
# Slice operation in string
# syntax : string[start index: end index: step increment]
# step increment default is 1
# Ex 1: s = "abcdefghi"
# If step value is +ve move to forward direction (begin to end-1)
# If step value is -ve move backward direction (begin to end +1)
# In forward direction if end value is 0 then result is always empty
# In backward direction if end value is -1 the result is always empty
# Default value of begin in forward direction is 0 and end is len(string)
# Default value of begin in backward direction is -1 and end is -(len(s)+1)
"""----------------------------------------------------------------------------------------------------------------"""
"""Count() :
syntax - string.count(substring, start, end)

Parameters:
substring: The string you want to count
start (optional): Index to start from
end (optional): Index to stop before

What it does
Counts how many times the substring appears in the given range of the string.
Returns an integer. """

"""
# Ex1: count "na" in "banana"
# 0 1 2 3 4 5
# b a n a n a
s = "banana"
scount = s.count("na") # if start and end index is not specified it counts till end of string
print(f"substring appears {scount} times") # output = 2

s1 =s.count("na",1,5) # with start index and end index
print(f"substring appears {s1} times")

# Ex2 count single char
# h e l l o w o r l d
# 0 1 2 3 4 5 6 7 8 9
l1 = "hello world"
lcount = l1.count("l")
print(f"substring appears {lcount} times")

# Ex3 list count
l2 = [1,2,3,4,2,2,2,2]
l3=l2.count(2)
print(f"substring appears {l3} times")
"""

#Replace():

"""
syntax : string.replace(old, new, count)
| Parameter            | Description                                             |
| -------------------- | ------------------------------------------------------- |
| `old`                | The substring you want to replace                       |
| `new`                | The substring to replace it with                        |
| `count` *(optional)* | The maximum number of replacements (from left to right) |
"""

"""
s = "banana"
print(s.replace("na", "XY"))

# Replace the first occurence
s = "banana"
print(s.replace("na", "XY",1))

# Replace a word in sentence
text = "I love apples. Apples are tasty."
print(text.replace("apples", "oranges"))

"""

"""Strings in Python are immutable → replace() returns a new string, it does not change the original.
The replacement happens from left to right.
It is case-sensitive."""

# split()
"""
it's essential for breaking strings into parts (often used in text processing, CSV parsing, etc.).
syntax :string.split(separator, maxsplit)
Returns A list of strings
| Parameter                | Description                                                             |
| ------------------------ | ----------------------------------------------------------------------- |
| `separator` *(optional)* | The delimiter (what to split on). Default is **any whitespace**.        |
| `maxsplit` *(optional)*  | The maximum number of splits. Remaining string goes into the last item. |
"""
"""
s = "Python is awesome"
print(s.split())

# split specific char
s = "apple,banana,grape"
print(s.split(","))

# split by space
s = "Python is awesome"
print(s.split(" ", 1))

# split by newline
s = "line1\nline2\nline3"
print(s.split("\n"))

# use split to process input
s = input("Enter comma-separated values: ")  # e.g., "10,20,30"
values = s.split(",")
print(values)
"""

"""
# join() - Joines the elements of the string
syntax: separator.join(iterable)

separator: The string used to join the items (like a space, comma, etc.)
iterable: A list (or other iterable) of strings

Returns: A single string where the elements are joined using the separator.

imp: All elements in the list must be strings. If not, you'll get a TypeError.

join vs split:
| Purpose      | Method    | Example                     | Result            |
| ------------ | --------- | --------------------------- | ----------------- |
| Split string | `split()` | `"a,b,c".split(",")`        | `['a', 'b', 'c']` |
| Join strings | `join()`  | `",".join(['a', 'b', 'c'])` | `'a,b,c'`         |

"""
"""
# join with spaces
words = ["Python", "is", "fun"]
result = " ".join(words)
print(result)

# join with commas
items = ["apple", "banana", "cherry"]
print(",".join(items))

# join with hypens
print("-".join(["2025", "05", "23"]))

#join with string
print(".".join("ABC"))

"""

"""Case of strings
Python handles the case (uppercase/lowercase) of strings. 
Python provides several built-in string methods to change or check the case of characters in a string.

# lower() - converts all cases to lower
s = "HeLLo"
print(s.lower())   # Output: "hello"

#upper() - Converts all characters in the string to uppercase.
s = "HeLLo"
print(s.upper())   # Output: "HELLO"

#.capitalize() -Capitalizes only the first character and lowers the rest.
s = "python is cool"
print(s.capitalize())   # Output: "Python is cool"

#.title() -Capitalizes the first letter of each word.
s = "python is cool"
print(s.title())   # Output: "Python Is Cool"

# .swapcase() -Swaps the case of each letter — lower becomes upper, and upper becomes lower.
s = "PyTHon"
print(s.swapcase())   # Output: "pYthON"

# .islower() - Checks if all letters are lowercase.
s = "hello"
print(s.islower())   # Output: True

#.isupper() Checks if all letters are uppercase
s = "HELLO"
print(s.isupper())   # Output: True

# .istitle() Checks if the string is in title case (first letter of each word is capitalized).
s = "Hello World"
print(s.istitle())   # Output: True
"""

# checking the start and end of the string  startswith and endswith,returns true or false
# syntax : s.startswith()
# syntax : s.endswith()

# common char type in python
"""
| Method       | Description                                        | Example                       |
| ------------ | -------------------------------------------------- | ----------------------------- |
| `.isalpha()` | Checks if all characters are **letters**           | `"abc".isalpha()` → ✅         |
| `.isdigit()` | Checks if all characters are **digits**            | `"123".isdigit()` → ✅         |
| `.isalnum()` | Checks if all characters are **letters or digits** | `"abc123".isalnum()` → ✅      |
| `.isspace()` | Checks if all characters are **whitespace**        | `"   ".isspace()` → ✅         |
| `.isupper()` | Checks if all letters are **uppercase**            | `"HELLO".isupper()` → ✅       |
| `.islower()` | Checks if all letters are **lowercase**            | `"hello".islower()` → ✅       |
| `.istitle()` | Checks if string is in **title case**              | `"Hello World".istitle()` → ✅ |

"""
"""
# example program
s = "A1 b$"

for ch in s:
    if ch.isalpha():
        print(f"'{ch}' is a letter.")
    elif ch.isdigit():
        print(f"'{ch}' is a digit.")
    elif ch.isspace():
        print(f"'{ch}' is a space.")
    else:
        print(f"'{ch}' is a special character.")
#Usecase :
"""
"""
Validating passwords (check for letters, numbers, symbols)

Filtering out unwanted characters

Tokenizing and parsing text

Creating custom input rules
"""

# format() Python — it's used to insert variables into strings in a clean, flexible, and readable way.
# syntax :"template string {}".format(value) - You use {} as placeholders in the string, and format() fills them in.

""""
#  using single values
name = "Alice"
print("Hello, {}!".format(name))

# using multiple values
name = "Alice"
age = 25
print("Name: {}, Age: {}".format(name, age))

# using positional arguments
print("Second: {1}, First: {0}".format("apple", "banana"))

"""
"""
| Feature             | Example                         | Output          |
| ------------------- | ------------------------------- | --------------- |
| Insert variable     | `"Hello {}".format("World")`    | `"Hello World"` |
| Positional indexing | `"{1} {0}".format("a", "b")`    | `"b a"`         |
| Named arguments     | `"{name}".format(name="Alice")` | `"Alice"`       |
| Number formatting   | `"%.2f" → {:.2f}`               | `"3.14"`        |
| Text alignment      | `"{:<10}".format("Hi")`         | `"Hi        "`  |
"""



