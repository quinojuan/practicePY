factura = int(input("Cual es el total de la factura: "))
personas = int(input("Cuantos comenzales son: "))
cuanta_propina = int(input("Cuánta propina quiere dejar 1 (18%), 2 (20%), 3 (25%): "))

if cuanta_propina == 1:
  propina_total = round(factura * 0.18)
elif cuanta_propina == 2:
  propina_total = round(factura * 0.20)
elif cuanta_propina == 3:
  propina_total = round(factura * 0.25)
else:
  print("Asumimos que no deja propina") 
  propina_total = 0
  
factura_con_propina = round(factura + propina_total)
costo_factura_por_persona = round(factura / personas)
propina_por_persona = round(propina_total / personas)
costo_final_por_persona = round(costo_factura_por_persona + propina_por_persona)

choice = int(input("Quiere ser generoso y pagar el 70'%' usted?: 1(SI) 2(NO)"))

if choice == 1:
  print(f'''\nResumen de persona generosa:
      Factura: ${factura}
      Cantidad de personas: {personas}
      Propina total: ${propina_total}
      Factura con propina: ${factura_con_propina}
      Quien invita el 70%: ${factura * 0.7}
      Invitado: ${factura * 0.3}
      Propina que pone quien invita: ${propina_total * 0.7}
      Propina que pone el invitado ${propina_total * 0.3}
      
      Anfitrion: $ {(factura * 0.7) + (propina_total * 0.7)}
      Invitado: $ {(factura * 0.3) + (propina_total * 0.3)}
      ''')
else:
  print(f'''\nResumen:
      Factura: ${factura}
      Cantidad de personas: {personas}
      Propina total: ${propina_total}
      Factura con propina: ${factura_con_propina}
      Costo por persona sin propina: ${costo_factura_por_persona}
      Propina por persona: ${propina_por_persona}
      
      Cada individuo paga: $ {costo_final_por_persona}
      ''')