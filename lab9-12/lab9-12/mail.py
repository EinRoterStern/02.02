import re
from typing import Pattern

def check_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,4}(?:\.[a-zA-Z]{2,4})?$'
    return bool(re.match(pattern,email))
