from django.http import JsonResponse
from . import models


def product(request):
    product_obj = models.Product.objects.all().order_by('-id').values()
    return JsonResponse({"product": list(product_obj)})


def collection(request):
    collection_obj = models.Collection.objects.all().order_by('-id').values()
    return JsonResponse({"collection": list(collection_obj)})


def product_query(request, slug):
    product_obj = models.Product.objects.filter(slug=slug).values()
    collection = models.Collection.objects.filter(id=models.Product.objects.get(slug=slug).collection_id).values()
    return JsonResponse({"product": list(product_obj), "collection": list(collection)})


def collection_query(request, slug):
    collection_id = models.Collection.objects.get(slug=slug).id
    product_obj = models.Product.objects.filter(collection=collection_id).order_by('-id').values()
    collection_obj = models.Collection.objects.filter(slug=slug).order_by('-id').values()
    return JsonResponse({"collection": list(collection_obj), "items": list(product_obj)})
