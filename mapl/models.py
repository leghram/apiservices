from django.db import models

# Create your models here.
class Operadora(models.Model):
  id_p = models.AutoField(primary_key=True)
  nombre = models.CharField(max_length=30, unique=True, default='desconocido')

  class Meta:
    db_table = 'operadoras'
    ordering = ['id_p','nombre']



class Moneda(models.Model):
  id_p = models.AutoField(primary_key=True)
  nombre = models.CharField(max_length=30, unique=True, default='desconocido')
  cambio_soles = models.DecimalField(max_digits=5 , decimal_places=2)

  class Meta:
    db_table = 'monedas'
    ordering = ['id_p','nombre','cambio_soles']



class Pais(models.Model):
  id_p = models.AutoField(primary_key=True)
  nombre = models.CharField(max_length=30, unique=True, default='desconocido')

  class Meta:
    db_table = 'paises'
    ordering = ['id_p','nombre']




class Ciudad(models.Model):
  id_p = models.AutoField(primary_key=True)
  nombre = models.CharField(max_length=30, unique=True, default='desconocido')
  #FOREIGN KEY PARA DEFINIR LA FOREIGN
  id_pais = models.ForeignKey(to=Pais, related_name='paises', on_delete=models.CASCADE)

  class Meta:
    db_table = 'ciudades'
    ordering = ['id_p','nombre']


  

class Rol(models.Model):
  id_p = models.AutoField(primary_key=True)
  nombre = models.CharField(max_length=30, unique=True, default='usuario')

  class Meta:
    db_table = 'roles'
    ordering = ['id_p','nombre']



class TipoOperacion(models.Model):
  id_p = models.AutoField(primary_key=True)
  nombre = models.CharField(max_length=30, unique=True, default='deposito')

  class Meta:
    db_table = 'tipos_operaciones'
    ordering = ['id_p','nombre']


class CategoriaUsuario(models.Model):
  id_p = models.AutoField(primary_key=True)
  nombre = models.CharField(max_length=30, unique=True, default='normal')

  class Meta:
    db_table = 'categorias_usuarios'
    ordering = ['id_p','nombre']



class TipoPrestamo(models.Model):
  id_p = models.AutoField(primary_key=True)
  nombre = models.CharField(max_length=30, unique=True, default='personal')

  class Meta:
    db_table = 'tipos_prestamos'
    ordering = ['id_p','nombre']



class TipoInteres(models.Model):
  id_p = models.AutoField(primary_key=True)
  nombre = models.CharField(max_length=30, unique=True, default='normal')
  porcentaje = models.IntegerField()

  class Meta:
    db_table = 'tipos_intereses'
    ordering = ['id_p','nombre']



class Agencia(models.Model):
  id_p = models.AutoField(primary_key=True)
  nombre = models.CharField(max_length=30, unique=True, default='arequipa')
  ciudad_id = models.ForeignKey(to=Ciudad, related_name='ciudadesAgencia', on_delete=models.CASCADE)
  pais_id = models.ForeignKey(to=Pais, related_name='paisesAgencia', on_delete=models.CASCADE)

  class Meta:
    db_table = 'agencias'
    ordering = ['id_p','nombre']


class CategoriaPublicacion(models.Model):
  id_p = models.AutoField(primary_key=True)
  nombre = models.CharField(max_length=30, unique=True, default='negocios')

  class Meta:
    db_table = 'categorias_publicaciones'
    ordering = ['id_p','nombre']




class PublicacionBanco(models.Model):
  id_p = models.AutoField(primary_key=True)
  titulo = models.CharField(max_length=150, default='Sin Titulo')
  texto = models.TextField()
  url_imagen = models.CharField(max_length=300, default='http://loremflickr.com/640/480/business')
  categoria_publicacion_id = models.ForeignKey(to=CategoriaPublicacion, related_name='categoriasid', on_delete=models.CASCADE)

  class Meta:
    db_table = 'publicaciones_banco'
    ordering = ['id_p','titulo']


