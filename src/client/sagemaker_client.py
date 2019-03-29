import boto3 as boto3


class SageMakerClient:
    _instance = None

    def __new__(cls,
                aws_access_key_id: str = None,
                aws_secret_access_key: str = None,
                region_name: str = None,
                profile_name: str = None):

        if cls._instance is None:
            cls._instance = object.__new__(cls)
            cls._instance.session = boto3.Session(
                aws_access_key_id=aws_access_key_id,
                aws_secret_access_key=aws_secret_access_key,
                region_name=region_name,
                profile_name=profile_name)
            cls._instance.client = cls._instance.session.client('sagemaker')

        return cls._instance

