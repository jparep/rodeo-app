import os
from pathlib import Path
import environ

# Initialize environ
env = environ.Env(DEBUG=(bool, False))

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Load environment variables from .env file
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))
