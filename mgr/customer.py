import json
from django.http import JsonResponse

from sales.views import listcustomers, addcustomer, modifycustomer, deletecustomer


def dispatcher(request):
    # 将请求参数统一放入request的params属性中，方便后续处理

    # GET请求 参数在url中，通过request对象的 GET属性获取
    if request.method == 'GET':
        request.params = request.GET
        print('request.params', request.params)

    if 'usertype' not in request.session:
        return JsonResponse({'ret': 302, 'msg': '未登录', 'redirect': '/mgr/sign.html'}, status=302)

    if request.session['usertype'] != 'mgr':
        return JsonResponse({'ret': 302, 'msg': '用户非mgr类型', 'redirect': '/mgr/sign.html'}, status=302)

    # POST/PUT/DELETE请求 参数 从 request对象的body属性中获取
    elif request.method in ['POST', 'DELETE', 'PUT']:
        request.params = json.loads(request.body)
        print('request.params', request.params)

    # 根据不同的action分派给不同的函数进行处理
    action = request.params['action']
    if action == 'list_customer':
        return listcustomers(request)
    elif action == 'add_customer':
        return addcustomer(request)
    elif action == 'modify_customer':
        return modifycustomer(request)
    elif action == 'del_customer':
        return deletecustomer(request)

    else:
        return JsonResponse({'ret': 1, 'msg': '不支持该类型http请求'})