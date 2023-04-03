from mysite.settings import *
from decouple import config
SECRET_KEY=config('SECRET_KEY')

ALLOWED_HOSTS = ['https://calorietracker-production.up.railway.app/']