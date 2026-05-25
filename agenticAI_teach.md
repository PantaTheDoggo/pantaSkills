
# Teach: Agentic Coding with Claude Code

Bem-vindo. Este é um material em áudio derivado da skill Agentic Coding with Claude Code. Cada faixa cobre um conceito independente. Você pode ouvir em qualquer ordem.

---

# 1. Context Engineering — Por Que o Contexto Importa Mais que o Prompt

Context engineering é a disciplina que decide qual informação chega ao modelo em cada etapa. Nesta faixa, vamos entender por que ela vai muito além de escrever bons prompts.

Para começar, é importante distinguir prompt engineering de context engineering. Prompts são textos estáticos escritos antes da execução. O contexto é dinâmico. Ele cresce e muda a cada interação do agente.

Em seguida, precisamos saber onde o verdadeiro trabalho acontece. O desafio principal não está na chamada ao modelo de linguagem em si. Está no sistema ao redor, chamado de agent harness. Esse harness gerencia as chamadas de ferramentas, o loop de execução e as barreiras de segurança. Mais importante, ele decide qual parte do contexto enviar ao modelo a cada passo.

O contexto chega de várias fontes ao mesmo tempo. Ele inclui as instruções do desenvolvedor, a entrada do usuário e os resultados das ferramentas, entre outras. Em agentes de longa duração, essas fontes se acumulam sem parar. Por isso, selecionar e comprimir o contexto torna-se uma necessidade, não um opcional.

A regra central é esta: trate context engineering como uma disciplina separada de prompt engineering. A maior parte da engenharia real de um agente acontece no harness, e não nos textos dos prompts. Um equívoco frequente é dedicar todo o esforço ao prompt e ignorar como o contexto evolui ao longo da sessão.

Context engineering é a fundação de qualquer agente de alta qualidade. Quem domina o harness, domina o comportamento do agente.

---

# 2. Os Três Problemas do Contexto Sem Controle

Quando o contexto cresce sem controle, surgem problemas sérios. Nesta faixa, vamos conhecer as três principais classes de problemas e por que ignorá-los compromete toda a sessão.

O primeiro problema chama-se context poisoning, ou envenenamento de contexto. Ele ocorre quando uma alucinação do modelo ou um erro de ferramenta entra no histórico da sessão. A partir daí, esse erro contamina todas as respostas seguintes. O modelo trata o erro como fato e constrói raciocínio sobre ele.

O segundo é o context confusion, ou confusão de contexto. Nesse caso, informação irrelevante está presente no contexto. O modelo não consegue ignorá-la e acaba sendo influenciado por ela. A resposta desvia do que realmente era necessário.

Em seguida, há o context clash, ou colisão de contexto. Esse problema aparece quando partes do contexto se contradizem. O modelo recebe informações conflitantes e produz comportamento imprevisível. Sem uma fonte de verdade clara, a qualidade degrada rapidamente.

Além desses problemas qualitativos, o contexto sem controle traz consequências práticas. A janela de contexto é limitada e pode ser excedida. O custo por requisição aumenta com o tamanho do contexto. A latência cresce também. E a qualidade piora progressivamente à medida que o contexto acumula ruído.

A regra é clara: nunca deixe o contexto crescer sem estrutura, seleção ou controle. Em agentes que funcionam por muitos turnos, o gerenciamento de contexto é tão importante quanto a lógica do próprio agente.

---

# 3. As Três Camadas de Memória do Claude Code

O Claude Code organiza a memória persistente em três camadas. Nesta faixa, vamos entender cada camada e quando usar cada uma.

A primeira camada é a project memory, ou memória de projeto. Ela fica num arquivo chamado CLAUDE.md na raiz do projeto. Seu escopo é a equipe inteira. Ela é versionada junto com o código, o que significa que todos os membros do time a compartilham. Nela ficam a arquitetura do projeto, os padrões adotados e as convenções de código.

A segunda camada é a user memory, ou memória do usuário. Ela fica no diretório pessoal do desenvolvedor, dentro da pasta de configuração do Claude. Seu escopo é pessoal e abrange todos os projetos daquele usuário. Aqui ficam preferências individuais, atalhos e hábitos de trabalho.

A terceira camada são os dynamic imports, ou importações dinâmicas. Eles permitem referenciar arquivos de contexto externos de dentro de qualquer CLAUDE.md. Basta usar o símbolo arroba seguido do caminho do arquivo. Com isso, é possível modularizar o contexto por domínio, carregando apenas o que for necessário para cada tarefa.

A regra é usar importações dinâmicas para manter os arquivos CLAUDE.md enxutos. Em vez de um único arquivo enorme, você cria contextos específicos por domínio e os importa conforme necessário. Um erro comum é adicionar entradas ao CLAUDE.md via scripts sem verificar duplicatas. A prática correta é checar se a entrada já existe antes de adicionar qualquer linha nova.

As três camadas trabalham juntas. O projeto define o contexto compartilhado, o usuário define suas preferências, e as importações dinâmicas trazem contexto específico quando necessário.

---

# 4. As Quatro Estratégias de Context Engineering

O Claude Code aplica quatro estratégias para gerenciar o contexto ao longo de uma sessão. Nesta faixa, vamos conhecer cada uma delas e como se complementam.

A primeira estratégia é escrever, ou persistir contexto. Quando o contexto é gravado na hierarquia de memória, ele sobrevive entre sessões. O desenvolvedor não precisa reintroduzir as mesmas informações a cada nova conversa.

A segunda estratégia é selecionar contexto de forma inteligente. O Claude varre diretórios automaticamente em busca de arquivos de contexto relevantes. Ele prioriza os mais recentes e os mais frequentemente acessados. O desenvolvedor também pode adicionar memória persistente manualmente, informando se a entrada deve ir para o nível de projeto ou de usuário. Antes de editar um arquivo, o Claude recupera automaticamente o estilo de código existente no projeto.

