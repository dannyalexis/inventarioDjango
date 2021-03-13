from django.urls import path
from .views import MovimientosView, PersonaView, PersonasView, ProductosView, ProductoView, CategoriasView,CategoriaView, UsuarioView, UsuariosView

urlpatterns = [
    path('productos', ProductosView.as_view(), name="Productos"),
    path('producto/<str:nombre>', ProductoView.as_view()),
    path('categorias', CategoriasView.as_view(), name="Categorias"),
    path('categoria/<int:id>', CategoriaView.as_view()),
    path('usuarios', UsuariosView.as_view(), name="Usuarios"),
    path('usuario/<int:id>', UsuarioView.as_view()),
    path('personas', PersonasView.as_view(), name="Personas"),
    path('persona/<int:id>', PersonaView.as_view()),
    path('movimientos', MovimientosView.as_view(), name="Movimientos"),
    

]