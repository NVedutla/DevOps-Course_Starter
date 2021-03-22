import pytest
import dotenv
from requests.models import Response
import todo_app.app as app
import unittest.mock as mock
import tests.sample_response as sample_response
import json as json

@pytest.fixture
def client():
    # Use our test integration config instead of the 'real' version
    file_path = dotenv.find_dotenv('.env.test')
    dotenv.load_dotenv(file_path, override=True)
    # Create the new app.
    test_app = app.create_app()
    # Use the app to create a test_client that can be used in our tests.
    with test_app.test_client() as client:
        yield client
@mock.patch("requests.request")
def test_index_page(mock_get_requests, client): 
    mock_get_requests.side_effect = alternate_test
    response = client.get('/')
    assert 'to_do' in response.data.decode()

def alternate_test(method, url,params):
     response = mock.Mock(ok=True)  
     response.json.return_value = sample_response.sample_card_response

     return response