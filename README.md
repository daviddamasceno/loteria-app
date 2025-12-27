# Sorteador Lotérico

Este é um projeto simples para gerar números de loteria de forma aleatória. É ideal para iniciantes que desejam entender como uma aplicação web moderna funciona, utilizando tecnologias como FastAPI para o backend, Vue.js para o frontend e Docker para containerização.

## Como funciona?

A aplicação possui uma interface web amigável onde você pode:

*   Definir o **range máximo** de números (por exemplo, 60 para a Mega-Sena).
*   Escolher **quantos números** deseja sortear.
*   Clicar em "Gerar Números" para ver os números da sorte.
*   Visualizar um **histórico** dos jogos gerados.
*   **Copiar** todo o histórico para colar em uma planilha ou onde preferir.

## Pré-requisitos

Para executar este projeto, você precisa ter o [Docker](https://www.docker.com/get-started) e o [Docker Compose](https://docs.docker.com/compose/install/) instalados em sua máquina.

## Como executar

Siga os passos abaixo para ter a aplicação rodando em seu ambiente local.

**1. Clone o repositório:**

```bash
git clone <URL_DO_SEU_REPOSITORIO>
```
*(Substitua `<URL_DO_SEU_REPOSITORIO>` pela URL do seu projeto no Git)*

**2. Acesse a pasta do projeto:**

```bash
cd loteria-app
```

**3. Inicie a aplicação com Docker Compose:**

Este comando irá construir a imagem Docker e iniciar o container em segundo plano (`-d`).

```bash
docker-compose up -d
```

**Pronto!** A aplicação estará disponível no seu navegador em: `http://localhost:80`

## Como usar

1.  Acesse `http://localhost:80` no seu navegador.
2.  Preencha os campos "Range Máximo" e "Quantos números sortear?".
3.  Clique em "Gerar Números".
4.  Os números sorteados aparecerão na tela e serão adicionados ao histórico à esquerda.
5.  Para copiar o histórico, clique no botão "Copiar Histórico".
