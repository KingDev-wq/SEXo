import random
import time
import os
import requests

caracteres = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
codigos = []
gerando = False

def gerar_codigo():
    return "https://discord.gift/" + "".join(random.choices(caracteres, k=16))

def iniciar_geracao():
    global gerando
    gerando = True
    while gerando:
        novo = gerar_codigo()
        codigos.append(novo)
        print(f"[GERADO] {novo}")
        time.sleep(0.1)

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
            time.sleep(0.5)  # para evitar bloqueios por flood
        except Exception as e:
            print(f"Erro ao verificar {codigo}: {e}")
    if not achou:
        print("Nenhum código válido encontrado.")

def menu():
    while True:
        os.system("clear")
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
        op = input("Escolha uma opção: ")
        if op == "1":
            print("Iniciando gerador (Ctrl+C para parar)...")
            try:
                iniciar_geracao()
            except KeyboardInterrupt:
                global gerando
                gerando = False
                print("\nGeração parada.")
                input("Pressione Enter para continuar...")
        elif op == "2":
            verificar_codigos_reais()
            input("\nEnter para voltar ao menu...")
        elif op == "3":
            codigos.clear()
            print("Códigos resetados.")
            input("Enter para continuar...")
        elif op == "4":
            print("Criado por KING - Verificador Real de Nitro.")
            input("Enter para continuar...")
        elif op == "5":
            print("Saindo...")
            break
        else:
            print("Opção inválida.")
            input("Enter para continuar...")

menu()
