# akshara-DRF
A django rest framework based django project.

## Requirements (Tested on)
1. Ubuntu 18.04
2. Python 3
3. django 2.1.2
4. django rest framework (latest)
4. postgresql (latest)

## To populate the database from the CSV file.
1. git clone https://github.com/bickypaul/akshara-DRF/
2. cd akshara/
3. Make sure you have configured your database with postgresql in the settings.py file.
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'database name',
        'USER': 'your db user name',
        'PASSWORD': 'your password',
        'HOST': 'localhost',
        'PORT': '',
    }
}
```
4. python3 manage.py makemigrations
5. python3 manage.py migrate
6. python3 manage.py createsuperuser
7. pip3 install django-postgres-copy
8. python3 manage.py shell
```
from api.models import Boundary, GPContest, School
from postgres_copy import CopyMapping
b = CopyMapping(Boundary, 'boundaries.csv', dict(district='District', block='Block', cluster='Cluster', gram_panchayat='Grama Panachayat'))
b.save()
```
9. Similary for other two models we will do.
10. Map the model fields with the headers in csv within the dict function as shown above.
```
gp = CopyMapping(GPContest, 'contest.csv', dict(district='District', block='Block', cluster='Cluster', gram_panchayat='Grama Panachayat', addition='Addition', subtraction='Subtraction', multiplication='Multiplication', division='Division'))
gp.save()

s = CopyMapping(School, 'school.csv', dict(schoolname='Name of the school', addition='Addition', subtraction='Subtraction', multiplication='Multiplication', division='Division'))
s.save()
```
11. Note: district, block, cluster and gram_panchayat are the model fields for Boundary Table.
12. Model fields for GPContest table are: district, block, cluster, gram_panchayat, addition, subtraction, multiplication and division 
13. Model fields for School table are: schoolname, addition, subtraction, multiplication, division.
14. CSV file for GPContest table is 'contest.csv'
15. CSV file for School table is 'school.csv'
16. After populating the database exit from the shell.


## How to execute it to run on your local machine
1. python3 manage.py runserver
2. Goto http://localhost:8000

## API Endpoints.
### GET http://localhost:8000/api/boundaries/
1. It lists all Boundaries cotaining Ditrict, Block, Cluster, Grama Panchayat, for example:
```json
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
```

### GET http://localhost:8000/api/gpcontest/
1. It list the results along with Boundaries containing District, Block, Cluster, Grama Panchayat, addition, subtraction, multiplication, division. For example:
```json
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
```
### GET http://localhost:8000/api/gpcontest/aggregate?district=Ballari
1. It will aggregate the results of the District and represent in percentages of addition, subraction, multiplication and division respectively. for example:
```json
{
    "district": "Ballari",
    "addition": 83.43,
    "subtraction": 69.82,
    "multiplication": 43.79,
    "division": 59.17
}
```
2. similarly it will show up results for block, cluster, grampanchayat, schoolname. other results are:
#### http://localhost:8000/api/gpcontest/aggregate?block=Chintamani
```json
{
    "block": "Chintamani",
    "addition": 76.32,
    "subtraction": 71.05,
    "multiplication": 28.95,
    "division": 52.63
}
```
#### http://localhost:8000/api/gpcontest/aggregate?cluster=Dambal
```json
{
    "cluster": "Dambal",
    "addition": 92.31,
    "subtraction": 97.44,
    "multiplication": 89.74,
    "division": 94.87
}
```
#### http://localhost:8000/api/gpcontest/aggregate?gram_panchayat=Demahalli
```json
{
    "gram_panchayat": "Demahalli",
    "addition": 65.38,
    "subtraction": 50.0,
    "multiplication": 0.0,
    "division": 26.92
}
```
#### http://localhost:8000/api/gpcontest/aggregate?schoolname=GHPS%20MALLIGAHALLI
```json
{
    "name_of_school": "GHPS MALLIGAHALLI",
    "addition": 75.0,
    "subtraction": 62.5,
    "multiplication": 6.25,
    "division": 31.25
}
```


