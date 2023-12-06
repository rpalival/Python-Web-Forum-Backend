from flask import Flask
from secrets import randbelow

app = Flask(__name__)

@app.get("/random/<int:sides>")
def roll(sides):
    if sides <= 0:
        return {'err': 'need a positive number of sides' }, 400
    return {'num': randbelow(sides) + 1}