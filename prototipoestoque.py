#Sistema de estoque sem preços
import os
import json
from datetime import datetime, date

class Estoque:
    def __init__(self, arquivo_estoque='estoque.json'):
        self.arquivo_estoque = arquivo_estoque
        self.estoque = self.carregar_estoque()

    def carregar_estoque(self):
        if os.path.exists(self.arquivo_estoque):
            with open(self.arquivo_estoque, 'r', encoding='utf-8') as f:
                return json.load(f)
        return {}

    def salvar_estoque(self):
        with open(self.arquivo_estoque, 'w', encoding='utf-8') as f:
            json.dump(self.estoque, f, indent=4, ensure_ascii=False)

    def tradutor_str_pra_data(self, validade_str):
        """
        Aceita 'dd/mm/YYYY' ou 'dd/mm/YY'. Retorna date.
        Lança ValueError se inválido.
        """
        if validade_str is None:
            return None
        for fmt in ("%d/%m/%Y", "%d/%m/%y"):
            try:
                return datetime.strptime(validade_str, fmt).date()
            except ValueError:
                pass
        raise ValueError(f"Formato de validade inválido: {validade_str}. Use dd/mm/aaaa")

    def _format_validade(self, validade_date):
        if validade_date is None:
            return None
        return validade_date.strftime("%d/%m/%Y")

    def _is_vencido(self, validade_date):
        if validade_date is None:
            return False
        return validade_date < date.today()

    def adicionar_item(self, nome, quantidade, validade=None):
        """
        validade opcional: string 'dd/mm/aaaa' ou None.
        se não for informado nenhuma validade, o codigo vai determinar como null (indefinido/não perecivel no terminal)
        """

        # traduz e formata para armazenamento
        if validade is not None:
            validade_date = self.tradutor_str_pra_data(validade)
            validade_str = self._format_validade(validade_date)
        else:
            validade_str = None

        key = nome
        if key in self.estoque:
            self.estoque[key]['quantidade'] += quantidade
            # atualiza validade se fornecida (substitui)
            if validade_str is not None:
                self.estoque[key]['validade'] = validade_str
        else:
            self.estoque[key] = {
                'quantidade': quantidade,
                'validade': validade_str
            }
        self.salvar_estoque()

    def remover_item(self, nome, quantidade):
        if nome in self.estoque and self.estoque[nome]['quantidade'] >= quantidade:
            self.estoque[nome]['quantidade'] -= quantidade
            if self.estoque[nome]['quantidade'] == 0:
                del self.estoque[nome]
            self.salvar_estoque()
        else:
            print("Item não encontrado ou quantidade insuficiente.")

    def remover_itens_vencidos(self):
        removidos = []
        chave = list(self.estoque)
        for nome in chave:
            val_str = self.estoque[nome].get('validade')
            if val_str:
                try:
                    val_date = self.tradutor_str_pra_data(val_str)
                    if self._is_vencido(val_date):
                        removidos.append(nome)
                        del self.estoque[nome]
                except ValueError:
                    # se formato inválido, ignora aqui (pode-se logar)
                    pass
        if removidos:
            self.salvar_estoque()
        return removidos


    def gerar_relatorio(self):
        total_vencidos = 0
        print("Relatório de Estoque:")
        for nome, info in self.estoque.items():
            validade = info.get('validade')
            vencido = False
            if validade:
                try:
                    vencido = self._is_vencido(self.tradutor_str_pra_data(validade))
                except ValueError:
                    pass
            else:
                validade = "indefinido/não perecivel"
            if vencido:
                total_vencidos += 1
            vencido_tag = " - VENCIDO" if vencido else ""
            print(f"Item: {nome}, Quantidade: {info['quantidade']} unidades, Validade: {validade}{vencido_tag}")
        if total_vencidos:
            print(f"Itens vencidos: {total_vencidos}")

if __name__ == "__main__":

    #NOTA: o padrao das validades deve ser nos formatos 'dd/mm/aaaa' ou 'dd/mm/aa'
    estoque = Estoque()
    estoque.adicionar_item("Caneta", 100)
    estoque.adicionar_item("Caderno", 50,)

    estoque.adicionar_item("Tinta b/ água", 20, "14/09/2024")
    estoque.adicionar_item("Tinta b/ água", 100)
    estoque.remover_item("Caneta", 20)

    print("--- Relatório ---")
    estoque.gerar_relatorio()



    removidos = estoque.remover_itens_vencidos()
    if removidos:
        print("Itens a serem removidos por vencimento de validade:", removidos)