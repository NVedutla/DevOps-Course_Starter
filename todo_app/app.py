from flask import Flask, render_template, redirect, request
from todo_app.flask_config import Config
import todo_app.data.session_items as session_items
import requests

app = Flask(__name__)
app.config.from_object(Config)

@app.route('/')
def index():
    url = "https://api.trello.com/1/boards/BOARD_ID_GOES_HERE/cards"

    query = {
        'key': 'YOUR_KEY',
        'token': 'YOUR_TOKEN'
    }

    response = requests.request(
        "GET",
        url,
        params=query
    )

    data_dictionary = response.json()

    return render_template('index.html') 


@app.route('/additem',  methods=['POST'])
def add_item():
    new_title = request.form.get("newItem")

    session_items.add_item(new_title)

    return redirect("/")


if __name__ == '__main__':
    app.run()
