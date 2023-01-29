from solution import BankAccount
import pytest


def test_create_bank_accounts():
    bankaccount1 = BankAccount("bacc1")
    bankaccount2 = BankAccount("bacc2")
    bankaccount3 = BankAccount("bacc3")

    assert bankaccount1.name == "bacc1"
    assert bankaccount1.accountnumber == 1
    assert bankaccount1.balance == 0

    assert bankaccount2.name == "bacc2"
    assert bankaccount2.accountnumber == 2
    assert bankaccount2.balance == 0

    assert bankaccount3.name == "bacc3"
    assert bankaccount3.accountnumber == 3
    assert bankaccount3.balance == 0


def test_deposit_bank_account():
    bankaccount1 = BankAccount("bacc1")

    assert bankaccount1.name == "bacc1"
    assert bankaccount1.accountnumber == 4
    assert bankaccount1.balance == 0

    bankaccount1.deposit(50)

    assert bankaccount1.balance == 50
    assert bankaccount1.getBalance() == "$50.00"


def test_withdraw_bank_account():
    bankaccount1 = BankAccount("bacc1")

    assert bankaccount1.name == "bacc1"
    assert bankaccount1.accountnumber == 5
    assert bankaccount1.balance == 0

    bankaccount1.deposit(800)

    assert bankaccount1.balance == 800
    assert bankaccount1.getBalance() == "$800.00"

    bankaccount1.withdraw(50)

    assert bankaccount1.balance == 750
    assert bankaccount1.getBalance() == "$750.00"


def test_withdraw_bank_account_overdraft():
    bankaccount1 = BankAccount("bacc1")

    assert bankaccount1.name == "bacc1"
    assert bankaccount1.accountnumber == 6
    assert bankaccount1.balance == 0

    with pytest.raises(ValueError):
        bankaccount1.withdraw(50)
