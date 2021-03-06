from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Boundary, GPContest, School
from .serializers import BoundarySerializer, GPContestSerializer
from django.db.models import Avg

#This api view lists the Boundaries (District, Block, Cluster, Grama Panchayat)
class BoundaryAPIView(generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class = BoundarySerializer
    queryset = Boundary.objects.all()

# This api view lists the GP Contest Data (District, Block, Cluster, Grama Panchayat,
# Addition, Subtraction, Multiplication and Division)
class GPContestAPIView(generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class = GPContestSerializer
    queryset = GPContest.objects.all()

# This api view aggregates the results (addition, subtraction, multiplication, division)
# based on the search parameters in the url.
class GPContestAggregateAPIView(APIView):
    def get(self, request, format=None):
        qs = GPContest.objects.all()
        qschool = School.objects.all()
        q_param = list(self.request.GET.keys())
        k = q_param[0]
        query = self.request.GET.get(k)
        content = {}
        if hasattr(GPContest, k) or hasattr(School, k):
            if k == 'district':
                qs = qs.filter(district=query).aggregate(
                    addition=Avg('addition')*100,
                    subtraction=Avg('subtraction')*100,
                    multiplication=Avg('multiplication')*100,
                    division=Avg('division')*100)
                if qs['addition'] is None:
                    return Response({'Error': '{} does not exist.'.format(query)}, status=status.HTTP_404_NOT_FOUND)
                else:
                    content['district'] = query
                    content = GPContestAggregateAPIView.resDict(content, qs)
            elif k == 'block':
                qs = qs.filter(block=query).aggregate(
                    addition=Avg('addition')*100,
                    subtraction=Avg('subtraction')*100,
                    multiplication=Avg('multiplication')*100,
                    division=Avg('division')*100)
                if qs['addition'] is None:
                    return Response({'Error': '{} does not exist.'.format(query)}, status=status.HTTP_404_NOT_FOUND)
                else:
                    content['block'] = query
                    content = GPContestAggregateAPIView.resDict(content, qs)
            elif k == 'cluster':
                qs = qs.filter(cluster=query).aggregate(
                    addition=Avg('addition')*100,
                    subtraction=Avg('subtraction')*100,
                    multiplication=Avg('multiplication')*100,
                    division=Avg('division')*100)
                if qs['addition'] is None:
                    return Response({'Error': '{} does not exist.'.format(query)}, status=status.HTTP_404_NOT_FOUND)
                else:
                    content['cluster'] = query
                    content = GPContestAggregateAPIView.resDict(content, qs)
            elif k == 'gram_panchayat':
                qs = qs.filter(gram_panchayat=query).aggregate(
                    addition=Avg('addition')*100,
                    subtraction=Avg('subtraction')*100,
                    multiplication=Avg('multiplication')*100,
                    division=Avg('division')*100)
                if qs['addition'] is None:
                    return Response({'Error': '{} does not exist.'.format(query)}, status=status.HTTP_404_NOT_FOUND)
                else:
                    content['gram_panchayat'] = query
                    content = GPContestAggregateAPIView.resDict(content, qs)
            elif k == 'schoolname':
                qschool = qschool.filter(schoolname=query).aggregate(
                    addition=Avg('addition')*100,
                    subtraction=Avg('subtraction')*100,
                    multiplication=Avg('multiplication')*100,
                    division=Avg('division')*100)
                if qschool['addition'] is None:
                    return Response({'Error': '{} does not exist.'.format(query)}, status=status.HTTP_404_NOT_FOUND)
                else:
                    content['name_of_school'] = query
                    content = GPContestAggregateAPIView.resDict(content, qschool)
        else:
            return Response({'Error': '{} does not exist'.format(k)}, status=status.HTTP_404_NOT_FOUND)
        return Response(content, status=status.HTTP_200_OK)    

    @staticmethod
    def resDict(content, qs):
        content['addition'] = round(qs['addition'], 2)
        content['subtraction'] = round(qs['subtraction'], 2)
        content['multiplication'] = round(qs['multiplication'], 2)
        content['division'] = round(qs['division'], 2)

        return content



