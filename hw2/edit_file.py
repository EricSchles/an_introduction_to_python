file_handle = open("practicing_file_writing.txt", "r")

file_contents = file_handle.read()

file_handle.close()

file_contents += " Sincerely, Python"

file_handle = open("practicing_file_updating.txt", "w")

file_handle.write(file_contents)

file_handle.close()