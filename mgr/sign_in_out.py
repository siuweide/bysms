from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout

# 登录处理
def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_active:
                if user.is_superuser:
                    login(request, user)
                    # 在session中存入用户类型
                    request.session['usertype'] = 'mgr'
                    return JsonResponse({'ret': 0})
                else:
                    return JsonResponse({'ret': 1, 'msg': '请使用管理员账号登录'})
            else:
                return JsonResponse({'ret': 1, 'msg': '用户已被禁用'})
        else:
            return JsonResponse({'ret': 1, 'msg': '用户名或密码错误'})
    else:
        return JsonResponse({'ret': 1, 'msg': '请检查是否为post请求方法'})

# 登出处理
def signout(request):
    if request.method == 'POST':
        logout(request)
        return JsonResponse({'ret': 0})
    else:
        return JsonResponse({'ret': 1, 'msg': '请检查是否为post请求方法'})