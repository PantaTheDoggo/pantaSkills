# Teach: Software Mistakes and Tradeoffs

Bem-vindo. Este é um material em áudio derivado da skill Software Mistakes and Tradeoffs. Cada faixa cobre um conceito independente. Você pode ouvir em qualquer ordem.

---

# 1. Filosofia de Tradeoffs

Nesta faixa, vamos explorar a filosofia fundamental por trás das decisões de design em software. O conceito central é simples: toda escolha técnica tem um custo.

Toda decisão de design fecha portas. Quando você escolhe como estruturar um sistema, você limita as direções em que ele pode evoluir. Quanto mais tempo o sistema vive, mais difícil é reverter essas decisões estruturais.

Por isso, a primeira habilidade de um engenheiro experiente não é saber a resposta certa. É saber articular o raciocínio por trás de cada caminho possível. Isso significa identificar os prós e contras de cada direção. É preciso entender também o contexto que torna uma opção preferível à outra.

Veja agora um exemplo prático de armadilha frequente. Quando há alternativas de desempenho em jogo, o instinto é decidir por intuição. A regra é medir antes de escolher. Sem dados reais, qualquer decisão entre alternativas de desempenho é uma suposição disfarçada de raciocínio técnico.

A regra é a seguinte: ao tomar qualquer decisão de design, identifique explicitamente os prós e contras de cada direção disponível. Um erro comum é omitir essa etapa, o que torna impossível revisar a decisão com inteligência no futuro.

Tradeoffs não são problemas a resolver. São a natureza do design de software. A função do engenheiro é torná-los visíveis e deliberados.

---

# 2. Testes: Unit, Integration e End-to-End

Nesta faixa, você vai aprender como decidir o que testar e em que proporção. A escolha entre testar pela interface pública ou expor detalhes internos tem consequências amplas. Elas vão além dos testes em si.

Quando um método privado tem lógica complexa, surge a dúvida de como testá-lo. Há duas abordagens principais. A primeira é o teste pela caixa preta. Você testa apenas o comportamento visível pela interface pública, sem acessar detalhes internos. Isso resulta em testes menos acoplados à implementação e mais fáceis de manter.

A segunda abordagem é elevar a visibilidade do método para permitir acesso direto nos testes. Em algumas linguagens, isso significa tornar o método público. Costuma-se marcá-lo com uma anotação que avisa que a mudança existe apenas para testes. O problema é que outros desenvolvedores costumam ignorar essa marcação. Eles passam a usar o método como parte da API, ou interface de programação, do sistema.

A regra é a seguinte. Prefira tornar o método visível apenas dentro do mesmo pacote, em vez de torná-lo completamente público. Essa escolha dá acesso suficiente para os testes sem expor o método a consumidores externos. É um meio-termo que preserva o encapsulamento sem sacrificar a testabilidade.

Em seguida, considere a composição da sua suíte de testes. Os testes de unidade, ou unit tests, verificam classes e métodos isolados. Eles são os mais rápidos e baratos de criar. Os testes de integração verificam como os componentes se comunicam entre si. Já os testes de ponta a ponta exercitam o sistema completo. Eles exigem infraestrutura específica e são os mais lentos a executar.

A pirâmide de testes reflete a proporção ideal. Deve haver mais testes de unidade do que de integração, e mais de integração do que de ponta a ponta. Essa estrutura equilibra velocidade de feedback com cobertura abrangente do sistema.

A regra é combinar sempre testes de unidade e testes de integração. Cobrir cem por cento do código apenas com testes de unidade dá falsa segurança. Os algoritmos ficam bem testados, mas não há garantia de que os componentes se integram corretamente. Um erro comum é adicionar testes de ponta a ponta tarde demais no projeto. A infraestrutura necessária é cara para criar depois que o sistema já está em produção. A regra é tratar esses testes como funcionalidades do projeto, planejadas desde o início.

A qualidade de uma suíte de testes não está na contagem de testes, mas na sua composição. Decidir o que testar, como acessar e em que proporção é parte do design do sistema.

---

# 3. Singleton Pattern — Tradeoffs em Contexto Multithreaded

Nesta faixa, você vai aprender por que o padrão singleton, um dos mais conhecidos em engenharia de software, esconde armadilhas sérias em contextos com múltiplas threads. As consequências de ignorá-las afetam diretamente a performance e a correção do sistema.

O singleton garante que apenas uma instância de uma classe exista durante a execução do programa. A implementação mais simples verifica se a instância já foi criada, e se não, cria uma nova. Esse modelo funciona bem quando há apenas uma thread de execução.

O problema surge com múltiplas threads. Quando duas threads chegam ao mesmo tempo à verificação inicial, ambas podem enxergar a instância como nula e criar objetos distintos. O resultado é a quebra da garantia fundamental do padrão.

A primeira tentativa de solução é sincronizar o método inteiro. Isso força as threads a esperarem sua vez para acessar o método. O sistema fica correto, mas a um custo alto. Em benchmarks com cem threads e cinquenta mil operações, essa abordagem chegou a trezentos e dezesseis milissegundos. Isso representa uma penalidade de mais de cem vezes em relação às alternativas.

A regra é evitar a sincronização completa do método em sistemas com alta concorrência. Ela introduz thread contention severa e degrada a performance de maneira desproporcional ao benefício.

A solução recomendada para alta concorrência é o double-checked locking. A ideia é verificar a instância duas vezes: uma vez sem sincronização, e uma segunda vez dentro do bloco sincronizado. Isso garante que a sincronização só ocorra durante a inicialização, quando de fato é necessária. Após a criação da instância, o caminho rápido sem bloqueio é utilizado. No mesmo benchmark, essa abordagem levou aproximadamente dois vírgula seis milissegundos.

Há um detalhe crítico nessa implementação. O campo da instância deve ser declarado como volátil, em inglês volatile. Sem essa palavra-chave, o compilador pode reordenar instruções de forma que outra thread enxergue um objeto parcialmente construído. O volatile garante visibilidade imediata das escritas entre threads.

A regra é usar volatile com double-checked locking para singletons compartilhados entre threads.

Uma terceira abordagem é o thread confinement usando ThreadLocal. Em vez de uma única instância compartilhada, cada thread recebe a sua própria cópia. Não há competição, não há sincronização. O benchmark mediu aproximadamente cinco vírgula seis milissegundos. Essa abordagem é adequada quando o estado não precisa ser compartilhado entre threads.

Há também alternativas que evitam o singleton por completo. O static initializer cria a instância na carga da classe, delegando ao sistema o controle do ciclo de vida. O tipo enum em Java garante exatamente uma instância por design, sem código de proteção adicional.

