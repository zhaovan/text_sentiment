import sys
# print sys.argv[0] prints test.py
# print sys.argv[1] prints your_var_1

def hello(word):
    print ("Hi")
    sys.stdout.flush()

if __name__ == "__main__":
    hello()
