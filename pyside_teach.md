
# Teach: PySide6 GUI Development

Bem-vindo. Este é um material em áudio derivado da skill PySide6. Cada faixa cobre um conceito independente. Você pode ouvir em qualquer ordem.

---

# 1. Instalação

Nesta faixa você vai aprender o que é o PySide6, por que ele é a escolha certa para projetos comerciais e como configurar o ambiente de desenvolvimento do zero.

O PySide6 é o binding oficial do Python para o framework Qt 6, mantido pela The Qt Company. Um binding é a ponte que permite chamar código Qt, escrito em C++, a partir do Python. O ponto mais importante sobre o PySide6 é sua licença, a LGPL, ou Library General Public License. Com ela, você pode usar o PySide6 em aplicações comerciais sem pagar royalties. A alternativa mais conhecida, o PyQt6, exige uma licença comercial separada para projetos proprietários. Para qualquer projeto que possa ser comercializado, prefira o PySide6.

Em seguida, o primeiro passo de qualquer projeto é criar um ambiente virtual. Um ambiente virtual isola as dependências do projeto, evitando conflitos com outras instalações Python na mesma máquina. O Python moderno já inclui a ferramenta para criar ambientes virtuais. A regra é simples: sempre use ambiente virtual. Nunca instale o PySide6 diretamente no Python do sistema.

Com o ambiente virtual ativado, a instalação do PySide6 é feita pelo gerenciador de pacotes pip, com o pacote de nome PySide6. A instalação traz automaticamente três componentes: os essenciais do Qt, os módulos adicionais e o shiboken6, que é a camada de conversão entre Python e C++. Você não precisa instalar esses componentes separadamente.

Um ponto sobre versões: o PySide6 requer Python na versão 3.9 ou superior. Para ambientes de produção, fixe a versão mínima e máxima do PySide6 no arquivo de requisitos do projeto. Isso garante que atualizações automáticas não quebrem a aplicação. A prática recomendada é indicar que a versão deve ser igual ou superior à 6.7, mas inferior à 7.

Com esses passos, seu ambiente está pronto para desenvolver com PySide6.

---

# 2. Imports Essenciais

Nesta faixa você vai aprender como o PySide6 organiza suas classes em módulos e por que a forma de importá-las afeta a manutenibilidade do código.

O PySide6 divide suas classes em módulos separados. Cada módulo agrupa funcionalidades relacionadas. Essa separação permite que apenas o necessário seja carregado na inicialização da aplicação.

Os três módulos mais usados são o QtCore, o QtWidgets e o QtGui. O QtCore é o núcleo invisível da aplicação. Ele contém sinais e slots, timers, threads, o loop de eventos e tipos básicos. O QtWidgets reúne todos os elementos visuais da interface. Botões, rótulos, campos de texto e layouts vivem nesse módulo. O QtGui cuida da apresentação visual. Fontes, ícones, cores, eventos de teclado e a ferramenta de desenho QPainter pertencem a ele.

Além dos três centrais, existem módulos especializados. O QtSql conecta a aplicação a bancos de dados. O QtNetwork gerencia requisições HTTP e conexões de rede. O QtMultimedia lida com áudio e vídeo. O QtCharts oferece componentes para visualizações e gráficos.

A regra principal sobre como importar é ser explícito. Liste por nome cada classe que o módulo realmente usa. Essa prática torna as dependências rastreáveis e evita conflitos de nomes entre módulos.

Um erro comum é importar tudo de um módulo usando o asterisco. Em projetos de produção, essa prática é proibida. Ela polui o espaço de nomes e torna impossível identificar de onde cada classe vem.

Com módulos bem escolhidos e imports explícitos, o código comunica intenção. Qualquer desenvolvedor que abrir o arquivo saberá exatamente quais dependências aquele módulo possui.

---

# 3. Estrutura da Aplicação

Nesta faixa você vai entender como uma aplicação Qt é organizada por dentro. Vamos ver o que é o event loop, como criar sua primeira janela no estilo orientado a objetos e como estruturar os arquivos do projeto.

O coração de qualquer aplicação Qt é o event loop. Quando você chama o método de execução do objeto QApplication, o programa entra em um laço. Esse laço fica aguardando eventos do sistema operacional, como cliques do mouse, pressionamentos de tecla ou notificações de timer. Cada evento é despachado ao objeto correto. O programa permanece nesse estado até que o usuário feche a janela.

Há duas regras absolutas sobre o QApplication. Primeiro, deve existir exatamente uma instância por processo. Segundo, essa instância deve ser criada antes de qualquer widget. Violar qualquer uma dessas regras causa falha imediata na inicialização.

A forma mais simples de criar uma aplicação é no estilo script: criar o QApplication, criar um widget, chamar show e iniciar o event loop. Essa abordagem funciona para experimentos rápidos. Para qualquer coisa além de um protótipo, ela não escala.

A forma recomendada é o estilo orientado a objetos. Você cria uma classe que herda de QWidget ou de QMainWindow. O construtor chama o construtor pai com super e em seguida chama um método privado de inicialização da interface. O programa principal cria uma instância dessa classe, chama show e inicia o event loop. Esse padrão separa a construção da interface da lógica de execução.

Ao inicializar o QApplication, configure também o nome da aplicação, o nome da organização e o domínio. Essas três propriedades são usadas automaticamente pelo sistema de configurações persistentes do Qt. Se você não as definir, o sistema de configurações precisará de parâmetros manuais em cada uso.

Vamos agora falar sobre a organização dos arquivos do projeto. Em um projeto pequeno, um único arquivo é aceitável. Em qualquer projeto que crescerá, separe as responsabilidades em pastas distintas. A pasta de views contém as classes de janela e os arquivos de interface visual. A pasta de models contém os dados e as regras de negócio. A pasta de controllers coordena a lógica entre views e models. A pasta de resources guarda imagens e folhas de estilo. A pasta de utils abriga funções auxiliares.

Uma convenção importante sobre nomenclatura: o nome do arquivo deve corresponder ao nome da classe. Um arquivo chamado settings dialog ponto py deve conter uma classe chamada SettingsDialog. Isso permite localizar qualquer classe pelo nome do arquivo sem precisar abrir o projeto.

A regra final é sobre caminhos de arquivo. Nunca use caminhos absolutos dentro do projeto. Use sempre caminhos relativos à raiz do projeto. Caminhos absolutos quebram quando o projeto é movido de pasta ou executado em outra máquina.

Resumindo: o event loop é o mecanismo central de toda aplicação Qt. Use o estilo orientado a objetos desde o início. Configure o nome e a organização no QApplication. Organize os arquivos em pastas por responsabilidade.

---

# 4. QWidget — Propriedades e Métodos

Nesta faixa você vai aprender o que é o QWidget, quais propriedades ele controla e como usá-lo para posicionar, exibir e personalizar qualquer elemento da interface.

O QWidget é a classe base de todo elemento visual no Qt. Cada botão, rótulo ou campo de texto herda diretamente do QWidget. Ele define uma área retangular na tela, gerencia sua própria pintura e recebe eventos de entrada do usuário. Quando um widget não tem pai, ele aparece como uma janela independente. Quando tem pai, ele é embutido na área desse pai.

O primeiro grupo de funcionalidades é o controle de geometria. É possível definir o título da janela, a posição na tela e as dimensões em chamadas separadas ou em conjunto. O QWidget também aceita limites mínimos e máximos de tamanho, controlando o quanto o usuário pode redimensionar a janela. Quando um tamanho fixo é definido, o redimensionamento fica completamente bloqueado.

Em seguida, há os controles de visibilidade. Os métodos de exibir e ocultar um widget são diretos. Há dois métodos para forçar um redesenho da interface. O primeiro redesenha imediatamente. O segundo agenda o redesenho para o próximo ciclo do event loop. A regra é sempre preferir o método que agenda, pois ele é mais eficiente.

O terceiro grupo é o controle de foco de teclado. É possível conceder ou remover o foco de um widget por código. A política de foco define se o widget aceita foco via teclado, via clique do mouse, ou por ambos. Para campos interativos, a política forte é a mais comum, pois aceita as duas formas.

Vamos ao ícone da janela. O QIcon é a classe que representa ícones no Qt. Para definir o ícone da janela, basta carregar um arquivo de imagem pelo caminho relativo ao diretório de trabalho. Em sistemas com tema de ícones, é possível usar um ícone padrão do sistema pelo seu nome. Os modos do ícone, como normal, desabilitado, ativo e selecionado, permitem que a interface reaja visualmente ao estado do elemento.

Os tooltips são textos de ajuda exibidos quando o usuário mantém o cursor sobre um elemento. O texto aceita HTML básico, ou seja, marcação de hipertexto simples, incluindo tags como negrito. A fonte dos tooltips pode ser configurada globalmente para toda a aplicação.

Para centralizar uma janela na tela, o procedimento envolve três etapas. Primeiro, obter a geometria disponível do monitor principal. Segundo, calcular o ponto central desse retângulo. Terceiro, mover a janela para que seu centro coincida com o centro da tela. A regra é executar esse procedimento antes de exibir a janela.

Por fim, os cursores. O QWidget permite trocar o cursor do mouse quando o ponteiro está sobre o widget. Há cursores padrão para estados como carregamento e seleção. O método para restaurar o cursor original desfaz qualquer personalização definida anteriormente.

Resumindo: o QWidget é a fundação de toda interface Qt. Dominar suas propriedades de geometria, visibilidade e foco é o ponto de partida para controlar qualquer elemento visual da aplicação.

---

# 5. QMainWindow

Nesta faixa você vai aprender como estruturar a janela principal de uma aplicação profissional. O QMainWindow oferece zonas pré-construídas para cada elemento da interface. Você vai entender como cada zona funciona e qual é a regra essencial para persistir o layout entre sessões.

O QMainWindow vai além de um simples widget de janela. Ele organiza a interface em cinco zonas fixas. A barra de menus fica no topo. Uma ou mais barras de ferramentas ficam logo abaixo. O widget central ocupa a área principal de trabalho. Os dock widgets encaixam nas laterais. E a barra de status fica no rodapé. Essa estrutura pré-definida elimina a necessidade de compor o layout manualmente.

O widget central é obrigatório. Sem ele, a janela não está completa. Ele pode ser qualquer widget: um editor de texto, uma lista ou uma área de desenho personalizada. Você o define chamando setCentralWidget no construtor da janela.

A barra de status exibe mensagens de contexto ao usuário. O método showMessage recebe o texto e um tempo em milissegundos. Quando o tempo acaba, a mensagem desaparece. Para exibir informação permanente, como o número de versão do programa, use addPermanentWidget com um QLabel. Esse widget fica fixo do lado direito e não é substituído por mensagens temporárias.

Em seguida, vem o conceito central dos menus: a QAction. Uma ação representa uma operação da aplicação, como abrir um arquivo, salvar ou copiar. Você cria a ação uma vez e a adiciona tanto ao menu quanto à barra de ferramentas. Isso evita duplicação de código. Cada ação pode ter um ícone, um texto de exibição, um atalho de teclado e uma dica para a barra de status.

Para os atalhos de teclado, o Qt fornece constantes padronizadas dentro da classe QKeySequence. Use sempre essas constantes em vez de escrever strings como Ctrl mais S diretamente. A razão é simples: o Qt adapta as constantes ao sistema operacional atual. O atalho de desfazer, por exemplo, é Ctrl mais Z no Windows e no Linux, e Command mais Z no macOS. Com as constantes, o código funciona corretamente em todas as plataformas sem modificação.

Veja agora as barras de ferramentas. Elas são criadas com o método addToolBar. Além de receber ações, uma toolbar também aceita widgets comuns, como um campo de busca. Você pode definir em quais bordas da janela a barra pode ser posicionada e se o usuário tem permissão para movê-la.

Os dock widgets são painéis que podem ser encaixados nas laterais da janela ou destacados como janelas flutuantes independentes. Você define em quais bordas cada dock pode ser posicionado com setAllowedAreas.

A regra mais importante ao trabalhar com toolbars e dock widgets é sempre atribuir um nome único com setObjectName. Esse nome é exigido pelo Qt para salvar e restaurar o estado da interface entre sessões. Sem ele, o Qt não consegue identificar cada elemento ao restaurar. Para salvar, chame saveGeometry e saveState no evento de fechamento da janela. Para restaurar, chame restoreGeometry e restoreState na inicialização. Um equívoco frequente é esquecer o setObjectName e perceber o problema somente quando o layout não é restaurado entre execuções.

Resumindo: o QMainWindow fornece a estrutura completa de uma janela profissional. O widget central é obrigatório. A QAction centraliza a lógica de operações e é compartilhada entre menus e barras de ferramentas. As constantes de QKeySequence garantem atalhos portáveis entre plataformas. E o setObjectName é essencial para persistir a geometria e o estado da interface.

---

# 6. Qt Style Sheets (QSS)

Nesta faixa você vai aprender como personalizar a aparência de uma aplicação Qt usando folhas de estilo, sem tocar na lógica do programa.

O QSS, ou Qt Style Sheets, usa uma sintaxe muito próxima do CSS, a linguagem de estilos usada na web. Ele permite separar a aparência visual da aplicação do código de comportamento. Essa separação é importante porque a equipe de design pode ajustar cores, fontes e bordas sem precisar entender o código Python.

Há duas formas de aplicar um estilo. A primeira é global: você chama setStyleSheet no objeto QApplication, e o estilo afeta todos os widgets da aplicação. A segunda é local: você chama setStyleSheet em um widget específico, e o estilo se aplica somente a ele e sobrepõe o estilo global. Combine as duas: defina o tema geral no QApplication e personalize exceções em widgets individuais.

Vamos falar sobre seletores. O seletor mais simples é por tipo de widget. Você escreve o nome da classe, como QPushButton, seguido das propriedades entre chaves. Tudo que for um QPushButton vai receber aquele estilo. O segundo seletor é por nome de objeto. Você atribui um nome ao widget com setObjectName e depois referencia esse nome no estilo usando o caractere de hash. Isso é ideal para estilizar elementos específicos sem afetar outros widgets do mesmo tipo. O terceiro seletor é por propriedade dinâmica. Você define uma propriedade no widget com setProperty e a usa como filtro no QSS. Quando a propriedade muda em tempo de execução, é necessário forçar o Qt a reavaliar o estilo chamando unpolish e polish no widget. Caso contrário, o estilo novo não será aplicado.

Os pseudo-estados são uma das funcionalidades mais poderosas do QSS. Eles permitem definir estilos diferentes para estados interativos do widget, sem escrever nenhum código Python adicional. O pseudo-estado hover aplica o estilo quando o cursor está sobre o widget. O pressed aplica quando o botão é pressionado. O disabled aplica quando o widget está desabilitado. O focus aplica quando o widget tem o foco de teclado. E o checked aplica para checkboxes e radio buttons quando estão marcados.

Para projetos de médio e grande porte, a boa prática é manter os estilos em um arquivo separado com extensão qss. No código Python, você abre esse arquivo e passa seu conteúdo para setStyleSheet. Isso mantém o código Python limpo e permite trocar o tema inteiro trocando apenas um arquivo.

Há também uma forma rápida de implementar um tema escuro sem escrever muito QSS. Você define o estilo da aplicação como Fusion, que é o estilo multiplataforma do Qt, e depois cria uma paleta personalizada. A paleta define as cores para cada função visual: o fundo da janela, o texto, a cor base dos campos de entrada, a cor dos botões e a cor de destaque para itens selecionados. Ao aplicar a paleta ao QApplication, toda a aplicação muda de tema.

