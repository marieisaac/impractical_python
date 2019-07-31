#from palindrome
import palindrome

def main():
    d = open("words.txt", "r")
    wrds = []
    for line in d:
        wrd = line.strip()
        wrds.append(wrd)
    for array_variable1 in wrds:
        for array_variable2 in wrds:
            phrase = array_variable1 + " " + array_variable2
            if palingram(phrase):
                print(phrase)

# def ifWeDidntUseAnArray():
#     d = open("words.txt", "r")
#     for array_variable_temp1 in d:
#         array_variable1 = array_variable_temp1.strip()
#         e = open("words.txt", "r")
#         for array_variable_temp2 in e:
#             array_variable2 = array_variable_temp2.strip()
#             if palingram(array_variable1 + " " + array_variable2):
#                 print(array_variable1 + " " + array_variable2)



def palingram(sentence):
    replaced = sentence.replace(" ", "")
    return palindrome.palindrome(replaced)

if __name__ == "__main__":
    main()
