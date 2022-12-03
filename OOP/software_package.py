# COMPOSITION | WEEK 5

# Say we have a package class that represents a software package which could be installed on every machine on our network. This class has a lot of information on the software, like the name, the version, the size, and more. We also have a repository class that represents all the packages that we have available for installation internally. In this class, we want to know how many packages there are and what's the total size of all the packages.

class Repository:
    def __init__(self):
        self.packages = {}
    def add_package(self, package):
        self.packages[package.name] = package
    def total_size(self):
        result = 0
        for package in self.packages.values():
            result += package.size
        return result