from lib.handler import dispatcherBase
from order.views import addorder, listorder

Action2Handler = {
    'list_order': listorder,
    'add_order': addorder,
}

def dispatcher(request):
    return dispatcherBase(request, Action2Handler)