A alternativa mais robusta, porém, é a injeção de dependência, ou dependency injection. Em vez de acessar um singleton a partir de qualquer ponto do código, você cria uma única instância em um ponto central e a injeta nos componentes que precisam dela. Esse padrão elimina a necessidade do singleton e melhora a testabilidade do sistema.

A regra final desta faixa é a seguinte: prefira dependency injection a singletons sempre que possível. Crie uma instância em um ponto central e injete nos serviços que precisam dela. Quando singletons forem inevitáveis, use double-checked locking com volatile para alta concorrência, ou ThreadLocal quando o estado for privado por thread.

---

# 4. Microserviços versus Monolito

Nesta faixa, você vai aprender quando microserviços fazem sentido e quando um monolito é a escolha mais sábia. O tema central é que nenhuma arquitetura é superior em abstrato. O contexto é sempre o que decide.

A arquitetura de microserviços divide o sistema em serviços independentes, cada um com seu próprio processo de deploy. A primeira vantagem é a escalabilidade horizontal. Ao adicionar instâncias de um único serviço, o throughput cresce de forma proporcional. Um monolito escala verticalmente, limitado pelos recursos de uma única máquina.

A segunda vantagem é a velocidade de desenvolvimento. Equipes independentes evoluem seus serviços sem conflitos de codebase. Cada time pode usar as tecnologias que fazem mais sentido para seu domínio e publicar releases sem depender de outros times.

A terceira vantagem é o risco menor por deploy. Releases menores e mais frequentes contêm menos mudanças. Elas são mais fáceis de entender e mais simples de investigar quando há um problema. A regra é a seguinte: prefira lançamentos pequenos e frequentes a deploys grandes e esporádicos.

Em seguida, considere os custos. Microserviços exigem uma camada de infraestrutura que um monolito não precisa. Cada serviço precisa se registrar em um service registry, que é um catálogo de serviços disponíveis na rede. Um load balancer consulta esse registry para distribuir o tráfego. Um erro comum é migrar para microserviços sem planejar essa infraestrutura. Service registry, load balancer, distributed tracing e health checks são requisitos, não recursos opcionais.

O distributed tracing merece atenção especial. Quando um erro ocorre em um sistema com vários serviços, é preciso rastrear o fluxo de uma requisição entre múltiplos serviços para encontrar a causa raiz. Sem essa ferramenta, investigar problemas de integração se torna muito difícil.

A regra sobre monolitos é objetiva. Se a equipe é pequena e os requisitos de escala são baixos, a arquitetura monolítica é a escolha correta. O custo operacional de microserviços não se justifica nesse contexto. Arquiteturas reais são frequentemente híbridas, com parte monolito legado e parte microserviços novos. Esse espectro é normal.

Para tomar qualquer decisão arquitetural, siga um framework simples. Primeiro, liste os prós e contras de cada opção. Em seguida, adicione o contexto real: tamanho da equipe, acordo de nível de serviço, prazo de entrega e requisitos de escala. Por fim, responda qual design é melhor neste contexto específico. A regra fundamental é nunca avaliar um padrão arquitetural em abstrato. O contexto determina se ele é adequado ou não.

---

# 5. Compartilhamento de Código — Biblioteca, Microserviço ou Duplicação

Nesta faixa, você vai aprender como decidir quando compartilhar código entre times. As opções disponíveis são três: duplicar, criar uma biblioteca ou extrair para um microserviço. Cada uma tem um perfil de tradeoff distinto.

A primeira opção é a mais contraintuitiva. Duplicar código entre dois times independentes elimina a necessidade de sincronização. A Lei de Amdahl, aplicada a times, define um limite claro. Quanto menor a fração de trabalho que exige coordenação, maior o ganho de velocidade ao escalar o time. Eliminar duplicação exige sincronização. E sincronização tem custo. A regra é a seguinte: antes de centralizar código entre times independentes, avalie o custo de sincronização exigido. Em certos contextos, duplicar preserva autonomia de entrega.

Em seguida, considere a biblioteca compartilhada. Ela centraliza correções de bugs e garante consistência entre os consumidores. No entanto, ela cria uma nova entidade com ciclo de vida próprio. Isso inclui processo de deploy, práticas de desenvolvimento e documentação própria. Um risco específico das bibliotecas é o conflito de dependências transitivas. Imagine que sua biblioteca usa a versão vinte e sete de uma dependência popular. Um dos clientes usa a versão vinte e oito via outra biblioteca. O compilador pode escolher a versão errada e causar um erro em tempo de execução. A regra é minimizar dependências diretas de uma biblioteca compartilhada. Cada dependência propagada aumenta o risco de conflito para todos os consumidores.

A terceira opção é extrair a lógica para um microserviço. O cliente não importa código. Ele faz chamadas a uma interface de programação via protocolo HTTP. Isso elimina o problema de dependências transitivas. Por outro lado, cada chamada adiciona a latência do serviço ao tempo de resposta total. Se o serviço downstream fica indisponível, o cliente precisa de mecanismos de resiliência. A regra é implementar retentativas com espera progressiva. Primeira tentativa após um segundo, segunda após dez, terceira após trinta segundos. Use também um circuit breaker para interromper chamadas quando o serviço estiver fora do ar de forma prolongada.

Vamos ao framework de decisão. Duplicação preserva autonomia, mas não propaga correções de bugs. Biblioteca propaga correções, mas cria acoplamento de dependências. Microserviço oferece autonomia e propagação, ao custo de infraestrutura operacional. A regra final é direta. Se a lógica tem domínio de negócio próprio e alta complexidade, prefira o microserviço. Se a lógica é simples com poucas dependências, prefira a biblioteca. Se os times precisam evoluir em direções divergentes, aceite a duplicação.

Um erro comum é assumir que duplicação entre codebases é sempre ruim. Bug fixes não propagados são um custo real. Mas a perda de autonomia de time pode ser um custo ainda maior. A escolha certa depende do contexto.

---

# 6. Herança, Composição e Duplicação Intencional

Nesta faixa, você vai aprender quando usar herança, quando preferir composição e quando aceitar duplicação de código de forma deliberada. O tema central é que eliminar duplicação pode criar acoplamento que prejudica mais do que a duplicação em si.

Comece pelo padrão Template Method. Ele usa herança para compartilhar a estrutura de um algoritmo entre variantes. A classe base implementa o fluxo principal e delega apenas a parte variável às subclasses via método abstrato. Imagine um sistema de rastreamento de requisições. O fluxo de verificar o buffer, adicionar a carga e marcar como processado é idêntico para todos os tipos. Apenas a criação da carga difere por tipo. O Template Method centraliza essa lógica comum no pai e pede que cada filho implemente somente a parte que varia.

