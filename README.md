# 🎮 Jogo da Forca

Um jogo da forca simples desenvolvido em **Python**, onde o jogador tenta descobrir uma palavra secreta letra por letra antes de acabar suas tentativas.

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Status](https://img.shields.io/badge/status-concluído-brightgreen)

---

## 📋 Sobre o projeto

Este projeto é uma versão interativa do clássico jogo da forca, criada para praticar lógica de programação, manipulação de strings e controle de fluxo em Python. O jogo apresenta um menu inicial, regras acessíveis e dificuldade ajustável.

## ✨ Funcionalidades atuais

- 🎮 Menu inicial com opções: jogar, ver regras e sair
- 🧠 Três níveis de dificuldade: fácil, médio e difícil
- 🔤 Escolha aleatória de palavras a partir de `palavras.txt`
- ✅ Validação de entrada para aceitar apenas letras válidas
- 🚫 Bloqueio de letras repetidas, com aviso claro ao jogador
- 🔁 Permite reiniciar uma nova partida sem fechar o programa
- 🎉 Exibe a palavra secreta de maneira amigável ao final da partida

## 🧰 Requisitos

- [Python 3.x](https://www.python.org/downloads/) instalado na máquina

Nenhuma dependência externa é necessária: o jogo usa apenas bibliotecas padrão do Python.

## 🚀 Como executar

1. Abra um terminal na pasta do projeto:
   ```bash
   cd c:\Projetos\jogo-da-forca
   ```
2. Execute o jogo:
   ```bash
   python app.py
   ```

## 📁 Estrutura do projeto

```
jogo-da-forca/
├── app.py          # Lógica principal do jogo
├── palavras.txt    # Lista de palavras utilizadas pelo jogo
├── regras.txt      # Regras do jogo exibidas no menu
└── README.md       # Documentação do projeto
```

## 🕹️ Como jogar

1. Escolha a opção "Jogar" no menu inicial.
2. Selecione o nível de dificuldade: fácil, médio ou difícil.
3. A palavra secreta será escolhida automaticamente.
4. Digite uma letra por vez e pressione Enter.
5. Se a letra estiver correta, ela é revelada na palavra.
6. Se a letra não estiver correta, você perde uma tentativa.
7. O jogo termina quando:
   - ✅ Você adivinha toda a palavra, ou
   - ❌ Suas tentativas se esgotam.

## 🛠️ Personalização

- Adicione ou remova palavras no arquivo `palavras.txt`, uma palavra por linha.
- Edite `regras.txt` para alterar o texto exibido na opção de regras.

## 🤝 Contribuindo

Contribuições são bem-vindas! Abra uma *issue* ou envie um *pull request* com melhorias, novas funcionalidades ou correções.

## 📄 Licença

Este projeto está disponível sob a licença MIT.
