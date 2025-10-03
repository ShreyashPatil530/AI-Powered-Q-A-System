import mysql.connector
from datetime import datetime

DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': 'shreyash7710',
    'database': 'qa_system'
}

def get_connection():
    """Create and return MySQL database connection"""
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        return conn
    except mysql.connector.Error as e:
        print(f"Database connection error: {e}")
        return None

def create_database():
    """Create database and table if they don't exist"""
    try:
        conn = mysql.connector.connect(
            host=DB_CONFIG['host'],
            user=DB_CONFIG['user'],
            password=DB_CONFIG['password']
        )
        cursor = conn.cursor()
        
        cursor.execute("CREATE DATABASE IF NOT EXISTS qa_system")
        cursor.execute("USE qa_system")
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS qa_logs (
                id INT AUTO_INCREMENT PRIMARY KEY,
                question TEXT NOT NULL,
                answer TEXT NOT NULL,
                timestamp DATETIME NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        
        conn.commit()
        cursor.close()
        conn.close()
        print("Database and table created successfully")
        
    except mysql.connector.Error as e:
        print(f"Database creation error: {e}")

def log_question_answer(question, answer, timestamp):
    """
    Log question and answer to MySQL database
    Args:
        question: User's question
        answer: AI-generated answer
        timestamp: Datetime object
    """
    try:
        conn = get_connection()
        if not conn:
            return
        
        cursor = conn.cursor()
        query = """
            INSERT INTO qa_logs (question, answer, timestamp)
            VALUES (%s, %s, %s)
        """
        cursor.execute(query, (question, answer, timestamp))
        
        conn.commit()
        cursor.close()
        conn.close()
        
    except mysql.connector.Error as e:
        print(f"Logging error: {e}")

create_database()
