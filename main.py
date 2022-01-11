import sys
from Repository import rep

if __name__ == '__main__':
    rep.create_tables()
    rep.read_config(sys.argv[1])
    rep.read_orders(sys.argv[2] , sys.argv[3])