Em seguida vem a terceira estratégia: comprimir o contexto. O comando de limpeza reseta completamente o histórico da conversa, mas preserva as memórias de projeto e de usuário. O comando de compactação, por outro lado, sumariza a conversa em forma comprimida, mantendo as decisões-chave e descartando detalhes menores. A regra é usar a compactação quando o contexto acumulou muito mas o trabalho ainda não terminou. Use a limpeza quando a direção da conversa ficou confusa ou irrelevante.

A quarta estratégia é isolar o contexto em subagentes. Cada subagente roda em sua própria janela de contexto, sem herdar o histórico completo do agente principal. O agente principal atua como gerente e delega tarefas a especialistas. A regra é usar subagentes para tarefas paralelas ou especializadas. Nunca force o agente principal a fazer tudo de uma vez com todo o contexto disponível.

Essas quatro estratégias, escrever, selecionar, comprimir e isolar, formam o conjunto completo de ferramentas de context engineering. Usadas juntas, elas mantêm o contexto relevante, enxuto e organizado ao longo de sessões longas.

---

# 5. Context Switching Dinâmico com Hooks

É possível automatizar a troca de contexto no Claude Code usando hooks. Nesta faixa, vamos ver como um script conectado ao ciclo de vida do agente pode carregar o contexto certo no momento certo.

Para começar, o hook chamado UserPromptSubmit dispara sempre que o usuário envia um prompt. A ele podemos conectar um script que examina duas informações: o branch Git ativo e o texto da query do usuário. Com base nessas informações, o script decide qual arquivo de contexto carregar automaticamente.

Por exemplo, ao trabalhar no branch de autenticação, o script pode carregar o contexto do sistema de autenticação. Ao trabalhar num branch de hotfix, carrega o contexto de produção. Da mesma forma, se a query menciona banco de dados, o contexto de banco de dados é injetado. Se menciona interface de programação, o contexto de API entra no lugar.

A regra essencial deste padrão é a idempotência. O script deve verificar se a referência ao arquivo de contexto já está no CLAUDE.md antes de adicioná-la. Isso evita que o arquivo cresça indefinidamente a cada prompt enviado. O operador de redirecionamento direto, sem verificação prévia, é o principal erro a evitar aqui.

O context switching dinâmico elimina a necessidade de o desenvolvedor gerenciar manualmente qual contexto está ativo. O contexto certo aparece automaticamente conforme o trabalho muda de domínio.

---

# 6. A Zona Goldilocks dos System Prompts

A Anthropic descreve uma zona ideal para system prompts chamada Goldilocks Zone, ou zona do equilíbrio perfeito. Nesta faixa, vamos entender os dois extremos problemáticos e como encontrar o meio-termo.

O primeiro extremo é o prompt excessivamente específico. Ele trata o modelo de linguagem como uma máquina de estados determinística. O desenvolvedor enumera cada passo, cada condição e cada caminho possível. O resultado é lógica engessada, manutenção custosa e falha inevitável em situações não previstas.

O segundo extremo é o prompt excessivamente vago. Ele oferece sinal insuficiente para um comportamento consistente. Sem guia acionável, o modelo assume contexto que não existe. Os limites de atuação ficam indefinidos. O agente se comporta de forma imprevisível de sessão para sessão.

O meio-termo aproveita o raciocínio do próprio modelo. Um bom prompt de nível médio tem cinco elementos. O primeiro é identidade e escopo claros: quem é o agente e o que ele cobre. O segundo são objetivos em vez de regras: defina a meta e deixe o agente escolher as ferramentas. O terceiro é um framework de raciocínio: passos gerais que funcionam em múltiplos cenários. O quarto são princípios como heurísticas, por exemplo, se múltiplas soluções existem, escolha a mais simples. O quinto são limites claros: quando escalar para um humano e com qual critério explícito.

A regra é preferir frameworks de raciocínio a fluxogramas. O modelo aplica princípios gerais a situações novas muito melhor do que segue scripts rígidos. Um equívoco frequente é prescrever cada passo do agente em vez de definir sua identidade, seu objetivo e seus princípios de decisão.

Prompts bem calibrados tornam o agente resiliente a situações inesperadas. Um framework de raciocínio funciona onde um script rígido inevitavelmente falha.

---

# 7. Spec-Driven Design — Especificar Antes de Implementar

Spec-driven design é a prática de criar um documento de especificação antes de iniciar qualquer implementação. Nesta faixa, vamos ver por que isso melhora radicalmente a qualidade do código gerado pelo agente.

O problema que este padrão resolve é direto. Sem contexto estruturado, o agente produz código inconsistente ao longo de sessões com múltiplos prompts. Cada novo prompt recomeça sem uma visão unificada do que está sendo construído.

O workflow começa ativando o modo de planejamento e selecionando o modelo mais avançado disponível. Em seguida, você descreve o projeto e pede ao agente para pesquisar e gerar a especificação. Esse documento é então salvo num arquivo dentro do diretório de memória do projeto. Ao implementar qualquer funcionalidade, você referencia o spec no prompt usando o símbolo arroba seguido do caminho do arquivo.

Um spec útil cobre as dimensões essenciais do projeto. Isso inclui a visão geral, o escopo mínimo viável, o modelo de dados, os requisitos de interface, a arquitetura técnica e as histórias de usuário principais.

A regra é usar o próprio modelo de linguagem para ajudar a gerar o spec inicial. O resultado será mais completo e estruturado do que uma especificação escrita manualmente em pouco tempo. Um equívoco frequente é pular esta etapa por parecer burocrática. Sem o spec, o agente perde coerência nas sessões longas.

