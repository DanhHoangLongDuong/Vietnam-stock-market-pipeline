from google.cloud import bigquery
from dotenv import load_dotenv
import os

load_dotenv()

project_id = os.getenv("GCP_project")
if not project_id:
    raise ValueError("GCP_project is not set. Add it to .env")

client = bigquery.Client(project=project_id)

print(f"project ID: {client.project}")
print(f"Default Location: {client.location}")

datasets = list(client.list_datasets())
print(f"items: {len(datasets)}")

for d in datasets:
    print(d.dataset_id)