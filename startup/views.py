from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from .models import Product
from .models import StepProduct
from .models import Lastip
from .forms import ProductForm
from django.shortcuts import redirect
from .createdefaultdata import PopulateDb
from django.http import HttpResponseRedirect
from django.db import models


def createdata(request):
    PopulateDb()
    products = Product.objects.all()
    return HttpResponseRedirect("/")


def home(request):
    alert = False
    if request.user.is_superuser:
        currentIp = None
        if request.environ.get("HTTP_X_FORWARDED_FOR") is None:
            currentIp = request.environ["REMOTE_ADDR"]
        else:
            currentIp = request.environ["HTTP_X_FORWARDED_FOR"]  # if behind a proxy
        list_ip = Lastip.objects.all()
        if len(list_ip) > 0:
            last_list_ip = list_ip[len(list_ip) - 1]
            if last_list_ip.ip != currentIp:
                alert = True
                last_list_ip.ip = currentIp
                last_list_ip.save()
        else:
            alert = True
            newIp = Lastip(ip=currentIp)
            newIp.save()

    products = Product.objects.all()

    return render(
        request, "startup/product_list.html", {"products": products, "alert": alert}
    )


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    steps = (
        StepProduct.objects.filter(code=product.code)
        .order_by("creation_date")
        .reverse()
    )
    return render(
        request, "startup/product_detail.html", {"product": product, "steps": steps}
    )


def search(request):
    if request.method == "GET":
        print(request.GET["code"])
        codeInput = request.GET["code"]
        product = Product.objects.filter(code=codeInput)
        if len(product) > 0:
            steps = (
                StepProduct.objects.filter(code=product[0].code)
                .order_by("creation_date")
                .reverse()
            )
            return render(
                request,
                "startup/product_detail.html",
                {"product": product[0], "steps": steps},
            )

    products = Product.objects.all()
    return render(
        request, "startup/product_list.html", {"products": products, "empty": True}
    )


def add_new(request):
    product = Product()
    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            product = form.save(commit=False)
            product.save()

            txbool = False
            if product.transactionid != None:
                txbool = True

            return render(
                request,
                "startup/product_detail.html",
                {
                    "product": product,
                    "txbool": txbool,
                },
            )
    else:
        form = ProductForm(instance=product)

    return render(request, "startup/add_new.html", {"form": form})
