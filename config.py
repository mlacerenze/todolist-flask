class Config:
  DEBUG = True 
  TESTING = True
  
  # DB Config
  SECRET_KEY = 'secret'
  SQLALCHEMY_DATABASE_URI = 'sqlite:///../instance/db_personalweb.db'
  SQLALCHEMY_TRACK_MODIFICATIONS = False
  
class ProductionConfig(Config):
  DEBUG = False 
  TESTING = False 
  
class DevelopmentConfig(Config):
  DEBUG = True 
  TESTING = True