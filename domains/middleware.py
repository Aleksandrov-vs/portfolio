from django.utils.deprecation import MiddlewareMixin


class CurrentDomainMiddleware(MiddlewareMixin):
    def process_request(self, request):
        from .models import Domain
        print(Domain.objects.get_current(request))
        request.domain = Domain.objects.get_current(request)