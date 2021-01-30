from flask import Flask, render_template, redirect, request
import requests
import os
from todo_app.data.todo_item import TodoItem

app = Flask(__name__)

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
        'idList': os.getenv("TRELLO_LIST_TODO_ID")
    }

    response = requests.request(
        "POST",
        url,
        params=query
    )

    if response.status_code != 200:
        raise Exception(f"Wrong status code returned for Trello request: {response}")
    
    return redirect("/")

@app.route('/complete-item',  methods=['POST'])
def complete_item():
    url = f"https://api.trello.com/1/cards/{request.form.get('todo-id')}"
    #PUT /1/cards/{cardID}?idList={listID}        
    query = {
        'key': os.environ.get("TRELLO_KEY"),
        'token': os.environ.get("TRELLO_TOKEN"),
        'idList': os.getenv("TRELLO_LIST_DONE_ID")
    }

    response = requests.put(
        url,
        params=query
    )

    if response.status_code != 200:
        raise Exception(f"Wrong status code returned for Trello request: {response}")

    return redirect("/")


if __name__ == '__main__':
    app.run()
