from rest_framework.views import APIView, Response
from works.models import Work


class WorksApiView(APIView):

    def get(self, request):
        works = Work.objects.all()
        data = dict()
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