Por fim, os sub-controles permitem estilizar partes internas de widgets compostos. Um QSpinBox, por exemplo, tem botões de incremento e decremento que são sub-controles. Você os referencia com dois dois-pontos seguidos do nome do sub-controle. Dentro do estilo, você define a origem da área de referência e a posição do elemento dentro dela.

Resumindo: o QSS é a ferramenta para separar aparência de lógica. Aplique estilos globais no QApplication e estilos específicos por nome de objeto. Use pseudo-estados para comportamentos interativos. Carregue folhas de estilo de arquivo para facilitar manutenção. E para temas escuros, combine o estilo Fusion com uma paleta personalizada.

---

# 7. Layout Management

Nesta faixa você vai aprender por que o posicionamento absoluto de widgets deve ser evitado e como usar os gerenciadores de layout do Qt para criar interfaces que se adaptam a qualquer ambiente.

A ideia central dos gerenciadores de layout é simples. Em vez de dizer ao Qt onde exatamente cada widget deve ficar na tela, você descreve as relações entre os widgets. O Qt calcula automaticamente a posição e o tamanho de cada elemento. Quando a janela é redimensionada, a interface se ajusta sozinha. Quando a fonte do sistema muda ou a densidade de pixels por polegada, chamada de DPI, é diferente, os elementos se reorganizam corretamente.

Isso contrasta com o posicionamento absoluto. Com ele, cada widget recebe coordenadas e dimensões fixas em pixels. O resultado parece correto no ambiente de desenvolvimento. Mas quebra em qualquer tela com resolução diferente, em sistemas com fontes maiores ou quando a janela é simplesmente redimensionada. Use posicionamento absoluto apenas para protótipos que não precisam ser mantidos.

O primeiro gerenciador de uso geral é o QHBoxLayout, que organiza widgets em uma linha horizontal. Para organização vertical, usa-se o QVBoxLayout. Os dois funcionam da mesma forma, apenas em eixos diferentes. Você adiciona widgets ao layout chamando o método de adição. Ao final, atribui o layout ao widget chamando setLayout.

Um recurso essencial desses dois gerenciadores é o espaço elástico, chamado de stretch. Quando adicionado entre widgets, ele ocupa todo o espaço livre não pertencente a nenhum widget. Esse é o mecanismo para empurrar um botão até a extremidade da janela ou distribuir widgets uniformemente. O fator de estiramento define quanto espaço cada widget ocupa quando a janela cresce. Ele é passado como segundo argumento ao método de adição do widget.

Em seguida, o QGridLayout organiza widgets em uma grade de linhas e colunas. Cada widget é inserido informando sua linha e sua coluna. Um widget pode ocupar mais de uma linha ou mais de uma coluna ao mesmo tempo. É possível definir qual coluna ou linha deve crescer quando a janela é ampliada.

O QFormLayout é especializado para formulários com pares de rótulo e campo. Você adiciona cada par informando o texto do rótulo e o widget do campo juntos. O Qt cuida do alinhamento entre rótulos e campos, adaptando o estilo visual à plataforma atual.

Para interfaces com múltiplas páginas, usa-se o QStackedWidget. Ele mantém vários widgets empilhados e exibe apenas um de cada vez. Você alterna entre páginas pelo índice numérico ou pelo próprio widget. O padrão mais comum é conectar o QStackedWidget a um seletor. Quando o usuário muda a seleção, a página troca automaticamente.

Por fim, o QSplitter divide a área da janela em regiões redimensionáveis pelo usuário. O usuário arrasta a divisória para redistribuir o espaço entre os painéis. É possível definir tamanhos iniciais para cada painel e indicar qual deles deve crescer prioritariamente.

A regra central é: nunca use posicionamento absoluto em código de produção. Escolha o gerenciador pela estrutura que está construindo. Linha ou coluna simples pedem QHBoxLayout ou QVBoxLayout. Grade com widgets de tamanhos variados pede QGridLayout. Formulário pede QFormLayout. Páginas alternadas pedem QStackedWidget. Painéis redimensionáveis pelo usuário pedem QSplitter.

Resumindo: gerenciadores de layout descrevem relações, não coordenadas fixas. Com eles, a interface se adapta automaticamente a qualquer tela ou configuração do sistema.

---

# 8. Sinais e Slots

Nesta faixa você vai aprender o mecanismo central de comunicação do Qt. Sinais e slots permitem que objetos troquem mensagens sem se conhecer diretamente. Esse princípio é chamado de baixo acoplamento.

Um sinal é emitido quando algo acontece. Quando o usuário clica um botão, o botão emite seu sinal de clique. Um slot é qualquer função que reage a esse sinal.

A conexão entre sinal e slot é estabelecida em tempo de execução. Você chama o método de conexão no sinal e passa o slot como argumento. O Qt cuida do despacho. Para desfazer a conexão, use o método de desconexão com o mesmo slot. Para remover todos os slots de uma vez, chame desconexão sem argumento.

Essa arquitetura permite sincronizar widgets sem que um conheça o tipo do outro. Por exemplo, o sinal de mudança de valor de um controle giratório pode se conectar diretamente ao slot de definir valor de um contador numérico. Os dois se sincronizam automaticamente.

Vamos agora aos sinais personalizados. Para criar um sinal próprio, declare-o como atributo de classe, usando a classe Signal com o tipo que ele vai carregar. Um sinal sem argumento notifica que um evento ocorreu. Um sinal com inteiro comunica um progresso. Um sinal com string entrega um resultado. Para disparar o sinal, chame o método emit com o valor correspondente.

O decorator Slot é opcional no PySide6. Quando adicionado a um método, ele declara o tipo esperado do argumento. Isso melhora o desempenho e facilita a introspecção interna do Qt. A recomendação é usá-lo em slots que recebem tipos específicos e são chamados frequentemente.

Há uma regra importante sobre onde sinais são declarados. Sinais são atributos de classe, não de instância. Você os declara no corpo da classe, fora do construtor. Quando acessa o sinal via self, o PySide6 o promove automaticamente para um descritor de instância. Cada instância opera seu próprio sinal sem interferir nas outras.

As combinações de conexão são flexíveis. Um sinal pode se conectar a vários slots. Vários sinais podem apontar para o mesmo slot. Um sinal pode se conectar a outro sinal, encadeando notificações. Se o sinal carrega mais argumentos do que o slot espera, os excedentes são descartados.

Em seguida, um recurso para evitar loops de sinalização. Quando dois controles estão sincronizados entre si, alterar um dispara o sinal do outro, que por sua vez dispara o primeiro, criando um ciclo infinito. O método blockSignals suspende os sinais de um objeto temporariamente. Passe verdadeiro para suspender e falso para restaurar. Use esse padrão sempre que dois controles forem sincronizados em ambas as direções.

A regra sobre funções anônimas é simples. Funções lambda são convenientes para conexões rápidas. O problema é que não podem ser desconectadas individualmente depois. Use-as apenas em conexões permanentes, que durarão pelo tempo de vida do widget.

Resumindo: sinais e slots desacoplam quem emite de quem responde. Objetos se comunicam sem dependências diretas. Esse padrão é a fundação de toda interface Qt modular e extensível.

---

# 9. Eventos

Nesta faixa você vai aprender como o Qt entrega interações do usuário à aplicação por meio de eventos, como tratá-los nos seus próprios widgets e como monitorar eventos de outros widgets sem precisar modificá-los.

Toda interação com o usuário, seja um clique, uma tecla pressionada, o redimensionamento de uma janela ou uma notificação do sistema operacional, chega à aplicação como um objeto do tipo QEvent. O event loop, que você configurou com QApplication, é responsável por capturar esses eventos, convertê-los em objetos QEvent e despachá-los ao widget correto.

Para tratar eventos no seu próprio widget, você sobrescreve os métodos de evento correspondentes. Cada tipo de evento tem seu método: keyPressEvent para teclas pressionadas, mousePressEvent para cliques do mouse, mouseDoubleClickEvent para duplos cliques, resizeEvent para redimensionamento, closeEvent para o fechamento da janela. Esses métodos recebem um objeto de evento que contém os detalhes da interação. No método de teclas, por exemplo, você consulta qual tecla foi pressionada. No método de clique, você consulta qual botão do mouse foi usado e em qual posição.

Há uma regra obrigatória ao sobrescrever esses métodos: sempre chame o método do pai com super quando o evento não for tratado pelo seu código. Se você não fizer isso, o Qt não conseguirá propagar o evento pela hierarquia de widgets, e comportamentos padrão deixarão de funcionar.

Uma situação especial é o closeEvent. Quando o usuário tenta fechar a janela, você pode interceptar essa ação e pedir confirmação. Se o usuário confirmar, você chama event.accept() para permitir o fechamento. Se o usuário cancelar, você chama event.ignore() para bloquear o fechamento e manter a janela aberta.

Para rastrear o movimento do mouse sem nenhum botão pressionado, é preciso ativar o mouse tracking no widget. Essa opção é desativada por padrão porque gerar eventos de movimento contínuos tem um custo. Existe uma armadilha conhecida ao ativar essa opção em uma QMainWindow: você precisa ativar o mouse tracking tanto na janela principal quanto no centralWidget. Ativar apenas em um dos dois não é suficiente.

Às vezes você quer reagir ao Tab ou às teclas de seta, que não chegam pelos métodos keyPressEvent normais. Para esses casos, você sobrescreve o método event, que recebe todos os eventos antes de serem distribuídos aos handlers específicos. Verifique o tipo do evento com QEvent.Type, trate o caso especial e retorne True para indicar que o evento foi consumido. Para todos os outros tipos, passe o evento ao método event do pai.

Para detectar combinações de teclas como Ctrl mais S ou Ctrl mais Shift mais Z, você consulta o atributo modifiers do evento junto com a tecla. Os modificadores disponíveis são ControlModifier para Ctrl, ShiftModifier para Shift, AltModifier para Alt e MetaModifier para a tecla Windows ou Command no Mac. Para combinar dois modificadores, use o operador de barra vertical entre eles.

Event filters resolvem um problema diferente: monitorar eventos de um widget que você não controla, sem precisar criar uma subclasse só para isso. Você registra a sua janela como filtro do outro widget chamando installEventFilter. A partir daí, todos os eventos daquele widget passam pelo método eventFilter da sua janela antes de serem entregues. No eventFilter, você verifica se o receptor é o widget esperado e se o tipo de evento é o que você quer interceptar. Se for, você age e retorna True. Em todos os outros casos, você deve retornar a chamada ao eventFilter do pai. Essa chamada ao super é obrigatória. Ignorá-la quebra o comportamento de outros filtros instalados na cadeia.

A regra mais importante de toda esta seção é sobre desempenho: handlers de evento devem retornar rapidamente. O event loop não processa nada enquanto um handler está em execução. Se você fizer uma operação demorada dentro de um handler, a interface congela. Para qualquer operação que leve mais de alguns milissegundos, use QThread.

Resumindo: eventos são o mecanismo pelo qual o Qt comunica interações à sua aplicação. Sobrescreva os handlers que você precisa e sempre propague o restante com super. Use event filters para monitorar widgets externos sem subclassificar. Nunca bloqueie o event loop.

---

# 10. Timers

Nesta faixa você vai aprender como executar código periodicamente em uma aplicação Qt sem travar a interface. Vamos entender o que é o QTimer, como usá-lo de forma correta e quando escolher entre disparo repetitivo e disparo único.

O QTimer é a ferramenta padrão para executar tarefas em intervalos regulares no Qt. Ele se integra diretamente ao event loop da aplicação. Isso significa que o timer não precisa de uma thread separada para funcionar.

Quando o intervalo configurado expira, o QTimer emite um sinal chamado timeout. Esse sinal é conectado a um slot, que é a função que executará a tarefa. O padrão é o mesmo da seção de sinais e slots.

Para criar um timer repetitivo, instancie o QTimer com a janela como pai, conecte o sinal timeout ao slot desejado e chame o método start com o intervalo em milissegundos. Para pausar o timer, use o método stop. Para mudar o intervalo sem reiniciá-lo, use setInterval.

Em seguida, existe o timer de disparo único. Quando você precisa que uma ação ocorra apenas uma vez após um atraso, use o método estático singleShot do QTimer. Você passa o tempo em milissegundos e o slot a ser chamado. O timer é criado, dispara e destrói-se automaticamente.

O QTimer complementa o módulo de data e hora do Qt. O QDateTime representa um ponto no tempo com data e hora combinadas. O QTime representa apenas a hora. Ambos oferecem métodos para formatar valores como texto, usando padrões de letras: quatro algarismos para o ano, dois para o mês, dois para o dia, e assim por diante.

Para integrar com o módulo datetime nativo do Python, a solução recomendada é converter por string. Você formata o datetime do Python como texto e usa o método fromString do QDateTime para fazer o parse com o mesmo padrão. O caminho inverso é análogo: converta o QDateTime para string com toString e use strptime do Python para interpretar o resultado.

O QLCDNumber é um widget que exibe valores numéricos no estilo de relógio digital. Ele é combinado frequentemente com um QTimer para criar relógios ou contadores na interface. Configure o número de dígitos com setDigitCount e passe uma string formatada ao método display.

A regra mais importante sobre o QTimer é a seguinte. O slot conectado ao timeout deve retornar rapidamente. Se o slot executar uma operação longa, o event loop ficará bloqueado durante toda a execução. Isso congela a interface para o usuário. Para tarefas longas, o correto é usar threads, que serão vistas na próxima seção.

Um equívoco frequente é usar o QTimer para tarefas que exigem precisão de milissegundos. O QTimer depende do event loop, que pode ter latência variável dependendo da carga da aplicação. Para requisitos de tempo muito preciso, o Qt não é a ferramenta adequada.

Resumindo, o QTimer é a forma correta de executar código periodicamente no Qt sem bloquear a interface. Use disparo repetitivo para tarefas contínuas e singleShot para atrasos pontuais. O slot deve sempre retornar rápido para preservar a responsividade da aplicação.

---

# 11. Threading — QThread e QRunnable

Nesta faixa você vai aprender como executar operações longas sem travar a interface. O Qt impõe regras estritas sobre o que pode ser feito em cada thread.

A regra fundamental do Qt não admite exceção. Apenas a thread principal pode acessar ou modificar widgets. Tocar em um widget a partir de outra thread torna o comportamento imprevisível. Toda operação longa deve ser movida para uma thread separada. Exemplos comuns são leitura de arquivo, chamadas de rede e cálculos pesados. Os resultados chegam de volta à interface por meio de sinais e slots.

O padrão recomendado envolve dois objetos: um Worker e uma thread. O Worker herda de QObject e contém o método de execução. A thread é uma instância de QThread. O passo central é chamar moveToThread no Worker, passando a thread como argumento. Isso transfere a afinidade do Worker para a thread secundária. A partir daí, os slots do Worker são executados fora da thread principal.

O Worker declara sinais para comunicação com a interface. Há tipicamente um sinal de progresso, um sinal de resultado e um sinal de conclusão. Quando a thread inicia, ela dispara o slot de execução do Worker. O sinal de progresso é emitido a cada passo do trabalho. A progress bar se conecta a esse sinal e atualiza automaticamente.

Há um detalhe importante sobre a destruição dos objetos. O Worker deve se conectar ao próprio deleteLater no sinal de conclusão. A thread também deve fazer o mesmo. Isso garante que ambos sejam destruídos corretamente após o trabalho terminar.

Em seguida, veja o segundo padrão: QRunnable com QThreadPool. Esse padrão é chamado de disparar e esquecer. Um QRunnable é uma tarefa simples com apenas um método de execução. O QThreadPool mantém um conjunto de threads e distribui as tarefas automaticamente. Para iniciar, basta chamar start no pool global. Use esse padrão quando a tarefa não precisa reportar progresso nem retornar valores à interface.

