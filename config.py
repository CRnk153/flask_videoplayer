class Config:
    DEBUG = True
    SECRET_KEY = 'your_secret_key_here'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///app.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    TEMPLATES_AUTO_RELOAD = True
    WTF_CSRF_ENABLED = True
    WTF_CSRF_SECRET_KEY = 'another_secret_key'
