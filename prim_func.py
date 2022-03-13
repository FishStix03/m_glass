from cryptography import fernet
from cryptography.fernet import Fernet

#functions contained in this file
#

#create_acount(username, password, key_file, db)    //inserts the new user data into db. Keyfile is used to encrypt password
#login(username, password, key_file, db)            //return userid from db, -1 if incorrect password, -2 if username doesn't exist

def signup(username, pw, re_pw, key_file, db):
    #check if passwords match
    if pw != re_pw:
        print("Passwords don't match")
        print(pw)
        print(re_pw)
        return -1

    #check the length of the password
    if len(pw) < 5 or len(pw) > 31:
        print("Password must between 6 and 30 characters long")
        return -2

    #check characters of the password
    if not pw.isascii():
        print("Invalid character(s)")
        return -3
    
    #check length of username
    if len(username) < 5 or len(username) > 31:
        print("Username must between 6 and 30 characters long")
        return -4
    
    #check characters of username
    if not username.isascii():
        print("Invalid character(s)")
        return -5

    #check if username exists
    cursor = db.cursor(buffered=True)
    cursor.execute("SELECT username FROM accounts")
    other_names = cursor.fetchall()
    for x in other_names:
        x = str(x)
        x = x[2 : len(x)-3]
        if x == username:
            print("Username exists")
            return -6

    #valid
    return create_acount(username, pw, key_file, db)

def create_acount(username, password, key_file, db):
    cursor = db.cursor()
    #encrypt password
    file = open(key_file, "r")
    key = bytes(file.read(), 'ascii')
    f = Fernet(key)
    password = bytes(password, 'ascii')
    encrypted_pw = f.encrypt(password)
    file.close()
    #insert new account into database
    cursor.execute("INSERT INTO accounts (username, pw) VALUES(%s, %s)", (username, encrypted_pw))
    db.commit()
    cursor.execute("SELECT id FROM accounts WHERE username = %s", (username, ))
    account_id = cursor.fetchone()
    return account_id[0]

def login(username, password, key_file, db):
    #check for username
    cursor = db.cursor(buffered=True)
    cursor.execute("SELECT username FROM accounts")
    other_names = cursor.fetchall()

    for x in other_names:
        x = str(x)
        x = x[2 : len(x)-3]
        if x == username:
            #fetch encrypted password
            cursor.execute("SELECT pw FROM accounts WHERE username = %s", (username, ))
            encrypted_pw = cursor.fetchone()
            encrypted_pw = encrypted_pw[0]

            #decrypt password
            file = open(key_file, "r")
            key = bytes(file.read(), 'ascii')
            f = Fernet(key)
            encrypted_pw = bytes(encrypted_pw, 'ascii')
            decrypted_pw = f.decrypt(encrypted_pw)
            file.close()

            #see if passwords match
            password = bytes(password, 'ascii')
            if decrypted_pw != password:
                print("Incorrect password")
                return -1
            else:
                cursor.execute("SELECT id FROM accounts WHERE username = %s", (username, ))
                account_id = cursor.fetchone()
                return account_id[0]
                

    print("username does not exist")
    return -2

