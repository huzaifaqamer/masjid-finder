from datetime import datetime

from rest_framework.views import APIView
from rest_framework.response import Response

from masajid_finder.models import Masjid


class FindMosques(APIView):

    def get(self, request):
        self.ne_lat = request.GET.get('ne_lat')
        self.ne_lng = request.GET.get('ne_lng')
        self.sw_lat = request.GET.get('sw_lat')
        self.sw_lng = request.GET.get('sw_lng')
        self.namaz = request.GET.get('namaz')
        return Response(self.find_within_box())

    def find_within_box(self):
        current_time = datetime.time(datetime.now())
        filters = {
            '{0}__gt'.format(self.namaz): current_time,
            'latitude__range': (self.sw_lat, self.ne_lat),
            'longitude__range': (self.sw_lng, self.ne_lng)
        }
        return Masjid.objects.filter(**filters).values(
                'name', 'latitude', 'longitude', self.namaz)
