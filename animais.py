from datetime import datetime

# Classe base Animal, que representa animais em geral
class Animal:
    def __init__(self, nome, data_nascimento):
        # Encapsulamento: uso de atributos protegidos (com o prefixo _)
        self._nome = nome
        # Conversão da data de nascimento para um objeto datetime
        self._data_nascimento = datetime.strptime(data_nascimento, "%Y-%m-%d")

    # Método para calcular a idade do animal
    def calcular_idade(self):
        hoje = datetime.now()
        idade = hoje.year - self._data_nascimento.year
        # Ajuste da idade se o aniversário ainda não ocorreu este ano
        if hoje.month < self._data_nascimento.month or (hoje.month == self._data_nascimento.month and hoje.day < self._data_nascimento.day):
            idade -= 1
        return idade

    # Método abstrato para fazer som (será implementado nas classes filhas)
    def fazer_som(self):
        pass

# Classe Peixes, que herda de Animal
class Peixes(Animal):
    def __init__(self, nome, data_nascimento, cor, tamanho, nadadeiras, escamas, tipo_agua):
        super().__init__(nome, data_nascimento)
        self._cor = cor
        self._tamanho = tamanho
        self._nadadeiras = nadadeiras
        self._escamas = escamas
        self._tipo_agua = tipo_agua

    # Método específico para peixes: nadar
    def nadar(self):
        print(f'{self._nome} está nadando em água {self._tipo_agua}')

    # Método para exibir características do peixe, incluindo idade
    def exibir_caracteristicas(self):
        print(f'{self._nome} ({self._cor}):\nTamanho: {self._tamanho}\nNadadeiras: {self._nadadeiras}\nEscamas: {self._escamas}')
        print(f'Idade: {self.calcular_idade()} anos')

    # Implementação do método abstrato fazer_som para peixes
    def fazer_som(self):
        print(f'{self._nome} faz bolhas e sons de água.')

    # Método para verificar se o peixe pode viver em água doce
    def pode_viver_em_agua_doce(self):
        return self._tipo_agua == 'doce'

# Classe PeixesAguaDoce, que herda de Peixes (específica para peixes de água doce)
class PeixesAguaDoce(Peixes):
    def __init__(self, nome, data_nascimento, cor, tamanho, nadadeiras, escamas):
        super().__init__(nome, data_nascimento, cor, tamanho, nadadeiras, escamas, tipo_agua='doce')

# Classe PeixesAguaSalgada, que herda de Peixes (específica para peixes de água salgada)
class PeixesAguaSalgada(Peixes):
    def __init__(self, nome, data_nascimento, cor, tamanho, nadadeiras, escamas):
        super().__init__(nome, data_nascimento, cor, tamanho, nadadeiras, escamas, tipo_agua='salgada')

    # Método para verificar se o peixe pode viver em água salgada
    def pode_viver_em_agua_salgada(self):
        return self._tipo_agua == 'salgada'

# Classe Aves, que herda de Animal
class Aves(Animal):
    def __init__(self, nome, data_nascimento, cor):
        super().__init__(nome, data_nascimento)
        self._cor = cor

    # Método específico para aves: voar
    def voar(self):
        print(f'{self._nome} está voando.')

    # Método para exibir a cor do animal
    def cor_animal(self):
        print(f'{self._nome} tem a cor: {self._cor}')

# Classe AvesDeRapina, que herda de Aves (específica para aves de rapina)
class AvesDeRapina(Aves):
    def __init__(self, nome, data_nascimento, cor, envergadura_asas):
        super().__init__(nome, data_nascimento, cor)
        self._envergadura_asas = envergadura_asas

    # Método específico para aves de rapina: caçar
    def cacar(self):
        print(f'{self._nome} está caçando.')

    # Método para exibir características do animal, incluindo idade
    def exibir_caracteristicas(self):
        super().cor_animal()
        print(f'Envergadura das asas: {self._envergadura_asas}')
        print(f'Idade: {self.calcular_idade()} anos')

# Classe AvesAquaticas, que herda de Aves (específica para aves aquáticas)
class AvesAquaticas(Aves):
    def __init__(self, nome, data_nascimento, cor, habitat_aquatico):
        super().__init__(nome, data_nascimento, cor)
        self._habitat_aquatico = habitat_aquatico

    # Método específico para aves aquáticas: nadar
    def nadar(self):
        print(f'{self._nome} está nadando em seu habitat aquático: {self._habitat_aquatico}')

    # Método para exibir o habitat das aves, incluindo idade
    def exibir_habitat(self):
        print(f'{self._nome} habita principalmente em ambientes aquáticos, como {self._habitat_aquatico}')
        print(f'Idade: {self.calcular_idade()} anos')


if __name__ == "__main__":
    # Criando instâncias de diferentes animais
    peixe_doce = PeixesAguaDoce("Betta", "2022-01-15", "Azul", "Pequeno", 2, "Escamoso")
    peixe_salgado = PeixesAguaSalgada("Tubarão", "2020-03-10", "Cinza", "Grande", 5, "Escamoso")
    ave_rapina = AvesDeRapina("Águia", "2018-07-03", "Marrom", "Grande")
    ave_aquatica = AvesAquaticas("Pato", "2020-09-12", "Branco", "Lagos e rios")

    print("Peixe de água doce:")
    peixe_doce.nadar()
    peixe_doce.exibir_caracteristicas()
    peixe_doce.fazer_som()  # Demonstrando polimorfismo com o método fazer_som
    print(f"Pode viver em água doce? {peixe_doce.pode_viver_em_agua_doce()}")

    print("\nPeixe de água salgada:")
    peixe_salgado.nadar()
    peixe_salgado.exibir_caracteristicas()
    peixe_salgado.fazer_som()
    print(f"Pode viver em água salgada? {peixe_salgado.pode_viver_em_agua_salgada()}")

    print("\nAve de rapina:")
    ave_rapina.voar()
    ave_rapina.cacar()
    ave_rapina.exibir_caracteristicas()

    print("\nAve aquática:")
    ave_aquatica.voar()
    ave_aquatica.nadar()
    ave_aquatica.exibir_habitat()