from ast import Try
from typing import Type
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseServerError
from utils import customer_coll, customer1, customer2, customer3, db

# Create your views here.


def say_hello(request):
    x = 1
    y = 2
    z = x + y
    return render(request, 'hello.html', {'name': 'Angelita', 'value': z})

# CRUD


def retrieveCustomers(request):
    try:
        allCustomers = customer_coll.find({})
        return render(request, 'customers.html', {'customers': allCustomers})
    except Exception as err:
        return render(request, 'customers.html', {'error': err})


def retrieveCustomer(request):
    try:
        allCustomers = customer_coll.find_one({'name': request.name})
        return render(request, 'customers.html', {'customer': request})
    except Exception as err:
        return render(request, 'customers.html', {'error': err})


def createCustomer(request):
    try:
        customer_coll.insert_one(request)
        return HttpResponse()
    except Exception as err:
        return HttpResponseServerError()


def deleteCustomer(request):
    try:
        customer_coll.delete_one({"name": request.name})
        return HttpResponse(HttpResponse.status_code)
    except Exception as err:
        return HttpResponseServerError()


def patchCustomer(request):
    try:
        customer_coll.update_one(
            {"name": "Pinco"}, {'$set': {'surname': request.surname}})
        return HttpResponse(HttpResponse.status_code)
    except Exception as err:
        return HttpResponseServerError()
