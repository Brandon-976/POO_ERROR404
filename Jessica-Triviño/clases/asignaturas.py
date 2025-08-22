asignaturas = {
    "POO1": 'A11',
    "REDES1" : 'B12',
    "DATOS": 'C13',
    "OPERATIVOS": 'D14',
    "COMPILADORES": 'E15',

}
print("escribe la asignatura")
subj= str(input())
if subj in asignaturas:
    print(f"la asignatura{subj} su codigo es{asignaturas[subj ]}")
    

