from flask import Flask
from threading import Thread
from random import choice
import requests

app = Flask('')

quote = ["It’s too bad she won’t live. But then again, who does?", "Now I wanna dance, I wanna win. I want that trophy, so dance good.", "I've got a bad feeling about this", "🤔"]

@app.route('/')
def home():
	# a = requests.get("https://cataas.com/cat")
	return """
    <h1 style='color: black; font-family: monospace;'>hackerman101</h1>
    <p>{p}</p>
		<img src="https://cataas.com/cat" alt="cat">
    """.format(p = choice(quote))
	# return choice(quote)

@app.route('/heyo')
def heyo():
  return "heyo"

def run():
  app.run(host='0.0.0.0',port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()