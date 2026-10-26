with open("example.txt","r") as file:
   print("--read all--")
   content = file.read()
   print(content) 

with open("example.txt","r") as file:
   print("--line by line--")
   print(file.readline())
   print(file.readline())

with open("example.txt","r") as file:
    print(file.readlines())

with open("example.txt","r") as file:
    lines = file.readlines()
    for line in lines:
        print(line)

with open("example.txt","w") as file:
    file.write("Weclome to Python in CACTS")

with open("example.txt","w") as file:
    file.writelines(["Weclome to Python in CACTS Again","\ngood evening"])

with open("example.txt","a") as file:
    file.write("\nWeclome to Python in CACTS Append")


data = {
    "name": "Test",
    "age": 21,
    "course": "Python"
}

import json
with open("data.json", "w") as file:
    json.dump(data, file, indent=4)

with open("data.json", "r") as file:
    data = json.load(file)
    print(data)
    print(data["course"])

try:
    with open("../data.txt","r") as file:
        print(file.read())
except FileNotFoundError:
    print("File not found!")

import glob
files = glob.glob("example*")
print(files)

files = glob.glob("**/*.py", recursive=True)
print(files)

for file in glob.iglob("*.py"):
    print(file)
