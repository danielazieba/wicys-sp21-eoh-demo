starter_text_file = open('game_text.txt', mode='r')
starter_text = starter_text_file.read()
starter_text_file.close()
buffer_text = "=========================\n"
hint_text = "Hints will unlock based on the things you've done in the game. Be warned: opening this page multiple times might unlock more hints, so if you want to see a past one without getting new hints, scroll back up in your terminal window instead of re-opening the hints option."
hints = ["Try going to the computer!", "Look in the bedroom for a possible password hint", "Consulting our Caesar cipher guide might help you apply the hint you can find in the game.", "You know that this puzzle involves Caesar ciphers, so what you're trying to find here is the number of rotations you need to go back to the original password text.", "How well do 9 rotations work on the whiteboard text?"]
curr_hint_index = 0

def get_curr_hint():
    curr_hint_text = hint_text + "\n\n"
    for i in range(len(hints)):
        if i <= curr_hint_index:
            curr_hint_text += "Hint " + str(i + 1) + ": " + hints[i] + "\n"
        else:
            curr_hint_text += "Hint " + str(i + 1) + ": " + "LOCKED" + "\n"

    return curr_hint_text

player_entered_game = input(starter_text + "\n\n\n" + "Your input: ")
while (player_entered_game != "start"):
    print(buffer_text)
    player_entered_game = input(starter_text + "\n\n\n" + "Your input: ")
print(buffer_text)

starter_text_file_001 = open('game_text_001.txt', mode='r')
starter_text_001 = starter_text_file_001.read()
starter_text_file_001.close()
player_start_game = input(starter_text_001 + "\n\n\n" + "Your input: ")
possible_options_living_room = ["A", "B", "C", "H"]
password_unlocked = False
curr_text = player_start_game
curr_location = "livingroom"

intro_kitchen_text_file = open('default_kitchen.txt', mode='r')
intro_kitchen_text = intro_kitchen_text_file.read()
intro_kitchen_text_file.close()

kitchen_option_file = open('kitchen_options.txt', mode='r')
kitchen_options = kitchen_option_file.read()
kitchen_option_file.close()

bedroom_text_file = open('default_bedroom.txt', mode='r')
bedroom_text = bedroom_text_file.read()
bedroom_text_file.close()

bedroom_options = open('bedroom_options.txt', mode='r')
bedroom_opt = bedroom_options.read()
bedroom_options.close()

living_room_nonstart_file = open('default_living_room.txt', mode='r')
living_room_nonstart = living_room_nonstart_file.read()
living_room_nonstart_file.close()

whiteboard_file = open('whiteboard.txt', mode='r')
whiteboard_text = whiteboard_file.read()
whiteboard_file.close()

living_room_opt_file = open('living_room_options.txt', mode='r')
living_room_opt = living_room_opt_file.read()
living_room_opt_file.close()

while not password_unlocked:    
    if curr_location == "livingroom":
        if curr_text == "A":
            curr_text = buffer_text + intro_kitchen_text + "\n\n\n" + "Your input: "
            curr_location = "kitchen"
        elif curr_text == "B":
            curr_text = buffer_text + bedroom_text + "\n\n\n" + bedroom_opt + "\n\n\n" + "Your input: "
            curr_location = "bedroom"
        elif curr_text == "C":
            curr_text = buffer_text + "You try to log on to your computer to browse cooking videos, but it seems to be locked." + "\n\n\n" + "Options: either type your password guess, X to exit computer screen, or H for hint.\n\n" + "What is the password? "
            curr_location = "computer"
        elif curr_text == "H":
            if curr_hint_index >= 1:
                curr_hint_index += 1
            curr_text = buffer_text + get_curr_hint() + "\n\n\n" + living_room_opt + "\n\n\n" + "Your input: "
    elif curr_location == "kitchen":
        if curr_text == "A":
            coffee_text = "You take a closer look at the coffee brewer, which appears to have an electronic display.\n\nHowever, the display is only showing a frowning face right now, and pressing all of the buttons only result in loud, angry beeps."
            curr_text = buffer_text + coffee_text + "\n\n" + kitchen_options + "\n\n\n" + "Your input: "
        elif curr_text == "B":
            toast_text = "The toaster appears to be fully functional and ready to toast, but there is no bread available. Perhaps you could find some in a cabinet?"
            curr_text = buffer_text + toast_text + "\n\n" + kitchen_options + "\n\n\n" + "Your input: "
        elif curr_text == "C":
            cabinet_text = "You try to open the cabinet which you suspect may store your bread supply, but it is tightly locked with a combination lock."
            curr_text = buffer_text + cabinet_text + "\n\n" + kitchen_options + "\n\n\n" + "Your input: "
        elif curr_text == "D":
            fridge_text = "You pull as hard as you can on the fridge handle, but it doesn't budge. Seems like it might have to do with the fact that this is a smart fridge."
            curr_text = buffer_text + fridge_text + "\n\n" + kitchen_options + "\n\n\n" + "Your input: "
        elif curr_text == "E":
            curr_text = buffer_text + living_room_nonstart + "\n\n\n" + "Your input: "
            curr_location = "livingroom"
        elif curr_text == "H":
            if curr_hint_index >= 1:
                curr_hint_index += 1
            curr_text = buffer_text + get_curr_hint() + "\n\n\n" + kitchen_options + "\n\n\n" + "Your input: "
    elif curr_location == "bedroom":
        if curr_text == "A":
            curr_text = buffer_text + "You inspect your bed further, but looking at it just makes you sleepy. You step away before you sink back into it and sleep for another few hours." + "\n\n\n" + bedroom_opt + "\n\n\n" + "Your input: " 
        elif curr_text == "B":
            curr_text = buffer_text + whiteboard_text + "\n\n\n" + bedroom_opt + "\n\n\n" + "Your input: "
            if curr_hint_index == 0:
                curr_hint_index += 2
            elif curr_hint_index == 1:
                curr_hint_index += 1
        elif curr_text == "C":
            curr_text = buffer_text + living_room_nonstart + "\n\n\n" + "Your input: "
            curr_location = "livingroom"
        elif curr_text == "H":
            if curr_hint_index >= 1:
                curr_hint_index += 1
            curr_text = buffer_text + get_curr_hint() + "\n\n\n" + bedroom_opt + "\n\n\n" + "Your input: "

    elif curr_location == "computer":
        if curr_hint_index == 0:
            curr_hint_index += 1

        if curr_text == "delilah":
            password_unlocked = True
            break
        elif curr_text == "X":
            curr_text = buffer_text + living_room_nonstart + "\n\n\n" + "Your input: "
            curr_location = "livingroom"
        elif curr_text == "H":
            if curr_hint_index > 1:
                curr_hint_index += 1
            curr_text = buffer_text + get_curr_hint() + "\n\n\n" + "You are still at the computer. Try a password, or hit X to leave the computer." + "\n\n\n" + "Your input: "
        else:
            curr_text = buffer_text + "Password guess is incorrect! Try again, or hit X to leave the computer, or press H to see hints." + "\n\n\n" + "Your input: "
    curr_text = input(curr_text)

final_text_file = open('final_text.txt',mode='r')
final_text = final_text_file.read()
final_text_file.close()
print(buffer_text)
print(final_text)
