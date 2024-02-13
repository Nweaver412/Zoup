from Group.group import SymmetricGroup
from Group.group import DihedralGroup

if __name__ == "__main__":
    G = SymmetricGroup(5)
    sigma = G.parse_cycle_notation("(1,3) (2,5,4)")
    order_sigma = G.order(sigma)
    print(G.sign(sigma))
    print(order_sigma)
 