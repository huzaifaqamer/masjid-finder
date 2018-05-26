from decouple import config
from .base import *


DEBUG = False

ALLOWED_HOSTS = [config('ALLOWED_HOST_1')]