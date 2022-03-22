from django.shortcuts import render

# Create your views here.
def Sendmail(request):
    obj1 = SendMail.objects.all()
    form = SendMailForm()
    if request.method == 'POST':
        form = SendMailForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    form = SendMailForm()
    context = {'obj1': obj1,'form':form}
    return render(request,'home.html',context)