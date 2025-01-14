# Usar imagem base Python "slim"
FROM python:3.9-slim

# Diretório de trabalho no container
WORKDIR /app

# Copia o arquivo main.py para dentro do container
COPY main.py /app/

# Comando para executar o scrip python
CMD ["python", "main.py"]