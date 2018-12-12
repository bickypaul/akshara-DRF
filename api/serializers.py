from rest_framework import serializers
from .models import Boundary, GPContest

# Boundary Serializers.
class BoundarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Boundary
        fields = [
            'pk',
            'district',
            'block',
            'cluster',
            'gram_panchayat',
        ]

        read_only_fields = [
            'pk',
            'district',
            'block',
            'cluster',
            'gram_panchayat',
        ]


#GP contest Serializer
class GPContestSerializer(serializers.ModelSerializer):
    class Meta:
        model = GPContest
        fields = [
            'district',
            'block',
            'cluster',
            'gram_panchayat',
            'addition',
            'subtraction',
            'multiplication',
            'division',
        ]

        read_only_fields = [
            'district',
            'block',
            'cluster',
            'gram_panchayat',
            'addition',
            'subtraction',
            'multiplication',
            'division',
        ]
