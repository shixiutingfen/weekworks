CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'

DEBUG = True

# configuration page num
PER_PAGE = 10

# configuration mysql
SQLALCHEMY_DATABASE_URI = "mysql://%s:%s@%s/%s?charset=utf8" % ('root', 'test123', '127.0.0.1', 'dayfilm')

SECRET_KEY = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
USERNAME = 'shixiuting'
PASSWORD = '123'

UPLOAD_FOLDER = './static/upload/'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

RECAPTCHA_PUBLIC_KEY = '6Ld4rwITAAAAAKUD5AntlHi7HL36W2vHJQOIjQmA'
RECAPTCHA_PRIVATE_KEY = '6Ld4rwITAAAAAFE8nTS852QbsqCBx1mN8D4BqenE'