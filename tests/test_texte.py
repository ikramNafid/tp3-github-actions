import pytest
from app.texte import nettoyer_texte


# Test paramétré : plusieurs exemples de nettoyage
@pytest.mark.parametrize("entree, attendu", [
    ("  BONJOUR   monde  ", "bonjour monde"),
    (" déjà propre ", "déjà propre"),
    ("", ""),
    ("     ", ""),
    ("PYTHON", "python"),
])
def test_nettoyer_texte(entree, attendu):
    assert nettoyer_texte(entree) == attendu


# Vérifier les entrées non textuelles
@pytest.mark.parametrize("entree", [
    123,
    None,
])
def test_nettoyer_texte_type_invalide(entree):
    with pytest.raises(TypeError):
        nettoyer_texte(entree)


# Vérifier qu'un texte déjà nettoyé reste identique
def test_nettoyer_texte_deja_nettoye_ne_change_pas_resultat():
    texte = "bonjour monde"

    resultat_initial = nettoyer_texte(texte)
    resultat_final = nettoyer_texte(resultat_initial)

    assert resultat_final == resultat_initial