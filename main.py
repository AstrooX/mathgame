import random
import time

# Define game messages in English
messages_en = {
    "welcome": "Welcome to the Number Guessing Game!",
    "choose_lang": "Please choose a language:",
    "lang_choice": "Enter your choice (1/2):",
    "invalid_choice": "Invalid choice. Please select a valid option (1/2).",
    "easy": "Easy (3 guesses, 1x level multiplier)",
    "medium": "Medium (5 guesses, 2x level multiplier)",
    "hard": "Hard (7 guesses, 3x level multiplier)",
    "start_level": "Let's start level {}!",
    "tip": "Tip: Secret Number - {} = {}",
    "win": "You Win!",
    "game_over": "Game over. You made it to level {}.",
    "lost": "You Lost at level {}. The secret number was {}.",
    "move_on": "Let's move on to level {}!",
    "guess": "Enter your guess (guess {} of {}): ",
    "tip_choice": "Do you want a tip? (y/n): ",
    "invalid_tip_choice": "Invalid choice. Please enter 'y' or 'n'.",
}

# Define game messages in Portuguese
messages_pt = {
    "welcome": "Bem-vindo ao Jogo de Adivinhação de Números!",
    "choose_lang": "Por favor, escolha um idioma:",
    "lang_choice": "Digite sua escolha (1/2):",
    "invalid_choice": "Escolha inválida. Por favor, selecione uma opção válida (1/2).",
    "easy": "Fácil (3 tentativas, multiplicador de nível 1x)",
    "medium": "Médio (5 tentativas, multiplicador de nível 2x)",
    "hard": "Difícil (7 tentativas, multiplicador de nível 3x)",
    "start_level": "Vamos começar o nível {}!",
    "tip": "Dica: Número Secreto - {} = {}",
    "win": "Você venceu!",
    "game_over": "Fim de jogo. Você chegou ao nível {}.",
    "lost": "Você perdeu no nível {}. O número secreto era {}.",
    "move_on": "Vamos avançar para o nível {}!",
    "guess": "Digite seu palpite (palpite {} de {}): ",
    "tip_choice": "Você quer uma dica? (s/n): ",
    "invalid_tip_choice": "Escolha inválida. Por favor, digite 's' ou 'n'.",
}

# Define the default messages to be used in case of an invalid language choice
messages_default = messages_en

# Ask the user to choose a language
print(messages_default["choose_lang"])
print("1. English")
print("2. Português")

lang_choice = input(messages_default["lang_choice"])

# Select the messages to use based on the user's language choice
if lang_choice == "1":
    messages = messages_en
elif lang_choice == "2":
    messages = messages_pt
else:
    print(messages_default["invalid_choice"])
    messages = messages_default

# Define the play_game function using the selected messages
def play_game(guess_limit, level_multiplier):
    tip_count = 0
    tip_limit = 3
    level = 1

    while True:
        print(messages["start_level"].format(level))
        secret_number = random.randint(1, 10 * level_multiplier)
        guess_count = 0
        tips_used = 0

        while guess_count < guess_limit:
            guess = int(input(messages["guess"].format(guess_count + 1, guess_limit)))
            guess_count += 1

            if tips_used < tip_limit:
                tip_choice = input(messages["tip_choice"])
                while tip_choice.lower() not in ["y", "n"]:
                    tip_choice = input(messages["invalid_tip_choice"])

                if tip_choice.lower() == "y":
                    tip_x = random.randint(1, 100)
                    print(messages["tip"].format(tip_x, secret_number - tip_x))
                    tips_used += 1

            if guess == secret_number:
                print(messages["win"])
                level += 1
                time.sleep(1)
                if level > 3:
                    print(messages["game_over"].format(level - 1))
                    break
                else:
                    print(messages["move_on"].format(level))
                    break

        if guess_count == guess_limit:
            print(messages["lost"].format(level, secret_number))
            break


# Define the menu options
menu_options = [
    {
        "text": messages["easy"],
        "guess_limit": 3,
        "level_multiplier": 1,
    },
    {
        "text": messages["medium"],
        "guess_limit": 5,
        "level_multiplier": 2,
    },
    {
        "text": messages["hard"],
        "guess_limit": 7,
        "level_multiplier": 3,
    },
]

# Print the menu
print("Menu:")
for i, option in enumerate(menu_options):
    print(f"{i + 1}. {option['text']}")

# Ask the user to choose a game mode
choice = input("Choose a game mode (1-3): ")
while choice not in ["1", "2", "3"]:
    choice = input("Invalid choice. Please choose a valid option (1-3): ")

# Play the selected game mode
selected_option = menu_options[int(choice) - 1]
play_game(selected_option["guess_limit"], selected_option["level_multiplier"])
# Define the ASCII art for the game
ascii_art = """
 _____ _           _   _     _       _     _ 
/  ___| |         | | | |   (_)     | |   | |
\ `--.| |__  _   _| |_| |__  _ _ __ | |_  | |
 `--. \ '_ \| | | | __| '_ \| | '_ \| __| | |
/\__/ / | | | |_| | |_| | | | | |_) | |_  |_|
\____/|_| |_|\__,_|\__|_| |_|_| .__/ \__| (_)
                               | |          
                               |_|          
"""

# Print the ASCII art
print(ascii_art)

