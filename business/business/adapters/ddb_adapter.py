import os
import boto3
import botocore
import logging
from typing import List

log_level = os.environ.get("LOG_LEVEL", "INFO")
logging.root.setLevel(logging.getLevelName(log_level))
logger = logging.getLogger(__name__)


class AmazonDynamoDbAdapter:
    def __init__(self):
        self.dynamodb_resource = boto3.resource("dynamodb")

    def put_item(self, table: str, item: dict):
        dynamodb_table = self.dynamodb_resource.Table(table)

        try:
            resp = dynamodb_table.put_item(Item=item)
            return resp
        except Exception as e:
            logger.error(
                f"An Error occured while trying to save the item {item} : {e}"
            )
            raise e
    
    def scan(self, table: str) -> List:
        dynamodb_table = self.dynamodb_resource.Table(table)
        
        try:
            records = dynamodb_table.scan()
            data = records.get("Items", [])
            while "LastEvaluatedKey" in records:
                records = dynamodb_table.scan(
                    ExclusiveStartKey=records["LastEvaluatedKey"]
                )
                data.extend(records.get("Items", []))
            return data

        except botocore.exceptions.ClientError as e:
            logger.error(
                f"An Error occured while trying to scan items from table {table}"
            )
            raise e
