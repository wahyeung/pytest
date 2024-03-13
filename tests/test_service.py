import pytest
import requests
from source import service
from unittest.mock import Mock, patch

@patch("source.service.get_user_from_db")
def test_get_user_from_db(mock_get_user_from_db):
    mock_get_user_from_db.return_value = "Mocked Alice"
    user_name = service.get_user_from_db(1)
    assert user_name == "Mocked Alice"

@patch("requests.get")
def test_get_users(mock_get):
    #build a mock obj
    mock_response = Mock()
    #Set mock response status code 200, indates request successfully
    mock_response.status_code = 200
    #Mocking the json() method call of the response object to return a specific value.
    mock_response.json.return_value = {"id" : 1, "name": "John Doe"}
    #apply mock response, use mock_get replace requests_get
    mock_get.return_value = mock_response
    #call function
    data = service.get_users()
    assert data == {"id": 1, "name": "John Doe"}


@patch("requests.get")
def test_get_users_error(mock_get):
    mock_response = Mock()
    mock_response.status_code = 400
    mock_get.return_value = mock_response
    with pytest.raises(requests.HTTPError):
        service.get_users()