import graphviz
import os

# Define o diretório de saída para os diagramas
output_directory = "diagramas_sgil"
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

def gerar_diagrama_casos_uso():
    dot = graphviz.Digraph('SGIL_Diagrama_Casos_Uso', comment='Diagrama de Casos de Uso - SGIL', format='png')
    dot.attr(rankdir='LR', label='Diagrama de Casos de Uso - SGIL', fontsize='20')

    # Atores
    with dot.subgraph(name='cluster_atores') as sa:
        sa.attr(label='Atores', style='filled', color='lightgrey')
        sa.node_attr.update(shape='actor', style='filled', fillcolor='beige')
        sa.node('Cliente')
        sa.node('Funcionario', label='Funcionário (Vendedor/Caixa)')
        sa.node('Gerente', label='Gerente/Administrador')

    # Casos de Uso
    with dot.subgraph(name='cluster_casos_uso') as sc:
        sc.attr(label='Casos de Uso do Sistema', style='filled', color='lightcyan')
        sc.node_attr.update(shape='ellipse', style='filled', fillcolor='lightblue')

        # Casos de Uso do Cliente
        sc.node('CU_PesquisarProdutos', 'Pesquisar Produtos\n(RF09, RF10)')
        sc.node('CU_RealizarAutoatendimentoCompra', 'Realizar Autoatendimento\nde Compra')
        sc.node('CU_CadastrarSe', 'Cadastrar-se no Sistema')

        # Casos de Uso do Funcionário
        sc.node('CU_RealizarVenda', 'Realizar Venda\n(RF05)')
        sc.node('CU_ProcessarPagamento', 'Processar Pagamento\n(RF06)')
        sc.node('CU_CadastrarCliente', 'Cadastrar Cliente\n(RF01)')
        sc.node('CU_CancelarVenda', 'Cancelar Venda\n(RF14)')
        sc.node('CU_ConsultarEstoqueFunc', 'Consultar Estoque')


        # Casos de Uso do Gerente
        sc.node('CU_GerenciarFuncionarios', 'Gerenciar Funcionários\n(RF02, RNF05)')
        sc.node('CU_GerenciarProdutos', 'Gerenciar Produtos\n(RF03, RF11)')
        sc.node('CU_GerenciarFornecedores', 'Gerenciar Fornecedores\n(RF12)')
        sc.node('CU_GerenciarEstoque', 'Gerenciar Estoque\n(RF04, RF08)')
        sc.node('CU_GerarRelatorios', 'Gerar Relatórios\n(RF07, RF08)')
        sc.node('CU_GerenciarPromocoes', 'Gerenciar Promoções\n(RF13)')
        sc.node('CU_AuditarTransacoes', 'Auditar Transações')


    # Relacionamentos
    dot.edge('Cliente', 'CU_PesquisarProdutos')
    dot.edge('Cliente', 'CU_RealizarAutoatendimentoCompra')
    dot.edge('Cliente', 'CU_CadastrarSe')

    dot.edge('Funcionario', 'CU_RealizarVenda')
    dot.edge('Funcionario', 'CU_CadastrarCliente')
    dot.edge('Funcionario', 'CU_CancelarVenda')
    dot.edge('Funcionario', 'CU_ConsultarEstoqueFunc')
    dot.edge('Funcionario', 'CU_PesquisarProdutos') 

    dot.edge('Gerente', 'CU_GerenciarFuncionarios')
    dot.edge('Gerente', 'CU_GerenciarProdutos')
    dot.edge('Gerente', 'CU_GerenciarFornecedores')
    dot.edge('Gerente', 'CU_GerenciarEstoque')
    dot.edge('Gerente', 'CU_GerarRelatorios')
    dot.edge('Gerente', 'CU_GerenciarPromocoes')
    dot.edge('Gerente', 'CU_AuditarTransacoes')

    # Relações de Inclusão e Extensão
    dot.edge('CU_RealizarVenda', 'CU_ProcessarPagamento', label='<<include>>', style='dashed', arrowhead='empty')
    dot.edge('CU_RealizarAutoatendimentoCompra', 'CU_ProcessarPagamento', label='<<include>>', style='dashed', arrowhead='empty')
    dot.edge('CU_CancelarVenda', 'CU_AuditarTransacoes', label='<<notifica>>\n(potencial extensão)', style='dashed', arrowhead='open', dir='back')


    # Para Fornecedor (indireto, representado pela ação do Gerente)
    with dot.subgraph(name='cluster_fornecedor_interacao') as sf:
        sf.attr(label='Interação com Fornecedor (Indireta)', style='dotted')
        sf.node('Fornecedor_Nota', 'Fornecedor é cadastrado e seus\nprodutos gerenciados pelo Gerente.', shape='note', fillcolor='yellow')
        # sf.edge('Gerente', 'Fornecedor_Nota', style='dotted', dir='none') # Opcional se quiser linkar explicitamente

    dot.render(filename='sgil_diagrama_casos_uso', directory=output_directory, view=False)
    print(f"Diagrama de Casos de Uso gerado em: {os.path.join(output_directory, 'sgil_diagrama_casos_uso.png')}")

