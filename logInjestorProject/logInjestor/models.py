from django.db import models

class LogEntry(models.Model):
    """
    Model representing a log entry in the system.

    Attributes:
        level (str): The log level, e.g., 'INFO', 'ERROR', etc.
        message (str): The log message providing details about the event.
        resourceId (str): Identifier for the resource associated with the log entry.
        timestamp (datetime): The timestamp when the log entry was created.
        traceId (str): Identifier for distributed tracing.
        spanId (str): Identifier for the span of the distributed trace.
        commit (str): Identifier for the version or commit related to the log entry.
        metadata (dict): Additional metadata stored as JSON.

    Methods:
        __str__: Human-readable representation of the log entry.

    Example:
        log_entry = LogEntry(
            level='INFO',
            message='Application started',
            resourceId='123',
            timestamp=datetime.now(),
            traceId='abc123',
            spanId='xyz456',
            commit='abc789',
            metadata={'key': 'value'}
        )
    """

    level = models.CharField(max_length=255, db_index=True)
    message = models.TextField(db_index=True)
    resourceId = models.CharField(max_length=255, db_index=True)
    timestamp = models.DateTimeField(db_index=True)
    traceId = models.CharField(max_length=255, db_index=True)
    spanId = models.CharField(max_length=255, db_index=True)
    commit = models.CharField(max_length=255, db_index=True)
    metadata = models.JSONField()

    def __str__(self):
        """
        Returns a human-readable string representation of the log entry.

        Example:
            "INFO - Application started"
        """
        return f"{self.level} - {self.message}"
