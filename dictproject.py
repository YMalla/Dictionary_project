#TODO: bring dictionary.json into a dictionary data structure
import json
import difflib

dictfile = open("dictionary.json")
database = json.load(dictfile)
dictfile.close()

#TODO: define function to provide definition of input word
def print_definition(inputword):
    inputword = inputword.lower()
    if inputword in database:
        print(database[inputword])
    else:
        print("not available")
        closewords = difflib.get_close_matches(inputword, database)
        if len(closewords):
            print("Did you mean: " + str(closewords) + "?")
        else:
            print("No close matches")
while True:
    #TODO: Have a user input the word to be defined
    myword = input("enter a word or type X to quit: ")
    
    if myword.upper() == "X" :
        break
    
    #TODO: print the definition of myword
    print_definition(myword)


