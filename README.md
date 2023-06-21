# fake_phantom

**SIM**, o .env esta versionado, **SIM**, isso é errado e falha de segurança.

Mas...

Este projeto **não deve ser usado em prod**, ok??. (o.O)

## Objetivo

O objetivo deste projeto é fornecer umn simples endpoint para testes com requisições HTTP

Criadas:
- GET
- POST
- PUT

Pendentes:
- DELETE
- HEAD
- OPTIONS
- PATCH

## Modo de usar

### Com Docker/Docker Compose
```shell
docker-compose up --build
```
ou
```shell
docker-compose up --build --force-recreate
```
ou fazendo o build com o docker e usando sua imagem

### Sem Docker
#### Python 3.10 deve esta instalado.

Criando seu venv
```shell
python -m venv venv
```
Ative seu venv
```shell
# No Linux
./venv/bin/activate
# No Wndows com cmd
./venv/Scripts/Activate 
```
Instale os pacotes:
```shell
# Na raiz do projeto DIGITE:
pip install --upgrade pip
pip install -r ./requirements.txt
```
Execute o projeto
```shell
python ./endpointlocal.py
```