import os

class TodoItem:
    def __init__(self, id, status, title, last_modified_date):
        self.id = id
        self.status = status
        self.title = title
        self.last_modified_date = last_modified_date

    @classmethod
    def from_trello_card(cls, card):
        id = card["id"]
        title = card["name"]

        id_list = card["idList"]

        last_modified_date = card["dateLastActivity"]

        status = ""

        if id_list == os.getenv("TRELLO_LIST_TODO_ID"):
            status = "To Do"
        elif id_list == os.getenv("TRELLO_LIST_DOING_ID"):
            status = "Doing"
        elif id_list == os.getenv("TRELLO_LIST_DONE_ID"):
            status = "Done"

        return cls(id, status, title, last_modified_date)

    @classmethod
    def from_trello_card_type(cls, card, type):
        id = card["id"]
        title = card["name"]

        id_list = card["idList"]

        status = ""

        if id_list == os.getenv("TRELLO_LIST_TODO_ID"):
            status = "To Do"
        elif id_list == os.getenv("TRELLO_LIST_DOING_ID"):
            status = "Doing"
        elif id_list == os.getenv("TRELLO_LIST_DONE_ID"):
            status = "Done"

        return cls(id, status, title)    
