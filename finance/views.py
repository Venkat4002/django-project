from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def feeCollection(request):
    return render(request,'finance/fee-collection.html')
def feeDuesReport(request):
    return render(request,'finance/fee-due.html')
def feeCollectionReport(request):
    return render(request,'finance/feecollection-Report.html')
