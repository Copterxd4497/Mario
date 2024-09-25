def print_space(length):
    print(" " * length, end="")

def print_row(length):
    print("#" * length, end="")

def main():
    while True:
        try:
            height = int(input("Height: "))
            if 1 <= height <= 8:
                break
            else:
                print("Height must be between 1 and 8.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

    for i in range(1, height + 1):
        print_space(height - i)
        print_row(i)
        print_space(2)
        print_row(i)
        print()

if __name__ == "__main__":
    main()