Para proteger dados compartilhados entre threads, use QMutex. Ele garante que apenas uma thread por vez execute um trecho crítico. A forma preferível é usar o QMutexLocker dentro de um bloco de contexto. O QMutexLocker libera o mutex automaticamente ao sair do bloco. Isso funciona mesmo quando ocorre uma exceção.

Por outro lado, quando o dado é lido muito mais frequentemente do que escrito, use QReadWriteLock. Ele permite leituras simultâneas por múltiplas threads. Uma escrita exige acesso exclusivo e bloqueia todos os leitores. Use QReadLocker para leituras e QWriteLocker para escritas.

Por fim, uma observação sobre alternativas. O Qt tem um módulo chamado QtConcurrent que simplifica operações paralelas, mas ele não está disponível no PySide6. Para esses casos, use QThreadPool ou o concurrent.futures da biblioteca padrão do Python. Um erro frequente é usar o processEvents da QCoreApplication para tentar simular paralelismo. Esse método processa eventos pendentes na thread principal, mas não cria paralelismo real. A interface pode parecer responsiva por um instante, mas o programa permanece bloqueado durante o processamento.

Resumindo, a thread principal é a única que pode tocar em widgets. Use Worker com moveToThread quando precisar de comunicação bidirecional. Use QRunnable para tarefas independentes. Proteja dados compartilhados com QMutex ou QReadWriteLock conforme o padrão de acesso ao dado.

---

# 12. Animações com QPropertyAnimation

Nesta faixa você vai aprender como criar animações fluidas em interfaces Qt. Vamos ver como animar propriedades de widgets, como controlar o ritmo da animação com curvas de easing e como encadear múltiplas animações.

O QPropertyAnimation, ou animação de propriedade, é a ferramenta principal para animações no Qt. Ele interpola automaticamente o valor de qualquer propriedade de um objeto Qt entre dois valores ao longo do tempo. A palavra interpolação significa que o Qt calcula todos os valores intermediários sozinho. Você define o valor inicial, o valor final e a duração em milissegundos.

Um ponto fundamental: a animação é gerenciada pelo loop de eventos da aplicação. Isso significa que você não precisa de threads extras para animar. A animação roda no mesmo ciclo que atualiza a interface, sem custo adicional de sincronização.

Para animar a posição ou o tamanho de um widget, você cria a animação indicando o widget alvo e o nome da propriedade que deseja mover. O Qt usa esse nome para ler e escrever a propriedade a cada quadro. Após definir duração, valor inicial, valor final e curva de easing, você chama o método de iniciar.

Para criar um efeito de aparecer e desaparecer gradualmente, o Qt exige uma etapa extra. É preciso adicionar um efeito gráfico de opacidade ao widget antes de animar. Esse efeito é um objeto separado que controla a transparência do widget. A animação então age sobre a propriedade de opacidade desse efeito. Para fade in, ela interpola de zero a um. Para fade out, de um a zero.

Em seguida, vamos falar sobre curvas de easing, que controlam o ritmo da animação. Uma curva linear mantém velocidade constante do início ao fim. A curva InOutQuad acelera no começo e desacelera no fim, resultando num movimento mais natural. OutBounce faz o elemento quicar ao chegar no destino. OutElastic cria um efeito elástico, como se o elemento fosse puxado por um elástico. OutBack faz o elemento ultrapassar levemente o destino antes de estabilizar. A escolha da curva é o que distingue uma animação mecânica de uma animação que parece viva.

Para composição de animações, o Qt oferece dois tipos de grupos. O grupo sequencial executa as animações uma após a outra. Entre elas, você pode inserir pausas com duração em milissegundos. O grupo paralelo executa todas as animações ao mesmo tempo. Um grupo pode ser adicionado dentro de outro, formando hierarquias complexas. A regra é chamar o método de início somente no grupo mais externo.

Os parâmetros avançados das curvas de easing permitem ajuste fino do comportamento. A amplitude controla a intensidade do efeito, como a altura do quique. O overshoot define o quanto a animação ultrapassa o valor final antes de retornar. O período controla a frequência das oscilações. Esses parâmetros não se aplicam a todos os tipos de curva. OutBounce usa amplitude. OutElastic usa amplitude e período. OutBack usa overshoot.

O Qt também oferece animações baseadas em estados com a QStateMachine, ou máquina de estados. Cada estado define o valor que uma propriedade deve assumir quando o sistema entra naquele estado. As transições entre estados podem carregar animações associadas. Nesse modelo, use o método assignProperty para definir o valor por estado, em vez de definir valores de início e fim diretamente na animação. O Qt interpola automaticamente entre o valor do estado de origem e o do estado destino.

Para animações que exigem controle manual, você pode usar um timer disparando a cada dezesseis milissegundos, o que equivale a sessenta quadros por segundo. A cada disparo, você atualiza as propriedades manualmente e solicita um redesenho. Esse método dá mais controle, mas exige que você calcule os valores intermediários.

A regra para escolher o método é a seguinte. Use QPropertyAnimation quando quiser interpolar automaticamente uma propriedade com uma curva de easing. Use o timer manual quando a lógica de animação for complexa demais para interpolação simples. Use QStateMachine quando as animações forem acionadas por mudanças de estado da interface.

Resumindo, o QPropertyAnimation simplifica animações ao eliminar threads e cálculo manual de valores intermediários. A curva de easing e o método de composição são o que determinam a qualidade visual e a complexidade da animação.

---

# 13. Referência de Widgets

Nesta faixa você vai conhecer os principais widgets do PySide6. O objetivo é saber qual componente usar para cada tipo de interação e quando escolher a variante simples em vez da arquitetura model/view.

Todos os widgets herdam de QWidget. Isso significa que todos compartilham a mesma base de geometria, visibilidade e tratamento de eventos. O comportamento comum você aprende uma vez, e vale para qualquer widget da biblioteca.

A primeira decisão ao montar uma interface é escolher entre um widget simples e a combinação model/view. Widgets simples, como QListWidget ou QTableWidget, armazenam os dados internamente. São convenientes para listas estáticas ou pequenas. A combinação de QListView ou QTableView com um modelo externo é preferível quando os dados mudam em tempo de execução ou aparecem em mais de um lugar na interface.

Para texto e rótulos, o QLabel exibe texto estático ou imagens, com suporte a HTML simples. O QLineEdit é o campo de texto de uma única linha, adequado para formulários. O QTextEdit suporta texto com formatação rica. O QPlainTextEdit, por outro lado, é otimizado para texto sem formatação e performa melhor em situações de logging ou exibição de saída de console.

Para seleções e controles de valor, o QCheckBox oferece uma opção marcável, com suporte opcional a três estados: marcado, desmarcado e parcial. O QRadioButton funciona em grupos e garante exclusividade dentro do grupo. O QComboBox é uma lista suspensa que pode ser tornada editável. O QSpinBox controla valores inteiros e o QDoubleSpinBox controla valores de ponto flutuante.

Para botões, o QPushButton é o botão de comando padrão. O QToolButton é mais compacto, adequado para barras de ferramentas, e pode exibir um menu popup ao ser pressionado.

Para feedback visual, o QProgressBar vai de um mínimo a um máximo. Definir ambos os limites como zero ativa o modo indeterminado, útil quando a duração da operação é desconhecida. O QSlider e o QDial são controles de intervalo, um horizontal ou vertical e o outro circular.

Para datas e horários, o QDateEdit, o QTimeEdit e o QDateTimeEdit cuidam cada um de seu tipo. O QCalendarWidget oferece um calendário mensal interativo para seleção de datas.

No grupo dos organizadores, o QGroupBox agrupa widgets com borda e título. O QSplitter divide uma área em painéis redimensionáveis pelo usuário. O QStackedWidget mostra um único widget por vez, sem abas visíveis. O QTabWidget faz o mesmo, mas com abas clicáveis na parte superior. O QScrollArea envolve um widget grande para torná-lo rolável.

A regra é a seguinte: prefira model/view sempre que os dados forem dinâmicos ou compartilhados entre partes distintas da interface. Widgets simples armazenam dados internamente, o que dificulta a sincronização quando o mesmo dado precisa aparecer em dois lugares ao mesmo tempo.

Um equívoco comum é usar QTextEdit para exibir saída de texto puro, como logs. O QPlainTextEdit é a escolha correta nesse caso, pois evita o custo de processamento da formatação rica que o QTextEdit carrega.

Resumindo, o catálogo de widgets do PySide6 cobre desde rótulos simples até calendários e visualizações hierárquicas. Conhecer a função de cada um e saber quando escalar para model/view são as duas decisões fundamentais ao projetar qualquer formulário ou interface.

---

# 14. Validação de Entrada

Nesta faixa, vamos explorar como o PySide6 valida entradas do usuário. O Qt oferece três estratégias complementares que você pode combinar no mesmo campo de texto. Cada uma age em um momento diferente: uma restringe enquanto o usuário digita, outra define o formato esperado e a terceira oferece sugestões.

A validação de entrada deve ocorrer na borda do sistema, antes que dados externos entrem na lógica da aplicação. A primeira estratégia é o QValidator. Ele restringe quais caracteres o usuário pode digitar enquanto o campo está sendo preenchido. O Qt fornece três validadores prontos. O QIntValidator aceita apenas inteiros dentro de um intervalo definido. O QDoubleValidator lida com números de ponto flutuante e limita a quantidade de casas decimais. O QRegularExpressionValidator aplica um padrão de expressão regular a qualquer entrada de texto. Você associa um validador a um campo de texto com o método setValidator.

A segunda estratégia são as máscaras de entrada, ativadas com o método setInputMask. Uma máscara define o formato exato do campo, posição por posição. Cada posição aceita um tipo específico de dado. O caractere nove representa um dígito obrigatório. O zero representa um dígito opcional. A letra A maiúscula exige uma letra ou dígito naquela posição. Com essas regras, você cria máscaras para endereços de rede, telefones e datas sem escrever nenhuma lógica de validação manual.

A terceira estratégia é o QCompleter. Ele apresenta sugestões enquanto o usuário digita. Você pode alimentá-lo com uma lista simples de palavras ou com um modelo de dados mais complexo. É possível configurar a sensibilidade a maiúsculas e o modo de exibição das sugestões. O modo mais comum é o de popup, que exibe uma lista flutuante logo abaixo do campo.

Além da validação em si, o QLineEdit oferece propriedades complementares de controle. O método setMaxLength limita quantos caracteres o campo aceita. O setPlaceholderText exibe um texto de dica quando o campo está vazio. O setEchoMode controla como o conteúdo digitado é exibido. O modo Password substitui cada caractere por um ponto, ideal para campos de senha. Por fim, setReadOnly torna o campo não editável, útil para exibir informações sem permitir alteração.

A regra fundamental é a seguinte: nunca use a validação da interface para substituir a validação na lógica de negócios. O QValidator e as máscaras são uma primeira linha de defesa que melhora a experiência do usuário. Mas os dados devem ser validados novamente ao serem processados. Um erro comum é aplicar o QIntValidator sem verificar se o campo está vazio antes de converter o valor. Um campo vazio passa pela validação sem emitir erro, mas a conversão de string vazia para inteiro resulta em exceção.

Em resumo, o Qt oferece três camadas de validação no campo de texto: restrição de caracteres com QValidator, formato fixo com máscaras de entrada e sugestão de valores com QCompleter. Use as três em conjunto quando o contexto exigir precisão na entrada.

---

# 15. Desenhando Formas com QPainter

Nesta faixa você vai aprender a desenhar formas personalizadas em um widget. O QPainter é o motor de desenho 2D do Qt.

O QPainter é a API unificada de desenho do Qt. Com ele você traça linhas, retângulos, elipses, texto e curvas. Todos esses elementos compartilham o mesmo objeto configurado. Duas propriedades definem a aparência. A caneta, chamada QPen, controla bordas e linhas. O pincel, chamado QBrush, controla o preenchimento das formas.

A primeira regra é onde colocar o código de desenho. Todo desenho deve ficar dentro do método paintEvent do widget. O Qt chama esse método automaticamente quando a tela precisa ser atualizada. Para solicitar um redesenho, chame o método update. Nunca chame paintEvent diretamente.

A segunda regra é como criar o QPainter dentro de um widget. Passe o próprio widget ao construtor do QPainter. Não use os métodos begin e end em widgets. Esses métodos existem para outros destinos de pintura, como arquivos de imagem ou SVG.

Com o QPainter criado, o primeiro passo é ativar o antialiasing. O antialiasing suaviza bordas serrilhadas de formas inclinadas. Ative o antialiasing de renderização e o antialiasing de texto separadamente. O resultado é muito mais polido do que o padrão sem suavização.

Em seguida, configure a caneta e o pincel. A caneta define a cor da borda, a espessura e o estilo da linha, como sólida, tracejada ou pontilhada. O pincel define a cor de preenchimento, e aceita transparência por meio do canal alfa. Depois passe os dois ao QPainter com setPen e setBrush.

Vamos ao repertório de primitivos disponíveis. O QPainter tem métodos para ponto único, linha, retângulo, retângulo arredondado, elipse, arco, setor circular, polígono e texto. Uma observação sobre arcos: os ângulos são expressos em dezesseis avos de grau, não em graus inteiros. Para um arco de noventa graus, multiplique o valor por dezesseis.

Para formas mais complexas, use o QPainterPath. Com ele você define contornos arbitrários passo a passo. Posicione a caneta com moveTo, adicione linhas com lineTo e curvas bezier com cubicTo. Feche o contorno com closeSubpath e passe o resultado ao método drawPath.

Por outro lado, quando um widget precisa se atualizar periodicamente, combine-o com um temporizador. O exemplo clássico é um relógio analógico. Conecte o sinal de timeout do temporizador ao slot update. A cada segundo, o Qt redesenha os ponteiros na posição correta.

Nesse exemplo há uma distinção importante sobre transformações. Ao desenhar as marcações do mostrador, deixe a rotação acumular a cada iteração. Cada marcação gira seis graus a mais que a anterior, o que é intencional. Já ao desenhar os ponteiros do relógio, isole cada rotação com o par save e restore. Chame save antes de girar, desenhe o ponteiro e chame restore em seguida. Sem esse isolamento, a rotação de um ponteiro contamina o próximo.

A regra geral para transformações é sempre parear save e restore. Antes de aplicar qualquer translação, escala, rotação ou cisalhamento, chame save. Após terminar o trecho, chame restore. Transformações não revertidas acumulam e corrompem tudo que vem depois.

Veja agora como exportar um desenho para SVG. SVG, sigla para Scalable Vector Graphics, ou gráficos vetoriais escaláveis, é um formato independente de resolução. Crie um objeto QSvgGenerator, configure o caminho do arquivo e o tamanho da imagem. Abra o QPainter sobre esse gerador com begin, execute todos os métodos de desenho normalmente e feche com end. O código de desenho não muda, apenas o destino muda.

A regra sobre SVG é precisa. Use uma única função de desenho compartilhada entre o paintEvent e a exportação. Nunca crie dois QPainter sobre o mesmo QSvgGenerator. Isso gera um arquivo SVG inválido.

Por fim, o QPainter oferece modos de composição. Eles controlam como cada pixel novo se combina com os pixels já desenhados. Os modos incluem Difference, Overlay, Xor e SoftLight, entre outros. Aplique o modo antes de desenhar o elemento desejado. Redefina o modo padrão, chamado SourceOver, logo após. Um modo de composição esquecido afeta tudo que vier a seguir.