class Usuario(models.Model):
  id_p = models.AutoField(primary_key=True)
  nombre = models.CharField(max_length=30, default='Jhon Doe')
  apellido = models.CharField(max_length=30, default='Kard')
  direcion = models.CharField(max_length=100, default='39178 Ernser Haven')
  fecha_nacimiento = models.DateField()
  correo = models.EmailField(unique=True)
  contrasena = models.CharField(max_length=100, default='contrasena')
  url_perfil = models.CharField(max_length=200, default='https://cloudflare-ipfs.com/ipfs/Qmd3W5DuhgHirLHGVixi6V76LhCkZUz6pnFt5AJBiyvHye/avatar/1071.jpg')
  ciudad_id = models.ForeignKey(to=Ciudad, related_name='ciudadusario', on_delete=models.CASCADE)
  pais_id = models.ForeignKey(to=Pais, related_name='paisusuario', on_delete=models.CASCADE)
  rol_id = models.ForeignKey(to=Rol, related_name='rolusuario',on_delete=models.CASCADE, default='1')

  class Meta:
    db_table = 'usuarios'
    ordering = ['id_p','nombre']



class Comentario(models.Model):
  id_p = models.AutoField(primary_key=True)
  descripcion = models.CharField(max_length=300, default='Sin comentarios')
  usuario_id = models.ForeignKey(to=Usuario, related_name='usuariocomentario', on_delete=models.CASCADE)
  publicacion_banco_id = models.ForeignKey(to=PublicacionBanco, related_name='publicacionbancocomentario', on_delete=models.CASCADE) 

  class Meta:
    db_table = 'comentarios'
    ordering = ['id_p','descripcion']


class NumeroTelefono(models.Model):
  id_p = models.AutoField(primary_key=True)
  numero = models.IntegerField()
  usuario_id = models.ForeignKey(to=Usuario, related_name='numerousuario',on_delete=models.CASCADE)
  operadora_id = models.ForeignKey(to=Operadora, related_name='numerooperadora',on_delete=models.CASCADE)

  class Meta:
    db_table = 'numeros_telefonos'
    ordering = ['id_p','numero']



class CuentaBancaria(models.Model):
  id_p = models.AutoField(primary_key=True)
  numero_cuenta = models.CharField(max_length=15, unique=True)
  numero_tarjeta = models.CharField(max_length=20, unique=True)
  pin = models.CharField(max_length=6)
  usuario_id = models.ForeignKey(to=Usuario, related_name='cuentausario', on_delete=models.CASCADE)
  moneda_id = models.ForeignKey(to=Moneda, related_name='monedacuenta', on_delete=models.CASCADE)

  class Meta:
    db_table = 'cuentas_bancarias'
    ordering = ['id_p','numero_cuenta']


# a partir d aqui adsfasdf asdf asdf 
# asdfas 




class Prestamo(models.Model):
  id_p = models.AutoField(primary_key=True)
  monto = models.DecimalField(max_digits=10 , decimal_places=2)
  fecha_inicio = models.DateField()
  fecha_final = models.DateField()
  cuenta_bancaria_id = models.ForeignKey(to=CuentaBancaria, related_name='cuentaprestamo', on_delete=models.CASCADE)
  tipo_prestamo_id = models.ForeignKey(to=TipoPrestamo, related_name='tipoprestamo', on_delete=models.CASCADE)

  class Meta:
    db_table = 'prestamos'
    ordering = ['id_p','monto']






class Operacion(models.Model):
  id_p = models.AutoField(primary_key=True)
  monto = models.DecimalField(max_digits=10 , decimal_places=2)
  fecha= models.DateField()
  tipo_operacion = models.ForeignKey(to=TipoOperacion, related_name='operacionoperacion', on_delete=models.CASCADE)
  cuenta_bancaria_destino_id = models.ForeignKey(to=CuentaBancaria, related_name='cuentabancaoperacion', on_delete=models.CASCADE)


  class Meta:
    db_table = 'operaciones'
    ordering = ['id_p','monto']





class TipoPromocion(models.Model):
  id_p = models.AutoField(primary_key=True)
  descripcion = models.CharField(max_length=30, unique=True)
  cantidad = models.IntegerField()

  class Meta:
    db_table = 'tipos_promociones'
    ordering = ['id_p','cantidad']






class PromocionDisponibleUsuario(models.Model):
  id_p = models.AutoField(primary_key=True)
  cuenta_bancaria_id = models.ForeignKey(to=CuentaBancaria, related_name='promocuentabancarai', on_delete=models.CASCADE)
  tipo_promocion_id = models.ForeignKey(to=TipoPromocion, related_name='promociondisponible', on_delete=models.CASCADE)

  class Meta:
    db_table = 'promociones_disponibles_usuarios'
    ordering = ['id_p']





