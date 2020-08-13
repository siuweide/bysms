from django.http import JsonResponse
from common.models import Customer

def listcustomers(request):
    obj = list(Customer.objects.values())
    return JsonResponse({"ret":0, "retlist":obj})

def addcustomer(request):
    info = request.params['data']

    print('info------------>', info)
    # 从请求消息中  获取要添加客户的信息
    # 并且插入到数据库中
    # 返回值 就是对应插入记录的对象
    record = Customer.objects.create(name=info['name'],
                                     phonenumber=info['phonenumber'],
                                     address=info['address'])

    return JsonResponse({'ret':0, 'id': record.id})

def modifycustomer(request):

    customerid = request.params['id']
    newdata = request.params['newdata']

    try:
        customer = Customer.objects.get(id=customerid)
    except Customer.DoesNotExist:
        return {'ret':1, 'msg': f'id为`{customerid}`的客户不存在'}

    if 'name' in newdata:
        customer.name = newdata['name']
    if 'phonenumber' in newdata:
        customer.phonenumber = newdata['phonenumber']
    if 'address' in newdata:
        customer.address = newdata['address']

    customer.save()

    return JsonResponse({'ret': 0})

def deletecustomer(request):

    customerid = request.params['id']

    try:
        customer = Customer.objects.get(id=customerid)
    except Customer.DoesNotExist:
        return {'ret': 1, 'msg': f'id为`{customerid}`的客户不存在'}

    customer.delete()
    return JsonResponse({'ret: 0'})