Em resumo, o QPainter centraliza todo o desenho 2D do Qt. O código vai no paintEvent, e as formas são configuradas com caneta e pincel. Transformações exigem o par save e restore para não vazar entre elementos.

---

# 16. Imagens com QPixmap e QImage

Nesta faixa você vai aprender como o Qt trabalha com imagens. Existem dois tipos de imagem distintos, cada um com papel bem definido.

O Qt oferece QPixmap e QImage para manipular imagens. O QPixmap é otimizado para exibição na tela. Ele pode residir na memória da GPU, a unidade de processamento gráfico, tornando a renderização muito eficiente. A restrição importante é que o QPixmap só pode ser usado na thread principal da aplicação.

Em seguida, o QImage. Ele permite acesso direto a cada pixel da imagem. É projetado para leitura, escrita e processamento. Ao contrário do QPixmap, o QImage pode ser usado em qualquer thread. A regra é direta: para exibir, use QPixmap. Para manipular pixels, use QImage.

Com o QPixmap, as operações principais são carregar, escalar, recortar e salvar. Ao escalar, você informa as dimensões máximas ao Qt. Você também informa que a proporção deve ser preservada. Uma transformação suave mantém a qualidade visual. O resultado pode ser atribuído diretamente a um QLabel. Para salvar em JPEG, é possível controlar a qualidade da compressão.

Uma operação especial é criar um QPixmap com fundo transparente. Você cria o pixmap com as dimensões desejadas e preenche com a cor transparente. Em seguida, usa um QPainter para desenhar sobre ele. Ao usar QPainter sobre QPixmap, você deve chamar o método de finalização explicitamente. Isso é diferente do QPainter em um QWidget, onde o encerramento é automático.

O QImage expõe os pixels de forma direta. Você pode ler e alterar a cor de qualquer pixel por coordenada. O acesso por pixel é lento e serve apenas para pequenas quantidades de pontos. Para processamento intensivo, o QImage pode expor seus bytes brutos como buffer de memória. Com a biblioteca numpy, esse buffer vira um array tridimensional com altura, largura e canais de cor.

Um padrão valioso é usar o QImage como tela permanente em aplicativos de desenho. O usuário desenha com o mouse, e o conteúdo deve sobreviver a repaints. A solução é manter um QImage como estado da aplicação. Ao mover o mouse com o botão pressionado, você desenha no QImage com um QPainter temporário. No evento de pintura do widget, você simplesmente copia o QImage para a tela.

A regra central é que o QImage é o canvas permanente e o paintEvent é apenas o mecanismo de exibição. Um erro comum é desenhar diretamente no paintEvent esperando que o conteúdo persista. O paintEvent é chamado a qualquer momento pelo sistema e seu conteúdo é descartado a cada chamada.

Com QPixmap para exibição e QImage para processamento, você domina as duas formas de trabalhar com imagens no Qt.

---

# 17. Graphics View Framework

O Graphics View Framework é a escolha certa para criar editores gráficos, diagramas e jogos 2D no Qt. Nesta faixa você vai entender como ele organiza objetos visuais e como os exibe na tela com eficiência.

O conceito central do framework é a separação entre cena e view. A cena é o espaço lógico onde os itens existem, em coordenadas independentes da tela. A view é o widget que projeta a cena para o usuário. Essa separação permite aplicar zoom, rotação e deslocamento sem mover os itens. Você pode ter múltiplas views exibindo a mesma cena ao mesmo tempo.

O framework é composto por três classes principais. A primeira é a QGraphicsScene, que funciona como um container lógico de itens bidimensionais. A segunda é a QGraphicsItem, a classe base abstrata para qualquer elemento na cena. A terceira é a QGraphicsView, o widget que exibe a cena dentro de uma janela.

Para adicionar um item à cena, você instancia um tipo concreto, como retângulo, elipse ou texto, define sua posição e cores, e chama o método de adição da cena. Cada item recebe flags que controlam seu comportamento. Com a flag de movimentação, o usuário pode arrastar o item com o mouse. Com a flag de seleção, o item pode ser clicado para ficar selecionado. Com a flag de foco, o item pode receber eventos de teclado.

A ordem de sobreposição entre itens é controlada por um valor numérico chamado z-value. Itens com z-value maior aparecem na frente dos demais. Você também pode controlar a visibilidade e a opacidade de cada item individualmente.

Em seguida, veja como funcionam as transformações. Escala e rotação são aplicadas na view, não na cena. Quando você aumenta o zoom, os itens não se movem. Apenas a projeção muda. O método fitInView ajusta a view para exibir toda a cena de uma vez, respeitando a proporção escolhida.

O framework também oferece efeitos gráficos aplicáveis a qualquer item. O efeito de sombra projetada cria profundidade visual com deslocamento configurável. O efeito de desfoque suaviza as bordas do item. O efeito de colorização tinge o item com uma cor. O efeito de opacidade torna o item semitransparente. Para ativar suavização de bordas em toda a cena, habilite o antialiasing diretamente na view.

A regra mais importante sobre efeitos é a seguinte: nunca use o mesmo objeto de efeito em mais de um item. Cada item precisa de sua própria instância. Compartilhar instâncias causa comportamento visual inesperado.

O Graphics View Framework é mais adequado do que desenhar diretamente no paintEvent quando a cena contém muitos elementos interativos e independentes. Para conteúdo estático simples, a abordagem direta com QPainter continua sendo a mais eficiente.

---

# 18. Arquitetura Model-View

Nesta faixa você vai aprender como o Qt separa dados de exibição. Essa separação é a base de qualquer interface que lida com dados dinâmicos.

A arquitetura Model-View é um princípio fundamental do Qt. A ideia central é que os dados nunca devem se misturar com o código de exibição. Os dados ficam no modelo. A apresentação fica na view. Com essa separação, os mesmos dados podem aparecer em múltiplas views ao mesmo tempo. E a lógica de negócio não precisa saber nada sobre como os dados são exibidos.

O Qt define quatro papéis nessa arquitetura. O modelo, derivado de QAbstractItemModel, guarda os dados brutos. A view, derivada de QAbstractItemView, exibe esses dados para o usuário. O delegate controla como cada célula é renderizada e como o usuário edita seu conteúdo. E o modelo proxy, o QSortFilterProxyModel, intercepta o modelo original para filtrar ou ordenar os dados sem tocar na fonte.

Uma decisão importante é saber quando usar esse padrão completo. Para dados estáticos simples ou volumes pequenos, o QListWidget e o QTableWidget são mais práticos. Eles combinam modelo e view em uma única classe, sem configuração adicional. O padrão completo se justifica quando os dados mudam com frequência, quando você precisa de filtros ou ordenação, ou quando os mesmos dados precisam aparecer em mais de um lugar.

Vejamos o QSortFilterProxyModel. Esse proxy se posiciona entre o modelo original e a view. Você configura em qual coluna o filtro deve atuar. Define se a busca é sensível a maiúsculas ou não. Em seguida, conecta o sinal de mudança de texto de um campo de busca ao método de filtro do proxy. A view recebe o proxy como modelo e mostra apenas as linhas que correspondem ao texto digitado. Com uma propriedade adicional, você ativa a ordenação por clique no cabeçalho de cada coluna.

Para criar um modelo completamente customizado, você herda de QAbstractTableModel e implementa seis métodos. O método rowCount informa quantas linhas existem. O columnCount informa o número de colunas. O método data retorna o valor de uma célula para o papel de exibição. O headerData fornece os títulos das colunas e das linhas. O setData persiste a edição do usuário e emite o sinal de mudança de dados. E o método flags declara quais operações cada célula aceita, como seleção, ativação e edição.

A regra central é esta. Nunca coloque dados diretamente em uma view. Os dados vivem no modelo. A view apenas consulta o modelo quando precisa renderizar algo. Um erro comum é sincronizar manualmente os dados entre a view e uma estrutura interna. Com o padrão correto, o modelo é a fonte única de verdade, e a view sempre lê dele.

Em resumo, a arquitetura Model-View do Qt é a fundação para interfaces que lidam com dados dinâmicos. Ao separar claramente o modelo da view, você ganha flexibilidade e evita a duplicação de estado.

---

# 19. Drag and Drop

Nesta faixa você vai aprender como implementar arrastar e soltar em widgets PySide6, usando o protocolo MIME que o Qt define internamente.

Drag-and-drop no Qt funciona com base em um protocolo chamado MIME. Quando o usuário começa a arrastar algo, os dados são empacotados num objeto chamado QMimeData. Esse objeto recebe um tipo MIME, que é uma string descrevendo o formato dos dados — texto simples, URL de arquivo, imagem, ou um formato customizado da sua aplicação. O widget que recebe o drop inspeciona esses tipos disponíveis para decidir se aceita ou rejeita o objeto sendo arrastado. Essa negociação automática é o que garante que dados arrastados de uma aplicação possam ser soltos em outra aplicação diferente.

Para um widget de lista aceitar e produzir drags, três propriedades precisam ser configuradas no construtor. A primeira habilita que o widget receba drops, com setAcceptDrops ativado. A segunda habilita que itens possam ser iniciados como drag, com setDragEnabled ativado. A terceira define o modo de operação, com setDragDropMode configurado para DragDrop, indicando que o widget pode tanto originar quanto receber. Por fim, setDefaultDropAction define se a operação é uma movimentação ou uma cópia. Com essas configurações, o QListWidget já trata o drag-and-drop de seus próprios itens sem código adicional.

Para um drag completamente customizado, você precisa substituir três eventos no widget de origem. No mousePressEvent, quando o botão esquerdo é pressionado, você cria um QMimeData, define os dados com métodos como setText ou setUrls, cria um QDrag apontando para o widget, associa o QMimeData ao drag, e chama drag.exec para iniciar a operação. A chamada a exec bloqueia até que o usuário solte o objeto em algum lugar.

No widget de destino, dois eventos controlam o recebimento. O dragEnterEvent é chamado quando o cursor entra na área do widget durante um drag. Aqui você verifica se o QMimeData contém o tipo esperado — por exemplo, hasText para texto simples. Se sim, você chama event.acceptProposedAction para indicar aceitação. O dropEvent é chamado quando o usuário de fato solta o objeto. Nele você extrai os dados do mimeData do evento e processa o conteúdo recebido, confirmando a ação com acceptProposedAction.

Existem quatro eventos de drag-and-drop no total. O QDragEnterEvent dispara quando o drag entra no widget. O QDragLeaveEvent dispara quando o drag sai sem soltar. O QDragMoveEvent dispara a cada movimento dentro do widget, útil para feedback visual em tempo real. O QDropEvent dispara quando o usuário solta o objeto.

A regra central é separar claramente o papel de cada widget: quem origina o drag configura o QMimeData e chama drag.exec; quem recebe implementa dragEnterEvent e dropEvent, inspeciona o tipo MIME antes de aceitar, e extrai os dados no dropEvent.

---

# 20. Diálogos Integrados

Nesta faixa você vai conhecer os diálogos prontos que o Qt oferece. Eles cobrem os casos mais comuns de interação com o usuário. Há diálogos para selecionar arquivos, escolher cores, solicitar entrada e exibir mensagens.

Um diálogo modal bloqueia a janela pai até o usuário responder. Isso é adequado para confirmações e para coletar dados críticos. O Qt oferece diversas classes prontas para as situações mais frequentes.

Para selecionar arquivos, o Qt fornece o QFileDialog. A forma mais simples é usar a função estática getOpenFileName. Ela recebe o título, o diretório inicial e os filtros de tipo de arquivo. O retorno é o caminho do arquivo escolhido. Para salvar, existe getSaveFileName. Para múltiplos arquivos, existe getOpenFileNames. Para selecionar um diretório, use getExistingDirectory.

Quando você precisa de controle mais fino, instancie o QFileDialog diretamente. Configure o modo de seleção, os filtros e o diretório inicial antes de exibir o diálogo. Depois chame exec e leia os caminhos selecionados com selectedFiles.

Em seguida, o QInputDialog serve para receber um único valor do usuário. Há funções estáticas para texto, inteiro, decimal e seleção em lista. Todas retornam o valor e um booleano que indica se o usuário confirmou. Verifique sempre esse booleano antes de usar o valor.

O QColorDialog exibe um seletor de cores. A função estática getColor retorna um objeto de cor. Antes de aplicar, verifique se a cor é válida com o método isValid. Para incluir o canal de transparência, passe a opção ShowAlphaChannel ao chamar a função.

Para mensagens e confirmações, use o QMessageBox. Ele tem funções estáticas para quatro situações: informação, aviso, erro crítico e pergunta. A função question exibe botões configuráveis e retorna qual foi pressionado. Isso permite identificar se o usuário escolheu salvar, descartar ou cancelar.

Quando uma operação longa precisa de feedback visual, use o QProgressDialog. Defina o intervalo numérico e a mensagem ao criar o diálogo. Em cada iteração, atualize o progresso e chame processEvents para manter a interface responsiva. Verifique wasCanceled para interromper a operação se o usuário cancelar.

Para diálogos com layout personalizado, crie uma subclasse de QDialog. Use QDialogButtonBox para os botões de confirmação e cancelamento. Conecte o sinal accepted ao método accept e o rejected ao reject. Isso garante que o diálogo retorne o código correto ao fechar.

A regra é usar as funções estáticas para os casos simples e instanciar diretamente quando precisar de configuração fina. Um erro comum é verificar o retorno de exec como verdadeiro ou falso simples. O correto é comparar com o código Accepted da classe QDialog.

Os diálogos prontos do Qt cobrem a maioria dos casos de interação com o usuário. Prefira-os para manter a interface consistente com o sistema operacional.

---

# 21. Configurações Persistentes

Nesta faixa você vai aprender como salvar e recuperar preferências do usuário entre sessões, sem se preocupar com o mecanismo de armazenamento de cada sistema operacional.

O QSettings é a solução do Qt para persistência de configurações. Por trás de uma interface uniforme de chave e valor, ele usa o registro do Windows no Windows, arquivos plist no macOS e arquivos ini no Linux. Você escreve o mesmo código Python nos três sistemas, e o Qt cuida das diferenças.

A forma mais conveniente de usar o QSettings começa no objeto principal da aplicação. Ao configurar o nome da aplicação e o nome da organização no QApplication, qualquer ponto do código pode criar um QSettings sem argumentos. O Qt resolve automaticamente onde armazenar as configurações. Sem essa configuração prévia, você precisaria passar o nome da organização e o nome da aplicação toda vez que criasse um QSettings.

Para gravar uma configuração, você chama o método setValue com uma chave e um valor. A chave pode incluir uma barra para indicar hierarquia, como janela barra geometria. Isso organiza as configurações em grupos, tornando-as mais legíveis. Os valores aceitos incluem strings, números, listas e dados binários como a geometria da janela serializada.

Para ler de volta, você chama value com a mesma chave. É importante sempre passar um valor padrão para o caso de a chave não existir ainda, como na primeira execução. Também é possível informar o tipo esperado, como int ou list, para que o Qt converta o valor armazenado para o tipo correto. Sem essa dica de tipo, o retorno pode vir como string mesmo que você tenha gravado um número.

Quando você tem várias configurações relacionadas, o mecanismo de grupos ajuda a organizar. Você inicia um grupo com beginGroup, faz as leituras e escritas, e encerra com endGroup. Isso agrupa as chaves sob um prefixo comum. Em Python moderno, isso também pode ser feito com um gerenciador de contexto, que garante o fechamento automático do grupo.

A regra central é configurar o nome da aplicação e da organização no início do programa, uma única vez no QApplication. Nunca repita esses nomes nos objetos QSettings individuais. Um erro comum é gravar e ler com chaves ligeiramente diferentes, como usar um espaço num lugar e um underline em outro. Isso cria configurações duplicadas que nunca se sobrepõem.

