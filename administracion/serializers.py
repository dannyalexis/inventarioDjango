from django.db.models import fields
from .models import MovimientoModel, PersonaModel, ProductoModel, CategoriaModel, UsuarioModel

#rest
from rest_framework import serializers

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductoModel
        fields = "__all__"
    def update(self):
        self.instance.productoNombre = self.validated_data.get("productoNombre",self.instance.productoNombre)
        self.instance.productoStock = self.validated_data.get("productoStock",self.instance.productoStock)
        self.instance.productoDescripcion = self.validated_data.get("productoDescripcion",self.instance.productoDescripcion)
        #self.instance.productoImagen=self.validated_data.get("productoImagen",self.instance.productoImagen)
        self.instance.productoEstado=self.validated_data.get("productoEstado",self.instance.productoEstado)
        self.instance.productoMedida =self.validated_data.get("productoMedida",self.instance.productoMedida)
        self.instance.categoriaId = self.validated_data.get("categoriaId",self.instance.categoriaId)
        self.instance.save()
        return self.instance

    def delete(self):
        self.instance.productoEstado = False
        self.instance.save()
        return self.instance

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriaModel
        fields = "__all__"
    def update(self):
        self.instance.categoriaNombre = self.validated_data.get("categoriaNombre", self.instance.categoriaNombre)
        self.instance.categoriaDescripcion = self.validated_data.get("categoriaDescripcion", self.instance.categoriaDescripcion)
        self.instance.save()
        return self.instance
    def delete(self):
        self.instance.categoriaEstado = False
        self.instance.save()
        return self.instance

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsuarioModel
        fields="__all__"
    
    def update(self):
        self.instance.usuarioDocumento = self.validated_data.get("usuarioDocumento", self.instance.usuarioDocumento)
        self.instance.usuarioCargo = self.validated_data.get("usuarioCargo", self.instance.usuarioCargo)
        self.instance.usuarioNombre = self.validated_data.get("usuarioNombre",self.instance.usuarioNombre)
        self.instance.usuarioTelefono = self.validated_data.get("usuarioTelefono", self.instance.usuarioTelefono)
        self.instance.usuarioUsers = self.validated_data.get("usuarioUsers", self.instance.usuarioUsers)
        self.instance.usuarioEstado = self.validated_data.get("usuarioEstado", self.instance.usuarioEstado)
        self.instance.save()
        return self.instance

    def delete(self):
        self.instance.usuarioEstado = False
        self.instance.save()
        return self.instance

class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonaModel
        fields="__all__"
    def update(self):
        self.instance.personaCargo = self.validated_data.get("personaCargo", self.instance.personaCargo)
        self.instance.personaNombre = self.validated_data.get("personaNombre", self.instance.personaNombre)
        self.instance.personaDocumento = self.validated_data.get("personaDocumento", self.instance.personaDocumento)
        self.instance.personaTelefono = self.validated_data.get("personaTelefono", self.instance.personaTelefono)
        self.instance.personaEstado = self.validated_data.get("personaEstado", self.instance.personaEstado)
        self.instance.save()
        return self.instance
    
    def delete(self):
        self.instance.personaEstado = False
        self.instance.save()
        return self.instance

class MovimientoSerializer(serializers.ModelSerializer):
    #persona = PersonaSerializer(source="personaId", read_only=True)
    usuario = UsuarioSerializer(source="usuarioId", read_only=True)
    producto = ProductoSerializer(source="productoId", read_only=True)
    class Meta:
        model= MovimientoModel
        fields="__all__"
        #exclude = ["personaId","usuarioId","productoId"]












