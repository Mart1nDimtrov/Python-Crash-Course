unconfirmed_users = ['Alice','Brian','Candace']
confirmed_users = []

while unconfirmed_users:
	confirmed_user = unconfirmed_users.pop()
	print(f'Confirming user: {confirmed_user.title()}')
	confirmed_users.append(confirmed_user)

print('The following users have been confirmed:')
for user in confirmed_users:
	print(user.title())