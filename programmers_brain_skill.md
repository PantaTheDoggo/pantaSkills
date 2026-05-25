<!-- AGENTE-PROGRESSO
fonte: d:\Skillstore\[MANNING] The Programmer's Brain.pdf
próximo: EXTRAÇÃO COMPLETA — todos os 13 capítulos extraídos (PDF páginas 1-258)
último-heading: ## 13 Onboarding de Novos Desenvolvedores
última-linha: > ⚠ Evite: apresentar domínio + workflow + codebase + ferramentas simultaneamente no onboarding...
status: CONCLUÍDO
-->

# Skill: The Programmer's Brain — Referência Consolidada

> **Fonte**: The Programmer's Brain, Felienne Hermans, Manning, 2021
> **Alvo**: Cognição aplicada à programação — leitura, escrita e colaboração em código
> **Última extração**: 2026-05

---

## Índice

| # | Seção |
|---|---|
| 1 | [Três Tipos de Confusão e Processos Cognitivos](#1-três-tipos-de-confusão-e-processos-cognitivos) |
| 2 | [Chunking — Como o Cérebro Supera os Limites da STM](#2-chunking--como-o-cérebro-supera-os-limites-da-stm) |
| 3 | [Aprender e Reter Sintaxe com Eficácia](#3-aprender-e-reter-sintaxe-com-eficácia) |
| 4 | [Carga Cognitiva e Técnicas para Ler Código Complexo](#4-carga-cognitiva-e-técnicas-para-ler-código-complexo) |
| 5 | [Compreensão Profunda de Código](#5-compreensão-profunda-de-código) |
| 6 | [Modelos Mentais e Máquinas Nocionais](#6-modelos-mentais-e-máquinas-nocionais) |
| 7 | [Transfer de Conhecimento e Misconceptions](#7-transfer-de-conhecimento-e-misconceptions) |
| 8 | [Nomenclatura de Identificadores](#8-nomenclatura-de-identificadores) |
| 9 | [Code Smells e Antipadrões Linguísticos](#9-code-smells-e-antipadrões-linguísticos) |
| 10 | [Resolução de Problemas Complexos](#10-resolução-de-problemas-complexos) |
| 11 | [O Ato de Escrever Código](#11-o-ato-de-escrever-código) |
| 12 | [Dimensões Cognitivas de Codebases (CDCB)](#12-dimensões-cognitivas-de-codebases-cdcb) |
| 13 | [Onboarding de Novos Desenvolvedores](#13-onboarding-de-novos-desenvolvedores) |

---

## 1 Três Tipos de Confusão e Processos Cognitivos

Toda confusão ao ler código tem uma raiz cognitiva específica. Identificar o tipo correto direciona a solução.

| Tipo de Confusão | Causa | Processo Cognitivo |
|---|---|---|
| Falta de conhecimento | Não sabe o significado de um símbolo ou keyword | LTM (Long-term Memory) |
| Falta de informação | Precisa navegar em outros arquivos/módulos para entender | STM (Short-term Memory) |
| Falta de poder de processamento | Não consegue acompanhar todos os passos de execução mentalmente | Working Memory |

**LTM (Long-term Memory)** — Armazena fatos permanentemente: sintaxe de linguagem, algoritmos conhecidos, significado de keywords. Análogo ao HD do computador.

**Regra**: Quando a confusão vem de não saber o que um operador ou palavra-chave faz, o problema está na LTM — a solução é estudo deliberado da sintaxe da linguagem.

**STM (Short-term Memory)** — Armazena temporariamente informação recém-lida. Capacidade limitada (menos de 12 itens). Análogo à RAM. É esvaziada após o cérebro resolver o problema em mãos.

**Regra**: Quando a confusão vem de ter que navegar por muitos arquivos para entender o código, o STM está sobrecarregado — reduza a profundidade de navegação necessária.

**Working Memory** — Onde o pensamento ativo ocorre: é o processador do cérebro. Combina informação da LTM e STM para formar novas ideias e soluções. *Tracing* (execução mental do código passo a passo) usa intensivamente a working memory.

**Regra**: Quando a confusão vem de não conseguir seguir todos os passos de um algoritmo mentalmente, a working memory está sobrecarregada — use auxílios externos (tabela de estados, gráfico de dependências).

Os três processos atuam simultaneamente. Exemplo: ao ler código Java familiar, a LTM preenche lacunas (sintaxe de for-loop), a STM retém o nome da variável atual, e a working memory decide o significado do trecho lido.

> ⚠ Evite: usar tracing mental para todo o código — anote valores intermediários externamente quando sentir sobrecarga.

## 2 Chunking — Como o Cérebro Supera os Limites da STM

A STM tem capacidade de 2 a 6 elementos e retém informação por no máximo 30 segundos. Experts superam esse limite combinando informações em **chunks** — unidades reconhecíveis que ocupam um único slot na STM.

**Chunking em código**: quando a LTM contém um padrão (ex.: "for-loop em Java", "Singleton"), o programador o trata como um chunk, não como uma sequência de tokens. Isso libera slots da STM para outros elementos.

**Regra**: quanto mais padrões nomeados (design patterns, algoritmos, idiomas da linguagem) estiverem na LTM, menos slots da STM serão consumidos ao ler código, permitindo processar trechos maiores.

**Memória icônica** — estágio antes da STM: todo código visualizado entra primeiro na memória icônica (buffer visual brevíssimo). O cérebro seleciona *o que* transferir para a STM; parte do código visível nunca chega a ser processado conscientemente. Implicação prática: ao revisar código rapidamente, você vê mais do que processa.

**Como escrever código fácil de chunkar**:

1. **Use design patterns nomeados** — expor explicitamente que o código usa Observer, Strategy, etc. reduz o tempo de manutenção por outros programadores (pesquisa de Tichy).

2. **Escreva comentários de alto nível** — `# This function prints the tree in order` ajuda chunking. Comentários de baixo nível (`# increment i`) sobrecarregam o processo e devem ser evitados.

3. **Inclua beacons** — elementos de código que revelam a intenção ao primeiro olhar:
   - *Simple beacons*: nomes de variáveis, métodos e tipos autoexplicativos (`root`, `left`, `right` → binary tree).
   - *Compound beacons*: combinações de elementos simples que juntos revelam a estrutura (`self.left` + `self.right` → tree node com dois filhos).

**Regra**: nomes de variáveis são o principal beacon. Uma variável como `l` usada como índice de loop compromete o chunking; `idx` ou `index` funciona como beacon imediato.

> ⚠ Evite: comentários que explicam o *que* o código faz (isso o código já diz); prefira comentários que expliquem o *por que* ou que nomeiem o padrão de alto nível.

**Autodiagnóstico via reprodução de código** — o que você consegue reproduzir de memória revela o que está na sua LTM. Partes que não consegue reproduzir indicam conceitos (de linguagem ou domínio) ainda não internalizados.

> 💡 Nota: experts agrupam keywords por semântica de programação (TRUE+FALSE; IF+THEN+ELSE); iniciantes agrupam por frases mnemônicas. O agrupamento semântico acelera chunking.

## 3 Aprender e Reter Sintaxe com Eficácia

Mais sintaxe na LTM → melhor chunking → leitura de código mais rápida. Buscar sintaxe online interrompe o fluxo de trabalho: leva ~15 min para retomar o contexto após uma interrupção (pesquisa de Parnin com 10.000 sessões de 85 programadores).

**Flashcards para programação** — método: prompt de um lado (conceito), código do outro. Processo:
1. Leia o lado do prompt.
2. Escreva o código sem ver a resposta.
3. Vire e compare.

**Regra**: adicione um flashcard (a) ao aprender novo conceito/biblioteca ou (b) sempre que estiver prestes a pesquisar algo no Google — esse impulso indica que o conceito ainda não está na LTM.

**Regra**: remova flashcards que você acerta consistentemente; apps como Anki fazem isso automaticamente via espaçamento.

**Curva do esquecimento** — após 1 hora, ~50% do conteúdo lido é esquecido; após 2 dias, apenas ~25% permanece sem revisão (Ebbinghaus, 1885, confirmado por Murre, 2015).

**Espaçamento (spaced repetition)** — espalhar as repetições ao longo do tempo é mais eficaz do que concentrá-las em poucos dias. Estudar 26 vezes com intervalos de 8 semanas produce retenção superior a estudar 13 vezes com intervalos de 2 semanas (pesquisa de Bahrick et al., 1993).

**Regra**: revisite flashcards uma vez por mês para manutenção de longo prazo — ritmo sustentável que evita a curva de esquecimento.

**Storage strength vs retrieval strength** — informação pode estar armazenada na LTM (storage strength alta) mas difícil de recuperar (retrieval strength baixa). Ver o código repetidas vezes sem tentar recordá-lo não melhora a retrieval strength.

**Retrieval practice** — tentar recordar ativamente, mesmo que sem sucesso, fortalece a retrieval strength. A tentativa em si cria a trilha de recuperação.

**Regra**: antes de pesquisar sintaxe no Google, tente recordá-la por 30 segundos. A tentativa — mesmo que falhe — fortalece a memória para a próxima vez.

**Schemata** — memórias na LTM são armazenadas em rede, não em hierarquia. Informação nova é "ancorada" em schemata existentes; quanto mais conexões, mais fácil de recuperar.

**Elaboração** — ao aprender um conceito novo, conecte-o explicitamente a conhecimento existente:
- Quais conceitos similares você já conhece?
- O conceito novo tem equivalente em outras linguagens?
- Qual paradigma ou domínio ele representa?
- Como se compara sintaticamente com alternativas?

**Regra**: elaboração ativa na hora do aprendizado aumenta a storage strength inicial, prevenindo a perda de detalhes antes mesmo da primeira revisão.

> ⚠ Evite: só reler a sintaxe sem tentar recordá-la — isso não melhora retrieval strength e perpetua o ciclo de ter que pesquisar sempre.

## 4 Carga Cognitiva e Técnicas para Ler Código Complexo

**Working memory = STM aplicada a um problema.** Capacidade idêntica à STM: 2-6 elementos. Quando o código ultrapassa essa capacidade, o programador precisa anotar informação externamente.

**Tipos de carga cognitiva** (Sweller):

| Tipo | Definição | Equivalente em código |
|---|---|---|
| **Intrinsic** | Complexidade inerente ao problema | Complexidade acidental inevitável do algoritmo |
| **Extraneous** | Complexidade adicionada acidentalmente | Nomes ruins, lambdas desconhecidos, código desestruturado |
| **Germane** | Esforço cognitivo de gravar novo conhecimento na LTM | (abordado no Capítulo 10) |

**Regra**: reduza sempre a carga extrínseca — ela não faz parte do problema real e pode ser eliminada. Carga intrínseca não pode ser reduzida sem simplificar o problema.

**Refatoração cognitiva** — mudança temporária no código para facilitar a compreensão agora, sem intenção de manter a mudança. Não confundir com refatoração de manutenção.

Quando usar:
- Inline método com nome vago (`calculate()`, `transform()`) — substitua a chamada pelo corpo do método para ler com contexto.
- Substitua construtos desconhecidos por equivalentes familiares:
  - Lambda → classe com método nomeado
  - List comprehension → for-loop explícito
  - Ternário → if/else em múltiplas linhas

> 💡 Nota: o que é difícil de ler depende do prior knowledge de quem lê. Lambdas e list comprehensions não são objetivamente "mais legíveis" — apenas são mais legíveis para quem os conhece.

**Regra**: após compreender o código, reverta as mudanças de refatoração cognitiva se o restante da equipe usa os construtos originais.

**Gráfico de dependências** — técnica para código com estrutura complexa e altamente interconectada:

1. Circule todas as variáveis (cor 1).
2. Trace linhas entre ocorrências da mesma variável.
3. Circule todos os métodos/funções chamados (cor 2).
4. Trace linha de cada chamada até a definição do método; atenção especial a métodos invocados uma única vez (candidatos a inline).
5. Circule instâncias de classes (cor 3).
6. Trace linha de instâncias até a definição da classe.

O padrão resultante permite seguir o fluxo do código pelas linhas traçadas, sem precisar pesquisar definições durante a leitura — reduz carga cognitiva.

**Tabela de estados** — técnica para código com cálculos complexos entre variáveis interdependentes:

1. Liste todas as variáveis → uma coluna por variável.
2. Execute mentalmente o código passo a passo (tracing) → uma linha por iteração ou etapa significativa.
3. Registre o valor de cada variável em cada célula.

A tabela externaliza os valores intermediários, liberando working memory para entender a lógica de alto nível.

**Regra**: use gráfico de dependências para entender a *estrutura* do código e tabela de estados para entender os *cálculos*. Combine as duas técnicas em código complexo.

> ⚠ Evite: reler o mesmo trecho de código repetidas vezes sem anotar nada — isso consome working memory sem aumentar a compreensão. Anote variáveis, valores ou estrutura externamente.

## 5 Compreensão Profunda de Código

### Papéis das Variáveis (framework de Sajaniemi — 11 papéis)

Identificar o papel de cada variável converte a leitura de sintaxe em leitura de intenção. Programas com "stepper + most wanted holder" são tipicamente programas de busca.

| Papel | Descrição |
|---|---|
| **Fixed value** | Valor constante após inicialização (constantes, dados de arquivo) |
| **Stepper** | Itera através de sequência conhecida (`i` em for-loop, `size/2` em busca binária) |
| **Flag** | Indica que algo aconteceu ou é verdade (`is_set`, `is_error`; frequentemente Boolean) |
| **Walker** | Percorre estrutura de dados de forma desconhecida antes do loop (ponteiro em linked list, índice em binary tree) |
| **Most recent holder** | Guarda o último valor encontrado na iteração (`line = file.readline()`) |
| **Most wanted holder** | Guarda melhor valor encontrado até agora (mínimo, máximo, primeiro match) |
| **Gatherer** | Acumula/agrega valores em um único resultado (`sum += list[i]`) |
| **Container** | Estrutura que armazena múltiplos elementos (list, array, stack, tree) |
| **Follower** | Rastreia valor anterior/subsequente, sempre acoplado a outra variável (ponteiro para nó anterior) |
| **Organizer** | Variável temporária de rearranjo (versão ordenada de lista existente) |
| **Temporary** | Uso brevíssimo, geralmente para swap ou cálculo intermediário (`temp`) |

**Regra**: ao ler código desconhecido, anote o papel de cada variável. Reduz carga cognitiva e revela a estrutura do algoritmo.

### Text Knowledge vs. Plan Knowledge (Pennington)

- **Text structure knowledge**: saber o que cada keyword e variável faz — conhecimento superficial/sintático.
- **Plan knowledge**: entender as intenções e decisões do criador do código — o "por quê" da estrutura.

Ter text knowledge sem plan knowledge cria a sensação frustrante de "entendo cada linha mas não sei o que o código faz".

**Quatro estágios de compreensão profunda** (Sillito):
1. **Encontrar um ponto focal** — `main()`, linha de erro, linha sinalizada pelo profiler.
2. **Expandir a partir do focal** — determinar o slice: todas as linhas que transitivamente relacionam-se à focal.
3. **Entender um conceito a partir de entidades relacionadas** — identificar métodos chamados em múltiplos lugares (papel central), descartar métodos não usados no slice.
4. **Entender conceitos entre múltiplas entidades** — estruturas de dados, operações permitidas, restrições.

**Regra**: ao começar a ler código desconhecido, identifique o ponto focal antes de qualquer outra coisa. Ler sem ponto focal leva a leitura excessiva e overload da working memory.

### Estratégias de Compreensão de Texto Aplicadas a Código

Leitura de código ativa as mesmas áreas cerebrais de linguagem natural (BA21, BA44 — Siegmund, 2014). Habilidade em linguagem natural é o segundo melhor preditor de aprendizado de programação (17% da variância); working memory é o primeiro (34%).

1. **Ativar** — escanear o código por 5-10 min antes de ler em profundidade; identifique conceitos, sintaxe e domínio presentes. Aprenda conceitos desconhecidos antes de mergulhar no código (aprender conceito e código simultaneamente sobrecarrega a working memory).

2. **Monitorar** — marque linhas enquanto lê: ✓ (entendido) / ? (confuso). Na segunda leitura, foque nas linhas com ?.

3. **Determinar importância** — identifique as linhas mais impactantes na execução. Compare com a equipe: divergências revelam diferenças de background e são oportunidade de aprendizado.

4. **Inferir** — liste todos os identificadores (variáveis, classes, métodos) e categorize:
   - Nomes de domínio: `Customer`, `Package`
   - Nomes de conceito de programação: `Tree`, `List`
   - Nomes combinados: `CustomerList`
   - Nomes ambíguos sem contexto: exigem investigação com o framework de papéis

5. **Visualizar** — tabela de operações: para cada identificador, liste todas as operações em que aparece. Permite inferir tipos e papéis de variáveis em código muito complexo.

6. **Questionar** — perguntas para plan knowledge:
   - Quais são os 5 conceitos mais centrais?
   - Quais decisões o criador tomou (algoritmo, design pattern, biblioteca)?
   - Quais premissas essas decisões assumem?
   - Quais alternativas existiriam?

7. **Sumarizar** — escreva um resumo em linguagem natural: objetivo, linhas mais importantes, conceitos de domínio, construtos de programação, decisões do criador. Pode virar documentação do código.

> ⚠ Evite: mergulhar em código desconhecido linha a linha sem escanear primeiro — a ativação prévia de conhecimento relacionado reduz substancialmente a carga cognitiva da leitura subsequente.

## 6 Modelos Mentais e Máquinas Nocionais

**Representação influencia solução**: a forma como você enquadra um problema determina a estratégia de resolução. Exemplo: o problema trem+pássaro é trivial se modelado do ponto de vista do tempo total (30 min × 75 km/h = 37,5 km), mas extremamente complexo se modelado da trajetória do pássaro. Em programação, escolher lista vs. árvore, microserviços vs. monolito, já é uma escolha de representação.

**Modelos externos** — estado tabelas, grafos de dependências, diagramas UML — reduzem carga cognitiva ao externalizar informação e ajudam a LTM a encontrar memórias relevantes.

### Modelos Mentais

Modelos mentais são representações abstratas na working memory usadas para raciocinar sobre o problema. Características:

- **Incompletos**: abstraem detalhes irrelevantes (ex.: "variável como caixa" ignora endereçamento de memória).
- **Instáveis**: evoluem com o aprendizado.
- **Coexistentes**: podem ser múltiplos e até inconsistentes entre si.
- **Frugais**: a mente prefere trabalho físico extra a esforço mental maior (ex.: debugar com tweaks em vez de criar um modelo mental consistente).

**Como criar modelo mental de código complexo** (3 passos):
1. Construa modelos locais primeiro (state tables, dependency graphs) — reduzem carga cognitiva e servem de blocos de construção.
2. Liste todos os objetos relevantes e os relacionamentos entre eles.
3. Responda perguntas sobre o sistema usando o modelo e refine: elementos principais, relacionamentos, objetivo, caso de uso típico.

**Flashcards de modelos mentais** — além de flashcards de sintaxe, mantenha flashcards de *como pensar sobre código*: nome do modelo de um lado, visualização e perguntas disparadoras do outro. Inclua: estruturas de dados, design patterns, architectural patterns, diagramas (ER, sequência, Petri nets).

**Regra**: ao enfrentar código difícil, percorra seu deck de modelos mentais e pergunte "esse padrão se aplica aqui?". Se sim, crie uma instância concreta do modelo (o que são os nós? as arestas? as folhas?).

### Máquinas Nocionais

Uma **máquina nocional** é uma abstração correta e consistente de como um computador executa código — diferente do modelo mental, que pode ser incorreto. Quando o programador internaliza a máquina nocional, ela se torna seu modelo mental.

Exemplos:
- "Variável como caixa" — funciona bem para atribuição simples; falha ao explicar que uma variável só pode ter um valor.
- "Variável como etiqueta/name tag" — mais correto: etiqueta só vai em uma coisa por vez.
- "Função como viajante com mochila" — mochila transporta parâmetros de entrada (e de saída quando há return).
- "Cálculo como substituição" — correto para raciocinar sobre expressões, mas esconde detalhes de stack evaluation.

**Máquinas nocionais operam em diferentes níveis de abstração** (da mais alta para a mais baixa): linguagem de programação → compilador/interpretador → VM/bytecode → sistema operacional. Ao usar uma máquina nocional, identifique quais detalhes estão sendo abstraídos — abstrair detalhes relevantes para o problema em mãos é um antipadrão.

**Máquinas nocionais conflitantes** — "caixa" e "etiqueta" são modelos que não podem coexistir como um único modelo consistente. A caixa implica que pode conter múltiplos valores (misconception). Ao ensinar ou comunicar sobre programação, escolha o modelo baseado no que o interlocutor já conhece (schemata existente na LTM).

**Regra**: ao explicar conceitos de programação, escolha analogias cujo domínio seja familiar ao interlocutor — isso conecta ao schema existente sem criar carga cognitiva extra.

> ⚠ Evite: usar o mesmo modelo nocional para todos os contextos — identifique os limites de cada abstração e mude de modelo quando a abstração esconder detalhes relevantes ao problema.

## 7 Transfer de Conhecimento e Misconceptions

**Transfer** — quando conhecimento de um domínio ajuda a executar tarefas em outro.

| Tipo | Descrição | Exemplo |
|---|---|---|
| **Low-road** | Automatizado, inconsciente | Ctrl+C/Ctrl+V em editor novo |
| **High-road** | Consciente, deliberado | "Java requer declaração de tipo; Python requer?" |
| **Near** | Domínios próximos | Java → C# |
| **Far** | Domínios distantes | Java → Prolog; pouco provável de ocorrer espontaneamente |
| **Positivo** | Conhecimento existente ajuda | Saber loops em Java facilita loops em Python |
| **Negativo** | Conhecimento existente atrapalha | Assumir que Python requer tipo estático como Java |

**Fatores que aumentam transfer**:
- Domínio profundo da tarefa original (expertise → mais chunks e modelos transferíveis)
- Similaridade entre as tarefas e o contexto (mesmo IDE para múltiplas linguagens favorece transfer)
- Identificar explicitamente atributos críticos antes de aprender ("onde posso aproveitar o que já sei?")

**Regra**: ao aprender nova linguagem ou framework, dedique tempo explícito a mapear similaridades e diferenças com o que já conhece (syntax, type system, conceitos, runtime, práticas de teste). Isso ativa transfer positivo e previne negativo.

### Misconceptions — Bugs no Pensamento

Uma **misconception** é uma crença:
1. Incorreta
2. Mantida consistentemente em diferentes situações
3. Mantida com confiança

Exemplo clássico em programação: "Uma variável pode guardar uma relação" (transferida da matemática) → assume que mudar `maximum` também muda `total = maximum + 12`. Exemplo: "While loop para imediatamente quando condição muda" (transferida do inglês natural).

**Misconceptions não são eliminadas por correção simples** — o modelo antigo permanece na LTM e pode ressurgir em situações de alta carga cognitiva. A correção exige **conceptual change**: substituição ativa do modelo mental por um novo, não apenas adição de informação.

> 💡 Nota: mesmo após aprender o modelo correto, o modelo antigo incorreto pode reaparecer em situações de pressão — isso é um fenômeno normal de como a memória funciona, não sinal de incompetência.

**Como prevenir misconceptions ao aprender nova linguagem**:
1. Manter postura de "posso estar errado" mesmo quando confiante.
2. Estudar proativamente misconceptions comuns (Sorva, 2012: lista de 162 misconceptions de novatos).
3. Buscar programadores que aprenderam as mesmas linguagens na mesma ordem — eles conhecem as armadilhas específicas.
4. Programar em pares — expõe conflitos de premissas.

**Como combater misconceptions no codebase**:
- Adicione testes para verificar suas premissas sobre o código ("esse valor nunca pode ser negativo" → escreva um teste que prove isso).
- Adicione documentação em locais estratégicos sobre comportamentos contraintuitivos.

> ⚠ Evite: assumir que conhecer uma linguagem bem significa que o transfer para outra será automático ou completo — far transfer (ex.: Java → Prolog) requer aprendizado novo substancial, incluindo flashcards de sintaxe e novas estratégias de resolução de problemas.

## 8 Nomenclatura de Identificadores

**Por que nomes importam**:
- Identificadores compõem 33% dos tokens e 72% dos caracteres de codebases reais (estudo com Eclipse ~2M linhas).
- 1 em cada 4 code reviews contém comentários sobre nomes.
- Nomes são a documentação mais acessível — estão dentro do código, sem necessidade de navegação externa.
- Nomes servem como beacons.

**Naming é difícil durante a codificação** — ao resolver problemas, a working memory está em capacidade máxima; escolher um bom nome aumenta a carga. Use placeholder names ao codar; avalie e melhore nomes no code review, não enquanto programa.

**Nomes têm impacto persistente** (Lawrie, 2007): a qualidade de nomenclatura definida nas fases iniciais de um projeto tende a permanecer inalterada. Invista em convenções de naming desde o início do projeto.

### O que Ativa na Leitura de um Nome

Três tipos de conhecimento que nomes podem ativar na LTM do leitor:

| Tipo | Exemplos |
|---|---|
| **Domínio** | `Customer`, `Shipment`, `Invoice` |
| **Conceito de programação** | `Tree`, `List`, `Hashmap` |
| **Convenção** | `i`, `j` (loop counters), `n`, `m` (dimensions), `s` (string), `c` (char) |

> 💡 Nota: fora de i/j/k/n (inteiros), s (string) e c (char), letras únicas têm baixo consenso de tipo entre programadores — não assuma que `t` ou `b` comunicará o tipo esperado ao leitor.

### Regras Práticas de Nomenclatura

**Butler's naming conventions** (problemas a evitar):
- Nomes menores que 8 chars (exceto convenções: i, j, k, m, n, x, y, z, etc.)
- Mais de 4 palavras (excede working memory)
- Abreviações não-padrão (`pag_countr`)
- Notação húngara de sistema (`int_page_counter`)
- Underscores externos/consecutivos (`__page_counter_`)
- Capitalização inconsistente

**Consistência supera qualidade individual** (Allamanis): nomes consistentemente mediocres são melhores do que bons nomes inconsistentes. Consistência suporta chunking — o leitor aprende o padrão e pode processar nomes mais rapidamente.

**Palavras completas > abreviações > letras únicas**:
- Palavras completas → 19% mais bugs encontrados por minuto em code review (Hofmeister, C# study)
- Mais sílabas → mais difícil de memorizar (STM); tradeoff entre clareza e recordação
- Prefixos/sufixos: avalie se o benefício de clareza supera o custo cognitivo de nomes mais longos

**Camel case vs. snake case** (Binkley, 2009): camel case → 51,5% maior chance de selecionar identificador correto; snake case → 0,5s mais rápido de processar. Treinamento em um estilo impacta negativamente performance no outro — siga a convenção do codebase.

### Name Molds (Feitelson)

Name molds são padrões de combinação de palavras: `max_X`, `X_per_Y`, `max_X_per_Y`, `X_num`, etc. Múltiplos molds no mesmo codebase criam carga cognitiva extrínseca. Programadores raramente escolhem o mesmo nome (probabilidade mediana de 7%), mas conseguem entender os nomes escolhidos por outros — porque os molds são compartilhados implicitamente.

**Regra**: ao iniciar um projeto, defina explicitamente 2-4 molds que o time usará. Em projetos existentes, levante os molds presentes e decida quais consolidar.

### Modelo de 3 Passos para Bons Nomes (Feitelson)

1. **Selecione os conceitos** — quais informações o objeto carrega? Para que é usado? Se você sente necessidade de comentar o nome, o comentário pertence ao nome.
2. **Escolha as palavras** — use o vocabulário do domínio; mantenha um lexicon do projeto para resolver ambiguidades entre sinônimos.
3. **Construa o nome** — escolha um mold; siga a ordem natural da linguagem (`max_points` > `points_max`); adicione preposições quando ajudar (`indexOf`, `elementAt`).

Nomes gerados com esse modelo foram avaliados como superiores em proporção 2:1 (experimento com 100 participantes).

**Código com nomes ruins tem mais bugs** (Butler, 2009): posições no código com violações de naming têm correlação estatística com posições de bugs. Use detecção de violações de naming como heurística para identificar áreas de risco no codebase.

> ⚠ Evite: avaliar qualidade de nomes enquanto está ativamente resolvendo o problema — o momento certo é o code review, quando a working memory está disponível para esta tarefa.

## 9 Code Smells e Antipadrões Linguísticos

**Code smells** (Fowler, 1999) são estruturas de código que — sem necessariamente introduzir um bug — correlacionam estatisticamente com maior frequência de bugs e maior propensão a mudanças futuras.

### Os 22 Code Smells de Fowler

| Nível | Code smell |
|---|---|
| **Método** | Long method, Long parameter list, Switch statements, Speculative generality, Temporary field |
| **Classe** | Large class (God class), Lazy class, Data class, Refused bequest, Alternative classes with different interfaces, Incomplete library class |
| **Codebase** | Duplicated code, Divergent change, Shotgun surgery, Feature envy, Data clumps, Primitive obsession, Message chains, Middle man, Inappropriate intimacy, Comments, Parallel inheritance hierarchies |

### Base Cognitiva dos Code Smells

Code smells não são arbitrários — cada um corresponde a uma sobrecarga cognitiva específica:

| Code smell | Mecanismo cognitivo afetado |
|---|---|
| **Long parameter list** | Excede capacidade da working memory (2-6 elementos); o leitor não consegue manter todos os parâmetros simultaneamente |
| **Complex switch statement** | Cada caso adiciona um elemento à working memory (tracing de múltiplos caminhos); rapidamente ultrapassa o limite |
| **God class / Long method** | Impede chunking eficiente — o leitor não consegue tratar o bloco como um chunk único na STM |
| **Duplicated code** | Induz "wrong chunking": o leitor assume que dois trechos similares são idênticos (chunk único) e para de ler o segundo, perdendo diferenças críticas |

**Regra**: ao revisar código, use a base cognitiva dos smells como diagnóstico — não é apenas "convenção ruim", é um preditor de onde colegas terão dificuldade cognitiva real.

### Antipadrões Linguísticos (Arnaoudova, 2014)

Antipadrões linguísticos são inconsistências entre o nome de um identificador e seu comportamento real. Estudados por Arnaoudova em 6 categorias:

**Métodos**:
| Categoria | Antipadrão | Exemplo |
|---|---|---|
| Método faz mais do que o nome diz | Nome sugere getter, mas método modifica estado | `getValues()` que apaga o cache |
| Método faz menos do que o nome diz | Nome sugere ação, mas é no-op condicional | `save()` que só salva se dirty=true, sem avisar |
| Método faz o oposto do nome | Nome afirmativo, comportamento negativo | `isValid()` que retorna lista de erros (não Boolean) |

**Identificadores (atributos/variáveis)**:
| Categoria | Antipadrão | Exemplo |
|---|---|---|
| Nome contém mais informação do que o valor | Nome sugere coleção, valor é escalar | `pageElements` que contém apenas o total count |
| Nome contém menos informação do que o valor | Nome sugere escalar, valor é coleção | `element` que é uma lista |
| Nome contém informação oposta ao valor | Nome e tipo contradizem o conteúdo | `isFound` declarado como `int` contendo lista de índices |

### Impacto Cognitivo Medido (fNIRS)

Fakhoury et al. (2018) mediram carga cognitiva por fNIRS (fluxo de sangue oxigenado no córtex pré-frontal) durante leitura de código:

- **Antipadrões linguísticos** → aumento estatisticamente significativo na carga cognitiva vs. código correto.
- **Inconsistências estruturais** (código mal-formatado/indentalado) → *sem diferença estatística* vs. controle.

**Mecanismos cognitivos**:
1. **Ativação errada de LTM**: ler `retrieveElements()` ativa schema de "retorna coleção"; se o método retorna escalar, o schema errado foi carregado → dissonância que exige processamento extra.
2. **Wrong chunking**: ler `isValid` ativa chunk "retorna Boolean"; se retorna lista de inteiros, o chunk está errado → o leitor precisa desfazer e reprocessar o significado.

**Regra**: naming consistente com comportamento é mais importante do que formatting consistente — o impacto cognitivo de nomes enganosos é mensurável via neuroimagem; o de código levemente mal-formatado não.

> ⚠ Evite: nomear getters que modificam estado, flags que contêm listas, ou métodos de ação que são no-ops condicionais — cada um desses causa ativação errada de schema na LTM do leitor e exige reprocessamento cognitivo.

## 10 Resolução de Problemas Complexos

**Resolução de problemas não é uma habilidade genérica** — pesquisa mostra consistentemente que não existe processo cognitivo universal para resolução de problemas. Técnicas genéricas como os 3 passos de Pólya (entender → planejar → executar) dependem de conhecimento de domínio na LTM para funcionarem.

**Regra**: ao enfrentar um problema de programação, busque estratégias específicas do domínio na LTM em vez de aplicar um método genérico — o método genérico não fornece clues suficientes para o cérebro recuperar as memórias relevantes.

### Tipos de Memória na LTM

| Tipo | Subtipo | Descrição | Criação |
|---|---|---|---|
| **Implícita (Procedural)** | — | "Memória muscular"; habilidades executadas sem atenção consciente (touch typing, adicionar colchete de fechamento) | Por repetição |
| **Explícita (Declarativa)** | Episódica | Memórias de experiências ("como resolvi aquele bug na semana passada") | Automática, fortalecida pela revisão |
| **Explícita (Declarativa)** | Semântica | Fatos e conceitos ("sintaxe do for-loop em Java") | Requer atenção explícita (flashcards) |

**Experts dependem fortemente de memória episódica** — ao invés de resolver problemas, *recriam* soluções de problemas similares passados.

**Implicação prática**: experiência acumulada é uma coleção de soluções episódicas. Cada problema resolvido gera uma instância de memória que pode ser recuperada em situações similares futuras.

### Automatização — Criando Memórias Implícitas

**Automatização** é o processo de praticar uma habilidade até atingir a fase autônoma, onde pode ser executada sem esforço cognitivo consciente. Skills automatizadas não adicionam carga cognitiva, liberando a working memory para problemas maiores.

**Três fases de aquisição de habilidade**:

| Fase | Característica | Indicador |
|---|---|---|
| **Cognitiva** | Atenção explícita necessária; schemata sendo criados/atualizados | Precisa pensar em cada passo individualmente |
| **Associativa** | Repetição cria padrões; ações eficazes são retidas | Usa truques e atalhos mentais |
| **Autônoma** | Habilidade perfeita; execução sem esforço; sem necessidade de verificar | Faz corretamente em qualquer contexto, sem pensar |

**Teoria das instâncias (Logan)**: automatização ocorre quando você recupera memórias episódicas de execuções anteriores em vez de raciocinar sobre a tarefa. Automatização completa = total dependência da memória episódica, zero raciocínio.

**Regra — deliberate practice para automatização**:
1. Escreva muitas variações pequenas do skill-alvo (não apenas resolva problemas inteiros).
2. Adapte programas existentes em vez de criar do zero — foca nas diferenças entre o conhecido e o novo.
3. Use spaced repetition: pratique diariamente até atingir consistência autônoma.

> 💡 Nota: programar muito não automatiza automaticamente habilidades específicas. Deliberate practice explícita (ex.: escrever 100 for-loops intencionalmente) é necessária para construir memória implícita em áreas ainda problemáticas.

### Worked Examples — Aprender de Soluções de Outros

**Worked example** = solução explicada de um problema, com o raciocínio passo a passo detalhado.

**Efeito Sweller** (experimento com 9ºanos, álgebra): o grupo que recebeu exemplos resolvidos (receitas) resolveu problemas 5× mais rápido — e também performou melhor em *novos* problemas. Replicado em matemática, música, xadrez, esporte e programação.

**Explicação via carga cognitiva**: quando a working memory está cheia com intrinsic + extraneous load, não há espaço para **germane load** (o esforço de armazenar informação na LTM). Estudar exemplos resolvidos libera working memory → permite aprendizado real.

| Tipo de carga | Definição |
|---|---|
| **Intrinsic** | Complexidade do problema em si |
| **Extraneous** | Complexidade acidental da apresentação |
| **Germane** | Esforço de consolidar novo conhecimento na LTM |

**Regra**: "You don't become an expert by doing expert things" (Kirschner). Estude código de outros + explicações, não apenas programe.

**Como usar worked examples no dia a dia**:
- Clube de leitura de código com colegas (code-reading.org).
- Ler código de bibliotecas/frameworks conhecidos no GitHub.
- Ler blog posts que explicam como um problema foi resolvido.
- Escrever um resumo do seu próprio código e trocar com colegas.

> ⚠ Evite: assumir que programar mais é suficiente para se tornar melhor em resolver problemas — prática sem reflexão e sem estudo de soluções existentes produz pouco ganho em habilidade de resolução de problemas.

## 11 O Ato de Escrever Código

### 5 Atividades de Programação (Framework CDN — Green, Blackwell, Petre)

| Atividade | Descrição | Sistema mais exigido |
|---|---|---|
| **Searching** | Procurar informação específica no codebase (localização de bug, chamadas de método) | STM |
| **Comprehension** | Ler/executar código para entender funcionalidade (58% do tempo dos devs) | Working memory |
| **Transcription** | "Só codar" — plano definido, implementando sem busca ou compreensão | LTM |
| **Incrementation** | Mix de searching + comprehension + transcription para adicionar nova feature | Todos os 3 |
| **Exploration** | Esboçar com código; ganha clareza ao programar, sem plano fixo | Working memory (principalmente) |

**Debugging** não é uma atividade separada — é uma sequência de exploration + searching + comprehension + transcription.

**Regra**: ao iniciar uma tarefa de incrementation (a mais comum na vida profissional), decomponha explicitamente em subtarefas (search, then comprehend, then transcribe) e suporte cada uma com a técnica certa.

**Suporte por atividade**:
- **Searching**: anote o que está procurando, onde já buscou, o que encontrou. Deixe "migalhas de pão" em comentários.
- **Comprehension**: desenhe modelo do código e atualize-o. Externaliza a working memory. Refatoring cognitivo é válido.
- **Transcription**: invista em LTM (sintaxe, APIs). Automatize se necessário.
- **Exploration**: documente direção e decisões de design mesmo que brevemente.

### Interrupções — Custo e Mitigação

**Dados sobre interrupções**:
- 20% do tempo de desenvolvimento é perdido com interrupções (Van Solingen).
- Após interrupção, são necessários ~15-20 minutos para retomar o contexto.
- Um programador médio tem apenas 1 sessão de 2h ininterrupta por dia (Parnin).
- 62% dos devs consideram recuperação de interrupções um problema sério (Microsoft).
- Interrupções durante tarefas (vs. entre tarefas) causam mais irritação, mais ansiedade, e 2× mais erros (Bailey).

**O que acontece após a interrupção**: a working memory perde as informações sobre o código. O programador precisa renaivegar em vários pontos do código para reconstruir o contexto.

**3 técnicas para lidar com interrupções**:

1. **Armazene o modelo mental** — ao ser interrompido, faça um brain dump do estado atual em um comentário. Inclua: o que está fazendo, por quê essa abordagem, quais alternativas foram descartadas, qual é o próximo passo. Essa documentação é recuperável mais rápido do que notas externas.

2. **Suporte a memória prospectiva** — memória prospectiva é a memória de lembrar de fazer algo no futuro. Use TODO comments com datas de expiração; defina status no Slack para sinalizar que está em deep work e não quer ser interrompido.

3. **Subgoal labeling** — antes de começar uma tarefa, escreva os passos no código como comentários (`# parse text`, `# filter tree`, `# flatten`). Após interrupção, os subgoals fornecem a estrutura para retomada imediata. Subgoals também servem como documentação posterior.

**Warm-up cognitivo** (Nakagawa, 2014): a carga cognitiva em tarefas de compreensão é maior no *meio* da tarefa — há uma fase de aquecimento e resfriamento. Interruptions destroem o trabalho de aquecimento.

**Regra**: ao precisar parar no meio de uma tarefa, documente o estado mental explicitamente em comentários — o código não preserva o "por quê" das decisões.

**FlowLight** (Züger): luz física controlada por padrões de digitação/mouse detecta programador em deep work e sinaliza verde/vermelho. Estudo com 400+ participantes mostrou redução de 46% nas interrupções.

**Multitasking**: evidências consistentes que o cérebro não consegue multitask em tarefas cognitivamente exigentes. Estudantes que leram texto com mensagens instantâneas levaram 50% mais tempo. Heavy Facebook users tinham GPA significativamente mais baixo, especialmente os que respondiam mensagens imediatamente.

**Regra**: programar e usar Slack simultaneamente reduz qualidade do código — use status/FlowLight para criar períodos de deep work protegidos.

> ⚠ Evite: responder mensagens e programar simultaneamente — multitasking em tarefas cognitivas é impossível para o cérebro humano; você produz mais erros e leva mais tempo, mesmo sentindo que está sendo produtivo.

## 12 Dimensões Cognitivas de Codebases (CDCB)

**CDN (Cognitive Dimensions of Notation)** — framework de Green, Blackwell e Petre para avaliar o impacto cognitivo de linguagens de programação. **CDCB** é a extensão do livro aplicada a *codebases* (bibliotecas, frameworks, módulos).

### As 12 Dimensões

| Dimensão | O que avalia | Impacto cognitivo |
|---|---|---|
| **Error Proneness** | Facilidade de cometer erros | Type systems reduzem error proneness; nomes vagos e convenções inconsistentes aumentam |
| **Consistency** | Similaridade entre elementos similares | Inconsistência causa carga extrínseca; antipadrões linguísticos diminuem consistência |
| **Diffuseness** | Espaço/tamanho que construtos ocupam | Código difuso (mais linhas/chunks) é mais lento para busca |
| **Hidden Dependencies** | Visibilidade das dependências | Dependências ocultas dificultam searching; IDEs ajudam mas exigem ação explícita |
| **Provisionality** | Facilidade de pensar/esboçar usando o sistema | Sistemas muito estritos (tipos, assertions) dificultam exploração; Scratch/Python têm alta provisionality |
| **Viscosity** | Dificuldade de fazer mudanças | Sistemas tipados têm menor viscosidade (type system guia); sistemas sem modularidade têm maior |
| **Progressive Evaluation** | Facilidade de executar código parcial/incompleto | Live programming (Smalltalk, Scratch) = alta progressive evaluation; compile/run obrigatório = baixa |
| **Role Expressiveness** | Clareza do papel de cada elemento | Parênteses em chamadas de função, syntax highlighting, prefixo `is_` = alta role expressiveness |
| **Closeness of Mapping** | Proximidade entre código e domínio do problema | APL/COBOL têm alta closeness para seus domínios; Python/Java são genéricos (baixa por padrão) |
| **Hard Mental Operations** | Operações cognitivamente exigentes que o sistema impõe | Muitos parâmetros em ordem específica → STM overload; nomes não-informativos → LTM extra |
| **Secondary Notation** | Capacidade de adicionar significado extra (não formal) | Comentários, named parameters Python, whitespace adicional = secondary notation |
| **Abstraction** | Capacidade do usuário criar abstrações tão poderosas quanto as built-ins | Subclasses, decorators, funções de primeira classe = alta abstraction; assembly = baixa |
| **Visibility** | Facilidade de ver diferentes partes do sistema | Visibilidade baixa dificulta compreensão de relacionamentos entre classes/funções |

### Trade-offs entre Dimensões

Design maneuvers (mudanças em uma dimensão) tipicamente afetam outras:

- **Error proneness ↓ ↔ Viscosity ↑** — adicionar tipos reduz erros mas exige mais trabalho em cada mudança.
- **Provisionality + Progressive Evaluation ↑ ↔ Error Proneness ↑** — código parcial/incompleto pode permanecer no codebase sem ser limpo.
- **Role Expressiveness ↑ ↔ Diffuseness ↑** — named parameters e type annotations aumentam clareza mas aumentam tamanho do código.

**Regra**: ao fazer um design maneuver, avalie explicitamente quais outras dimensões serão impactadas positiva e negativamente antes de aplicar.

### Dimensões por Atividade de Programação

| Atividade | Dimensões que ajudam | Dimensões que prejudicam |
|---|---|---|
| **Searching** | Secondary notation, Consistency | Diffuseness, Hidden dependencies |
| **Comprehension** | Role expressiveness, Abstraction, Visibility | Visibility baixa |
| **Transcription** | — | Consistency (exige conformidade ao padrão) |
| **Incrementation** | Closeness of mapping | Hard mental operations, Viscosity |
| **Exploration** | Provisionality, Progressive evaluation | Hard mental operations, Abstraction excessiva |

**Regra**: identifique qual atividade seu codebase/library suportará mais (busca em código legado → otimize secondary notation; adição de features → otimize closeness of mapping e reduza viscosity).

**Regra**: analise as dimensões do seu codebase anualmente como checklist. Codebases mudam de perfil com o tempo — um projeto novo (incrementation-heavy) tem necessidades opostas a uma biblioteca estável (searching-heavy).

**Domain-Driven Design como closeness of mapping**: DDD prescreve que nomes e estruturas no código reflitam o domínio do negócio — é uma aplicação intencional de closeness of mapping. `findCustomers()` > `executeQuery()`.

> ⚠ Evite: avaliar linguagens apenas por características técnicas (paradigma, tipagem, performance) — o impacto cognitivo das dimensões CDCB é um preditor igualmente importante de como desenvolvedores interagirão com o código.

## 13 Onboarding de Novos Desenvolvedores

### O Problema Central: Curva da Expertise

**Curse of expertise**: ao dominar uma skill, o expert inevitavelmente esquece o quão difícil foi aprendê-la e superestima o quanto um novato pode processar simultaneamente.

**Problema típico de onboarding**:
1. Senior apresenta domínio + workflow + codebase + pessoas ao mesmo tempo.
2. Pede tarefa "simples" (small bug, small feature).
3. Novato falha → senior acha que novato "não é muito bom"; novato acha que o projeto é impossível.

**Causa real**: working memory do novato está sobrecarregada. Sem espaço para germane load, o novato não retém o que aprendeu — o onboarding é desperdiçado.

### Estágios Neo-Piagetianos para Programação (Lister)

Os estágios de Piaget são *domain-specific*: um programador experiente em Java pode estar no estágio sensorimotor ao aprender Haskell.

| Estágio | Comportamento em programação | Como apoiar |
|---|---|---|
| **Sensorimotor** | Não consegue traçar um programa corretamente; entendimento incoerente da execução | Foque em modelo de execução antes de qualquer conceito abstrato |
| **Preoperacional** | Traça pequenos trechos; raciocina indutivamente (adivinha comportamento por poucos exemplos); diagramas não ajudam ainda | Flashcards de sintaxe; mais exemplos de tracing; evite diagramas |
| **Concreto-operacional** | Raciocina dedutivamente sobre o código; reconhece chunks; usa diagramas; ainda pode falta visão global | Diagramas agora ajudam; tasks de exploration guiada |
| **Formal operacional** | Raciocina lógica e sistematicamente; reflete sobre próprias ações (essencial para debug) | Autonomia; code review discussions; design discussions |

**Regra diagnóstica**: se um novato não consegue traçar corretamente um programa simples, está no estágio sensorimotor — não adianta explicar arquitetura ou design patterns ainda.

### Onda Semântica (Maton) — Como Ensinar Conceitos

Ao ensinar um novo conceito, siga a onda:

1. **Abstract** — por que esse conceito existe? Para que serve? (ex.: "funções variádicas permitem número variável de argumentos")
2. **Unpacking** (concreto) — como usar na prática? Sintaxe, detalhes de implementação.
3. **Repacking** (abstract) — integre ao conhecimento existente: compare com outras linguagens, identifique quando usar.

**3 antipadrões a evitar**:
- **High flatline**: só explicação abstrata → novato não sabe como usar.
- **Low flatline**: só detalhes concretos → novato não sabe quando/por que usar.
- **Downward escalator**: vai de abstrato para concreto mas esquece o repacking → o conhecimento não é integrado à LTM.

**Regra**: sempre pergunte ao novato ao final de uma explicação: "Como isso se compara com o que você já conhece em X?" — força o repacking ativamente.

### 3 Atividades para Melhorar o Onboarding

**1. Separe as atividades de programação**

Não peça incrementation (que mistura searching + comprehension + transcription) logo de início. Ofereça tarefas em atividades isoladas, progressivamente:

| Atividade | Exemplo de task inicial |
|---|---|
| Exploration | Navegar o codebase e descrever o que cada módulo faz |
| Searching | Encontrar a classe que implementa uma interface específica |
| Comprehension | Resumir um método específico em linguagem natural |
| Transcription | Implementar um método a partir de um plano detalhado já fornecido |
| Incrementation | Adicionar uma feature com apoio do senior (apenas após as anteriores) |

**2. Apoie a memória do novato**

- **LTM**: documente previamente todos os conceitos de domínio, frameworks, bibliotecas e ferramentas que aparecem no código. Uma frase como "usamos Laravel no Heroku com Jenkins" contém 3 unknowns para um novato.
- **STM**: separe o aprendizado do domínio da exploração do código — não apresente os dois ao mesmo tempo.
- Use vocabulário compartilhado de ciência cognitiva: "Estou com carga cognitiva muito alta nessa parte" é mais preciso e acionável do que "Estou confuso".

**3. Gerencie a carga cognitiva explicitamente**

- Introduza conceitos um por vez.
- Separe aprendizado de linguagem de aprendizado do domínio do negócio.
- Respeite o estágio neo-Piagetian: se o novato está em sensorimotor, nenhuma explicação de alto nível será efetiva ainda.

> ⚠ Evite: apresentar domínio + workflow + codebase + ferramentas simultaneamente no onboarding — o excesso de carga elimina o espaço para germane load, tornando o onboarding ineficaz independentemente da qualidade das explicações.
