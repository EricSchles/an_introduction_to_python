import os
from glob import glob

os.chdir("to_traverse")

files = glob("*.txt")

first_file = open(files[0], "r")
second_file = open(files[1], "r")

contents_one = first_file.read()
contents_two = second_file.read()

print("The two files are equal:")
print(contents_one == contents_two)