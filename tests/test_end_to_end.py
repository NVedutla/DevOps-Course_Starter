from flask import Flask, render_template, redirect, request
import requests
import os
from threading import Thread
import pytest, time
import todo_app.app as app
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys


def create_trello_board():
    url = f"https://api.trello.com/1/boards"
    query = {
        'key': os.environ.get("TRELLO_KEY"),
        'token': os.environ.get("TRELLO_TOKEN"),
        'name': 'Test Board'
    }

    response = requests.request(
        "POST",
        url,
        params=query
    )
    return response.json()['id']

def list_trello_board(board_id):
    url = f"https://api.trello.com/1/boards/{board_id}/lists" 
    
    query = {
        'key': os.environ.get("TRELLO_KEY"),
        'token': os.environ.get("TRELLO_TOKEN")       
    }

    response = requests.request(
        "GET",
        url,
        params=query
    )
    output = response.json()
    

    for list in output:
        list_id = list["id"]
        list_name = list["name"]
        if list_name == "To Do":
            os.environ['TRELLO_LIST_TODO_ID'] = list_id 

def delete_trello_board(BOARD_ID):
    url = f"https://api.trello.com/1/boards/{BOARD_ID}"
    query = {
        'key': os.environ.get("TRELLO_KEY"),
        'token': os.environ.get("TRELLO_TOKEN"),
        
    }

    response = requests.request(
        "DELETE",
        url,
        params=query
    )
    return response

import os 
import dotenv

@pytest.fixture(scope='module')
def test_app(): 
    
    file_path = dotenv.find_dotenv('.env')
    dotenv.load_dotenv(file_path, override=True)
    # Create the new board & update the board id environment variable
    board_id = create_trello_board() 
    os.environ['TRELLO_BOARD_ID'] = board_id

    list_trello_board(board_id) 
    # construct the new application
    application = app.create_app() 
    # start the app in its own thread.
    thread = Thread(target=lambda: application.run(use_reloader=False)) 
    thread.daemon = True
    thread.start() 
    yield application 
    # Tear Down
    thread.join(1) 
    delete_trello_board(board_id)     

@pytest.fixture(scope="module")
def driver(): 
    with webdriver.Firefox() as driver:
        yield driver

def test_task_journey(driver, test_app): 
    driver.get('http://localhost:5000/') 
    assert driver.title == 'To-Do App'
    elem = driver.find_element_by_name("newItem")
    elem.clear()
    elem.send_keys("test to do")
    elem.send_keys(Keys.RETURN)
    time.sleep(1)
    assert "test to do"  in driver.page_source
    
