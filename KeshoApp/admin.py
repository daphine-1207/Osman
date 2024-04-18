from django.contrib import admin
from .models import * #here we are trying to acces our classes which are our models upon wc we are going to build interfaces
#from .models import CategoryStay, Babe
#from .models import CategoryStay
#from .models import Babe

# Register your models here.
admin.site.register(CategoryStay)
admin.site.register(Babe)
admin.site.register(Payment)