Com o QSettings, as preferências do usuário sobrevivem ao fechamento da aplicação de forma transparente e portável.

---

# 22. Ícone na Bandeja do Sistema

Nesta faixa você vai aprender como manter uma aplicação ativa em segundo plano com um ícone na bandeja do sistema, o mesmo mecanismo que clientes de email e agentes de sincronização usam.

O QSystemTrayIcon permite que sua aplicação viva discretamente na área de notificação do sistema operacional. Com ele, você pode esconder a janela principal sem encerrar o programa, exibir notificações rápidas e oferecer um menu de contexto com as ações mais usadas.

O primeiro passo ao criar o ícone é verificar se o sistema suporta a bandeja. Nem todos os ambientes gráficos oferecem essa área. Se não houver suporte, informe o usuário com uma mensagem de erro adequada. Em seguida, crie o ícone com uma imagem e configure o texto que aparece ao passar o mouse sobre ele.

O menu de contexto é um objeto QMenu comum. Você adiciona ações para mostrar a janela, escondê-la e encerrar a aplicação. Em seguida, associa o menu ao ícone. A ação de mostrar a janela é geralmente conectada ao duplo clique no ícone, que é o comportamento que o usuário espera intuitivamente.

Para exibir uma notificação temporária, o QSystemTrayIcon tem um método que recebe o título, o texto, o ícone de notificação e a duração em milissegundos. Essas notificações aparecem como balões ou notificações nativas, dependendo do sistema.

Um padrão muito comum é interceptar o fechamento da janela. Em vez de encerrar o programa quando o usuário clica no botão fechar, o evento de fechamento é ignorado, a janela é escondida e uma notificação informa que a aplicação continua rodando na bandeja. Isso cria a experiência de minimizar para a bandeja.

A regra é sempre verificar o suporte antes de usar. E sempre fornecer uma opção de saída real, seja no menu da bandeja ou por outro meio. Aplicações que ficam na bandeja sem opção de encerramento confundem o usuário.

Com o QSystemTrayIcon, sua aplicação pode rodar em segundo plano de forma discreta e ainda manter contato com o usuário quando necessário.

---

# 23. Área de Transferência

Nesta faixa você vai aprender como ler e escrever na área de transferência do sistema, integrando sua aplicação ao mecanismo de copiar e colar do sistema operacional.

A área de transferência no Qt usa o mesmo protocolo de transferência de dados do drag-and-drop. Os dados são representados por um objeto QMimeData, que suporta múltiplos formatos ao mesmo tempo. O sistema operacional distribui o formato mais adequado dependendo de qual aplicação colará os dados.

Para acessar a área de transferência, você obtém o objeto global de clipboard a partir da aplicação Qt. Esse objeto é único por processo e compartilhado por todas as janelas.

A operação mais simples é trabalhar com texto puro. Você pode escrever uma string na área de transferência com um método direto, e ler o texto atual com outro método. Para imagens, o comportamento é análogo: escreve-se um QPixmap e recupera-se da mesma forma.

O clipboard emite um sinal quando o conteúdo muda. Isso permite que sua aplicação reaja em tempo real a colagens vindas de outros programas, sem precisar consultar a área de transferência periodicamente.

Para formatos mais ricos, como enviar texto e endereços de arquivo ao mesmo tempo, você cria um objeto QMimeData manualmente, define os dados em cada formato desejado e passa o objeto para a área de transferência. O destinatário pode então escolher qual formato consumir.

A regra central é sempre verificar se os dados estão presentes antes de ler. Ao colar, inspecione o formato disponível antes de extrair o conteúdo. Um erro comum é tentar ler texto de uma área de transferência que contém apenas uma imagem.

Com essa API, sua aplicação pode participar plenamente do fluxo de copiar e colar do sistema operacional.

---

# 24. Tela de Splash

Nesta faixa você vai aprender como exibir uma tela de carregamento enquanto a aplicação inicializa, melhorando a percepção de desempenho pelo usuário.

A tela de splash é um elemento visual exibido imediatamente após o lançamento da aplicação, antes que a janela principal esteja pronta. Ela dá ao usuário a certeza de que o programa iniciou, mesmo quando há operações pesadas acontecendo, como conexão com banco de dados ou carregamento de plugins.

O QSplashScreen recebe uma imagem no momento da criação. Assim que você chama show, a imagem aparece na tela, geralmente centralizada no monitor principal. Ela não tem barra de título nem bordas, dando um visual limpo e profissional.

Enquanto a tela de splash está visível, você pode exibir mensagens de progresso sobrepostas à imagem. O método showMessage recebe o texto, o alinhamento e a cor. Para que o texto apareça imediatamente, é necessário forçar o processamento de eventos logo depois. Sem esse passo, a mensagem só aparece na próxima iteração do event loop, o que pode acontecer tarde demais.

Quando a janela principal estiver pronta, você chama finish passando a janela. O Qt fecha o splash de forma suave assim que a janela for exibida. A ordem correta é: exibir o splash, fazer a inicialização, criar a janela principal, chamar finish e só então exibir a janela.

A regra é não usar o splash como substituto para progresso real. Se a inicialização for muito longa, considere mover parte do trabalho para uma thread separada. O splash é um recurso visual, não uma desculpa para bloquear o event loop por vários segundos.

Com o QSplashScreen, o lançamento da aplicação parece mais rápido e profissional, mesmo quando há operações de carga que levam alguns momentos.

---

# 25. Banco de Dados com QtSql

Nesta faixa você vai aprender como conectar uma aplicação PySide6 a bancos de dados relacionais, executar queries com segurança e exibir os dados em views integradas.

O módulo QtSql oferece uma camada de abstração sobre diferentes bancos relacionais. Com ele, você usa a mesma API para SQLite, PostgreSQL, MySQL e outros, trocando apenas o driver de conexão. Para aplicações locais, o SQLite é a escolha mais comum porque não exige servidor separado e já está incluído no Qt.

A conexão começa criando um objeto de banco de dados e informando qual driver usar. Em seguida, você configura o nome do banco, o host e as credenciais quando necessário. O método open retorna falso se a conexão falhar. A boa prática é abrir a conexão logo após criar o QApplication, antes de exibir qualquer janela.

Para executar queries, o Qt oferece o objeto QSqlQuery. Você cria uma query, chama exec e itera pelos resultados com next. Em cada linha, o método value retorna o valor de uma coluna, seja pelo índice numérico ou pelo nome da coluna. O acesso por nome é mais legível e resistente a mudanças na ordem das colunas.

A regra mais importante sobre queries é nunca construir SQL concatenando strings de entrada do usuário. Isso abre a aplicação para ataques de injeção de SQL. O modo correto é usar prepared statements. Você escreve a query com marcadores de posição, como dois pontos seguidos do nome do parâmetro, e vincula os valores com bindValue. O Qt cuida da formatação segura automaticamente.

Para transações, o Qt permite iniciar, confirmar e reverter. Use transações sempre que precisar garantir que um conjunto de operações seja atômico, como transferir valores entre contas. Se qualquer operação falhar, reverta todas.

Além das queries manuais, o Qt oferece modelos prontos que se integram diretamente com as views. O QSqlQueryModel serve para exibição somente leitura. O QSqlTableModel permite editar os dados e envia as mudanças de volta ao banco. O modo de edição mais seguro é o manual, onde as alterações são acumuladas e enviadas todas de uma vez quando o usuário confirma.

Para relacionamentos entre tabelas, o QSqlRelationalTableModel resolve automaticamente chaves estrangeiras e exibe os valores da tabela relacionada. O delegate relacional substitui campos de ID por ComboBoxes com os valores legíveis.

A regra final é preferir sempre o padrão de model e view em vez de preencher manualmente um QTableWidget com dados do banco. O modelo cuida da sincronização. O QTableWidget manual é útil apenas quando você precisa de controle total sobre cada célula individual.

---

# 26. QStandardItemModel

Nesta faixa você vai aprender a usar o modelo padrão do Qt para exibir dados em listas, tabelas e árvores sem precisar implementar um modelo do zero.

O QStandardItemModel é o modelo genérico que o Qt oferece para situações onde os dados cabem em memória e não precisam de uma fonte customizada. Ele funciona com qualquer view: lista, tabela ou árvore. Cada célula é representada por um objeto QStandardItem, que pode carregar texto, ícone, dica de ferramenta e dados arbitrários.

Para usar como tabela, você cria o modelo informando o número de linhas e colunas iniciais, define os rótulos das colunas e adiciona linhas como listas de itens. Cada item pode ter comportamentos específicos, como ser marcável com checkbox ou ser somente leitura. A view recebe o modelo e exibe os dados automaticamente.

Para listas, o modelo funciona da mesma forma, mas cada linha tem apenas um item. Para árvores, você acessa o item raiz invisível e adiciona itens pai com seus respectivos filhos. Cada item pai pode ter quantas colunas e quantos filhos quiser.

Para acessar ou modificar um item específico, use o método item com a linha e a coluna. Você pode alterar o texto, a cor de fundo, a fonte ou qualquer dado customizado armazenado no papel UserRole. O papel UserRole é o mecanismo padrão para associar um identificador ou objeto Python a um item sem exibi-lo diretamente.

A regra de quando usar o QStandardItemModel é simples. Se os dados são estáticos ou mudam pouco, e o volume é pequeno, use-o. Se os dados vêm de um banco de dados ou de uma API e precisam de filtros ou ordenação dinâmica, prefira implementar um modelo customizado derivando de QAbstractTableModel.

---

# 27. QTreeWidget e QTableWidget

Nesta faixa você vai aprender sobre os widgets de conveniência do Qt para listas e tabelas, quando usá-los e quando preferir o padrão completo de model e view.

O QTreeWidget e o QTableWidget são chamados de widgets de conveniência porque combinam modelo e view em uma única classe. Você não precisa criar um modelo separado. Eles são adequados para dados estáticos, volumes pequenos e prototipagem rápida.

O QTreeWidget exibe dados hierárquicos. Você define o número de colunas, os rótulos de cabeçalho, e adiciona itens como objetos QTreeWidgetItem. Cada item pode ter filhos, formando uma árvore. Você pode expandir itens por padrão, adicionar ícones nas colunas e reagir a cliques e duplos cliques com sinais.

O QTableWidget exibe dados em grade. Você cria com o número de linhas e colunas. Cada célula recebe um objeto QTableWidgetItem com o texto desejado. Também é possível colocar qualquer widget numa célula, como uma barra de progresso ou um ComboBox. Isso é feito com setCellWidget.

Uma propriedade importante é o modo de edição. Por padrão, o usuário pode editar qualquer célula. Para tabelas somente leitura, configure os gatilhos de edição para nenhum. A seleção por linha inteira, em vez de por célula individual, é uma boa prática para tabelas que representam registros.

A regra é clara: use QTreeWidget e QTableWidget para prototipagem e dados simples. Quando os dados são dinâmicos, precisam de filtros, precisam de ordenação ou são compartilhados entre múltiplas views, migre para o padrão de model e view com QStandardItemModel ou QAbstractTableModel.

---

# 28. Requisições HTTP

Nesta faixa você vai aprender como fazer requisições de rede em PySide6 de forma assíncrona, sem bloquear a interface do usuário.

O Qt oferece o QNetworkAccessManager para comunicação HTTP. Ele executa as requisições de forma integrada ao event loop. Quando a resposta chega, ela é entregue via sinal, sem bloquear a interface. Isso é fundamental: nunca faça requisições de rede na thread principal de forma síncrona.

O padrão recomendado é encapsular o gerenciador de rede em uma classe de serviço. Essa classe cria um único QNetworkAccessManager e o reutiliza para todas as requisições. Reutilizar o gerenciador é importante porque ele mantém internamente um pool de conexões e um cache HTTP. Criar um novo gerenciador a cada requisição desperdiça esses recursos.

Para uma requisição GET, você cria um objeto de requisição com a URL, configura os cabeçalhos necessários como tipo de conteúdo e tokens de autenticação, e chama get no gerenciador. O método retorna um objeto de resposta imediatamente. Você conecta o sinal de finalização da resposta a um método que extrai os dados. Dentro desse método, verifique se houve erro antes de processar o conteúdo. Ao final, sempre chame deleteLater na resposta para liberar a memória.

Para requisições POST com dados em formato JSON, você prepara o corpo como um documento JSON, codifica em bytes e passa junto com a requisição. Para formulários, o corpo é uma sequência de pares chave e valor codificados no formato de URL.

Para downloads com acompanhamento de progresso, conecte o sinal de progresso de download da resposta. Ele informa quantos bytes foram recebidos e o total esperado. Isso permite exibir uma barra de progresso ao usuário.

Uma observação importante: o suporte a FTP foi removido do Qt 6. Para transferências FTP, use a biblioteca da linguagem Python em uma thread separada, integrando o resultado de volta à interface via sinais.

A regra central é tratar a rede sempre como uma operação assíncrona. Nunca espere o resultado de uma requisição bloqueando o event loop. Use sempre o padrão de sinal e slot para receber a resposta.

---

# 29. Serviços do Sistema Operacional e Vigilância de Arquivos

Nesta faixa você vai aprender como abrir arquivos e URLs com os aplicativos padrão do sistema e como monitorar mudanças no sistema de arquivos em tempo real.

O QDesktopServices permite que sua aplicação delegue ações ao sistema operacional. Com ele, você pode abrir uma URL no navegador padrão, abrir um arquivo com o aplicativo associado, ou abrir uma pasta no gerenciador de arquivos. Tudo com uma única chamada. O usuário vê o comportamento que já conhece, sem que sua aplicação precise implementar um visualizador próprio.

Além de abrir recursos, o Qt oferece uma forma de descobrir caminhos importantes do sistema de arquivos. O QStandardPaths resolve diretórios como Documentos, Downloads, área de dados da aplicação e pasta temporária. O resultado é o caminho correto para cada sistema operacional. Nunca construa esses caminhos manualmente com strings fixas, porque eles diferem entre Windows, macOS e Linux.

Em seguida, o QFileSystemWatcher permite monitorar arquivos e pastas por mudanças. Você adiciona os caminhos que deseja observar. Quando um arquivo é modificado, o sinal fileChanged é emitido com o caminho do arquivo. Quando o conteúdo de uma pasta muda, seja por criação ou exclusão de arquivos, o sinal directoryChanged é emitido.

Um detalhe importante: quando um arquivo é deletado e recriado, alguns sistemas de arquivos removem o watcher automaticamente. Por isso, no handler de mudança de arquivo, verifique se o arquivo ainda está na lista de monitorados e readicione se necessário.

A regra é usar o QFileSystemWatcher para configurações que podem ser editadas externamente, como arquivos de configuração. Com ele, a aplicação recarrega a configuração automaticamente sem precisar reiniciar. Um erro comum é confundir modificação de arquivo com modificação de pasta. O sinal directoryChanged indica que a estrutura da pasta mudou, não o conteúdo de um arquivo específico dentro dela.

---

# 30. Desfazer e Refazer com QUndoStack

Nesta faixa você vai aprender como implementar desfazer e refazer em qualquer editor usando o padrão Command do Qt.

O QUndoStack implementa o padrão de design chamado Command. Nesse padrão, cada operação que o usuário realiza é encapsulada num objeto de comando. Esse objeto sabe como executar a operação, e também sabe como desfazê-la. A pilha mantém o histórico de comandos e gerencia automaticamente quais ações de menu estão habilitadas.

Para implementar, você cria uma classe que herda de QUndoCommand para cada tipo de operação. O construtor recebe o estado anterior e o novo estado. O método redo aplica a operação. O método undo reverte para o estado anterior. Um texto descritivo, como renomear arquivo, aparece no menu de desfazer para orientar o usuário.

