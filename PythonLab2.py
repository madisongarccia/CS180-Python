import json
import string
import argparse
import os

def main(inputString):
    special_characters = ['!','#','$','%','&','?','.',',']
    for i in special_characters:
        inputString = inputString.replace(i,'')
    all_lower = inputString.lower()
    splitWords = all_lower.split(' ')
    store_dict = {}
    count = 1
    for i in splitWords:
        if i in store_dict:
            count += 1
            store_dict[i] = count
        else:
            count = 1
            store_dict[i] = count
    print(store_dict)
    

    # Write the code to count the number of words here
    # Remember to save the dictionary as a json file named "word-counts.json"


    return None

if __name__ == "__main__":
    parser = argparse.ArgumentParser("Word Counter")
    parser.add_argument("-s","--string",type=str,required=True, help="Sentence to have the number of words counted")
    args = parser.parse_args()
    main(args.string)