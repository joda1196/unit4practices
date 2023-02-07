from django.test import TestCase
from app import models


class Test_TaxiBusiness(TestCase):
    # ==========CREATE==========#
    def test_can_create(self):
        taxi = models.create_taxi(3, 2, 1.5, "van")

        self.assertEqual(taxi.passengers, 2)
        self.assertEqual(taxi.taxi_number, 111)
        self.assertTrue(taxi.occupied)

        taxi2 = models.create_taxi(6, 0, 1.0, "car", "wait before loading")

        self.assertEqual(taxi2.taxi_number, 122)
        self.assertEqual(taxi2.notes, "wait before loading")

        taxi3 = models.create_taxi(5, 0, 1.4, "van")
        self.assertEqual(taxi3.taxi_number, 133)

    # ==========UPDATE==========#
    def test_can_update_taxi(self):
        taxi = models.create_taxi(3, 0, 1.5, "van")
        taxi2 = models.create_taxi(5, 3, 2, "car")

        self.assertFalse(taxi.occupied)

        taxi = models.send_taxi(taxi.taxi_number, 3)

        self.assertEqual(taxi.passengers, 3)
        self.assertTrue(taxi.occupied)

    # ==========SEND==========#
    def test_send_taxi(self):
        taxi = models.create_taxi(3, 0, 1.5, "van")
        taxi2 = models.create_taxi(5, 3, 2, "car")

        with self.assertRaises(ValueError):
            models.send_taxi(taxi.taxi_number, 5)

        with self.assertRaises(ValueError):
            models.send_taxi(165, 4)

        with self.assertRaises(ValueError):
            models.send_taxi(taxi2.taxi_number, 3)

    # ==========END==========#
    def test_end_fare(self):
        taxi = models.create_taxi(3, 0, 1.5, "van")
        taxi2 = models.create_taxi(5, 3, 2, "car")

        self.assertEqual(models.end_fare(taxi2.taxi_number, 4.5), 9)

        with self.assertRaises(ValueError):
            models.end_fare(taxi.taxi_number, 3)

        with self.assertRaises(ValueError):
            models.end_fare(166, 3)

        models.send_taxi(taxi.taxi_number, 3)

        self.assertEqual(models.get_taxi(taxi.taxi_number).occupied, True)
        self.assertEqual(models.get_taxi(taxi.taxi_number).passengers, 3)

        models.end_fare(taxi.taxi_number, 5.0)

        self.assertEqual(models.get_taxi(taxi.taxi_number).occupied, False)
        self.assertEqual(models.get_taxi(taxi.taxi_number).passengers, 0)

    # ==========DELETE TAXI==========#
    def test_remove_taxi(self):
        taxi = models.create_taxi(3, 0, 1.5, "van")
        taxi2 = models.create_taxi(5, 3, 2, "car")
        taxi3 = models.create_taxi(5, 0, 1.4, "van")

        models.remove_taxi(taxi3.taxi_number)

        with self.assertRaises(ValueError):
            models.get_taxi(taxi3.taxi_number)

        self.assertEqual(len(models.TaxiBusiness.objects.all()), 2)

    # ==========FIND TAXI==========#
    def test_find_taxi(self):
        taxi = models.create_taxi(3, 0, 1.5, "van")
        taxi2 = models.create_taxi(5, 3, 2, "car")
        taxi3 = models.create_taxi(5, 0, 1.4, "van")

        found = models.get_taxi(122)

        self.assertIsNotNone(found)

    # ==========FILTER UNOCCUPIED==========#
    def test_filter_unoccupied(self):
        taxi = models.create_taxi(3, 0, 1.5, "van")
        taxi2 = models.create_taxi(5, 3, 2, "car")
        taxi3 = models.create_taxi(5, 0, 1.4, "van")

        self.assertIsNotNone(models.filter_unoccupied())
        self.assertEqual(len(models.filter_unoccupied()), 2)

    # ==========FILTER UNOCCUPIED & CAPACITY==========#
    def test_filter_unoccupied(self):
        taxi = models.create_taxi(3, 0, 1.5, "van")
        taxi2 = models.create_taxi(5, 3, 2, "car")
        taxi3 = models.create_taxi(5, 0, 1.4, "van")

        self.assertIsNotNone(models.filter_unoccupied_capacity(4))
        self.assertEqual(len(models.filter_unoccupied_capacity(4)), 1)
