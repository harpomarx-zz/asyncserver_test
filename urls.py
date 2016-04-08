from views import wshandler, handle

routes = [
    ('GET', '/echo', wshandler),
    ('GET', '/{name}', handle)
]
