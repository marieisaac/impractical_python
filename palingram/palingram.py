#from palindrome
import palindrome

def main():
    # d = open("words.txt", "r")
    # for line in d:
    #     s = line.strip()
    #     if palindrome.palindrome(s):
    #         print(s)

    dictionary = [
        "taco cat",
        "nurses run",
        "rat tar",
        "logan murphy",
        "marine isaac",
        "liz isaac"
    ]
    for phrase in dictionary:
        if palingram(phrase):
            print(phrase)

def palingram(sentence):
    replaced = sentence.replace(" ", "")
    return palindrome.palindrome(replaced)

if __name__ == "__main__":
    main()
