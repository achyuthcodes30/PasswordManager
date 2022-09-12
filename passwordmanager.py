
from test_hash import verify_password
from menu import menu, create, find, find_accounts,update_masterpass



passw = input('Please provide the master password to start using password_manager: ')

if (verify_password(passw)):
    print('You\'re in')

else:
    print('no luck')
    exit() 

choice = menu()
while choice != 'Q':
    if choice == '1':
        create()
    if choice == '2':
        find_accounts()
    if choice == '3':
        find()
    if choice == '4':
        update_masterpass()
    else:
        choice = menu()
exit()
