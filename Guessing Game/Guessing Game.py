from random import randint
print('Let\'s see how good you are at a guessing game')
# Generating random integers for each level
a = randint(1, 50)
b = randint(1, 100)
c = randint(1, 200)
d = 3  # Number of chances

def levels_useripc():
    play = True
    while play:
        # Asking user at what level they want to play this game
        while True:
            try:
                level = input('\nOn what level you want to play this game (Easy "1-50", Normal "1-100", Hard "1-200") -- ').capitalize()
                if level not in ['Easy', 'Normal', 'Hard']:
                    raise ValueError('\nType a correct spelling of level\'s')
                break  # Exit loop if level is valid
            except ValueError as e:
                print(e)
        
        # Set the target number based on level
        if level == 'Easy':
            target = a
        elif level == 'Normal':
            target = b
        elif level == 'Hard':
            target = c

        # Give the user a fixed number of chances
        chances = d
        while chances > 0:
            try:
                user_ip = int(input('Type a number -- '))
            except ValueError:
                print('\nType a number, not an alphabet or word!!')
                continue

            if user_ip == target:
                print('\nYou are a Master in this Game')
                break  # Exit the chance loop on a correct guess
            elif user_ip < target:
                print('You went too low')
            else:
                print('You went too high')
            chances -= 1
            if chances > 0:
                print(f'You have {chances} chances left.')
            else:
                print('\nNo more chances left.')
        
        # Ask the user if they want to play again
        again = input("\nDo you want to play again? (yes/no): ").lower()
        if again not in ['yes', 'y']:
            play = False
            print("Thanks for playing!")
if __name__ == '__main__':
    levels_useripc()