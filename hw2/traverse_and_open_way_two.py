import os

os.chdir("to_traverse")

first_file = open("practicing_file_writing.txt", "r")
second_file = open("practicing_file_updating.txt", "r")

contents_one = first_file.read()
contents_two = second_file.read()

print("The two files are equal:")
print(contents_one == contents_two)