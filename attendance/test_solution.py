from solution import AttendanceTracker
import pytest


def test_attendance_is_class():
    algebra = AttendanceTracker()

    algebra.add_student("Connor")
    algebra.add_student("Luc")
    algebra.add_student("Bryan")

    assert algebra.students == {
        "Connor": ["Connor", False],
        "Luc": ["Luc", False],
        "Bryan": ["Bryan", False],
    }


def test_check_in_student():
    algebra = AttendanceTracker()

    algebra.add_student("Connor")
    algebra.add_student("Luc")
    algebra.add_student("Bryan")

    algebra.check_in("Luc")

    assert algebra.students["Luc"] == ["Luc", True]


def test_add_already_existing_student():
    algebra = AttendanceTracker()

    algebra.add_student("Connor")
    algebra.add_student("Luc")
    algebra.add_student("Bryan")

    with pytest.raises(ValueError):
        algebra.add_student("Bryan")


def test_no_student_check_in():
    algebra = AttendanceTracker()

    algebra.add_student("Connor")
    algebra.add_student("Luc")
    algebra.add_student("Bryan")

    with pytest.raises(ValueError):
        algebra.check_in("Alyx")


def test_no_student_check_in():
    algebra = AttendanceTracker()

    algebra.add_student("Connor")
    algebra.add_student("Luc")
    algebra.add_student("Bryan")


def test_del_student():
    algebra = AttendanceTracker()

    algebra.add_student("Connor")
    algebra.add_student("Luc")
    algebra.add_student("Bryan")

    algebra.delete_student("Luc")

    assert algebra.students == {
        "Connor": ["Connor", False],
        "Bryan": ["Bryan", False],
    }


def test_no_student_del():
    algebra = AttendanceTracker()

    with pytest.raises(ValueError):
        algebra.delete_student("Luc")
