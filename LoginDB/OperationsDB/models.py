from django.db import models,connections

# Create your models here.
def getAllData():
    cursor = connections['Postgres_Config'].cursor()
    query = '''SELECT username,password FROM registrations."users" '''
    cursor.execute(query)
    data = cursor.fetchall()
    return data