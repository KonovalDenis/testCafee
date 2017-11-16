from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from .models import Table
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import json
from django.core.mail import send_mail

# Create your views here.

def editTables(request):
	tables = Table.objects.all()
	context = {"title":"reservation",
			   "tables":tables
			   }
	return render(request,"editTables.html", context)

def reservation(request):
	tables = Table.objects.all()
	context = {"title":"reservation",
			   "tables":tables
			   }
	return render(request,"reservation.html", context)




@csrf_protect
def upload_tables(request):
	tablesJS = request.POST.get("tables")
	tables = json.loads(tablesJS)
	print(tables)
	print("wer")
	currentDataBase = Table.objects.all()
	for table in tables:
		# Если стол уже существовал то обновляем все поля кроме брони
		try:
			oldTable = Table.objects.get(number = int(table['number']))
			oldTable.number = table['number']
			oldTable.shape = table['shape']
			oldTable.chairs_count = table['chairs_count']
			oldTable.width = float(table['width'][0:-1])
			oldTable.height = float(table['height'][0:-1])
			oldTable.pos_X = float(table['pos_X'][0:-1])
			oldTable.pos_y = float(table['pos_Y'][0:-1])
			oldTable.save()
		# Если не существовал, то создаем новый
		except Exception:
			newTable = Table(number = table['number'], shape = table['shape'], chairs_count = table['chairs_count'], 
				width = float(table['width'][0:-1]), height = float(table['height'][0:-1]), pos_X = float(table['pos_X'][0:-1]),
				pos_y = float(table['pos_Y'][0:-1]))
			newTable.save()
	
	return HttpResponseRedirect("/editTables/")


@csrf_protect
def reserve_tables(request):
	def beautyfyTables(tables):
		beauty = ""
		for table in tables:
			beauty += table +", "
		return beauty
	def beautifyDate(date):
		date = date.split("-")
		if date[1] == '1':
			date[1] = " January "
		if date[1] == '2':
			date[1] = " February "
		if date[1] == '3':
			date[1] = " March "
		if date[1] == '4':
			date[1] = " April "
		if date[1] == '5':
			date[1] = " May "
		if date[1] == '6':
			date[1] = " June "
		if date[1] == '7':
			date[1] = " July "
		if date[1] == '8':
			date[1] = " August "
		if date[1] == '9':
			date[1] = " September "
		if date[1] == '10':
			date[1] = " October "
		if date[1] == '11':
			date[1] = " November "
		if date[1] == '12':
			date[1] = " December "
		return date[2] + date[1] + date[0]

	date = request.POST.get("reserveDate")
	print("date = ", date)
	tableNumbers = request.POST.get("tablesForReservation")
	tableNumbers = json.loads(tableNumbers)
	email = request.POST.get("email")
	print (tableNumbers)
	for i in tableNumbers:
		table = Table.objects.get(number = int(i))
		table.booked += "("+date+" : "+email + "),"
		table.save()
	message = "You ordered table(s) № {} for {}. We are waiting for You in our Cafee.".format(beautyfyTables(tableNumbers), beautifyDate(date))
	send_mail('Бронь столика В тестовом кафе', message, 'testcafee2017@gmail.com',[email])
	
	return HttpResponseRedirect("/reservation/")

def table_status(request):
	if request.GET:
		user = request.user
		print (user)
		checkDate = request.GET['checkDate']
		print(checkDate)
		busyTables = Table.objects.filter(booked__contains = checkDate)
		busyTablesArray = []
		for table in busyTables:
			busyTablesArray.append(table.number)
		busyTablesArray = json.dumps(busyTablesArray, sort_keys=True, indent=4)


		return HttpResponse(busyTablesArray)
	