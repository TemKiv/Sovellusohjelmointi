class Config:
    DEBUG = True

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://{Teemu}:{}@localhost/{DIYinstructions}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

