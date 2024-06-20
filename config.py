class Config:
    SERVER_NAME = '127.0.0.1:5000'
    DEBUG = True
    SECRET_KEY = b'\xefP\x83\xf1JA\xdf\xdcI\x1f\x82\xa7'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///app.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    TEMPLATES_AUTO_RELOAD = False
    WTF_CSRF_ENABLED = True
    WTF_CSRF_SECRET_KEY = b'w\xf6M{|\xd7\xf6\x17\xed\xf3\xe1\xe2'
