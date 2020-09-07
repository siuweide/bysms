from lib.handler import dispatcherBase
from medicine.views import listmedicine, addmedicine, modifymedicine, deletemedicine

Action2Handler = {
    'list_medicine': listmedicine,
    'add_medicine': addmedicine,
    'modify_medicine': modifymedicine,
    'del_medicine': deletemedicine,
}

def dispatcher(request):
    return dispatcherBase(request, Action2Handler)