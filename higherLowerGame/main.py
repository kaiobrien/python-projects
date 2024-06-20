from art import logo, vs
from game_data import data
import random

score = 0
def format_data(account):
    """Takes the account data and returns the printable format."""
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}"

def check_answer(guess, a_followers, b_followers):
    """Takes the user guess and the follower counts and returns if the user is right"""
    #this if statement checks if a has more followers than b and if yes AND the user guess is a then the return is True
    #if a is > than b but the user guess is b then the return is False
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"


print(logo)
account_b = random.choice(data)
game_should_continue = True
while game_should_continue:
    account_a = account_b
    account_b = random.choice(data)
    while account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Against B: {format_data(account_b)}")

    guess = input("Who has more followers: A or B:\n").lower()

    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]

    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    if is_correct:
        score += 1
        print(f"You're right! Current score: {score}")
    else:
        game_should_continue = False
        print(f"You're wrong. Final score: {score}")