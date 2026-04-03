from component import FileSystemComponent

class Directory(FileSystemComponent):
    def __init__(self, name):
        self.name = name
        self.children = []

    def add(self, component):
        if component not in self.children:
            self.children.append(component)
        else:
            print("Бұл элемент бұрын қосылған")

    def remove(self, component):
        if component in self.children:
            self.children.remove(component)
        else:
            print("Элемент табылмады")

    def display(self, indent=0):
        print(" " * indent + f"{self.name}")
        for child in self.children:
            child.display(indent + 2)

    def get_size(self):
        total = 0
        for child in self.children:
            total += child.get_size()
        return total
