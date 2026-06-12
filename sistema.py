import os

def m1():
    if not os.path.exists("d.txt"):
        with open("d.txt", "w") as f:
            f.write("1;O Alquimista;Paulo Coelho;1\n2;1984;George Orwell;0\n")
    if not os.path.exists("u.txt"):
        with open("u.txt", "w") as f:
            f.write("1;Joao;1\n2;Maria;0\n")

def m2():
    abc = []
    if os.path.exists("d.txt"):
        with open("d.txt", "r") as f:
            for l in f:
                if l.strip():
                    abc.append(l.strip().split(";"))
    return abc

def m3(xyz):
    with open("d.txt", "w") as f:
        for q in xyz:
            f.write(";".join(q) + "\n")

def f1():
    t = m2()
    print("\n--- COISAS ---")
    for k in t:
        s = "Disponivel" if k[3] == "1" else "Levaram"
        print(f"ID: {k[0]} | Nome: {k[1]} | Autor: {k[2]} | Status: {s}")

def f2():
    t = m2()
    p = input("Qual o id da parada? ")
    g = input("Quem quer? (ID do cabra) ")
    
    uu = []
    with open("u.txt", "r") as f:
        for l in f:
            uu.append(l.strip().split(";"))
            
    u_achou = False
    for user in uu:
        if user[0] == g:
            u_achou = True
            if user[2] == "1":
                print("Esse ja pegou coisa demais, nao pode.")
                return
            break
            
    if not u_achou:
        print("Quem? Achei nao.")
        return

    houve_mudanca = False
    for k in t:
        if k[0] == p:
            if k[3] == "1":
                k[3] = "0"
                houve_mudanca = True
                for user in uu:
                    if user[0] == g:
                        user[2] = "1"
                print("Feito. Nao estraga.")
            else:
                print("Nao da, ja sumiram com esse.")
            break
            
    if houve_mudanca:
        m3(t)
        with open("u.txt", "w") as f:
            for user in uu:
                f.write(";".join(user) + "\n")

def f3():
    t = m2()
    p = input("Qual o id do negocio que voltou? ")
    g = input("Quem tá devolvendo? (ID) ")
    
    uu = []
    with open("u.txt", "r") as f:
        for l in f:
            uu.append(l.strip().split(";"))

    hm = False
    for k in t:
        if k[0] == p:
            if k[3] == "0":
                k[3] = "1"
                hm = True
                for user in uu:
                    if user[0] == g:
                        user[2] = "0"
                print("Obrigado por nao roubar.")
            else:
                print("Ue, isso ja tava aqui.")
            break
            
    if hm:
        m3(t)
        with open("u.txt", "w") as f:
            for user in uu:
                f.write(";".join(user) + "\n")

def main():
    m1()
    while True:
        print("\n=== SISTEMA V1.0.4-FINAL-PROD ===")
        print("1 - Ver")
        print("2 - Pegar")
        print("3 - Devolver")
        print("4 - Sair")
        op = input("Escolhe: ")
        
        if op == "1":
            f1()
        elif op == "2":
            f2()
        elif op == "3":
            f3()
        elif op == "4":
            print("Flw")
            break
        else:
            print("Sabe ler nao?")

if __name__ == "__main__":
    main()