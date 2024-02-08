#!/usr/bin/env python3
"""_summary_

This module contains a function called
`filter_datum` that takes in a list
of fields, a redaction string, a
log message, and a separator. It
obfuscates the log message by replacing
occurrences of the fields with the redaction string.

Example:
    fields = ['password', 'credit_card']
    redaction = '***'
    message = 'User: john, password: secret, credit_card: 1234567890'
    separator = ': '
    filtered_message = filter_datum(fields, redaction, message, separator)
    print(filtered_message)
    # Output: 'User: john, password: ***, credit_card: **********'
"""
import re
from typing import List, Tuple
import logging


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    class RedactingFormatter(logging.Formatter):
        """
        Custom log formatter that redacts sensitive information.
        """

        def __init__(self, fields: Tuple[str, ...]):
            """
            Initialize the RedactingFormatter.

            Args:
                fildes (List[str]): List of sensitive fields to redact.
            """
            super(RedactingFormatter, self).__init__(self.FORMAT)
            self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
            """
            Formats the log record by filtering sensitive data.

            Args:
                record (logging.LogRecord): The log record to be formatted.

            Returns:
                str: The formatted log record.
            """
            record.msg = filter_datum(record.msg, self.REDACTION,
                                      self.FORMAT, self.SEPARATOR)
            return super(RedactingFormatter, self).format(record)


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """
    Obfuscates sensitive data in a log message.

    Args:
        fields (list): List of sensitive fields to be obfuscated.
        redaction (str): String used for obfuscation.
        message (str): Log message to be obfuscated.
        separator (str): Separator used to separate fields in the log message.

    Returns:
        str: Obfuscated log message.
    """
    for f in fields:
        message = re.sub(f'{f}=.*?{separator}',
                         f'{f}={redaction}{separator}', message)
    return message
