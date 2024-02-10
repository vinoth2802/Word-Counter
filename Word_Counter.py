#This Program is for Word Counter
#Created by Vinothkumar J


def count_word(input_string):

    #Check for empty string
    try:
        if len(input_string)==0:
            raise Exception("Empty string is entered.")
    except Exception as e:
        print(e)

    #Remove leading and trailing whitespace
    #Change the string to lower case
    formatted_string=input_string.strip().lower()

    #split the string into words
    words=formatted_string.split()

    #Filter the numerical strings out of the words list
    formatted_words=[]
    for word in words:
        if  word.isalpha():
            formatted_words.append(word)

    return  len(formatted_words)

input_string=input("Enter the String :")
print("Word Count : ",count_word(input_string))