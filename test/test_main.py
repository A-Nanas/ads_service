from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

def test_read_main():
    responce = client.get('/')
    assert responce.status_code == 200
    assert responce.json() == 'OK'

test_read_main()