A regra é a seguinte: use Template Method quando a estrutura do algoritmo é idêntica entre variantes e apenas um passo concreto difere entre subclasses.

O problema surge quando os requisitos começam a divergir. Suponha que uma das subclasses precise de um buffer ilimitado, enquanto as demais continuam com o limite original. A mudança no método da classe base afeta todas as subclasses ao mesmo tempo. Não há como alterar o comportamento de uma sem expor as demais à mudança.

A tentação nesse momento é verificar o tipo concreto dentro da classe base usando a instrução de verificação de tipo. Isso é um antipadrão grave. O pai passa a conhecer os detalhes internos dos filhos. O encapsulamento se desfaz e o benefício da herança se anula.

A regra é evitar verificações de tipo concreto na classe base para tratar casos específicos de subclasses. Se isso for necessário, é sinal de que a hierarquia de herança precisa ser repensada.

A alternativa é a composição. Em vez de uma hierarquia de herança, você cria interfaces independentes para cada responsabilidade. Por exemplo, uma interface para transformação de carga e outra para estratégia de buffer. Cada combinação de comportamento é montada injetando as implementações desejadas no construtor. Qualquer transformação pode ser combinada com qualquer estratégia de buffer, sem hierarquia.

Os tradeoffs são claros. Composição oferece maior flexibilidade quando os requisitos variam de forma independente em múltiplas dimensões. O custo é que há mais abstrações para o leitor do código compreender. Herança produz menos abstrações, mas cria acoplamento implícito entre subclasses via classe pai.

A regra é a seguinte: prefira composição quando os requisitos das subclasses tendem a variar de forma independente em múltiplas dimensões.

Por fim, considere o tema da duplicação intencional. Existem dois tipos de duplicação. A primeira é a duplicação inherente. Dois componentes resolvem o mesmo problema e devem evoluir juntos. Nesse caso, abstrair é a decisão correta. A segunda é a duplicação incidental. Dois componentes parecem idênticos hoje, mas podem seguir caminhos diferentes amanhã. Nesse caso, abstrair cria acoplamento desnecessário.

O erro mais comum é agir apenas pela aparência do código. Quando dois trechos parecem iguais, a reação imediata é criar uma abstração. Mas similaridade visual não implica equivalência de domínio. Dois módulos podem ter a mesma estrutura agora e divergir completamente nas próximas iterações.

A regra é a seguinte: antes de criar uma abstração para eliminar duplicação, verifique se os dois componentes realmente resolvem o mesmo problema de negócio. Se puderem evoluir de forma distinta, mantenha-os independentes.

A regra final desta faixa é sobre o momento certo de abstrair. Deixe abstrações emergirem da prática. Implemente os componentes de forma independente, observe os padrões comuns ao longo do tempo e só então abstraia o que se mostrou estável. É mais fácil fundir dois conceitos similares do que separar uma abstração prematura.

---

# 7. Tratamento de Exceções

Nesta faixa, você vai aprender como projetar o tratamento de exceções de forma que o sistema permaneça rastreável, correto e com contratos claros. O tema central é que excecões mal tratadas geram falhas silenciosas — o pior tipo de bug em produção.

Comece pela hierarquia básica. Em Java, toda exceção descende de Throwable. As subclasses diretas são Error e Exception. Errors não devem ser capturados — representam falhas irrecuperáveis da JVM. Dentro de Exception, há duas famílias. As checked exceptions obrigam o caller a tomar uma decisão explícita em tempo de compilação. As unchecked exceptions não exigem captura, mas podem ser declaradas na assinatura para documentar pré-condições.

A regra é usar captura granular por tipo quando o tratamento difere entre exceções. Se você captura Exception genérico onde apenas tipos específicos são esperados, você intercepta RuntimeExceptions que deveriam propagar para o nível correto da call stack.

Em seguida, considere o design de APIs públicas. Checked exceptions em APIs públicas tornam o contrato explícito. O caller sabe o que pode falhar sem ler a implementação. Unchecked exceptions são adequadas para documentar pré-condições, como IllegalArgumentException e IllegalStateException. Quando você precisar converter uma checked exception em unchecked, preserve sempre a causa original. Uma unchecked exception sem causa é uma pista de debug apagada.

O próximo tema são os antipadrões. O mais perigoso é o swallowing: capturar a exceção e não fazer nada, ou apenas imprimir com printStackTrace. A informação é perdida e o sistema continua em estado inconsistente sem sinalização. Um segundo antipadrão é o resource leak. Se você fecha um recurso depois de código que pode lançar uma exceção, e a exceção ocorrer, o fechamento nunca será executado. A solução é o bloco try-with-resources. Qualquer objeto que implemente AutoCloseable é fechado automaticamente ao sair do bloco, mesmo que uma exceção ocorra. A regra é implementar AutoCloseable em qualquer objeto que consuma recursos do sistema.

Um terceiro antipadrão é usar exceções para controle de fluxo. Lançar uma exceção para bifurcar a lógica de negócio, em vez de usar uma condição, gera código difícil de ler e degrada a performance. Use tipos funcionais como Try ou Either nesses casos.

Sobre exceções de bibliotecas de terceiros: expor o tipo de exceção de uma lib na assinatura pública do seu componente cria acoplamento direto. Se você trocar a lib, quebra a compatibilidade. A solução é criar uma exceção de domínio própria que encapsula a exceção da lib usando factory methods com construtor privado. Passe sempre a Throwable original como causa da exceção de domínio, para que o stack trace completo permaneça acessível.

Em ambientes com múltiplas threads, o comportamento das exceções muda. Quando você submete uma tarefa com submit e chama Future.get, a exceção do worker thread é encapsulada em ExecutionException e propagada para o chamador. Esse é o padrão correto quando o resultado importa. Quando você usa execute para tarefas fire-and-forget, uma exceção no worker thread é descartada silenciosamente. Para evitar isso, registre um UncaughtExceptionHandler na thread factory do pool. Sem ele, threads que falham não são recriadas, e o pool esvazia progressivamente.

Em código assíncrono com CompletableFuture, quando você faz ponte com código síncrono que lança checked exceptions, use completeExceptionally em vez de relançar como RuntimeException. O relançamento gera stack traces aninhados — CompletionException envolvendo RuntimeException envolvendo a causa original — que obscurecem o diagnóstico.

A abordagem funcional com o tipo Try, disponível na biblioteca Vavr para Java, permite encadear transformações sem misturar try-catch blocks à lógica de negócio. Você encapsula a operação que pode falhar em Try.of, e em seguida encadeia map, mapTry e onFailure. No final, extrai o valor com getOrElse para um valor padrão, ou deixa o Try propagar para o caller decidir. A regra é retornar Try quando não há valor padrão razoável — quem chamou o método tem mais contexto para decidir o tratamento.

