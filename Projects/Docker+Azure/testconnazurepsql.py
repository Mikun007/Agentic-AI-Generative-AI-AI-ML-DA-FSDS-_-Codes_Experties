import psycopg2
import os
import dotenv
dotenv.load_dotenv()

conn = psycopg2.connect(
        host=os.getenv("DB_HOST"),  # e.g. mikun1.postgres.database.azure.com
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),  # format: user@server
        password=os.getenv("DB_PASSWORD"),
        port=5432,
        sslmode="require"
)
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS files (
    id SERIAL PRIMARY KEY,
    filename TEXT NOT NULL,
    uploaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
""")

conn.commit()
cur.close()
conn.close()

print("Table created!")