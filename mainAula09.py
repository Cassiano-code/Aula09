from classesAula09 import Pessoa
from classesAula09 import Fisica
from classesAula09 import Juridica

p = Pessoa("2312","joao","rua tupininba","3342424")
f = Fisica("11","Carlos","rua nao sei","88888888","378273899","25",70,1.60)
j = Juridica("2312a","joaoa","rua tupininbaa","3342424a","111111111","1212","5")

print("Dados pessoais:")
print(p.getNome())
print(p.getTelefone())
print("Pessoa fisica CPF: ")
print(f._getCpf())
print("Calculo IMC: ")
print(f.setCalculaIMC())
print("CNPJ pessoa juridica: ")
print(j._getCnpj())
print("Emissao nota fiscal: ")
print(j.getEmiteNF())

