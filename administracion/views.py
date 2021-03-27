from django.db.models import query
from django.shortcuts import render
from .models import MovimientoModel, PersonaModel, ProductoModel, CategoriaModel, UsuarioModel
from .serializers import MovimientoSerializer, PersonaSerializer, ProductoSerializer, CategoriaSerializer, UsuarioSerializer
#REST
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
# Create your views here.

class ProductosView(ListCreateAPIView): 
    #consulta a la base de datos para efectuar está vista 
    queryset=ProductoModel.objects.all() # SELECT * FROM
    # es la forma en la cual vamos a decorar el resultado, para mostrar al cliente
    serializer_class= ProductoSerializer
    def get(self, request):
        respuesta = self.get_serializer(self.get_queryset(), many=True)
        return Response({
            "ok":True,
            "content":respuesta.data,
            "message":None
        }, status=status.HTTP_200_OK)

    def post(self,request):
        producto = self.get_serializer(data=request.data)
        if producto.is_valid():
            producto.save()
            return Response({
                "ok":True,
                "content":producto.data,
                "message":"Se creo exitosamente el producto"
            }, status.HTTP_201_CREATED)
        else:
            return Response({
                "ok":False,
                "content":producto.errors,
                "message":"Hubo un error al guardar el producto"
            }, status.HTTP_400_BAD_REQUEST)

class ProductoView(RetrieveUpdateDestroyAPIView):
    queryset= ProductoModel.objects.all()
    serializer_class = ProductoSerializer
    def get(self, request, nombre):
        respuesta = self.get_serializer(self.get_queryset().filter(productoNombre__contains=nombre).first())
        return Response({
            "ok":True,
            "content":respuesta.data,
            "message":None
        })
    def put(self, request, id):
        producto = self.get_queryset().filter(productoId=id).first()
        respuesta = self.get_serializer(producto, data=request.data)
        if respuesta.is_valid():
            resultado = respuesta.update()
            return Response({
                "ok":True,
                "content":self.serializer_class(resultado).data,
                "message": "Se actulizo exitosamente el producto"
            }, status=status.HTTP_201_CREATED)
        else:
            return Response({
                "ok":False,
                "content":respuesta.errors,
                "message":"hubo un error al actualizar el producto"
            }, status.HTTP_400_BAD_REQUEST)
    def delete(self, request, id):
        producto = self.get_queryset().filter(productoId=id).first()
        respuesta = self.get_serializer(producto)
        respuesta.delete()
        return Response({
            "ok":True,
            "content":respuesta.data,
            "message":"Se elimino el producto exitosamente"
        })

class CategoriasView(ListCreateAPIView):
    queryset=CategoriaModel.objects.all() 
    serializer_class= CategoriaSerializer
    def get(self, request):
        respuesta = self.get_serializer(self.get_queryset(), many=True)
        return Response({
            "ok":True,
            "content":respuesta.data,
            "message":None
        }, status=status.HTTP_200_OK)

    def post(self, request):
        categoria = self.get_serializer(data=request.data)
        if categoria.is_valid():
            categoria.save()
            return Response({
                "ok":True,
                "content":categoria.data,
                "message":"Se creo exitosamente la categoria"
            }, status.HTTP_201_CREATED)
        else:
            return Response({
                "ok":False,
                "content":categoria.errors,
                "message":"Hubo un error al guardar la categoria"
            }, status.HTTP_400_BAD_REQUEST)

class CategoriaView(RetrieveUpdateDestroyAPIView):
    queryset= CategoriaModel.objects.all()
    serializer_class = CategoriaSerializer
    def get(self, request, id):
        respuesta = self.get_serializer(self.get_queryset().filter(categoriaId=id).first())
        return Response({
            "ok":True,
            "content":respuesta.data,
            "message":None
        })
    def put(self, request, id):
        categoria = self.get_queryset().filter(categoriaId=id).first()
        respuesta = self.get_serializer(categoria, data=request.data)
        if respuesta.is_valid():
            resultado = respuesta.update()
            return Response({
                "ok":True,
                "content":self.serializer_class(resultado).data,
                "message": "Se actulizo exitosamente la categoria"
            }, status=status.HTTP_201_CREATED)
        else:
            return Response({
                "ok":False,
                "content":respuesta.errors,
                "message":"hubo un error al actualizar la categoria"
            }, status.HTTP_400_BAD_REQUEST)
    def delete(self, request, id):
        categoria = self.get_queryset().filter(categoriaId=id).first()
        respuesta = self.get_serializer(categoria)
        respuesta.delete()
        return Response({
            "ok":True,
            "content":respuesta.data,
            "message":"Se elimino la categoria exitosamente"
        })

class UsuariosView(ListCreateAPIView):
    queryset = UsuarioModel.objects.all()
    serializer_class = UsuarioSerializer
    def get(self, request):
        respuesta = self.get_serializer(self.get_queryset(), many=True)
        return Response({
            "ok":True,
            "content":respuesta.data,
            "message":None
        }, status=status.HTTP_200_OK)

    def post(self, request):
        usuario = self.get_serializer(data=request.data)
        if usuario.is_valid():
            usuario.save()
            return Response({
                "ok":True,
                "content":usuario.data,
                "message":"Se creo exitosamente el usuario"
            }, status.HTTP_201_CREATED)
        else:
            return Response({
                "ok":False,
                "content":usuario.errors,
                "message":"Hubo un error al guardar el usuario"
            }, status.HTTP_400_BAD_REQUEST)

