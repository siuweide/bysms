from django.contrib import admin
from .models import Customer, Medicine, Order, OrderMedicine

@admin.register(Customer)
class CuestomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phonenumber', 'address')

@admin.register(Medicine)
class MedicineAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'sn', 'desc')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'customer')

@admin.register(OrderMedicine)
class OrderMedicineAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'medicine')