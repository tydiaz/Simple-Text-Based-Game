# Tyler Diaz 8/7/2021
import time
import string

# dictionary that links a room to other rooms.
# links one item for each room except Security Room
all_rooms = {
    'security room': {'west': 'weapons room'},
    'weapons room': {
        'south': 'hangout room',
        'east': 'security room',
        'item': 'Thermal Rifle'
    },
    'hangout room': {
        'west': 'kitchen',
        'east': 'medical',
        'south': 'foyer',
        'north': 'weapons room',
        'item': 'Blood Wine'
    },
    'kitchen': {'east': 'hangout room', 'item': 'Protein Bar'},
    'medical': {
        'north': 'jail',
        'west': 'hangout room',
        'item': 'Bandages'
    },
    'jail': {'south': 'medical', 'item': 'Keys'},
    'foyer': {
        'east': 'kahmeete\'s bedroom',
        'west': 'kahmeete\'s office',
        'north': 'hangout room',
        'item': 'Time Grenade'
    },
    'kahmeete\'s bedroom': {'west': 'foyer', 'item': 'Note'},
    'kahmeete\'s office': {'east': 'foyer'}
}


# Function that prints help menu
def menu():
    print('-' * 60)
    print("Space-Time Text Adventure Game")
    print("Collect 7 items to win the game, or be lost in time by Kahmeete.")
    print('Move commands: go North, go East, go South, go West')
    print('Add Inventory: get "item name"')
    print('To display all items to collect enter: show items')
    print('To display this menu during gameplay enter: help')
    print('To quit game enter: quit')
    print('-' * 60)
    print()


# function that prints current player status
def show_status(current_loc, inventory_list, rooms):
    # Print some gui
    print('-' * 60)
    # print current room with first letter in each word uppercase
    print(f'You are in {string.capwords(current_loc)}')
    # print inventory
    print(f'Inventory: {inventory_list}')
    # calls the print_item function
    print_item(rooms, current_loc)


# function that prints item in room if item exists
def print_item(rooms, current_room):
    if 'item' in rooms[current_room].keys():
        item = rooms[current_room]['item']
        print(f'You see: {item}')


# function that adds item to players inventory and deletes item from dict if player gets item
def getting_inventory(command, inventory_list, rooms, current_loc):
    # set item to command with uppercase for each word
    item = command[1].title()

    # if current location is security room than print message and sleep for 1 sec
    if current_loc == 'security room':
        print('This room does not contain any items.')
        time.sleep(1)
    # if item is in the players inventory print message and sleep for 1 sec
    elif item in inventory_list:
        print('You already have that item!')
        time.sleep(1)
    # if 'item' not in dictionary keys print message and sleep for 1 sec
    elif 'item' not in rooms[current_loc].keys():
        print('This room does not contain anymore items.')
        time.sleep(1)
    # if item in dictionary with key 'item'
    elif item == rooms[current_loc]['item']:
        # append item to inventory
        inventory_list.append(item)
        # delete 'item' from dictionary
        del rooms[current_loc]['item']
        # print item player picked up then sleep for 1 second
        print(f'You picked up: {item}')
        time.sleep(1)
    else:
        # print message and sleep for 1 second
        print('Cannot get that item because it does not exist!')
        time.sleep(1)


# function prints messages if player wins
def print_win(current_loc):
    print('\nCongratulations! You have successfully gotten all the items and reached {}!'
          .format(string.capwords(current_loc)))
    print('You have successfully defeated Kahmeete and saved the Princess of Time!')


# function prints messages if player loses
def print_lose(current_loc):
    print(f'\nYou are in {string.capwords(current_loc)}')
    print('\nYou do not have enough items to defeat Kahmeete!')
    print('Kahmeete used the T.T.A.D. "Time Traveling Alien Device on you!"')
    print('You are lost in the past and you will never rescue the Princess of Time!')


# function that prints goodbye message
def goodbye():
    # sleep for 1 second then print goodbye.
    time.sleep(1)
    print('Goodbye!')


# main function for the game
def main(rooms):
    # Sleep for 2 seconds before starting game
    time.sleep(2)
    # Set current room is set to the start room
    current_room = 'security room'
    # an empty list to grow your inventory
    inventory = []
    # make directions into a list
    directions = ['north', 'south', 'east', 'west']
    # make a list of all items
    all_items = ['Thermal Rifle', 'Blood Wine', 'Protein Bar', 'Bandages', 'Keys', 'Time Grenade', 'Note']

    # Create while True loop
    while True:
        # call function that shows current player stats
        show_status(current_room, inventory, rooms)
        # get user input and lowercase all letters and strip any whitespaces
        prompt = 'What is your move:\n$ '
        player_command = input(prompt).lower().strip()
        # split user command into a list with a max split of 1
        split_command = player_command.split(' ', 1)

        # if player enters quit, print message and break out of loop
        if player_command == 'quit':
            print('\nExiting game....')
            break
        # if player enters show items, print list of all items and sleep for 1 second
        elif player_command == 'show items':
            print(all_items)
            time.sleep(1)
        # if player enters help, call menu function then sleep for 2 seconds
        elif player_command == 'help':
            menu()
            time.sleep(2)
        # if index 0 of split_command is go and index 1 of split command is in directions
        elif split_command[0] == 'go' and split_command[1] in directions:
            # if index 1 of split command is in rooms dictionary
            if split_command[1] in rooms[current_room]:
                # update current room to the next room in dictionary based on the direction from split command
                current_room = rooms[current_room][split_command[1]]
                # if current room is kahmeetes office and length of inventory equals length of all_items
                if current_room == 'kahmeete\'s office' and len(inventory) == len(all_items):
                    # call print_win function for congratulations than break out of loop
                    print_win(current_room)
                    break
                # if current room is kahmeetes office and length of inventory does not equal length of all_items
                elif current_room == 'kahmeete\'s office' and len(inventory) != len(all_items):
                    # call print_lose function for message and break out of loop
                    print_lose(current_room)
                    break
            # if player enters wrong direction print message
            else:
                print('You cannot go that way!')
                time.sleep(1)
        # if index 0 of split command is get, than call the getting_inventory function
        elif split_command[0] == 'get':
            getting_inventory(split_command, inventory, rooms, current_room)
        # if players input does not match any of above than print message and sleep for 1 second
        else:
            print('Invalid command!')
            time.sleep(1)


if __name__ == '__main__':
    # calls the help menu function
    menu()
    # calls the main function to play game
    main(all_rooms)
    # calls the goodbye function for goodbye message
    goodbye()
