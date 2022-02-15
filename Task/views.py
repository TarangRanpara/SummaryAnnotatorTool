from django.shortcuts import redirect, render
from django.contrib.auth import get_user_model
from .models import SummaryTask
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='/login')
def article_list_view(request):
    try:
    
        session_user = request.session['username']
        user_id = get_user_model().objects.get(username = session_user).pk

        summaries = SummaryTask.objects.filter(annotator = user_id)

        to_be_done = [(summary.pk, "to be done")  for summary in summaries if summary.done == False]
        completed = [(summary.pk, "completed")  for summary in summaries if summary.done == True]
        return render(
            request, 
            "articles.html", 
            {'username': session_user, 'summaries': to_be_done, 'completed': completed}
        )

    except Exception as e:
        print(e)
        return redirect("/login")

@login_required(login_url='/login')
def article_edit_view(request, id):
    summary_obj = SummaryTask.objects.get(pk = int(id))
    summary_txt = summary_obj.article
    gold_txt = summary_obj.gold 
    title_txt = summary_obj.title

    if request.method == "POST":
        print(request.POST)
        summary_obj.grammatical_correctness = int(request.POST.get('gc'))
        summary_obj.arrangement = int(request.POST.get('flow'))
        summary_obj.quality = int(request.POST.get('tq'))
        # professional = request.POST.get() 
        summary_obj.singlePoint = int(request.POST.get('concise'))
        summary_obj.enoughDetails = int(request.POST.get('enough'))
        summary_obj.subjectiveScore = int(request.POST.get('score'))

        summary_obj.done = True
        summary_obj.save()
        return redirect("/articles")

    return render(
        request, 
        "articleBody.html", 
        {
            'summary': summary_txt, 
            'title': title_txt, 
            'gold': gold_txt
        }
    )