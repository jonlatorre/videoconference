# -*- coding: utf-8 -*-

#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.template import defaultfilters #para el slug
import hashlib

# Create your models here.

class Sala(models.Model):
    nombre = models.CharField(_('Nombre de la sala (25 carácteres).'),max_length=25,blank=True)
    slug = models.SlugField()
    participante_1_nombre = models.CharField(max_length=25,blank=False)
    participante_2_nombre = models.CharField(max_length=25,blank=False)
    participante_3_nombre = models.CharField(max_length=25,blank=True)
    participante_4_nombre = models.CharField(max_length=25,blank=True)
    participante_5_nombre = models.CharField(max_length=25,blank=True)
    participante_6_nombre = models.CharField(max_length=25,blank=True)
    participante_7_nombre = models.CharField(max_length=25,blank=True)
    participante_8_nombre = models.CharField(max_length=25,blank=True)
    participante_9_nombre = models.CharField(max_length=25,blank=True)
    participante_10_nombre = models.CharField(max_length=25,blank=True)
    participante_1_hash = models.CharField(max_length=25,blank=True)
    participante_2_hash = models.CharField(max_length=25,blank=True)
    participante_3_hash = models.CharField(max_length=25,blank=True)
    participante_4_hash = models.CharField(max_length=25,blank=True)
    participante_5_hash = models.CharField(max_length=25,blank=True)
    participante_6_hash = models.CharField(max_length=25,blank=True)
    participante_7_hash = models.CharField(max_length=25,blank=True)
    participante_8_hash = models.CharField(max_length=25,blank=True)
    participante_9_hash = models.CharField(max_length=25,blank=True)
    participante_10_hash = models.CharField(max_length=25,blank=True)
    
    def save(self, *args, **kwargs):
        self.slug = defaultfilters.slugify(self.nombre)
        self.generar_hashes()
        super(Sala, self).save(*args, **kwargs)
        
    def generar_hashes(self):
        for num in range(1,11):
            nombre = getattr(self, "participante_%d_nombre"%num)
            if len(nombre) > 0 :
                h = hashlib.sha1(nombre)
                h = h.hexdigest()
                print "Generado hash %s para %s"%(h,nombre)
                setattr(self,"participante_%d_hash"%num,h)
    def comprobar_hash(self,h):
        """Comprobamos si el hash está en la lista y el participante puede entrar (devolvemos true)"""
        for num in range(1,11):
            clave = getattr(self, "participante_%d_hash"%num)
            print "Comparando %s con %s"%(h,clave)
            if h == clave:
                print "Hemos encontrado el hash!!"
                return True
        return False
