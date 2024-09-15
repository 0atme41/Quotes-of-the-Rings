# Quotes-of-the-Rings

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
