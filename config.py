import os
import json

class Config:
    ENV = os.getenv('FLASK_ENV', 'development')
    with open('settings/config.json') as config_file:
        config_data = json.load(config_file)
        environment_config = config_data.get(ENV, config_data['development'])
    SECRET_KEY = os.getenv('SECRET_KEY', 'mysecretkey')
    SQLALCHEMY_DATABASE_URI = environment_config.get('SQLALCHEMY_DATABASE_URI', 'mysql+pymysql://root@localhost:3307/chatbot_db')
    SQLALCHEMY_TRACK_MODIFICATIONS = environment_config.get('SQLALCHEMY_TRACK_MODIFICATIONS', False)

config = Config()