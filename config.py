import os

class Config():
	'''
		Set config variables for the flask app
    using Environment variables where available.
    Otherwise create the config variable if not done already
  '''

	FLASK_APP = os.getenv('FLASK_APP')
  FLASK_ENV = os.getenv('FLASK_ENV')
  SECRET_KEY = os.environ.get('SECRET_KEY') or 'Ryan will never get access to my CSS'