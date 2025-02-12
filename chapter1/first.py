# # modules is a file conataning python code by some one else which can impote and used our program

# # this is pyhon pyjokes module which is used to get jokes

# # two types of modules inpython

# # 1. built in modules(pre-installes moduels in python) 
# # 2. external modules(we need to install these modules)














 
# pyjokes module is used to get jokes in python  (external module)  (pip install pyjokes)  

import pyjokes

jokes = pyjokes.get_joke()

print(jokes)



























# PIP is the packege manager for python whhich is used to install mudules and packeges in pthon

# pip install pyjokes we used this command to install pyjoke module

# modules is a file conataning python code by some one else which can impote and used our program


# # print("Hello, World!")

# #we used "#"" to write single line comment
# # print("hello world") 

  



 
# # we usedd triple quite to write multi line comment
# """ hi my neme is abdullah 
#  what is your NameError
#  i am larning python form harrty """






# # PRACTICE SET



# # Program to print "Twinkle, Twinkle, Little Star" poem

# # print('''Twinkle, twinkle, little star

# # How I wonder what you are

# # Up above the world so high

# # Like a diamond in the sky

# # Twinkle, twinkle little star

# # How I wonder what you are

# # When the blazing sun is gone

# # When he nothing shines upon

# # Then you show your little light

# # Twinkle, twinkle, all the night

# # Twinkle, twinkle, little star

# # How I wonder what you are''')


# 2. #print REPL and print the table of 5 using it 


# # print('5 x 1 =', 5 * 1)
# # print('5 x 2 =', 5 * 2)
# # print('5 x 3 =', 5 * 3)
# # print('5 x 4 =', 5 * 4)
# # print('5 x 5 =', 5 * 5)
# # print('5 x 6 =', 5 * 6)
# # print('5 x 7 =', 5 * 7)
# # print('5 x 8 =', 5 * 8)
# # print('5 x 9 =', 5 * 9)
# # print('5 x 10 =', 5 * 10)




















# 3. install external module and perfoem operation in your intrest  (pyttsx3)  (text to speech) 

# pyttsx3 is a text-to-speech conversion library in Python. Unlike alternative libraries, it works offline, and is compatible with both Python 2 and 3. The library is cross-platform and plays nicely with other Python packages. It is very easy to use and supports several languages.


# import pyttsx3

# engine = pyttsx3.init()

# engine.say("hey how are you?")

# engine.runAndWait()






























# # 4. write a python program to print the content of directory using os module
 

 
# import os

# # Specify the directory path
# directory_path = input("/")

# # Check if the directory exists
# if os.path.exists(directory_path) and os.path.isdir(directory_path):
#     # Get the list of files and folders in the specified directory
#     directory_contents = os.listdir(directory_path)

#     # Print the contents of the directory
#     print(f"Contents of the directory '{directory_path}':")
#     for item in directory_contents:
#         print(item)
# else:
#     print(f"The directory '{directory_path}' does not exist.")
 