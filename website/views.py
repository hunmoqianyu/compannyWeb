import json

from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from website.models import Product, MainIMG, New_Product
from django.db.models import Q
from django.core.mail import send_mail

"""首页"""


def index(request):
    mainImg = MainIMG.objects.all()
    new_product1 = New_Product.objects.filter(type='1')
    new_product2 = New_Product.objects.filter(type='2')
    new_product3 = New_Product.objects.filter(type='3')
    new_product4 = New_Product.objects.filter(type='4')
    new_product5 = New_Product.objects.filter(type='5')
    return render(request, 'index.html', {'main_img': mainImg,
                                          'product1': new_product1,
                                          'product2': new_product2,
                                          'product3': new_product3,
                                          'product4': new_product4,
                                          'product5': new_product5})


def product(request, product_pk):
    pro = Product.objects.filter(type=product_pk)
    if request.is_ajax() and request.method == "POST":
        """使用Q对象进行筛选"""
        size = request.POST.getlist("size[]")
        platform = request.POST.getlist("platform[]")
        func = request.POST.getlist("func[]")
        if len(size) > 0:
            q1 = Q()
            q1.connector = 'OR'
            for i in size:
                q1.children.append(("size", i))
            pro = pro.filter(q1)
        if len(platform) > 0:
            q2 = Q()
            q2.connector = "OR"
            for i in platform:
                q2.children.append(("platform", i))
            pro = pro.filter(q2)
        if len(func) > 0:
            q3 = Q()
            q3.connector = "OR"
            for i in func:
                q3.children.append(("function", i))
            pro = pro.filter(q3)
        msg_list = list(pro.values())
        print(msg_list)
        return JsonResponse(msg_list, safe=False)
    return render(request, 'product.html', {"pro": pro})


def profile(request):
    return render(request, 'profile.html')


def contact(request):
    return render(request, 'contact.html')


def feedback(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        address = request.POST.get('address')
        text = request.POST.get('content')
        message = "收到一则网站留言来自" + name + "。\n电话号码为：" + phone + "\n邮箱为：" + email + "\n地址:" + address + "\n留言内容" + text + "\n"
        send_mail(
            '网站留言',
            message,
            'liqy2758@163.com',
            ['2100878136@qq.com'],
            fail_silently=False
        )
        return HttpResponse("留言成功")
    return render(request, 'feedback.html')


def clients(request):
    return render(request, 'clients.html')


def support(request):
    return render(request, 'support.html')


def download(request):
    return render(request, 'download.html')


def aft_sale(request):
    return render(request, 'aft_sale.html')


def problems(request):
    return render(request, 'problems.html')


def suc_case(request):
    return render(request, 'suc_case.html')


def custom_made(request):
    return render(request, 'custom_made.html')
