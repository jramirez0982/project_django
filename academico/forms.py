from django.forms import *
from academico.models import *

class CarreraForm(ModelForm) :
    class Meta :
        model = Carrera
        fields = "__all__"
