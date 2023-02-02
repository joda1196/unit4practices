from django.test import TestCase
from app import models
from .models import LeaveRequest
import datetime


class ExpenseTrackerTestCase(TestCase):
    # def setUp(self):
    #     LeaveRequest.objects.create(
    #         date_requested=datetime.datetime.now(),
    #         employee_name="Joe Trott",
    #         is_sick=False,
    #         is_personal=True,
    #         is_paid=True,
    #     )

    def test_create_leaverequest(self):
        LeaveRequest.create_leaverequest(
            "2023-02-01",
            "Joe Trott",
            False,
            True,
            True,
        )
        request = LeaveRequest.objects.get(employee_name="Joe Trott")
        self.assertEqual(request.is_approved, False)
        self.assertEqual(request.date_requested, "2023-02-01")
