import unittest
from validator import validate_registration

class TestRegistrationFlow(unittest.TestCase):

    def setUp(self):
        # Her testten önce çalışır. (Hocanın istediği Setup metodu)
        print("Test basliyor...")

    def tearDown(self):
        # Her testten sonra çalışır. (Hocanın istediği Teardown metodu)
        print("Test bitti. Veriler temizleniyor...")

    # 1. Başarılı Kayıt (Geçerli Sınıf)
    def test_valid_registration(self):
        self.assertTrue(validate_registration("Ali", "Yilmaz", "ali@test.com", "15/05/1995", "Password123", "Password123"))

    # 2. İsim boş bırakılmış (Geçersiz Sınıf)
    def test_empty_first_name(self):
        self.assertFalse(validate_registration("", "Yilmaz", "ali@test.com", "15/05/1995", "Password123", "Password123"))

    # 3. Soyisim boş bırakılmış
    def test_empty_last_name(self):
        self.assertFalse(validate_registration("Ali", "", "ali@test.com", "15/05/1995", "Password123", "Password123"))

    # 4. Hatalı E-posta - @ işareti yok (Equivalence Partitioning)
    def test_invalid_email_no_at(self):
        self.assertFalse(validate_registration("Ali", "Yilmaz", "alitest.com", "15/05/1995", "Password123", "Password123"))

    # 5. Hatalı E-posta - domain yok
    def test_invalid_email_no_domain(self):
        self.assertFalse(validate_registration("Ali", "Yilmaz", "ali@", "15/05/1995", "Password123", "Password123"))

    # 6. Hatalı Tarih Formatı (Tire ile ayrılmış)
    def test_invalid_dob_format(self):
        self.assertFalse(validate_registration("Ali", "Yilmaz", "ali@test.com", "15-05-1995", "Password123", "Password123"))

    # 7. Gelecekte bir tarih girilmiş
    def test_future_dob(self):
        self.assertFalse(validate_registration("Ali", "Yilmaz", "ali@test.com", "15/05/2050", "Password123", "Password123"))

    # 8. Olmayan bir gün girilmiş (32 Mayıs)
    def test_invalid_dob_day(self):
        self.assertFalse(validate_registration("Ali", "Yilmaz", "ali@test.com", "32/05/1995", "Password123", "Password123"))

    # 9. Şifre 8 karakter (Boundary Value Analysis - Sınırda geçerli)
    def test_password_exact_8_chars(self):
        self.assertTrue(validate_registration("Ali", "Yilmaz", "ali@test.com", "15/05/1995", "12345678", "12345678"))

    # 10. Şifre 7 karakter (Boundary Value Analysis - Sınırın hemen altı geçersiz)
    def test_password_7_chars(self):
        self.assertFalse(validate_registration("Ali", "Yilmaz", "ali@test.com", "15/05/1995", "1234567", "1234567"))

    # 11. Şifreler eşleşmiyor
    def test_passwords_do_not_match(self):
        self.assertFalse(validate_registration("Ali", "Yilmaz", "ali@test.com", "15/05/1995", "Password123", "Password321"))

    # 12. Şifre tekrarı boş bırakılmış
    def test_empty_confirm_password(self):
        self.assertFalse(validate_registration("Ali", "Yilmaz", "ali@test.com", "15/05/1995", "Password123", ""))

    # 13. Şifre boş bırakılmış
    def test_empty_password(self):
        self.assertFalse(validate_registration("Ali", "Yilmaz", "ali@test.com", "15/05/1995", "", ""))

    # 14. E-posta alanı tamamen boş (Equivalence Partitioning - Boş girdi)
    def test_empty_email(self):
        self.assertFalse(validate_registration("Ali", "Yilmaz", "", "15/05/1995", "Password123", "Password123"))

    # 15. Çok uzun bir şifre girilmesi (100 karakter)
    def test_very_long_password(self):
        long_pass = "a" * 100
        self.assertTrue(validate_registration("Ali", "Yilmaz", "ali@test.com", "15/05/1995", long_pass, long_pass))

if __name__ == '__main__':
    unittest.main()