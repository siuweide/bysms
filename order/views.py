from django.db.models import F
from django.http import JsonResponse
from django.db import IntegrityError, transaction

from common.models import Order, OrderMedicine

def addorder(request):

    info = request.params['data']

    # 从请求消息中 获取要添加订单的信息
    # 并且插入到数据库中

    with transaction.atomic():
        new_order = Order.objects.create(name=info['name'],
                                         customer_id=info['customerid'])

        batch = [OrderMedicine(medicine_id=mid, order_id=new_order.id, amount=1) for mid in info['medicineids']]
        OrderMedicine.objects.bulk_create(batch)

    return JsonResponse({'ret': 0, 'orderId': new_order.id})

def listorder(request):

    obj = Order.objects.annotate(customer_name=F('customer__name'),
                                 medicines_name=F('medicines__name')).\
                        values('id', 'name', 'customer_name', 'medicines_name', 'create_data')
    retlist = list(obj)
    newlist = []
    id2order = {}
    for one in retlist:
        orderid = one['id']
        if orderid not in id2order:
            newlist.append(one)
            id2order[orderid] = one
        else:
            id2order[orderid]['medicines_name'] += ' | ' + one['medicines_name']

    return JsonResponse({'ret': 0, 'retlist': newlist})




