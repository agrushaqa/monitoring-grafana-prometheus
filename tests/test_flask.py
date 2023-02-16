from app.api import app
import socket


class TestFlask:

    def test_api_computer_name(self):
        with app.test_client() as test_client:
            response = test_client.get('/computer_name')
            assert response.status_code == 200
            assert str(socket.gethostname()) in str(response.data)
