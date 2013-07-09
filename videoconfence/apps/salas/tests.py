"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase


class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)

class Salastest(TestCase):
	from models import Sala
	s = Sala()
	s.nombre = "Una sala de prueba"
	s.participante_1_nombre = 'Pedrito1'
	s.participante_2_nombre = 'Pedrito2'
	s.participante_3_nombre = 'Pedrito3'
	s.participante_4_nombre = 'Pedrito4'
	s.participante_5_nombre = 'Pedrito5'
	s.participante_6_nombre = 'Pedrito6'
	s.participante_7_nombre = 'Pedrito7'
	s.participante_8_nombre = 'Pedrito8'
	s.participante_9_nombre = 'Pedrito9'
	s.participante_10_nombre = 'Pedrito10'
	s.save()
	print "El slug es... ",s.slug
	#print "leemos el ultimo hash"
	texto = 'ffb8f020ce392b3bba038db7e751042c5d90bfeb'
	print "preguntamos por el"
	s.comprobar_hash(texto)
	s.delete()
	
