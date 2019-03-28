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