O spec é o contrato que mantém o agente alinhado com a intenção do desenvolvedor ao longo de toda a implementação.

---

# 8. Plan Mode — Planejar Antes de Executar

O plan mode é o modo somente leitura do Claude Code. Nesta faixa, vamos entender quando ativá-lo e por que o modelo escolhido faz toda a diferença.

Em plan mode, o agente usa exclusivamente ferramentas de leitura. Ele pode pesquisar na web, ler arquivos e explorar o repositório. Nenhuma edição de arquivo ocorre. Esse isolamento é valioso porque permite pensar sem consequências: o agente pode explorar abordagens sem comprometer o código.

Os casos de uso principais são três. O primeiro é gerar a especificação antes de implementar. O segundo é explorar o repositório antes de decidir a abordagem. O terceiro é pesquisar APIs, ou interfaces de programação, e documentação externa. Em todos esses casos, o desenvolvedor quer informação e plano, não ação imediata.

A regra mais importante do plan mode é a escolha do modelo. Use sempre o modelo de raciocínio mais avançado disponível. Um plano de qualidade depende de raciocínio profundo. A qualidade do plano gerado afeta diretamente a qualidade de toda a implementação subsequente. Um equívoco frequente é usar um modelo mais leve para economizar. O plano ruim gera implementação ruim, e o custo total acaba maior.

Plan mode é a fase de investimento. Um bom plano reduz retrabalho, elimina inconsistências e torna cada prompt de implementação mais preciso.

---

# 9. Estrutura de Diretório de Memória

A organização dos arquivos de memória afeta diretamente o funcionamento das importações dinâmicas. Nesta faixa, vamos ver como estruturar o diretório de memória corretamente.

A recomendação é centralizar toda a memória de longo prazo em um único diretório chamado memory, dentro do projeto. Dentro desse diretório, crie subdiretórios por domínio. Um subdiretório para frontend, outro para spec, outro para backend. Cada um contém seu próprio arquivo de memória.

A regra crítica é de localização. O diretório memory deve ficar dentro do diretório de trabalho onde o Claude Code é aberto. Não no diretório pai. Não em um irmão. No diretório de trabalho ou em um de seus filhos.

A razão é técnica. Referências com o símbolo arroba são resolvidas em relação ao diretório de trabalho atual. Se o Claude Code for aberto no diretório pai do projeto, as referências não serão resolvidas. O contexto não será carregado, mesmo que os arquivos existam fisicamente no disco.

O erro a evitar é abrir o Claude Code no diretório raiz do repositório quando o projeto fica num subdiretório. Centralizar todo contexto de longo prazo no diretório memory permite reutilização entre sessões e facilita referenciar contextos específicos com importações dinâmicas em qualquer prompt.

---

# 10. Hierarquia Completa de Memória em Cinco Níveis

O Claude Code usa cinco níveis de memória, carregados de forma cumulativa do mais alto ao mais específico. Nesta faixa, vamos conhecer cada nível e dois comportamentos especiais de carregamento.

O primeiro nível é a política gerenciada. Fica em um diretório de sistema, controlado por DevOps ou TI. É a prioridade máxima e não pode ser sobrescrita por nenhum outro nível. Toda a organização compartilha esse contexto.

O segundo nível é a memória de usuário. Aplica-se a todos os projetos do usuário e fica no diretório pessoal de configuração do Claude. Prioridade alta, mas subordinada ao nível de política.

O terceiro nível é a memória de projeto. Fica no CLAUDE.md da raiz do projeto. É versionada com Git e compartilhada com a equipe.

O quarto nível são as regras de projeto. Ficam em arquivos Markdown dentro do diretório rules do ponto-claude. Cada arquivo cobre um domínio específico: segurança, linting, arquitetura. Útil para projetos grandes onde um único CLAUDE.md ficaria pesado demais.

O quinto nível é a memória local de projeto. Fica no arquivo CLAUDE.local.md, que deve estar no gitignore. É para overrides pessoais sem afetar o time.

Dois comportamentos de carregamento são importantes. O primeiro é a descoberta ascendente. Ao iniciar, o Claude busca arquivos de memória a partir do diretório de trabalho e sobe em direção à raiz do sistema de arquivos. Todos os CLAUDE.md encontrados no caminho são carregados e combinados.

O segundo é o carregamento preguiçoso. Arquivos de memória em subdiretórios abaixo do diretório de trabalho carregam somente quando o Claude acessa arquivos naquele subdiretório. Isso economiza tokens desnecessários na abertura da sessão.

A regra para projetos grandes é separar as regras por domínio no diretório rules do ponto-claude. Concentrar tudo em um único CLAUDE.md enorme prejudica a manutenção e carrega tokens desnecessários em cada sessão.

---

# 11. Adicionando Entradas de Memória

O Claude Code oferece três formas de adicionar entradas à memória persistente. Nesta faixa, vamos ver cada uma e como mantê-las eficazes ao longo do tempo.

O primeiro método é prefixar o texto com o símbolo de hash no prompt. Ao fazer isso, o Claude pede confirmação e armazena a entrada no arquivo de memória correspondente, seja no nível de projeto ou de usuário.

O segundo método é o comando de memória, que abre o arquivo de memória diretamente no editor. Isso permite edição manual e revisão completa do que está armazenado.

O terceiro método é o comando de inicialização. Ele escaneia o repositório inteiro e gera um CLAUDE.md automaticamente, incluindo a stack tecnológica, as variáveis de ambiente e a estrutura do projeto. É o ponto de partida ideal para projetos que ainda não têm memória configurada.

A regra central é manter arquivos de memória concisos e específicos. Memória excessiva ou vaga desperdiça tokens, confunde o modelo e reduz a qualidade das respostas. Cada entrada deve ter um propósito claro.

