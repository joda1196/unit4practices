from django.db import models
from datetime import datetime


class LeaveRequest(models.Model):
    date_requested = models.DateTimeField(default=datetime.today(), blank=True)
    employee_name = models.TextField()
    is_sick = models.BooleanField()
    is_personal = models.BooleanField()
    is_paid = models.BooleanField()
    is_approved = models.BooleanField(default=False, blank=True)
    approved_by = models.TextField(blank=True)
    notes = models.TextField(blank=True)

    @classmethod
    def create_leaverequest(
        cls,
        date_requested,
        employee_name,
        is_sick,
        is_personal,
        is_paid,
        is_approved,
        approved_by,
        notes,
    ):
        cls.objects.create(
            employee_name=employee_name,
            is_sick=is_sick,
            is_personal=is_personal,
            is_paid=is_paid,
        )

    @classmethod
    def approve_request(cls, employee_name):
        request = cls.objects.get(employee_name=employee_name)
        request.is_approved = True
        request.save()

    @classmethod
    def sort_by_date(cls):
        return cls.objects.filter(is_approved=False)

    @classmethod
    def sort_by_sick(cls):
        return cls.objects.filter(is_sick=True)

    @classmethod
    def sort_by_approved(cls):
        return cls.objects.filter(is_approved=True)

    @classmethod
    def sort_by_paid(cls):
        return cls.objects.filter(is_paid=True)

    @classmethod
    def sort_by_personal(cls):
        return cls.objects.filter(is_personal=True)

    # @classmethod
    # def sort_by_employee(cls):
    #     if

    @classmethod
    def goodbye_request(cls, employee_name):
        return cls.objects.filter(employee_name).delete()

    def update_expense(
        self,
        date_requested,
        employee_name,
        is_sick,
        is_personal,
        is_paid,
        approved_by,
        notes,
    ):
        if date_requested:
            self.date_requested = date_requested
        if employee_name:
            self.employee_name = employee_name
        if is_sick:
            self.is_sick = is_sick
        if is_personal:
            self.is_personal = is_personal
        if is_paid:
            self.is_paid = is_paid
        if approved_by:
            self.approved_by = approved_by
        if notes:
            self.notes = notes
        self.save()
