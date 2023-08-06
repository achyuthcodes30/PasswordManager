# PasswordManager
A command line based secure password manager with a master password to store passwords of various social media accounts in hashed form on a local PostgreSQL database, with features to update and delete accounts and passwords from it.

## Prerequisites
1. **Python** ([install](https://www.python.org/))
2. **PostgreSQL** ([install](https://www.postgresql.org/))

## To run locally

1. Clone this repository 
```
git clone https://github.com/achyuthcodes30/PasswordManager.git
```
2. Change directories to the project folder using 'cd' command.
3. Create server and databases on PostgreSQL database using the pgadmin interface.
4. Set the master password by running-
   ```
   python setmasterpassword.py
   ```
5. Start storing, updating and removing passwords by running-
   ```
   python passwordmanager.py
   ```
