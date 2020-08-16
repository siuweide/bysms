import json
from django.http import JsonResponse

def dispatcherBase(request, action2HandlerTable):

    if 'usertype' not in request.session:
        return JsonResponse({'ret': 302, 'msg': '未登录', 'redirect': '/mgr/sign.html'}, status=302)

    if request.session['usertype'] != 'mgr':
        return JsonResponse({'ret': 302, 'msg': '用户非mgr类型', 'redirect': '/mgr/sign.html'}, status=302)

    # GET请求 参数在url中，通过request对象的 GET属性获取
    if request.method == 'GET':
        request.params = request.GET
        print('request.params', request.params)

    elif request.method in ['POST', 'DELETE', 'PUT']:
        request.params = json.loads(request.body)
        print('request.params', request.params)

    action = request.params['action']
    if action in action2HandlerTable:
        handlerFunc = action2HandlerTable[action]
        return handlerFunc(request)
    else:
        return JsonResponse({'ret': 1, 'msg': 'action参数错误'})