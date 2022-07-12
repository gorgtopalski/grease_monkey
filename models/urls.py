from django.urls import path, re_path
from models.views import ModelCreateView, ModelDetailView, ModelListView, ModelUpdateView, ProductionCreateView, ProductionDetailView, ProductionJobChange, ProductionListView, ProductionListViewJson, ProductionUpdateView 

app_name = 'models'

urlpatterns = [
    path('add/', ModelCreateView.as_view(), name='model-add'),
    path('<int:pk>/', ModelDetailView.as_view(), name='model-show'),
    path('<int:pk>/update/', ModelUpdateView.as_view(), name='model-update'),
    path('', ModelListView.as_view(), name='model-list'),

    path('<int:model>/production/add/', ProductionCreateView.as_view(), name='production-add'),
    path('<int:model>/production/add/<int:line>/<int:production>/', ProductionCreateView.as_view(), name='production-add'),
    path('production/<int:pk>/', ProductionDetailView.as_view(), name='production-show'),
    path('production/<int:pk>/update/', ProductionUpdateView.as_view(), name='production-update'),
    path('production/change/', ProductionJobChange.as_view(), name='production-job-change'),
    path('production/', ProductionListView.as_view(), name='production-list'),
    re_path(r'^production/datatable/data/$', ProductionListViewJson.as_view(), name='production-list-json'),
]