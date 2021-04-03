censor = input()
frase = input()
if censor in frase:
    frase = frase.replace(censor, '*'*len(censor))
print(frase)