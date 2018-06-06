from django.urls import path
from persona.views import *

urlpatterns = [
    path('', persona_page, name = "persona_page"),
    path('new/', new_persona, name = "new_persona"),
    path('save/', save_persona, name = "save_persona"),
    path('<int:persona_id>/', view_persona, name = "view_persona"),
]
