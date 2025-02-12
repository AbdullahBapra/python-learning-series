
# strinf function in python are used to manipulate strings. Some of the string functions are:

# 1. len() : len() function is used to get the length of a string. It returns the number of characters in a string.


name = 'abdullah faheem bapras'

print(len(name)) # 21


# 2. lower() : lower() function is used to convert all the characters of a string to lowercase.


print(name.lower()) # abdullah faheem bapras



# 3. upper() : upper() function is used to convert all the characters of a string to uppercase.


print(name.upper()) # ABDULLAH FAHEEM BAPRAS


# 4. title() : title() function is used to convert the first character of each word to uppercase and the rest of the characters to lowercase.



print(name.title()) # Abdullah Faheem Bapras



# 5. capitalize() : capitalize() function is used to convert the first character of a string to uppercase and the rest of the characters to lowercase.


print(name.capitalize()) # Abdullah faheem bapras


# 6. count() : count() function is used to count the number of occurrences of a substring in a string. It takes a substring as an argument and returns the number of occurrences of that substring in the string.


print(name.count('a')) # 5



# 7. find() : find() function is used to find the index of the first occurrence of a substring in a string. It takes a substring as an argument and returns the index of the first occurrence of that substring in the string. If the substring is not found in the string, it returns -1.


print(name.find('a')) # 0


# 8. replace() : replace() function is used to replace a substring with another substring in a string. It takes two arguments, the substring to be replaced and the substring to replace it with.



print(name.replace('a', 'A')) # AbdullAh fAheem bAprAs



# 9. split() : split() function is used to split a string into a list of substrings. It takes a delimiter as an argument and splits the string at each occurrence of the delimiter. If no delimiter is specified, it splits the string at whitespace characters.



print(name.split()) # ['abdullah', 'faheem', 'bapras']


# 10. replace() : replace() function is used to replace a substring with another substring in a string. It takes two arguments, the substring to be replaced and the substring to replace it with.



print(name.replace('a', 'A')) # AbdullAh fAheem bAprAs


# 11. strip() : strip() function is used to remove leading and trailing whitespace characters from a string.


name = '   abdullah faheem bapras   '

print(name.strip()) # abdullah faheem bapras



# 12. lstrip() : lstrip() function is used to remove leading whitespace characters from a string.


print(name.lstrip()) # abdullah faheem bapras


# 13. startswith() : startswith() function is used to check if a string starts with a specified substring. It takes a substring as an argument and returns True if the string starts with that substring, otherwise it returns False.


print(name.startswith('a')) # False



# 14. endswith() : endswith() function is used to check if a string ends with a specified substring. It takes a substring as an argument and returns True if the string ends with that substring, otherwise it returns False.



print(name.endswith('s')) # True