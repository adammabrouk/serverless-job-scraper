import os
import logging
from business.adapters.ddb_adapter import AmazonDynamoDbAdapter
from business.adapters.s3_adapter import AmazonS3Adapter
from trigger_apify_scraper import trigger_apify_scraper

log_level = os.environ.get("LOG_LEVEL", "INFO")
logging.root.setLevel(logging.getLevelName(log_level))
logger = logging.getLogger(__name__)

db_adapter = AmazonDynamoDbAdapter()
s3_adapter = AmazonS3Adapter()

JOBS_TABLE_NAME = os.environ.get("JOBS_TABLE_NAME")
APIFY_WEBHOOK_URL = os.environ.get("APIFY_WEBHOOK_URL")
USER_REPORTS_S3_BUCKET = os.environ.get("USER_REPORTS_S3_BUCKET")
PRESIGNED_URL_EXPIRATION_TIME = 7200 # In Seconds

def handler(event, context):


    trigger_apify_scraper(
        db_adapter=db_adapter,
        s3_adapter=s3_adapter,
        jobs_table_name=JOBS_TABLE_NAME,
        apify_webhook_url=db_adapter,
        user_reports_s3_bucket=USER_REPORTS_S3_BUCKET,
        presigned_url_expiration_time=PRESIGNED_URL_EXPIRATION_TIME
    )        

    return {"statusCode": 200}
