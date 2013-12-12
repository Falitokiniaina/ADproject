import psycopg2
import sys

def CleaningViews(schema):
    if not parsing_result: return None
    global db_schema
    db_schema = schema
    if parsing_result.type=='rule':
        statement = CreateViews(parsing_result)
    elif parsing_result.type=='query':
        statement = CreateSelect(parsing_result)
    return statement