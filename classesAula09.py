class Pessoa:

    def __init__(self, codigo, nome,endereco,telefone):
        self.codigo = codigo
        self._nome = nome
        self.__endereco = endereco
        self._telefone = telefone

    def getNome(self):
        return self._nome

    def getTelefone(self):
        return self._telefone



class Fisica(Pessoa):

    def __init__(self, codigoF, nomeF, enderecoF, telefoneF, cpf, idade, peso, altura):
        Pessoa.__init__(self, codigoF, nomeF, enderecoF,telefoneF)
        self._cpf = cpf
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def _getCpf(self):
        return self._cpf

    def setCalculaIMC(self):
        imc = float(self.peso /(self.altura * self.altura))
        self.imc = imc
        return self.imc

class Juridica(Pessoa):

    def __init__(self, codigoJ, nomeJ,enderecoJ,telefoneJ,cnpj,inscEst,quantFunc):
        Pessoa.__init__(self, codigoJ, nomeJ, enderecoJ,telefoneJ)
        self._cnpj = cnpj
        self._inscEst = inscEst
        self.quantFunc = quantFunc

    def _getCnpj(self):
        return self._cnpj
    
    def getEmiteNF(self):
        NF =+ 1
        print("Codigo NF: " + str(NF))
        print("CNPJ: " + self._cnpj)
        print("Inscrição Estadual: " + self._inscEst)
        print("Quantidade Trabalhadores: " + self.quantFunc)

        
                        

        
