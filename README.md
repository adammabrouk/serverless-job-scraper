# foragetools-backend

To deploy the project execute the following commands

```
$ pip install aws-sam-cli
$ pip install --upgrade Flask==2.1.0
$ pip install click==8.0.4 scancode-toolkit
$ sam build --profile=adamDevForage
$ sam deploy --guided --region us-east-1 --stack-name forage-backend --profile=adamDevForage
```