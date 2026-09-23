class Estoque:
    def __init__(self,codigo_estoque,localizacao,capacidade,quantidade,caixas,data):
        self.codigo_estoque = codigo_estoque
        self.localizacao = localizacao
        self.capacidade = capacidade
        self.quantidade = quantidade
        self.caixas = caixas
        self.data = data

    def mostrarestoque(self):
        print(f"Cd:{self.codigo_estoque}| Lc:{self.localizacao}| Cp:{self.capacidade}| Qt:{self.quantidade}| Cx:{self.caixas}| Dt:{self.data}")

    def registrarentrada(self):
        data_entrada = input("Dia de entrada no estoque: ")
        dono = input("Responsalvel: ")
        descricao = input("Descrição: ")

        print("--- Registro de Entrada ---")
        print(f"Dia: {data_entrada}")
        print(f"Responvel: {dono}")
        print(f"Descrição: {descricao}")

    def saidaestoque(self):
        data_saida = input("Que dia saiu: ")
        responsavel = input("Responsavel: ")
        local = input("Pra onde foi: ")

        print("--- Registro de Saida ---")
        print(f"Dia {data_saida}")
        print(f"Responsavel: {responsavel}")
        print(f"Local: {local}")

teste =Estoque("30","Roraima","200","1000","4 caixas","09/01/2009")
teste.mostrarestoque()
teste.saidaestoque()
        