Um hábito útil após adicionar memória é limpar o histórico da conversa e verificar se o Claude responde com base na memória armazenada, e não no histórico da conversa atual. Isso confirma que a entrada foi salva corretamente e está sendo carregada.

---

# 12. Hooks — Tipos e Configuração

Hooks são comandos automáticos executados em pontos específicos do ciclo de vida do Claude Code. Nesta faixa, vamos conhecer os eventos disponíveis e como configurá-los corretamente.

Existem cinco eventos principais. O primeiro é PreToolUse, que dispara antes de qualquer ferramenta ser executada. O segundo é PostToolUse, que dispara após a execução de uma ferramenta. O terceiro é Notification, acionado quando o Claude envia notificações. O quarto é UserPromptSubmit, disparado quando o usuário submete um prompt. O quinto é Stop, que executa imediatamente antes do Claude finalizar a resposta.

Para configurar um hook, use o comando de hooks dentro do Claude Code. Selecione o evento desejado, defina o comando a executar e escolha o escopo: projeto ou usuário. Hooks de projeto ficam no arquivo settings.json dentro do ponto-claude. Hooks de usuário aplicam-se a todos os projetos.

Um detalhe importante é o campo matcher. Quando ele está vazio, o hook se aplica a todos os eventos do tipo, sem filtro adicional. Após configurar qualquer hook, reinicie o Claude Code para carregar as novas configurações.

A regra é manter hooks de alta frequência, como Stop e PostToolUse, leves e rápidos. Prefira comandos nativos do sistema operacional para tocar sons ou notificar, em vez de scripts com dependências pesadas. Hooks pesados em eventos de alta frequência introduzem latência perceptível em cada interação.

Um erro comum é não testar os hooks em isolamento antes de ativá-los. Hooks podem bloquear ações, modificar comportamento do agente e até disparar subagentes. Sempre teste separadamente antes de deixar ativo em produção.

---

# 13. Skills — Slash Commands Customizados

Skills são prompts reutilizáveis invocados como slash commands. Nesta faixa, vamos entender como criá-los, como eles funcionam e a regra de segurança mais importante.

Uma skill é um arquivo Markdown com frontmatter YAML. Esse arquivo fica dentro de um diretório com o nome da skill, dentro do diretório skills do ponto-claude. O nome da skill no frontmatter determina como o usuário a invoca pela interface.

O frontmatter tem dois papéis. Primeiro, ele é avaliado antes do corpo do prompt. Segundo, ele define quais ferramentas a skill pode usar. O corpo do arquivo contém as instruções da skill em si.

Dentro da skill, é possível injetar contexto dinâmico com um padrão especial. Ao colocar um ponto de exclamação seguido de um comando entre crases, o Claude executa esse comando antes de processar a skill e injeta o resultado como contexto. Por exemplo, injetar o status do Git ou as mudanças recentes antes de criar um commit. Esse é o padrão de recuperação antes de geração, aplicado diretamente na skill.

Também é possível passar argumentos ao invocar uma skill. O texto que vem após o nome da skill é substituído onde o placeholder de argumentos aparece no arquivo.

A regra de segurança mais importante é sempre definir quais ferramentas a skill pode usar no frontmatter. Sem essa restrição, um contexto envenenado pode fazer o agente executar ações não intencionais com acesso total ao sistema. O princípio do menor privilégio se aplica diretamente aqui: forneça apenas as ferramentas que a skill realmente precisa.

---

# 14. Rewind — Checkpointing e Desfazer

O Claude Code cria checkpoints automáticos antes de cada edição de arquivo. Nesta faixa, vamos entender como usar o sistema de rewind e o que ele não cobre.

Para invocar o rewind, pressione Escape duas vezes ou use o comando de rewind. Isso abre uma interface com três opções de restauração.

A primeira opção restaura o código e a conversa. Ela reverte os arquivos modificados e o histórico da sessão. É a opção mais usada quando se quer desfazer completamente uma linha de experimentação.

A segunda opção restaura apenas a conversa. Ela reverte o histórico da sessão, mas mantém as edições nos arquivos. Útil quando a direção da conversa foi ruim, mas o código gerado é aproveitável.

A terceira opção restaura apenas o código. Ela reverte os arquivos, mas mantém o histórico da conversa. Após restaurar o código, é possível re-emitir o prompt com ajustes, pois o contexto da sessão permanece intacto.

Os checkpoints persistem por trinta dias. Isso oferece uma janela ampla para desfazer decisões de implementação.

Há limitações importantes a conhecer. Comandos de shell executados pelo Claude não são rastreados e não podem ser revertidos pelo rewind. Edições feitas manualmente fora do Claude Code também não são capturadas. Por fim, o rewind não substitui o Git. Ele é uma rede de segurança local de curto prazo, não um histórico permanente. A regra é usá-lo como proteção para experimentos e combiná-lo com o Git para um histórico limpo e definitivo.

---

# 15. MCP — Model Context Protocol

O MCP, ou Protocolo de Contexto para Modelos, é uma camada de abstração padronizada. Ela conecta agentes de inteligência artificial a ferramentas, fontes de dados e serviços externos. Nesta faixa, vamos entender como funciona e por que o escopo de configuração é crítico.

O grande benefício do MCP é a reutilização. Uma funcionalidade implementada uma vez em um servidor MCP fica disponível em qualquer cliente compatível. Claude Code, Cursor e GitHub Copilot são exemplos de clientes que falam esse protocolo. Isso elimina a reimplementação de integrações.

Em seguida, veja a arquitetura central, que tem três peças. O host MCP é a aplicação de inteligência artificial com suporte ao protocolo. O cliente MCP reside no host e gerencia a comunicação com os servidores. O servidor MCP é o gateway que expõe ferramentas, recursos e prompts através de métodos padronizados.

