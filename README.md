# JobScraper-Backend

## Overview

JobScraper-Backend is a serverless application designed to scrape job listings from Google Jobs and process the data for further use. The project leverages AWS services such as DynamoDB and S3 for data storage and retrieval, and is built using the AWS Serverless Application Model (SAM).

## Key Features

* **Integration with AWS services**: The project uses AWS services such as DynamoDB and S3 for data storage and retrieval.
* **Serverless architecture**: The project is built using AWS SAM (Serverless Application Model), which simplifies the deployment and management of serverless applications.
* **Automated job scraping**: The project includes functionality to trigger job scraping from Google Jobs and handle the results using Apify.
* **Data processing and storage**: The project processes job subscription data and stores the results in S3.
* **Custom library**: The project includes a custom library for handling business logic.

## Deployment

To deploy the project, execute the following commands:

```
$ pip install aws-sam-cli
$ pip install --upgrade Flask==2.1.0
$ pip install click==8.0.4 scancode-toolkit
$ sam build --profile=adamDevForage
$ sam deploy --guided --region us-east-1 --stack-name job-scraper-backend --profile=adamDevForage
```

## TODO

* Make the project name more generic.
* Update the `description` field in the `business/setup.py` file.
* Update the `stack_name` and `s3_prefix` fields in the `samconfig.toml` file.
* Update the `FunctionName` properties in the `template.yaml` file.
* Update the `stack_name` in the deployment commands in the `README.md` file.