Por fim, considere a performance. Benchmarks JMH com cinquenta mil iterações mostram que throw-catch e o tipo Try têm custo idêntico: cerca de cem milissegundos. O que custa sete vezes mais é chamar getStackTrace explicitamente. O que custa trinta vezes mais é passar a exceção para logger.error com um appender de arquivo. A regra é: se você vai relançar uma exceção para um nível superior, não a logue no nível intermediário. Ela será logada definitivamente no nível que a capturar, sem duplicação.

O custo real do tratamento de exceções não está no throw ou no catch. Está no que você faz depois que a exceção chegou.

---

# 8. Extensibilidade e Flexibilidade de APIs

Nesta faixa, você vai aprender como decidir o quanto uma API deve ser extensível. O tema central é que flexibilidade tem custo, e esse custo cresce com a abordagem escolhida.

A primeira decisão é sobre o ponto de partida. Ao projetar um componente compartilhado, comece com a implementação mais simples possível, sem pontos de extensão. A extensibilidade especulativa — aquela que antecipa casos de uso antes de ter clientes reais — introduz abstrações sem benefício prático e aumenta o custo de manutenção. A regra é: adicionar extensibilidade depois é seguro; remover features de uma API pública é uma breaking change. Portanto, comece simples e adicione com base em demanda real.

Quando a extensão necessária é o suporte a diferentes implementações de uma biblioteca de terceiros, a solução é criar uma interface interna. Em vez de acoplar o componente a uma lib específica, você expõe uma interface com os métodos que o componente precisa. Qualquer lib pode ser adaptada para essa interface. O tradeoff é que abstrair reduz o acoplamento no componente, mas move complexidade para os clientes. Cada cliente precisa implementar a interface para a lib que usa. A regra é fornecer sempre uma implementação padrão da interface. Clientes que usam a lib mais comum usam o default sem escrever nenhum código. Apenas os que precisam de uma alternativa implementam a interface.

Uma segunda forma de extensibilidade é a Hooks API. Hooks permitem ao cliente injetar código entre fases do lifecycle do componente. Imagine que o componente processa uma requisição HTTP. Um hook permite que o cliente adicione um header de rastreamento antes do envio, sem que o componente precise prever essa necessidade. Os hooks são injetados via construtor como uma lista e executados em cada fase relevante.

Há dois cuidados obrigatórios ao usar Hooks API. O primeiro é a guarda contra exceções. Código do cliente pode lançar unchecked exceptions. Se a exceção escapar, ela interrompe o lifecycle do componente para todos os outros chamadores. A regra é envolver cada chamada de hook em try-catch e logar a exceção sem propagar. O segundo cuidado é o impacto de performance. Hooks síncronos que fazem I/O ou chamadas de rede aumentam diretamente a latência. A solução é submeter cada hook a um thread pool dedicado e aguardar todos com invokeAll antes de avançar para a próxima fase. Mesmo com paralelização, a latência adicionada é pelo menos igual ao hook mais lento.

Uma terceira forma de extensibilidade é o Listener API, que implementa o padrão Observer. Diferente do hooks, o componente não aguarda a conclusão dos listeners antes de continuar. Os eventos são emitidos de forma assíncrona. Um cuidado fundamental aqui é propagar estado via wrapper imutável. Se você passa uma referência mutável para os listeners, um cliente pode modificá-la acidentalmente, corrompendo os dados vistos pelos outros listeners. Use wrappers como Collections.unmodifiableList para garantir falha explícita em caso de tentativa de modificação. Se o objeto propagado for imutável por design, não é necessário criar cópia defensiva, o que poupa memória considerável quando há múltiplos listeners.

O framework de decisão para extensibilidade é direto. Quanto maior a flexibilidade desejada, maior a complexidade a gerenciar. Design sem extensão tem custo zero. Abstração com implementação padrão tem custo baixo. Hooks e Listener APIs têm custo alto em gerenciamento de exceções, thread pools, imutabilidade e back pressure. A regra final é: não escolha o máximo de flexibilidade especulativamente. A complexidade operacional segue na mesma direção.

---

# 9. Otimização de Performance — Hot Path vs. Premature Optimization

Nesta faixa, você vai aprender como identificar o que realmente vale otimizar e em que ordem. O tema central é que sem dados, qualquer otimização é uma suposição disfarçada de raciocínio técnico.

Considere um exemplo típico. Um desenvolvedor substitui processamento sequencial por paralelo em uma coleção de dez mil elementos porque intuitivamente parece mais rápido. Um benchmark mostra desempenho idêntico. A otimização adicionou complexidade ao código sem nenhum benefício mensurável, porque o tamanho real da coleção nunca foi medido. A regra é: não otimize sem dados. Toda otimização antes de medir é prematura.

A pergunta correta não é qual parte do código é mais lenta. É qual parte do código tem maior impacto total no sistema. Para isso, existe uma fórmula direta. Multiplique o número de requisições por segundo de um endpoint pela latência no percentil noventa e nove. O resultado é o impacto proporcional daquele endpoint no trabalho total do sistema.

Veja um exemplo real. Um serviço tem dois endpoints. O primeiro retorna a palavra do dia. Ele recebe uma requisição por segundo com trezentos e sessenta milissegundos de latência. O produto é trezentos e sessenta. O segundo endpoint verifica se uma palavra existe. Ele recebe vinte requisições por segundo com cinco mil milissegundos de latência. O produto é cem mil. O segundo endpoint representa mais de noventa e nove por cento do trabalho total. Otimizar o primeiro, mesmo que ele seja o mais lento isoladamente, teria impacto desprezível.

A essa seção de código que concentra a maior proporção do trabalho chamamos de hot path. É o código executado em quase toda requisição real do usuário. O Princípio de Pareto aplicado a software define que oitenta por cento do trabalho é feito por vinte por cento do código. Identificar esse vinte por cento e otimizá-lo é o que move o sistema.

Para configurar benchmarks de forma correta, leve em conta o SLA. Dado um SLA de dez mil requisições por segundo e latência média de cinquenta milissegundos, o número mínimo de threads necessário é quinhentos. Um único thread com cinquenta milissegundos de latência serve apenas vinte requisições por segundo. Rodar o performance test com menos threads do que o SLA requer não valida o SLA.

A detecção do hot path usa dois tipos de ferramenta. Ferramentas black-box como Gatling simulam o tráfego real por endpoint e retornam os percentis por cenário. Ferramentas white-box como MetricsRegistry instrumentam fases internas do sistema com timers para identificar qual subfase específica consome mais tempo. A regra é usar as duas em sequência: primeiro encontre o endpoint que é o hot path, depois identifique qual subfase interna é o gargalo.

