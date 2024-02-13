"""
Initializing data types for most common group types

"""
from itertools import permutations
import math

from itertools import permutations

class SymmetricGroup:
    def __init__(self, n):
        self.n = n
        self.elements = list(permutations(range(1, n + 1)))
        self.elements_by_cycles = [(perm, self.cycle_notation(perm)) for perm in self.elements]

    def list(self):
        """
        Return list of groups within a group.

        Returns:
        - List of groups.
        """
        return self.elements

    def parse_cycle_notation(self, cycle_notation):
        """
        Parse a cycle notation string into a tuple representing the permutation.

        Parameters:
        - cycle_notation (str): A cycle notation string.

        Returns:
        - tuple: A tuple representing the permutation.
        """
        cycles = cycle_notation.split(" ")
        perm = []
        for cycle in cycles:
            cycle = cycle.strip('()')
            elements = list(map(int, cycle.split(',')))
            perm.extend(elements)
        return tuple(perm)

    def cycle_notation(self, perm):
        """
        Convert a permutation tuple into a cycle notation string.

        Parameters:
        - perm (tuple): A permutation represented as a tuple.

        Returns:
        - str: A cycle notation string.
        """
        cycles = []
        visited = set()
        for i in perm:
            if i not in visited:
                cycle = [i]
                visited.add(i)
                next_element = perm[i - 1]
                while next_element != i:
                    cycle.append(next_element)
                    visited.add(next_element)
                    next_element = perm[next_element - 1]
                cycles.append(tuple(cycle))
        return " ".join([f"({','.join(map(str, cycle))})" for cycle in cycles])

    def _count_transpositions(self, perm_list):
        """
        Count the number of transpositions in a permutation.

        Parameters:
        - perm_list (list): A list representation of a permutation.

        Returns:
        - int: The number of transpositions.
        """
        transpositions = 0
        for i in range(self.n - 1):
            if perm_list[i] > perm_list[i + 1]:
                perm_list[i], perm_list[i + 1] = perm_list[i + 1], perm_list[i]
                transpositions += 1
        return transpositions

    def sign(self, perm):
        """
        Calculate the sign of a permutation.

        Parameters:
        - perm (tuple): A permutation represented as a tuple.

        Returns:
        - int: 1 if the sign is positive, -1 if the sign is negative.
        """
        perm_list = list(perm)
        transpositions = self._count_transpositions(perm_list)
        return 1 if transpositions % 2 == 0 else -1

    def order(self, perm):
        """
        Calculate the order (factorial) of the size of the group.
        Utilizes a loop for values not in the precomputed dictionary.

        Parameters:
        - perm (tuple): A permutation represented as a tuple.

        Returns:
        - int: The factorial of the size of the group.
        """
        val = self.n
        if val <= 10:
            fac = {1: 1, 2: 2, 3: 6, 4: 24, 5: 120, 6: 720, 7: 5040, 8: 40320, 9: 362880, 10: 3628800}
            return fac[val]
        else:
            result = 1
            transpositions = self._count_transpositions(list(perm))
            for i in range(2, val + 1):
                result *= i
            return result

    def abelian(self, perm):
        """
        Check to see if not empty or singleton set, thus determining
        if is abelian.

        Parameters:
        - perm (tuple): A permutation represented as a tuple.

        Returns:
        - Bool: True if Abelian, False if not.
        """
        val = self.n
        return True if val >= 2 else False

    def __repr__(self):
        return f"SymmetricGroup({self.n})"



class CyclicGroup: # TODO

    def sign(): #TODO
        return
    
    def order(): #TODO
        return

    def abelian(): #TODO
        return

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
