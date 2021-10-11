# Drafts from the Monday week 4 Q&A session.
# ---

# a = 6

# What we did in the Week 3 workshop
# if a > 5:
#     raise ValueError('a is too large!')

# Bonus tip: catching errors (not part of the syllabus!)
try:
    # do something
except:
    # if the bit in "try" produces a runtime error
  
  
  
# ---
# Example of catching an error
    
my_string = 'Hello!'

try:
    # Extract the 10th character of my_string
    print(my_string[9])
except:
    my_string *= 2
    print(my_string)
    # print('Oh no, that failed! :(')


# ---
# A fancy way to catch errors: Practice W3, question 1
s1 = '4'
s2 = '2'
f1 = 4.0
f2 = 2.0
i1 = 4
i2 = 2

operation = 's1 / f2'
print(operation)
eval(operation)


# Put all operations in a list, as *strings*
operations = ['...', '...', ...]

# Use eval() to try all of them, print('error')
# if they don't work
for op in operations:
    try:
        eval(op)
    except:
        print('error')

# try:
#     print(s1 / f2)
# except:
#     print('error')
    



# ---
# How input() works in VSCode

# age = int(input("What is your age? "))
# print(age)