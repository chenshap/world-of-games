import os

from flask import Flask, render_template
# import redis


app = Flask(__name__)
# cache = redis.Redis(host=os.environ.get('REDIS_HOST'), port=6379)

@app.route('/')
def score():

    with open('/Users/chenshapira/PycharmProjects/WorldOfGames/scores.txt', 'r') as f:
        score = f.readlines()[0]
    # marked_up_text = score.textile(score)
    try:
        return render_template("score.html", score=score)
    except:
        return render_template("error.html")

