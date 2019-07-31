from math import ceil
#strings are a bunch of characters
#array is a bunch of things (string is an array too!)

def palindrome(wrd):
    for i in range(int(ceil(len(wrd)/2))):
        left = wrd[i]
        right = wrd[len(wrd)-i-1]
        if (left != right):
            return False
        #print(("\t") + str(i) + " : " + left + ", " + right)
    return True


def main():
    d = open("words.txt", "r")
    for line in d:
        s = line.strip()
        if palindrome(s):
            print(s)

if __name__ == "__main__":
    main()

# def palindromeWRONG(wrd):
#     #wrd=apple
#     for i in range(len(wrd)):
#         #i=0
#         left = wrd[i]
#         #left=a
#         right = wrd[len(wrd)-i-1]
#         #right=e
#         if (left == right):
#             return True
#             #print(("\t") + str(i) + " : " + left + ", " + right)
#     return False
