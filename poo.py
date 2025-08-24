class Aluno:
    """
    Classe que representa um aluno no sistema.
    Esta é a classe base que contém todas as informações e comportamentos de um aluno.
    """
    """
    Classe que representa um aluno no sistema.
    Esta é a classe base que contém todas as informações e comportamentos de um aluno.
    """
    
    def __init__(self, matricula, nome, idade, email, telefone): # Método construtor (inicializador) da classe Aluno.
        """
        Método construtor (inicializador) da classe Aluno.
        É executado automaticamente quando criamos um novo objeto Aluno.
        
        Parâmetros:
        - matricula: número único de identificação do aluno
        - nome: nome completo do aluno
        - idade: idade do aluno
        - email: endereço de email do aluno
        - telefone: número de telefone do aluno
        """
        # Atributos de instância - cada aluno terá seus próprios valores
        self.matricula = matricula      # Número único de identificação
        self.nome = nome                # Nome do aluno
        self.idade = idade              # Idade do aluno
        self.email = email              # Email do aluno
        self.telefone = telefone        # Telefone do aluno
        self.notas = []                 # Lista vazia para armazenar as notas
        self.faltas = 0                 # Contador de faltas, inicia em 0
    
    def adicionar_nota(self, nota):
        """
        Método para adicionar uma nota ao aluno.
        
        Parâmetros:
        - nota: valor da nota (deve estar entre 0 e 10)
        
        Retorna:
        - True se a nota foi adicionada com sucesso
        - False se a nota é inválida
        """
        # Validação: verifica se a nota está no intervalo válido (0 a 10)
        if 0 <= nota <= 10:
            # Se válida, adiciona a nota à lista de notas do aluno
            self.notas.append(nota)
            return True  # Retorna True indicando sucesso
        else:
            # Se inválida, exibe mensagem de erro
            print("Nota deve estar entre 0 e 10")
            return False  # Retorna False indicando falha
    
    def calcular_media(self):
        """
        Método para calcular a média das notas do aluno.
        
        Retorna:
        - A média das notas se houver notas cadastradas
        - 0 se não houver notas
        """
        # Verifica se existem notas na lista
        if self.notas:
            # Se existem notas, calcula a média: soma todas as notas e divide pela quantidade
            return sum(self.notas) / len(self.notas)
        # Se não existem notas, retorna 0
        return 0
    
    def adicionar_falta(self):
        """
        Método para adicionar uma falta ao aluno.
        Incrementa o contador de faltas em 1.
        """
        # Incrementa o contador de faltas
        self.faltas += 1
    
    def get_status(self):
        """
        Método para determinar o status do aluno baseado na média.
        
        Retorna:
        - "Aprovado" se média >= 7
        - "Recuperação" se média >= 5 e < 7
        - "Reprovado" se média < 5
        """
        # Calcula a média atual do aluno
        media = self.calcular_media()
        
        # Verifica o status baseado na média
        if media >= 7:
            return "Aprovado"      # Média 7 ou superior = Aprovado
        elif media >= 5:
            return "Recuperação"   # Média entre 5 e 6.9 = Recuperação
        else:
            return "Reprovado"     # Média menor que 5 = Reprovado
    
    def __str__(self):
        """
        Método especial que define como o objeto será exibido quando convertido para string.
        É chamado automaticamente quando usamos print() ou str() no objeto.
        
        Retorna:
        - String formatada com informações do aluno
        """
        # Retorna uma string formatada com nome, matrícula e média
        return f"Aluno: {self.nome} (Matrícula: {self.matricula}) - Média: {self.calcular_media():.2f}"


