from django.shortcuts import render,redirect
from .models import Question,Quiz,History
from datetime import datetime
from accounts.models import CustomUser
from django.db.models import Case,When
from django.contrib import auth,messages
# Create your views here.

def index(request):
    
    return render(request,'home.htm')


def create_1(request):
    
    if request.method == 'POST':
        count = request.POST.get("count")
        print(count)
        request.session['count'] = count
        return redirect('create')
        
    count = 10
    context = {
        "count":count,
    }
    return render(request,'cc.htm',context)

def create(request):
    if request.method == "POST":
        quz = Quiz(title=request.POST.get("title"),number_of_questions=request.session['count'])
        quz.save()
        for i in range(1,int(request.session['count'])+1):
            s = Question(title=request.POST.get(f"question_{i}"),
                     num = i,option_1=request.POST.get(f"{i}_opt_1")
                     ,option_2=request.POST.get(f"{i}_opt_2")
                     ,option_3=request.POST.get(f"{i}_opt_3")
                     ,option_4=request.POST.get(f"{i}_opt_4")
                     ,answer=request.POST.get(f"{i}_answer"))
            s.save()
            quz.questions.add(s)
            quz.save()
        quz.save()
        
        
    count = request.session['count']
    context = {
        "count":str(count),
    }
    return render(request,'create_quiz.htm',context)
    
    
def view(request,pk):
    quz = Quiz.objects.get(pk=pk)
    context = {
        's':quz,
    }
    return render(request,'view.htm',context)

def view_all(request):
    quz = Quiz.objects.all()
    context = {
        'quz':quz,
    }
    
    return render(request,'view_all.htm',context)



def take(request,pk):
    quz = Quiz.objects.get(pk=pk)
    
    
    if request.method == "POST":
        key = []
        result = []
        score = 0
        
            
        for i in quz.questions.all():
            key.append(i.answer)
        for i in range(1,len(key)+1):
            try:
                result.append(int(request.POST.get(f"{i}")))
            except:
                
                date = str(datetime.now())
                date = date.split()[1]
                print(date)
                context = {
                    's':quz,
                    'date':date,
                }
                messages.error(request, 'Error ! , Please answer all the question')
                return render(request,'take_quiz.htm',context)
        
        
        print(key)
        print(result)
        for i in range(len(key)):
            if key[i] == result[i]:
                score+=10
        
        
        if request.user.is_authenticated:
            user = CustomUser.objects.get(username=request.user.username)
            his = History(user=user,quiz_id=quz.id,score=score)
            his.save()
            hist = History.objects.filter(user=user)
            ids = []
            for i in hist:
                ids.append(i.quiz_id)
            preserved = Case(*[When(pk=pk,then=pos) for pos,pk in enumerate(ids)] )
            quiz = Quiz.objects.filter(id__in=ids).order_by(preserved)
            hist = History.objects.order_by('-date')
            
            context = {
                'his':his,
                "quz":quz,
            } 
        
        return render(request,'result.htm',context)
        
        
        
        
        
    
    date = str(datetime.now())
    date = date.split()[1]
    print(date)
    context = {
        's':quz,
        'date':date,
    }
    return render(request,'take_quiz.htm',context)






def history(request):
    if request.user.is_authenticated:
        user = CustomUser.objects.get(username=request.user.username)
        hist = History.objects.filter(user=user)
        ids = []
        for i in hist:
            ids.append(i.quiz_id)
        preserved = Case(*[When(pk=pk,then=pos) for pos,pk in enumerate(ids)] )
        quiz = Quiz.objects.filter(id__in=ids).order_by(preserved)
        s =  []
        for i in quiz:
            s.append(History.objects.order_by('-date').filter(quiz_id=i.id).first())
        
        # hist = hist.objects.order_by('-date')
        dictt = {}
        for i in range(len(quiz)):
            dictt[quiz[i]] = s[i]
        print(dictt)
        
        context = {
            'his':dictt,
        } 
        
        return render(request,'history.htm',context)
    
    return render(request,'history.htm')





