from django.shortcuts import render, redirect
from ..forms import RegistrationForm, LoginForm 
from ..models import User


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('login')
            except Exception as e:
                print(f"Error saving user: {e}")  # طباعة الخطأ في وحدة التحكم
                form.add_error(None, 'حدث خطأ أثناء التسجيل. يرجى المحاولة مرة أخرى.')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})




def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            try:
                user = User.objects.get(username=username, password=password)
                return redirect('index')  # استبدل بـ URL الصفحة الرئيسية
            except User.DoesNotExist:
                form.add_error(None, 'اسم المستخدم أو كلمة المرور غير صحيحة')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})