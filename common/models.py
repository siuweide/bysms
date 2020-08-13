from django.db import models

class Customer(models.Model):
    name = models.CharField('客户名称', max_length=200)
    phonenumber = models.CharField('联系电话', max_length=200)
    address = models.CharField('地址', max_length=200)

class Medicine(models.Model):
    name = models.CharField('药品名称', max_length=200)
    sn = models.CharField('药品编号', max_length=200)
    desc = models.CharField('描述', max_length=200)

class Order(models.Model):
    name = models.CharField('订单名称', max_length=200)
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    medicines = models.ManyToManyField(Medicine, through='OrderMedicine')

    # 为了提高效率，这里存放 订单 medicines 冗余数据
    medicinelist = models.CharField(max_length=2000, null=True, blank=True)

class OrderMedicine(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    medicine = models.ForeignKey(Medicine, on_delete=models.PROTECT)

    # 订单中药品数量
    amount = models.PositiveIntegerField()