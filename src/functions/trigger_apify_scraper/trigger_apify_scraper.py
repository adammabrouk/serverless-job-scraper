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
    jobs_table_name: str,
    apify_webhook_url: str
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
            f"private/{username}/results/{subscription_id}_{date_of_extraction}_.csv"
        )

        
        data_to_send = {
            "url" : job_search_url,
            "s3_object_key" : object_name
        } 

        requests.post(
            url=apify_webhook_url,
            json=data_to_send
        )
