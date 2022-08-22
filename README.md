# Quotes-of-the-Rings

## Summary

Quotes of the Rings is a very boring Flask web application that gives the user a random LOTR movie quote, and the user has to guess which character said the quote. A score is calculated after the user misses a quote, and an average score is calculated by storing every score from every user in a database. The database of quotes was constructed from The One Api, an application programming interface that stores a bunch of LOTR info. Unfortunately, some of the quotes are formatted horrendously (lack of commas, lack of spaces, etc.) even though I went through manually and fixed some of them. The back-end was pretty easy due to the simplistic nature of the application and lack of sessions, logins, or anything interesting. The front-end sucked because I hate it with everything I hold dear on this good earth. Front-end is a garbage bad thing and i get a self-inducecd aneurysm every time i google css attribues if i have to make one for file for these jfjioaefweiggoeri rgoeioeaeaoooooiooo

## File Descriptions

static/style.css - *stylesheet for entire website*
templates/index.html - *website homepage, links to gameplay and about page*
templates/about.html - *about page, links back to index*
templates/game.html - *actual 'gameplay', redirects to itself if the answer is right, redirects to fail otherwise*
templates/fail.html - *end screen, shows your score, average score, and the correct answer to the missed quote*
prep.py - *a script that repeatedly called The One Api and contructed a SQL database based on the info*
test.py - *a script that made a command-line program version of the server-side code*
app.py - *server-side code, handles all requests made to webpages*
quotes.db - *SQL database of all LOTR movie quotes and the corresponding character's name*
Procfile - *Web hosting requirement*
requirements.txt - *List of included packages necessary for the application*

---

That's about it.