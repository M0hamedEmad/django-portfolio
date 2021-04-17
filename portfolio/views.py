from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from .decorators import admin_only
from .models import Project, ActiveSections
from .forms import ProjectForm, ActiveSectionForm

@login_required
@admin_only
def create_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, files=request.FILES)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.author = request.user
            new_form.save()
            form = ProjectForm()

    form = ProjectForm()

    context = {
        'title':'Add New Project',
        'form':form,
    }
    return render(request, 'portfolio/project_form.html', context)

@login_required
@admin_only
def updateProject(request, pk):
    instance = get_object_or_404(Project, id=pk)

    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=instance, files=request.FILES)
        if form.is_valid():
            form.save()
            form = ProjectForm(instance=instance)
    
    form = ProjectForm(instance=instance)

    context = {
        'title':f"update | {instance.title}",
        'form':form,
    }
    return render(request, 'portfolio/project_form.html', context)

@login_required
@admin_only
def deleteProject(request, pk):
    instance = get_object_or_404(Project, id=pk)

    if request.method == 'POST':
        instance.delete()
        return redirect('/')
    
    context = {
        'title':f"delete {instance.title}",
        'instance':instance,
    }
  
    return render(request, 'portfolio/delete_project.html', context)

@login_required
@admin_only
def dashboard(request):
    projects = Project.objects.all()
    active_projects_count = projects.filter(active=True).count

    paginator = Paginator(projects, 25)
    
    page_number = request.GET.get('page')
    try:
        projects = paginator.get_page(page_number)
    except EmptyPage:
        projects = paginator.get_page(paginator.page_num)

    except PageNotAnInteger:
        projects = paginator.get_page('1')


    context = {
        'title':'dashboard',
        'projects':projects,
        'active_projects_count':active_projects_count
    }
    
    return render(request, 'portfolio/index.html', context)

@login_required
@admin_only
def activeSection(request):

    instance = ActiveSections.objects.first()
    
    if instance:
        form = ActiveSectionForm(request.POST or None, instance=instance)
        if form.is_valid():
            form.save()
            form = ActiveSectionForm(instance=instance)
       
    else:
        form = ActiveSectionForm(request.POST or None)
        if form.is_valid():
            form.save()
            form = ActiveSectionForm(instance=request.POST)
        
    context = {
        'title':f"Active section",
        'form':form,
    }
    return render(request, 'portfolio/project_form.html', context)

def home(request):
    projects = Project.objects.all().order_by('created_at')[0:3]

    active_section = ActiveSections.objects.first()
    if active_section:
        about       = active_section.about
        services    = active_section.services
        portfolio   = active_section.portfolio
        experience  = active_section.experience
        contact     = active_section.contact

    else:
        pass

    context = {
        'title':'Portfolio',
        'projects':projects,
        'about':about,
        'services':services,
        'portfolio':portfolio,
        'experience':experience,
        'contact':contact,
    }
    return render(request, 'home.html', context)
