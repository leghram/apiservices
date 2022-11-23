from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, UpdateAPIView, DestroyAPIView, RetrieveAPIView
# from .serializers import OperadoraSerializer, MonedaSerializer, PaisSerializer, CiudadSerializer
from .serializers import *

# from .models import Operadora, Moneda, Pais, Ciudad
from .models import *

#
class OperadorasView(ListCreateAPIView):
  queryset = Operadora.objects.all()
  serializer_class = OperadoraSerializer

  def get(self, request):
    lista_operadoras = self.get_queryset()
    lista_serializada = self.serializer_class(lista_operadoras, many= True)
    return Response(data={
      'mensaje':'las tareas son',
      'content':lista_serializada.data
    }, status=200)

  def post(self, request):
    body = request.data
    instancia_serializador = self.serializer_class(data=body)
    validacion =instancia_serializador.is_valid(raise_exception=True)

    if validacion:
      instancia_serializador.save()
      return Response(data=instancia_serializador.data , status=201)


class UpdateOperadorasView(UpdateAPIView):
  queryset = Operadora.objects.all()
  serializer_class = OperadoraSerializer

class DeleteOperadorasView(DestroyAPIView):
  queryset = Operadora.objects.all()
  serializer_class = OperadoraSerializer

class RetrieveOperadorasView(RetrieveAPIView):
  queryset = Operadora.objects.all()
  serializer_class = OperadoraSerializer
#




#PRUEBAS CON MONEDAS PARA DELETE Y UPDATE
class MonedasView(ListCreateAPIView):
  queryset = Moneda.objects.all()
  serializer_class = MonedaSerializer

## LA CLASE DE ARRIBA SI VALE, ESTAS DOS DE ABAJO SON PRUEBAS  

class UpdateMonedasView(UpdateAPIView):
  queryset = Moneda.objects.all()
  serializer_class = MonedaSerializer

class DeleteMonedasView(DestroyAPIView):
  queryset = Moneda.objects.all()
  serializer_class = MonedaSerializer

class RetrieveMonedasView(RetrieveAPIView):
  queryset = Moneda.objects.all()
  serializer_class = MonedaSerializer


#
class PaisesView(ListCreateAPIView):
  queryset = Pais.objects.all()
  serializer_class = PaisSerializer

class UpdatePaisesView(UpdateAPIView):
  queryset = Pais.objects.all()
  serializer_class = PaisSerializer

class DeletePaisesView(DestroyAPIView):
  queryset = Pais.objects.all()
  serializer_class = PaisSerializer

class RetrievePaisesView(RetrieveAPIView):
  queryset = Pais.objects.all()
  serializer_class = PaisSerializer
#



#
class CiudadesView(ListCreateAPIView):
  queryset = Ciudad.objects.all()
  serializer_class = CiudadSerializer

class UpdateCiudadesView(UpdateAPIView):
  queryset = Ciudad.objects.all()
  serializer_class = CiudadSerializer

class DeleteCiudadesView(DestroyAPIView):
  queryset = Ciudad.objects.all()
  serializer_class = CiudadSerializer
class RetrieveCiudadesView(RetrieveAPIView):
  queryset = Ciudad.objects.all()
  serializer_class = CiudadSerializer
#



#
class RolesView(ListCreateAPIView):
  queryset = Rol.objects.all()
  serializer_class = RolSerializer

class UpdateRolesView(UpdateAPIView):
  queryset = Rol.objects.all()
  serializer_class = RolSerializer

class DeleteRolesView(DestroyAPIView):
  queryset = Rol.objects.all()
  serializer_class = RolSerializer

class RetrieveRolesView(RetrieveAPIView):
  queryset = Rol.objects.all()
  serializer_class = RolSerializer
#


#
class TiposOperacionesView(ListCreateAPIView):
  queryset = TipoOperacion.objects.all()
  serializer_class = TipoOperacionSerializer

class UpdateTiposOperacionesView(UpdateAPIView):
  queryset = TipoOperacion.objects.all()
  serializer_class = TipoOperacionSerializer

class DeleteTiposOperacionesView(DestroyAPIView):
  queryset = TipoOperacion.objects.all()
  serializer_class = TipoOperacionSerializer
  
class RetrieveTiposOperacionesView(RetrieveAPIView):
  queryset = TipoOperacion.objects.all()
  serializer_class = TipoOperacionSerializer
#


#
class CategoriasUsuariosView(ListCreateAPIView):
  queryset = CategoriaUsuario.objects.all()
  serializer_class = CategoriaUsuarioSerializer

