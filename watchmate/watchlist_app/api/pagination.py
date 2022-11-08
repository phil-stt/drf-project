from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination, CursorPagination


class WatchListPagination(PageNumberPagination):
    page_size = 7
    # page_query_param = 'p'
    page_size_query_param = 'size'
    max_page_size = 10
    # last_page_strings = 'end'


class WatchListLOPagination(LimitOffsetPagination):
    default_limit = 10
    max_limit = 50
    limit_query_param = 'limit'
    offset_query_param = 'start'

# Sometimes used to force users to visit each page (e.g. Terms & Conditions)
class WatchListCPagination(CursorPagination):
    page_size = 5
    ordering = 'created'
    cursor_query_param = 'record'
