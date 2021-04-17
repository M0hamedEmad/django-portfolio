from django import forms
from .models import Project, ActiveSections
from ckeditor_uploader.widgets import CKEditorUploadingWidget 

class ProjectForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Project
        fields = [
            'title',
            'description',
            'category',
            'created_at',
            'image',
            'active',
        ]


    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)
        
        classes = """block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 
                focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input"""

        self.fields['title'].widget.attrs = {
            'class': classes,
            'placeholder':'title of your project',
        }

        self.fields['description'].widget.attrs = {
             'class':"""block w-full mt-1 text-sm dark:text-gray-300 dark:border-gray-600 dark:bg-gray-700
            form-textarea focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:focus:shadow-outline-gray""",
            'rows':'19'
        }


        self.fields['category'].widget.attrs = {'class':classes}

        self.fields['active'].widget.attrs = { 'class': 
        """text-purple-600 form-checkbox focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:focus:shadow-outline-gray""",
        }

        self.fields['created_at'].widget.attrs = {
            'class':classes
        }

        self.fields['image'].widget.attrs = {
            'class':"project_form_img",
        }

class ActiveSectionForm(forms.ModelForm):

    class Meta:
        model = ActiveSections
        fields = [
            'about',
            'services',
            'portfolio',
            'experience',
            'contact',
        ]


    def __init__(self, *args, **kwargs):
        super(ActiveSectionForm, self).__init__(*args, **kwargs)

        classes =  """block w-full mt-1 text-sm dark:text-gray-300 dark:border-gray-600 dark:bg-gray-700 form-select focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:focus:shadow-outline-gray"""

        self.fields['about'].widget.attrs = { 'class': classes}
        self.fields['services'].widget.attrs = { 'class': classes}
        self.fields['portfolio'].widget.attrs = { 'class': classes}
        self.fields['experience'].widget.attrs = { 'class': classes}
        self.fields['contact'].widget.attrs = { 'class': classes}
