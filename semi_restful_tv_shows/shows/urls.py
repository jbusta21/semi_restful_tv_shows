from django.urls import path
from . import views

urlpatterns = [
    path('new_show', views.add_show),
    path('submit_show', views.submit_show),
    path('<int:show_id>/edit_show', views.edit_show),
    path('<int:show_id>', views.display_show),
    path('<int:show_id>/submit_edit', views.submit_edit),
    path('<int:show_id>/delete_show', views.delete_show)
]