class UpdateCategoriasUsuariosView(UpdateAPIView):
  queryset = CategoriaUsuario.objects.all()
  serializer_class = CategoriaUsuarioSerializer

class DeleteCategoriasUsuariosView(DestroyAPIView):
  queryset = CategoriaUsuario.objects.all()
  serializer_class = CategoriaUsuarioSerializer

class RetrieveCategoriasUsuariosView(RetrieveAPIView):
  queryset = CategoriaUsuario.objects.all()
  serializer_class = CategoriaUsuarioSerializer
#


#
class TiposPrestamosView(ListCreateAPIView):
  queryset = TipoPrestamo.objects.all()
  serializer_class = TipoPrestamoSerializer

class UpdateTiposPrestamosView(UpdateAPIView):
  queryset = TipoPrestamo.objects.all()
  serializer_class = TipoPrestamoSerializer

class DeleteTiposPrestamosView(DestroyAPIView):
  queryset = TipoPrestamo.objects.all()
  serializer_class = TipoPrestamoSerializer

class RetrieveTiposPrestamosView(RetrieveAPIView):
  queryset = TipoPrestamo.objects.all()
  serializer_class = TipoPrestamoSerializer
#


#
class TiposInteresesView(ListCreateAPIView):
  queryset = TipoInteres.objects.all()
  serializer_class = TipoInteresSerializer

class UpdateTiposInteresesView(UpdateAPIView):
  queryset = TipoInteres.objects.all()
  serializer_class = TipoInteresSerializer

class DeleteTiposInteresesView(DestroyAPIView):
  queryset = TipoInteres.objects.all()
  serializer_class = TipoInteresSerializer

class RetrieveTiposInteresesView(RetrieveAPIView):
  queryset = TipoInteres.objects.all()
  serializer_class = TipoInteresSerializer
#


#
class AgenciasView(ListCreateAPIView):
  queryset = Agencia.objects.all()
  serializer_class = AgenciaSerializer

class UpdateAgenciasView(UpdateAPIView):
  queryset = Agencia.objects.all()
  serializer_class = AgenciaSerializer

class DeleteAgenciasView(DestroyAPIView):
  queryset = Agencia.objects.all()
  serializer_class = AgenciaSerializer

class RetrieveAgenciasView(RetrieveAPIView):
  queryset = Agencia.objects.all()
  serializer_class = AgenciaSerializer
#


#
class CategoriasPublicacionesView(ListCreateAPIView):
  queryset = CategoriaPublicacion.objects.all()
  serializer_class = CategoriaPublicacionSerializer

class UpdateCategoriasPublicacionesView(UpdateAPIView):
  queryset = CategoriaPublicacion.objects.all()
  serializer_class = CategoriaPublicacionSerializer

class DeleteCategoriasPublicacionesView(DestroyAPIView):
  queryset = CategoriaPublicacion.objects.all()
  serializer_class = CategoriaPublicacionSerializer

class RetrieveCategoriasPublicacionesView(RetrieveAPIView):
  queryset = CategoriaPublicacion.objects.all()
  serializer_class = CategoriaPublicacionSerializer
#


#
class PublicacionesBancoView(ListCreateAPIView):
  queryset = PublicacionBanco.objects.all()
  serializer_class = PublicacionBancoSerializer

class UpdatePublicacionesBancoView(UpdateAPIView):
  queryset = PublicacionBanco.objects.all()
  serializer_class = PublicacionBancoSerializer

class DeletePublicacionesBancoView(DestroyAPIView):
  queryset = PublicacionBanco.objects.all()
  serializer_class = PublicacionBancoSerializer

class RetrievePublicacionesBancoView(RetrieveAPIView):
  queryset = PublicacionBanco.objects.all()
  serializer_class = PublicacionBancoSerializer
#


#
class UsuariosView(ListCreateAPIView):
  queryset = Usuario.objects.all()
  serializer_class = UsuarioSerializer

class UpdateUsuariosView(UpdateAPIView):
  queryset = Usuario.objects.all()
  serializer_class = UsuarioSerializer

class DeleteUsuariosView(DestroyAPIView):
  queryset = Usuario.objects.all()
  serializer_class = UsuarioSerializer

class RetrieveUsuariosView(RetrieveAPIView):
  queryset = Usuario.objects.all()
  serializer_class = UsuarioSerializer
#


