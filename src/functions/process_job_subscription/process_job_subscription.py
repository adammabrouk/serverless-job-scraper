import os
import logging
from dataclasses import asdict
from business.business.adapters.ddb_adapter import (
    AmazonDynamoDbAdapter,
)
from business.business.models.job import (
    JobSubscription,
)

log_level = os.environ.get("LOG_LEVEL", "INFO")
logging.root.setLevel(logging.getLevelName(log_level))


logger = logging.getLogger(__name__)


def process_job_subscription(
    record: dict,
    db_adapter: AmazonDynamoDbAdapter,
    jobs_table_name: str,
):

    job_subscription = JobSubscription.from_sqs(record["body"])
    logger.info(job_subscription)
    db_adapter.put_item(
        table=jobs_table_name,
        item=asdict(job_subscription),
    )
