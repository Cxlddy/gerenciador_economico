import os 
import time
from tqdm import tqdm
import pandas as pd
from src.database.database import Database
from src.gastos import Gastos
from pathlib import Path

database = Database()
gastos = Gastos()

def carregando():
    for i in tqdm(range(100)):
        time.sleep(0.05)

def clear():
    os.system(command='cls' if os.name == 'nt' else 'clear')

while True:
    clear()
    print("\n==== MENU INICIAL ====")
    print("\n[1] - Adicionar Gasto\n[2] - Remover gasto\n[3] - Ver tabela de gastos\n[4] - Exportar gastos\n[5] - Buscar gasto\n[0] - Sair")
    esco = input("Escolha: ")
    
    if esco == "1":
        clear()
        tipo = input("Digite o tipo do gasto: ")
        valor = float(input("Digite o valor do gasto: "))
        desc = input("Digite uma descrição para o gasto: ")
        print("\n- Adicionar gasto -")
        gastos.adicionar_gasto(tipo, desc, valor)

    elif esco == "2":
        clear()
        print("\n- Remover Gasto -")
        gastos.remover_gasto()

    elif esco == "3":
        clear()
        database.ler_dataframe()
        input("Pressione Enter para sair...")
    
    elif esco == "4":
        clear()
        print("Digite o caminho onde deseja guardar o excel:")
        print("Exemplo: C:\Downloads\gastos.xlsx")
        CAMINHO = input("\nCaminho: ")
        caminho_excel = Path(CAMINHO)
        carregando()
        database.exportar_excel(caminho_excel)
        database.formatar_excel(caminho_excel)
        print(f"Excel exportado em: {caminho_excel}")
        input("\nDigite Enter para continuar...")

    elif esco == "5":
        clear()
        print("\n- Busca de Gastos -")
        tipo = input("Digite o tipo do gasto que deseja buscar: ")
        valor_min = input("Digite o valor mínimo dos dados que aparecerão: ")
        valor_max = input("Digite o valor máximo dos gastos que aparecerão: ")
        descricao = input("Digite a descrição do gasto: ")
        data = input("Digite a data do gasto: ")
        gastos.buscar_gastos(tipo, valor_min, valor_max, descricao, data)
        input("Digite Enter para continuar...")
    
    elif esco == "0":
        break