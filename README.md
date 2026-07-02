# 🎮 Jogo da Forca

Um clássico jogo da forca desenvolvido em **Python**, no qual o jogador tenta adivinhar uma palavra secreta, letra por letra, antes que suas tentativas se esgotem.

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Status](https://img.shields.io/badge/status-concluído-brightgreen)
![Licença](https://img.shields.io/badge/licença-MIT-lightgrey)

---

## 📋 Sobre o projeto

Este é um projeto simples e didático, ideal para praticar lógica de programação, manipulação de strings e estruturas de repetição em Python. A cada rodada, uma palavra é sorteada aleatoriamente de uma lista, e o jogador precisa descobri-la letra por letra antes de esgotar o número de tentativas.

## ✨ Funcionalidades

- 🎲 Escolha aleatória de palavras a partir de um arquivo de texto (`palavras.txt`)
- ❤️ Sistema de tentativas com contagem de erros
- 🔤 Feedback visual da palavra secreta, mostrando letras acertadas e espaços em branco para as ainda não descobertas
- 🏆 Mensagens de vitória ao completar a palavra corretamente
- 💀 Mensagem de derrota ao esgotar as tentativas
- ✅ Validação de entrada (evita letras repetidas ou caracteres inválidos)

## 🧰 Requisitos

- [Python 3.x](https://www.python.org/downloads/) instalado na máquina

Não há dependências externas — o jogo utiliza apenas bibliotecas nativas do Python.

## 🚀 Como executar

1. Clone este repositório ou baixe os arquivos do projeto:
   ```bash
   git clone https://github.com/seu-usuario/jogo-da-forca.git
   cd jogo-da-forca
   ```
2. Execute o jogo com o seguinte comando:
   ```bash
   python app.py
   ```

## 📁 Estrutura do projeto

```
jogo-da-forca/
├── app.py          # Lógica principal do jogo
├── palavras.txt    # Lista de palavras utilizadas pelo jogo
└── README.md        # Documentação do projeto
```

## 🕹️ Como jogar

1. O jogo escolhe automaticamente uma palavra secreta da lista em `palavras.txt`.
2. A palavra é exibida com traços (`_`) representando cada letra ainda não descoberta.
3. Digite uma letra por vez e pressione Enter.
4. Se a letra estiver na palavra, ela é revelada em sua posição correta.
5. Se a letra não estiver na palavra, uma tentativa é perdida.
6. O jogo termina quando:
   - ✅ Você descobre todas as letras da palavra (**vitória**), ou
   - ❌ Suas tentativas se esgotam (**derrota**).

## 🛠️ Personalização

Você pode adicionar ou remover palavras facilmente editando o arquivo `palavras.txt`, inserindo uma palavra por linha.

## 🤝 Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma *issue* ou enviar um *pull request* com melhorias, novas funcionalidades ou correções de bugs.

## 📄 Licença

Este projeto está sob a licença MIT. Consulte o arquivo `LICENSE` para mais detalhes.