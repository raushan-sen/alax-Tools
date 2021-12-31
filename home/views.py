from django.shortcuts import render
from home.models import *
import random
import pyrebase
from home.demo import *

apis=FirebaseStorage.objects.all()[len(FirebaseStorage.objects.all())-1]
config={"apiKey":apis.apiKey,"authDomain": apis.authDomain,"databaseURL": apis.databaseURL,"storageBucket": apis.storageBucket}
# Create your views here.

def home(request):
    return render(request, 'index.html')

def mcq(request):
    if request.method=='POST':
        Title=request.POST.get('title')
        Content=request.POST.get('content')
        Featuredimage=request.FILES['feature-image']
        simple=request.POST.get('simple-mcq')
        case=request.POST.get('case-based-mcq')
        imagebased=request.POST.get('image-base-mcq')
        myquizcontent=request.POST.get('my-quiz-content')
        filess=Files(random.randint(0,9),Featuredimage)
        filess.save()
        full_file=Files.objects.all()[0].Feature_image.name
        firebase = pyrebase.initialize_app(config)
        st=firebase.storage()
        file_namesave='alax/fimage/'+full_file.replace('static/alax/','')
        st.child(file_namesave).put(full_file)
        f=Files.objects.filter(Feature_image__contains=full_file)
        f.delete()
        os.remove(full_file)
        image_link="https://firebasestorage.googleapis.com/v0/b/tool-text.appspot.com/o/"+"alax%2Ffimage%2F"+full_file.replace('static/alax/','')+"?alt=media&token=d18e84b1-d8d0-4b67-96c2-c68895447321"
        All_File(random.randint(0,9),image_link,full_file.replace('static/alax/','')).save()
        All_full_content=full_bhi_content(Content.split('\r\n'),myquizcontent.split('\r\n'),simple,case,imagebased,image_link)
        context={
            "title":Title,
            "All_full_content":All_full_content,
            "image_url":image_link,
        }
        return render(request, 'mcq-codes.html',context)

    return render(request, 'mcq.html')

def uploads(request):
    if request.method=='POST':
        Filex=request.FILES['our-file']
        filess=Files(random.randint(0,9),Filex)
        filess.save()
        full_file=Files.objects.all()[0].Feature_image.name
        firebase = pyrebase.initialize_app(config)
        st=firebase.storage()
        file_namesave='alax/fimage/'+full_file.replace('static/alax/','')
        st.child(file_namesave).put(full_file)
        f=Files.objects.filter(Feature_image__contains=full_file)
        f.delete()
        os.remove(full_file)
        image_link="https://firebasestorage.googleapis.com/v0/b/tool-text.appspot.com/o/"+"alax%2Ffimage%2F"+full_file.replace('static/alax/','')+"?alt=media&token=d18e84b1-d8d0-4b67-96c2-c68895447321"
        All_File(random.randint(0,9),image_link,full_file.replace('static/alax/','')).save()
        

    return render(request, 'upload-file.html',{'files':All_File.objects.all()})
