from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('categorias/', views.lista_categorias, name='lista_categorias'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('signup/', views.signup, name='signup'),
    path('listSubastas/', views.ListarYParticiparSubastas.as_view(), name='listSubastas'),
    path('agregarSubasta/', views.agregarSubasta, name='agregarSubasta'),
    path('participacionSubasta/<int:subasta_id>/<int:monto>/', views.participacionSubasta, name='participacionSubasta'),
    path('checkout/<int:id_producto>/', views.CheckOut, name='checkout'),
    path('payment-success/<int:id_producto>/', views.PaymentSuccessful, name='payment-success'),
    path('payment-failed/<int:id_producto>/', views.paymentFailed, name='payment-failed'),
    path('products/', views.ProductView, name='products'),
]
