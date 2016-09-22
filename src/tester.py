import argparse

from autocorrect import Autocorrecter

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("dict_file", type=str)
    args = parser.parse_args()
    ac = Autocorrecter(args.dict_file)

    while True:
        word = input()
        if word == 'q':
            print("Bye!")
            return
        ac.correct(word)

if __name__=="__main__":
    main()
