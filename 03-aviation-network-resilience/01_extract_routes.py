#!/usr/bin/env python3
"""
PROJECT 3: NETWORK RESILIENCE ANALYSIS
Step 1: Extract Routes from Project 1 Database
"""

import psycopg2
import pandas as pd
import os

print("=" * 70)
print("PROJECT 3: EXTRACT ROUTES FROM PROJECT 1 DATABASE")
print("=" * 70)
print()

DB_HOST = "localhost"
DB_PORT = 5432
DB_NAME = "aviation_cost_db"
DB_USER = "postgres"
DB_PASSWORD = os.environ.get("AVIATION_DB_PASSWORD", "")

print("Step 1: Connecting to Project 1 database...")
print(f"  Host: {DB_HOST}")
print(f"  Database: {DB_NAME}")
print()

try:
    conn = psycopg2.connect(
        host=DB_HOST,
        port=DB_PORT,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )
    cursor = conn.cursor()
    print("✅ Database connection successful!")
    print()
except Exception as e:
    print(f"❌ Connection failed: {e}")
    exit(1)

print("Step 2: Querying unique routes from otp_events...")
print()

query_routes = """
SELECT 
    departing_port,
    arriving_port,
    COUNT(*) AS flight_count,
    SUM(CAST(passengers AS INTEGER)) AS annual_passengers
FROM otp_events
WHERE departing_port IS NOT NULL 
  AND arriving_port IS NOT NULL
  AND CAST(passengers AS INTEGER) > 0
GROUP BY departing_port, arriving_port
ORDER BY annual_passengers DESC;
"""

try:
    df_routes = pd.read_sql(query_routes, conn)
    print(f"✅ Query successful!")
    print(f"   Found {len(df_routes)} unique routes")
    print()
except Exception as e:
    print(f"❌ Query failed: {e}")
    exit(1)

print("Step 3: Validating route data...")
print()

print(f"  Total routes: {len(df_routes)}")
print(f"  Total passengers: {df_routes['annual_passengers'].sum():,.0f}")
print(f"  Total flights: {df_routes['flight_count'].sum():,}")
print()

print("  Busiest routes (top 10):")
print()
for idx, row in df_routes.head(10).iterrows():
    print(f"    {row['departing_port']} → {row['arriving_port']:3} | {row['annual_passengers']:>10,.0f} pax | {row['flight_count']:>5} flights")
print()

print("Step 4: Extracting unique airports...")
print()

departing = set(df_routes['departing_port'].unique())
arriving = set(df_routes['arriving_port'].unique())
all_airports = sorted(departing.union(arriving))

print(f"✅ Found {len(all_airports)} unique airports")
print(f"   {', '.join(all_airports)}")
print()

print("Step 5: Saving to CSV...")
print()

os.makedirs("data", exist_ok=True)

output_file_routes = "data/routes_from_bitre.csv"
df_routes.to_csv(output_file_routes, index=False)
print(f"✅ Saved: {output_file_routes}")

output_file_airports = "data/airports_list.csv"
pd.DataFrame({
    'airport_code': all_airports,
}).to_csv(output_file_airports, index=False)
print(f"✅ Saved: {output_file_airports}")
print()

cursor.close()
conn.close()

print("=" * 70)
print("SUMMARY")
print("=" * 70)
print(f"Routes extracted: {len(df_routes)}")
print(f"Airports found: {len(all_airports)}")
print(f"Total passengers: {df_routes['annual_passengers'].sum():,.0f}")
print()
print("✅ Ready for network graph building!")
print()
