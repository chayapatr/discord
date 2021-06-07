from flask import Flask
from threading import Thread
from random import choice

app = Flask('')

quote = ["It’s too bad she won’t live. But then again, who does?", "Now I wanna dance, I wanna win. I want that trophy, so dance good.", "I've got a bad feeling about this", "🤔"]

@app.route('/')
def home():
    return choice(quote)

def run():
  app.run(host='0.0.0.0',port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()