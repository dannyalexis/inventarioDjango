from django.db import models
from django.db.models.fields import related

# Create your models here.
class CategoriaModel(models.Model):
    categoriaId = models.AutoField(auto_created=True, primary_key=True, unique=True, null=False, db_column='categoria_id')
    categoriaNombre= models.CharField(max_length=45, db_column='categoria_nombre')
    categoriaDescripcion= models.CharField(max_length=45, db_column='categoria_descripcion')
    categoriaEstado = models.BooleanField(default=True, db_column='categoria_estado')
    class Meta:
        db_table='t_categoria'
        verbose_name_plural = "Categorias"
        verbose_name = "Categoria"

    def __str__(self):
        return self.categoriaNombre

class ProductoModel(models.Model):
    productoId =models.AutoField(primary_key=True, unique=True, null=False, db_column='producto_id') 
    categoriaId = models.ForeignKey(CategoriaModel, on_delete=models.PROTECT, db_column='categoria_id', related_name='CategoriaProductos')
    productoNombre = models.CharField(max_length=45, db_column='producto_nombre')
    productoStock = models.CharField(max_length=45, db_column='producto_stock')
    productoDescripcion = models.CharField(max_length=45, db_column='producto_descripcion')
    productoImagen = models.CharField(max_length=45, db_column='producto_imagen')
    productoEstado = models.BooleanField(default=True, db_column='producto_estado')
    productoMedida= models.CharField(max_length=45, db_column='producto_medida')
    class Meta:
        db_table = 't_producto'
        verbose_name_plural = 'Productos'
        verbose_name = "Producto"
        
    def __str__(self):
        return self.productoNombre

class PersonaModel(models.Model):
    personaId =models.AutoField(primary_key=True, unique=True,null=False, db_column='persona_id')
    personaCargo= models.CharField(max_length=45, db_column='persona_cargo')
    personaNombre= models.CharField(max_length=45, db_column='persona_nombre')
    personaDocumento= models.CharField(max_length=45, db_column='persona_documento')
    personaTelefono= models.CharField(max_length=45, db_column='persona_Telefono')
    personaEstado= models.BooleanField(default=True, db_column='persona_estado')
    class Meta:
        db_table='t_persona'
        verbose_name_plural="Personas"
        verbose_name = "Persona" 
    def __str__(self):
        return self.personaNombre

class UsuarioModel(models.Model):
    usuarioId =models.AutoField( primary_key=True, unique=True,null=False, db_column='usuario_id')
    usuarioDocumento= models.CharField(max_length=45, db_column='usuario_documento')
    usuarioCargo= models.CharField(max_length=45, db_column='usuario_cargo')
    usuarioNombre= models.CharField(max_length=45, db_column='usuario_nombre')
    usuarioTelefono= models.CharField(max_length=45, db_column='usuario_telefono')
    usuarioUsers= models.CharField(max_length=45, db_column='usuario_users')
    usuarioEstado= models.BooleanField(default=True, db_column='usuario_estado')
    class Meta:
        db_table='t_usuario'
        verbose_name_plural='Usuarios'
        verbose_name="Usuario"
        
    def __str__(self):
        return self.usuarioNombre

class MovimientoModel(models.Model):
    movimientoId =models.AutoField( primary_key=True, unique=True,null=False, db_column='movimiento_id')
    movimientoTipo = models.CharField(max_length=45, db_column='movimiento_tipo')
    movimientoCantidad = models.IntegerField(db_column='movimiento_cantidad')
    movimientoFecha = models.DateTimeField(db_column='movimiento_fecha')
    personaId = models.ForeignKey(PersonaModel, on_delete=models.PROTECT, db_column='persona_id', related_name='PersonaMovimiento')
    usuarioId = models.ForeignKey(UsuarioModel, on_delete=models.PROTECT, db_column='usuario_id', related_name='UsuarioMovimiento')
    productoId = models.ForeignKey(ProductoModel, on_delete=models.PROTECT, db_column='producto_id', related_name='ProductoMovimiento')
    
    createdAt = models.DateTimeField(db_column='fecCreacion',auto_now_add=True) # auto_now_add sirve para cuando se
    updatedAt = models.DateTimeField(db_column='fecActualizacion', auto_now=True)
    class Meta:
        db_table='t_movimiento'
        verbose_name_plural = 'Movimientos'
        verbose_name = 'Movimiento'