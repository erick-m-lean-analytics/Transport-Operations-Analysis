import psycopg2
import os

print("Testing database connection...")
try:
    conn = psycopg2.connect(
        host='localhost', 
        port=5432, 
        database='aviation_cost_db',
        user='postgres', 
        password=os.environ.get('AVIATION_DB_PASSWORD', '')
    )
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM otp_events;")
    count = cursor.fetchone()[0]
    print(f"✅ SUCCESS - otp_events has {count:,} rows")
    cursor.close()
    conn.close()
except Exception as e:
    print(f"❌ FAILED: {e}")