Vamos agora ao escopo de configuração, que tem três níveis. O escopo de projeto usa um arquivo de configuração na raiz do repositório. Esse arquivo é versionado e compartilhado com o time, adequado para servidores sem segredos sensíveis. O escopo de usuário fica nas configurações pessoais e está disponível em todos os projetos. O escopo de sessão é temporário, ideal para tokens de curta duração ou servidores experimentais.

O problema central do MCP é o consumo de contexto. Cada servidor carregado injeta as definições de suas ferramentas no prompt do sistema antes de qualquer mensagem. Com muitos servidores ativos, esse custo pode ser enorme. Cinquenta e oito ferramentas podem consumir cinquenta e cinco mil tokens antes do primeiro prompt do usuário.

A solução é o escopo preciso. Em vez de um arquivo geral que carrega tudo, crie arquivos separados por tarefa. A opção de configuração estrita força o uso exclusivo do arquivo especificado, ignorando hierarquias de nível superior. Com ela, o consumo de tokens de MCP pode cair de cerca de vinte por cento para menos de três por cento da janela de contexto. Dentro de uma sessão, também é possível habilitar e desabilitar servidores dinamicamente sem modificar arquivos de configuração.

Vamos às limitações conhecidas do MCP. A primeira é a poluição de contexto. As definições de ferramentas são pré-carregadas no prompt do sistema sempre que a sessão começa. A segunda é o padrão de ida e volta. Cada chamada de ferramenta exige um ciclo completo entre o modelo e o servidor, e os resultados intermediários se acumulam no contexto.

A terceira limitação é o problema da língua nativa. Modelos de linguagem são treinados em código e linguagem natural, não em tokens de chamada de ferramenta JSON. Muitas ferramentas ou ferramentas complexas degradam a qualidade da seleção e do uso correto. A quarta limitação é que os esquemas JSON descrevem estrutura, não intenção. Eles não orientam quando usar uma ferramenta, como usá-la em contexto ou quando evitá-la.

Uma abordagem alternativa a essas limitações é o CodeMode. Em vez de expor ferramentas diretamente ao modelo, o CodeMode converte as definições MCP em uma API TypeScript. O modelo então escreve código contra essa API. Modelos têm vasto treinamento em TypeScript real, o que melhora a qualidade da geração. Os ciclos de ida e volta diminuem, e ferramentas encadeadas são resolvidas em um único bloco de código executado em sandbox isolada.

A regra geral é sempre escopo a configuração MCP para a tarefa em mãos. Nunca carregue todos os servidores em todas as sessões. Um erro comum é criar um único arquivo de configuração genérico que carrega tudo. Esse erro pode consumir dezenas de milhares de tokens antes mesmo do primeiro prompt. Quando a tarefa usa apenas um servidor específico, prefira a opção de configuração estrita.

---

# 16. Plugins — Instalação e Segurança

Nesta faixa, você vai aprender o que são plugins no Claude Code. Você vai entender como eles simplificam a distribuição de configurações e por que exigem atenção especial de segurança antes de instalar.

Um plugin empacota múltiplos primitivos do Claude Code em uma única unidade instalável. Slash commands, subagentes, servidores de contexto e hooks podem ser distribuídos juntos em um único artefato. Antes dos plugins, copiar configurações entre projetos era um processo manual e trabalhoso. Com plugins, tudo se resolve com alguns comandos de instalação.

Para gerenciar plugins, use o comando barra-plugin na interface do Claude Code. Essa interface permite navegar por marketplaces, adicionar repositórios de plugins e instalar pacotes completos ou apenas componentes individuais. É possível instalar somente um servidor de contexto ou somente um slash command, sem precisar instalar o plugin inteiro.

Em seguida, vamos ao ponto mais crítico desta faixa, que é a segurança. Plugins executam código diretamente na sua máquina local. O campo de descrição de um subagente instalado por um plugin é injetado no prompt do sistema do agente principal. Se esse campo contiver instruções maliciosas, o agente pode executar ações não autorizadas sem que você perceba.

A regra para instalar qualquer plugin é a seguinte. Antes de confirmar a instalação, abra o arquivo de marketplace e localize o campo source do plugin desejado. Navegue até esse diretório e inspecione o arquivo de configuração do plugin. Verifique quais agentes, comandos e hooks serão registrados.

Um erro comum é confiar na conveniência da interface sem verificar o que está sendo instalado. Trate plugins de fontes desconhecidas com o mesmo nível de cuidado que qualquer biblioteca de terceiros. A interface é simples, mas a responsabilidade de auditar o conteúdo é sempre sua.

Plugins resolvem um problema real de reutilização de configurações. O benefício é real, e o cuidado de segurança é igualmente necessário.

---

# 17. Integração com GitHub — Automatizando Workflows

Nesta faixa, você vai entender como o Claude Code se conecta ao GitHub. Você vai aprender o processo de configuração, como a integração funciona no dia a dia e os cuidados necessários para usá-la com segurança.

O Claude Code se integra ao GitHub por meio de GitHub Actions, o sistema de automação de workflows do GitHub. Uma vez configurado, Claude pode ser acionado diretamente em issues e pull requests do repositório. Basta mencionar arroba-claude em um comentário e a automação começa.

A instalação exige dois pré-requisitos. O GitHub Command Line Interface, ou CLI do GitHub, deve estar instalado e autenticado. O Claude Code deve estar aberto a partir de um diretório conectado a um repositório no GitHub. Com esses requisitos atendidos, o comando barra-install-github-app inicia o processo interativo.

Após a instalação, dois arquivos de workflow são adicionados ao repositório automaticamente. O primeiro é acionado quando alguém comenta em uma issue. O segundo executa revisão de código automática em novos pull requests. As credenciais de autenticação ficam armazenadas como secrets do GitHub Actions e nunca aparecem diretamente nos arquivos de workflow.