Para usar a pilha, você a cria no editor e pede a ela as ações de desfazer e refazer. Essas ações já vêm configuradas com os textos e os atalhos de teclado corretos. Você apenas as adiciona ao menu de edição. Quando o usuário realiza uma operação, em vez de executá-la diretamente, você cria o comando e empurra na pilha. A pilha chama redo automaticamente ao receber o comando.

A pilha também suporta o conceito de estado limpo. Quando você salva o arquivo, marca a posição atual como limpa. A pilha usa isso para determinar se o documento tem modificações não salvas. Isso alimenta o título da janela com o asterisco de modificado, por exemplo.

Para operações complexas que envolvem múltiplos passos, como formatar toda uma seleção de uma vez, você pode agrupar comandos em macros. O grupo aparece como um único item na pilha. Desfazê-lo reverte todos os passos de uma vez.

Outra otimização é mesclar comandos consecutivos do mesmo tipo. Se o usuário mover um item várias vezes seguidas, cada posição intermediária não precisa ficar na pilha. O método mergeWith permite que um comando absorva o seguinte, resultando em apenas uma entrada que vai do ponto inicial ao ponto final.

Com o QUndoStack, qualquer editor ganha desfazer e refazer de forma robusta, com pouco código duplicado e total integração com os menus da aplicação.

---

# 31. Sistema de Recursos

Nesta faixa você vai aprender como embutir imagens, folhas de estilo e fontes diretamente na aplicação, eliminando dependências de caminhos do sistema de arquivos.

O Qt Resource System resolve um problema clássico de distribuição: onde colocar os arquivos de assets. Quando você empacota uma aplicação, caminhos relativos ao projeto de desenvolvimento não existem na máquina do usuário. A solução do Qt é compilar esses arquivos diretamente dentro do código Python gerado.

O processo começa com um arquivo de recursos no formato XML. Nesse arquivo, você declara os assets em grupos chamados prefixos. Um grupo para ícones, outro para folhas de estilo, outro para fontes. Cada arquivo recebe um apelido que será usado no código, independente de onde o arquivo físico está na estrutura do projeto.

O segundo passo é compilar esse arquivo XML com a ferramenta pyside6-rcc. O resultado é um arquivo Python com todos os dados dos assets codificados como bytes. Você importa esse arquivo no código da aplicação. A simples importação já registra todos os recursos no Qt.

A partir daí, qualquer lugar do código pode acessar os recursos usando caminhos especiais que começam com dois pontos. Um ícone declarado no grupo de ícones com o apelido novo é acessado com dois pontos, barra, ícones, barra, novo ponto png. O Qt sabe exatamente onde estão os bytes desse ícone, sem consultar o sistema de arquivos.

Para carregar uma folha de estilo embutida, você a abre como se fosse um arquivo normal. O Qt intercepta o caminho com prefixo de dois pontos e retorna os bytes corretos. Para registrar uma fonte embutida, você a adiciona ao banco de fontes do Qt com o mesmo tipo de caminho.

A regra fundamental é nunca usar caminhos absolutos ou relativos ao sistema de arquivos para assets de interface. Quando o arquivo é empacotado para distribuição, o caminho relativo deixa de existir. Assets que não estão no sistema de recursos quebram em produção.

---

# 32. Deploy e Empacotamento

Nesta faixa você vai aprender como transformar uma aplicação PySide6 em um executável distribuível para Windows, macOS e Linux.

Distribuir uma aplicação PySide6 significa empacotar o interpretador Python, as bibliotecas Qt e todos os assets em um único artefato que o usuário pode instalar e executar sem ter Python instalado. Existem três ferramentas principais para isso.

A primeira e mais popular é o PyInstaller. Você o invoca na linha de comando, apontando para o arquivo principal da aplicação. Ele analisa os imports, coleta todas as dependências e gera um executável. Para aplicações gráficas, a opção windowed elimina a janela de terminal que apareceria junto. Para gerar um único arquivo executável em vez de uma pasta, use a opção onefile. O PyInstaller também aceita um arquivo de especificação para customizações avançadas, como incluir arquivos de dados extras ou excluir módulos desnecessários que aumentariam o tamanho.

A segunda opção é o Nuitka. Em vez de empacotar o Python, o Nuitka compila o código Python para código C e depois para código nativo. O resultado é um executável com melhor performance de inicialização e tamanho menor. A troca é que a compilação é mais lenta. Para projetos com requisitos de performance, o Nuitka vale o custo.

A terceira opção é o pyside6-deploy, a ferramenta oficial do Qt para Python. Ela gera um arquivo de especificação otimizado para o PySide6 e simplifica a configuração.

Independente da ferramenta, algumas práticas são obrigatórias. Todos os assets devem estar no sistema de recursos do Qt ou ser copiados com o executável. Caminhos absolutos de desenvolvimento quebram em produção. O executável deve ser testado em uma máquina limpa, sem Python instalado. No Windows, é necessário assinar o executável para evitar alertas de antivírus. No macOS, a notarização é obrigatória para distribuição fora da App Store.

A estrutura de pastas do projeto também importa para builds reproduzíveis. O ponto de entrada deve ser um arquivo único na raiz. As dependências devem estar em um ambiente virtual dedicado ao projeto. Isso garante que o PyInstaller não inclua pacotes irrelevantes instalados globalmente.

---

# 33. Migração para PySide6

Nesta faixa você vai aprender as principais mudanças entre versões antigas do Qt para Python e o PySide6 moderno.

O PySide6 traz mudanças importantes em relação ao PySide, ao PySide2 e até ao PyQt6. A principal delas é a unificação das enumerações em namespaces fortemente tipados. Em versões antigas, constantes como AlignCenter podiam ser acessadas diretamente na classe Qt. No PySide6, cada constante vive dentro do seu grupo específico. O alinhamento de centro agora fica dentro do grupo AlignmentFlag, dentro da classe Qt. Essa mudança torna o código mais explícito e evita colisões de nomes.

Outra mudança comum é a remoção do underscore no final de certos métodos. Em versões antigas, iniciar o event loop era feito com exec seguido de underscore. Hoje é simplesmente exec. O mesmo vale para métodos como open em dialogs e exec em queries SQL.

Algumas classes mudaram de módulo. O QAction, por exemplo, saiu do módulo QtWidgets e foi para o QtGui. O QStateMachine saiu do QtCore e ganhou um módulo próprio. Ao migrar código, os erros de importação revelam essas mudanças de local.

Para quem vem do PyQt6, a maior diferença é que o PyQt6 exige nomes de enum completamente qualificados em todos os contextos, enquanto o PySide6 é um pouco mais flexível em algumas situações. Para código que precisa rodar nos dois frameworks, é possível tentar importar do PyQt6 e, em caso de falha, importar do PySide6.

A ferramenta pyside6-codemods automatiza parte das substituições mais mecânicas. Mas a revisão manual dos enums e das mudanças de módulo ainda é necessária.

A regra ao migrar é tratar cada aviso de depreciação e cada erro de importação como um passo específico da migração. Não tente migrar tudo de uma vez sem testes. Migre módulo a módulo e verifique o comportamento a cada etapa.

---

# 34. Erros Comuns

Nesta faixa você vai conhecer os erros mais frequentes em aplicações PySide6 e como corrigi-los antes que cheguem à produção.

O primeiro grupo de erros envolve a ordem de criação dos objetos. O Qt exige que o QApplication exista antes de qualquer widget. Criar um widget antes do QApplication causa uma falha imediata. Da mesma forma, o event loop deve ser iniciado com exec no final do programa. Sem ele, a janela aparece e fecha imediatamente.

O segundo grupo envolve threads. A regra absoluta do Qt é que apenas a thread principal pode criar ou modificar widgets. Qualquer tentativa de atualizar a interface a partir de uma thread de trabalho causa comportamento imprevisível, incluindo travamentos silenciosos e crashes. A solução é emitir um sinal na thread de trabalho e conectá-lo a um slot na thread principal.

O terceiro grupo envolve sinais em ciclo. Quando dois widgets estão conectados mutuamente e a mudança de um dispara o outro, que por sua vez dispara o primeiro, o resultado é um loop infinito. A solução é usar o método blockSignals para desativar os sinais temporariamente enquanto você atualiza o valor programaticamente.

O quarto grupo envolve o evento de pintura. O paintEvent é chamado pelo Qt a qualquer momento. Você não controla quando ele é chamado. Por isso, nunca desenhe diretamente no paintEvent esperando que o conteúdo persista. Use um objeto de imagem como estado e copie-o para a tela dentro do paintEvent.

O quinto grupo envolve formulários de arquivo. As funções estáticas de diálogo de arquivo retornam sempre uma tupla com dois elementos: o caminho selecionado e o filtro usado. Se você armazenar o resultado em uma variável simples, terá uma tupla em vez do caminho. Sempre desempacote o retorno em duas variáveis.

A regra geral é ler os avisos do Qt no console com atenção. O Qt emite mensagens de aviso muito informativas que apontam o problema e muitas vezes a solução.

---

# 35. Checklist Geral

Nesta faixa você vai ter uma visão consolidada das boas práticas de aplicações PySide6, organizada como uma lista de verificação para revisar antes de publicar qualquer código.

O primeiro grupo cobre o setup da aplicação. O QApplication deve ser criado com os argumentos do sistema antes de qualquer widget. O nome da aplicação e da organização devem ser configurados logo em seguida para habilitar o sistema de configurações. O event loop deve ser iniciado com exec e seu código de retorno passado para sys.exit. Todo código de inicialização deve estar dentro da guarda de execução principal.

O segundo grupo cobre janelas e widgets. Toda janela deve herdar de QWidget ou QMainWindow e chamar o construtor pai. A construção da interface deve ser separada em métodos internos. Todo widget de nível superior deve ter show chamado. A centralização da janela deve acontecer antes de show. O QMainWindow exige que setCentralWidget seja chamado.

O terceiro grupo cobre threading. Nenhuma tarefa longa pode rodar na thread principal. Widgets nunca são acessados fora da thread principal. O padrão de worker com moveToThread é o mecanismo correto para tarefas com feedback.

O quarto grupo cobre banco de dados. A conexão deve ser aberta antes de exibir qualquer janela. Falhas de conexão devem ser tratadas e exibidas ao usuário. Todas as queries com dados externos devem usar prepared statements. A estratégia de edição do modelo SQL deve ser configurada antes de chamar select.

O quinto grupo cobre desenho. O QPainter em widgets usa o padrão QPainter com self dentro do paintEvent, sem begin e end. O QPainter em imagens exige o método end explícito. A chamada update é obrigatória quando os dados mudam e o widget precisa ser redesenhado.

Com essa lista em mãos, você consegue revisar qualquer aplicação PySide6 de forma sistemática antes de compartilhá-la.

---

# 36. Ferramentas de Desenvolvimento

Nesta faixa você vai conhecer as ferramentas essenciais para trabalhar com PySide6 de forma profissional.

A ferramenta mais importante do ecossistema Qt é o Qt Designer. Ele permite construir interfaces visuais arrastando widgets para uma tela, sem escrever código de posicionamento. O resultado é um arquivo de extensão ui, que é um documento XML descrevendo a estrutura da interface. O Designer está disponível para PySide6 através do Qt Online Installer.

O Designer oferece um modo de preview que permite testar o espaçamento, o alinhamento e o comportamento dos layouts antes de integrar com Python. Isso economiza ciclos de tentativa e erro. Cada widget no Designer deve receber um nome de objeto descritivo. Esse nome se torna o identificador pelo qual o código Python acessa o widget.

Além do Designer, o PySide6 inclui a ferramenta pyside6-uic para converter arquivos de interface em classes Python, a ferramenta pyside6-rcc para compilar recursos, e a ferramenta pyside6-deploy para empacotar a aplicação.

Para verificar se a instalação está funcionando, basta criar um arquivo Python que importa QApplication do módulo QtWidgets e imprime uma mensagem de confirmação. Se a importação falhar, o PySide6 não está instalado no ambiente ativo. A causa mais comum é tentar executar o script sem ativar o ambiente virtual primeiro.

---

# 37. Qt Designer: Workflow Completo

Nesta faixa você vai aprender o fluxo completo de trabalho com o Qt Designer, desde a criação do arquivo de interface até a integração com o código Python.

O Qt Designer é a ferramenta visual do Qt para criação de interfaces. O fluxo começa escolhendo um template: janela principal, diálogo ou widget simples. Você arrasta widgets da caixa de ferramentas para o canvas, ajusta o tamanho e aplica layouts. Os layouts são essenciais porque garantem que a interface redimensiona corretamente. Sem layout, os widgets ficam em posição absoluta e não se adaptam ao redimensionamento da janela.

Para cada widget que o código Python precisará acessar, defina um nome de objeto descritivo no editor de propriedades. Esse nome se torna o identificador direto no código. Um botão com o nome submitButton é acessado diretamente como janela ponto submitButton.

Existem duas formas de usar o arquivo de interface no Python. A primeira é o carregamento dinâmico. Você carrega o arquivo em tempo de execução com o QUiLoader. Qualquer mudança no Designer reflete imediatamente, sem regenerar arquivos. É a abordagem recomendada para prototipagem.

A segunda forma é converter o arquivo de interface em uma classe Python com a ferramenta pyside6-uic. Essa classe é então usada por herança múltipla na sua janela. O método setupUi inicializa todos os widgets definidos no Designer. Essa abordagem é recomendada para produção porque o código Python é verificável por linters e analisadores de tipo.

A regra fundamental é nunca editar o arquivo de interface manualmente nem editar a classe Python gerada. O arquivo de interface é a fonte de verdade do design. A classe gerada é um artefato descartável, regenerada a qualquer momento com um único comando.

Para projetos maiores, é possível combinar as duas abordagens. O Designer define a estrutura geral da janela, e o código Python injeta widgets dinâmicos nos layouts definidos no Designer. Isso é útil quando parte da interface depende de dados que só existem em tempo de execução.

---

# 38. Paradigma Model-View

Nesta faixa você vai aprender como o Qt separa dados de apresentação em um padrão que facilita reutilização e manutenção.

O paradigma Model-View do Qt é uma implementação do padrão de design de mesmo nome. A ideia central é que os dados nunca se misturam com o código de exibição. O modelo é o repositório dos dados. A view é o componente que os exibe. Quando o modelo muda, a view atualiza automaticamente. Vários views podem exibir o mesmo modelo ao mesmo tempo.

O Qt oferece modelos prontos para os casos mais comuns. O QStringListModel serve para listas simples de strings. O QStandardItemModel cobre tabelas e hierarquias. Para casos onde você precisa de controle total sobre o comportamento do modelo, o QAbstractTableModel é a base para implementar o seu próprio.

Para implementar um modelo customizado, você herda de QAbstractTableModel e implementa pelo menos três métodos: rowCount, columnCount e data. O rowCount informa quantas linhas existem. O columnCount informa o número de colunas. O data é chamado pela view para cada célula que precisa ser exibida, e retorna o valor correspondente.

Quando os dados do modelo mudam, o modelo deve notificar as views. Para mudanças em células específicas, emita o sinal dataChanged com os índices afetados. Para mudanças estruturais como inserção ou remoção de linhas, existe um protocolo de sinais específico que a view usa para reorganizar o que está exibindo.

Para adicionar filtros e ordenação sem alterar o modelo original, use o QSortFilterProxyModel. Esse proxy se interpõe entre o modelo e a view. Você configura um padrão de filtro e o proxy decide quais linhas mostrar. A ordenação por clique no cabeçalho da view também é ativada através do proxy.

