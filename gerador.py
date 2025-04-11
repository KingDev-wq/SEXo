import random
import time
import os
import requests
import threading

caracteres = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
codigos = []
gerando = False

ascii_caveira = """
⠀⠀⠀⠀⠀⣶⡆⠀⠀⠀⢀⣴⢦⠀⠀⠀⠀⣖⡶⠀⠀⠀⠀⡏⡧⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢹⣷⡀⠀⠀⢀⣿⣧⡀⠀⠀⢠⣾⣧⠀⠀⠀⣠⣾⡇⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢸⣿⣿⣦⡀⣼⣿⣿⣷⡀⢠⣿⣿⣿⡆⢀⣾⣿⣿⡇⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⠋⠙⢿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠠⣤⣉⣙⠛⠛⠛⠿⠿⠁⣴⣦⡈⠻⠛⠛⠛⢛⣉⣁⡤⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠈⠉⠛⠻⠿⠶⣶⣆⠈⢿⡿⠃⣠⣶⡿⠿⠟⠛⠉⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢠⣿⣿⣶⣶⣤⣤⣤⣤⡀⢁⣠⣤⣤⣤⣶⣶⣿⣿⡀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣸⣿⡏⠉⠙⠛⠿⢿⣿⣿⣾⣿⡿⠿⠛⠋⠉⠹⣿⡇⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠻⢿⣧⣀⠀⠀⣀⣀⣼⡿⣿⣯⣀⣀⠀⠀⣀⣼⡿⠗⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠙⠻⣿⣿⣿⣿⣿⠁⠘⣿⣿⣿⣿⣿⠟⠉⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣿⣿⣿⣇⣀⣀⣹⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⠿⣿⡿⢿⣿⠿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⡇⢀⣿⡇⢸⣿⡀⢸⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠁⠈⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
"""

def gerar_codigo():
    return "https://discord.gift/" + "".join(random.choices(caracteres, k=16))

def gerar_codigos():
    global gerando
    gerando = True
    while gerando:
        codigo = gerar_codigo()
        codigos.append(codigo)
        print(f"[GERADO] {codigo}")
        time.sleep(0.1)

def iniciar_geracao_com_enter():
    global gerando
    thread = threading.Thread(target=gerar_codigos)
    thread.start()
    input("\nPressione ENTER para parar a geração...\n")
    gerando = False
    thread.join()
    print("\nGeração encerrada. Retornando ao menu...")
    time.sleep(1)

def verificar_codigos_reais():
    print(f"\nVerificando {len(codigos)} códigos na API real do Discord...")
    achou = False
    for codigo in codigos:
        try:
            token = codigo.split("/")[-1]
            url = f"https://discordapp.com/api/v9/entitlements/gift-codes/{token}?with_application=false&with_subscription_plan=true"
            resposta = requests.get(url)
            if resposta.status_code == 200:
                print(f"[VÁLIDO] {codigo}")
                achou = True
            elif resposta.status_code == 404:
                print(f"[INVÁLIDO] {codigo}")
            else:
                print(f"[??] {codigo} | Código retornou {resposta.status_code}")
            time.sleep(0.5)
        except Exception as e:
            print(f"Erro ao verificar {codigo}: {e}")
    if not achou:
        print("Nenhum código válido encontrado.")
    input("\nPressione Enter para continuar...")

def menu():
    while True:
        os.system("clear")
        print(ascii_caveira)
        print("""
╔══════════════════════════════════════════╗
║      KING - TERMINAL NITRO CHECKER       ║
╚══════════════════════════════════════════╝

[1] Iniciar Gerador de Nitro
[2] Verificar Códigos (real)
[3] Resetar e Recomeçar
[4] Créditos do Projeto
[5] Sair
""")
        escolha = input("Escolha uma opção: ")
        if escolha == "1":
            iniciar_geracao_com_enter()
        elif escolha == "2":
            verificar_codigos_reais()
        elif escolha == "3":
            codigos.clear()
            print("Códigos resetados.")
            time.sleep(1)
        elif escolha == "4":
            print("Criado por KING - Scanner Nitro Hacker Style.")
            input("Pressione Enter para continuar...")
        elif escolha == "5":
            print("Encerrando...")
            break
        else:
            print("Opção inválida.")
            time.sleep(1)

menu()
