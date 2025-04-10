def check_vowels():
        # Código a implementar utilizando input.
	nombre = input(("Ingresa tu nombre: ").lower())
	
	print("Contiene a:", "a" in nombre or "A" in nombre)
	print("Contiene e:", "e" in nombre or "E" in nombre)
	print("Contiene i:", "i" in nombre or "I" in nombre)
	print("Contiene o:", "o" in nombre or "O" in nombre)
	print("Contiene u:", "u" in nombre or "U" in nombre)


 def slice_simple():
    texto = "Awesome".lower()

    print (texto[0:3])
    print (texto[2:5])
    print (texto[0:4]+texto[4:7])
