import json
import os
import logging

from business.adapters.s3_adapter import AmazonS3Adapter
from apify_client import ApifyClient
from handle_apify_webhook import handle_apify_webhook

log_level = os.environ.get("LOG_LEVEL", "INFO")
logging.root.setLevel(logging.getLevelName(log_level))

logger = logging.getLogger(__name__)
db_adapter = AmazonS3Adapter()

APIFY_TOKEN = os.environ.get("APIFY_TOKEN")
USER_REPORTS_S3_BUCKET = os.environ.get("USER_REPORTS_S3_BUCKET")

s3_adapter = AmazonS3Adapter()
a_client = ApifyClient(APIFY_TOKEN)

def handler(event, context):
    logger.info(event)

    handle_apify_webhook(
        s3_adapter=s3_adapter,
        bucket_name=USER_REPORTS_S3_BUCKET,
        a_client=a_client,
        apify_webhook_data=json.loads(event['event'])
    )
    
    return {"statusCode": 200, "body": "Export saved to S3 successfully"}
