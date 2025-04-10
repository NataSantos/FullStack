# Atividade Bônus (0,5 pontos)

## Informações Gerais
- **Participação**: Opcional (quem não entregar não será prejudicado)
- **Formato**: Individual, duplas ou trios
- **Entrega**: Todos devem postar a URL do projeto no GitHub
- **Como entregar**: Adicionar arquivo de texto com o link do GitHub na plataforma de entrega

## Descrição do Sistema
Desenvolva o painel administrativo de uma aplicação Django com relacionamento entre Produtos e Categorias de um restaurante.

### Modelos

#### Categoria
- **Nome da Categoria** (Exemplos: Pizza, Café, Burguer)

#### Produto
- **Nome do produto** (Exemplos: Pizza de Camarão, Café Cremoso, Burguer Triplo Capeado com Queijo)
- **Preço**
- **Descrição**
- **Categoria** (Chave Estrangeira)

### Requisitos do Painel Administrativo
- Exibir corretamente o nome do produto
- Exibir corretamente o nome da categoria
- Implementar filtro por Categoria

### Comandos
```bash
# Roda o server
python manage.py runserver
```