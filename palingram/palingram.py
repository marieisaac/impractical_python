#from palindrome
import palindrome

def main():
    d = open("words.txt", "r")
    for line in d:
        s = line.strip()
        if palindrome.palindrome(s):
            print(s)

if __name__ == "__main__":
    print("from palingram")
    main()
