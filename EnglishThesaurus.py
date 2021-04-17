import json
from difflib import get_close_matches

def define(word):

    def_dict = {}
    lowercase_word = word.lower()
    noun = word.title()
    acronym = word.capitalize()

    #load the dictionary from the JSON object
    data = json.load(open("EnglishThesaurus/data.json"))

    # First check if the word exists   
    if lowercase_word in data:
        def_dict[word] = data[word]
        return def_dict

    # Then check if the word is a name of a place or so
    elif noun in data:        
        def_dict[noun] = data[noun]
        return def_dict
    
    # Then check if the word is an acronym
    elif acronym in data:
        def_dict[acronym] =  data[acronym]
        return def_dict

    # if it doesn't then check possible matches in the dictionary 
    else:
        
        try:
            # Find the best possible match for the word user entered
            possible_matches = get_close_matches(lowercase_word, data.keys(), 1, 0.8)
            if len(possible_matches) == 0:
                possible_matches = get_close_matches(noun, data.keys(), 1, 0.8)
                if len(possible_matches) == 0:
                    possible_matches = get_close_matches(acronym, data.keys(), 1, 0.8)
            
            # Prompt the user if he meant to enter this best matching word instead
            user_input = input("Did you mean to enter %s instead? (Y/N) : " % possible_matches[0])


            # If it was originally a typo and he meant to enter the best possible matching word instead:
            if user_input.upper() == "Y":
                possible_match = possible_matches[0]
                possible_match_defn = data[possible_match]
                def_dict[possible_match] = possible_match_defn
                return def_dict

            # Else if he didn't mean to enter this best matching word:    
            elif user_input.upper() == "N":
                return "The word you entered doesn't exist in our dictionary."
            
            # If the user enters something other than Y or N:
            else:
                return "Invalid input. Please enter Y or N."

        # In case no match is returned by get_close_matches()
        except IndexError:
            return "This word doesn't exist in our dictionary."

try:
    word = input("Enter the word to search : ")

        # returnedVal can be a string msg if word not found or it can be a dictionary of the word/best match and its definition
    returnedVal = define(word)

    if isinstance(returnedVal, dict):          
        for key, def_list in returnedVal.items():
            print(key,":",sep=" ", end="\n")

            #the definitions for a word in the JSON file are in the form of a list
            for definition in def_list:
                print("---", definition, end="\n")

    elif isinstance(returnedVal, str):
        print(returnedVal)

except Exception as ex:
    print(ex.args)
