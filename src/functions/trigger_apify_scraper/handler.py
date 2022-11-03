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

def handler(event, context):


    trigger_apify_scraper(
        db_adapter=db_adapter,
        jobs_table_name=JOBS_TABLE_NAME,
        apify_webhook_url=APIFY_WEBHOOK_URL
    )        

    return {"statusCode": 200}
