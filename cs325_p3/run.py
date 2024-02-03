from module_1 import add
from module_2 import subtract
from module_3 import multiply

def main():
    a = 7
    b = 5

    print(add.add(a, b))
    print(subtract.subtract(a,b))
    print(multiply.multiply(a,b))

if __name__ == "__main__":
    main()