from .todo_item import TodoItem
import datetime

class ViewModel:
    def __init__(self, items):
        self._items = items 

    @property
    def items(self):
        return self._items

    @property
    def todo_items(self):
        output = []

        for item in self._items:
            if item.status == "To Do":
                output.append(item)

        return output

    @property
    def doing_items(self):
        output = []

        for item in self._items:
            if item.status == "Doing":
                output.append(item)

        return output

    @property
    def done_items(self):
        output = []

        for item in self._items:
            if item.status == "Done":
                output.append(item)

        return output

    @property
    def show_done_items(self):
        output = []

        for item in self._items:

            if item.status == "Done":
                output.append(item)
        if len( output) < 5:
            return True
        else:
            return False    

    @property
    def recent_done_items(self):
        output = []

        for item in self._items:
            if item.last_modified_date == datetime.date.today():
                output.append(item)

        return output  
    @property
    def older_done_items(self):
        output = []

        for item in self._items:
            if item.last_modified_date < datetime.date.today():
                output.append(item)

        return output  