import os
import logging
import requests
import boto3
from datetime import datetime
from business.adapters.ddb_adapter import AmazonDynamoDbAdapter
from business.adapters.s3_adapter import AmazonS3Adapter

log_level = os.environ.get("LOG_LEVEL", "INFO")
logging.root.setLevel(logging.getLevelName(log_level))
logger = logging.getLogger(__name__)


def trigger_apify_scraper(
    db_adapter: AmazonDynamoDbAdapter,
    s3_adapter: AmazonS3Adapter,
    jobs_table_name: str,
    apify_webhook_url: str,
    user_reports_s3_bucket: str,
    presigned_url_expiration_time: int,
):
    logger.info("Triggered")
    # Scan all Job Subscriptions
    all_jobs = db_adapter.scan(table=jobs_table_name)
    for job in all_jobs:

        search_query = "+".join(
            job.get("keywords")
            + job.get("location").replace(" ", "").split(",")
        )
        job_search_url = (
            f"https://www.google.com/search?q={search_query}&ibp=htl;jobs"
        )

        logger.info(f"The job search url is : {job_search_url}")

        username, subscription_id, date_of_extraction = (
            job.get("username"),
            job.get("subscription_id"),
            datetime.now().date().strftime("%Y-%m-%d"),
        )
        object_name = (
            f"private/{username}/{subscription_id}_{date_of_extraction}_.csv"
        )

        presigned_upload_data = s3_adapter.create_presigned_url(
            bucket_name=user_reports_s3_bucket,
            object_name=object_name,
            expiration_time=presigned_url_expiration_time,
        )

        logger.info(f"Presigned URL : {presigned_upload_data}")
        
        data_to_send = {
            "url" : job_search_url,
            "presigned_upload_data" : presigned_upload_data
        } 

        # requests.post(
        #     url=apify_webhook_url,
        #     data=data_to_send
        # )
