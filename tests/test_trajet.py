import pytest

from covoiturage.models import Trajet


def test_creation_d_un_trajet(db):
    trajet = Trajet.objects.create(
            conducteur="Steph",
            ville_depart="Sokode",
            ville_arrivee="Lome",
            date_depart="2026-10-17",
            heure_depart="18:00",
            places=4,
            prix_places=3000,
        )
    assert trajet.conducteur
    assert trajet.ville_depart
    assert trajet.ville_arrivee
    assert trajet.date_depart
    assert trajet.heure_depart
    assert trajet.places
    assert trajet.prix_places


def test_doit_avoire_au_moins_une_place(db):

    with pytest.raises(Exception):  # noqa: B017
        Trajet.objects.create(
            conducteur="Steph",
            ville_depart="Sokode",
            ville_arrivee="Lome",
            date_depart="2026-10-17",
            heure_depart="18:00",
            places=0,
            prix_places=3000,
        )

       


def test_trajet_affichage(db):
    trajet = Trajet.objects.create(
        conducteur="Steph",
        ville_depart="Sokode",
        ville_arrivee="Lome",
        date_depart="2026-11-14",
        heure_depart="07:00",
        places=4,
        prix_places=3000,
    )

    assert str(trajet) == "Sokode -> Lome, le 14/11/2026 a 07:00"