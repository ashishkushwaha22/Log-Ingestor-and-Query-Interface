from django.shortcuts import render
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated, IsAdminUser
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST

from .models import LogEntry
from .serializers import LogEntrySerializer, UserLoginSerializer
from .filters import LogEntryFilter

class LogEntryViewSet(viewsets.ModelViewSet):
    """
    ViewSet for handling CRUD operations on LogEntry model.

    Attributes:
        queryset (QuerySet): Set of LogEntry objects.
        serializer_class (LogEntrySerializer): Serializer class for LogEntry model.
        filter_backends (list): List of filter backends for the view.
        search_fields (list): List of fields to enable search functionality.
        filterset_class (LogEntryFilter): Filterset class for more advanced filtering.

    Methods:
        get_queryset: Custom method to filter queryset based on regex parameter.

    Example:
        To retrieve all log entries:
        GET /logentries/

        To retrieve log entries with a specific level:
        GET /logentries/?level=INFO

        To search for log entries with a specific message:
        GET /logentries/?search=error

        To filter log entries using a regex pattern in the message:
        GET /logentries/?regex=pattern
    """

    """
    Role-Based Access Control-
    
    IsAuthenticatedOrReadOnly: Any user, whether authenticated or not, can perform read operations (GET requests).
    Only authenticated users (those with a valid token or session) are allowed to perform write operations (POST, PUT, PATCH, DELETE requests).

    Uncomment below code to enable Role-Based Access Control, Get token from login/ API,
    then add it in header of request.
    """
    # permission_classes = [IsAuthenticatedOrReadOnly] 

    queryset = LogEntry.objects.all()
    serializer_class = LogEntrySerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['level', 'message', 'resourceId', 'traceId', 'spanId', 'commit', 'metadata__parentResourceId']
    filterset_class = LogEntryFilter

    def get_queryset(self):
        """
        Custom method to filter the queryset based on regex parameter.

        Example:
            To retrieve log entries with a message matching a regex pattern:
            GET /logentries/?regex=pattern
        """
        queryset = super().get_queryset()
        regex = self.request.query_params.get('regex', None)
        if regex:
            queryset = queryset.filter(message__iregex=regex)
        return queryset
    

class LoginAPIView(APIView):
    """
    API view to Login User and Get Auth token
    """

    # overiding the POST method
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            token, _ = Token.objects.get_or_create(user=user) #getting auth token for User. GET it already present or CREATE it not.
            return Response({
                'username': user.username,
                'token': token.key
            }, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
