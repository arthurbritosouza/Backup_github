<h1>Sistema de Backup Automático e Upload para o GitHub</h1>

<p>
Este script em Python realiza backups automáticos de projetos armazenados em uma pasta específica e faz o upload para repositórios no GitHub. Ele é ideal para quem deseja automatizar o gerenciamento de backups de código e garantir a segurança dos arquivos.
</p>

<h2>Funcionalidades</h2>
<ul>
  <li><strong>Cálculo do tamanho das pastas:</strong> Verifica se o projeto está dentro do limite de 2GB.</li>
  <li><strong>Cópia automática de projetos:</strong> Copia os projetos para uma pasta de backup.</li>
  <li><strong>Integração com GitHub:</strong> Inicializa o repositório Git, configura o remoto e faz o push automático.</li>
  <li><strong>Detecção de conflitos:</strong> Identifica e alerta sobre conflitos ao realizar o pull do repositório.</li>
</ul>

<h2>Pré-requisitos</h2>
<p>Certifique-se de que você tenha os seguintes itens instalados e configurados no seu ambiente:</p>
<ol>
  <li><strong>Python:</strong> Versão 3.8 ou superior.</li>
  <li><strong>Git:</strong> Configurado no ambiente de linha de comando.</li>
  <li><strong>Token de autenticação do GitHub:</strong> Para autenticação ao fazer push para o repositório remoto.</li>
</ol>

<h2>Estrutura do Projeto</h2>
<pre>
meu_projeto_backup/
├── script_backup.py  # O script principal que realiza o backup e upload
├── pasta_de_projetos/  # Pasta contendo os projetos a serem processados
└── pasta_de_backup/  # Pasta onde os backups serão armazenados
</pre>

<h2>Configuração</h2>
<ol>
  <li><strong>Clone ou crie o script:</strong> Certifique-se de salvar o script <code>script_backup.py</code> em um diretório no seu sistema.</li>
  <li><strong>Atualize os caminhos no script:</strong>
    <ul>
      <li><code>path_documents</code>: O caminho para a pasta onde estão os seus projetos.</li>
      <li><code>path_arquivos</code>: O caminho para a pasta onde os backups serão armazenados.</li>
    </ul>
  </li>
  <li><strong>Configure o repositório remoto:</strong>
    Substitua o campo <code>Repositório Git com o token de authenticação</code> pelo URL do seu repositório GitHub no formato:
    <pre>https://&lt;seu_token&gt;@github.com/&lt;seu_usuario&gt;/&lt;nome_do_repositorio&gt;.git</pre>
  </li>
</ol>

<h2>Como Usar</h2>
<ol>
  <li><strong>Execute o script:</strong>
    Rode o seguinte comando no terminal para executar o script:
    <pre>python script_backup.py</pre>
  </li>
  <li><strong>Acompanhe o processo:</strong>
    <ul>
      <li>O script verificará o tamanho das pastas.</li>
      <li>Copiará as pastas válidas para o diretório de backup.</li>
      <li>Inicializará o repositório Git (se necessário).</li>
      <li>Fará o commit e o push das alterações para o repositório remoto.</li>
    </ul>
  </li>
  <li><strong>Mensagens de status:</strong>
    O script exibirá mensagens indicando o progresso e quaisquer erros ou conflitos que precisem de atenção.
  </li>
</ol>

<h2>Detalhes Técnicos</h2>

<h3>Limite de Tamanho</h3>
<p>O script usa a função <code>get_directory_size</code> para calcular o tamanho de cada pasta. Se o tamanho exceder 2GB, o arquivo será ignorado e o nome será exibido no terminal.</p>

<h3>Processo de Backup</h3>
<ul>
  <li>Pastas válidas são copiadas para o diretório de backup usando a biblioteca <code>shutil</code>.</li>
  <li>O repositório Git é inicializado no diretório de backup, se ainda não existir.</li>
  <li>As alterações são commitadas e enviadas para o GitHub automaticamente.</li>
</ul>

<h3>Tratamento de Conflitos</h3>
<p>Se ocorrerem conflitos ao executar o <code>git pull</code>, o script aborta o merge automaticamente e alerta para a necessidade de resolução manual.</p>

<h2>Exemplo de Saída</h2>
<pre>
Arquivo projeto1 foi adicionado ao backup.
Backup realizado com sucesso!
Repositório iniciado com sucesso!
Remote configurado com sucesso.
Alterações locais commitadas.
Pull realizado com sucesso!
Push realizado com sucesso!
Arquivo Subido projeto1!
------------------------------------------------------------
</pre>

<h2>Observações</h2>
<ul>
  <li>Certifique-se de que o token do GitHub tenha permissões adequadas para leitura e gravação no repositório.</li>
  <li>O script assume que o branch principal é chamado <code>main</code>. Se o seu branch principal tiver outro nome, atualize o script.</li>
</ul>
