import sys

if __name__ == "__main__":
    word = sys.argv[1]

    if word == word[::-1]:
        print("Palindrome")
    else:
        print("Not Palindrome")