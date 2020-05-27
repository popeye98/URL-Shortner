
from django.urls import path,include
from shortner.views import kirr_redirect_view,KirrCBView
from . import views
urlpatterns = [
    path('a/<str:sc>',views.kirr_redirect_view,name="Home"),
    path('b/<str:sc>',views.KirrCBView.as_view()),

]