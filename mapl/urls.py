from django.urls import path 
# from .views import OperadorasView, MonedasView, PaisesView
from .views import *



urlpatterns = [
  path('operadoras',OperadorasView.as_view()),
  path('updateoperadoras/<int:pk>',UpdateOperadorasView.as_view()),
  path('deleteoperadoras/<int:pk>',DeleteOperadorasView.as_view()),
  path('retrieveoperadoras/<int:pk>',RetrieveOperadorasView.as_view()),

  path('monedas',MonedasView.as_view()),
  path('updatemonedas/<int:pk>',UpdateMonedasView.as_view()),
  path('deletemonedas/<int:pk>',DeleteMonedasView.as_view()),
  path('retrievemonedas/<int:pk>',RetrieveMonedasView.as_view()),

  path('paises',PaisesView.as_view()),
  path('updatepaises/<int:pk>',UpdatePaisesView.as_view()),
  path('deletepaises/<int:pk>',DeletePaisesView.as_view()),
  path('retrievepaises/<int:pk>',RetrievePaisesView.as_view()),


  path('ciudades',CiudadesView.as_view()),
  path('updateciudades/<int:pk>',UpdateCiudadesView.as_view()),
  path('deleteciudades/<int:pk>',DeleteCiudadesView.as_view()),
  path('retrieveciudades/<int:pk>',RetrieveCiudadesView.as_view()),


  path('roles',RolesView.as_view()),
  path('updateroles/<int:pk>',UpdateRolesView.as_view()),
  path('deleteroles/<int:pk>',DeleteRolesView.as_view()),
  path('retrieveroles/<int:pk>',RetrieveRolesView.as_view()),


  path('tiposoperaciones',TiposOperacionesView.as_view()),
  path('updatetiposoperaciones/<int:pk>',UpdateTiposOperacionesView.as_view()),
  path('deletetiposoperaciones/<int:pk>',DeleteTiposOperacionesView.as_view()),
  path('retrievetiposoperaciones/<int:pk>',RetrieveTiposOperacionesView.as_view()),


  path('categoriasusuarios',CategoriasUsuariosView.as_view()),
  path('updatecategoriasusuarios/<int:pk>',UpdateCategoriasUsuariosView.as_view()),
  path('deletecategoriasusuarios/<int:pk>',DeleteCategoriasUsuariosView.as_view()),
  path('retrievecategoriasusuarios/<int:pk>',RetrieveCategoriasUsuariosView.as_view()),


  path('tiposprestamos',TiposPrestamosView.as_view()),
  path('updatetiposprestamos/<int:pk>',UpdateTiposPrestamosView.as_view()),
  path('deletetiposprestamos/<int:pk>',DeleteTiposPrestamosView.as_view()),
  path('retrievetiposprestamos/<int:pk>',RetrieveTiposPrestamosView.as_view()),


  path('tiposintereses',TiposInteresesView.as_view()),
  path('updatetiposintereses/<int:pk>',UpdateTiposInteresesView.as_view()),
  path('deletetiposintereses/<int:pk>',DeleteTiposInteresesView.as_view()),
  path('retrievetiposintereses/<int:pk>',RetrieveTiposInteresesView.as_view()),


  path('agencias',AgenciasView.as_view()),
  path('updateagencias/<int:pk>',UpdateAgenciasView.as_view()),
  path('deleteagencias/<int:pk>',DeleteAgenciasView.as_view()),
  path('retrieveagencias/<int:pk>',RetrieveAgenciasView.as_view()),


  path('categoriaspublicaciones',CategoriasPublicacionesView.as_view()),
  path('updatecategoriaspublicaciones/<int:pk>',UpdateCategoriasPublicacionesView.as_view()),
  path('deletecategoriaspublicaciones/<int:pk>',DeleteCategoriasPublicacionesView.as_view()),
  path('retrievecategoriaspublicaciones/<int:pk>',RetrieveCategoriasPublicacionesView.as_view()),


  path('publicacionesbanco',PublicacionesBancoView.as_view()),
  path('updatepublicacionesbanco/<int:pk>',UpdatePublicacionesBancoView.as_view()),
  path('deletepublicacionesbanco/<int:pk>',DeletePublicacionesBancoView.as_view()),
  path('retrievepublicacionesbanco/<int:pk>',RetrievePublicacionesBancoView.as_view()),


  path('usuarios',UsuariosView.as_view()),
  path('updateusuarios/<int:pk>',UpdateUsuariosView.as_view()),
  path('deleteusuarios/<int:pk>',DeleteUsuariosView.as_view()),
  path('retrieveusuarios/<int:pk>',RetrieveUsuariosView.as_view()),


  path('comentarios',ComentariosView.as_view()),
  path('updatecomentarios/<int:pk>',UpdateComentariosView.as_view()),
  path('deletecomentarios/<int:pk>',DeleteComentariosView.as_view()),
  path('retrievecomentarios/<int:pk>',RetrieveComentariosView.as_view()),


  path('numerostelefonos',NumerosTelefonosView.as_view()),
  path('updatenumerostelefonos/<int:pk>',UpdateNumerosTelefonosView.as_view()),
  path('deletenumerostelefonos/<int:pk>',DeleteNumerosTelefonosView.as_view()),
  path('retrievenumerostelefonos/<int:pk>',RetrieveNumerosTelefonosView.as_view()),


  path('cuentasbancarias',CuentasBancariasView.as_view()),
  path('updatecuentasbancarias/<int:pk>',UpdateCuentasBancariasView.as_view()),
  path('deletecuentasbancarias/<int:pk>',DeleteCuentasBancariasView.as_view()),
  path('retrievecuentasbancarias/<int:pk>',RetrieveCuentasBancariasView.as_view()),


  path('prestamos',PrestamosView.as_view()),
  path('updateprestamos/<int:pk>',UpdatePrestamosView.as_view()),
  path('deleteprestamos/<int:pk>',DeletePrestamosView.as_view()),
  path('retrieveprestamos/<int:pk>',RetrievePrestamosView.as_view()),


  path('operaciones',OperacionesView.as_view()),
  path('updateoperaciones/<int:pk>',UpdateOperacionesView.as_view()),
  path('deleteoperaciones/<int:pk>',DeleteOperacionesView.as_view()),
  path('retrieveoperaciones/<int:pk>',RetrieveOperacionesView.as_view()),


  path('tipospromociones',TiposPromocionesView.as_view()),
  path('updatetipospromociones/<int:pk>',UpdateTiposPromocionesView.as_view()),
  path('deletetipospromociones/<int:pk>',DeleteTiposPromocionesView.as_view()),
  path('retrievetipospromociones/<int:pk>',RetrieveTiposPromocionesView.as_view()),


  path('promocionesdisponiblesusuarios',PromocionesDisponiblesUsuariosView.as_view()),
  path('updatepromocionesdisponiblesusuarios/<int:pk>',UpdatePromocionesDisponiblesUsuariosView.as_view()),
  path('deletepromocionesdisponiblesusuarios/<int:pk>',DeletePromocionesDisponiblesUsuariosView.as_view()),
  path('retrievepromocionesdisponiblesusuarios/<int:pk>',RetrievePromocionesDisponiblesUsuariosView.as_view()),


]
