import argparse
import numpy as np


def main(documentsTxt):
    documents = documentsTxt.strip().split('\n')
    unique_words = set()
    for doc in documents:
        unique_words.update(set(doc.lower().split()))

    word_to_index = {word: i for i, word in enumerate(sorted(unique_words))}
    n_docs = len(documents)
    n_words = len(unique_words)
    final_matrix = [[0]*n_words for i in range(n_docs)]

    for i, doc in enumerate(documents):
        for word in doc.lower().split():
            final_matrix[i][word_to_index[word]] += 1
    print('# Features:')
    for row in final_matrix:
        print(row)



if __name__ == "__main__":
    parser = argparse.ArgumentParser("One Hot Encoder")
    parser.add_argument("--fpath", type=str, help="Name of the txt file to be read in")
    args = parser.parse_args()
    main(open(args.fpath).read())