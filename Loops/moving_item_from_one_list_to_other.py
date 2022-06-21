# Moving Items form one list to another

# Start wiht users that need to be verified and an empty list to hold confirmed users.

unconfirmed_users = ['alice', 'brain', 'candace']
confirmed_users = []

# Verify each user untill ther are no more unconfirmed users.
# move each verifed user into the list of confirmed users.

while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)


# Display all confirmed users.
print("\nThe following users have been confirmed: ")
for cu in confirmed_users:
    print(cu.title())