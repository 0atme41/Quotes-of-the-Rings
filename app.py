from flask import Flask, render_template, request, redirect
from cs50 import SQL
import unidecode

app = Flask(__name__)

db = SQL("sqlite:///quotes.db")

# There are three main values that are used in logic statements and decide the user progression (stored in a dictionary)
vars = {
    "character": "", ## The global equivalent of the 'answer' variable
    "score": 0, ## Used to keep track of the user's score
    "change": True, ## A boolean to denote if the user's score should change to 0, or stay the same (throughout various requests)
    "avg": 0 ## Used to store a temporary average value based on numbers from quotes.db (per game)
}

def determine(usr_answer, answer):

    # In order to uniform the two bits of data more, white space is stripped from the user input and accents on characters in the database are removed
    ## Also, both strings are converted to uppercase
    usr_answer = usr_answer["usr_answer"].rstrip().upper()
    answer = unidecode.unidecode(answer.upper())

    # These two possible inputs are the only ones whose popular alias are not kangaroo words
    if usr_answer == "MERRY":
        usr_answer = "MERIADOC BRANDYBUCK"
    if usr_answer == "PIPPIN":
        usr_answer = "PEREGRIN TOOK"
    
    if usr_answer in answer and len(usr_answer) > 2:
        return True
    else:
        return False

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/game", methods=['GET', 'POST'])
def game():

    # This conditional is used to reset the user's score if they refresh the page
    ## A boolean value of 'False' denotes that the next site request is a 'valid' one for user progression in the game
    ### A boolean value of 'True' denotes that the user has not answered (made a POST request) and therefore the GET request is invalid towards the game progression
    if vars["change"] == True:
        vars["score"] = 0

    if request.method == "GET":

        rows = db.execute("SELECT * FROM quotes ORDER BY RANDOM() LIMIT 1")

        # Local variables are set
        answer = rows[0]["character"]
        quote = rows[0]["quote"]

        # The global variable encased in the 'vars' dictionary is set
        vars["character"] = answer

        # The randomly selected quote is passed to the front end
        return render_template("game.html", quote=quote)

    else:
        # This promotes a default 'change' value to 'True'
        ## This means that the user must actively answer questions before their GET requests
        vars["change"] = True
        
        answer = vars["character"]
        
        if determine(request.form, answer) == True:
            vars["score"] += 1
            vars["change"] = False # A 'change' value of 'False' ensures the user's score will not get reset upon the ensuing GET request
            return redirect("/game")
        else:
            # calculates the average score from previous games
            vars["avg"] = round(db.execute("SELECT AVG(score) AS score FROM scores")[0]["score"], 1) 
            
             # inserts the score from the new game into the database
            db.execute("INSERT INTO scores (score) VALUES (?)", vars["score"])
            return redirect("/fail")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/fail")
def fail():

    # If the user hasn't started a game yet, they shouldn't be able to access the end page
    ## However, it is possible to get to the /fail page during a game even before failure
    ### No complications arise because of this due to the fact that the GET request just prematurely ends the game
    if vars["character"] == "":
        return redirect("/")

    # The correct answer for the last question in addition to the user's score is passed to the front end
    return render_template("fail.html", answer = vars["character"], score = vars["score"], avg = vars["avg"])