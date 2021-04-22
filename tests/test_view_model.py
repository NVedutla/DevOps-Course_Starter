from datetime import date, timedelta
from todo_app.data.view_model import ViewModel
from todo_app.data.todo_item import TodoItem

def test_view_to_do_model():
   # assert 
   todo = TodoItem("1234", "To Do", "Test Title", date.today)
   doing = TodoItem("1234", "Doing", "Test Title", date.today)
   items=[todo, doing]
   view_model = ViewModel(items=items)
   
   assert len(view_model.todo_items) == 1
   assert view_model.todo_items[0].status == "To Do"
   

def test_view_doing_model():
   # assert 
   doing = TodoItem("5678", "Doing", "Test Title", date.today)
   items=[doing]
   view_model = ViewModel(items=items)
   
   assert len(view_model.doing_items) == 1
   assert view_model.doing_items[0].status == "Doing"

   
def test_view_done_model():
   # assert 
   done = TodoItem("9876", "Done", "Test Title", date.today)
   items=[done]
   view_model = ViewModel(items=items)
   
   assert len(view_model.done_items) == 1
   assert view_model.done_items[0].status == "Done"

def test_view_done_model_less_than_five():
   # assert 
   done = TodoItem("9876", "Done", "Test Title", date.today)
   items=[done]
   view_model = ViewModel(items=items)
   
   
   assert len(view_model.done_items) == 1
   assert(view_model.show_done_items == True)

def test_view_recent_done_items():
   # assert 
   done = TodoItem("9876", "Done", "Test Title", date.today())
   items=[done]
   view_model = ViewModel(items=items) 
  
   assert len(view_model.recent_done_items) == 1

def test_view_old_done_items():
   # assert 
   done = TodoItem("9876", "Done", "Test Title", date.today()-timedelta(1))
   items=[done]
   view_model = ViewModel(items=items) 
  
   assert len(view_model.older_done_items) == 1 