from flask import Flask, request, jsonify
import bcrypt
import psycopg2
import bcrypt

app = Flask(__name__)

def getcursor():
    connection = psycopg2.connect(
        dbname='MrDB',
        user='postgres',
        password='admin',
        host='localhost',
    )
    return connection.cursor(),connection

# Login
@app.route('/login', methods=['POST'])
def login():
    # Get Creds
    username = request.json.get('username')
    password = request.json.get('password')
    cursor,conn = getcursor()
    # Query
    query = '''SELECT password FROM registrations."users" WHERE username = %s'''
    cursor.execute(query, (username,))
    result = cursor.fetchone()
    if result:
        stored_password = result[0]
        authenticated = bcrypt.checkpw(password.encode('utf-8'), stored_password.encode('utf-8'))
    else:
        authenticated = False
    cursor.close()
    return jsonify({'Status': authenticated})

# Signup
@app.route('/signup', methods=['POST'])
def signup():
    # Get Creds
    username = request.json.get('username')
    password = request.json.get('password')
    firstname = request.json.get('firstname') 
    age = request.json.get('age')
    cursor, conn = getcursor()
    print(username,password,firstname,age,cursor)
    # Check if the username already exists
    query = '''SELECT * FROM registrations."users" WHERE username = %s'''
    cursor.execute(query, (username,))
    result = cursor.fetchone()
    if result:
        msg = {'Status':'User Exists'}
        return msg  
    
    # Encryption
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)

    # Insertion
    query = '''INSERT INTO registrations."users" (username, password, firstname, age, status) VALUES (%s, %s, %s, %s, %s)'''
    values = (username, hashed_password.decode('utf-8'), firstname, age, '1')
    cursor.execute(query, values)
    conn.commit()
    cursor.close()
    msg = {"status":"Account Created"}
    return msg

if __name__ == '__main__':
    app.run()