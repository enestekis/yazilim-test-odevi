import re
from datetime import datetime

def validate_registration(first_name, last_name, email, dob, password, confirm_password):
    # İsim ve Soyisim kontrolü (Boş olamaz)
    if not first_name or not last_name:
        return False
        
    # E-mail kontrolü (İçinde @ ve . olmalı)
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return False
        
    # Doğum Tarihi kontrolü (dd/mm/yyyy formatında ve geçmiş bir tarih olmalı)
    try:
        birth_date = datetime.strptime(dob, "%d/%m/%Y")
        if birth_date > datetime.now():
            return False
    except ValueError:
        return False
        
    # Şifre kontrolü (En az 8 karakter olmalı - Sınır Değer)
    if len(password) < 8:
        return False
        
    # Şifre eşleşme kontrolü
    if password != confirm_password:
        return False
        
    return True