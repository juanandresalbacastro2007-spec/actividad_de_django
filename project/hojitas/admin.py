from django.contrib import admin
# Register your models here.
from . models import Hoja #la información que necesito esta en modelo
#procedemos a registrarlo en el admin
admin.site.register(Hoja) #es decir que cuando se ejecute el administradoreste ya tenga la Hoja para manipular.