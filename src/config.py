import os, logging

DEBUG = True
HOST = os.getenv('HOST')
PORT = int(os.getenv('PORT', '5555'))

logging.basicConfig(
    filename=os.getenv('SERVICE_LOG', 'service.log'),
    level=logging.DEBUG,
    format='%(levelname)s: %(asctime)s pid:%(process)s module:%(module)s %(message)s',
    datefmt='%y-%m-%d %H:%M:%S',
)

AWS_SESSION = {
    'aws_access_key_id': os.getenv('AWS_ACCESS_KEY_ID', None),
    'aws_secret_access_key': os.getenv('AWS_SECRET_ACCESS_KEY', None),
    'region_name': os.getenv('AWS_REGION_NAME', 'us-east-2'),
    'profile_name': os.getenv('AWS_PROFILE', None)
}
