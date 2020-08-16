import json
import traceback
from django.db.models import F
from django.http import JsonResponse
from django.db import transaction

from common.models import Order, OrderMedicine

def addorder(request):

    info = request.params['data']

    # 从请求消息中 获取要添加订单的信息
    # 并且插入到数据库中

    with transaction.atomic():
        medicinelist = info['medicinelist']
        print('medicinelist------->', medicinelist)

        new_order = Order.objects.create(name=info['name'],
                                         customer_id=info['customerid'],
                                         # 写入json格式的药品数据到medicinelist字段中
                                         medicinelist=json.dumps(medicinelist, ensure_ascii=False))

        batch = [OrderMedicine(medicine_id=medicine['id'], order_id=new_order.id, amount=medicine['amount']) for medicine in info['medicinelist']]
        OrderMedicine.objects.bulk_create(batch)

    return JsonResponse({'ret': 0, 'orderId': new_order.id})

def listorder(request):

    obj = Order.objects.annotate(customer_name=F('customer__name')).\
                        values('id', 'name', 'customer_name', 'medicinelist', 'create_time')
    retlist = list(obj)

    return JsonResponse({'ret': 0, 'retlist': retlist})


def deleteorder(request):
    oid = request.params['id']

    try:
        order = Order.objects.get(id=oid)
        with transaction.atomic():
            # 先删除OrderMedicine里面的记录
            OrderMedicine.objects.filter(order_id=oid).delete()
            # 再删除Order里面的记录
            order.delete()
    except Order.DoesNotExist:
        return JsonResponse({'ret': 1, 'msg': f'id为{oid}不存在'})
    except:
        err = traceback.format_exc()
        return JsonResponse({'ret': 1, 'msg': err})




