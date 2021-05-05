# File for utility functions
from django.db import connection

from rest_framework.response import Response
from rest_framework import status


def error_prompt(error):
    '''
    Returns a Response object with data as error
    '''
    return Response(
        {'error': str(error)},
        status=status.HTTP_400_BAD_REQUEST
    )


def get_rows(query, *params):
    '''
    Returns a Response object with data as a list of values from the first field in the query if the query executes successfully else error
    '''
    
    with connection.cursor() as cursor:
        try:
            cursor.execute(query, params)
        except Exception as e:
            return error_prompt(e)

        rows = [label[0] for label in cursor.fetchall()]

    return Response(rows,
                    status=status.HTTP_200_OK)