class Turma:
    """
    Classe que representa uma turma de alunos.
    Uma turma pode conter vários alunos e tem um professor responsável.
    """
    
    def __init__(self, codigo, nome, professor):
        """
        Método construtor da classe Turma.
        
        Parâmetros:
        - codigo: código único da turma
        - nome: nome da turma (ex: "Matemática Básica")
        - professor: nome do professor responsável
        """
        # Atributos da turma
        self.codigo = codigo                    # Código único da turma
        self.nome = nome                        # Nome da turma
        self.professor = professor              # Nome do professor
        self.alunos = []                        # Lista vazia para armazenar os alunos
        self.capacidade_maxima = 30             # Número máximo de alunos na turma
    
    def adicionar_aluno(self, aluno):
        """
        Método para adicionar um aluno à turma.
        
        Parâmetros:
        - aluno: objeto da classe Aluno
        
        Retorna:
        - True se o aluno foi adicionado com sucesso
        - False se não foi possível adicionar
        """
        # Verifica se a turma ainda tem vagas
        if len(self.alunos) < self.capacidade_maxima:
            # Verifica se o aluno já não está na turma
            if aluno not in self.alunos:
                # Adiciona o aluno à lista de alunos da turma
                self.alunos.append(aluno)
                # Exibe mensagem de confirmação
                print(f"Aluno {aluno.nome} adicionado à turma {self.nome}")
                return True
            else:
                # Aluno já está na turma
                print(f"Aluno {aluno.nome} já está na turma")
                return False
        else:
            # Turma está lotada
            print("Turma está lotada")
            return False
    
    def remover_aluno(self, matricula):
        """
        Método para remover um aluno da turma pela matrícula.
        
        Parâmetros:
        - matricula: número da matrícula do aluno a ser removido
        
        Retorna:
        - True se o aluno foi removido
        - False se o aluno não foi encontrado
        """
        # Percorre a lista de alunos da turma
        for aluno in self.alunos:
            # Verifica se a matrícula corresponde
            if aluno.matricula == matricula:
                # Remove o aluno da lista
                self.alunos.remove(aluno)
                print(f"Aluno {aluno.nome} removido da turma")
                return True
        # Se chegou aqui, o aluno não foi encontrado
        print("Aluno não encontrado na turma")
        return False
    
    def buscar_aluno(self, matricula):
        """
        Método para buscar um aluno na turma pela matrícula.
        
        Parâmetros:
        - matricula: número da matrícula do aluno
        
        Retorna:
        - Objeto Aluno se encontrado
        - None se não encontrado
        """
        # Percorre a lista de alunos da turma
        for aluno in self.alunos:
            # Verifica se a matrícula corresponde
            if aluno.matricula == matricula:
                return aluno  # Retorna o objeto aluno encontrado
        # Se não encontrou, retorna None
        return None
    
    def listar_alunos(self):
        """
        Método para listar todos os alunos da turma.
        Exibe informações de cada aluno na tela.
        """
        # Verifica se existem alunos na turma
        if self.alunos:
            print(f"\nAlunos da turma {self.nome}:")
            # Percorre cada aluno e exibe suas informações
            for aluno in self.alunos:
                print(f"  - {aluno}")  # Usa o método __str__ do aluno
        else:
            # Se não há alunos, exibe mensagem
            print(f"Nenhum aluno cadastrado na turma {self.nome}")
    
    def calcular_media_turma(self):
        """
        Método para calcular a média geral da turma.
        
        Retorna:
        - A média das médias de todos os alunos
        - 0 se não há alunos na turma
        """
        # Verifica se existem alunos na turma
        if self.alunos:
            # List comprehension: cria uma lista com as médias de todos os alunos
            medias = [aluno.calcular_media() for aluno in self.alunos]
            # Calcula a média geral: soma todas as médias e divide pela quantidade
            return sum(medias) / len(medias)
        # Se não há alunos, retorna 0
        return 0
    
    def __str__(self):
        """
        Método especial para exibir informações da turma.
        
        Retorna:
        - String formatada com informações da turma
        """
        return f"Turma: {self.nome} (Código: {self.codigo}) - Professor: {self.professor} - Alunos: {len(self.alunos)}"


