Um scraper de filmes do IMDb que extrai detalhes de filmes da página de rankings do site e salva as informações em um arquivo CSV.

Funcionalidades

- Extrai detalhes de filmes da página de rankings do IMDb
- Salva as informações em um arquivo CSV
- Utiliza threads para melhorar a performance da raspagem de dados
- Implementa um atraso aleatório entre as requisições para evitar ser bloqueado pelo site

Requisitos

- Python 3.x
- Bibliotecas:
    - requests
    - beautifulsoup4
    - csv
    - concurrent.futures

Uso

1. Clone o repositório
2. Execute o script main.py (ou o nome do arquivo que contém a função scrape_movies)
3. Os detalhes dos filmes serão salvos em um arquivo chamado movies.csv

Estrutura do Arquivo CSV

O arquivo CSV terá as seguintes colunas:

- Título do filme
- Data de lançamento
- Avaliação do filme
- Sinopse do filme

Observações

- O script utiliza um User-Agent para simular uma requisição de um navegador
- O script implementa um atraso aleatório entre as requisições para evitar ser bloqueado pelo site
- O número máximo de threads pode ser ajustado alterando o valor da variável MAX_THREADS
