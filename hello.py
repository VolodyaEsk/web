""" WSGI-aplication """

def application(environ, start_response):
    # business logic
    status = '200 OK'
    headers = [
        ('Content-Type', 'text/plain')
    ]
    
    lst_body = environ['QUERY_STRING'].split('&')
    body = '\n'.join(lst_body)
    start_response(status, headers)
    return [body]
