from graph.graph import SymmetricGroup
from graph.graph import DihedralGroup

if __name__ == "__main__":
    symmetric_group_3 = SymmetricGroup(3)
    dihedral_group_4 = DihedralGroup(4)

    print("Symmetric Group S_3:", symmetric_group_3.list())
    print("Dihedral Group D_4:", dihedral_group_4.list())
