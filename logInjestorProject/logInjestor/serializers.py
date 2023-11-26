from rest_framework import serializers
from .models import LogEntry
from django.contrib.auth import authenticate

class MetadataSerializer(serializers.Serializer):
    """
    Serializer for metadata field in LogEntry model.

    Attributes:
        parentResourceId (str): Identifier for the parent resource.

    Example:
        metadata_data = {'parentResourceId': '123'}
        metadata_serializer = MetadataSerializer(data=metadata_data)
        if metadata_serializer.is_valid():
            metadata_instance = metadata_serializer.save()
    """
    parentResourceId = serializers.CharField(max_length=255)

class LogEntrySerializer(serializers.ModelSerializer):
    """
    Serializer for the LogEntry model.

    Attributes:
        metadata (MetadataSerializer): Serializer for the metadata field.

    Example:
        log_entry_data = {
            'level': 'INFO',
            'message': 'Application started',
            'resourceId': '123',
            'timestamp': '2023-11-18T12:00:00',
            'traceId': 'abc123',
            'spanId': 'xyz456',
            'commit': 'abc789',
            'metadata': {'parentResourceId': '456'}
        }
        log_entry_serializer = LogEntrySerializer(data=log_entry_data)
        if log_entry_serializer.is_valid():
            log_entry_instance = log_entry_serializer.save()
    """

    metadata = MetadataSerializer()

    class Meta:
        model = LogEntry
        fields = '__all__'


class UserLoginSerializer(serializers.Serializer):
    """
    Serializer class for Login User
    """

    username = serializers.CharField()
    password = serializers.CharField(style={'input_type': 'password'})

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        if username and password:
            user = authenticate(username=username, password=password) #using the authenticate() method from django.contrib.auth
            if not user:
                raise serializers.ValidationError('Invalid username or password.')
        else:
            raise serializers.ValidationError('Must include both username and password.')
        
        data['user'] = user
        return data