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
    path('area/save/', save_area, name = "save_area"),

    # Puestos
    path('puesto/', puesto_page, name = "puesto_page"),
    path('puesto/save/', save_puesto, name = "save_puesto"),

    # Editar y eliminar Areas y Puestos
    path('editar/', editar_area_puesto, name = 'editar_area_puesto'),
    path('editar/area/', editar_area, name = 'editar_area'),
    path('editar/area/<int:area_id>/', save_edit_area, name = 'save_edit_area')
]
