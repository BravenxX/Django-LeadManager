from rest_framework import serializers
from leads.models import Lead

# Lead serializer


class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
     #  fields = (name, ...)
        fields = '__all__'
