SECRET_KEY="sad@7&^sdfsdsaSDSFSD;@3"

# database configuration
HOSTNAME = '127.0.0.1'
PORT = '3306'
DATABASE = 'qaproject'
USERNAME = 'root'
PASSWORD = '123456'
DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME, PASSWORD, HOSTNAME, PORT, DATABASE)

SQLALCHEMY_DATABASE_URI = DB_URI


# mail configuration
MAIL_SERVER = "smtp.qq.com"
MAIL_USE_SSL = True
MAIL_PORT = 465
MAIL_USERNAME = "5956882@qq.com"
MAIL_PASSWORD = "yvgvxmmbqjwabjgf"
MAIL_DEFAULT_SENDER = "5956882@qq.com"
