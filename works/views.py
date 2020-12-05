from rest_framework.views import APIView, Response
from works.models import Work
from contact_information.models import ContactInformation
from rest_framework.permissions import AllowAny


class WorksApiView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        works = Work.objects.filter(domain=request.domain)
        data = dict()
        contact = ContactInformation.objects.get(domain=request.domain)
        data.update({
            'contact': {
                'phone_number': contact.phone_number,
                'email': contact.email
            }
        })
        for work in works:
            data.update({
                work.id: {
                    'name': work.name,
                    'description': work.description,
                    'photo': work.photo.url,
                    'video': work.video.url
                }
            })

        return Response(data)
