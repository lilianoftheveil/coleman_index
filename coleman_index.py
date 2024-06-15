# -*- coding: utf-8 -*-

def col(x):
    w = 1                                                   # Number of words
    for a in x:
        if a == " ":
            w = w + 1
    s = 0                                                   # Number of sentences
    for b in x:
        if b == "." or b == "!" or b == "?" or b == "...":
            s = s + 1
    l = 0                                                   # Number of letters
    for c in x:        # PYTHON Documentation (Utilities for ASCII characters - that check all letters lower and upper -)
        if c.isalpha():
            l = l + 1
    cl = (l / w * 100)
    cs = (s / w * 100)
    calcu = round((0.0588 * cl) - (0.296 * cs) - 15.8)      # Coleman-Liau index
    if calcu < 1:                                           # Print of the Before Grade 1
        print("Índice de Legibilidade: Pré-escolar")
    if calcu == 1 or calcu > 1 and calcu <= 16:             # Print of the Grade 1
        print(f"Índice de Legibilidade: {calcu}")                                        
    if calcu > 16:                                          # Print of the Grade more than 16
        print("Índice de Legibilidade: 16+")

    return((f"Número de Palavras: {w}"), (f"Número de Setenças: {s}"), (f"Número de Letras: {l}"))


while True:
    x = input("digite 'c' para escrever um texto ou 't' para abrir arquivo .txt: ").lower()
    if x == "t":
        y = input("caminho: ")  
        z = open(y).read()
        print(col(z))
        break
    elif x == "c":
        y = input("texto: ")    
        print(col(y))
        break
    else:
        print("entrada inválida.")
        continue