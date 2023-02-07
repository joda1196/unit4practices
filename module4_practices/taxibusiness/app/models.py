from django.db import models


class TaxiBusiness(models.Model):
    occupied = models.BooleanField()
    capacity = models.IntegerField()
    passengers = models.IntegerField()
    fare = models.FloatField()
    taxi_number = models.IntegerField(default=111)
    taxi_type = models.TextField()
    notes = models.TextField()

    def is_occupied(self):
        return self.passengers != 0


def create_taxi(capacity, passengers, fare, taxi_type, notes=""):
    taxi = TaxiBusiness(
        capacity=capacity,
        passengers=passengers,
        fare=fare,
        taxi_type=taxi_type,
        notes=notes,
    )
    taxi.occupied = taxi.is_occupied()

    top = TaxiBusiness.objects.all().last()
    if top != None:
        taxi.taxi_number = top.taxi_number + 11
    taxi.save()
    return taxi


def get_taxi(taxi_number):
    try:
        return TaxiBusiness.objects.get(taxi_number=taxi_number)
    except TaxiBusiness.DoesNotExist:
        raise ValueError("Not Found")


def send_taxi(taxi_number, passengers):
    taxi = get_taxi(taxi_number)
    if passengers > taxi.capacity or taxi.occupied == True:
        raise ValueError("Taxi occupied or too many.")
    else:
        taxi.passengers = passengers
        taxi.occupied = taxi.is_occupied()
    taxi.save()
    return taxi


def end_fare(taxi_number, distance):
    taxi = get_taxi(taxi_number)
    if not taxi.occupied:
        raise ValueError("Taxi is not on fare.")
    else:
        taxi.passengers = 0
        taxi.occupied = taxi.is_occupied()
    taxi.save()
    return taxi.fare * distance


def remove_taxi(taxi_number):
    TaxiBusiness.objects.get(taxi_number=taxi_number).delete()


def find_taxi(taxi_number):
    taxi = get_taxi(taxi_number)
    return taxi


def filter_unoccupied():
    taxi = TaxiBusiness.objects.filter(occupied=False)
    return taxi


def filter_unoccupied_capacity(capacity=0):
    if capacity != 0:
        taxi = TaxiBusiness.objects.filter(capacity__gte=capacity, occupied=False)
    return taxi
