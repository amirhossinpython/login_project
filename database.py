import mysql.connector
import hashlib

def get_db_connection():
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='user_system'
    )
    return connection

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def register_user(first_name, last_name, age, birth_place, national_code, city, phone, password):
    connection = get_db_connection()
    cursor = connection.cursor()
    
    hashed_password = hash_password(password)
    
    try:
        query = "INSERT INTO users (first_name, last_name, age, birth_place, national_code, city, phone, password) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        values = (first_name, last_name, age, birth_place, national_code, city, phone, hashed_password)
        cursor.execute(query, values)
        connection.commit()
        return True, "ثبت‌نام با موفقیت انجام شد"
    except mysql.connector.IntegrityError:
        return False, "این کد ملی قبلاً ثبت شده است"
    except Exception as e:
        return False, f"خطا: {str(e)}"
    finally:
        cursor.close()
        connection.close()

def login_user(national_code, password):
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    
    hashed_password = hash_password(password)
    
    query = "SELECT * FROM users WHERE national_code = %s AND password = %s"
    cursor.execute(query, (national_code, hashed_password))
    user = cursor.fetchone()
    
    cursor.close()
    connection.close()
    
    return user