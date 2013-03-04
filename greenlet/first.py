# 
# Derived from example found here:
# http://greenlet.readthedocs.org/en/latest/
#

from greenlet import greenlet

def test1():
    print(12)
    gr2.switch()
    print(34)

def test2():
    print(56)
    gr1.switch()
    print(78)

def main():
    global gr1, gr2
    gr1 = greenlet(test1)
    gr2 = greenlet(test2)
    gr1.switch()

if __name__ == "__main__":
    main()