Quando Claude recebe uma tarefa via issue, ele sempre cria uma branch separada para trabalhar. Ele nunca modifica a branch principal diretamente. O desenvolvedor mantém controle total porque precisa revisar, modificar se necessário e fazer o merge das mudanças propostas.

Por outro lado, há um risco importante a considerar. Sem contexto suficiente do repositório, Claude pode introduzir mudanças que parecem corretas mas quebram contratos com sistemas externos. Renomear uma variável que faz parte de uma interface pública é um exemplo típico.

A regra é revisar sempre o código gerado antes de fazer o merge. Para melhorar a qualidade das respostas, inclua um arquivo de contexto no repositório antes de acionar Claude em tarefas complexas. O Claude pode gerar esse arquivo escaneando a estrutura do projeto automaticamente. Quando versionado, esse arquivo de contexto fica disponível para todos os workflows automáticos.

A integração com GitHub é poderosa para delegar tarefas rotineiras. O retorno cresce com a qualidade do contexto disponível e com a revisão humana antes de cada merge.

---

# 18. Agentes Paralelos — Paralelizando Tarefas Independentes

Nesta faixa, você vai aprender como usar múltiplas instâncias do Claude Code ao mesmo tempo. Você vai entender quando o paralelismo funciona bem e quando ele cria mais problemas do que resolve.

O Claude Code permite rodar várias instâncias simultâneas no mesmo projeto. Cada instância tem acesso de leitura e escrita ao codebase completo. A ideia é dividir o trabalho entre agentes que operam em paralelo, reduzindo o tempo total da tarefa.

O paralelismo funciona bem para tarefas verdadeiramente independentes. Corrigir bugs em módulos separados, desenvolver componentes de interface em arquivos distintos ou escrever seções independentes de documentação são bons exemplos. Em todos esses casos, cada agente trabalha em sua área sem interferir no outro.

Em contraste, tarefas dependentes não se beneficiam do paralelismo. Uma funcionalidade que conecta camada visual e camada de dados não pode ser dividida quando um lado depende da interface do outro. Mudanças no mesmo arquivo por dois agentes resultam em conflitos inevitáveis. Refatorações que alteram interfaces compartilhadas também devem ser feitas em sequência.

Na prática, cada agente recebe seu próprio prompt em um terminal separado. O ponto crítico é especificar explicitamente no prompt quais arquivos cada agente pode modificar. Sem essa restrição, os agentes podem interferir uns nos outros mesmo em tarefas que pareciam independentes.

A regra é mapear as dependências antes de distribuir o trabalho. Para paralelismo robusto em ambientes de produção, use git worktrees. Essa funcionalidade do git mantém cada agente em seu próprio branch e diretório de trabalho, eliminando conflitos de merge em vez de apenas tentar evitá-los via instrução de prompt.

Um erro comum é assumir que qualquer tarefa pode ser paralelizada. O ganho de velocidade só se realiza quando as tarefas são genuinamente independentes. A complexidade de coordenação cresce rapidamente quando as dependências não foram mapeadas com antecedência.

---

# 19. Subagentes — Personalidades Especializadas com Contexto Isolado

Nesta faixa, você vai entender o que são subagentes no Claude Code. Você vai aprender como configurá-los, como o contexto flui entre o agente principal e os subagentes, e como evitar os erros mais comuns.

Um subagente é uma personalidade de IA pré-configurada à qual o agente principal pode delegar tarefas específicas. Cada subagente tem seu próprio prompt do sistema, seu próprio conjunto de ferramentas permitidas e sua própria janela de contexto isolada. Isso o torna diferente de simplesmente mudar as instruções dentro da mesma conversa.

Os arquivos de definição ficam em dois locais possíveis. No diretório de agentes do projeto, os subagentes são versionados e compartilhados com o time inteiro. No diretório de agentes do usuário, ficam disponíveis em todos os projetos sem precisar ser versionados. Essa hierarquia segue o mesmo padrão das memórias do Claude Code.

Cada subagente é definido por um arquivo com um cabeçalho de configuração. Os campos obrigatórios são o nome, que é o identificador único do subagente, e a descrição, que controla quando e como o agente principal invoca o subagente. Campos opcionais definem quais ferramentas ficam disponíveis, qual modelo usar e como identificar o agente visualmente na interface.

Em seguida, vamos ao ponto mais importante, que é o fluxo de contexto. O subagente recebe apenas o prompt gerado pelo agente principal. Ele não tem acesso ao histórico completo da conversa principal. Quando o subagente conclui, apenas o resultado final retorna ao agente principal. Os passos intermediários e os tokens consumidos internamente pelo subagente ficam fora do contexto principal. Isso mantém o contexto do agente principal enxuto mesmo em tarefas longas.

A descrição é o mecanismo central de controle. Ela instrui o agente principal sobre quando invocar o subagente e como formular o prompt enviado a ele. Para mudar quando um subagente é chamado, edite a descrição no cabeçalho de configuração. Alterações no corpo do arquivo de definição não afetam a seleção porque esse conteúdo só carrega após a escolha já ter sido feita.

A regra sobre ferramentas é aplicar o princípio do menor privilégio. Provisionar subagentes com mais ferramentas do que o necessário aumenta o contexto desnecessariamente e amplia a superfície de ação de forma indesejada.

Um erro grave é instalar subagentes de fontes não confiáveis sem revisar a descrição. Esse campo é injetado no prompt do sistema do agente principal e pode conter instruções maliciosas que executam ações não intencionais.

Subagentes são a ferramenta correta para delegar trabalho especializado e isolar contexto de tarefas complexas. A qualidade da delegação depende diretamente da clareza da descrição configurada.

---

# 20. Infinite Agentic Loop — Subagentes Paralelos em Escala

