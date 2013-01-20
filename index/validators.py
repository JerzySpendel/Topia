from django.core.exceptions import ValidationError

def validate_password(value):
  if len(value) <= 5:
    raise ValidationError(u'Password must have at least 6 characters')
