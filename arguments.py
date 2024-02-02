import argparse

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(help = "String needed", dest="my_string", type=str)
    parser.add_argument(help = "Integer needed", dest="my_int", type=int)
    parser.add_argument(help = "Float needed", dest="my_float", type=float)
    args = parser.parse_args()

    arg1 = args.my_string
    arg2 = args.my_int
    arg3 = args.my_float

    print(arg1, arg2, arg3)

if __name__ == "__main__":
    main()




