# core/logic.py

import webbrowser
import os
import random
import datetime
from multiprocessing import Process
from core import voice, database, media, utils, wolfram, nlp, pdfgen
import wikipedia
import pyjokes

app_keywords = ("zoom", "google", "google chrome", "spotify", "powerpoint", "power point", "paint",
                "whatsapp", 'vscode', 'vs code', 'visual studio', "command prompt", 'cmd', "mysql", "my sql",
                'excel', 'access', 'illustrator', 'word', 'instagram')


new_tab = 2

def output(query, raw_input):
    user = database.get_username()
    recdata = database.get_recent()

    def say(txt):
        voice.speak(txt)

    if "open" in raw_input:
        utils.handle_app_launch(raw_input[5:], say)

    elif any(op in raw_input for op in ["plus", "minus", "divide", "multiply", "into", "power", "+", "-", "*", "/"]):
        result = utils.calculate_expression(raw_input)
        say(result)

    elif query in ["who made you", "who is your maker"]:
        say(f"I am made by a wonderful person named Vibusha")

    elif query in ["what was my recent task", "recent"]:
        say(f"Your recent query was {recdata}")

    elif query in ["delete history"]:
        database.delete_history()
        say("History deleted successfully")

    elif query == "history":
        hist = database.fetch_history()
        if hist:
            for h in hist:
                print(h)
            pdfgen.create_pdf(hist)

            pdf_path = "resources/history.pdf"
            if os.path.exists(pdf_path):
                os.startfile(pdf_path)
            else:
                say("History PDF could not be generated.")
        else:
            say("No history found to display.")


    elif query == "my subscription":
        say("Showing subscriptions")
        webbrowser.open("https://www.youtube.com/subscription_manager", new=new_tab)

    elif query == "watch later":
        say("Taking you to Watch Later list")
        webbrowser.open("https://www.youtube.com/playlist?list=WL", new=new_tab)

    elif query in ["what is your name"]:
        say("Hey there, I am Ruhi, your virtual assistant")

    elif query in ["take picture", "photo", "picture", "pic", "take selfie"]:
        say(utils.pic_prompt())
        media.take_picture()

    elif query in ["thank you ruhi", "thanks ruhi", "thanks so much"]:
        say("Always here to help you. Come back soon.")

    elif query == "what is my name":
        say(f"Your name is {user}")

    elif query in ["change my name", "change my username"]:
        utils.change_name_prompt()

    elif query == "screenshot":
        say("Taking screenshot in 5 seconds")
        media.take_screenshot()
        say("Done")

    elif query == "joke":
        say(pyjokes.get_joke('en', 'all'))

    elif "say" in raw_input:
        say(raw_input[4:])

    elif "repeat" in raw_input:
        say(raw_input[6:])

    elif query in ["hi", "hello", "hey ruhi", "wassup"]:
        utils.wish_user(user)

    elif query == "what is up":
        say("Just helping out as always")

    elif query in ["battery", "battery percentage"]:
        say(utils.get_battery_status())
        utils.warn_if_low_battery(say)

    elif "what is" in raw_input:
        try:
            result = wolfram.query(raw_input)
            say(result)
        except:
            webbrowser.open(f"https://www.google.com/search?q={raw_input}")

    elif "who is" in raw_input:
        try:
            say(wolfram.query(raw_input))
        except:
            try:
                say(wikipedia.summary(raw_input[6:], sentences=2))
            except:
                webbrowser.open(f"https://www.google.com/search?q={raw_input}")

    else:
        fallback = nlp.classify(raw_input)
        if fallback != "sorry":
            say(fallback)
        else:
            webbrowser.open(f"https://www.google.com/search?q={raw_input}")

    # Save to history unless exempt
    if query not in ["history", "delete"]:
        dt = datetime.datetime.now()
        time_str = dt.strftime("%I:%M %p")
        date_str = dt.strftime("%B %d, %Y")
        database.insert_history(time_str, user, raw_input, date_str)
        database.update_recent(raw_input)
