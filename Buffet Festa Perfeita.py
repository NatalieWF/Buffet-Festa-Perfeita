# Questão do Buffet Festa Perfeita.
convidados = int(input("Quantidade de convidados (mínimo cinquenta): "))

if convidados < (50):
   resultado("Quantidade recomendada são de no mínimo 50 pessoas!")

else:
   carne = 0.300
   refrigerante = 3
   doce = 1
   total_de_carne = float(carne + carne * 6/100) * convidados, "Kg"



   print("Quantidade de carnes:", total_de_carne)
   print("Quantidade de latas de refrigerante:", (refrigerante + 9) * convidados)
   print("Quantidade de doces:", doce * convidados)