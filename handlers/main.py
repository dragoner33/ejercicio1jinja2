#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
from webapp2_extras import jinja2
from datetime import datetime

class MainHandler(webapp2.RequestHandler):
    def post(self):
        fecha = datetime.now()

        CIF = self.request.get("cif", "Desconocido")
        nombre = self.request.get("nombre", "Desconocido")
        direccion = self.request.get("direccion", "Desconocido")
        poblacion = self.request.get("poblacion", "Desconocido")
        provincia = self.request.get("provincia", "Desconocido")
        codigopostal = self.request.get("codigopostal", "Desconocido")
        pais = self.request.get("pais", "Desconocido")
        personadecontacto = self.request.get("personadecontacto", "Desconocido")
        email = self.request.get("email", "Desconocido")
        telefono = self.request.get("telefono", "Desconocido")

        CIFcl = self.request.get("cifcl", "Desconocido")
        nombrecl = self.request.get("nombrecl", "Desconocido")
        direccioncl = self.request.get("direccioncl", "Desconocido")
        poblacioncl = self.request.get("poblacioncl", "Desconocido")
        provinciacl = self.request.get("provinciacl", "Desconocido")
        codigopostalcl = self.request.get("codigopostalcl", "Desconocido")
        paiscl = self.request.get("paiscl", "Desconocido")
        personadecontactocl = self.request.get("personadecontactocl", "Desconocido")
        emailcl = self.request.get("emailcl", "Desconocido")
        telefonocl = self.request.get("telefonocl", "Desconocido")

        concepto = self.request.get("concepto", "Desconocido")
        precio = self.request.get("precio", "Desconocido")
        unidades = self.request.get("unidades", "Desconocido")
        importebruto = self.request.get("importebruto", "Desconocido")
        iva = self.request.get("iva", "Desconocido")
        importetot = self.request.get("importetot", "Desconocido")

        jinja = jinja2.get_jinja2(app=self.app)

        valores_plantilla = {"CIF_fac": CIF, "nombre_fac": nombre, "direccion_fac": direccion, "poblacion_fac": poblacion, "provincia_fac": provincia,
                             "codigopostal_fac": codigopostal,"pais_fac": pais, "personadecontacto_fac": personadecontacto,
                             "email_fac": email, "telefono_fac": telefono, "CIF_faccl": CIFcl, "nombre_faccl": nombrecl, "direccion_faccl": direccioncl,
                             "poblacion_faccl": poblacioncl, "provincia_faccl": provinciacl,"codigopostal_faccl": codigopostalcl,"pais_faccl": paiscl,
                             "personadecontacto_faccl": personadecontactocl, "email_faccl": emailcl, "telefono_faccl": telefonocl, "concepto_fac":concepto,
                             "precio_fac": precio, "unidades_fac": unidades, "importebruto_fac": importebruto, "iva_fac": iva, "importetot_fac": importetot,
                             "fecha_fac": fecha}

        self.response.write(jinja.render_template("factura.html", **valores_plantilla))


        if len(CIF.strip()) == 0:
           CIF = "Desconocida"
        if len(nombre.strip()) == 0:
            nombre = "Desconocido"
        if len(direccion.strip()) == 0:
            direccion = "Desconocido"
        if len(poblacion.strip()) == 0:
           poblacion = "Desconocido"
        if len(provincia.strip()) == 0:
            provincia = "Desconocido"
        if len(codigopostal.strip()) == 0:
            codigopostal = "Desconocido"
        if len(pais.strip()) == 0:
            pais = "Desconocido"
        if len(personadecontacto.strip()) == 0:
           personadecontacto = "Desconocido"
        if len(email.strip()) == 0:
            email = "Desconocido"
        if len(telefono.strip()) == 0:
            telefono = "Desconocido"
        if len(CIFcl.strip()) == 0:
           CIFcl = "Desconocida"
        if len(nombrecl.strip()) == 0:
            nombrecl = "Desconocido"
        if len(direccioncl.strip()) == 0:
            direccioncl = "Desconocido"
        if len(poblacioncl.strip()) == 0:
           poblacioncl = "Desconocido"
        if len(provinciacl.strip()) == 0:
            provinciacl = "Desconocido"
        if len(codigopostalcl.strip()) == 0:
            codigopostalcl = "Desconocido"
        if len(paiscl.strip()) == 0:
            paiscl = "Desconocido"
        if len(personadecontactocl.strip()) == 0:
           personadecontactocl = "Desconocido"
        if len(emailcl.strip()) == 0:
            emailcl = "Desconocido"
        if len(telefonocl.strip()) == 0:
            telefonocl = "Desconocido"
        if len(concepto.strip()) == 0:
            concepto = "Desconocido"
        if len(precio.strip()) == 0:
            precio = "Desconocido"
        if len(unidades.strip()) == 0:
            unidades = "Desconocido"
        if len(importebruto.strip()) == 0:
           importebruto = "Desconocido"
        if len(iva.strip()) == 0:
            iva = "Desconocido"
        if len(importetot.strip()) == 0:
            importetot = "Desconocido"




app = webapp2.WSGIApplication([
    ('/factura', MainHandler)
], debug=True)