class UsuarioView(RetrieveUpdateDestroyAPIView):
    queryset = UsuarioModel.objects.all()
    serializer_class = UsuarioSerializer
    def get(self, request, id):
        respuesta = self.get_serializer(self.get_queryset().filter(usuarioId=id).first())
        return Response({
            "ok":True,
            "content":respuesta.data,
            "message":None
        })
    def put(self, request, id):
        usuario = self.get_queryset().filter(usuarioId=id).first()
        respuesta = self.get_serializer(usuario, data=request.data)
        if respuesta.is_valid():
            resultado = respuesta.update()
            return Response({
                "ok":True,
                "content":self.serializer_class(resultado).data,
                "message": "Se actulizo exitosamente el usuario"
            }, status=status.HTTP_201_CREATED)
        else:
            return Response({
                "ok":False,
                "content":respuesta.errors,
                "message":"hubo un error al actualizar el usuario"
            }, status.HTTP_400_BAD_REQUEST)
    def delete(self, request, id):
        usuario = self.get_queryset().filter(usuarioId=id).first()
        respuesta = self.get_serializer(usuario)
        respuesta.delete()
        return Response({
            "ok":True,
            "content":respuesta.data,
            "message":"Se elimino el usuario exitosamente"
        })

class PersonasView(ListCreateAPIView): 
    #consulta a la base de datos para efectuar está vista 
    queryset=PersonaModel.objects.all() # SELECT * FROM
    # es la forma en la cual vamos a decorar el resultado, para mostrar al cliente
    serializer_class= PersonaSerializer
    def get(self, request):
        respuesta = self.get_serializer(self.get_queryset(), many=True)
        return Response({
            "ok":True,
            "content":respuesta.data,
            "message":None
        }, status=status.HTTP_200_OK)

    def post(self,request):
        persona = self.get_serializer(data=request.data)
        if persona.is_valid():
            persona.save()
            return Response({
                "ok":True,
                "content":persona.data,
                "message":"Se creo exitosamente la persona"
            }, status.HTTP_201_CREATED)
        else:
            return Response({
                "ok":False,
                "content":persona.errors,
                "message":"Hubo un error al registrar los datos de la persona"
            },status.HTTP_400_BAD_REQUEST)

class PersonaView(RetrieveUpdateDestroyAPIView):
    queryset= PersonaModel.objects.all()
    serializer_class = PersonaSerializer
    def get(self, request, id):
        respuesta = self.get_serializer(self.get_queryset().filter(personaId=id).first())
        return Response({
            "ok":True,
            "content":respuesta.data,
            "message":None
        })
    def put(self, request, id):
        persona = self.get_queryset().filter(personaId=id).first()
        respuesta = self.get_serializer(persona, data=request.data)
        if respuesta.is_valid():
            resultado = respuesta.update()
            return Response({
                "ok":True,
                "content":self.serializer_class(resultado).data,
                "message": "Se actulizo la persona exitosamente"
            }, status=status.HTTP_201_CREATED)
        else:
            return Response({
                "ok":False,
                "content":respuesta.errors,
                "message":"hubo un error al actualizar a la persona"
            }, status.HTTP_400_BAD_REQUEST)
    def delete(self, request, id):
        persona = self.get_queryset().filter(personaId=id).first()
        respuesta = self.get_serializer(persona)
        respuesta.delete()
        return Response({
            "ok":True,
            "content":respuesta.data,
            "message":"Se elimino a la persona exitosamente"
        })

class MovimientosView(ListCreateAPIView):
    queryset = MovimientoModel.objects.all()
    serializer_class = MovimientoSerializer
    def get(self, request):
        respuesta = self.get_serializer(self.get_queryset(), many=True)
        return Response({
            "ok":True,
            "content":respuesta.data
        })

    def post(self, request):
       info= request.data
       productoUsuario = self.get_serializer(data=info)
       if productoUsuario.is_valid():
           producto = ProductoModel.objects.filter(productoId=info['productoId']).first()
           #persona = PersonaModel.objects.filter(personaId=['personaId']).first()
           usuario = UsuarioModel.objects.filter(usuarioId=info['usuarioId']).first()
           if producto.productoEstado==True and usuario.usuarioEstado==True:
                productoUsuario.save()
                return Response({
                    "ok":True,
                    "content":productoUsuario.data,
                    "message":"Se agrego exitosamente el movimiento"
                }, status.HTTP_201_CREATED)
           else:
                return Response({
                    "ok":False,
                    "content":None,
                    "message":"No se logro ingresar  correctamente los datos, producto o usuario no esta correctamente habilitados"
                }, status=status.HTTP_400_BAD_REQUEST)
       else:
            return Response({
                "ok":False,
                "content":productoUsuario.errors,
                "message":"Hubo un error al registrar el movimiento"
            })












