import requests
import time
from cs50 import SQL

db = SQL("sqlite:///quotes.db")

# Personalized access token for The One Api
ACCESS_TOKEN = "Tmzf7BiII1SqbMePgIJC"

MOVIES = ["The Fellowship of the Ring", "The Two Towers ", "The Return of the King"]

header = {'Authorization' : f'Bearer {ACCESS_TOKEN}'}

# The One Api has a limit of 100 calls per 10 minutes
# If the request causes an error, the function sleeps for 12 minutes (to be safe)
def make_request(route):
    while True:
        try:
            return requests.get(f"https://the-one-api.dev/v2/{route}", headers = header).json()
        except:
            time.sleep(720)


movie_response = make_request("movie")


# Iterates through every movie
for movie_entry in movie_response["docs"]:

    # If the movie is in the main trilogy, lookup every quote in the movie
    if movie_entry["name"] in MOVIES:
        movie_ID = movie_entry["_id"]
        quote_response = make_request(f"movie/{movie_ID}/quote")

        # For every quote, lookup the character who said it
        for quote_entry in quote_response["docs"]:
            character_id = quote_entry["character"]
            character_response = make_request(f"character/{character_id}")

            # Adds the quote and corresponding character name to a row in a SQL database
            if character_response["docs"][0]["name"] != "MINOR_CHARACTER":
                db.execute("INSERT INTO quotes (quote, character) VALUES (?, ?)", quote_entry["dialog"], character_response["docs"][0]["name"])