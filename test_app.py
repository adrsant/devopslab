import pytest

from app import app as flask_app


@pytest.fixture
def app():
    yield flask_app


@pytest.fixture
def client(app):
    return app.test_client()


def test_index(app, client):
    res = client.get('/')
    assert 200 == res.status_code
    assert "Hello World" == res.get_data(as_text=True)
