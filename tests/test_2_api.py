import requests
from http import HTTPStatus
from api.questions_api import api
from utils.assertions import Assert
import json

def test_api_2():
    res =api.list_users()
    assert res.status_code == HTTPStatus.OK
    #Assert.validate_schema(res.json())
def test_api_2a():
    res =api.single_user_not_found()
    assert res.status_code == HTTPStatus.NOT_FOUND
    # Assert.validate_schema(res.json())
def test_api_2b():
    res =api.single_user()
    res_body = res.json()
    assert res.status_code == HTTPStatus.OK
    # Assert.validate_schema(res_body)
    assert res_body["data"]["first_name"] == "Janet"
    example = {
        "data": {
            "id": 2,
            "email": "janet.weaver@reqres.in",
            "first_name": "Janet",
            "last_name": "Weaver",
            "avatar": "https://reqres.in/img/faces/2-image.jpg"
        },
        "support": {
            "url": "https://reqres.in/#support-heading",
            "text": "To keep ReqRes free, contributions towards server costs are appreciated!"
        }
    }
    assert example == res_body
def test_api_2c():
    name1 = 'John'
    job1 = 'Walker'
    res =api.create(name1, job1)
    res_body = res.json()
    assert res_body["name"] == name1
    assert res_body["job"] == job1
    assert res.status_code == HTTPStatus.CREATED
    assert api.delete_user(res_body["id"]).status_code == HTTPStatus.NO_CONTENT
