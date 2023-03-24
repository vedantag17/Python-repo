import random

colors = ["R", "G", "B", "Y", "W", "O"]
tries = 10
code_length = 4

def generate_code():
    code = []

    for _ in range (code_length):
        color = random.choice(colors)
        code.append(color)

    return code

def guess_code():
    guess = input("Guess:").upper().split(" ")

    if len(guess) != code_length:
        print(f"You must guess {code_length} colors.")
        continue

    for color in guess:
        if color not in colors:
            print(f"Invalid color: {color}. Try again.")
            break
    else:
        break

    return guess

def check_code (guess,real_code):
    color_counts = {}
        

            

    