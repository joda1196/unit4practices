from django.db import models
from datetime import date


class LeaveRequest(models.Model):
    date_requested = models.DateField(blank=True)
    employee_name = models.TextField()
    is_sick = models.BooleanField(default=False)
    is_personal = models.BooleanField(default=False)
    is_paid = models.BooleanField(default=False)
    is_approved = models.BooleanField(default=False)
    approved_by = models.TextField(max_length=100)
    notes = models.TextField(blank=True, null=True)


def create_leaverequest(
    employee_name,
    is_sick,
    is_personal,
    is_paid,
    is_approved,
    approved_by,
    notes=None,
    date_requested=date.today(),
):
    request = LeaveRequest(
        employee_name=employee_name,
        is_sick=is_sick,
        is_personal=is_personal,
        is_paid=is_paid,
        is_approved=is_approved,
        approved_by=approved_by,
        notes=notes,
        date_requested=date_requested,
    )
    request.save()
    return request

    # LeaveRequest.objects.create(
    #     employee_name=employee_name,
    #     is_sick=is_sick,
    #     is_personal=is_personal,
    #     is_paid=is_paid,
    #     is_approved=is_approved,
    #     approved_by=approved_by,
    #     notes=notes,
    #     date_requested=date_requested,
    # )


def approve_request(employee_name):
    request = LeaveRequest.objects.get(employee_name=employee_name)
    request.is_approved = True
    request.save()
    return request


def sort_by_date(date_requested):
    return LeaveRequest.objects.filter(date_requested=date_requested)


def sort_by_sick():
    return LeaveRequest.objects.filter(is_sick=True)


def sort_by_approved():
    return LeaveRequest.objects.filter(is_approved=True)


def sort_by_paid():
    return LeaveRequest.objects.filter(is_paid=True)


def sort_by_personal():
    return LeaveRequest.objects.filter(is_personal=True)


def sort_by_employee(name, sort_type):
    LeaveRequest.objects.get(employee_name=name)


def goodbye_request(name):
    LeaveRequest.objects.get(employee_name=name).delete()


def update_request(employee_name, sort_type, content):
    request = LeaveRequest.objects.get(employee_name=employee_name)
    if sort_type == "name":
        request.employee_name = content
    elif sort_type == "date":
        request.date_requested = content
    elif sort_type == "sick":
        request.is_sick = content
    elif sort_type == "paid":
        request.is_paid = content
    elif sort_type == "personal":
        request.is_personal = content
    request.save()
