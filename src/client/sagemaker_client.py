import boto3 as boto3


class SageMakerClient:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = object.__new__(cls)
            cls._instance.session = boto3.Session(profile_name="profile")
            cls._instance.client = cls._instance.session.client('sagemaker')

        return cls._instance

