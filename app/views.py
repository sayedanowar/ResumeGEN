from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http.response import HttpResponseRedirect
from app.models import ResumeForm
from app.forms import LoginForm, SignupForm, UpdateUserForm
from django.contrib.messages.views import SuccessMessageMixin
from django.views import generic
from django.contrib.auth.models import User
from django.urls import reverse_lazy

# Create your views here.

def home(request):
    return render(request, 'index.html')

def userLogin(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            fm = LoginForm(request=request, data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                upass = fm.cleaned_data['password']
                user = authenticate(username=uname,password=upass)
                if user is not None:
                    login(request, user)
                    return HttpResponseRedirect('/dashboard/')
        else:
            fm = LoginForm()
        return render(request, 'logIn.html', {'form': fm})
    else:
        return HttpResponseRedirect('/dashboard/')

def userSignUp(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            fm = SignupForm(request.POST)
            if fm.is_valid():
                fm.save()
                fm = SignupForm()
                return HttpResponseRedirect('/login/')
        else:
            fm = SignupForm()
        return render(request, 'signUp.html', {'form': fm})
    else:
        return HttpResponseRedirect('/dashboard/')

def userLogOut(request):
    if request.user.is_authenticated:
        logout(request)
        return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/login/')

def userProfile(request):
    if request.user.is_authenticated:
        current_user = User.objects.get(id=request.user.id)
        fm = UpdateUserForm(request.POST or None, instance=current_user)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect('/dashboard/')
        return render(request, 'userProfile.html', {'form': fm})
    else:
        return HttpResponseRedirect('/login/')

def preview(request):
    if request.user.is_authenticated:
        details = ResumeForm.objects.filter(user=request.user)
        if(details):
            data = details[0]
        else:
            data = {}
        return render(request, 'preview.html', {'data': data})
    else:
        return HttpResponseRedirect('/login/')

def dashboard(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            userDetails = ResumeForm.objects.filter(user=request.user)
            if(userDetails):
                userDetails = userDetails[0]
                userDetails.fullname = request.POST.get('fullname')
                userDetails.jobTitle = request.POST.get('jobTitle')
                userDetails.email = request.POST.get('email')
                userDetails.ph = request.POST.get('ph')
                userDetails.location = request.POST.get('location')
                userDetails.portfolio = request.POST.get('portfolio')
                userDetails.siteLabel = request.POST.get('siteLabel')
                userDetails.facebook = request.POST.get('facebook')
                userDetails.fb_uname = request.POST.get('fb_uname')
                userDetails.instagram = request.POST.get('instagram')
                userDetails.ig_uname = request.POST.get('ig_uname')
                userDetails.twitter = request.POST.get('twitter')
                userDetails.tw_uname = request.POST.get('tw_uname')
                userDetails.gitHub = request.POST.get('gitHub')
                userDetails.gh_uname = request.POST.get('gh_uname')
                userDetails.linkedIn = request.POST.get('linkedIn')
                userDetails.ln_uname = request.POST.get('ln_uname')
                userDetails.about = request.POST.get('about')
                userDetails.eduName1 = request.POST.get('eduName1')
                userDetails.eduYear1 = request.POST.get('eduYear1')
                userDetails.eduType1 = request.POST.get('eduType1')
                userDetails.eduLoc1 = request.POST.get('eduLoc1')
                userDetails.eduGPA1 = request.POST.get('eduGPA1')
                userDetails.eduName2 = request.POST.get('eduName2')
                userDetails.eduYear2 = request.POST.get('eduYear2')
                userDetails.eduType2 = request.POST.get('eduType2')
                userDetails.eduLoc2 = request.POST.get('eduLoc2')
                userDetails.eduGPA2 = request.POST.get('eduGPA2')
                userDetails.eduName3 = request.POST.get('eduName3')
                userDetails.eduYear3 = request.POST.get('eduYear3')
                userDetails.eduType3 = request.POST.get('eduType3')
                userDetails.eduLoc3 = request.POST.get('eduLoc3')
                userDetails.eduGPA3 = request.POST.get('eduGPA3')
                userDetails.skill1 = request.POST.get('skill1')
                userDetails.skillDesc1 = request.POST.get('skillDesc1')
                userDetails.skill2 = request.POST.get('skill2')
                userDetails.skillDesc2 = request.POST.get('skillDesc2')
                userDetails.skill3 = request.POST.get('skill3')
                userDetails.skillDesc3 = request.POST.get('skillDesc3')
                userDetails.skill4 = request.POST.get('skill4')
                userDetails.skillDesc4 = request.POST.get('skillDesc4')
                userDetails.skill5 = request.POST.get('skill5')
                userDetails.skillDesc5 = request.POST.get('skillDesc5')
                userDetails.project1 = request.POST.get('project1')
                userDetails.projectLink1 = request.POST.get('projectLink1')
                userDetails.project1Desc1 = request.POST.get('project1Desc1')
                userDetails.project1Desc2 = request.POST.get('project1Desc2')
                userDetails.projectDate1 = request.POST.get('projectDate1')
                userDetails.project2 = request.POST.get('project2')
                userDetails.projectLink2 = request.POST.get('projectLink2')
                userDetails.project2Desc1 = request.POST.get('project2Desc1')
                userDetails.project2Desc2 = request.POST.get('project2Desc2')
                userDetails.projectDate2 = request.POST.get('projectDate2')
                userDetails.certName1 = request.POST.get('certName1')
                userDetails.certIssuer1 = request.POST.get('certIssuer1')
                userDetails.certLink1 = request.POST.get('certLink1')
                userDetails.certYear1 = request.POST.get('certYear1')
                userDetails.certName2 = request.POST.get('certName2')
                userDetails.certIssuer2 = request.POST.get('certIssuer2')
                userDetails.certLink2 = request.POST.get('certLink2')
                userDetails.certYear2 = request.POST.get('certYear2')
                userDetails.lang1 = request.POST.get('lang1')
                userDetails.langDesc1 = request.POST.get('langDesc1')
                userDetails.lang2 = request.POST.get('lang2')
                userDetails.langDesc2 = request.POST.get('langDesc2')
                userDetails.lang3 = request.POST.get('lang3')
                userDetails.langDesc3 = request.POST.get('langDesc3')
                userDetails.interests1 = request.POST.get('interests1')
                userDetails.interests2 = request.POST.get('interests2')
                userDetails.interests3 = request.POST.get('interests3')
                userDetails.interests4 = request.POST.get('interests4')
                userDetails.interests5 = request.POST.get('interests5')
                userDetails.save()
            else:
                fullname = request.POST.get('fullname')
                jobTitle = request.POST.get('jobTitle')
                email = request.POST.get('email')
                ph = request.POST.get('ph')
                location = request.POST.get('location')
                portfolio = request.POST.get('portfolio')
                siteLabel = request.POST.get('siteLabel')
                facebook = request.POST.get('facebook')
                fb_uname = request.POST.get('fb_uname')
                instagram = request.POST.get('instagram')
                ig_uname = request.POST.get('ig_uname')
                twitter = request.POST.get('twitter')
                tw_uname = request.POST.get('tw_uname')
                gitHub = request.POST.get('gitHub')
                gh_uname = request.POST.get('gh_uname')
                linkedIn = request.POST.get('linkedIn')
                ln_uname = request.POST.get('ln_uname')
                about = request.POST.get('about')
                eduName1 = request.POST.get('eduName1')
                eduYear1 = request.POST.get('eduYear1')
                eduType1 = request.POST.get('eduType1')
                eduLoc1 = request.POST.get('eduLoc1')
                eduGPA1 = request.POST.get('eduGPA1')
                eduName2 = request.POST.get('eduName2')
                eduYear2 = request.POST.get('eduYear2')
                eduType2 = request.POST.get('eduType2')
                eduLoc2 = request.POST.get('eduLoc2')
                eduGPA2 = request.POST.get('eduGPA2')
                eduName3 = request.POST.get('eduName3')
                eduYear3 = request.POST.get('eduYear3')
                eduType3 = request.POST.get('eduType3')
                eduLoc3 = request.POST.get('eduLoc3')
                eduGPA3 = request.POST.get('eduGPA3')
                skill1 = request.POST.get('skill1')
                skillDesc1 = request.POST.get('skillDesc1')
                skill2 = request.POST.get('skill2')
                skillDesc2 = request.POST.get('skillDesc2')
                skill3 = request.POST.get('skill3')
                skillDesc3 = request.POST.get('skillDesc3')
                skill4 = request.POST.get('skill4')
                skillDesc4 = request.POST.get('skillDesc4')
                skill5 = request.POST.get('skill5')
                skillDesc5 = request.POST.get('skillDesc5')
                project1 = request.POST.get('project1')
                projectLink1 = request.POST.get('projectLink1')
                project1Desc1 = request.POST.get('project1Desc1')
                project1Desc2 = request.POST.get('project1Desc2')
                projectDate1 = request.POST.get('projectDate1')
                project2 = request.POST.get('project2')
                projectLink2 = request.POST.get('projectLink2')
                project2Desc1 = request.POST.get('project2Desc1')
                project2Desc2 = request.POST.get('project2Desc2')
                projectDate2 = request.POST.get('projectDate2')
                certName1 = request.POST.get('certName1')
                certIssuer1 = request.POST.get('certIssuer1')
                certLink1 = request.POST.get('certLink1')
                certYear1 = request.POST.get('certYear1')
                certName2 = request.POST.get('certName2')
                certIssuer2 = request.POST.get('certIssuer2')
                certLink2 = request.POST.get('certLink2')
                certYear2 = request.POST.get('certYear2')
                lang1 = request.POST.get('lang1')
                langDesc1 = request.POST.get('langDesc1')
                lang2 = request.POST.get('lang2')
                langDesc2 = request.POST.get('langDesc2')
                lang3 = request.POST.get('lang3')
                langDesc3 = request.POST.get('langDesc3')
                interests1 = request.POST.get('interests1')
                interests2 = request.POST.get('interests2')
                interests3 = request.POST.get('interests3')
                interests4 = request.POST.get('interests4')
                interests5 = request.POST.get('interests5')
                data = ResumeForm(user=request.user, fullname=fullname, jobTitle=jobTitle, email=email, ph=ph, location=location, portfolio=portfolio, siteLabel=siteLabel, facebook=facebook, instagram=instagram, twitter=twitter, gitHub=gitHub, linkedIn=linkedIn, fb_uname=fb_uname, ig_uname=ig_uname, tw_uname=tw_uname, gh_uname=gh_uname, ln_uname=ln_uname, about=about, eduName1=eduName1, eduYear1=eduYear1, eduType1=eduType1, eduLoc1=eduLoc1, eduGPA1=eduGPA1, eduName2=eduName2, eduYear2=eduYear2, eduType2=eduType2, eduLoc2=eduLoc2, eduGPA2=eduGPA2, eduName3=eduName3, eduYear3=eduYear3, eduType3=eduType3, eduLoc3=eduLoc3, eduGPA3=eduGPA3, skill1=skill1, skill2=skill2, skill3=skill3, skill4=skill4, skill5=skill5, skillDesc1=skillDesc1, skillDesc2=skillDesc2, skillDesc3=skillDesc3, skillDesc4=skillDesc4, skillDesc5=skillDesc5, project1=project1, projectLink1=projectLink1, project1Desc1=project1Desc1, project1Desc2=project1Desc2, projectDate1=projectDate1, project2=project2, projectLink2=projectLink2, project2Desc1=project2Desc1, project2Desc2=project2Desc2, projectDate2=projectDate2, certName1=certName1, certIssuer1=certIssuer1, certLink1=certLink1, certYear1=certYear1, certName2=certName2, certIssuer2=certIssuer2, certLink2=certLink2, certYear2=certYear2, lang1=lang1, lang2=lang2, lang3=lang3, langDesc1=langDesc1, langDesc2=langDesc2, langDesc3=langDesc3, interests1=interests1, interests2=interests2, interests3=interests3, interests4=interests4, interests5=interests5)
                data.save()
            return HttpResponseRedirect('/preview/')
        details = ResumeForm.objects.filter(user=request.user)
        if(details):
            data = details[0]
        else:
            data = {}
        return render(request, 'dashboard.html', {'data': data})
    else:
        return HttpResponseRedirect('/login/')

class deleteUser(SuccessMessageMixin, generic.DeleteView):
    model = User
    template_name = 'deleteUser.html'
    success_url = reverse_lazy('home')
    
def error404(request, exception):
    return render(request, '404.html', status=404)

def error500(request):
    return render(request, '500.html', status=500)