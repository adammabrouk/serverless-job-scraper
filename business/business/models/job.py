import json
from uuid import uuid4
from typing import Optional, List
from dataclasses import dataclass, field


@dataclass
class JobSubscription:
    username: str
    subscription_id: str
    email: str
    location: str
    keywords: List[str] = field(default_factory=list)
    bucket: Optional[str] = ""

    @staticmethod
    def from_sqs(message):
        message = json.loads(message) if type(message) == str else message
        return JobSubscription(
            username=message.get("username", str(uuid4())),
            subscription_id=str(uuid4()),
            email=message.get("email-1"),
            location=", ".join(
                [
                    message.get("address-1").get("city"),
                    message.get("address-1").get("state"),
                    message.get("address-1").get("country"),
                ]
            ),
            keywords=message.get("text-1").split(" "),
            bucket="",
        )
