from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

class ProfissionaisLocalidadePagination(PageNumberPagination):
    page_size = 10
    
    def get_paginated_response(self, data):
        return Response({
            'quantidade_profissionais': (self.page.paginator.count - self.page_size)
            if self.page.paginator.count > self.page_size else 0,
            'profissionais': data
        })