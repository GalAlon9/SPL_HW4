import sys
from Repository import _Repository

if __name__ == '__main__':
    rep = _Repository(sys.argv[4])
    rep.create_tables()
    rep.read_config(sys.argv[1])
    rep.read_orders(sys.argv[2], sys.argv[3])



