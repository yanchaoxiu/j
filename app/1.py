from wsgiref.simple_server import make_server

def wsgi_app(environ,start_response):
    start_response('200 ok',[('Context-Type','text/plain')])
    return 'such a tiny wsgi app'

httpd=make_server('0.0.0.0',80,wsgi_app)
httpd.serve_forever()

class WSGI_APP:
    def __call__(self, environ, start_response):
        start_response('200 ok', [('Context-Type', 'text/plain')])
        return 'such a tiny wsgi app'
app=WSGI_APP()

