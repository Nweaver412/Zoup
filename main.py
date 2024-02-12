from Group.group import SymmetricGroup
from Group.group import DihedralGroup

if __name__ == "__main__":
    H = SymmetricGroup(3)
    G = DihedralGroup(6)

    print(G.list())

