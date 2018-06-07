from django.urls import path
from persona.views import *

urlpatterns = [
    path('', persona_page, name = "persona_page"),

    # Personas
    path('new/', new_persona, name = "new_persona"),
    path('save/', save_persona, name = "save_persona"),
    path('<int:persona_id>/', view_persona, name = "view_persona"),

    # Areas
    path('area/', area_page, name = "area_page"),
    path('area/save/', save_area, name = "save_area")
]
