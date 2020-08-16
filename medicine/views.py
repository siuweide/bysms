from django.db.models import Q

from common.models import Medicine
from django.http import JsonResponse
from django.core.paginator import Paginator, EmptyPage

def listmedicine(request):
    try:
        # 返回一个QuerySet对象，包含所有的记录
        qs = Medicine.objects.values().order_by('-id')

        keywords = request.params.get('keywords', None)
        if keywords:
            conditions = [Q(name__contains=one) for one in keywords.split(' ')]
            query = Q()
            for condition in conditions:
                query &= condition
            qs = qs.filter(query)

        # 要获取第几页的数据
        pagenum = request.params['pagenum']

        # 每页显示多少条记录
        pagesize = request.params['pagesize']

        # 使用分页对象，设定每页多少条记录
        paginator = Paginator(qs, pagesize)

        # 从数据库中读取数据，指定读取其中第几页
        page = paginator.page(pagenum)

        retlist = list(page)

        return JsonResponse({'ret': 0, 'retlist': retlist, 'total': paginator.count})

    except EmptyPage:
        return JsonResponse({'ret': 0, 'retlist': [], 'total': 0})

def addmedicine(request):
    info = request.params['data']
    if Medicine.objects.filter(name=info['name']).exists():
        return JsonResponse({'ret': 1, 'msg': '药品名已经存在'})

    medicine = Medicine.objects.create(name=info['name'],
                            sn=info['sn'],
                            desc=info['desc'])

    return JsonResponse({'ret': 0, 'medicineId': medicine.id})

def modifymedicine(request):
    medicineId = request.params['id']
    newdata = request.params['newdata']

    if not Medicine.objects.filter(id=medicineId).exists():
        return JsonResponse({'ret': 1, 'msg': '药品不存在, 无法修改'})

    medicine = Medicine.objects.get(id=medicineId)
    if 'name' in newdata:
        medicine.name = newdata['name']
    if 'sn' in newdata:
        medicine.sn = newdata['sn']
    if 'desc' in newdata:
        medicine.desc = newdata['desc']
    medicine.save()

    return JsonResponse({'ret': 0})

def deletemedicine(request):
    medicineId = request.params['id']

    if not Medicine.objects.filter(id=medicineId).exists():
        return JsonResponse({'ret': 1, 'msg': '药品不存在, 无法删除'})

    medicine = Medicine.objects.get(id=medicineId)
    medicine.delete()
    return JsonResponse({'ret': 0})