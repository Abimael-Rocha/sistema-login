# Sistema de Login Simples

Este projeto é um sistema de login simples em Python que utiliza MySQL para armazenar usuários e senhas. O projeto está configurado para ser executado em contêineres Docker e utiliza GitHub Actions para CI/CD.

## Estrutura de Pastas

/app

Dockerfile
app.py
requirements.txt
docker-compose.yml
.github
workflows
ci-cd.ym


## Pré-requisitos

- Docker
- Docker Compose
- Conta no Docker Hub
- Conta no GitHub

## Desenvolvimento

### Passos para Configurar o Ambiente de Desenvolvimento

1. **Clone o repositório:**

   ```sh
   git clone https://github.com/seu-usuario/seu-repositorio.git
   cd seu-repositorio
   
## Estrutura do Código

app.py: Código principal do sistema de login.
Dockerfile: Define a imagem Docker para a aplicação.
requirements.txt: Lista de dependências do Python.
docker-compose.yml: Configuração do Docker Compose para orquestrar os contêineres da aplicação e do banco de dados.
ci-cd.yml: Pipeline de CI/CD configurado para GitHub Actions.

## Implantação
Usando Docker

Construa a imagem Docker:

docker build -t login-app .

Execute a aplicação com Docker Compose:

docker-compose up --build

A aplicação estará rodando no terminal interativo.

## Usando GitHub Actions para CI/CD

Configure segredos no GitHub:

Vá para o repositório no GitHub.
Vá para Settings > Secrets and variables > Actions.
Adicione os segredos DOCKER_USERNAME e DOCKER_PASSWORD com suas credenciais do Docker Hub.
Pipeline de CI/CD:

O pipeline de CI/CD será acionado automaticamente em cada push ou pull request na branch main. Ele executa os seguintes passos:

Faz checkout do código.
Configura o Docker Buildx.
Faz login no Docker Hub.
Constrói a imagem Docker.
Sobe os serviços definidos no docker-compose.yml.
Aguarda o MySQL estar pronto para conexões.
Executa um teste básico.
Derruba os serviços do Docker Compose.

## Contribuição

Fork o repositório.
Crie uma branch para sua feature (git checkout -b feature/fooBar).
Commit suas mudanças (git commit -am 'Add some fooBar').
Push para a branch (git push origin feature/fooBar).
Crie um novo Pull Request.


Este `README.md` fornece uma visão geral completa do projeto, incluindo a estrutura das pastas, os pré-requisitos, as instruções de desenvolvimento e as instruções de implantação. Ele também inclui informações sobre como configurar o pipeline de CI/CD usando GitHub Actions e como contribuir para o projeto.



