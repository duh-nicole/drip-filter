"""
This is the main function to run drip-filter data filtering app by SoftStack Studios
Can file load, cute menu display, basic filter, save data
"""

import json
import os
from user import User

def get_integer_input(prompt, min_val=None):
    """
    check for validating integer input from user
    """
    while True:
        try:
            value = int(input(prompt))
            if min_val is not None and value < min_val:
                print(f"Jinkies! 😱 Value cannot be less than {min_val}!")
                continue
            return value
        except ValueError:
            print("Zoinks! 👻  Invalid input. Please enter a valid integer.")

def load_users_from_json(file_name):
    """
    loads data from json file and converts to user object
    """
    if not os.path.exists(file_name):
        print("Whoopsydaisy🌼! File was not found.")
        return None
    try:
        with open(file_name, 'r') as file:
            data = json.load(file)
            # conversion
            users = [User(d['id'], d['first_name'], d['last_name'], d['age'], d['city'], d['phone_number']) for d in
                     data]
            return users
    except json.JSONDecodeError:
        print(f"Eeks! 👻 Error: Invalid JSON format in file {file_name}.")
        return None
    except KeyError:
        print(f"Yikes! 😱 Error: Missing required magic keys in JSON data of file {file_name}.")
        return None

def save_users_to_json(users, file_name):
    """
    saves user object to json file
    """
    if not file_name.lower().endswith('.json'):
        file_name += '.json'
    # Convert list of User objects back to a list of dictionaries
    data_to_save = [user.to_dict() for user in users]
    try:
        with open(file_name, 'w') as file:
            json.dump(data_to_save, file, indent=4)
        print(f"\n✨ Tada! Your filtered data was saved in {file_name}")
    except IOError:
        print(f"Egads! 😱 Error: Could not save data to file {file_name}.")

def display_users(users):
    """
    Nice little list formatted to be aesthetically appealing
    """
    if not users:
        print("Zoinks! 👻 No data was found.")
        return
    print(f"\n🎉 Hooray! Here is the lovely people that match your selection.\n")
    for i, user in enumerate(users):
        print(str(user))
        if i < len(users) - 1:
            print("-----------------")

def filter_by_range(users, attribute_key, prompt_display):
    """
    Filters users by number in a given range
    """
    print(f"\n--- Filter by {prompt_display} ---")
    min_val = get_integer_input(f"Please give min {prompt_display} for filtering: ", min_val=0)
    while True:
        max_val = get_integer_input(f"Please give max {prompt_display} for filtering: ")
        if max_val < min_val:
            print("Max cannot be less than min!")
        else:
            break
    print(
        f"\n✨ Ta da! Here is the filtered data based on {prompt_display} between {min_val} and {max_val} inclusively.")
    filtered_users = [user for user in users if min_val <= getattr(user, attribute_key) <= max_val]
    return filtered_users

def filter_by_string_attribute(users, prompt_text, attribute_key, partial_match=False):
    """
    Filters users by a string attribute. 
    Can do exact match or partial match (like area codes).
    """
    print(f"\n--- Filter by {prompt_text} ---")
    search_term = input(f"Please enter {prompt_text.lower()} for filtering: ").strip().lower()
    
    if not search_term:
        print(f"No {prompt_text.lower()} entered. No filtering applied.")
        return []
    
    if partial_match:
        # This allows searching for "123" inside "123-456-7890"
        filtered_users = [user for user in users if search_term in getattr(user, attribute_key).lower()]
    else:
        # This stays as an exact match for things like City names
        filtered_users = [user for user in users if getattr(user, attribute_key).lower() == search_term]
    
    if filtered_users:
        print(f"\n🎉 Ta da! Found {len(filtered_users)} results for: '{search_term}'.")
    else:
        print(f"\nZoinks! 👻 No matches found for '{search_term}'.")
        
    return filtered_users


def main():
    """
    The big kahuna. Main function to run filter through data
    """
    print("\n" + "="*60)
    print("      💖 Welcome to drip-filter Data Filter 💖")
    print("          Let's work together and find your data!")
    print("="*60 + "\n")

    all_users = None
        # Loop to get a valid JSON file name
    while all_users is None:
        file_name = input("WhoopsyDaisy!  🌼 Please enter json file name (or Q to exit): ").strip()
        if file_name.lower() == 'q':
            print("Thanks for using our program! Good bye!")
            return
        all_users = load_users_from_json(file_name)
        if all_users:
            print("Yay! ✨ We found your file!")
    while True:
        print("\n" + "-"*60)
        print("          🌈 Filter Fun Menu 🌈")
        print("-" * 60)
        print("\nMake your selection mis amigos:")
        print("1 - Filter by age (min and max) 👶👵")
        print("2 - Filter by city 🏙️")
        print("3 - Filter by last name ✍️")
        print("4 - Filter by first name 👋")
        print("5 - Filter by id (min and max) #️⃣")
        print("6 - Filter by Phone/Area Code 📞")
        print("or enter Q to quit and say goodbye 🚪")
        print("-" * 60)

        choice = input("This is the part where you pick your filter ").strip().lower()
        
        if not choice:
            print("Zoinks! You didn't pick anything! Try again. 👻")
            continue
        filtered_data = []

        if choice == '1':
            filtered_data = filter_by_range(all_users, "age", "age")
        elif choice == '2':
            filtered_data = filter_by_string_attribute(all_users, "City", "city")
        elif choice == '3':
            filtered_data = filter_by_string_attribute(all_users, "Last Name", "last_name")
        elif choice == '4':
            filtered_data = filter_by_string_attribute(all_users, "First Name", "first_name")
        elif choice == '5':
            filtered_data = filter_by_range(all_users, "id", "id")
        elif choice == '6':
            filtered_data = filter_by_string_attribute(all_users, "Phone Number", "phone_number", partial_match=True)
        elif choice == 'q':
            print("Peacing out. Adios! 👋")
            break
        else:
            print("Oh no! 😔 Invalid option. Please choose from 1-5 or Q.")
            continue
        display_users(filtered_data)
        if filtered_data:
            save_choice = input("\nSave Your Filtered Data? Y/N ✨ \n").strip().lower()
            if save_choice == 'y':
                new_file_name = input("File Name?  ✍️ \n").strip()
                save_users_to_json(filtered_data, new_file_name)
        while True:
            back_to_menu_choice = input("Return to main menu? Y/N 💖 \n").strip().lower()
            if back_to_menu_choice == 'y':
                break
            elif back_to_menu_choice == 'n':
                print("Thanks for searching your data with JavaChips Tech. Good bye! 👋")
                return
            else:
                print("Jinkies! 🥺 That's not a Y or an N. Please try again!")

if __name__ == "__main__":
    main()
