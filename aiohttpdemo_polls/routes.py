from views import index

def setup_routes(app):
    app.router.add_get('/', index)

'''static files:
project_root is the path to the root folder.
'''
# def setup_static_routes(app):
#     app.router.add_static('/static/',
#                           path=PROJECT_ROOT / 'static',
#                           name='static')