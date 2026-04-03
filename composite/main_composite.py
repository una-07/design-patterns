from file import File
from directory import Directory

root = Directory("Root")

file1 = File("file1.txt", 10)
file2 = File("file2.txt", 20)

folder1 = Directory("Folder1")
folder2 = Directory("Folder2")

folder1.add(file1)
folder2.add(file2)

root.add(folder1)
root.add(folder2)

root.display()

print("\nЖалпы өлшем:", root.get_size(), "KB")
