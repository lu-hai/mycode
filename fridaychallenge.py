#!/usr/bin/python3

import requests

from pprint import pprint 

url = "https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey="

# this function grabs our credentials
def returncreds():
    ## first I want to grab my credentials
    with open("/home/student/news.cred", "r") as mycreds:
        newscreds = mycreds.read()
    ## remove any newline characters from the api_key
    newscreds = newscreds.strip("\n")
    return newscreds

# this is our main function
def main():
    ## first grab credentials
    newscreds = returncreds()

    ## make a call to NASAAPI with our key
    resp = requests.get(url + newscreds)

    ## strip off json
    apod = resp.json()
    n = 0

    for x in apod["articles"]:
        n += 1
        print("Article " + str(n) + ":")
        print(x["title"])



if __name__ == "__main__":
    main()

