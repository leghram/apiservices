from rest_framework import serializers
# from .models import Operadora, Moneda, Pais, Ciudad
from .models import *


class OperadoraSerializer(serializers.ModelSerializer):
  class Meta:
    model = Operadora
    fields ='__all__'


class MonedaSerializer(serializers.ModelSerializer):
  class Meta:
    model = Moneda
    fields ='__all__'


class PaisSerializer(serializers.ModelSerializer):
  class Meta:
    model = Pais
    fields ='__all__'


class CiudadSerializer(serializers.ModelSerializer):
  class Meta:
    model = Ciudad
    fields ='__all__'



class RolSerializer(serializers.ModelSerializer):
  class Meta:
    model = Rol
    fields ='__all__'


class TipoOperacionSerializer(serializers.ModelSerializer):
  class Meta:
    model = TipoOperacion
    fields ='__all__'


class CategoriaUsuarioSerializer(serializers.ModelSerializer):
  class Meta:
    model = CategoriaUsuario
    fields ='__all__'


class TipoPrestamoSerializer(serializers.ModelSerializer):
  class Meta:
    model = TipoPrestamo
    fields ='__all__'


class TipoInteresSerializer(serializers.ModelSerializer):
  class Meta:
    model = TipoInteres
    fields ='__all__'



class AgenciaSerializer(serializers.ModelSerializer):
  class Meta:
    model = Agencia
    fields ='__all__'


class CategoriaPublicacionSerializer(serializers.ModelSerializer):
  class Meta:
    model = CategoriaPublicacion
    fields ='__all__'


class PublicacionBancoSerializer(serializers.ModelSerializer):
  class Meta:
    model = PublicacionBanco
    fields ='__all__'

  
class UsuarioSerializer(serializers.ModelSerializer):
  class Meta:
    model = Usuario
    fields ='__all__'


class ComentarioSerializer(serializers.ModelSerializer):
  class Meta:
    model = Comentario
    fields ='__all__'



class NumeroTelefonoSerializer(serializers.ModelSerializer):
  class Meta:
    model = NumeroTelefono
    fields ='__all__'


class CuentaBancariaSerializer(serializers.ModelSerializer):
  class Meta:
    model = CuentaBancaria
    fields ='__all__'


class PrestamoSerializer(serializers.ModelSerializer):
  class Meta:
    model = Prestamo
    fields ='__all__'


class OperacionSerializer(serializers.ModelSerializer):
  class Meta:
    model = Operacion
    fields ='__all__'


class TipoPromocionSerializer(serializers.ModelSerializer):
  class Meta:
    model = TipoPromocion
    fields ='__all__'


class PromocionDisponibleUsuarioSerializer(serializers.ModelSerializer):
  class Meta:
    model = PromocionDisponibleUsuario
    fields ='__all__'