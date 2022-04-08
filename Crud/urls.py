from django.contrib import admin
from django.urls import path
from grid.views import addnew, index, edit, update, delete
from student.views import addstudent, home, editstudent, updatestudent, deletestudent
from pupil.views import addpupil, glav, editpupil, updatepupil, deletepupil

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('addnew', addnew, name='addnew'),
    path('edit/<int:id>', edit, name='edit'),
    path('update/<int:id>', update, name='update'),
    path('delete/<int:id>', delete, name='delete'),
    path('home', home, name='home'),
    path('addstudent', addstudent, name='addstudent'),
    path('editstudent/<int:id>', editstudent, name='editstudent'),
    path('updatestudent/<int:id>', updatestudent, name='updatestudent'),
    path('deletestudent/<int:id>', deletestudent, name='deletestudent'),
    path('glav', glav, name='glav'),
    path('addpupil', addpupil, name='addpupil'),
    path('editpupil/<int:id>', editpupil, name='editpupil'),
    path('updatepupil/<int:id>', updatepupil, name='updatepupil'),
    path('deletepupil/<int:id>', deletepupil, name='deletepupil')
]
