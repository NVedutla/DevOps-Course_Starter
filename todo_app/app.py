from flask import Flask, render_template, redirect, request
from todo_app.flask_config import Config
import todo_app.data.session_items as session_items
import requests
import os
from todo_app.data.todo_item import TodoItem

app = Flask(__name__)
app.config.from_object(Config)

@app.route('/')
def index():
    url = f"https://api.trello.com/1/boards/{os.environ.get('TRELLO_BOARD_ID')}/cards"

    query = {
        'key': os.environ.get("TRELLO_KEY"),
        'token': os.environ.get("TRELLO_TOKEN")
    }

    response = requests.request(
        "GET",
        url,
        params=query
    )

    #class_to_do = TodoItem()
   
    #for loop here
    #list of cards
    trello_cards = response.json()
    todo_items = [] # List of TodoItem

    for card in trello_cards:
        item = TodoItem.from_trello_card(card)
        todo_items.append(item)

    return render_template('index.html', todo_items = todo_items)


@app.route('/additem',  methods=['POST'])
def add_item():
    url = f"https://api.trello.com/1/cards"

    query = {
        'key': os.environ.get("TRELLO_KEY"),
        'token': os.environ.get("TRELLO_TOKEN"),
        'name': request.form.get("newItem"),
        'listId': 'WHAT AM I??'
    }

    response = requests.post(
        url,
        params=query
    )

    return redirect("/")


if __name__ == '__main__':
    app.run()
