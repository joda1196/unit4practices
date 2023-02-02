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

    @classmethod
    def create_taxi(cls, capacity, passengers, fare, taxi_type, notes=""):
        taxi = cls(
            capacity=capacity,
            passengers=passengers,
            fare=fare,
            taxi_type=taxi_type,
            notes=notes,
        )
        taxi.occupied = taxi.is_occupied()

        top = cls.objects.all().last()
        if top != None:
            taxi.taxi_number = top.taxi_number + 11
        cls.save(taxi)
        return taxi

    @classmethod
    def get_taxi(cls, taxi_number):
        try:
            return cls.objects.get(taxi_number=taxi_number)
        except cls.DoesNotExist:
            raise ValueError("Not Found")

    @classmethod
    def send_taxi(cls, taxi_number, passengers):
        taxi = cls.get_taxi(taxi_number)
        if passengers > taxi.capacity or taxi.occupied == True:
            raise ValueError("Taxi occupied or too many.")
        else:
            taxi.passengers = passengers
            taxi.occupied = taxi.is_occupied()
        taxi.save()
        return taxi

    def end_fare(cls, taxi_number, distance):
        taxi = cls.get_taxi(taxi_number)
        if not taxi.occupied:
            raise ValueError("Taxi is not on fare.")
        else:
            taxi.passengers = 0
            taxi.occupied = taxi.is_occupied()
        taxi.save()
        return taxi.fare * distance

    # def remove_taxi():
