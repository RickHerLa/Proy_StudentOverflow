import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'mi_clave_secreta'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres.lwybdtzwdaouuxppydfm:1234@aws-0-us-west-1.pooler.supabase.com:6543/postgres'
