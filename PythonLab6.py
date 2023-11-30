import argparse


def main(number):
    number_list = []
    for i in iter(str(number)):
        number_list.append(i)
    reversed_list = number_list[::-1]
    if reversed_list == number_list:
        print(True)
    else:
        print(False)




    # Write the code to determine whether or not a number is a pallindrome here.
    # Make sure that your terminal output matches the terminal output of the example given on the instructions.



if __name__ == "__main__":
    arg = argparse.ArgumentParser("Pallindrome Checker")
    arg.add_argument("--x", type=int, help="Input a number to determine if it's a pallindrome")
    parsed = arg.parse_args()
    main(parsed.x)