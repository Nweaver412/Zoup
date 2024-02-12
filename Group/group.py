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

    def abelian(): #TODO
        return

    def __repr__(self):
        return f"SymmetricGroup({self.n})"

# Broken Generate elements function. 
# TODO
class DihedralGroup: 
    def __init__(self, n):
        self.n = n
        self.elements = self.generate_elements()

    def generate_elements(self):
        rotations = [tuple(range(1, self.n + 1))]
        for i in range(1, self.n):
            rotation = tuple((j % self.n) + 1 for j in range(i, i + self.n))
            rotations.append(rotation)

        reflections = []
        for i in range(1, self.n + 1):
            reflection = tuple((i % self.n) + 1 for i in range(self.n, 0, -1))
            reflections.append(reflection)

        identity = tuple(range(1, self.n + 1))

        elements = [identity] + rotations + reflections
        return elements

    def list_elements(self):
        return self.elements
    
    def list(self):
        return self.elements

    def sign(): #TODO
        return

    def order(): #TODO
        return
    
    def abelian(): #TODO
        return

    def __repr__(self):
        return f"DihedralGroup({self.n})"
