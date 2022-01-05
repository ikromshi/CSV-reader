def read_file(filename):
    file = open(filename, "r")
    all_lines = file.readlines()
    file.close()
    return all_lines


def clean_word(list_of_words):
    final_list = []

    for word in list_of_words:
        new_words = ""
        words_as_list = list(word)
        while "\n" in words_as_list:
            words_as_list.remove("\n")

        for letter in words_as_list:
            new_words += letter
        final_list.append(new_words)
    return final_list


def data_into_dict(fn):
    my_dict = {}

    lines = read_file(fn)
    lines = clean_word(lines)
    names = []
    locations = []
    phone_numbers = []

    for data in lines:
        info = data.split(',')
        names.append(info[0])
        locations.append(info[1])
        phone_numbers.append(info[2])
    for i in range(len(names)):
        my_dict[names[i]] = [locations[i]] + [phone_numbers[i]]

    return my_dict


def change_data(dictionary):
    end_of_loop = False
    while not end_of_loop:
        change_type = input('Type one of the following: \n"S" to search \n"A" to add \n"U" to update the info of a person \n"E" to exit:\n ').upper()
        if change_type == "S":
            name = input("Enter the name: ")
            if name in dictionary:
                print(f"{name}'s location is {dictionary[name][0]}! Their phone number is {dictionary[name][1]}!\n")
            else:
                print("The name doesn't exist in the dictionary!\n")

        elif change_type == "A":
            name = input("Enter the name: ")
            if name in dictionary:
                print("The name already exists in the dictionary!\n")
            else:
                location = input("Enter the location: ")
                number = input('Enter the phone number: ')
                dictionary[name] = [location]
                dictionary[name].append(number)
                print(f"{name} will be added to the Data Collection once you exit the program!\n")

        elif change_type == "U":
            name = input("Enter the name: ")
            if name not in dictionary:
                print("The name doesn't exist in the dictionary!\n")
            else:
                type_change = input("Type 'L' to change the location, or 'N' to change the phone number: ").upper()
                if type_change == "L":
                    location = input("Enter the new location: ")
                    print(f"{name}'s location has been updated from '{dictionary[name][0]}' to '{location}' once you exit!\n")
                    dictionary[name][0] = location
                elif type_change == "N":
                    number = input("Enter the new phone number: ")
                    print(f"{name}'s phone number will be updated from '{dictionary[name][1]}' to '{number} once you exit!'\n")
                    dictionary[name][1] = number

        elif change_type == "E":
            end_of_loop = True


def write_file(filename, dictionary):
    file = open(filename, "w")
    for names, locations in dictionary.items():
        file.write(f"{names},{locations[0]},{locations[1]}\n")
    file.close()


def ascii_art():
    art = """
______         _           _                         _____                           _     
|  _  \       | |         | |                       /  ___|                         | |    
| | | |  __ _ | |_   __ _ | |__    __ _  ___   ___  \ `--.   ___   __ _  _ __   ___ | |__  
| | | | / _` || __| / _` || '_ \  / _` |/ __| / _ \  `--. \ / _ \ / _` || '__| / __|| '_ \ 
| |/ / | (_| || |_ | (_| || |_) || (_| |\__ \|  __/ /\__/ /|  __/| (_| || |   | (__ | | | |
|___/   \__,_| \__| \__,_||_.__/  \__,_||___/ \___| \____/  \___| \__,_||_|    \___||_| |_|                                                                                                                                                                                                                                         
"""
    print(art)


def main():
    # LEVEL FOUR
    ascii_art()
    filename = input("Enter the name of the file: ")
    dictionary = data_into_dict(filename)
    change_data(dictionary)
    write_file(filename, dictionary)


main()