A regra é sempre preferir o padrão Model-View quando os dados são dinâmicos, precisam de filtros, ou precisam aparecer em mais de um lugar. Para dados estáticos e volumes pequenos, os widgets de conveniência como QTableWidget são mais práticos.

---

# 39. Widgets Reutilizáveis e Customizados

Nesta faixa você vai aprender como criar seus próprios widgets compostos, encapsulando interface e comportamento em componentes reutilizáveis.

Um widget customizado em Qt é simplesmente uma classe que herda de QWidget ou de QFrame. Essa classe cria seus próprios widgets filhos, os organiza em um layout interno e expõe uma interface pública para o exterior. O widget resultante pode ser usado em qualquer lugar da aplicação como se fosse um widget nativo do Qt.

O ponto mais importante sobre a comunicação entre um widget customizado e o resto da aplicação é o uso de sinais. O widget define seus próprios sinais para notificar eventos internos. A janela pai conecta esses sinais a slots seus. Essa separação garante que o widget não precisa conhecer quem o usa. Isso é o que torna o componente genuinamente reutilizável.

O construtor do widget recebe os parâmetros necessários para sua configuração inicial. Esses parâmetros são usados para personalizar o comportamento sem precisar subclassificar o componente novamente. Para controle programático, o widget expõe métodos públicos que a aplicação pode chamar.

O estilo de um widget customizado pode ser aplicado diretamente a ele, usando setStyleSheet. Isso cria um escopo de estilo isolado que não vaza para outros widgets. A regra é que estilos que definem a identidade visual do componente devem estar no próprio componente, não espalhados pela aplicação.

Um exemplo típico é um painel de informação com título, mensagem e botão de fechar. O painel define um sinal chamado closed que é emitido quando o botão é pressionado. A janela pai conecta esse sinal para remover o painel da tela. O painel não sabe nada sobre a janela pai. Ele apenas anuncia que foi fechado.

Com esse padrão, sua base de código acumula componentes reutilizáveis que aceleram o desenvolvimento de novas funcionalidades.

---

# 40. Temas e Estilização

Nesta faixa você vai aprender como aplicar temas visuais consistentes em uma aplicação PySide6, incluindo suporte a modo escuro.

O Qt Style Sheet, abreviado como QSS, é a linguagem de estilização do Qt. Sua sintaxe é similar ao CSS da web. Seletores de tipo, identificadores e pseudo-estados definem quais widgets são afetados e em qual estado visual. A maioria das propriedades visuais pode ser controlada: cor de fundo, cor de texto, fontes, bordas e espaçamento interno.

Para aplicar um tema a toda a aplicação, use o método setStyleSheet do objeto QApplication. Qualquer widget que não tiver seu próprio estilo herdará o estilo global. Para sobrescrever o estilo em um widget específico, chame setStyleSheet diretamente nele. O estilo local tem prioridade sobre o global.

Para identificar widgets específicos no QSS, use o método setObjectName. O seletor com cerquilha seguido do nome seleciona exatamente aquele widget. Isso é equivalente ao seletor de ID no CSS da web.

Para implementar troca de tema em tempo de execução, crie funções que aplicam folhas de estilo diferentes. Uma função ativa o modo claro, outra ativa o modo escuro. Conecte o acionamento de um interruptor na interface a essas funções. O Qt redesenha toda a aplicação imediatamente ao receber a nova folha de estilo.

Uma propriedade útil é a detecção automática do esquema de cores do sistema operacional. O Qt oferece uma propriedade que indica se o sistema está em modo escuro ou claro. Com isso, a aplicação pode seguir automaticamente a preferência do sistema sem intervenção do usuário.

A regra é definir o estilo global no QApplication e estilos específicos nos widgets individuais. Não pulverize folhas de estilo por toda a aplicação sem organização. Considere carregar a folha de estilo de um arquivo do sistema de recursos, o que facilita a manutenção e permite trocar temas sem recompilar o código.

---

# 41. Leitura e Escrita de Arquivos

Nesta faixa você vai aprender como ler e escrever arquivos de texto, CSV e JSON em aplicações PySide6, integrando essas operações com os diálogos de arquivo do Qt.

A leitura e escrita de arquivos em Python é feita com o gerenciador de contexto with e o construtor open. O modo de abertura determina a operação: r para leitura, w para escrita e a para acréscimo ao final. A codificação UTF-8 deve ser sempre especificada para garantir que caracteres especiais funcionem em todos os sistemas operacionais.

Para arquivos CSV, use o módulo csv da biblioteca padrão do Python. O DictReader lê cada linha como um dicionário, onde as chaves são os nomes das colunas da primeira linha do arquivo. O DictWriter grava dicionários de volta. Uma observação importante para Windows: o parâmetro newline deve ser uma string vazia ao abrir arquivos CSV. Sem isso, cada linha no arquivo terá uma linha vazia entre elas no Windows.

Para arquivos JSON, o módulo json da biblioteca padrão serializa dicionários e listas. O método load lê do arquivo, e dump grava. Para facilitar a leitura humana, passe o parâmetro indent com um número de espaços. Para garantir que caracteres não ASCII sejam gravados como estão em vez de sequências escapadas, use ensure_ascii como falso.

Para conectar essas operações com a interface, use os diálogos de arquivo do Qt antes de abrir o arquivo. O diálogo de abertura retorna o caminho selecionado pelo usuário. O diálogo de salvar retorna onde o usuário quer guardar. Sempre verifique se o caminho retornado é válido antes de tentar abrir o arquivo.

O Qt também oferece uma API própria para JSON, o QJsonDocument. Ela é necessária quando você precisa interoperar com QML ou com o sistema de variantes do Qt. Para todos os outros casos, a biblioteca padrão do Python é mais simples e preferível.

A regra é sempre usar a codificação UTF-8 explicitamente. Nunca deixe o sistema decidir. Encoding incorreto é uma das causas mais comuns de bugs difíceis de reproduzir em máquinas com localização diferente.

---

# 42. SQLite com a Biblioteca Padrão

Nesta faixa você vai aprender como usar o banco de dados SQLite em aplicações PySide6 usando a biblioteca sqlite3 do Python, sem precisar do módulo QtSql.

O SQLite é um banco de dados relacional que armazena tudo em um único arquivo. A biblioteca sqlite3 do Python já inclui suporte completo a ele, sem instalação adicional. Para aplicações desktop que precisam de persistência estruturada sem um servidor de banco de dados, o SQLite é a escolha padrão.

O ponto de entrada é a função connect, que recebe o caminho do arquivo de banco. Se o arquivo não existir, é criado automaticamente. O gerenciador de contexto with garante que as transações sejam confirmadas automaticamente ao final do bloco. Se ocorrer um erro, as mudanças são revertidas.

Para criar a estrutura do banco, execute um comando SQL de criação de tabela com a cláusula de existência condicional. Isso garante que a tabela só é criada se ainda não existir. Chame essa função de inicialização antes de exibir qualquer janela.

Para as operações básicas, insira linhas com INSERT, leia com SELECT, atualize com UPDATE e remova com DELETE. A regra crítica é nunca construir queries com f-strings ou concatenação de strings quando os dados vêm do usuário. Use sempre o parâmetro de interrogação como marcador de posição e passe os valores como tupla. Isso previne ataques de injeção de SQL de forma automática.

Para acessar os resultados por nome de coluna em vez de posição numérica, configure a propriedade row_factory da conexão como sqlite3.Row antes de executar queries. Isso torna o código mais legível e resistente a mudanças na ordem das colunas.

Para exibir os dados em um QTableWidget, crie uma função que lê todas as linhas do banco e as insere no widget. Chame essa função sempre que os dados mudarem. Um padrão útil é uma flag booleana que indica se a tabela já foi inicializada, para evitar que o sinal de mudança de item dispare operações de banco durante o preenchimento inicial.

---

# 43. REST APIs com QThread

Nesta faixa você vai aprender como consumir APIs REST em uma aplicação PySide6 sem bloquear a interface, usando a biblioteca requests em uma thread separada.

A biblioteca requests é a forma mais popular de fazer requisições HTTP em Python. Ela oferece uma interface simples e legível para GET, POST e outros métodos. O problema é que requisições de rede podem levar vários segundos. Se você as fizer na thread principal, a interface congela durante a espera.

A solução é criar uma subclasse de QThread para encapsular a requisição. O método run, que é executado na thread separada, faz a requisição, processa a resposta e emite um sinal com os dados prontos. O sinal carrega os dados como um objeto Python, normalmente um dicionário ou lista. A janela principal recebe esse sinal e atualiza a interface.

Para GET, o método principal da biblioteca requests recebe a URL, parâmetros de query como dicionário e cabeçalhos como dicionário. O timeout deve ser sempre definido. Sem timeout, uma requisição a um servidor que não responde deixa a thread presa para sempre. Após a requisição, chame raise_for_status para lançar uma exceção em caso de erro HTTP como quatro zero quatro ou cinco zero zero.

Para POST com dados JSON, passe o dicionário com os dados usando o parâmetro json. A biblioteca cuida de serializar e definir o cabeçalho de tipo de conteúdo automaticamente. Para autenticação com token, adicione o cabeçalho Authorization com o prefixo Bearer.

Um detalhe importante sobre reutilização de threads: não chame start em uma thread que já está rodando. Verifique se a thread está em execução antes de iniciar uma nova requisição. Uma abordagem comum é desabilitar o botão de busca enquanto a thread está ativa e reabilitá-lo quando receber os dados ou o erro.

A regra é que chaves de API nunca devem estar fixas no código. Use variáveis de ambiente ou arquivos de configuração para armazená-las. Isso protege credenciais de vazar em repositórios de código.

---

# 44. Multimídia: Áudio e Vídeo

Nesta faixa você vai aprender como reproduzir arquivos de áudio e vídeo em uma aplicação PySide6 usando o módulo QtMultimedia.

O Qt oferece o QMediaPlayer como controlador central de reprodução de mídia. Ele gerencia o estado de reprodução, a posição e a duração do arquivo. Para áudio, você conecta um objeto QAudioOutput ao player. Esse objeto controla o volume e o dispositivo de saída. Para vídeo, você conecta um QVideoWidget, que é o widget onde o vídeo é exibido na janela.

Para carregar uma mídia, defina a fonte do player como uma URL apontando para o arquivo. Para arquivos locais, converta o caminho com a função fromLocalFile. Em seguida, chame play para iniciar.

Os três comandos de controle são play, pause e stop. O volume é um número de ponto flutuante entre zero e um. O objeto QAudioOutput aceita o método setVolume com esse intervalo.

Para exibir uma barra de progresso sincronizada com a reprodução, conecte dois sinais do player. O sinal durationChanged atualiza o máximo da barra quando o arquivo é carregado. O sinal positionChanged atualiza o valor atual da barra enquanto a mídia toca. Para o slider inverso, quando o usuário arrasta, conecte o sinal sliderMoved ao método setPosition do player.

Uma aplicação comum é carregar imagens da internet e exibi-las em um QLabel. O fluxo é: fazer a requisição HTTP, receber os bytes da resposta, criar um QPixmap a partir desses bytes com o método loadFromData, e atribuir o pixmap ao label. Isso deve ser feito em uma thread separada para não bloquear a interface enquanto a imagem é baixada.

Os codecs suportados dependem do sistema operacional. Para máxima compatibilidade, use MP3 para áudio e MP4 com H.264 para vídeo. Se o módulo QtMultimedia não estiver disponível, instale o pacote adicional de addons do PySide6.

---

# 45. Projetos de Referência

Nesta faixa você vai conhecer quatro projetos de referência que demonstram como os conceitos do PySide6 se combinam em aplicações reais.

O primeiro projeto é uma calculadora. Ela usa um grid layout para organizar os botões em uma grade, um campo de texto em modo somente leitura como display, e o ciclo completo de sinal e slot para processar cada tecla pressionada. O padrão de captura de variável em lambdas é essencial aqui: cada botão captura seu próprio rótulo no momento da criação para que o slot possa identificar qual botão foi pressionado. A avaliação da expressão matemática usa a função eval do Python com tratamento de exceção para capturar expressões inválidas.

O segundo projeto é um gerenciador de notas. Ele usa o QTextEdit para edição de texto com formatação rica, o QFileDialog para abrir e salvar arquivos, e o sistema de abas com QTabWidget para gerenciar múltiplos documentos ao mesmo tempo. O closeEvent rastreia mudanças não salvas e pergunta ao usuário o que fazer. O título da janela exibe o nome do arquivo atual e um asterisco quando há mudanças pendentes.

O terceiro projeto é um visualizador de imagens. Ele carrega imagens em um QPixmap, redimensiona para caber na janela mantendo a proporção, e implementa o resizeEvent para ajustar automaticamente quando a janela é redimensionada. É um exemplo claro de widget customizado que encapsula o QLabel com lógica de escala.

O quarto projeto é um navegador web embutido. Ele usa o QWebEngineView, que incorpora o mecanismo de renderização Chromium diretamente na aplicação. Uma barra de endereços e botões de navegação são widgets normais do Qt que controlam o QWebEngineView através de seus métodos e sinais.

A lição comum a todos esses projetos é que cada funcionalidade complexa se decompõe em peças pequenas e familiares: um widget para cada responsabilidade, sinais para comunicação, layouts para organização e slots para reagir a eventos. A combinação dessas peças é o que cria aplicações completas.

---

# 46. Multithreading e GUIs Responsivas

Nesta faixa você vai aprender como manter a interface responsiva enquanto tarefas pesadas rodam em segundo plano.

A regra mais fundamental do Qt é que apenas a thread principal pode modificar widgets. Qualquer operação lenta executada na thread principal trava a interface. O usuário vê a janela congelada e o sistema operacional pode exibir a mensagem de que o programa não está respondendo.

A solução é o padrão de worker com moveToThread. Você cria um objeto de trabalho derivando de QObject, não de QThread. Esse objeto define um método de execução e sinais para comunicar progresso e resultado. Na janela, você cria uma QThread, move o worker para ela, conecta o sinal de início da thread ao método de execução do worker e conecta os sinais de progresso e conclusão a slots na thread principal. Ao iniciar a thread, o worker começa a executar em paralelo.

Quando o worker termina, ele emite o sinal de conclusão. A thread se encerra, e os objetos são liberados com deleteLater. Esse método adia a destruição para o momento correto no event loop, evitando erros de acesso a memória liberada.

Para tarefas curtas e independentes que podem rodar em paralelo, use o QThreadPool com QRunnable. O pool gerencia um conjunto fixo de threads e distribui as tarefas automaticamente. Como o QRunnable não é um QObject, ele não pode ter sinais próprios. O padrão é criar um objeto auxiliar derivado de QObject apenas para os sinais e referenciá-lo dentro do runnable.

Para atrasar uma ação sem bloquear a interface, use QTimer com singleShot. Isso agenda a execução para depois de um intervalo, sem criar threads e sem suspender o event loop.

Os três erros mais comuns são: atualizar widgets de dentro de uma thread de trabalho, usar time.sleep na thread principal, e não chamar deleteLater nos objetos da thread ao concluir. Os dois primeiros travam ou crasham. O terceiro causa vazamento de memória.

---

# 47. GUIs Responsivas com Operações Longas

Esta faixa aprofunda o padrão de manter a interface responsiva, com foco na comunicação de progresso ao usuário durante operações de longa duração.

Quando uma operação pode levar vários segundos, o usuário precisa de feedback. Duas respostas imediatas comunicam que o sistema está trabalhando: desabilitar o botão que iniciou a operação e mostrar uma mensagem na barra de status. Isso evita que o usuário clique novamente e inicie uma segunda operação em paralelo.

