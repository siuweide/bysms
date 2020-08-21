from django.db.models import Q
from django.http import JsonResponse
from django.utils.datastructures import MultiValueDictKeyError

from common.models import Customer
from django.core.paginator import Paginator, EmptyPage


def listcustomers(request):
    qs = Customer.objects.values().order_by('-id')

    keywords = request.params.get('keywords', None)
    if keywords:
        conditions = [Q(name__contains=one) for one in keywords.split(' ')]
        query = Q()
        for condition in conditions:
            query &= condition
        qs = qs.filter(query)

    try:
        pagesize = request.params['pagesize']
        pagenum = request.params['pagenum']
    except MultiValueDictKeyError:
        return JsonResponse({"ret": 1, "msg": '请求参数错误'})

    if pagesize == '' or pagenum == '':
        return JsonResponse({"ret": 1, "msg": "pagesize or pagenum is not null"})

    try:
        pagesize = int(pagesize)
        pagenum = int(pagenum)
    except ValueError:
        msg = 'pagesize or pagenum must be int'
        return JsonResponse({"ret": 1, "msg": msg})


    paginator = Paginator(qs, pagesize)
    page = paginator.page(pagenum)

    retlist = list(page)
    return JsonResponse({"ret":0, "retlist":retlist})

def addcustomer(request):
    info = request.params['data']

    try:
        name = info['name']
        phonenumber = info['phonenumber']
        address = info['address']

        # 从请求消息中  获取要添加客户的信息
        # 并且插入到数据库中
        # 返回值 就是对应插入记录的对象
        record = Customer.objects.create(name=name,
                                         phonenumber=phonenumber,
                                         address=address)
    except KeyError:
        return JsonResponse({"ret": 1, "msg": '请求参数错误'})

    return JsonResponse({'ret': 0, 'id': record.id})

def modifycustomer(request):

    customerid = request.params['id']
    newdata = request.params['newdata']

    if not Customer.objects.filter(id=customerid).exists():
        return JsonResponse({'ret': 1, "msg": f'id为{customerid}的客户不存在'})

    customer = Customer.objects.get(id=customerid)
    if 'name' in newdata:
        customer.name = newdata['name']
    if 'phonenumber' in newdata:
        customer.phonenumber = newdata['phonenumber']
    if 'address' in newdata:
        customer.address = newdata['address']

    customer.save()
    modify_msg = {"name":customer.name, "phonenumber":customer.phonenumber, "address": customer.address}
    return JsonResponse({'ret': 0, 'modified_msg': modify_msg})

def deletecustomer(request):

    customerid = request.params['id']

    try:
        customer = Customer.objects.get(id=customerid)
    except Customer.DoesNotExist:
        return {'ret': 1, 'msg': f'id为`{customerid}`的客户不存在'}

    customer.delete()
    return JsonResponse({'ret: 0'})