from django.conf import settings

def datetime_to_str(datetime):
    return datetime.strftime(settings.DATETIME_INPUT_FORMATS[0])
