starter_text_file = open('game_text.txt', mode='r')
starter_text = starter_text_file.read()
starter_text_file.close()

player_entered_game = input(starter_text + "\n\n\n" + "Your input: ")
while (player_entered_game != "enter"):
    print("=========================\n")
    player_entered_game = input(starter_text + "\n\n\n" + "Your input: ")
print("You did it!")