Após identificar o gargalo — nesse exemplo, leitura de arquivo a cada requisição — a próxima decisão é a estratégia de cache. Há dois modelos. O cache eager carrega todos os dados na inicialização. Usa memória sempre e tem startup mais lento, mas nunca tem cache miss após o início. O cache lazy carrega sob demanda e aplica eviction por tempo de acesso inativo. Usa memória proporcionalmente ao tráfego real e é mais simples de escalar. Com a estratégia lazy implementada com eviction baseado em tempo, a latência do endpoint caiu de cinco mil milissegundos para sessenta e cinco, uma melhora de cerca de oitenta vezes.

Após cada otimização, recalcule a distribuição de impacto. O endpoint antes negligenciável pode passar a representar uma fração significativa do trabalho. No exemplo, após a otimização, o endpoint de palavra do dia passou a representar vinte e um por cento do trabalho total. Pode valer a pena investigá-lo em seguida.

Um detalhe importante: adapte o performance test ao comportamento da solução. Um cache testado com apenas seis palavras distintas não representa o hit-miss ratio real de um vocabulário grande. Use uma base de dados de entrada suficientemente diversificada para validar o comportamento do cache em condições reais.

Performance não é uma propriedade emergente do sistema. É uma decisão tomada com dados.

---

# 10. Simplicidade vs. Custo de Manutenção de APIs de Configuração

Nesta faixa, você vai aprender como decidir se uma ferramenta deve abstrair ou expor diretamente as configurações da biblioteca que usa internamente. O tema central é que essa escolha distribui o custo de manutenção de formas muito diferentes.

Considere dois serviços que usam a mesma biblioteca de acesso a um serviço de nuvem. O primeiro, chamado batch service, repassa o arquivo de configuração diretamente para o builder da biblioteca. O chamador estrutura o YAML exatamente no formato que a biblioteca espera, com a seção de autenticação, o nome da estratégia, o usuário e a senha. A vantagem é manutenção zero. Quando a biblioteca adiciona uma nova configuração, o chamador inclui a chave no YAML e ela é passada diretamente, sem nenhuma mudança no código do batch service. A desvantagem é que o chamador fica acoplado ao formato interno da biblioteca. Breaking changes na biblioteca se propagam diretamente para todos os chamadores.

O segundo serviço, chamado streaming service, expõe suas próprias configurações sob uma seção própria no YAML. O chamador desconhece o formato da biblioteca. O streaming service faz o mapeamento programático de suas configurações para os tipos esperados pela biblioteca. A vantagem é que mudanças na biblioteca ficam encapsuladas. Os usuários do streaming service não precisam alterar suas configurações. A desvantagem é que cada nova configuração da biblioteca exige uma alteração de código no streaming service.

A diferença fica clara quando há uma breaking change. Imagine que a estratégia de autenticação por senha em texto simples é depreciada e substituída por uma que exige a senha em hash. No batch service, todos os chamadores recebem uma exceção ao atualizar a biblioteca, e cada um precisa migrar manualmente para a nova estratégia. No streaming service, a migração é feita uma única vez dentro do builder. Os usuários da ferramenta não percebem nada.

O framework de decisão é direto. Se a biblioteca é estável e você controla seu ciclo de release, exponha as configurações diretamente. O custo de manutenção é zero. Se a biblioteca é externa e faz breaking changes com frequência, abstraia. O custo de manutenção é centralizado no serviço e os chamadores ficam protegidos. Se a biblioteca tem dezenas ou centenas de configurações, mapear tudo é impraticável. Exponha diretamente. Se vários serviços consomem a mesma biblioteca, abstrair amortiza o custo por todos eles.

A regra é esta: decisões técnicas têm impacto em quem usa a ferramenta. Expor os internos de uma biblioteca transfere o custo de cada migração futura para os usuários. Abstrair transfere esse custo para você, mas também significa que você o controla.

---

# 11. Data e Hora — Tradeoffs de Design

Nesta faixa, você vai aprender como trabalhar com data e hora de forma correta. Este é um dos domínios mais propensos a bugs silenciosos em sistemas reais, e a maioria deles começa com escolhas erradas de tipo ou de timezone.

Comece pelos tipos. A biblioteca java.time, disponível desde o Java 8, oferece um conjunto de tipos com semântica precisa. Instant representa um ponto no tempo independente de fuso horário. É o tipo correto para armazenar quando algo aconteceu. Duration representa uma quantidade exata de tempo decorrido, sem ambiguidade de calendário. LocalDate representa uma data sem hora e sem fuso, como uma data de entrega. ZonedDateTime representa uma data com hora e com timezone IANA. Period representa um intervalo em unidades de calendário como meses e anos, e é ambíguo em casos-limite. A regra é usar java.time e nunca usar as classes antigas java.util.Date e java.util.Calendar, que estão cheias de armadilhas históricas.

Em seguida, a distinção mais importante neste domínio: timezone não é offset UTC. Um offset como menos oito horas é um valor fixo. Um timezone IANA como America/Los_Angeles é uma regra que mapeia instants a offsets e muda conforme horário de verão e decisões políticas. Nunca use um offset fixo para representar uma zona geográfica. Offsets não capturam mudanças de horário de verão. Também evite abreviações como PST ou BST para parsing. Essas abreviações são ambíguas. BST pode significar British Summer Time ou British Standard Time. Use apenas para exibição. A regra é usar sempre identificadores IANA ao representar timezones.

Sobre testabilidade: qualquer código que chame Instant.now() ou LocalDate.now() diretamente é impossível de testar deterministicamente. O tempo avança entre a escrita e a execução do teste. A solução é injetar um Clock como dependência. Em produção, você passa Clock.systemUTC(). Em testes, você passa Clock.fixed com um instante específico e avança o tempo de forma controlada sem nenhum Thread.sleep. A regra é injetar Clock em qualquer componente que dependa do tempo atual.

Antes de implementar qualquer lógica de data e hora, defina com o responsável pelo produto três coisas. Primeiro, qual conceito está sendo armazenado: é um ponto no tempo, uma data local, uma data com fuso? Segundo, qual timezone é relevante: o do usuário, o do endereço de entrega, o do servidor? Nunca use o timezone do servidor como padrão. Um sistema não pode se comportar diferente dependendo de onde a máquina está hospedada. Terceiro, como a aritmética de calendário se comporta em casos-limite. Por exemplo: o que é três meses após o dia trinta e um de outubro? A resposta depende da regra de negócio, não da biblioteca.

Para armazenamento e transmissão, use sempre ISO-8601 com timezone explícito. Esse formato é não-ambíguo, legível por máquinas e humanos, e compatível entre sistemas. Evite chamar métodos que retornam strings dependentes do locale da JVM, pois o resultado varia entre ambientes.

