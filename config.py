from os import environ

RABBITMQ_CONNECTION = environ["RABBITMQ_CONNECTION"] if environ.get(
    "RABBITMQ_CONNECTION") else "localhost"
MINIO_ACCESS_KEY = environ["MINIO_ACCESS_KEY"] if environ.get(
    "MINIO_ACCESS_KEY") else "Q3AM3UQ867SPQQA43P2F"
MINIO_SECRET_KEY = environ["MINIO_SECRET_KEY"] if environ.get(
    "MINIO_SECRET_KEY") else "zuf+tfteSlswRu7BJ86wekitnifILbZam1KYY3TG"
MINIO_URL = environ["MINIO_URL"] if environ.get(
    "MINIO_URL") else "play.min.io:9000"
MINIO_BUCKET = environ["MINIO_BUCKET"] if environ.get(
    "MINIO_BUCKET") else "brains"
MONGO_URL = environ["MONGO_URL"] if environ.get("MONGO_URL") else "mongodb://localhost:27017" 
MONGO_DB = environ["MONGO_DB"] if environ.get("MONGO_DB") else "logsDB"
MONGO_COLLECTION = environ["MONGO_COLLECTION"] if environ.get("MONGO_COLLECTION") else "cloud_server"
PREPROCESSOR_MONGO_COLLECTION = environ["PREPROCESSOR_MONGO_COLLECTION"] if environ.get(
    "PREPROCESSOR_MONGO_COLLECTION") else "preprocessor"
CREATOR_MONGO_COLLECTION = environ["CREATOR_MONGO_COLLECTION"] if environ.get(
    "CREATOR_MONGO_COLLECTION") else "creator"
DEPLOYER_MONGO_COLLECTION = environ["DEPLOYER_MONGO_COLLECTION"] if environ.get(
    "DEPLOYER_MONGO_COLLECTION") else "deployer"
S3_ENDPOINT = environ["S3_ENDPOINT"] if environ.get("S3_ENDPOINT") else "s3.amazonaws.com"
S3_ACCESS_KEY = environ.get("S3_ACCESS_KEY")
S3_SECRET_KEY = environ.get("S3_SECRET_KEY")
S3_BUCKET = environ["S3_BUCKET"] if environ.get(
    "S3_BUCKET") else "brains"
EDGE_ENDPOINT = environ["EDGE_ENDPOINT"] if environ.get("EDGE_ENDPOINT") else "localhost:8001"

QUEUE = {
    "from_client": "from_client",
    "from_preprocessor": "from_preprocessor",
    "from_creator": "from_creator",
    "from_deployer": "from_deployer"
}
