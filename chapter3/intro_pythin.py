# strying is a datatype in python which is a sequence of characters. It is used to store text data. Strings are immutable in python. Strings are enclosed in single quotes or double quotes.


# we can create string in 3 ways:
# 1. Single quotes ''
# 2. Double quotes ""
# 3. Triple quotes ''' ''' or """ """ is used to create multiline line strings.


name = 'abdullah faheem bapras'

print(name)


name = "abdullah faheem bapras"

print(name)


name_intro = '''My name is Abdullah Faheem Bapras. 
I am a student of computer science.
I am learning python programming language.'''

print(name_intro)



# Accessing characters in a string


# we can access characters in a string using index. Index starts from 0. We can also use negative index to access characters from the end of the string.



name = 'abdullah faheem bapras'

print(name[0]) # a


# slicing in a string is used to access a range of characters in a string. We can use slicing to access a range of characters in a string. Slicing is done by using colon :. We can also use negative index in slicing.


print(name[1:5]) # bdul 1 to 4 index characters are printed bdul  (5 is not included)  


# we also use negative index in slicing. Negative index starts from -1. -1 is the last character of the string. -2 is the second last character of the string and so on.

print(name[-1]) # s last character of the string is printed s

print(name[-5:-1]) # bapr 5th to 2nd last characters are printed bapr (1st last is not included)


print(name[5:]) # hullah faheem bapras 5th index to last characters are printed hullah faheem bapras (5th index is included)
print(name[:5]) # abdul 0 to 4 index characters are printed abdul (5th index is not included) 



# slicing with skip value

# we can provide a skip value are part of slicing like this

print(name[0:10:2]) # adua 0 to 9 index characters are printed with a skip value of 2 adua (10th index is not included) 


# we can also use negative skip value in slicing


print(name[10:0:-2]) # aua 10 to 1 index characters are printed with a negative skip value of 2 aua (0th index is not included)


# we can also use negative index in slicing with negative skip value


print(name[-1:-10:-2]) # srpem 1 to 10 index characters are printed with a negative skip value of 2 srpem (-10th index is not included)