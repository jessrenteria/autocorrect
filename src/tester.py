import argparse

from autocorrect import Autocorrecter

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("dict_file", type=str)
    args = parser.parse_args()
    print("Creating dictionary...")
    ac = Autocorrecter(args.dict_file)
    print("Dictionary created! Please enter a word.")
    print("If the word is valid nothing will be printed,")
    print("otherwise a list of corrections will be suggested.")

    while True:
        print("> ", end="")
        word = input()
        if word == 'q':
            print("Bye!")
            return
        ac.correct(word)

if __name__=="__main__":
    main()