#
class ComentariosView(ListCreateAPIView):
  queryset = Comentario.objects.all()
  serializer_class = ComentarioSerializer

class UpdateComentariosView(UpdateAPIView):
  queryset = Comentario.objects.all()
  serializer_class = ComentarioSerializer

class DeleteComentariosView(DestroyAPIView):
  queryset = Comentario.objects.all()
  serializer_class = ComentarioSerializer

class RetrieveComentariosView(RetrieveAPIView):
  queryset = Comentario.objects.all()
  serializer_class = ComentarioSerializer
#



#
class NumerosTelefonosView(ListCreateAPIView):
  queryset = NumeroTelefono.objects.all()
  serializer_class = NumeroTelefonoSerializer

class UpdateNumerosTelefonosView(UpdateAPIView):
  queryset = NumeroTelefono.objects.all()
  serializer_class = NumeroTelefonoSerializer

class DeleteNumerosTelefonosView(DestroyAPIView):
  queryset = NumeroTelefono.objects.all()
  serializer_class = NumeroTelefonoSerializer

class RetrieveNumerosTelefonosView(RetrieveAPIView):
  queryset = NumeroTelefono.objects.all()
  serializer_class = NumeroTelefonoSerializer
#


#
class CuentasBancariasView(ListCreateAPIView):
  queryset = CuentaBancaria.objects.all()
  serializer_class = CuentaBancariaSerializer

class UpdateCuentasBancariasView(UpdateAPIView):
  queryset = CuentaBancaria.objects.all()
  serializer_class = CuentaBancariaSerializer

class DeleteCuentasBancariasView(DestroyAPIView):
  queryset = CuentaBancaria.objects.all()
  serializer_class = CuentaBancariaSerializer

class RetrieveCuentasBancariasView(RetrieveAPIView):
  queryset = CuentaBancaria.objects.all()
  serializer_class = CuentaBancariaSerializer
#


#
class PrestamosView(ListCreateAPIView):
  queryset = Prestamo.objects.all()
  serializer_class = PrestamoSerializer

class UpdatePrestamosView(UpdateAPIView):
  queryset = Prestamo.objects.all()
  serializer_class = PrestamoSerializer

class DeletePrestamosView(DestroyAPIView):
  queryset = Prestamo.objects.all()
  serializer_class = PrestamoSerializer

class RetrievePrestamosView(RetrieveAPIView):
  queryset = Prestamo.objects.all()
  serializer_class = PrestamoSerializer
#


#
class OperacionesView(ListCreateAPIView):
  queryset = Operacion.objects.all()
  serializer_class = OperacionSerializer

class UpdateOperacionesView(UpdateAPIView):
  queryset = Operacion.objects.all()
  serializer_class = OperacionSerializer

class DeleteOperacionesView(DestroyAPIView):
  queryset = Operacion.objects.all()
  serializer_class = OperacionSerializer

class RetrieveOperacionesView(RetrieveAPIView):
  queryset = Operacion.objects.all()
  serializer_class = OperacionSerializer
#


#
class TiposPromocionesView(ListCreateAPIView):
  queryset = TipoPromocion.objects.all()
  serializer_class = TipoPromocionSerializer

class UpdateTiposPromocionesView(UpdateAPIView):
  queryset = TipoPromocion.objects.all()
  serializer_class = TipoPromocionSerializer

class DeleteTiposPromocionesView(DestroyAPIView):
  queryset = TipoPromocion.objects.all()
  serializer_class = TipoPromocionSerializer

class RetrieveTiposPromocionesView(RetrieveAPIView):
  queryset = TipoPromocion.objects.all()
  serializer_class = TipoPromocionSerializer
#



#
class PromocionesDisponiblesUsuariosView(ListCreateAPIView):
  queryset = PromocionDisponibleUsuario.objects.all()
  serializer_class = PromocionDisponibleUsuarioSerializer

class UpdatePromocionesDisponiblesUsuariosView(UpdateAPIView):
  queryset = PromocionDisponibleUsuario.objects.all()
  serializer_class = PromocionDisponibleUsuarioSerializer

class DeletePromocionesDisponiblesUsuariosView(DestroyAPIView):
  queryset = PromocionDisponibleUsuario.objects.all()
  serializer_class = PromocionDisponibleUsuarioSerializer

class RetrievePromocionesDisponiblesUsuariosView(RetrieveAPIView):
  queryset = PromocionDisponibleUsuario.objects.all()
  serializer_class = PromocionDisponibleUsuarioSerializer
#  