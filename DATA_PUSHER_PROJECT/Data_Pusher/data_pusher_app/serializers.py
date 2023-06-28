from rest_framework import serializers
from .models import Account, Destination

class AccountSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Account
        fields = ('account_id','url','email_id','account_name','app_secret_token','website')
        read_only_fields = ('account_id','app_secret_token')

class DestinationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Destination
        fields = ('id','account','url','http_method','headers')
        read_only_fields = ('id','url',)

    def create(self, validated_data):
        request = self.context['request']
        url = request.build_absolute_uri()
        validated_data['url'] = url
        return super().create(validated_data)

class PostSerializer(serializers.ModelSerializer):
    class MySerializer(serializers.Serializer):

        Dest_url = serializers.URLField()
        http_method = serializers.CharField(max_length=10)
        headers = serializers.JSONField()
        data = serializers.JSONField()