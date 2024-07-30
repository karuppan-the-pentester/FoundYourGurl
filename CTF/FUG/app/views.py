from django.shortcuts import render,redirect
from .models import UsersDataBase,Notification

# Create your views here.
global IsLogin,username
IsLogin = False
username = ''


def index(request):
    return render(request, 'index.html')

def admission_page(request):
    return render(request, 'Admission_page.html')

def student_portal(request):
    Users = set()
    for i in UsersDataBase.objects.all():
        Users.add(i.RegNo)

    global IsLogin, username

    if IsLogin == False:
        if (request.method == 'POST'):
            username = request.POST.get('username')
            password = request.POST.get('password')

            for j in UsersDataBase.objects.filter(RegNo=username):
                if (username == j.RegNo and password == j.PassWord) :
                    IsLogin = True
                    return redirect('students_dashboard')
                else:
                    return redirect('students_portal')

        else:
            return render(request, 'student-portal.html')
    else:
        return redirect('students_dashboard')

def students_dashboard(request):
    if IsLogin == True:
        j=UsersDataBase.objects.get(RegNo=username)
        MessageList = []
        tempDict = {}
        for i in Notification.objects.filter(userid=username):
            tempDict['Title'] = i.title
            tempDict['Content'] = i.message
            tempDict['Time'] = i.time
            tempDict['Url'] = i.url
            MessageList.append(tempDict)

        return render(request, 'dashboard/index.html',{'ParsingData': {'Name':str(j.name),'Batch':str(j.Department),'ProfilePic':str(j.Photo) , 'Notification':len(MessageList)  }, 'UserMessage':MessageList })
    else:
        return redirect('students_portal')

def SignoutPage(request):
    global IsLogin
    IsLogin = False
    return redirect('students_portal')

def id_card(request,u_id):
    if IsLogin == True:
        try:
            j = UsersDataBase.objects.get(id=u_id)
            return render(request, 'id_card/index.html',{'UserData':{'Name':str(j.name), 'RegNo':str(j.RegNo), 'Department':str(j.Department), 'Batch':str(j.Batch),'FatherName':str(j.FatherName),'MotherName':str(j.MotherName),'DateOfBirth':str(j.DateOfBirth),'Address':str(j.Address),'Phone':str(j.Phone),'Photo':str(j.Photo)}})
        except Exception as e:
            print(e)
            return redirect('students_dashboard')
    else:
        return redirect('students_dashboard')

