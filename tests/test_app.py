from app import create_app
from flask import Flask


def test_app():
    assert isinstance(create_app(), Flask)


def test_hello(client):
    response = client.get("/hello")
    assert response.data.decode() == "hello"
