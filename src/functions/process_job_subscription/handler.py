import os
import json
import logging
from dataclasses import asdict
from business.business.adapters.ddb_adapter import AmazonDynamoDbAdapter
from business.business.models.job import JobSubscription
from process_job_subscription import process_job_subscription

log_level = os.environ.get("LOG_LEVEL", "INFO")
logging.root.setLevel(logging.getLevelName(log_level))


logger = logging.getLogger(__name__)
db_adapter = AmazonDynamoDbAdapter()

JOBS_TABLE_NAME = os.environ.get("JOBS_TABLE_NAME")


def handler(event, context):

    for record in event["Records"]:
        process_job_subscription(
            record=record,
            db_adapter=db_adapter,
            jobs_table_name=JOBS_TABLE_NAME
        )        

    return {"statusCode": 200, "body": "Record inserted successfully"}