Há dois casos-limite de calendário que merecem atenção especial. No horário de verão, ao adiantar o relógio, certos horários não existem. Ao atrasar o relógio, o mesmo horário ocorre duas vezes. Ambos os casos precisam ser tratados explicitamente na lógica de negócio. A classe ZonedDateTime oferece um construtor estrito que lança exceção em vez de resolver silenciosamente. Use-o quando a ambiguidade for inaceitável.

Por fim, sobre armazenamento de dados: separe sempre o que o usuário informou do que foi calculado a partir disso. Se o usuário marcou uma reunião em Paris às nove da manhã, armazene a data local e o identificador do timezone como source-of-truth. Derive o instant UTC para ordenação e consultas. Se as regras de timezone mudarem no futuro, você pode recalcular os derivados a partir da source-of-truth. Se armazenar apenas o instant UTC, a informação original do usuário é perdida para sempre.

Antes de escrever uma linha de código envolvendo data e hora, especifique em linguagem natural o que o negócio espera em cada caso-limite.

---

# 12. Data Locality e Processamento Big Data

Nesta faixa, você vai aprender por que processar grandes volumes de dados exige uma inversão fundamental na lógica de onde o processamento acontece. O tema central é que em big data, o bottleneck não é a CPU. É o transporte dos dados.

A abordagem padrão é enviar os dados para o código. Em volumes pequenos, isso funciona. Em volumes de dezenas ou centenas de gigabytes, a maior parte do tempo de processamento é gasta em transferência de rede ou de disco. A solução é inverter esse fluxo: serializar a função de processamento e enviá-la para o nó onde os dados já estão. O nó executa localmente e retorna apenas o resultado, que costuma ser muito menor do que os dados brutos. A isso chamamos data locality.

Dados históricos offline devem ser particionados por data para habilitar data locality em consultas temporais. Uma estrutura de diretórios com ano, mês e dia permite que uma consulta sobre um período específico acesse apenas as partições relevantes, sem escanear o conjunto completo. A granularidade do particionamento deve ser proporcional ao maior conjunto de dados que cabe em um único nó. Se um dia de dados não cabe, particione por hora. Se um ano é suficiente, use apenas o ano.

Para dados de usuários distribuídos por múltiplos nós, o particionamento usa uma função de hash aplicada ao identificador do usuário. Todos os dados do mesmo usuário chegam ao mesmo nó, o que permite processar o histórico de um usuário com acesso local. O problema com a divisão por módulo simples é que adicionar um novo nó redistribui a maioria dos dados — tipicamente mais de setenta por cento. A solução é o consistent hashing: ao adicionar um nó, apenas os dados do nó adjacente precisam ser redistribuídos, o que representa aproximadamente um sobre N dos dados totais.

Operações de big data se dividem em dois tipos. Transformações narrow operam dentro de uma única partição: filtros e mapeamentos não precisam mover dados entre nós. Transformações wide requerem dados de múltiplas partições: joins e agrupamentos por chave exigem shuffling, que é a transferência de dados entre nós para reunir os registros com a mesma chave no mesmo nó. A regra é minimizar wide transformations, pois cada shuffle adiciona latência proporcional ao volume de dados movido.

Quando você precisa fazer um join entre um dataset grande e um dataset pequeno que cabe na memória, use broadcast join. O dataset pequeno é enviado para todos os nós que contêm o dataset grande. O join é executado localmente em cada nó, eliminando o shuffle do dataset grande. O ganho de latência pode ser dramático.

Por fim, a escolha entre processamento em disco e em memória. O Hadoop grava o resultado de cada etapa em disco. O Spark mantém os dados intermediários em memória entre as etapas. O disco em HDD é cerca de oitenta vezes mais lento que a RAM. O disco em SSD é cerca de quatro vezes mais lento. Para pipelines com múltiplas etapas de transformação, o processamento em memória é a escolha certa, e o custo adicional de RAM é justificado pela diferença de velocidade.

---

# 13. Bibliotecas de Terceiro — Tradeoffs e Armadilhas

Nesta faixa, você vai aprender os erros mais comuns ao adotar bibliotecas externas e como avaliar uma biblioteca antes de introduzi-la no sistema. O tema central é que toda biblioteca tem defaults, e defaults convenientes em desenvolvimento podem ser perigosos em produção.

O exemplo mais direto é o timeout. A biblioteca OkHttp tem timeout infinito por padrão. Em um serviço com SLA de cem milissegundos, uma thread aguardando uma resposta upstream por cinco segundos está bloqueada sem servir outros requests. Em alta concorrência, isso degrada o throughput total em cascata. A regra é: ao importar qualquer biblioteca, leia a documentação de configuração. Nunca assuma que o default é seguro para produção. Em arquiteturas de microserviços, o timeout de cada cliente HTTP deve ser menor que o SLA do serviço que o usa.

A segunda armadilha é o modelo de concorrência. Código em ambientes event-loop ou reativos não pode chamar código bloqueante diretamente sem dedicar um thread pool separado para isso. Quando você precisa integrar uma biblioteca bloqueante em código assíncrono, envolva as chamadas bloqueantes em um executor dedicado e exponha um CompletableFuture. Quando o contrário for necessário, chame o Future com timeout explícito.

A terceira armadilha é a testabilidade. Bibliotecas de qualidade oferecem mecanismos de virtual time: um ticker injetável no cache, um scheduler controlável em código reativo. Esses mecanismos permitem avançar o tempo em testes sem Thread.sleep, o que reduz o tempo de execução da suite e elimina flakiness causado por diferenças de velocidade entre máquinas. A regra é verificar a testabilidade de uma biblioteca antes de adotá-la. Código que você não pode testar de forma controlada é código em que você não pode confiar.

A quarta armadilha é o problema de dependências transitivas. Cada biblioteca que você importa traz as suas próprias dependências. Se sua aplicação usa uma versão de uma biblioteca e uma lib de terceiros usa outra versão incompatível, o build tool escolhe uma e pode causar erros em tempo de execução. A solução é o shading: a biblioteca incorpora suas dependências com um prefixo de pacote próprio, isolando-as do classpath da aplicação. O tradeoff é que o shading aumenta o tamanho do binário. A regra é minimizar as dependências diretas de uma biblioteca compartilhada, pois cada dependência propagada para os consumidores aumenta o risco de conflito.

Por fim, antes de adotar qualquer biblioteca, avalie seis critérios. Estabilidade: ela tem release estável e commits recentes? Licença: é compatível com uso comercial? Dependências: há conflitos com a sua stack? Testabilidade: tem mecanismos de tempo virtual e fakes? Escalabilidade: suporta múltiplos nós sem estado global? Segurança: tem histórico de vulnerabilidades e atualizações frequentes? Monitore CVEs de todas as dependências e automatize atualizações de segurança.

