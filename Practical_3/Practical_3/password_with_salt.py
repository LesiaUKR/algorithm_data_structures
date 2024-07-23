import bcrypt
 
# Declaring our password
password = b'GeekPassword'
password_same = b'GeekPassword'

# Adding the salt to password
salt = bcrypt.gensalt()
# Hashing the password
hashed = bcrypt.hashpw(password, salt)

salt_same = bcrypt.gensalt()
hashed_same = bcrypt.hashpw(password_same, salt_same)
 
print(f"#1 Salt : {salt} | Hashed: {hashed}")
print(f"#1 Salt : {salt_same} | Hashed: {hashed_same}")









