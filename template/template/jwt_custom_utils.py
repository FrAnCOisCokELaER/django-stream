import jwt
import base64
from rest_framework_jwt.settings import api_settings


def jwt_get_username_from_payload_handler(payload):
    """
    Override this function if username is formatted differently in payload
    """
    return payload.get('sub')


def jwt_decode_handler(token):
    options = {
        'verify_exp': False,
        'verify_signature': True,
        'verify_sub': False,  # jhipster token is containing a sub claim
    }
    # get user from token, BEFORE verification, to get user secret key
    unverified_payload = jwt.decode(token, None, False)
    # secret_key = jwt_get_secret_key(unverified_payload)
    secret_key = api_settings.JWT_SECRET_KEY
    return jwt.decode(token, base64.b64decode(secret_key), algorithms='HS512', options=options)
