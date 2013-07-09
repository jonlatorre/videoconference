from django.conf.urls.defaults import *
from django.conf.urls.static import static
from views import *

urlpatterns = patterns("",
    url(r"^(?P<sala>\w+)/(?P<clave>\w+)/$", vista_sala),
)
