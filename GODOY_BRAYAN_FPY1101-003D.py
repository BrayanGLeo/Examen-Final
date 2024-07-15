from os import system
import random
system("cls")

#Link Github: https://github.com/BrayanGLeo/Examen-Final/blob/main/GODOY_BRAYAN_FPY1101-003D.py

trabajadores = [["Juan Pérez"],["María García"],["Carlos López"],["Ana Martínez"],["Pedro Rodríguez"],
                ["Laura Hernández"],["Miguel Sánchez"],["Isabel Gómez"],["Fransisco Díaz"],["Elena Fernández"]]

sueldos_menores_800=[]
sueldos_entre_800y2m=[]
sueldos_mayores_a_2m=[]

while True:
    print("""
    1. Asignar sueldos aleatorios
    2. Clasificar sueldos
    3. Ver etadísticas
    4. Reporte de sueldos
    5. Salir del programa
    """)
    op=input("Ingrese la opcion que desee: ")
    match op:
        case "1":
            for i in range(10):
                sueldo=random.randint(300000,2500000)
                trabajadores[i].append(sueldo)

            print("Sueldos creados con exito")
            input("Pulse enter para continuar......")
            system("cls")
        case "2":
            for r in range(10):
                if trabajadores[r][1] < 800000:
                    sueldos_menores_800.append(trabajadores[r])
                elif trabajadores[r][1] > 800000 and trabajadores[r][1] < 2000000:
                    sueldos_entre_800y2m.append(trabajadores[r])
                elif trabajadores[r][1] > 2000000:
                    sueldos_mayores_a_2m.append(trabajadores[r])

            sme=len(sueldos_menores_800)
            se=len(sueldos_entre_800y2m)
            sma=len(sueldos_mayores_a_2m)

            sueldomenores=0
            sueldoentre=0
            sueldosmayores=0

            for sueldo in sueldos_menores_800:
                sueldomenores+=sueldo[1]
            for sueldo in sueldos_entre_800y2m:
                sueldoentre+=sueldo[1]
            for sueldo in sueldos_mayores_a_2m:
                sueldosmayores+=sueldo[1] 

            print(f"""
Sueldos menores a $800.000 TOTAL:{sme}
Nombre Empleado          Sueldo
                """)
            for sueldo in sueldos_menores_800:
                print(f"{sueldo[0]}            ${sueldo[1]}")
            print(f"""
Sueldos entre $800.000 y $2.000.000 TOTAL:{se}
Nombre Empleado          Sueldo
                """)
            for sueldo in sueldos_entre_800y2m:
                print(f"{sueldo[0]}            ${sueldo[1]}")
            print(f"""
Sueldos mayores a $2.000.000 TOTAL:{sma}
Nombre Empleado          Sueldo
                """)
            for sueldo in sueldos_mayores_a_2m:
                print(f"{sueldo[0]}            ${sueldo[1]}")

            print(f"TOTAL SUELDOS: ${sueldomenores+sueldoentre+sueldosmayores}")
            input("Pulse enter para continuar......")
            system("cls")
        case "3":
            break
        case "4":
            break
        case "5":
            break
        case other:
            print("Opcion no existe!!!")
            input("Pulse enter para continuar......")
        

