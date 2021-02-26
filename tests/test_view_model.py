from todo_app.data.view_model import ViewModel
from todo_app.data.todo_item import TodoItem

def test_view_to_do_model():
   # assert 
   todo = TodoItem("1234", "To Do", "Test Title")
   doing = TodoItem("1234", "Doing", "Test Title")
   items=[todo, doing]
   view_model = ViewModel(items=items)
   
   assert len(view_model.todo_items) == 1
   assert view_model.todo_items[0].status == "To Do"
   #assert view_model.todo_items[0].status == "To Do"

def test_view_doing_model():
   # assert 
   doing = TodoItem("5678", "Doing", "Test Title")
   items=[doing]
   view_model = ViewModel(items=items)
   
   assert len(view_model.doing_items) == 1
   assert view_model.doing_items[0].status == "Doing"

   
def test_view_done_model():
   # assert 
   done = TodoItem("9876", "Done", "Test Title")
   items=[done]
   view_model = ViewModel(items=items)
   
   assert len(view_model.done_items) == 1
   assert view_model.done_items[0].status == "Done"