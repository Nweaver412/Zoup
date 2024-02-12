"""
Initializing data types for most common group types


"""
from itertools import permutations

class SymmetricGroup:
    def __init__(self, n):
        self.n = n
        self.elements = list(permutations(range(1, n + 1)))

    def list(self):
        return self.elements

    def sign(): #TODO
        return
    
    def order(): #TODO
        return

    def __repr__(self):
        return f"SymmetricGroup({self.n})"

class DihedralGroup:
    def __init__(self, n):
        self.n = n
        self.elements = [f"r{i}" for i in range(n)] + [f"s{i}" for i in range(n)]
    
    def list(self):
        return self.elements

    def sign(): #TODO
        return

    def order(): #TODO
        return

    def __repr__(self):
        return f"DihedralGroup({self.n})"