Nesta faixa, você vai aprender o padrão chamado Infinite Agentic Loop. Você vai entender como ele usa um prompt de alta ordem para gerar e coordenar múltiplos subagentes paralelos em larga escala.

O padrão se estrutura como um slash command que recebe três entradas. A primeira é o arquivo de especificação descrevendo o que deve ser implementado. A segunda é o diretório onde cada subagente vai gravar seu resultado. A terceira é o número de subagentes a criar, que pode ser um número fixo ou o valor infinito para execução contínua.

O agente principal não implementa o trabalho diretamente. Ele age como orquestrador em quatro fases. Na primeira, lê e compreende profundamente o arquivo de especificação. Na segunda, examina o diretório de saída para identificar o que já existe e a numeração em uso. Na terceira, define uma estratégia de iteração com nomes únicos para cada subagente. Na quarta fase, cria todos os subagentes simultaneamente usando a ferramenta de tarefas e monitora o progresso.

Cada subagente recebe um prompt cuidadosamente construído pelo orquestrador. Esse prompt inclui o spec completo, um snapshot do diretório de saída no momento do lançamento para evitar duplicatas, e um identificador único. O subagente também recebe instrução explícita para criar algo distinto do que já foi produzido nas iterações anteriores.

Há um aspecto financeiro importante neste padrão. Cada subagente consome tokens de forma independente. Seis subagentes em paralelo custam aproximadamente seis vezes o custo de um único agente. Quem usa uma chave de API direta deve monitorar o consumo com atenção.

A regra após uma execução paralela em larga escala é limpar o contexto antes de qualquer instrução subsequente. O contexto do agente principal fica saturado após coordenar múltiplos subagentes. Continuar sem limpar degrada a qualidade das respostas seguintes.

O Infinite Agentic Loop é um padrão avançado para geração em escala. Ele funciona melhor quando múltiplas variações independentes de um mesmo artefato precisam ser criadas rapidamente com qualidade consistente.

---

# 21. Output Styles — Definindo o Protocolo de Comunicação

Nesta faixa, vamos explorar os output styles do Claude Code. Eles permitem redefinir como o modelo estrutura e comunica suas respostas para toda uma sessão de trabalho.

Um output style substitui parte do system prompt padrão do Claude Code por instruções específicas de formatação. Ao selecionar um style, as instruções padrão de engenharia de software são removidas e substituídas pelo conteúdo do arquivo de style. As capacidades fundamentais de edição de arquivos e execução de comandos permanecem disponíveis.

Os output styles podem ser configurados em dois escopos. O escopo do usuário aplica o style a todos os projetos do desenvolvedor. O escopo do projeto sobrepõe o style do usuário e aplica apenas àquele projeto específico.

O formato do arquivo de style tem duas partes. Um cabeçalho de configuração com uma descrição é seguido do corpo do style. O corpo pode definir o estilo de comunicação, o formato esperado das respostas e um bloco de workflow. O bloco de workflow é especialmente útil. Nele você embute comportamento automático que o Claude executará sem que o usuário precise repetir a instrução a cada prompt. Por exemplo, você pode instruir o Claude a sempre salvar arquivos gerados e abri-los no navegador automaticamente.

Em seguida, vale explorar um uso avançado chamado YAML como output style. Em vez de respostas em prosa, o modelo estrutura toda a comunicação como dados YAML. A hierarquia, a indentação, a escolha de chaves e a ordenação carregam significado semântico. Dependências são expressas como relacionamentos pai-filho. Prioridade é expressa pela ordem dos elementos. Escopo é expresso pelo nível de aninhamento.

A regra desta seção é esta. Use output styles para definir o protocolo de comunicação de uma sessão inteira. Embuta regras de workflow no style para eliminar instruções repetitivas a cada prompt.

Um erro comum é escolher um formato que torna a saída ilegível no terminal, como HTML puro, sem incluir no próprio style a instrução para salvar o arquivo e abrir em um navegador.

Para encerrar esta faixa: output styles redefinem como o Claude se comunica em uma sessão. Eles substituem o system prompt padrão. O bloco de workflow embute automações que o modelo executa sem precisar ser instruído a cada turno.

---

# 22. Agent Skills — Carregamento Progressivo e Composição

Nesta faixa, vamos entender como as agent skills funcionam e por que elas são mais eficientes em termos de contexto do que outras formas de estender o Claude Code.

O problema central que as skills resolvem é o seguinte. Cada mecanismo de extensão tem um custo de contexto diferente. O arquivo CLAUDE.md é sempre carregado, mesmo quando seu conteúdo não é relevante para a tarefa atual. Servidores de ferramentas externas injetam definições de todas as ferramentas no system prompt antes de qualquer mensagem. As skills usam uma abordagem diferente chamada de divulgação progressiva.

A divulgação progressiva funciona em três fases. A primeira fase é sempre visível: apenas o cabeçalho da skill, com nome e descrição, é injetado permanentemente no system prompt. Esse texto curto é suficiente para o agente decidir quando invocar a skill. A segunda fase é a carga sob demanda: o corpo do arquivo da skill, com as instruções do workflow, carrega somente quando a skill é selecionada pelo agente. A terceira fase é a carga condicional: scripts auxiliares carregam apenas quando o agente decide executá-los. Scripts não usados em uma sessão nunca entram no contexto.

As skills ficam no diretório de skills do projeto, com um subdiretório para cada skill. Esse subdiretório contém o arquivo de definição e um diretório opcional de scripts. Quando a skill encapsula um workflow complexo, o script pode ser puramente determinístico. Ele não precisa envolver inteligência artificial internamente. O agente principal invoca o script, o script executa lógica determinística, e o resultado retorna ao agente.

Há opções adicionais de configuração no cabeçalho da skill. Uma delas desabilita a invocação automática pelo modelo, exigindo que o usuário acione a skill explicitamente por slash command. Outra faz a skill executar em um contexto de subagente isolado em vez do thread principal do agente.

