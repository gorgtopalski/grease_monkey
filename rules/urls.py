from django.urls import path, re_path

from rules.views import RulesCreateView, RulesDetailsView, RulesListView, SelectProductionToCreateRuleView

app_name = 'rules'

urlpatterns = [
    path('<int:production>/add', RulesCreateView.as_view(), name='rules-add'),
    path('<int:production>/update', RulesCreateView.as_view(), name='rules-update'),
    path('<int:production>/', RulesDetailsView.as_view(), name='rules-show'),
    path('', RulesListView.as_view(), name='rules-list'),
    path('select/', SelectProductionToCreateRuleView.as_view(), name='rules-select'),
]