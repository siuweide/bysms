from django.http import JsonResponse
from common.models import Medicine

def listmedicine(request):
    obj = list(Medicine.objects.values())
    return JsonResponse({'ret': 0, 'retlist': obj})

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