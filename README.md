# Language Model Policy Generation

### Installation
```bash
python -m venv .venv

source .venv/bin/activate

pip install -r requirements.txt
```

### Run
To download the FRED data from gcloud:

```bash
export GOOGLE_APPLICATION_CREDENTIALS="./service-account-key.json"

gcloud auth activate-service-account --key-file=$GOOGLE_APPLICATION_CREDENTIALS

gsutil cp gs://humun-storage/path/in/bucket/fred.parquet .

python convert_parquet_to_csv.py 

python split_fred.py 
```