from django.views.generic.simple import direct_to_template

def vista_sala(request,sala,clave):
	print "El usuario quiere ver la sala:",sala
	print "Y nos ha pasado la pass:",clave
	return direct_to_template(request,template = "salas/sala.html",extra_context={"sala": sala, "clave": clave})
