# core/wolfram.py

import wolframalpha

APP_ID = "V3P5H3-WEQ9KTLLL8"  # Replace with your own Wolfram Alpha App ID
client = wolframalpha.Client(APP_ID)

def query(text):
    try:
        res = client.query(text)
        return next(res.results).text
    except:
        return "Sorry, I couldn't find an answer."
