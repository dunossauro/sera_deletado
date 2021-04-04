from app import create_app


def client():
    app = create_app()

    with app.test_client() as client:
        yield client
