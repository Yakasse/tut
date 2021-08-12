import sys


if __name__ == "__main__":
    selection = sys.argv[1] if len(sys.argv) > 1 else "Default"
    print("Selected : ", selection)
