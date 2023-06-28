
from . import data_handler
from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter
from django.urls import path

router = DefaultRouter()
router.register(r'accounts', AccountViewSet)
router.register(r'destinations', DestinationViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('incoming_data', data_handler.incoming_data, name='incoming_data'),
    path('incoming_data', data_handler.incoming_data),
    path('accounts/<int:account_id>/destinations/', DestinationListView.as_view(), name='destination-list'),

]


#path('incoming_data', DestinationViewSet.as_view({'post': 'create'}), name='incoming_data'),
#  path('', include(router.urls)),
#  path('server/incoming_data', data_handler.data_handler),
#  path('accounts/<int:account_id>/destinations/', DestinationListView.as_view(), name='destination-list'),
#  path('post', include(router.urls)),
