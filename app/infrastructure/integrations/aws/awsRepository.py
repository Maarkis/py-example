from fastapi import Depends
from typing import Final
import boto3


class AwsPricingRepository:
    CLIENT_NAME: Final[str] = "pricing"

    def __init__(self, region: str = "us-east-1") -> None:
        self.region: str = region
        self.client: boto3.Pricing.Client = boto3.client(
            self.CLIENT_NAME, region_name=self.region
        )

    async def get_products(self, service_code: str):
        try:
            response = await self.client.get_products(ServiceCode=service_code)
            return response
        except Exception as e:
            raise e
