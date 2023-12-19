#!/usr/bin/python3

import requests

ITEMURL = "https://opentdb.com/api.php"

def main():

    questions = input("Pick how many questions")
    difficulty = input("Select difficulty")

    items = requests.get(f"{ITEMURL}?amount={questions}&difficulty={difficulty}")
    items = items.json()

    print.items

if __name__ == "__main__":
    main()

