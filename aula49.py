# INTRODUÇÃO AO DESEMPACOTAMENTO


nome1, nome2, nome3 = ["Nala", "Pablo", "Katy"]; # desempacotamento da lista
print(nome2)

_, _, nome, *_ = ["Nala", "Pablo", "Katy"]; # desempacotamento da lista ignorando os dois primeiros elementos
print(nome)