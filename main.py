import sys
from Repository import _Repository


def main():
    rep = _Repository()
    rep.create_tables()
    rep.read_config(sys.argv[1])
    rep.read_orders(sys.argv[2])


if __name__ == '__main__':
    main()
