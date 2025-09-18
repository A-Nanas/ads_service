from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

def test_create_post_not_authorised():
    responce = client.get('/post/')
    assert responce.status_code == 405
    assert responce.json() == {"detail": "Method Not Allowed"}

test_create_post_not_authorised()