def gerar_diagrama_pacotes():
    dot = graphviz.Digraph('SGIL_Diagrama_Pacotes', comment='Diagrama de Pacotes - SGIL', format='png')
    dot.attr(label='Diagrama de Pacotes - SGIL', fontsize='20', rankdir='TB') # TB ou LR
    dot.node_attr.update(shape='folder', style='filled', fillcolor='khaki')

    # Pacotes
    dot.node('InterfaceUsuario', 'Interface do Usuário\n(GUI, Terminais)')
    dot.node('GestaoCadastros', 'Gestão de Cadastros\n(Clientes, Funcionários, Produtos, Fornecedores)')
    dot.node('ProcessamentoVendas', 'Processamento de Vendas\n(Vendas, Pagamentos, Cancelamentos)')
    dot.node('GestaoEstoque', 'Gestão de Estoque\n(Controle, Alertas)')
    dot.node('ConsultasAutoatendimento', 'Consultas e Autoatendimento')
    dot.node('RelatoriosGerenciais', 'Relatórios Gerenciais')
    dot.node('GestaoPromocoes', 'Gestão de Promoções')
    dot.node('Seguranca', 'Segurança\n(Acesso, Autenticação, Autorização)')
    dot.node('Persistencia', 'Persistência de Dados\n(Banco de Dados)')

    # Dependências (<<usa>> ou <<depende>>)
    # Para simplificar, usamos setas normais para indicar dependência/uso
    dot.edge('InterfaceUsuario', 'GestaoCadastros', label='usa')
    dot.edge('InterfaceUsuario', 'ProcessamentoVendas', label='usa')
    dot.edge('InterfaceUsuario', 'ConsultasAutoatendimento', label='usa')
    dot.edge('InterfaceUsuario', 'Seguranca', label='usa')

    dot.edge('GestaoCadastros', 'Persistencia', label='usa')
    dot.edge('GestaoCadastros', 'Seguranca', label='usa')


    dot.edge('ProcessamentoVendas', 'GestaoCadastros', label='usa (Produtos, Clientes)')
    dot.edge('ProcessamentoVendas', 'GestaoEstoque', label='usa')
    dot.edge('ProcessamentoVendas', 'GestaoPromocoes', label='usa')
    dot.edge('ProcessamentoVendas', 'Persistencia', label='usa')
    dot.edge('ProcessamentoVendas', 'Seguranca', label='usa')


    dot.edge('GestaoEstoque', 'GestaoCadastros', label='usa (Produtos)')
    dot.edge('GestaoEstoque', 'Persistencia', label='usa')
    dot.edge('GestaoEstoque', 'Seguranca', label='usa')


    dot.edge('ConsultasAutoatendimento', 'GestaoCadastros', label='usa (Produtos)')
    dot.edge('ConsultasAutoatendimento', 'GestaoEstoque', label='usa')
    dot.edge('ConsultasAutoatendimento', 'Persistencia', label='usa')
    # Autoatendimento também pode precisar de segurança para login se for área restrita.

    dot.edge('RelatoriosGerenciais', 'Persistencia', label='usa')
    dot.edge('RelatoriosGerenciais', 'Seguranca', label='usa')


    dot.edge('GestaoPromocoes', 'GestaoCadastros', label='usa (Produtos)')
    dot.edge('GestaoPromocoes', 'Persistencia', label='usa')
    dot.edge('GestaoPromocoes', 'Seguranca', label='usa')

    dot.render(filename='sgil_diagrama_pacotes', directory=output_directory, view=False)
    print(f"Diagrama de Pacotes gerado em: {os.path.join(output_directory, 'sgil_diagrama_pacotes.png')}")

