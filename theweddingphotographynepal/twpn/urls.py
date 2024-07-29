"""theweddingphotographynepal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from . import views
from .views import AddServiceView, ProfileEdit, ServiceView, ServiceEdit, AddImageView

urlpatterns = [
    path('', views.index, name="TWPN Home"),
    path('about/', views.about, name="About Us"),
    path('studios/', views.studios, name="Wedding Photographers"),
    path('gallery/', views.gallery, name="Gallery"),
    path('membership/', views.membership, name="membership"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('kathmandu/', views.kathmandu, name="Kathmandu"),
    path('lalitpur/', views.lalitpur, name="Lalitpur"),
    path('bhaktapur/', views.bhaktapur, name="Bhaktapur"),
    path('studioview/', views.studioview, name="studioview"),
    path('selectvendor/', views.selectvendor, name="selectvendor"),
    path('comparetable/', views.comparetable, name="comparetable"),
    path('contactus', views.contactus, name="contactus"),
    path('requestid', views.requestid, name="requestid"),
    path('requestquote/', views.requestquote, name="requestquote"),
    path('addreview/', views.addreview, name="addreview"),
    path('editprofile/<int:pk>', ProfileEdit.as_view(), name="editprofile"),
    path('viewreview/', views.viewreview, name="viewreview"),
    path('viewquote/', views.viewquote, name="viewquote"),
    path('addservice/', AddServiceView.as_view(), name="addservice"),
    path('addimage/', AddImageView.as_view(), name="addimage"),
    path('viewservice/', ServiceView.as_view(), name="viewservice"),
    path('editservice/<int:pk>', ServiceEdit.as_view(), name="editservice"),
]
