# -*- coding: UTF-8 -*-
class Perfil_Vip(Perfil):
   'Classe padrão para perfis de usuários VIPs'
   def obter_creditos(self):
      return self.__curtidas * 10.0
