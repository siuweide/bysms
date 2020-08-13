import json

from django.http import JsonResponse

from order.views import addorder, listorder


def dispatcher(request):
    # 根据session判断用户是否登录的管理员账号
    if 'usertype' not in request.session:
        return JsonResponse({'ret': 302, 'msg': '未登录', 'redirect':'/mgr/sign.html'}, status=302)

    if request.session['usertype'] != 'mgr':
        return JsonResponse({'ret': 302, 'msg': '用户非mgr类型', 'redirect': '/mgr/sign.html'}, status=302)

    # 将请求参数统一放入request的params属性中，方便后续处理

    #GET请求 参数 在request对象的 GET属性中
    if request.method == 'GET':
        request.params = request.GET
        print('request.params-------->', request.params)

    # POST/PUT/DELETE请求 参数 从request 对象的body属性中获取
    elif request.method in ['POST', 'PUT', 'DELETE']:
        # 根据接口，POST/PUT/DELETE请求的消息体都是json格式
        request.params = json.loads(request.body)

    # 根据不同的action分派给不同的函数进行处理
    action = request.params['action']
    if action == 'list_order':
        return listorder(request)
    elif action == 'add_order':
        return addorder(request)

    # 订单暂不支持修改和删除
    else:
        return JsonResponse({'ret': 1, 'msg': '不支持该类型http请求'})