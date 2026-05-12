import psycopg2
import os

conn = psycopg2.connect(
    host='localhost', 
    port=5432, 
    database='aviation_cost_db',
    user='postgres', 
    password=os.environ.get('AVIATION_DB_PASSWORD', '')
)
cursor = conn.cursor()

# Get all column names from otp_events
cursor.execute("""
    SELECT column_name, data_type 
    FROM information_schema.columns 
    WHERE table_name = 'otp_events'
    ORDER BY ordinal_position
""")

print("Columns in otp_events table:")
print()
for col_name, data_type in cursor.fetchall():
    print(f"  {col_name:25} ({data_type})")

cursor.close()
conn.close()
