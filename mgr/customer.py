from lib.handler import dispatcherBase
from sales.views import listcustomers, addcustomer, modifycustomer, deletecustomer

Action2Handler = {
    'list_customer': listcustomers,
    'add_customer': addcustomer,
    'modify_customer': modifycustomer,
    'del_customer': deletecustomer,
}
def dispatcher(request):
    return dispatcherBase(request, Action2Handler)