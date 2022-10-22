import os
import json
import logging
from dataclasses import asdict
from adapters import AmazonDynamoDbAdapter
from models import JobSubscription

log_level = os.environ.get("LOG_LEVEL", "INFO")
logging.root.setLevel(logging.getLevelName(log_level))


logger = logging.getLogger(__name__)
db_adapter = AmazonDynamoDbAdapter()

JOBS_TABLE_NAME = os.environ.get("JOBS_TABLE_NAME")


def lambda_handler(event, context):

    for record in event["Records"]:
        job_subscription = JobSubscription.from_sqs(record["body"])
        logger.info(job_subscription)
        db_adapter.put_item(
            table=JOBS_TABLE_NAME, item=asdict(job_subscription)
        )

    return {"statusCode": 200, "body": "Record inserted successfully"}
