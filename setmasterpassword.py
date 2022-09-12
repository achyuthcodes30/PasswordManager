from database_manager import store_masterpassdb
from test_hash import hash_password

x=input("Please set the masterpassword for password manager")
master_hash=hash_password(x)
store_masterpassdb(master_hash)
