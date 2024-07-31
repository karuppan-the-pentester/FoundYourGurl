from django.shortcuts import render, redirect
from .models import UsersDataBase, Notification, Notes, gallery
from .forms import ImageForm

# Create your views here.
global IsLogin, username
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
                if (username == j.RegNo and password == j.PassWord):
                    IsLogin = True
                    return redirect('students_dashboard')
                else:
                    return redirect('students_portal')

        else:
            return render(request, 'student-portal.html')
    else:
        return redirect('students_dashboard')

def Gallery(request):
        ImageList = [{
            'Title': k.title,
            'Content': k.image.name,
            'id': k.id,
            'status': k.status,
            'UName': UsersDataBase.objects.get(RegNo=k.userid).name
        } for k in gallery.objects.filter(status="Published")]

        return render(request, 'gallery.html', {'gallery': ImageList})



def students_dashboard(request):
    if IsLogin == True:
        j = UsersDataBase.objects.get(RegNo=username)
        MessageList = []
        tempDict = {}
        for i in Notification.objects.filter(userid=username):
            tempDict['Title'] = i.title
            tempDict['Content'] = i.message
            tempDict['Time'] = i.time
            tempDict['Url'] = i.url
            MessageList.append(tempDict)

        return render(request, 'dashboard/index.html', {
            'ParsingData': {'Name': str(j.name), 'Batch': str(j.Department), 'ProfilePic': str(j.Photo),
                            'Notification': len(MessageList)}, 'UserMessage': MessageList})
    else:
        return redirect('students_portal')


def SignoutPage(request):
    global IsLogin
    IsLogin = False
    return redirect('students_portal')


def id_card(request, u_id):
    if IsLogin == True:
        try:
            j = UsersDataBase.objects.get(id=u_id)
            return render(request, 'id_card/index.html', {
                'UserData': {'Name': str(j.name), 'RegNo': str(j.RegNo), 'Department': str(j.Department),
                             'Batch': str(j.Batch), 'FatherName': str(j.FatherName), 'MotherName': str(j.MotherName),
                             'DateOfBirth': str(j.DateOfBirth), 'Address': str(j.Address), 'Phone': str(j.Phone),
                             'Photo': str(j.Photo)}})
        except Exception as e:
            print(e)
            return redirect('students_dashboard')
    else:
        return redirect('students_dashboard')


def notes(request):
    if IsLogin == True:
        j = UsersDataBase.objects.get(RegNo=username)
        MessageList = [{
            'Title': i.title,
            'Content': i.message,
            'Time': i.time,
            'Url': i.url
        } for i in Notification.objects.filter(userid=username)]

        NotesList = [{
            'id': k.id,
            'Title': k.title,
            'Content': k.message,
            'Description': k.description,
            'Photo': k.photo
        } for k in Notes.objects.filter(userid=username)]

        return render(request, 'dashboard/Notes.html',
                      {'ParsingData':
                           {'Name': str(j.name), 'Batch': str(j.Department), 'ProfilePic': str(j.Photo),
                            'Notification': len(MessageList)},
                       'UserMessage': MessageList,
                       'NotesList': NotesList})
    else:
        return redirect('students_dashboard')

def view_notes(request,notes_id):
    if IsLogin == True :
        UserNotesList = []
        for NotesID in Notes.objects.filter(userid=username):
            UserNotesList.append(NotesID.id)
        if(notes_id in UserNotesList):
            j = UsersDataBase.objects.get(RegNo=username)
            MessageList = [{
                'Title': i.title,
                'Content': i.message,
                'Time': i.time,
                'Url': i.url
            } for i in Notification.objects.filter(userid=username)]

            k = Notes.objects.get(id=notes_id)
            NotesList = {
                'id': k.id,
                'Title': k.title,
                'Content': k.message,
                'Description': k.description,
                'Photo': k.photo
            }

            return render(request, 'dashboard/ViewNote.html',
                          {'ParsingData':
                               {'Name': str(j.name), 'Batch': str(j.Department), 'ProfilePic': str(j.Photo),
                                'Notification': len(MessageList)},
                           'UserMessage': MessageList,
                           'NotesList': NotesList})
        else:
            return redirect('notes')

    else:
        return redirect('students_dashboard')

def gallery_stud(request):
    if IsLogin == True:
        j = UsersDataBase.objects.get(RegNo=username)
        MessageList = [{
            'Title': i.title,
            'Content': i.message,
            'Time': i.time,
            'Url': i.url
        } for i in Notification.objects.filter(userid=username)]

        ImageList = [{
            'Title': k.title,
            'Content': k.image.name,
            'id': k.id,
            'status': k.status
        } for k in gallery.objects.filter(userid=username)]

        return render(request, 'dashboard/Gallery-Stud.html', {
            'ParsingData': {'Name': str(j.name), 'Batch': str(j.Department), 'ProfilePic': str(j.Photo),
                            'Notification': len(MessageList)}, 'UserMessage': MessageList, 'gallery': ImageList})
    else:
        return redirect('students_portal')

def image_upload_view(request):
    if IsLogin == True:
        if request.method == 'POST':
            form = ImageForm(request.POST, request.FILES)
            if form.is_valid():
                img_obj = form.save(commit=False)
                img_obj.userid = username
                img_obj.save()
                return render(request, 'dashboard/ImageUpload.html', {'form': form, 'img_obj': img_obj})
        else:
            form = ImageForm(initial={'status': 'Pending'})

        return render(request, 'dashboard/ImageUpload.html', {'form': form})
    else:
        return redirect('students_dashboard')

