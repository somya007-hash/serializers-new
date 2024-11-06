from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def index(request):
    courses = {
        "instructor" : "abhijeet",
        "course_name" : "django rest framework",
        "course_provider" : "scaler",
    }
    if request.method == 'GET':
        print("$$$$$$$$$$$$$$$$$$$$$")
        data = request.GET.get('search')
        print(data)
        print("You hit a get method")
        print("$$$$$$$$$$$$$$$$$$$$$")
        return Response(courses)
    
    elif request.method == 'POST':
        data = request.data
        print("$$$$$$$$$$$$$$$$$$$$$")
        print(data)
        print("You hit a post method")
        print("$$$$$$$$$$$$$$$$$$$$$")
        return Response(courses)
    
    elif request.method == 'PUT':
        print("You hit a patch method")
        return Response(courses)
    
    else:
        print("you hit a delete method")
        return Response(courses)