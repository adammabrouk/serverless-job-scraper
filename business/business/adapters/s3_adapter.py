import os
import boto3
import botocore
import logging
from typing import Union, Literal

log_level = os.environ.get("LOG_LEVEL_DB_LOCK", "WARNING")
logging.getLogger("python_dynamodb_lock").setLevel(log_level)
logger = logging.getLogger(__name__)


class AmazonS3Adapter:
    def __init__(self):
        self.s3_client = boto3.client("s3")

    def create_presigned_url(
        self,
        bucket_name: str,
        object_name: str,
        expiration_time: int,
    ):

        response = self.s3_client.generate_presigned_post(
            Bucket=bucket_name,
            Key=object_name,
            ExpiresIn=expiration_time,
        )

        # The response contains the presigned URL
        return response
