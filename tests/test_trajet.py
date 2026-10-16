import pytest

from covoiturage.models import Reservation, Trajet


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

    with pytest.raises(Exception):
        trajet=Trajet.objects.create(
            conducteur="Steph",
            ville_depart="Sokode",
            ville_arrivee="Lome",
            date_depart="2026-10-17",
            heure_depart="18:00",
            places=0,
            prix_places=3000,
        )
        trajet.clean_fields()

       


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



def test_reservation_porte_sur_un_trajet(db):
    trajet1 = Trajet.objects.create(
        conducteur="Steph",
        ville_depart="Sokode",
        ville_arrivee="Lome",
        date_depart="2026-11-14",
        heure_depart="07:00",
        places=4,
        prix_places=3000,
    )
    trajet1 = Trajet.objects.get(id=1)
    reservation = Reservation.objects.create(
        nom_passager="Stephanie",
        nombre_de_places=3,
        trajet=trajet1
    )
    assert reservation.nom_passager
    assert reservation.nombre_de_places
    assert reservation.reservation


def test_affichage_reservation(db):
    reservation = Reservation.objects.create(
        nom_passager="Stephanie1",
        nombre_de_places=2,
    )   

    assert str(reservation) == "Stephanie1 : 2 places"


def test_reservation_une_fois_le_meme_trajet(db):
    with pytest.raises(Exception):  # noqa: B017
        trajet2 = Trajet.objects.create(
            conducteur="Steph1",
            ville_depart="Sokode",
            ville_arrivee="Lome",
            date_depart="2026-11-14",
            heure_depart="07:00",
            places=4,
            prix_places=3000,
        )
            
        Reservation.objects.create(
            nom_passager="Stephanie1",
            nombre_de_places=2,
            trajet=trajet2

        )   

        Reservation.objects.create(
            nom_passager="Stephanie1",
            nombre_de_places=3,
            trajet=trajet2
        )   
