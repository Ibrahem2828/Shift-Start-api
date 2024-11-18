from mongoengine import Document, StringField, EmailField, ListField, BooleanField
import bcrypt
from django.db import models


class Users(Document):
    username = StringField(required=True, unique=True)
    email = StringField(required=True, unique=True)
    password = StringField(required=True)
    is_admin = BooleanField(default=False)  # حقل لتحديد ما إذا كان المستخدم إداريًا
    permissions = ListField(StringField())  # حقل لتخزين الصلاحيات

    def __str__(self):
        return self.username

    def set_password(self, raw_password):
        # تشفير كلمة المرور
        self.password = bcrypt.hashpw(raw_password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    def check_password(self, raw_password):
        # التحقق من كلمة المرور
        return bcrypt.checkpw(raw_password.encode('utf-8'), self.password.encode('utf-8'))
