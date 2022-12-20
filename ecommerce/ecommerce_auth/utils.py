import re

import phonenumbers
from django.core.exceptions import ValidationError
from phonenumbers import geocoder

# def normalize_phone_number(phonenumber):
#     key = "+20"
#     if phonenumber[0:3] == key:
#         phonenumber = phonenumbers.parse(phonenumber)
#         if not phonenumbers.is_valid_number(phonenumber):
#             raise ValueError("the phone number is not valid")
#         user_number = re.findall("Number: ([0-9]*)", str(phonenumber))
#         user_number = user_number[0]
#         country = geocoder.description_for_number(phonenumber, "en")
#     else:
#         raise ValidationError("EGY number only")


# def get_country(phonenumber):
#     key = "+20"
#     if phonenumber[0:3] == key:
#         phonenumber = phonenumbers.parse(phonenumber)
#         if not phonenumbers.is_valid_number(phonenumber):
#             raise ValueError("the phone number is not valid")
#         country = geocoder.description_for_number(phonenumber, "en")
#     else:
#         raise ValidationError("EGY number only")


def normalize_phone_number(phonenumber):
    key = "+20"
    if phonenumber[0:3] == key:
        phonenumber = phonenumbers.parse(phonenumber)
        if not phonenumbers.is_valid_number(phonenumber):
            raise ValidationError("the phone number is not valid")
        user_number = re.findall("Number: ([0-9]*)", str(phonenumber))
        user_number = user_number[0]
        country = geocoder.description_for_number(phonenumber, "en")
        return country + "," + user_number
    else:
        raise ValidationError("EGY number only")


# normalize_phone_number(phonenumber).split(',')[1] ==> phone
# normalize_phone_number(phonenumber).split(',')[0] ==> country
