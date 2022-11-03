import os
import io
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
        self.s3_resource = boto3.resource("s3")

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

    def upload_binary_object(
        self, bucket_name: str, object_name: str, object_binary: io.BytesIO
    ):
        # Get bucket object
        boto_test_bucket = self.s3_resource.Bucket(bucket_name)

        # Upload the binary stream.
        boto_test_bucket.upload_fileobj(object_binary, object_name)
