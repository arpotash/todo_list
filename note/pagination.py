from rest_framework.pagination import PageNumberPagination


class ProjectPagination(PageNumberPagination):
    page_size = 10
    max_page_size = 100


class TODOPagination(PageNumberPagination):
    page_size = 20
    max_page_size = 100
