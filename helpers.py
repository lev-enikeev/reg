import base64

def encode_email(email):
    encoded = base64.b64encode(email.encode('utf-8'))
    return f'http://localhost:8000/confirm/?email={encoded.decode("utf-8")}'

def decode_email(encoded_email):
    return base64.b64decode(encoded_email).decode('utf-8')
