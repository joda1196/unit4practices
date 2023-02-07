from django.test import TestCase
from app import models
from datetime import date


class LeaveRequestTestCase(TestCase):
    # ------CREATE------
    def test_create_leaverequest(self):
        request = models.create_leaverequest(
            "Joe Trott",
            True,
            True,
            False,
            True,
            "Luis",
            "ASDF",
        )

        self.assertEqual(request.id, 1)
        self.assertEqual(request.employee_name, "Joe Trott")
        self.assertEqual(request.date_requested, date.today())

    # -----APPROVE-------
    def test_approve_request(self):
        models.create_leaverequest(
            "Joe Trott", True, True, False, False, "Luis", "ASDF", "2023-04-05"
        )
        request = models.approve_request("Joe Trott")
        self.assertTrue(request.is_approved)

    # ------DATE------
    def test_sort_by_date(self):
        models.create_leaverequest(
            "Joe Trott", True, True, False, False, "Luis", "ASDF", "2023-04-05"
        )
        models.create_leaverequest(
            "Luis", True, True, False, False, "Armando", "Best Student", "2023-04-05"
        )
        models.create_leaverequest("Armando", True, True, False, False, "Luis", "AAAA")
        request = models.sort_by_date("2023-04-05")
        self.assertIsNotNone(request)
        self.assertEqual(len(request), 2)

    # -----SICK-----
    def test_sort_by_sick(self):
        models.create_leaverequest(
            "Joe Trott", True, True, False, False, "Luis", "ASDF", "2023-04-05"
        )
        models.create_leaverequest(
            "Luis", True, True, False, False, "Armando", "Best Student", "2023-04-05"
        )
        models.create_leaverequest("Armando", False, True, False, False, "Luis", "AAAA")
        request = models.sort_by_sick()
        self.assertIsNotNone(request)
        self.assertEqual(len(request), 2)

    # -----Filter APPROVED-----
    def test_sort_by_approved(self):
        models.create_leaverequest(
            "Joe Trott", True, True, False, False, "Luis", "ASDF", "2023-04-05"
        )
        models.create_leaverequest(
            "Luis", True, True, False, False, "Armando", "Best Student", "2023-04-05"
        )
        models.create_leaverequest("Armando", False, True, False, False, "Luis", "AAAA")
        request = models.sort_by_approved()
        self.assertIsNotNone(request)
        self.assertEqual(len(request), 0)

    # -----Filter PAID-----
    def test_sort_by_paid(self):
        models.create_leaverequest(
            "Joe Trott", True, True, False, False, "Luis", "ASDF", "2023-04-05"
        )
        models.create_leaverequest(
            "Luis", True, True, True, False, "Armando", "Best Student", "2023-04-05"
        )
        models.create_leaverequest("Armando", False, True, False, False, "Luis", "AAAA")
        request = models.sort_by_paid()
        self.assertIsNotNone(request)
        self.assertEqual(len(request), 1)

    # -----Filter PAID-----
    def test_sort_by_personal(self):
        models.create_leaverequest(
            "Joe Trott", True, True, False, False, "Luis", "ASDF", "2023-04-05"
        )
        models.create_leaverequest(
            "Luis", True, False, True, False, "Armando", "Best Student", "2023-04-05"
        )
        models.create_leaverequest("Armando", False, True, False, False, "Luis", "AAAA")
        request = models.sort_by_personal()
        self.assertIsNotNone(request)
        self.assertEqual(len(request), 2)

    # -----Filter DELETE-----
    def test_delete_request(self):
        models.create_leaverequest(
            "Joe Trott", True, True, False, False, "Luis", "ASDF", "2023-04-05"
        )
        models.create_leaverequest(
            "Luis", True, False, True, False, "Armando", "Best Student", "2023-04-05"
        )
        models.create_leaverequest("Armando", False, True, False, False, "Luis", "AAAA")
        models.goodbye_request("Joe Trott")
        request = models.LeaveRequest.objects.all()
        self.assertEqual(len(request), 2)

    # -----UPDATE-----
    def test_update_request(self):
        emp1 = models.create_leaverequest(
            "Joe Trott", True, True, False, False, "Luis", "ASDF", "2023-04-05"
        )
        emp2 = models.create_leaverequest(
            "Luis", True, False, True, False, "Armando", "Best Student", "2023-04-05"
        )
        emp3 = models.create_leaverequest(
            "Armando", False, True, False, False, "Luis", "AAAA"
        )
        request = models.update_request(
            "Joe Trott",
        )
