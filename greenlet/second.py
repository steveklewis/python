# 
# Derived from example found here:
# http://greenlet.readthedocs.org/en/latest/
#

from greenlet import greenlet

def test1(x, y):
    z = gr2.switch(x+y)
    print(z)

def test2(u):
    print(u)
    gr1.switch(42)

def main():
    global gr1, gr2
    gr1 = greenlet(test1)
    gr2 = greenlet(test2)
    gr1.switch("hello", " world")

if __name__ == "__main__":
    main()
