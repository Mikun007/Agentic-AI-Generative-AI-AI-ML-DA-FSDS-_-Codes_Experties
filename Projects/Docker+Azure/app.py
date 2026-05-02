import os
from flask import Flask, render_template, request, redirect
from azure.storage.blob import BlobServiceClient
import psycopg2
import dotenv

dotenv.load_dotenv()

app = Flask(__name__)

# Config from Environment Variables
blob_acount_url = os.getenv("AZURE_BLOB_ACCOUNT_URL")
storage_credential = os.getenv("AZURE_STORAGE_CREDENTIAL")
CONTAINER_NAME = os.getenv("AZURE_CONTAINER_NAME")

blob_service_client = BlobServiceClient(account_url=f"{blob_acount_url}", credential=storage_credential)

def get_db_connection():
    return psycopg2.connect(
        host=os.getenv("DB_HOST"),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        port=5432,
        sslmode="require"
    )

@app.route('/')
def index():
    return render_template('upload.html')

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    if file:
        filename = file.filename
        blob_client = blob_service_client.get_blob_client(container=CONTAINER_NAME, blob=filename)
        blob_client.upload_blob(file, overwrite=True)
        
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("INSERT INTO files (filename) VALUES (%s)", (filename,))
        conn.commit()
        cur.close()
        conn.close()
        return redirect('/')
    return "No file selected"

if __name__ == "__main__":
    # Crucial for Azure: listen on 0.0.0.0 and the PORT env var
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port)
