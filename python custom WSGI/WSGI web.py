from wsgiref.simple_server import make_server



def web_app(environment,response):
    status = '200 OK'
    header = [('Content-type','text/html; charset=utf-8')]
    response(status,header)
    return [b'<strong> Hello world I just create my first WSGI server</strong>']

with make_server('',8000,web_app) as server:
    print("Serving on port 8000....\nVisit http://127.0.0.1:8000\nTo to kill the server enter 'control + C' ")
    server.serve_forever()