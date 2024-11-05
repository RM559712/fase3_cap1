# FIAP - Faculdade de Informática e Administração Paulista

<p align="center">
<a href= "https://www.fiap.com.br/"><img src="assets/images/logo-fiap.png" alt="FIAP - Faculdade de Informática e Admnistração Paulista" border="0" width=40% height=40%></a>
</p>

<br>

# Agro-DOS - Alertas meteorológicos para plantio

## 👨‍👩 Grupo

Grupo de número <b>27</b> formado pelos integrantes mencionados abaixo.

## 👨‍🎓 Integrantes: 
- <a href="https://www.linkedin.com/in/cirohenrique/">Ciro Henrique</a> ( <i>RM559040</i> )
- <a href="javascript:void(0)">Enyd Bentivoglio</a> ( <i>RM560234</i> )
- <a href="https://www.linkedin.com/in/marcofranzoi/">Marco Franzoi</a> ( <i>RM559468</i> )
- <a href="https://www.linkedin.com/in/rodrigo-mazuco-16749b37/">Rodrigo Mazuco</a> ( <i>RM559712</i> )

## 👩‍🏫 Professores:

### Tutor(a) 
- <a href="https://www.linkedin.com/in/lucas-gomes-moreira-15a8452a/">Lucas Gomes Moreira</a>

### Coordenador(a)
- <a href="https://www.linkedin.com/in/profandregodoi/">André Godoi</a>

## 📜 Descrição

<b>Referência</b>: https://on.fiap.com.br/mod/assign/view.php?id=430788&c=11356

Essa versão possui funcionalidades que visam auxiliar o plantio de diferentes culturas através de alertas meteorológicos de acordo com a região desejada.

Algumas informações sobre os módulos dessa versão:

- Módulo "Culturas": Permite que sejam cadastradas diferentes culturas com seus respectivos ranges de parâmetros ideais (<i>mínimo e máximo</i>) para as medições de temperatura, umidade, velocidade do vento e quantidade de chuva.
- Módulo "Análises e alertas para plantio": A partir das culturas previamente cadastradas e parametrizadas, permite que sejam efetuadas análises com alertas para as medições de temperatura, umidade, velocidade do vento e quantidade de chuva
a partir de uma determinada localização ao redor do mundo. A localização pode ser definida através do nome da cidade, seguida das siglas de estado/província e país ou através da longitude e latitude do local desejado. Ao final, é disponibilizado um relatório detalhado contendo informações atualizadas para cada medição e uma análise final.

## 📁 Estrutura de pastas

Dentre os arquivos e pastas presentes na raiz do projeto, definem-se:

<PENDENTE>

1. <b>assets</b>: Diretório para armazenamento de arquivos complementares da estrutura do sistema.
    - Diretório "images": Diretório para armazenamento de imagens.

2. <b>config</b>: Diretório para armazenamento de arquivos em formato <i>json</i> contendo configurações.
    - Arquivo "db.json": Configurações destinadadas à conexão com banco de dados.
    - Arquivo "params.json": Configurações do sistema em geral.

3. <b>document</b>: Diretório para armazenamento de documentos relacionados ao sistema.

4. <b>scripts</b>: Diretório para armazenamento de scripts.
    - Diretório "oracle": Diretório para armazenamento de scripts do banco de dados Oracle.
        - Arquivo "CROP.sql": Scripts da tabela "CROP".
        - Arquivo "CROP_SEQ.sql": Scripts do <i>sequencial</i> da coluna "CRP_ID".
        - Arquivo "queries.sql": Scripts genéricos do banco de dados.
        - Arquivo "TRIGGER_CRP_ID.sql": Scripts da <i>trigger</i> da coluna "CRP_ID".
        - Arquivo "TRIGGER_CRP_UPDATE_DATE.sql": Scripts da <i>trigger</i> da coluna "CRP_UPDATE_DATE".

5. <b>src</b>: Diretório para armazenamento de código fonte do sistema em Python.
    - Diretório "custom": Diretório para armazenamento <i>classes/componentes</i> auxiliares do sistema.
    - Diretório "models": Diretório para armazenamento <i>classes/componentes</i> relacionados ao banco de dados.
    - Diretório "prompt": Diretório para armazenamento arquivos de inicialização do sistema em formato <i>prompt</i>.

6. <b>README.md</b>: Documentação do sistema em formato markdown.

## 🔧 Como executar o código

Como se trata de uma versão em formato <i>prompt</i>, para execução das funcionalidades, os seguintes passos devem ser seguidos:

1. Utilizando algum editor de código compatível com a linguagem de programação Python (<i>VsCode, PyCharm, etc.</i>), acesse o diretório "./src/prompt".
2. Neste diretório, basta abrir o arquivo "main.py" e executá-lo.

Para essa versão não são solicitados parâmetros para acesso como por exemplo <i>username</i>, <i>password</i>, <i>token access</i>, etc.

## 🗃 Histórico de lançamentos

* 1.0.0 - 15/10/2024

## 📋 Licença

Desenvolvido pelo Grupo 27 para o projeto da fase 2 (<i>Cap 6 - Python e além</i>) da <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://fiap.com.br">Fiap</a>. Está licenciado sobre <a href="http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution 4.0 International</a>.</p>