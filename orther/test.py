from django.db import connection
import os
import django

# Đặt đường dẫn đến settings của dự án Django của bạn
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Website.settings')

# Khởi tạo môi trường Django
django.setup()


# Thực hiện truy vấn SQL trực tiếp
with connection.cursor() as cursor:
    cursor.execute("SELECT * FROM account")
    results = cursor.fetchall()

for row in results:
    print(row)

