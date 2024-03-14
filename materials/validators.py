import re

from rest_framework.exceptions import ValidationError


def validate_youtube_url(value):
    youtube_regex = r'https?://(www.)?youtube.com'

    if not re.search(youtube_regex, value):
        raise ValidationError('This field must contain a URL from www.youtube.com')
