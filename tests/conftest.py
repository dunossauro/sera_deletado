from app import create_app
from pytest import fixture


@fixture
def client():
    app = create_app()

    with app.test_client() as client:
        yield client
