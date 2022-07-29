

from art import logo
from art import vs
from game_data import data
import random


game_over = False
score = 0


def options():
    length = len(data)
    x = random.randint(0, length - 1)
    dic = data[x]
    data.pop(x)
    length -= 1
    return dic


A = options()
B = options()


def compare(A, B):
    A_count = A["follower_count"]
    B_count = B["follower_count"]
    answer = input("who has more followers? A or B :").lower()
    if answer == "a" and A_count > B_count:
        return "right_answer!!"
    elif answer == "b" and B_count > A_count:
        return "right_answer!!"
    else:
        return "wrong_answer!!"


while not game_over:
    print(logo)
    print(f"Compare A : {A['name']} , a {A['description']}, from {A['country']} ")
    print(vs)
    print(f"Against B : {B['name']} , a {B['description']}, from {B['country']} ")
    result = compare(A, B)
    if result == "right_answer!!":
        score += 1
        print(f"{result} your score : {score}")
    if result == "wrong_answer!!":
        print(f"{result} final score : {score}")
        game_over = True
    A = B
    B = options()

