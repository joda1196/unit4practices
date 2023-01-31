In this practice you need to accomplish the following:

1. Create a model called LeaveRequest.
2. In LeaveRequest it should have the following fields:

- [ ] 'date_requested': Should be a datetime field that is [OPTIONAL] and defaults as the current date.
- [ ] 'employee_name': Should be a text field that holds the employees name that made the request.
- [ ] 'is_sick': Should be a boolean field. True for is_sick leave and False otherwise.
- [ ] 'is_personal': should be a boolean field. True for is_personal leave and False otherwise.
- [ ] 'is_paid': should be a boolean field. True for a paid leave and False otherwise.
- [ ] 'Is_approved': should be a boolean field. True for approved and False otherwise. (Should default False)
- [ ] 'approved_by': should be a text field (Should be an [OPTIONAL] field) putting the name of the boss that approved the leave.
- [ ] 'notes': an [OPTIONAL] text field for any given notes on the topic.

3. You should have the following functions capable in your model:

- [ ] Create a LeaveRequest.
- [ ] Approve a LeaveRequest - should approve a already created leave request and require the person to give their name and change is_approved to True.
- [ ] Filter by date: should be able to search by a given date of what leave requests are present.
- [ ] Filter by is_sick:
- [ ] Filter by is_approved:
- [ ] Filter by is_paid:
- [ ] Filter by is_personal:
- [ ] Filter by employee (all filters should allow you to filter by both the given parameter and the employee to just show that employees sick and approved, personal and paid leaves)
- [ ] Delete a leave request from the object id.
- [ ] Update a leave request and be able to change any of the given parameters except approval.

4. You should write your own tests for each of these functionalities.
