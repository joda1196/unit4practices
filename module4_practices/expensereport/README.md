In this practice you need to accomplish the following:

1. Create a model called ExpenseTracker.
2. In ExpenseTracker it should have the following fields:

- [ ] 'Date' a DateField that takes datetime.
- [ ] 'Location' a TextField that takes the location of the expense.
- [ ] 'Amount' a FloatField that takes the amount spent at that location.
- [ ] 'Notes' an Optional TextField that takes notes on the expense.

3. You should have the following functions capable in your model:

- [ ] Create an Expense.
- [ ] Update an Expense. You should be able to change any of the fields based on the argument given (if notes, change notes, etc.). You should not be able to put anything other than a date in datetime fashion in Date field or in Location.
- [ ] Delete an Expense given the object id.
- [ ] Filter expenses by location, and amount.
- [ ] Show a report of all expenses.
- [ ] You should have a helper function that returns the amount as a currency string.

4. You should write your own tests for each of these functionalities.
