# Análise das Comissões

Um app bem simples que baixa e disponibiliza informação sobre os membros das comissões e os PLs e PECs que eles apresentaram nos últimos anos.

## Instalar
O crawler depende das seguintes bibliotecas python:
* lxml
    
Para rodar basta executar: 
    python crawler.py

Você pode editar o arquivo para adicionar outros tipos de proposições e outros anos (mas o sistema usa a base atual de parlamentares, então não faz muito sentido pegar anos anteriores.)

## Rodando
O app é basicamente um arquivo HTML e Javascript e não precisa de nada além disso para rodar.
Por razões de segurança do browser, talvez você não consiga rodar apenas abrindo o arquivo index.php

Utilize algum servidor HTML local.

Usando python você pode criar um executando:

    python -m SimpleHTTPServer 8080
    
E abrir o seu browser em [http://0.0.0.0:8080](http://0.0.0.0:8080)


## ToDo
* Disponibilizar mais informações sobre os PLs.
* Disponibilizar link para consultar diretamente o PL
* Mais informações sobre o parlamentar
* Buscar e exibir as atribuições da comissão
* Melhorar a visualização geral para facilitar a navegação entre os parlamentares
* Criar uma nuvem de palavras por parlamentar baseado nos projetos propostos
* Criar uma lista de stopwords comuns do tipo "Acrescenta", "Altera", "Da nova redação".
