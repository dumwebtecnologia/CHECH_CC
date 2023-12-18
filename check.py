def check_cc(number):
  # Converte a string em uma lista de inteiros
  digits = [int(d) for d in number]
  # Inverte a lista
  digits.reverse()
  # Multiplica os dígitos das posições ímpares por 2
  doubled = [d * 2 if i % 2 == 1 else d for i, d in enumerate(digits)]
  # Subtrai 9 dos dígitos que são maiores que 9
  subtracted = [d - 9 if d > 9 else d for d in doubled]
  # Soma todos os dígitos
  total = sum(subtracted)
  # Verifica se a soma é divisível por 10
  return total % 10 == 0