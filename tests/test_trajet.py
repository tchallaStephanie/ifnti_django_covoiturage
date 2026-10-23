import pytest

from covoiturage.models import Reservation, Trajet


@pytest.fixture
def trajet_sokode_lome(db):
    trajet = Trajet.objects.create(
            conducteur="Steph",
            ville_depart="Sokode",
            ville_arrivee="Lome",
            date_depart="2026-10-17",
            heure_depart="18:00",
            places=4,
            prix_places=3000,
        )

    return trajet

def test_creation_d_un_trajet(db, trajet_sokode_lome):
    
    assert trajet_sokode_lome.conducteur
    assert trajet_sokode_lome.ville_depart
    assert trajet_sokode_lome.ville_arrivee
    assert trajet_sokode_lome.date_depart
    assert trajet_sokode_lome.heure_depart
    assert trajet_sokode_lome.places
    assert trajet_sokode_lome.prix_places


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

       


def test_trajet_affichage(db, trajet_sokode_lome):
   
    assert str(trajet_sokode_lome) == "Sokode -> Lome, le 2026-10-17 a 18:00"



def test_reservation_porte_sur_un_trajet(db, trajet_sokode_lome):
    reservation = Reservation.objects.create(
        nom_passager="Stephanie",
        nombre_de_places=3,
        trajet=trajet_sokode_lome
    )
    assert reservation.nom_passager
    assert reservation.nombre_de_places
    assert reservation.trajet


def test_affichage_reservation(db):
    reservation = Reservation.objects.create(
        nom_passager="Stephanie1",
        nombre_de_places=2,
        trajet=Trajet.objects.create(
            conducteur="Steph",
            ville_depart="Sokode",
            ville_arrivee="Lome",
            date_depart="2026-10-17",
            heure_depart="18:00",
            places=0,
            prix_places=3000,
        )
    )   
    assert str(reservation) == "Stephanie1 : 2 places"


def test_reservation_une_fois_le_meme_trajet(db, trajet_sokode_lome):
        trajet3 = Trajet.objects.create(
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
            trajet=trajet_sokode_lome

        ) 

        Reservation.objects.create(
            nom_passager="Stephanie1",
            nombre_de_places=3,
            trajet=trajet3
        ) 
