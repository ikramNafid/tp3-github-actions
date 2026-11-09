
from unittest.mock import Mock
import pytest
from app.moderation import decider


# Test 1 : le modèle détecte un spam
def test_decider_bloque_spam():
    modele = Mock()
    modele.predict.return_value = "spam"

    resultat = decider(modele, "Offre miracle")

    assert resultat == "bloquer"
    modele.predict.assert_called_once_with("Offre miracle")


# Test 2 : le modèle détecte un message normal
def test_decider_autorise_message_normal():
    modele = Mock()
    modele.predict.return_value = "normal"

    resultat = decider(modele, "Bonjour")

    assert resultat == "autoriser"
    modele.predict.assert_called_once_with("Bonjour")


# Test bonus : le modèle déclenche une erreur
def test_decider_propage_erreur():
    modele = Mock()
    modele.predict.side_effect = RuntimeError("Modele indisponible")

    with pytest.raises(RuntimeError, match="Modele indisponible"):
        decider(modele, "Bonjour")