O QProgressBar é o componente padrão para exibir progresso numérico. O worker emite um sinal de progresso a cada iteração, geralmente um número de zero a cem. Na thread principal, o slot conectado atualiza o valor da barra. Como sinais entre threads são automaticamente enfileirados pelo event loop, essa atualização é segura.

Quando o resultado chega, o slot na thread principal reabilita o botão, atualiza a barra com cem por cento e processa os dados. Uma mensagem temporária na barra de status com a duração de alguns segundos confirma a conclusão.

Uma armadilha comum é tentar usar processEvents dentro de um loop longo como substituto de threading. Isso processa os eventos pendentes sem criar threads, o que parece funcionar para tarefas simples. O problema é que o código permanece na thread principal. Operações de IO bloqueiam de qualquer forma, e o usuário ainda não pode interagir livremente com a interface durante o processamento.

A regra é clara: se a operação pode travar o event loop por mais de duzentos milissegundos, use uma thread.

---

# 48. Tratamento de Erros e Debugging

Nesta faixa você vai aprender como tratar erros em aplicações PySide6 de forma profissional e como depurar problemas com sinais e slots.

Exceções que escapam de um slot podem causar comportamento indefinido no event loop do Qt. A prática correta é capturar exceções dentro de cada slot e comunicar a falha ao usuário de forma controlada. Para erros esperados, como arquivo não encontrado, use QMessageBox.warning. Para erros inesperados, use QMessageBox.critical. Nunca deixe uma exceção propagar silenciosamente.

Para registro de eventos e diagnóstico, use o módulo logging da biblioteca padrão do Python. Configure o nível de log no início do programa. Use o nível debug para informações detalhadas de desenvolvimento, info para eventos normais, warning para situações incomuns e error para falhas. Em produção, configure o log para gravar em arquivo para que erros relatados por usuários possam ser investigados.

Depurar problemas com sinais e slots é desafiador porque sinais desacoplam o código. Um sinal é emitido num lugar, e o slot é executado em outro. Para rastrear o fluxo, adicione slots de debug temporários que apenas registram no log quando um sinal é emitido. Coloque esses slots antes do slot real para confirmar que o sinal está sendo emitido corretamente.

Outra estratégia é adicionar pontos de parada no IDE dentro de slots. O depurador para a execução como esperado. Lembre-se, porém, que o depurador não para automaticamente no momento em que um sinal é emitido, apenas quando a execução chega ao slot.

O padrão profissional combina os três elementos: tratamento de exceção direcionado por tipo de erro, logging persistente para diagnóstico pós-fato, e depurador interativo para análise de comportamento incorreto sem crash.

---

# 49. Testes Automatizados de GUI

Nesta faixa você vai aprender como escrever testes automatizados para aplicações PySide6, cobrindo tanto a lógica de negócio quanto a interação com a interface.

A ferramenta padrão para testes em Python é o pytest. Para testar interfaces Qt, a extensão pytest-qt adiciona um fixture chamado qtbot. O qtbot permite criar widgets, simular cliques de mouse, simular pressionamentos de tecla e esperar por sinais.

Um teste básico de interface cria a janela, registra ela no qtbot e simula uma interação. Em seguida, verifica se o estado da interface corresponde ao esperado. Por exemplo, após clicar um botão, o texto de um rótulo deve mudar para o valor esperado.

Para testes que envolvem operações assíncronas, como workers em threads, o qtbot oferece o método waitSignal. Dentro de um bloco with waitSignal, você chama o código que inicia a operação assíncrona. O teste aguarda o sinal com um timeout definido. Se o sinal não chegar dentro do tempo, o teste falha. Isso evita que testes assíncronos passem por coincidência de tempo.

A separação entre lógica e interface é fundamental para testes eficientes. Coloque as regras de negócio em classes Python puras, sem nenhuma dependência do Qt. Essas classes podem ser testadas com pytest simples, sem precisar do qtbot. Isso torna os testes mais rápidos e mais fáceis de escrever.

Para simulação de teclado e mouse de baixo nível, o Qt oferece o módulo QTest. Ele é útil quando você precisa testar interações que o qtbot não suporta diretamente.

A regra é cobrir a lógica de negócio com testes unitários puros e cobrir os fluxos críticos de interface com testes de integração usando qtbot. Não duplique a cobertura de lógica no nível de widget. Cada tipo de teste deve testar o que só ele pode testar.

---

# 50. UX e Design de Interface

Nesta faixa você vai aprender os princípios de experiência do usuário que se aplicam diretamente ao desenvolvimento de interfaces com PySide6.

O primeiro princípio é o agrupamento visual. Controles relacionados devem estar próximos entre si. O QGroupBox cria uma caixa com título que agrupa visualmente os elementos. Espaçadores em layouts separam grupos distintos. O usuário percebe a estrutura sem precisar lê-la explicitamente.

O segundo princípio é o uso de layouts gerenciados. Nunca use coordenadas absolutas em aplicações de produção. Layouts como QVBoxLayout, QHBoxLayout e QGridLayout garantem que a interface se adapta a diferentes resoluções, diferentes tamanhos de fonte e diferentes escalas de DPI. Uma interface com posições fixas quebra em qualquer ambiente diferente do desenvolvimento.

O terceiro princípio é o feedback de progresso. Quando uma operação demora, o usuário precisa saber que o programa está trabalhando. O padrão correto é desabilitar o botão que iniciou a operação, mostrar uma mensagem na barra de status e atualizar uma barra de progresso. Quando a operação termina, reabilite o botão e mostre uma mensagem de conclusão por alguns segundos.

O quarto princípio é a consistência de ações. Use um único objeto QAction para cada operação da aplicação. Esse objeto é atribuído ao menu e à toolbar ao mesmo tempo. Ícone, texto, atalho de teclado e dica de ferramenta são definidos uma única vez. Isso garante que qualquer mudança na ação reflita em todos os lugares automaticamente.

O quinto princípio é o teste com dados extremos. Antes de entregar uma interface, teste com textos longos, com janela redimensionada ao mínimo e ao máximo, e com fontes maiores. Widgets devem expandir corretamente, texto deve ser recortado ou envolvido, e nada deve sobrepor outro elemento.

---

# 51. Atalhos de Teclado, Menus e Toolbars

Nesta faixa você vai aprender como estruturar menus e toolbars em uma janela principal, reutilizando ações e respeitando os atalhos de teclado que os usuários já conhecem.

O mecanismo central é o QAction. Uma ação encapsula uma operação da aplicação. Ela tem um ícone, um texto de label, uma dica de ferramenta, um atalho de teclado e um sinal triggered. Quando o usuário clica no menu, no botão da toolbar ou pressiona o atalho, o mesmo sinal é emitido. Você conecta esse sinal ao método que realiza a operação uma única vez.

Para construir o menu, você acessa a barra de menus da janela principal, adiciona um menu e adiciona a ação a ele. Para construir a toolbar, você cria uma toolbar e adiciona a mesma ação. O objeto QAction é compartilhado entre os dois. Se você desabilitar a ação, ela fica inativa tanto no menu quanto na toolbar automaticamente.

Os aceleradores mnemônicos são ativados com o caractere e comercial antes de uma letra no texto da ação. O usuário pode pressionar Alt mais essa letra para ativar o menu ou a ação sem usar o mouse. Isso é importante para acessibilidade e para usuários avançados que preferem o teclado.

Os atalhos de teclado padrão devem ser respeitados. Os usuários esperam que Control mais O abra um arquivo, Control mais S salve, Control mais Z desfaça e Control mais Y refaça. Usar esses atalhos para outras funções causa confusão. O Qt oferece constantes de atalhos padrão que você pode usar sem precisar especificar a combinação de teclas manualmente.

A regra para toolbars é colocar apenas as ações mais frequentes. Não duplique toda a barra de menus na toolbar. Uma toolbar com dez ícones sem labels é difícil de usar. Limite a toolbar às cinco ou seis ações que o usuário realiza dezenas de vezes por dia.

---

# 52. Acessibilidade

Nesta faixa você vai aprender como tornar uma aplicação PySide6 utilizável por pessoas com diferentes necessidades, incluindo usuários de leitores de tela e de navegação por teclado.

O Qt se integra automaticamente com as APIs de acessibilidade nativas de cada plataforma. No Windows, ele usa a API de UI Automation. No macOS, usa o Accessibility Framework. No Linux, usa o ATK. Isso significa que leitores de tela como o NVDA no Windows ou o Orca no Linux já conseguem anunciar widgets padrão do Qt sem configuração adicional.

Para melhorar a experiência com leitores de tela, adicione metadados de acessibilidade a cada widget interativo. O nome acessível é o que o leitor de tela anuncia quando o usuário navega ao widget. A descrição acessível fornece informação adicional sobre o propósito do controle. Para botões com apenas ícones, sem texto visível, o nome acessível é obrigatório.

A navegação por teclado usa a tecla Tab para percorrer os controles em ordem. Por padrão, o Qt define essa ordem com base na posição dos widgets na tela. Quando a ordem padrão não é intuitiva, defina a ordem explicitamente com o método setTabOrder. Passe o widget atual e o próximo como argumentos.

Para o contraste visual, evite transmitir informação apenas por cor. Um campo inválido que fica vermelho é inacessível para usuários com daltonismo. Combine a cor com um ícone de aviso ou uma mensagem de texto. Essa regra vale para qualquer estado visual que comunique algo ao usuário.

Para escalabilidade, use layouts gerenciados e fontes relativas. O usuário pode ter configurado o sistema operacional para exibir textos em tamanhos maiores. Com layouts gerenciados, a interface se adapta sem sobreposição. Com fontes fixas em tamanho absoluto, a interface quebra.

Com esses ajustes, a aplicação se torna utilizável para um público muito mais amplo, sem custo significativo de desenvolvimento.

---

# 53. Internacionalização e Localização

Nesta faixa você vai aprender como preparar uma aplicação PySide6 para ser traduzida para múltiplos idiomas.

Internacionalização é a prática de escrever o código de forma que ele possa ser adaptado a diferentes idiomas e culturas. O Qt oferece uma infraestrutura completa para isso, composta por ferramentas e uma API de runtime.

O primeiro passo é marcar todas as strings visíveis ao usuário para tradução. Em métodos de classes que herdam de QObject, isso é feito chamando o método tr com a string. Esse método retorna a string traduzida em runtime, ou a string original se a tradução não estiver disponível.

O segundo passo é extrair as strings marcadas com a ferramenta lupdate. Ela analisa o código fonte e gera um arquivo de tradução no formato ts, que é XML. Esse arquivo é enviado para tradutores.

O terceiro passo é traduzir as strings no Qt Linguist, que é a ferramenta visual do Qt para tradução. O tradutor abre o arquivo ts, vê o texto original e preenche a tradução em cada linha.

O quarto passo é compilar o arquivo de tradução com a ferramenta lrelease. Ela gera um arquivo binário qm, que é o formato que o Qt carrega em runtime.

O quinto passo é carregar a tradução no início do programa. Crie um objeto QTranslator, carregue o arquivo qm correspondente ao idioma do sistema e instale o tradutor na aplicação. O Qt usa o nome do locale do sistema para selecionar o arquivo correto.

A regra mais importante é fazer tudo isso desde o início do projeto. Adicionar internacionalização depois que o código está escrito exige encontrar e marcar cada string espalhada pelo código, o que é tedioso e propenso a omissões.

Uma consideração importante sobre layout: textos traduzidos podem ser trinta a cinquenta por cento mais longos que o original em inglês. Certifique-se que os layouts expandem os widgets adequadamente e que textos longos não são cortados.

---

# 54. Qt Quick e QML

Nesta faixa você vai conhecer o Qt Quick, o framework declarativo do Qt para interfaces modernas com animações fluidas.

O Qt Quick usa a linguagem QML para descrever interfaces. QML é uma linguagem declarativa, similar ao CSS em alguns aspectos, mas com capacidade de expressar lógica, bindings de propriedade e animações. A ideia central é que você descreve o que a interface deve ser, e o Qt cuida de como renderizá-la.

A estrutura básica de um arquivo QML é uma hierarquia de elementos. O elemento raiz é geralmente uma janela ou um retângulo. Dentro dele, você aninha outros elementos como botões, textos e imagens. Cada elemento tem propriedades que controlam sua aparência e comportamento. O sistema de ancoragem posiciona elementos em relação uns aos outros sem coordenadas absolutas.

As animações em QML são expressas diretamente na definição dos elementos. Você declara que uma propriedade deve ser animada ao mudar de valor. Por exemplo, quando a cor de um retângulo muda, você pode declarar que a mudança deve ocorrer com uma transição suave de duzentos milissegundos. O Qt executa a interpolação automaticamente.

Para integrar Python com QML, você usa o QQmlApplicationEngine. Ele carrega o arquivo QML e exibe a interface. Para expor dados e lógica Python ao QML, você registra objetos como propriedades de contexto. O QML pode então ler propriedades e chamar métodos desses objetos.

Os animators são uma variação das animações que rodam na thread de renderização em vez da thread principal. Isso permite animações de rotação e escala muito fluidas sem sobrecarregar a thread da interface.

A regra sobre quando usar QML versus Widgets é a seguinte: use Widgets para aplicações de produtividade clássicas, como editores, planilhas e formulários. Use QML para interfaces com animações intensas, design muito customizado, ou quando o visual precisa ser completamente diferente do padrão da plataforma.

---

# A. Troubleshooting e FAQ

Nesta faixa você vai conhecer os problemas mais frequentes em aplicações PySide6 e as soluções diretas para cada um.

O problema mais comum é a interface que congela durante uma operação. A causa é sempre a mesma: a operação está rodando na thread principal. A solução é mover o código para um worker em uma thread separada e comunicar o resultado de volta via sinal.

No Linux, uma mensagem de erro que diz que não foi possível carregar o plugin de plataforma xcb indica que bibliotecas do sistema estão faltando. As bibliotecas necessárias incluem libxcb-xinerama, libxcb1, libxkbcommon-x11 e libgl1. Ao empacotar a aplicação com PyInstaller, a pasta platforms contendo o plugin libqxcb precisa estar incluída no pacote.

No Windows, crashes silenciosos geralmente indicam conflito de DLLs ou incompatibilidade de arquitetura. A ferramenta Dependencies, disponível gratuitamente, permite visualizar quais DLLs o executável precisa e quais estão faltando. Confirme que o interpretador Python e as bibliotecas Qt são ambos de sessenta e quatro bits.

Quando ícones ou folhas de estilo não carregam após empacotamento, a causa são caminhos relativos que funcionam em desenvolvimento mas não existem no executável final. A solução é usar o sistema de recursos do Qt para embutir os assets, ou usar o atributo frozen do módulo sys para detectar se está rodando como executável e resolver o caminho de base dinamicamente.

Quando sinais não são disparados, verifique quatro coisas: o objeto que emite o sinal ainda existe e não foi destruído pelo coletor de lixo, a assinatura do sinal bate com a do slot, não há um sleep bloqueando o event loop antes da emissão, e o slot está corretamente conectado antes da ação ser acionada.

Quando clicar um botão não faz nada, confirme que o sinal clicked foi conectado ao método correto, que o método existe e está definido com self como primeiro parâmetro, e que o objeto da janela não foi recriado depois da conexão.

Para obter o visual nativo do sistema operacional em vez do visual padrão do Qt, aplique o estilo da plataforma com setStyle. O Fusion é um estilo moderno e consistente que funciona bem em todas as plataformas como alternativa.

Com esse guia de troubleshooting, você resolve a maioria dos problemas rapidamente sem precisar buscar a causa no código inteiro.
