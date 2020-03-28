import re
patron=re.compile("^[A-Z](\d){3}[a-z]{3}[^\w]{3}$")
cadena=input(" Ingrese la contraseña: ");
m=patron.match(cadena)
if m!=None:
   print(f"la contraseña {cadena} es valida")
else:
    print(f"la contraseña {cadena} NO es valida") 
