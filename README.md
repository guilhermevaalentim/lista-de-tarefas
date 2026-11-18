# Lista de Tarefas 📋

Aplicação de linha de comando em Python para gerenciar tarefas direto no terminal. Projeto de estudo para praticar listas, dicionários, funções e tratamento de erros.

## Funcionalidades

- Adicionar tarefa
- Listar tarefas
- Remover tarefa pelo nome
- Tratamento de entradas inválidas no menu (letras, texto vazio e números fora das opções)
- Não aceita nome de tarefa em branco ao adicionar ou remover

## Tecnologias

- Python 3.12 ou superior

## Como executar

Pré-requisito: Python 3.12 ou superior instalado.

```bash
git clone https://github.com/guilhermevaalentim/lista-de-tarefas.git
cd lista-de-tarefas
python app.py     # Windows
python3 app.py    # Linux / macOS
```

## Como usar

Ao iniciar, o programa mostra o menu principal:

```
1. Adicionar Tarefa.
2. Listar Tarefas.
3. Remover Tarefa.
4. Sair.

Selecione uma opção:
```

Digite o número da opção desejada e siga as instruções na tela.

## Limitações e próximos passos

- [ ] Salvar as tarefas em arquivo (hoje voltam à lista inicial ao fechar o programa)
- [ ] Impedir tarefas com nomes repetidos
- [ ] Listar as tarefas numeradas e remover pelo número
- [ ] Tornar a limpeza de tela compatível com Linux e macOS (hoje usa `cls`)

## Autor

Guilherme Pereira Valentim
