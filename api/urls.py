from django.urls import path
from .views import BoundaryAPIView, GPContestAPIView, GPContestAggregateAPIView

app_name = 'api'

urlpatterns = [
    path('boundaries/', BoundaryAPIView.as_view(), name='list-boundaries'),
    path('gpcontest/', GPContestAPIView.as_view(), name='list-gpcontest'),
    path('gpcontest/aggregate', GPContestAggregateAPIView.as_view(), name='aggregate-gpcontest'),
]

# Examples
# GET boundaries/

#RESPONSE:
'''
{
    "count": 2,
    "next": "http://localhost:8000/api/boundaries/?limit=5&offset=5",
    "previous": null,
    "results": [
        {
            "pk": 1,
            "district": "Chamarajanagara",
            "block": "Chamaraja nagar",
            "cluster": "Bagali",
            "gram_panchayat": "Demahalli"
        },
        {
            "pk": 2,
            "district": "Ballari",
            "block": "Siruguppa",
            "cluster": "Talur",
            "gram_panchayat": "Uththanuru"
        },
}
'''
# GET gpcontest/

#RESPONSE
'''
{
    "count": 2,
    "next": "http://localhost:8000/api/gpcontest/?limit=5&offset=5",
    "previous": null,
    "results": [
        {
            "district": "Chamarajanagara",
            "block": "Chamaraja nagar",
            "cluster": "Bagali",
            "gram_panchayat": "Demahalli",
            "addition": 0,
            "subtraction": 1,
            "multiplication": 0,
            "division": 0
        },
        {
            "district": "Chamarajanagara",
            "block": "Chamaraja nagar",
            "cluster": "Bagali",
            "gram_panchayat": "Demahalli",
            "addition": 1,
            "subtraction": 1,
            "multiplication": 0,
            "division": 1
        },
}
'''

# GET /gpcontest/aggregate?district=Ballari

# Note: We can replace district with block or cluster or grampanchayat or schoolname
# to get results based on query parameters.

#RESPONSE:
'''
{
    "district": "Ballari",
    "addition": 83.43,
    "subtraction": 69.82,
    "multiplication": 43.79,
    "division": 59.17
}
'''