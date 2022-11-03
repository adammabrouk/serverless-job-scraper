import io
import json
from business.adapters.s3_adapter import AmazonS3Adapter
from apify_client import ApifyClient


def handle_apify_webhook(
    s3_adapter: AmazonS3Adapter,
    bucket_name: str,
    a_client: ApifyClient,
    apify_webhook_data: dict,
):
    # Extract the input then the S3 Path
    run_id = apify_webhook_data.get("eventData").get("actorRunId")

    s3_object_key = (
        a_client.run(run_id)
        .key_value_store()
        .get_record("INPUT")
        .get("s3_object_key")
    )
    # Download the Export ( As Binary )
    export_binary = (
        a_client.run(run_id).dataset().download_items(item_format="xlsx")
    )
    # Create binary stream
    export_binary_buf = io.BytesIO()
    export_binary_buf.write(export_binary)
    # Reset read pointer or uploaded files will be empty!
    export_binary_buf.seek(0)
    # Upload the export to S3
    s3_adapter.upload_binary_object(
        bucket_name=bucket_name,
        object_name=s3_object_key,
        object_binary=export_binary_buf,
    )
