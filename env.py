host = '157.230.209.171'
user = 'kalpana_1827'
password = 'MzKQXEB0SmpJezIt08aBEYB32Q1m8QXW'


def get_db_url(db, user=user, host=host, password=password):
    '''
    This function uses my info from my env file to
    create a connection url to access the Codeup db.
    It takes in a string name of a database as an argument.
    '''
    url = f'mysql+pymysql://{user}:{password}@{host}/{db}'
    return url