class SistemaCadastro:
    """
    Classe principal do sistema de cadastro.
    Gerencia todas as operações do sistema, incluindo alunos e turmas.
    """
    
    def __init__(self):
        """
        Método construtor do sistema.
        Inicializa as estruturas de dados necessárias.
        """
        self.alunos = {}              # Dicionário para armazenar alunos (matrícula -> aluno)
        self.turmas = {}              # Dicionário para armazenar turmas (código -> turma)
        self.proxima_matricula = 1001 # Contador para gerar matrículas únicas
    
    def cadastrar_aluno(self, nome, idade, email, telefone):
        """
        Método para cadastrar um novo aluno no sistema.
        
        Parâmetros:
        - nome: nome do aluno
        - idade: idade do aluno
        - email: email do aluno
        - telefone: telefone do aluno
        
        Retorna:
        - Objeto Aluno criado
        """
        # Gera a próxima matrícula disponível
        matricula = self.proxima_matricula
        # Cria um novo objeto Aluno
        aluno = Aluno(matricula, nome, idade, email, telefone)
        # Adiciona o aluno ao dicionário usando a matrícula como chave
        self.alunos[matricula] = aluno
        # Incrementa o contador de matrículas
        self.proxima_matricula += 1
        # Exibe mensagem de confirmação
        print(f"Aluno {nome} cadastrado com sucesso! Matrícula: {matricula}")
        return aluno
    
    def buscar_aluno_por_matricula(self, matricula):
        """
        Método para buscar um aluno pela matrícula.
        
        Parâmetros:
        - matricula: número da matrícula
        
        Retorna:
        - Objeto Aluno se encontrado
        - None se não encontrado
        """
        # Usa o método get() do dicionário para buscar a matrícula
        # Se não encontrar, retorna None automaticamente
        return self.alunos.get(matricula)
    
    def buscar_aluno_por_nome(self, nome):
        """
        Método para buscar alunos pelo nome (busca parcial).
        
        Parâmetros:
        - nome: nome ou parte do nome a ser buscado
        
        Retorna:
        - Lista com todos os alunos que contêm o nome buscado
        """
        # Lista para armazenar os alunos encontrados
        encontrados = []
        # Percorre todos os valores (alunos) do dicionário
        for aluno in self.alunos.values():
            # Verifica se o nome buscado está contido no nome do aluno (case insensitive)
            if nome.lower() in aluno.nome.lower():
                # Se encontrou, adiciona à lista
                encontrados.append(aluno)
        return encontrados
    
    def listar_todos_alunos(self):
        """
        Método para listar todos os alunos cadastrados no sistema.
        """
        # Verifica se existem alunos cadastrados
        if self.alunos:
            print("\n=== TODOS OS ALUNOS CADASTRADOS ===")
            # Percorre todos os alunos e exibe suas informações
            for aluno in self.alunos.values():
                print(f"  {aluno}")  # Usa o método __str__ do aluno
        else:
            print("Nenhum aluno cadastrado no sistema")
    
    def criar_turma(self, codigo, nome, professor):
        """
        Método para criar uma nova turma.
        
        Parâmetros:
        - codigo: código único da turma
        - nome: nome da turma
        - professor: nome do professor
        
        Retorna:
        - Objeto Turma criado
        - None se o código já existe
        """
        # Verifica se o código da turma já existe
        if codigo not in self.turmas:
            # Cria um novo objeto Turma
            turma = Turma(codigo, nome, professor)
            # Adiciona a turma ao dicionário usando o código como chave
            self.turmas[codigo] = turma
            print(f"Turma {nome} criada com sucesso!")
            return turma
        else:
            print("Código de turma já existe")
            return None
    
    def listar_todas_turmas(self):
        """
        Método para listar todas as turmas criadas no sistema.
        """
        # Verifica se existem turmas criadas
        if self.turmas:
            print("\n=== TODAS AS TURMAS ===")
            # Percorre todas as turmas e exibe suas informações
            for turma in self.turmas.values():
                print(f"  {turma}")  # Usa o método __str__ da turma
        else:
            print("Nenhuma turma criada no sistema")
    
    def menu_principal(self):
        """
        Método que exibe o menu principal do sistema.
        Loop infinito que permite ao usuário navegar pelas opções.
        """
        # Loop infinito para manter o menu ativo
        while True:
            # Exibe o cabeçalho do menu
            print("\n" + "="*50)
            print("    SISTEMA DE CADASTRO DE ALUNOS")
            print("="*50)
            # Lista todas as opções disponíveis
            print("1. Cadastrar novo aluno")
            print("2. Buscar aluno por matrícula")
            print("3. Buscar aluno por nome")
            print("4. Listar todos os alunos")
            print("5. Criar nova turma")
            print("6. Adicionar aluno à turma")
            print("7. Listar turmas")
            print("8. Gerenciar notas")
            print("9. Sair")
            print("="*50)
            
            # Solicita a escolha do usuário
            opcao = input("Escolha uma opção: ")
            
            # Estrutura condicional para executar a opção escolhida
            if opcao == "1":
                self.cadastrar_aluno_menu()
            elif opcao == "2":
                self.buscar_aluno_matricula_menu()
            elif opcao == "3":
                self.buscar_aluno_nome_menu()
            elif opcao == "4":
                self.listar_todos_alunos()
            elif opcao == "5":
                self.criar_turma_menu()
            elif opcao == "6":
                self.adicionar_aluno_turma_menu()
            elif opcao == "7":
                self.listar_turmas_menu()
            elif opcao == "8":
                self.gerenciar_notas_menu()
            elif opcao == "9":
                print("Saindo do sistema...")
                break  # Sai do loop e encerra o programa
            else:
                print("Opção inválida!")
    
    def cadastrar_aluno_menu(self):
        """
        Método que implementa o menu para cadastrar um novo aluno.
        Solicita os dados do usuário e chama o método de cadastro.
        """
        print("\n--- CADASTRAR NOVO ALUNO ---")
        # Solicita cada dado do aluno
        nome = input("Nome: ")
        idade = int(input("Idade: "))  # Converte para inteiro
        email = input("Email: ")
        telefone = input("Telefone: ")
        # Chama o método de cadastro com os dados coletados
        self.cadastrar_aluno(nome, idade, email, telefone)
    
    def buscar_aluno_matricula_menu(self):
        """
        Método que implementa o menu para buscar aluno por matrícula.
        """
        print("\n--- BUSCAR ALUNO POR MATRÍCULA ---")
        # Solicita a matrícula e converte para inteiro
        matricula = int(input("Digite a matrícula: "))
        # Busca o aluno no sistema
        aluno = self.buscar_aluno_por_matricula(matricula)
        # Verifica se o aluno foi encontrado
        if aluno:
            # Exibe as informações detalhadas do aluno
            print(f"\nAluno encontrado: {aluno}")
            print(f"Email: {aluno.email}")
            print(f"Telefone: {aluno.telefone}")
            print(f"Faltas: {aluno.faltas}")
        else:
            print("Aluno não encontrado")
    
    def buscar_aluno_nome_menu(self):
        """
        Método que implementa o menu para buscar aluno por nome.
        """
        print("\n--- BUSCAR ALUNO POR NOME ---")
        # Solicita o nome (ou parte do nome)
        nome = input("Digite o nome (ou parte): ")
        # Busca alunos que contêm o nome
        alunos = self.buscar_aluno_por_nome(nome)
        # Verifica se encontrou algum aluno
        if alunos:
            print(f"\nAlunos encontrados ({len(alunos)}):")
            # Exibe cada aluno encontrado
            for aluno in alunos:
                print(f"  {aluno}")
        else:
            print("Nenhum aluno encontrado")
    
    def criar_turma_menu(self):
        """
        Método que implementa o menu para criar uma nova turma.
        """
        print("\n--- CRIAR NOVA TURMA ---")
        # Solicita os dados da turma
        codigo = input("Código da turma: ")
        nome = input("Nome da turma: ")
        professor = input("Professor: ")
        # Chama o método de criação da turma
        self.criar_turma(codigo, nome, professor)
    
    def adicionar_aluno_turma_menu(self):
        """
        Método que implementa o menu para adicionar aluno à turma.
        """
        print("\n--- ADICIONAR ALUNO À TURMA ---")
        # Verifica se existem turmas criadas
        if not self.turmas:
            print("Nenhuma turma criada. Crie uma turma primeiro.")
            return
        
        # Exibe as turmas disponíveis
        print("Turmas disponíveis:")
        for codigo, turma in self.turmas.items():
            print(f"  {codigo}: {turma.nome}")
        
        # Solicita o código da turma
        codigo_turma = input("Digite o código da turma: ")
        # Verifica se a turma existe
        if codigo_turma not in self.turmas:
            print("Turma não encontrada")
            return
        
        # Solicita a matrícula do aluno
        matricula = int(input("Digite a matrícula do aluno: "))
        # Busca o aluno no sistema
        aluno = self.buscar_aluno_por_matricula(matricula)
        # Verifica se o aluno foi encontrado
        if aluno:
            # Adiciona o aluno à turma
            self.turmas[codigo_turma].adicionar_aluno(aluno)
        else:
            print("Aluno não encontrado")
    
    def listar_turmas_menu(self):
        """
        Método que implementa o menu para listar turmas.
        """
        # Lista todas as turmas
        self.listar_todas_turmas()
        # Se existem turmas, permite ver detalhes de uma específica
        if self.turmas:
            codigo = input("\nDigite o código da turma para ver detalhes (ou Enter para voltar): ")
            # Verifica se o código foi fornecido e se a turma existe
            if codigo in self.turmas:
                # Lista os alunos da turma específica
                self.turmas[codigo].listar_alunos()
    
    def gerenciar_notas_menu(self):
        """
        Método que implementa o menu para gerenciar notas dos alunos.
        """
        print("\n--- GERENCIAR NOTAS ---")
        # Solicita a matrícula do aluno
        matricula = int(input("Digite a matrícula do aluno: "))
        # Busca o aluno no sistema
        aluno = self.buscar_aluno_por_matricula(matricula)
        # Verifica se o aluno foi encontrado
        if aluno:
            # Exibe as informações atuais do aluno
            print(f"Aluno: {aluno.nome}")
            print(f"Notas atuais: {aluno.notas}")
            print(f"Média atual: {aluno.calcular_media():.2f}")
            print(f"Status: {aluno.get_status()}")
            
            # Menu para adicionar nota ou voltar
            opcao = input("\n1. Adicionar nota\n2. Voltar\nEscolha: ")
            if opcao == "1":
                # Solicita a nova nota
                nota = float(input("Digite a nota (0-10): "))
                # Adiciona a nota ao aluno
                aluno.adicionar_nota(nota)
                # Exibe as informações atualizadas
                print(f"Nova média: {aluno.calcular_media():.2f}")
                print(f"Novo status: {aluno.get_status()}")
        else:
            print("Aluno não encontrado")


