from lib.handler import dispatcherBase
from order.views import addorder, listorder, deleteorder

Action2Handler = {
    'list_order': listorder,
    'add_order': addorder,
    'delete_order': deleteorder,
}

def dispatcher(request):
    return dispatcherBase(request, Action2Handler)