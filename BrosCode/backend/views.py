from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
import os
from datetime import datetime
#url= "https://raw.githubusercontent.com/Sidop03/BrosCode/main/oursheet%20-%20Sheet1.csv"
df = pd.read_csv('BrosCode - Sheet1.csv')
# Create your views here.
def home(request):
    return render(request,'hostelportal.html',{'NAME':'HARSHIT'})
def csvwarden(request):
    return render(request, "wardendashboard.html")
def csvstudent(request):
    return render(request, "student.html")
def page(request):
    print(request,"this is request")
    wname = request.GET['wname']
    empId = request.GET['empId']
    wblock = request.GET['block']
    wnamelist = []          
    empIdlist = []         
    wblocklist = []
    print(wname, "this is wname")    
    print(empId, "this is empId")    
    for i in range(len(df['0'])):
        wnamelist.append(df['0'][i])
        empIdlist.append(df['1'][i])
        wblocklist.append(df['2'][i])

    # Assuming you have empId, wname, and wblock as variables

    finallist = []

    # You need to use a loop to iterate over the existing DataFrame, not just based on the length of empIdlist
    for i in range(len(df['0'])):
        finallist.append([wnamelist[i], empIdlist[i], wblocklist[i]])
    if empId not in empIdlist:
        wnamelist.append(wname)
        empIdlist.append(empId)
        wblocklist.append(wblock)
        finallist.append([wnamelist[len(wnamelist)-1], empIdlist[len(wnamelist)-1], wblocklist[len(wnamelist)-1]])
    print(wblocklist)
    print(finallist)
    dfe = pd.DataFrame(finallist)
    print(dfe,"this isdatafram")
    dfe.to_csv('BrosCode - Sheet1.csv')
    os.system("git add 'BrosCode - Sheet1.csv'")
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    os.system("git commit -m 'changed again{dt_string}'")
    os.system("git push origin master")
    return render(request,'page.html')
def actit(request):
    df = pd.read_csv('Details.csv')
    Block = request.GET.get('block', '')
    roomNo = request.GET.get('roomNo', '')
    roomType = request.GET.get('roomType', '')
    occupancy = request.GET.get('occupancy', '')
    residents = request.GET.get('residents', '')

    Blocklist = []          
    roomNolist = []         
    roomTypelist = []
    occupancylist = []
    residentslist = []
    print(Block, "this is block")    
    print(roomNo, "this is roomNo")    
    for i in range(len(df['0'])):
        Blocklist.append(df['0'][i])
        roomNolist.append(df['1'][i])
        roomTypelist.append(df['2'][i])
        occupancylist.append(df['3'][i])  # Access 'occupancy' by its actual name
        residentslist.append(df['4'][i])  # Access 'residents' by its actual name



    # Assuming you have empId, wname, and wblock as variables

    finallist = []

    # You need to use a loop to iterate over the existing DataFrame, not just based on the length of empIdlist
    for i in range(len(df['0'])):
        finallist.append([Blocklist[i], roomNolist[i], roomTypelist[i], occupancylist[i],residentslist[i]])
    if (roomNo not in roomNolist):
        Blocklist.append(Block)
        roomNolist.append(roomNo)
        roomTypelist.append(roomType)
        occupancylist.append(occupancy)
        residentslist.append(residents)

        finallist.append([Blocklist[len(Blocklist)-1], roomNolist[len(roomNolist)-1], roomTypelist[len(roomTypelist)-1],occupancylist[len(occupancylist)-1],residentslist[len(residentslist)-1]])
    print(Blocklist)
    print(finallist)
    dfe = pd.DataFrame(finallist)
    print(dfe,"this isdatafram")
    dfe.to_csv('Details.csv')
    os.system("git add 'Details.csv'")
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    os.system("git commit -m 'changed again{dt_string}'")
    os.system("git push origin master")
    return render(request, 'page copy.html')
def doit(request):
    df = pd.read_csv('Details.csv')
    Block = request.GET['block']
    roomNo = request.GET['roomNo']
    roomType = request.GET['roomType']
    occupancy = request.GET['occupancy']
    residents = request.GET['residents']
    Blocklist = []          
    roomNolist = []         
    roomTypelist = []
    occupancylist = []
    residentslist = []
    print(Block, "this is block")    
    print(roomNo, "this is empId")    
    for i in range(len(df['0'])):
        Blocklist.append(df['0'][i])
        roomNolist.append(df['1'][i])
        roomTypelist.append(df['2'][i])
        occupancylist.append(df['3'][i])  # Access 'occupancy' by its actual name
        residentslist.append(df['4'][i])


    # Assuming you have empId, wname, and wblock as variables

    finallist = []

    # You need to use a loop to iterate over the existing DataFrame, not just based on the length of empIdlist
    for i in range(len(df['0'])):
        finallist.append([Blocklist[i], roomNolist[i], roomTypelist[i], occupancylist[i],residentslist[i]])
    if roomNo not in roomNolist:
        Blocklist.append(Blocklist)
        roomNolist.append(roomNolist)
        roomTypelist.append(roomTypelist)
        occupancylist.append(occupancylist)
        residentslist.append(residentslist)

        finallist.append([Blocklist[len(Blocklist)-1], roomNolist[len(roomNolist)-1], roomTypelist[len(roomTypelist)-1],occupancylist[len(occupancylist)-1],residentslist[len(residentslist)-1]])
    print(Blocklist)
    print(finallist)
    dfe = pd.DataFrame(finallist)
    print(dfe,"this isdatafram")
    dfe.to_csv('Details.csv')
    os.system("git add 'Details.csv'")
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    os.system("git commit -m 'changed again{dt_string}'")
    os.system("git push origin master")
    return render(request,'page.html')