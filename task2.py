import random

print(" Welcome to the Guess the Number Game!")
print("I have selected a number between 1 and 100.")
print("Try to guess it! I'll give you hints...")

# Generate random number
secret_number = random.randint(1, 100)
attempts = 0

while True:
    try:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < secret_number:
            print("📉 Too low! Try a higher number.")
        elif guess > secret_number:
            print("📈 Too high! Try a lower number.")
        else:
            print(f"🎉 Correct! You guessed the number in {attempts} attempts.")
            break

    except ValueError:
        print(" Please enter a valid number!")
