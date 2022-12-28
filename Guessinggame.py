import random

print("---------------------------")
print("     M&M Guessing Game!")
print("---------------------------")


mm_count = random.randint(1, 100)

print("Guess the number of M&Ms in the jar to get free lunch! (Between 1-100)")
print()

attempt_limit = 5
attempts = 0

while attempts < attempt_limit:
    guess = int(input("How many M&Ms are in the jar? "))
    attempts += 1

    if guess == mm_count:
        print(f"You got a free lunch! It was {guess}")
        break
    elif guess < mm_count:
        print("Sorry that guess is too LOW!")
    elif guess > mm_count:
        print("Sorry that guess is too HIGH!")

print(f"Bye, you used {attempts} tries")
