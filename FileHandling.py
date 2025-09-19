file1 = open("python.txt", "r")
content = file1.read()
print("Reading a file: ", content)

file = open("python.txt", "w")
file.write("I am using python\nI am writing a code for file handling")
file.close()

file2 = open("python.txt", "r")
content = file2.read()
print("Reading a file: ", content)

f = open("python.txt", "r")
for line in f:
    print(line.strip())
f.close()

file = open("python.txt", "a")
file.write("I am writing this new line in this")
file.close()

with open("python.txt", "r") as f1:
    print(f1.read())

# writing a list of lines
lines = ["Python is easy\n", "Learning file handling\n", "Keep learning python\n"]
with open("Python.txt", "w") as file2:
    file2.writelines(lines)

# reading into a list
with open("Python.txt", "r") as fi:
    line = fi.readlines()
    print(line)




