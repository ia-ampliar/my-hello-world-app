# Usar Python 3.8 slim
FROM python:3.8-slim

# Instalar pacotes pré-compilados do OpenSlide e suas dependências
RUN apt-get update && apt-get install -y \
    libopenslide0 \
    python3-openslide \
    # Se quiser instalar as ferramentas CLI do OpenSlide, adicione:
    # openslide-tools \
    && rm -rf /var/lib/apt/lists/*

# Se quiser instalar boto3 e outras libs Python via pip
RUN pip install --no-cache-dir openslide-python boto3

# Cria um diretório de trabalho
WORKDIR /app

# Copia seu script
COPY main.py /app/

# Comando de entrada (executa o script)
CMD ["python", "main.py"]


