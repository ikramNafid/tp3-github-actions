
import pytest
from app.web import create_app


# Fixture : préparer un client de test
@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    return app.test_client()


# Test 1 : message normal
def test_api_message_normal(client):
    response = client.post(
        "/moderate",
        json={"message": "bonjour"}
    )

    assert response.status_code == 200
    assert response.get_json() == {"decision": "autoriser"}


# Test 2 : message contenant spam
def test_api_message_spam(client):
    response = client.post(
        "/moderate",
        json={"message": "ceci est du SPAM"}
    )

    assert response.status_code == 200
    assert response.get_json() == {"decision": "bloquer"}


# Test 3 : message absent
def test_api_message_absent(client):
    response = client.post("/moderate", json={})

    assert response.status_code == 400
    assert response.get_json() == {"error": "Invalid message"}


# Test 4 : type de message invalide
def test_api_message_type_invalide(client):
    response = client.post(
        "/moderate",
        json={"message": 42}
    )

    assert response.status_code == 400
    assert response.get_json() == {"error": "Invalid message"}


# Test bonus 1 : message composé uniquement d'espaces
def test_api_message_espaces(client):
    response = client.post(
        "/moderate",
        json={"message": "   "}
    )

    assert response.status_code == 400
    assert response.get_json() == {"error": "Invalid message"}


# Test bonus 2 : corps JSON de type liste
def test_api_corps_json_liste(client):
    response = client.post(
        "/moderate",
        json=["bonjour"]
    )

    assert response.status_code == 400
    assert response.get_json() == {"error": "JSON object required"}
