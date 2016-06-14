import os
DEBUG = True

POSTGRES = {
    'user': os.getenv('POSTGRES_USER', 'dbadmin'),
    'pw': os.getenv('POSTGRES_PW', 'dbadmin'),
    'host': os.getenv('POSTGRES_HOST', 'localhost'),
    'port': os.getenv('POSTGRES_PORT', '5432'),
    'db': os.getenv('POSTGRES_DB', 'enyadb'),
}


DB_URI = 'postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES
