from django.http import HttpResponse
from django.shortcuts import render
from user_management.models import Teacher

def home(request):
    # data = {
    #     'name': 'Rishav',
    #     'age': 25,
    #     'city': 'New York'
    # }
    teacher = Teacher.objects.filter(subject='harish')
    
    if not teacher:
        return HttpResponse("No teacher found with the subject 'harish'")
    data = {
        'name':teacher[0].name,
        'email':teacher[0].email,
        'subject':teacher[0].subject,
        'phone_number':teacher[0].phone_number
    }
    print(teacher)
    return render(request, 'index.html', {'data': data})