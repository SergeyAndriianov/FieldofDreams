import random

words = ["apple", "banana", "cherry", "date", "fig", "grape"]

chosen_word = random.choice(words)

attempts = int(input("Введіть кількість спроб: "))

display_word = ["*"] * len(chosen_word)

word_letters = list(chosen_word)

while attempts > 0:

    print("".join(display_word))

    guess = input("Введіть букву або слово: ").lower()

    if guess == chosen_word:

        print("Вітаю, ви вгадали слово!")
        break
    elif len(guess) == 1 and guess.isalpha():

        if guess in chosen_word:

            for i in range(len(chosen_word)):
                if chosen_word[i] == guess:
                    display_word[i] = guess
            if "*" not in display_word:
                print("Вітаю, ви вгадали слово!")
                break
        else:

            print("Такої літери немає")
        attempts -= 1
    else:

        print("Невірний ввід. Введіть одну букву або слово.")

if attempts == 0:
    print(f"Ви програли. Загадане слово було '{chosen_word}'.")
