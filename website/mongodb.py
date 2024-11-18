# import os
# import django

# # إعداد Django
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')  # استبدل 'your_project' باسم مشروعك
# django.setup()

# from shift_api.models import Product  # استبدل 'your_app' باسم تطبيقك

# try:
#     product1 = Product(name='منتج مثال 1', price=50.00, description='وصف المنتج 1')
#     product1.save()
#     print("تم إضافة المنتج 1 بنجاح")
# except Exception as e:
#     print(f"حدث خطأ أثناء إضافة المنتج 1: {e}")

# try:
#     product2 = Product(name='منتج مثال 2', price=75.00, description='وصف المنتج 2')
#     product2.save()
#     print("تم إضافة المنتج 2 بنجاح")
# except Exception as e:
#     print(f"حدث خطأ أثناء إضافة المنتج 2: {e}")




import os
import django
from pymongo import MongoClient

# تعيين متغير البيئة
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")

# إعداد Django
django.setup()

# الاتصال بقاعدة البيانات
client = MongoClient('mongodb://localhost:27017/')
db = client['shift_start']

collection_names = db.list_collection_names()

# اختبار الاتصال
try:
    db.command("ping")  # هذا الأمر يتحقق من الاتصال
    print("conected")
except Exception as e:
    print("error", e)

print("Collections in the database:")
for name in collection_names:
    print(name)