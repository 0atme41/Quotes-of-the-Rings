from cs50 import SQL
import unidecode

db = SQL("sqlite:///quotes.db")

score = 0

# Cleaning up data sucks
def determine(usr_answer, answer):

    # In order to uniform the two bits of data more, white space is stripped from the user input and accents on characters in the database are removed
    usr_answer = usr_answer.rstrip()
    answer = unidecode.unidecode(answer)

    # These two possible inputs are the only ones whose popular alias are not kangaroo words
    if usr_answer == "MERRY":
        usr_answer = "MERIADOC BRANDYBUCK"
    if usr_answer == "PIPPIN":
        usr_answer = "PEREGRIN TOOK"
    
    if usr_answer in answer and len(usr_answer) > 2:
        return True
    else:
        return False

while True:

    # Select a random row from the database
    rows = db.execute("SELECT * FROM quotes ORDER BY RANDOM() LIMIT 1")
    answer = rows[0]["character"]
    quote = rows[0]["quote"]
    print(f"Quote:    \"{quote}\"")
    usr_answer = input("Character: ")

    is_correct = determine(usr_answer.upper(), answer.upper())

    if is_correct:
        print("Correct!")
        score += 1
    else:
        print("Incorrect.")
        print(f"Correct Answer: {answer}")
        print(f"Score: {score}")

        avg = 0
        
        # calculates the average score from previous games
        for dict in db.execute("SELECT * FROM scores"):
            avg += dict["score"]
        avg /= db.execute("SELECT COUNT(*) as count FROM scores")[0]["count"]

        print(f"The average score is {round(avg, 1)}.")

        # inserts the score from the new game into the database
        db.execute("INSERT INTO scores (score) VALUES (?)", score)
        
        while True:
            play = input("Play Again? (y/n) ")

            if play.upper() == "Y":
                score = 0
                break
            elif play.upper() == "N":
                exit()