---

# 14. Consistência e Atomicidade em Sistemas Distribuídos

Nesta faixa, você vai aprender por que lógica correta em um único nó pode produzir resultados incorretos em sistemas distribuídos, e como projetar operações que resistem a falhas de rede e retries.

Toda chamada de rede pode falhar de três formas. A aplicação de destino falha. A rede sofre uma partição. O pacote de resposta é perdido. Do ponto de vista de quem chamou, um timeout não permite saber se a operação foi executada ou não. A resposta padrão é fazer retry até obter sucesso. Isso é chamado de at-least-once delivery: a operação será executada pelo menos uma vez, mas pode ser executada mais de uma vez.

Para que at-least-once delivery funcione sem gerar estados inconsistentes, a operação precisa ser idempotente. Uma operação idempotente produz o mesmo estado independentemente do número de vezes que é executada. Leituras são naturalmente idempotentes. Deleções por identificador único também. Escritas que enviam estado completo do agregado são idempotentes: reprocessar o mesmo evento sobrescreve com o mesmo estado. Escritas que enviam apenas deltas não são idempotentes: reprocessar "adicione um item" duplica o item.

Em arquiteturas com filas persistentes, o padrão CQRS separa o modelo de escrita do modelo de leitura. O producer publica eventos para um tópico. Cada serviço consumidor cria seu próprio modelo de leitura otimizado para o seu caso de uso. Os times trabalham de forma independente. O custo é que os dados ficam duplicados em múltiplos locais e cada chamada de rede pode falhar, exigindo deduplicação no lado do consumidor.

A deduplicação ingênua implementa três estágios: buscar o identificador no banco de dados, executar a ação, salvar o identificador. O problema é que esses três estágios não são atômicos. Se a ação bloquear por mais tempo que o timeout do caller, o retry chega antes do identificador ser salvo. O resultado é que a ação é executada duas vezes. Em cenários com múltiplos nós, dois nós distintos podem executar a busca ao mesmo tempo, não encontrar o identificador, e executar a ação de forma duplicada.

A solução é reduzir os três estágios a uma única operação atômica no banco de dados: o upsert. O upsert insere o identificador se ele não existe e retorna se a inserção foi realizada. Não há janela entre a verificação e a inserção onde outra thread ou outro nó pode se intercalar. A maioria dos bancos de dados distribuídos oferece essa primitiva. Combine deduplicação atômica com mecanismos de rollback para o caso em que a inserção foi bem-sucedida mas a ação falhou, para evitar que eventos sejam marcados como processados quando não foram.

---

# 15. Semântica de Entrega em Sistemas Distribuídos

Nesta faixa, você vai aprender como projetar sistemas que toleram falhas sem perder dados e sem processar o mesmo dado duas vezes. O tema central é a semântica de entrega: at-least-once, at-most-once e effectively exactly-once.

O ponto de partida é a arquitetura pub-sub. Em conexão request-response direta entre producers e consumers, N producers conectados a M consumers criam N vezes M conexões. A falha de qualquer consumer impacta todos os producers. A solução é um componente intermediário, uma fila persistente, que desacopla producers de consumers. O producer publica eventos sem conhecer quem os consome. A fila persiste os eventos enquanto o consumer está offline. Quando o consumer volta, ele retoma de onde parou.

O Apache Kafka implementa esse modelo com tópicos divididos em partições. Cada mensagem recebe um offset, que é um identificador monotonicamente crescente dentro de cada partição. A partition key determina para qual partição cada mensagem vai. Todas as mensagens com a mesma chave vão para a mesma partição, o que garante ordenação dentro de cada partição. Um consumer group processa cada partição com exatamente um consumer por vez, permitindo paralelismo controlado.

No lado do producer, o parâmetro acks controla quantos brokers precisam confirmar o recebimento antes do envio ser considerado bem-sucedido. Com acks igual a all, todos os brokers do grupo de replicação precisam confirmar: máxima consistência, sem perda de dados em falha de broker. Com acks igual a um, apenas o leader confirma: maior disponibilidade, mas perda possível se o leader cair antes de replicar. Com acks igual a zero, fire-and-forget sem confirmação: máxima disponibilidade, perda de dados esperada.

No lado do consumer, a semântica de entrega depende de quando o offset é confirmado. Com auto-commit, o offset é confirmado automaticamente a cada cinco segundos. Se o consumer falha antes do commit, o próximo consumer a assumir essa partição reprocessa os eventos do período. Isso é at-least-once delivery. Com commit manual após o processamento, você garante at-least-once sem a janela de duplicação do auto-commit. Com commit antes do processamento, você garante at-most-once: cada evento é marcado como processado antes de ser processado, então uma falha no processamento resulta em perda do evento.

A estratégia de offset reset define o comportamento quando não há offset confirmado para uma partição. Com earliest, o consumer recomeça do início do tópico, garantindo que nenhum evento seja perdido. Com latest, o consumer começa do evento mais recente, descartando tudo que aconteceu durante a ausência. Para sistemas de pagamento, use earliest. Para sistemas de alerta onde eventos antigos têm pouco valor, use latest.

O effectively exactly-once combina at-least-once com deduplicação. Transações no Kafka garantem que um producer não publique o mesmo evento duas vezes dentro dos limites do Kafka. Mas se o evento que disparou o producer veio de outro sistema com at-least-once delivery, o producer recebe duplicatas e as trata como eventos independentes. A regra é: effectively exactly-once só funciona se todos os componentes do pipeline implementam essa semântica. Um único componente com at-least-once contamina todo o fluxo downstream.

A fault tolerance via fila funciona porque a fila absorve picos de tráfego e períodos de indisponibilidade. Se o serviço de billing fica offline por cinco segundos recebendo cinquenta eventos por segundo, acumulam-se duzentos e cinquenta eventos no tópico. Quando o serviço volta, ele processa os eventos acumulados com a capacidade disponível além do tráfego normal. A regra é dimensionar o SLA do consumer para ser significativamente maior que o throughput do producer. A diferença é o buffer que determina o tempo de recuperação.

---

# 16. Versionamento e Compatibilidade

Nesta faixa, você vai aprender como versionar bibliotecas e APIs de forma que mudanças não quebrem os consumidores de forma inesperada. O tema central é que compatibilidade tem múltiplas dimensões, e ignorar qualquer uma delas cria bugs que só aparecem em produção.