A regra mais importante é sobre o campo de descrição no cabeçalho. Ele é o único campo que afeta quando a skill é invocada automaticamente pelo modelo. Edições no corpo do arquivo de skill, como adicionar frases de gatilho em uma seção de instruções, não têm efeito na seleção. Isso porque o corpo carrega apenas após a skill já ter sido escolhida.

Para encerrar esta faixa: agent skills usam divulgação progressiva para minimizar o custo de contexto. Apenas o cabeçalho é sempre visível. O workflow e os scripts carregam somente quando necessários. Essa arquitetura torna as skills mais eficientes do que servidores de ferramentas ou arquivos de memória para workflows reutilizáveis.

---

# 23. Git Worktrees e Agentes em Paralelo

Nesta faixa, vamos ver como o Claude Code Desktop e os Git Worktrees permitem executar múltiplas instâncias do Claude em paralelo com isolamento real de branch e diretório.

O Claude Code Desktop opera em dois modos. O modo local usa Git Worktrees, onde todo o processamento acontece na máquina do desenvolvedor. O modo cloud usa instâncias containerizadas na infraestrutura da Anthropic. Nesse modo, a Anthropic clona o repositório, trabalha no código, faz commit e cria pull requests, como qualquer outro desenvolvedor no projeto.

Git Worktrees são o mecanismo central de isolamento. Eles permitem fazer checkout de múltiplos branches do mesmo repositório em diretórios separados, simultaneamente, sem duplicar o repositório inteiro. Cada instância do Claude opera em seu próprio worktree e branch. Os commits vão para o branch do worktree, não para o branch principal. O branch principal permanece intocado até o merge explícito.

O fluxo de trabalho com worktrees paralelos tem etapas claras. Primeiro, identifique tarefas verdadeiramente independentes, que operem em arquivos diferentes sem dependências entre si. Segundo, inicie uma instância do Claude por tarefa, cada uma em seu próprio worktree. Terceiro, cada agente faz commit em seu branch isolado. Quarto, valide os resultados localmente antes de fazer merge. Por fim, limpe os diretórios de worktree após a conclusão.

Por outro lado, existem situações em que o paralelismo não é adequado. Features fortemente acopladas, onde uma depende da interface da outra, geram discrepâncias quando desenvolvidas em paralelo. Mudanças no mesmo arquivo criam conflitos de merge inevitáveis. Migrações de banco de dados e mudanças em configuração compartilhada têm restrições de ordenação que exigem execução sequencial. Trabalho exploratório e depuração também são mais eficazes em uma sessão focada.

A regra é simples. Comece sequencial. Paralelise somente após confirmar que as tarefas não interagem. Git Worktrees são o mecanismo correto para paralelismo robusto em produção. Múltiplos agentes no mesmo branch sem worktrees inevitavelmente causam conflitos difíceis de rastrear retroativamente.

Para encerrar esta faixa: Git Worktrees permitem que múltiplas instâncias do Claude trabalhem em paralelo com isolamento real de branch e diretório. A chave para o sucesso é confirmar que as tarefas são genuinamente independentes antes de paralelizar.

---

# 24. Deep Agents — O Que Torna um Agente Verdadeiramente Capaz

Nesta faixa final, vamos entender o que distingue os deep agents dos agentes simples e por que essa distinção é fundamental para tarefas de longa duração.

Os agentes simples, também chamados de shallow agents, usam o loop ReAct. Esse loop segue três passos em ciclo: raciocinar, agir e observar. A cada ciclo, o resultado da ação entra no contexto e permanece lá. Para tarefas longas, esse acúmulo contínuo leva ao apodrecimento de contexto: contradições, ruído excessivo e degradação progressiva da qualidade das respostas.

Deep agents endereçam esse problema com quatro capacidades específicas. A primeira é a ferramenta de planejamento. Em vez de simplesmente tentar e falhar, o agente mantém uma lista de tarefas explícita em Markdown. Ele revisa e atualiza o plano entre steps. Quando algo falha, ele replaneja de forma controlada em vez de repetir cegamente a mesma ação.

A segunda capacidade é a hierarquia de subagentes. O agente principal delega subtarefas a subagentes especializados. Cada subagente tem seu próprio contexto isolado. O agente principal recebe apenas o artefato final. Os passos intermediários do subagente não poluem o contexto principal.

A terceira capacidade é usar o filesystem como motor de contexto. O filesystem guarda toda a informação disponível sobre o projeto. O agente usa buscas precisas para selecionar apenas o que a tarefa atual precisa. A qualidade do agente é diretamente limitada pela qualidade dessa seleção. Mesmo o melhor modelo retorna resultados incorretos quando recebe contexto incompleto ou incorreto.

A quarta capacidade é um system prompt abrangente. Ele estabelece identidade e escopo claros, empodera o agente com objetivos em vez de listas de passos, fornece um framework de raciocínio reutilizável e usa heurísticas comprimidas que o agente aplica a situações novas.

A regra central desta seção é esta. A maior parte da inovação em deep agents acontece na camada de orquestração, o harness, não no modelo base. Quem domina o harness define a qualidade do agente.

Um equívoco frequente é tratar deep agents como agentes simples com mais steps. Sem ferramenta de planejamento, sem filesystem como contexto e sem isolamento via subagentes, a execução de tarefas longas inevitavelmente degrada.

Para encerrar esta faixa, e o audiobook completo: deep agents são aqueles que planejam explicitamente, delegam com isolamento de contexto, selecionam informação com precisão do filesystem e operam com um system prompt que empodera em vez de prescrever. Esses quatro pilares separam um agente capaz em tarefas longas de um que funciona apenas em tarefas curtas.
