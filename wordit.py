
import json

def main():

    user_greetings()
    
    user_prompt = input("Choose Your Quest(Add or Remove or Search): ")
    
    global personal_dictionary
    
    personal_dictionary = load_data()
    
    while True:
        if user_prompt.lower() == "add":
            number_of_words = int(input("How many words do you want to add: "))
            for i in range(number_of_words):
                add_word()
            prompt_continue_add = input("Do you want to add any other words? (Yes/No): ")
            if prompt_continue_add.lower() == "yes":
                add_word()
                prompt_continue_add = input("Do you want to add any other words? (Yes/No): ")
            if prompt_continue_add == "No" or prompt_continue_add == "no":
                search_prompt = input("Do you want to search any words? (Yes/No): ")
                while search_prompt.lower() == "yes":
                    search_word()
                    search_prompt = input("Do you want to search any words? (Yes/No): ")
                if search_prompt.lower() == "no":
                    remove_word_prompt = input ("Do you want to remove any words? (Yes/No): ")
                    while remove_word_prompt.lower() == "yes":
                        remove_word()
                        remove_word_prompt = input ("Do you want to remove any other words? (Yes/No): ")
                    if remove_word_prompt.lower() == "no":
                        print("\nThank you for using WordIt. Here's a list of words you have learnt so far:\n")
                        for word, meaning in personal_dictionary.items():
                            print(f"{word}: {meaning}\n")
                        print("Happy Learning!")
                        break        
        elif user_prompt.lower() == "remove":
            remove_word()
            next_prompt = input("Do you want to remove another word? (Yes/No): ")
            while next_prompt.lower() == "yes":
                remove_word()
            if next_prompt.lower() == "no":
                prompt_continue_add = input("Do you want to add any other words? (Yes/No): ")
                if prompt_continue_add == "Yes" or prompt_continue_add == "yes":
                    add_word()
                    prompt_continue_add = input("Do you want to add any other words? (Yes/No): ")
                    if prompt_continue_add == "No" or prompt_continue_add == "no":
                        search_prompt = input("Do you want to search any words? (Yes/No): ")
                        while search_prompt.lower() == "yes":
                            search_word()
                            search_prompt = input("Do you want to search any words? (Yes/No): ")
                        if search_prompt.lower() == "no":
                            print("\nThank you for using WordIt. Here's a list of words you have learnt so far:\n")
                            for word, meaning in personal_dictionary.items():
                                print(f"{word}: {meaning}\n")
                            print("Happy Learning!")
                            break
        elif user_prompt.lower() == "search":
            search_word()
            next_word_prompt = input("Do you want to search for another word? (Yes/No): ")
            while next_word_prompt.lower() == "yes":
                search_word()
            if next_word_prompt.lower() == "no":
                print("Thank you for using WordIt!")
                break
        else:
            print("Invalid input! Please try again!")
            user_prompt = input("Choose Your Quest(Add or Remove or Search): ")
    
    save_data()

    

'''

The user_greetings() function is a simple function to greet
the users when they start the program.

'''

def user_greetings():

    #Welcome statement
    
    print("Welcome to WordIt, Your Personal Dictionary!\n")
    
    print(
'''WordIt is a simple vocabulary notebook, that allows you to add words along with their meanings and build your own personal dictionary. It also
allows you to remove, as well as search for words and their meanings in the dictionary. Use WordIt to level up your vocabulary building game!\n'''
    )
    


'''

The add_word() function takes a user input, and adds it to the empty dictionary. After each addition
of words, it also returns the newly added word with its meaning. The function does not take
any arguments.

'''

def add_word():
    
    word_entry = input("Enter the word: ")
    
    meaning_entry = input("Enter the meaning: ")
    
    personal_dictionary[word_entry] = meaning_entry
    
    
        
        
'''

The remove_word() function takes a user input, and removes it from the dictionary. After each removal
of words, it returns the newly removed word. The function does not take any arguments.

'''

def remove_word():
    
    word_entry = input("Enter the word: ")
    
    removed_word = personal_dictionary.pop(word_entry)
    
    print(f"The removed word is {word_entry}\n")
    
'''

The search_word() function takes a user input, and adds it and checks whether it is present in the dictionary. 
If it is, the word is returned with its meaning. If not, the user gets an error message.
The function does not take any arguments.

'''

def search_word():
    
    word_entry = input("Enter the word: ")
    while True:
        if personal_dictionary.get(word_entry) is not None:
            search_result = personal_dictionary.get(word_entry)
            print(f"The meaning of {word_entry} is {search_result}.")
            break
        else:
            print ("Word not found!")
            next_step = input("Do you want to add this missing word? (Yes or No): ")
            if next_step == "Yes" or next_step == "yes":
                main()
            else:
                print("Thank you for using WordIt.\nHappy Learning!")
                break

'''

The save_data() function saves any entries made into the dictionary variable
to a JSON file to for recording the user entries.

'''

def save_data():
    with open ("personal_dictionary.json", "w") as file:
        json.dump(personal_dictionary, file)

'''

The load_data function will allow the program to load the entries of previous
sessions in the personal_dictionary variable everytime the script is run.

'''

def load_data():
    try:
        with open("personal_dictionary.json", "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        return {}
        
            
    

if __name__ == "__main__":
    main()
