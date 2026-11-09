
from unittest.mock import patch
import pytest
from app.surveillance import surveiller


# Test 1 : le taux dépasse le seuil
def test_surveillance_declenche_alerte():
    with patch("app.surveillance.envoyer_notification") as notifier:
        resultat = surveiller(0.15)

        assert resultat == "alerte"
        notifier.assert_called_once_with("Taux eleve")


# Test 2 : le taux est inférieur au seuil
def test_surveillance_sans_alerte():
    with patch("app.surveillance.envoyer_notification") as notifier:
        resultat = surveiller(0.05)

        assert resultat == "ok"
        notifier.assert_not_called()


# Test 3 : le taux est exactement égal au seuil
def test_surveillance_seuil_exact():
    with patch("app.surveillance.envoyer_notification") as notifier:
        resultat = surveiller(0.10)

        assert resultat == "ok"
        notifier.assert_not_called()


# Test bonus : vérifier la propagation d'une erreur
def test_surveillance_propage_erreur_notification():
    with patch("app.surveillance.envoyer_notification") as notifier:
        notifier.side_effect = RuntimeError("Notification indisponible")

        with pytest.raises(RuntimeError, match="Notification indisponible"):
            surveiller(0.15)

from app.notifications import envoyer_notification

def test_notification_non_configuree():
    with pytest.raises(RuntimeError, match="Service non configure"):
        envoyer_notification("Test")