# =====================================================
# FUNÇÃO PRINCIPAL - PONTO DE ENTRADA DO PROGRAMA
# =====================================================

def main():
    """
    Função principal que inicia o sistema.
    Esta é a primeira função executada quando o programa é iniciado.
    """
    # Mensagem de boas-vindas
    print("Bem-vindo ao Sistema de Cadastro de Alunos!")
    
    # Cria uma instância do sistema de cadastro
    sistema = SistemaCadastro()
    
    # =====================================================
    # DADOS DE EXEMPLO - PARA DEMONSTRAÇÃO DO SISTEMA
    # =====================================================
    
    print("\nAdicionando dados de exemplo...")
    
    # Cadastra três alunos de exemplo
    aluno1 = sistema.cadastrar_aluno("João Silva", 18, "joao@email.com", "(11) 99999-1111")
    aluno2 = sistema.cadastrar_aluno("Maria Santos", 19, "maria@email.com", "(11) 99999-2222")
    aluno3 = sistema.cadastrar_aluno("Pedro Costa", 17, "pedro@email.com", "(11) 99999-3333")
    
    # Adiciona algumas notas aos alunos para demonstração
    aluno1.adicionar_nota(8.5)  # João: primeira nota
    aluno1.adicionar_nota(7.0)  # João: segunda nota
    aluno2.adicionar_nota(9.0)  # Maria: primeira nota
    aluno2.adicionar_nota(8.5)  # Maria: segunda nota
    aluno3.adicionar_nota(6.5)  # Pedro: primeira nota
    aluno3.adicionar_nota(7.5)  # Pedro: segunda nota
    
    # Cria uma turma de exemplo
    turma1 = sistema.criar_turma("TURMA001", "Matemática Básica", "Prof. Silva")
    
    # Adiciona os alunos à turma
    turma1.adicionar_aluno(aluno1)
    turma1.adicionar_aluno(aluno2)
    turma1.adicionar_aluno(aluno3)
    
    # Confirma que os dados foram adicionados
    print("\nDados de exemplo adicionados com sucesso!")
    
    # =====================================================
    # INICIA O SISTEMA INTERATIVO
    # =====================================================
    
    # Chama o menu principal do sistema
    sistema.menu_principal()


# =====================================================
# VERIFICAÇÃO DE EXECUÇÃO DIRETA
# =====================================================

if __name__ == "__main__":
    """
    Esta verificação garante que o código só será executado
    se o arquivo for executado diretamente (não importado).
    """
    main()  # Chama a função principal