def gerar_diagrama_classes():
    dot = graphviz.Digraph('SGIL_Diagrama_Classes', comment='Diagrama de Classes - SGIL', format='png')
    dot.attr(label='Diagrama de Classes - SGIL', fontsize='20', rankdir='TB') # TB ou LR
    dot.node_attr.update(shape='record', style='filled', fillcolor='lightgoldenrodyellow')

    # Classes Principais (com atributos e alguns métodos chave)
    # Usando HTML-like labels para melhor formatação de atributos e métodos
    dot.node('Pessoa', '{Pessoa (Abstrata)|+ nome: String\l+ cpf: String\l+ endereco: String\l+ telefone: String\l+ email: String\l|}')
    dot.node('Cliente', '{Cliente|+ idCliente: int\l+ historicoCompras: List<Venda>\l|+ cadastrar()\l+ pesquisarProduto()\l+ realizarCompraAutoatendimento()\l}')
    dot.node('UsuarioSistema', '{UsuarioSistema (Abstrata)|+ login: String\l+ senhaHash: String\l+ nivelAcesso: Enum\l|}')
    dot.node('Funcionario', '{Funcionário|+ idFuncionario: int\l+ cargo: String\l|+ realizarVenda()\l+ cadastrarCliente()\l+ processarPagamento()\l+ cancelarVenda()\l}')
    dot.node('Gerente', '{Gerente|+ idGerente: int\l|+ gerenciarProduto()\l+ gerenciarFuncionario()\l+ gerarRelatorio()\l+ gerenciarEstoque()\l+ gerenciarFornecedor()\l+ gerenciarPromocao()\l}')

    dot.node('Produto', '{Produto|+ idProduto: int\l+ nome: String\l+ descricao: String\l+ preco: float\l+ isbn: String (Livro)\l+ categoria: String\l- idFornecedor: int\l|+ atualizarInformacoes()\l+ verificarEstoque(): int\l}')
    dot.node('ItemEstoque', '{ItemEstoque|+ idItemEstoque: int\l+ quantidade: int\l+ localizacao: String\l|+ atualizarQuantidade(novaQtd: int)\l}')
    dot.node('Fornecedor', '{Fornecedor|+ idFornecedor: int\l+ nomeFantasia: String\l+ cnpj: String\l+ contato: String\l|+ cadastrar()\l+ atualizarDados()\l}')
    dot.node('Venda', '{Venda|+ idVenda: int\l+ dataHora: DateTime\l+ valorTotal: float\l- idCliente: int (opcional)\l- idFuncionario: int\l|+ adicionarItem(item: ItemVenda)\l+ calcularTotal(): float\l+ registrarPagamento(pag: Pagamento)\l}')
    dot.node('ItemVenda', '{ItemVenda|+ idItemVenda: int\l- idProduto: int\l+ quantidade: int\l+ precoUnitario: float\l+ subtotal: float\l|}')
    dot.node('Pagamento', '{Pagamento|+ idPagamento: int\l+ formaPagamento: Enum\l+ valor: float\l+ dataHora: DateTime\l+ status: Enum\l|+ processar()\l+ emitirComprovante()\l}')
    dot.node('Promocao', '{Promocao|+ idPromocao: int\l+ descricao: String\l+ dataInicio: Date\l+ dataFim: Date\l+ tipoDesconto: Enum\l+ valorDesconto: float\l|+ aplicarDesconto(produto: Produto): float\l}')

    # Relacionamentos
    # Herança
    dot.edge('Cliente', 'Pessoa', arrowhead='empty', label='herda de') # Seta de herança
    dot.edge('UsuarioSistema', 'Pessoa', arrowhead='empty', label='herda de')
    dot.edge('Funcionario', 'UsuarioSistema', arrowhead='empty', label='herda de')
    dot.edge('Gerente', 'UsuarioSistema', arrowhead='empty', label='herda de')

    # Associações / Agregações / Composições
    dot.edge('Venda', 'Cliente', label='', arrowhead='vee', tailport='e', headport='w')
    dot.edge('Venda', 'Funcionario', label='', arrowhead='vee', tailport='e', headport='w')
    dot.edge('Venda', 'ItemVenda', label='1 contém *', arrowhead='diamond', dir='forward') # Composição (preenchido se for direto)
    dot.edge('ItemVenda', 'Produto', label='1 refere-se a 1', arrowhead='vee')
    dot.edge('Venda', 'Pagamento', label='1 processa 1..*', arrowhead='vee') # Venda pode ter múltiplos pagamentos parciais, ou um

    dot.edge('Produto', 'Fornecedor', label='fornecido', arrowhead='vee', tailport='e', headport='w')
    dot.edge('ItemEstoque', 'Produto', label='', arrowhead='vee', tailport='e', headport='w') # Cada produto tem uma entrada de estoque (simplificado)
    dot.edge('Promocao', 'Produto', label='* aplica-se a *', arrowhead='vee', dir='both', edgetooltip='Relação M:N, geralmente tabela de junção') # Indicando M:N

    dot.render(filename='sgil_diagrama_classes', directory=output_directory, view=False)
    print(f"Diagrama de Classes gerado em: {os.path.join(output_directory, 'sgil_diagrama_classes.png')}")

