from django.shortcuts import render, redirect
from mongoengine import DoesNotExist, NotUniqueError
from django.shortcuts import get_object_or_404
from .models import Users
from django.contrib import messages  

def delete_user(request, username):
    current_user = request.user

    if current_user.is_admin:
        user_to_delete = Users.objects(username=username).first()
        if user_to_delete:
            user_to_delete.delete()
            messages.success(request, 'تم حذف المستخدم بنجاح.')
        else:
            messages.error(request, 'المستخدم غير موجود.')
    else:
        messages.error(request, 'ليس لديك الصلاحيات الكافية لحذف هذا المستخدم.')

    return redirect('user_list')


# ///////////////////////////////////////////////////////





def user_list(request, username=None, user_id=None):
    if user_id:
        user = get_object_or_404(Users, id=user_id)
        users = [user]
        username = user.username
    else:
        users = Users.objects.all()
        username = None

    return render(request, 'registration/user_list.html', {  
        'users': users,
        'current_user': request.user,
        'username': username,
        'user_id': user_id
    })



# ///////////////////////////////////////////////////////




def register_user(request):
    error_message = None

    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        permissions = request.POST.getlist('permissions')

        try:
            new_user = Users(username=username, email=email)
            new_user.set_password(password)
            new_user.permissions = permissions
            new_user.save()

            return redirect('home', username=new_user.username, user_id=new_user.id)
        except NotUniqueError:
            error_message = "اسم المستخدم موجود بالفعل."
        except Exception as e:
            error_message = str(e)

    return render(request, 'registration/register.html', {'error_message': error_message}) 
  


# ///////////////////////////////////////////////////////



def login_user(request):
    error_message = None

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = Users.objects.get(username=username)

            if user.check_password(password):
                if username == 'Admin0' and password == '$2b$12$BONq5bFrM61nq/x6Vz3K/O9pSb0.K7Tm86tRfFUqFqafNUzRgJ8Cu':
                    return redirect('user_list')
                else:
                    return redirect('home', username=username, user_id=user.id)
            else:
                error_message = "كلمة المرور غير صحيحة."

        except DoesNotExist:
            error_message = "اسم المستخدم غير موجود."
        except Exception as e:
            error_message = str(e)

    return render(request, 'registration/login.html', {'error_message': error_message})  

def home_view(request, username, user_id):
    return render(request, 'registration/home.html', {  
        'username': username,
        'user_id': user_id
    })



# ///////////////////////////////////////////////////////



def index(request):
    return render(request, 'registration/index.html')  