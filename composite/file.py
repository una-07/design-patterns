from component import FileSystemComponent

class File(FileSystemComponent):
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def display(self, indent=0):
        print(" " * indent + f"📄 {self.name} ({self.size} KB)")

    def get_size(self):
        return self.size
