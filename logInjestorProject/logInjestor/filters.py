from django_filters import rest_framework as filters
from .models import LogEntry

class LogEntryFilter(filters.FilterSet):
    """
    FilterSet for LogEntry model, enabling filtering based on specified fields.

    Attributes:
        level (CharFilter): Filter log entries based on the log level (case-insensitive).
        message (CharFilter): Filter log entries based on the log message (case-insensitive).
        resourceId (CharFilter): Filter log entries based on the resource identifier.
        timestamp (DateTimeFromToRangeFilter): Filter log entries based on a range of timestamps.
        traceId (CharFilter): Filter log entries based on the trace identifier.
        spanId (CharFilter): Filter log entries based on the span identifier.
        commit (CharFilter): Filter log entries based on the commit identifier.
        parentResourceId (CharFilter): Filter log entries based on the parent resource identifier in metadata.

    Example:
        To filter log entries with a specific level:
        GET /logentries/?level=INFO

        To filter log entries with a specific message:
        GET /logentries/?message=error

        To filter log entries within a timestamp range:
        GET /logentries/?timestamp_after=2023-01-01T00:00:00&timestamp_before=2023-12-31T23:59:59

        To filter log entries based on parent resource identifier in metadata:
        GET /logentries/?parentResourceId=456
    """

    level = filters.CharFilter(lookup_expr='icontains')
    message = filters.CharFilter(lookup_expr='icontains')
    resourceId = filters.CharFilter()
    timestamp = filters.DateTimeFromToRangeFilter()
    traceId = filters.CharFilter()
    spanId = filters.CharFilter()
    commit = filters.CharFilter()
    parentResourceId = filters.CharFilter(field_name='metadata__parentResourceId', lookup_expr='icontains')

    class Meta:
        model = LogEntry
        fields = ['level', 'message', 'resourceId', 'timestamp', 'traceId', 'spanId', 'commit', 'parentResourceId']
