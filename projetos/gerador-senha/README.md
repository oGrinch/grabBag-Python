# Gerador de Senhas Aleatórias 🔐

Este é um programa simples, feito em **Python** para **gerar senhas fortes e aleatórias**, com base nas preferências do usuário.  
É voltado para **fins educacionais** e uso pessoal, utilizando bibliotecas padrão e interação com o usuário.

---

## ✨ Funcionalidades

O gerador permite ao usuário escolher e configurar:

- **Tamanho da senha** (até 60 caracteres, pode ser ajustado caso prefira)
- **Incluir ou não** os seguintes tipos de caracteres:
  - Letras **maiúsculas**
  - Letras **minúsculas**
  - **Números**
  - **Caracteres especiais** (como !, @, #, ...)

Além disso, também conta com:
- **Validação de entrada** com mensagens claras
- **Tratamento de erros** para evitar que entradas inválidas travem o programa

---

## 🚀 Como usar

Este código foi desenvolvido e testado no VSCode, mas pode ser executado em qualquer terminal com o Python 3 instalado.

### Etapas:

1. O terminal pedirá o número de caracteres desejado para a senha (máximo de 60).
2. Em seguida, serão feitas perguntas sobre quais tipos de caracteres devem ser incluídos.
3. Ao final, o programa exibirá a senha gerada aleatoriamente com base nas opções escolhidas.

Para sair, basta fechar o terminal ou interromper a execução (Ctrl+C).

---

## 💡 Aprendizados

Este projeto reforça o uso de conceitos fundamentais de **Python**, incluindo:

- **Importação de módulos padrão**, como `string`, e `random`
- **Estruturação do código com funções**, facilitando reutilização e leitura
- **Laços de repetição com `while True`** para garantir entrada válida do usuário
- **Condicionais** para lógica de controle (if, elif, else)
- **Tratamento de exceções com `try` / `except`**, evitando que o programa quebre com erros inesperados
- **Uso de operadores lógicos** e manipulação de strings para gerar combinações seguras

---

## ⚠️ Aviso

Embora este gerador funcione bem para aprendizado e uso casual, **não é recomendado para criação de senhas altamente sensíveis**, 
pois não faz uso de nenhum mecanismo de segurança criptográfica (como `secrets`, por exemplo, ou outros similares).

Para aplicações reais que exigem máxima segurança, recomenda-se o uso de bibliotecas como `secrets` ou `passlib`.

---
