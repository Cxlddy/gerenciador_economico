from datetime import datetime
from .database.database import Database


class Gastos:
    def __init__(self):
        self.db = Database()
        self.gastos = self.db.carregar_dados()

    def salvar(self):
        self.db.salvar_dados(self.gastos)

    def gerar_id(self):
        if not self.gastos:
            return 1
        return max(g["id"] for g in self.gastos) + 1

    def adicionar_gasto(self, tipo, desc, valor, data=None):
        agora = datetime.now()

        novo_gasto = {
            "id": self.gerar_id(),
            "data": str(data) if data else agora.strftime("%Y-%m-%d"),
            "tipo": tipo,
            "valor": float(valor),
            "horario": agora.strftime("%H:%M:%S"),
            "descricao": desc,
        }

        self.gastos.append(novo_gasto)
        self.salvar()
        print("Gasto salvo com sucesso!")
        return novo_gasto

    def remover_gasto(self, id_gasto):
        for gasto in self.gastos:
            if gasto["id"] == id_gasto:
                self.gastos.remove(gasto)
                self.salvar()
                print("Gasto removido com sucesso!")
                return True

        return False

    def listar_gastos(self):
        return self.gastos

    def buscar_gastos(self, tipo=None, valor_min=None, valor_max=None, descricao=None, data=None):
        resultados = self.gastos

        if tipo:
            resultados = [g for g in resultados if g["tipo"] == tipo]

        if valor_min is not None:
            resultados = [g for g in resultados if float(g["valor"]) >= valor_min]

        if valor_max is not None:
            resultados = [g for g in resultados if float(g["valor"]) <= valor_max]

        if descricao:
            resultados = [
                g for g in resultados
                if descricao.lower() in g["descricao"].lower()
            ]
        
        if data:
            resultados = [g for g in resultados if data in g["data"]]

        print(f"\n {resultados}")
        return resultados