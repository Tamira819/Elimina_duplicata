import os
import shutil

# Caminhos para as pastas de destino e fotos
pasta_destino = r'C:/Users/TamiradeSenaAbo-gane/Documents/new_catalog/fotos2/55_INV25'
pasta_fotos = r'C:/Users/TamiradeSenaAbo-gane/OneDrive - LORE CONFECCOES LTDA/Fotos Coleção/55_LORE_INV25_E-commerce_1100x1540/Fotos'

# Função para copiar uma foto por referência limpa
def copiar_fotos_unicas(pasta_fotos, pasta_destino):
    # Cria a pasta de destino se ela não existir
    if not os.path.exists(pasta_destino):
        os.makedirs(pasta_destino)
        print(f"Pasta {pasta_destino} criada.")
    
    # Conjunto para armazenar referências já processadas
    referencias_processadas = set()

    # Percorre os arquivos na pasta
    for arquivo in os.listdir(pasta_fotos):
        if arquivo.endswith('_1.jpg') or arquivo.endswith('.jpeg'):
            referencia_completa = arquivo[6:13]  # Extrai a referência limpa (ex: BL41007)
                
            # Verifica se a referência já foi processada
            if referencia_completa and referencia_completa not in referencias_processadas:
                caminho_origem = os.path.join(pasta_fotos, arquivo)
                caminho_destino = os.path.join(pasta_destino, arquivo)
                    
                # Copia a imagem para a pasta de destino
                shutil.copy(caminho_origem, caminho_destino)
                print(f"Imagem {arquivo} copiada para {pasta_destino}.")
                    
                # Marca a referência como processada
                referencias_processadas.add(referencia_completa)

# Chamada da função
copiar_fotos_unicas(pasta_fotos, pasta_destino)

# Exibe o resultado
print("Processo concluído.")