Comece pelo Semantic Versioning. Uma versão tem três partes: major, minor e patch. Incrementar o patch significa um bug fix compatível em ambas as direções. Incrementar o minor significa uma nova funcionalidade compatível com versões anteriores. Incrementar o major sinaliza uma breaking change. Versões com major zero são instáveis: sem garantias de compatibilidade entre patches. A regra é usar prerelease labels desde o primeiro release público e reservar a numeração zero apenas para prototipagem precoce.

Há duas dimensões de compatibilidade relevantes. Backward compatibility significa que a nova versão funciona com código escrito para a versão antiga. Forward compatibility significa que a versão antiga funciona com dados ou código da versão nova. Em APIs de rede, backward compatibility é o padrão esperado. Formatos como Protocol Buffers e Apache Avro foram projetados para suportar as duas direções.

Para bibliotecas compiladas, existem três tipos de compatibilidade independentes. Source compatibility significa que o consumer pode recompilar contra a nova versão sem erros. Binary compatibility significa que o bytecode compilado contra a versão antiga executa contra a nova versão sem erros em tempo de execução. Semantic compatibility significa que o comportamento permanece equivalente. A binary incompatibility é a mais perigosa porque aparece apenas em tempo de execução e apenas nos code paths que chamam o método afetado, que frequentemente são os caminhos de tratamento de erro — os menos cobertos por testes.

A Lei de Hyrum formaliza um princípio importante: com um número suficiente de usuários de uma API, não importa o que o contrato promete. Todo comportamento observável do sistema será dependido por alguém. Isso significa que afrouxar uma validação pode silenciosamente quebrar código que dependia da exceção como mecanismo de validação. Alterar qual overload chama qual pode quebrar subclasses que sobrescriam métodos. A regra é documentar explicitamente quais comportamentos fazem parte do contrato público e quais são detalhes de implementação.

O problema do diamond dependency ocorre quando componente A e componente B dependem de versões diferentes de uma mesma biblioteca. Em plataformas com classpath compartilhado como a JVM, o build tool escolhe uma versão e pode causar erros em tempo de execução. A solução por shading resolve o conflito, mas torna objetos da mesma biblioteca incompatíveis entre componentes. A regra é usar shading quando a biblioteca é usada apenas como detalhe de implementação e nenhum objeto dela aparece na API pública.

Para gerenciar breaking changes, comece com uma API mínima. Adicionar funcionalidade é seguro; remover é breaking. Marque partes instáveis com anotações de Beta. Use final em classes onde herança não é necessária. Agrupe breaking changes planejadas em um único major bump em vez de publicá-las individualmente. Publique um guia de migração explícito para cada major bump.

Em APIs de rede, há dois modelos de versionamento. No client-controlled, o cliente especifica a versão exata e o servidor retorna apenas o que essa versão conhece. O custo é manter implementações de múltiplas versões simultâneas. No server-controlled, o cliente especifica apenas a versão major e pode receber campos novos que não conhece. O problema é o read-modify-write: o cliente atualiza um recurso enviando todos os campos que conhece, e campos desconhecidos são sobrescritos como vazios. A solução é patch semantics: o cliente especifica explicitamente quais campos está atualizando.

Para armazenamento de dados, as mudanças têm consequências distintas. Renomear um campo em Protocol Buffers não afeta os dados armazenados, pois o formato binário usa números de campo, não nomes. Mas quebra o código gerado. Remover um campo exige reservar o número do campo para evitar reutilização acidental. Adicionar um campo é sempre backward compatible. A regra para migrations sem downtime é um processo gradual: adicionar o novo campo, ler de ambos, escrever em ambos, migrar os dados existentes, e só então remover o campo antigo.

---

# 17. Tendências vs. Custo de Manutenção

Nesta faixa, você vai aprender como avaliar novos frameworks e padrões antes de adotá-los. O tema central é que toda tecnologia nova introduz complexidade, e essa complexidade precisa ser justificada pelo problema específico que você está resolvendo.

Comece pela Dependency Injection. A versão manual é simples: todas as dependências são instanciadas em um único ponto de entrada e injetadas via construtor nas classes que precisam delas. O ciclo de vida é explícito, fácil de depurar e fácil de alterar. Um framework de DI como o Spring automatiza esse processo com anotações. O lifecycle e o ordering ficam implícitos, gerenciados pelo container. O problema é que o framework oculta o que está acontecendo. Problemas de lifecycle são muito mais difíceis de diagnosticar. Todas as classes ficam acopladas às anotações do framework. E uma feature do framework puxa outra: gerenciar escopo por request exige o componente web do Spring. A regra é usar um framework de DI somente quando suas features específicas, como gerenciamento de escopo complexo ou AOP, são genuinamente necessárias. Para a maioria dos casos, DI manual é mais simples e mais transparente.

Em seguida, a programação reativa. A evolução natural de código bloqueante é para código assíncrono com CompletableFuture. Uma terceira opção é o Flux do Project Reactor. O Flux oferece composição de pipelines assíncronas com múltiplos schedulers. O problema é que retornar Flux de um método força todos os callers a adotar a API reativa. A reatividade se propaga pelo codebase de forma invasiva. Além disso, controlar em qual thread cada operação executa é difícil, e misturar código bloqueante com hot datasources dentro de um Flux pode causar bloqueio indefinido. A regra é: adote reactive end-to-end ou não adote. Reactive em um único subcomponente importa a invasividade sem o benefício sistêmico. Para paralelismo com dados finitos, CompletableFuture resolve com muito menos complexidade.

Sobre programação funcional em linguagens orientadas a objeto: técnicas como recursão têm limitações importantes que variam por linguagem. Em Java, cada chamada recursiva aloca um frame na call stack. Com cem mil elementos, isso causa StackOverflowError. Java não tem otimização de tail call como linguagens funcionais nativas. A regra é implementar operações sobre coleções grandes de forma imperativa, com loops, e usar os construtos funcionais da biblioteca padrão quando disponíveis. Imutabilidade, por sua vez, é thread-safe por definição, mas cria pressão no garbage collector em hot paths de alto throughput. Meça o impacto antes de adotar imutabilidade pervasiva.

A última discussão é sobre inicialização lazy versus eager. Com inicialização lazy, o sistema inicia mais rápido, mas os primeiros requests pagam o custo de estabelecer conexões e popular caches. Erros de inicialização aparecem tarde, possivelmente após o deploy ter se completado, já afetando usuários. Com inicialização eager, o sistema é mais lento para iniciar, mas as conexões críticas são estabelecidas durante o deploy. Em ambientes com rolling deployment, uma falha de inicialização eager derruba a nova instância antes que a versão anterior seja removida, permitindo rollback sem impacto. A regra é usar eager para recursos críticos como conexões de banco de dados e caches essenciais, e lazy apenas para features raramente usadas.

A regra mais importante sobre tendências é perguntar: o problema que esse framework resolve é realmente o meu problema?