def gerar_modelo_entidade_relacionamento():
    dot = graphviz.Digraph('SGIL_MER', comment='Modelo Entidade Relacionamento - SGIL', format='png')
    dot.attr(label='Modelo Entidade Relacionamento (MER) - SGIL', fontsize='20', rankdir='TB')
    dot.node_attr.update(shape='record', style='filled', fillcolor='lightsteelblue')

    # Entidades (Tabelas)
    dot.node('TB_CLIENTE', '{TB_CLIENTE |<pk> ID_CLIENTE (PK)\l| NOME\l CPF\l ENDERECO\l TELEFONE\l EMAIL\l HISTORICO_COMPRAS (TEXT)\l}')
    dot.node('TB_USUARIO', '{TB_USUARIO |<pk> ID_USUARIO (PK)\l| NOME\l CPF\l LOGIN\l SENHA_HASH\l NIVEL_ACESSO (FK para TB_NIVEL_ACESSO ou ENUM)\l TIPO_USUARIO (Enum: FUNCIONARIO, GERENTE)\l CARGO (se Funcionario)\l}') # Unificando Funcionario e Gerente
    dot.node('TB_PRODUTO', '{TB_PRODUTO |<pk> ID_PRODUTO (PK)\l| NOME\l DESCRICAO\l PRECO\l ISBN\l CATEGORIA\l<fk_forn> ID_FORNECEDOR (FK)\l}')
    dot.node('TB_ESTOQUE_ITEM', '{TB_ESTOQUE_ITEM |<pk_prod> ID_PRODUTO (PK, FK)\l| QUANTIDADE\l LOCALIZACAO\l}') # Rel 1:1 com Produto, ID_PRODUTO é PK e FK.
    dot.node('TB_FORNECEDOR', '{TB_FORNECEDOR |<pk> ID_FORNECEDOR (PK)\l| NOME_FANTASIA\l CNPJ\l CONTATO\l}')
    dot.node('TB_VENDA', '{TB_VENDA |<pk> ID_VENDA (PK)\l| DATA_HORA\l VALOR_TOTAL\l<fk_cli> ID_CLIENTE (FK, nullable)\l<fk_func> ID_USUARIO_FUNCIONARIO (FK)\l}')
    dot.node('TB_ITEM_VENDA', '{TB_ITEM_VENDA |<pk> ID_ITEM_VENDA (PK)\l|<fk_venda> ID_VENDA (FK)\l<fk_prod> ID_PRODUTO (FK)\l| QUANTIDADE\l PRECO_UNITARIO\l SUBTOTAL\l}')
    dot.node('TB_PAGAMENTO', '{TB_PAGAMENTO |<pk> ID_PAGAMENTO (PK)\l|<fk_venda> ID_VENDA (FK)\l| FORMA_PAGAMENTO\l VALOR\l DATA_HORA\l STATUS\l}')
    dot.node('TB_PROMOCAO', '{TB_PROMOCAO |<pk> ID_PROMOCAO (PK)\l| DESCRICAO\l DATA_INICIO\l DATA_FIM\l TIPO_DESCONTO\l VALOR_DESCONTO\l}')
    dot.node('TB_PROMOCAO_PRODUTO', '{TB_PROMOCAO_PRODUTO |<fk_promo> ID_PROMOCAO (PK, FK)\l|<fk_prod> ID_PRODUTO (PK, FK)\l}') # Tabela de Junção M:N

    # Relacionamentos (Chaves Estrangeiras)
    dot.edge('TB_PRODUTO:fk_forn', 'TB_FORNECEDOR:pk', label='  é fornecido por')
    dot.edge('TB_ESTOQUE_ITEM:pk_prod', 'TB_PRODUTO:pk', label='  refere-se a (1:1)')
    dot.edge('TB_VENDA:fk_cli', 'TB_CLIENTE:pk', label='  registra (0..1)')
    dot.edge('TB_VENDA:fk_func', 'TB_USUARIO:pk', label='  realizada por (1)') # Assumindo ID_USUARIO em TB_USUARIO
    dot.edge('TB_ITEM_VENDA:fk_venda', 'TB_VENDA:pk', label='  pertence a (1)')
    dot.edge('TB_ITEM_VENDA:fk_prod', 'TB_PRODUTO:pk', label='  contém (1)')
    dot.edge('TB_PAGAMENTO:fk_venda', 'TB_VENDA:pk', label='  efetuado para (1)')
    dot.edge('TB_PROMOCAO_PRODUTO:fk_promo', 'TB_PROMOCAO:pk', label='  detalha')
    dot.edge('TB_PROMOCAO_PRODUTO:fk_prod', 'TB_PRODUTO:pk', label='  aplicada em')

    # Para Cliente e UsuarioSistema, optei por uma TB_USUARIO mais genérica para Funcionário/Gerente e TB_CLIENTE separada,
    # já que clientes podem não ser usuários do sistema interno.

    dot.render(filename='sgil_mer', directory=output_directory, view=False)
    print(f"Modelo Entidade Relacionamento gerado em: {os.path.join(output_directory, 'sgil_mer.png')}")


if __name__ == '__main__':
    print("Gerando diagramas para o SGIL...\n")
    gerar_diagrama_casos_uso()
    gerar_diagrama_pacotes()
    gerar_diagrama_classes()
    gerar_modelo_entidade_relacionamento()
    print("\nTodos os diagramas foram gerados na pasta 'diagramas_sgil'.")