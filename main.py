import boto3
import openslide
import os
from urllib.parse import urlparse

def main():
    s3_tcga_name = 's3://tcga-completo/TCGA-3M-AB46/TCGA-3M-AB46-01A-01-TS1.E3B69170-C92D-4196-9DD5-F65762D4C700.svs'
    local_filename = 'temp.svs'

    # Faz parse do caminho S3 para obter bucket e key
    parsed = urlparse(s3_tcga_name, allow_fragments=False)
    bucket_name = parsed.netloc           # "tcga-completo"
    key_name = parsed.path.lstrip('/')    # "TCGA-3M-AB46/TCGA-3M-AB46-01A-01-TS1.E3B69170-C92D-4196-9DD5-F65762D4C700.svs"

    # Inicializa o cliente S3
    s3 = boto3.client('s3')

    # Baixa o arquivo para local
    s3.download_file(bucket_name, key_name, local_filename)

    # Abre com OpenSlide
    wsi = openslide.OpenSlide(local_filename)
    print("Level dimensions:", wsi.level_dimensions)
    wsi.close()

    # Remove o arquivo local
    os.remove(local_filename)

if __name__ == "__main__":
    main()
