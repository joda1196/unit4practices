from django.test import TestCase
from .models import TaxiBusiness


class Test_TaxiBusiness(TestCase):
    def test_can_create(self):
        taxi = TaxiBusiness.create_taxi(3, 2, 1.5, "van")

        self.assertEqual(taxi.passengers, 2)
        self.assertEqual(taxi.occupied, True)
        self.assertEqual(taxi.taxi_number, 111)
        self.assertTrue(taxi.occupied)

        taxi2 = TaxiBusiness.create_taxi(6, 0, 1.0, "car", "wait before loading")

        self.assertEqual(taxi2.taxi_number, 122)
        self.assertEqual(taxi2.notes, "wait before loading")
        taxi3 = TaxiBusiness.create_taxi(5, 0, 1.4, "van")
        self.assertEqual(taxi3.taxi_number, 133)

    def test_can_update_taxi(self):
        taxi = TaxiBusiness.create_taxi(3, 0, 1.5, "van")
        taxi2 = TaxiBusiness.create_taxi(5, 3, 2, "car")
        self.assertFalse(taxi.occupied)
        taxi = TaxiBusiness.send_taxi(taxi.taxi_number, 3)
        self.assertEqual(taxi.passengers, 3)
        self.assertTrue(taxi.occupied)

        with self.assertRaises(ValueError):
            TaxiBusiness.send_taxi(taxi.taxi_number, 5)

        with self.assertRaises(ValueError):
            TaxiBusiness.send_taxi(165, 4)

        with self.assertRaises(ValueError):
            TaxiBusiness.send_taxi(taxi2.taxi_number, 3)

    # def test_send_taxi(self):
    #     taxi = TaxiBusiness.create_taxi(3, 0, 1.5, "van")
    #     taxi2 = TaxiBusiness.create_taxi(5, 3, 2, "car")
    #     taxi3 = TaxiBusiness.create_taxi(5, 0, 1.4, "van")
    #     self.assertEqual(TaxiBusiness.)
