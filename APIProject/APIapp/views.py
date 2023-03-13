from django.shortcuts import render,redirect
from .models import Movie,student
from django.http import JsonResponse
from rest_framework import viewsets
from .serializers import MovieSerializer
from .forms import StudentForm,MovieForm
from rest_framework.authentication import BasicAuthentication , SessionAuthentication
from rest_framework.permissions import IsAuthenticated , IsAuthenticatedOrReadOnly
from rest_framework.decorators import api_view, throttle_classes
from rest_framework.response import Response
from rest_framework.throttling import UserRateThrottle , AnonRateThrottle


def movie_list(request):
    movie = Movie.objects.all()
    if request.method == 'GET':
        st = request.GET.get('searchname')
        if st !=None:
            movie = Movie.object.filter(name__icontains=st)
    return render(request,'movielist.html',{'movie':movie})




class MovieViewset(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    throttle_classes = [AnonRateThrottle]

@api_view(['GET','POST'])
@throttle_classes([UserRateThrottle])
def movie_data(request):

    if request.method == 'GET':
        movieS = Movie.objects.all()
        serializer = MovieSerializer(movieS,many=True)
        return Response(serializer.data)

    if request.method =='POST':
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

@api_view(['GET','PUT','DELETE'])
def movie_detail(request, pk):
    if request.method == 'GET':
        movie = Movie.objects.get(pk=pk)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)

    if request.method == 'PUT':
        movie = Movie.object.get(pk=pk)
        serializer = MovieSerializer(movie,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.errors)

    if request.method == 'DELETE':
        movie = Movie.objects.get(pk=pk)
        movie.delete()
        return Response("data has been deleted succesfully!")


def student_list(request):
    data = student.objects.all()
    return render(request,'student.html',{'data':data})

def Addstudent(request):
    form = StudentForm
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/student-list')
    return render(request,'addstudent.html',{'form':form})

def update_movie(request,id):
    movie = Movie.object.get(id=id)
    form = MovieForm(instance=movie)
    if request == 'POST':
        form = MovieForm(request.Post,instance=movie)
        if form.is_valid():
            form.save()
    return render(request,'updatemovie.html',{'form':form})

def delete_movie(request,id):
    movie = Movie.objects.filter(id=id).delete()
    return redirect('/')

def SlidesPage(request):
    sld = Slides.objects.all()
    return render(request,'Slides.html',{'slid':slide})


