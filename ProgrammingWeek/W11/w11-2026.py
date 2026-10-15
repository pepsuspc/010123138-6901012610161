# w11 : Python (text mode)
# built-in class File (object + method), os module : path, directory, file size
import os

f = open("output.txt", "w")  # f is an object
f.write("Hello, everybody")  # write() is a method
f.close()                    # do not forget to close the file

print(os.getcwd())   # current working directory
print(os.listdir())  # list of files and directories in cwd

print(os.path.exists("output.txt"))  # the path exists?
print(os.path.isfile("output.txt"))  # is it a file?
print(os.path.isdir("output.txt"))   # is it a directory?

file_size = os.path.getsize("output.txt")
print("File Size is :", file_size, "bytes")
