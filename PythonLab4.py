import argparse as ap

def main(array):
    empirical_mean = sum(array)/len(array)
    empirical_variance = sum((i - empirical_mean)**2 for i in array)/len(array)
    print(f'mean = {empirical_mean}')
    print(f'variance = {empirical_variance}')
    # Write the compute the variance and the mean of a given list of numbers
    # Make sure that your terminal output matches the terminal output of the example given on the instructions.


if __name__ == "__main__":
    argParse = ap.ArgumentParser("Variance and Mean Calculator")
    argParse.add_argument("--array", nargs="+", type=int, help="Input a list of numbers to compute the variance and mean of")
    parsedArgs = argParse.parse_args()
    main(parsedArgs.array)