from django.urls import path
from .views import create_record,get_all_records, get_records, update_record, delete_record, search_record

urlpatterns = [
    path('create/record/', create_record ,name='create-record' ),
    path('get/records/', get_all_records ,name='get-all-records' ),
    path('get/records/<int:id>/', get_records ,name='get-records' ), # dynamic url
    path('update/record/<int:id>/', update_record ,name='update-record' ),
    path('delete/record/<int:id>/', delete_record ,name='delete-record' ),
    path('search/data/', search_record ,name='search-record' ),
]