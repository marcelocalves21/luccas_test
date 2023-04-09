new_func= 'Marcelo'
edit = 3
# f = open(f"{new_func}.txt", "x")
f = open(f"{new_func}.txt", "a")
f.write(f"\n########## Marcelo {edit} edicao #############\n")
f.close()

#open and read the file after the appending:
f = open("Marcelo.txt","r")
print(f.read())