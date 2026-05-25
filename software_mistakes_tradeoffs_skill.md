
# Skill: Software Mistakes and Tradeoffs — Referência Consolidada

> **Fonte**: Software Mistakes and Tradeoffs, Tomasz Lelek & Jon Skeet, Manning, 2022
> **Alvo**: engenharia de software, design de sistemas, decisões técnicas
> **Última extração**: 2026-05 — Todos os 13 capítulos extraídos (completo)

---

## Índice

| # | Seção |
|---|---|
| 1 | [Filosofia de Tradeoffs](#1-filosofia-de-tradeoffs) |
| 2 | [Testes: Unit vs. Integration vs. End-to-End](#2-testes-unit-vs-integration-vs-end-to-end) |
| 3 | [Singleton Pattern — Tradeoffs em Contexto Multithreaded](#3-singleton-pattern--tradeoffs-em-contexto-multithreaded) |
| 4 | [Microservices vs. Monolith — Tradeoffs de Arquitetura](#4-microservices-vs-monolith--tradeoffs-de-arquitetura) |
| 5 | [Compartilhamento de Código — Biblioteca vs. Microserviço vs. Duplicação](#5-compartilhamento-de-código--biblioteca-vs-microserviço-vs-duplicação) |
| 5.1 | [Duplicação entre codebases](#51-duplicação-entre-codebases) |
| 5.2 | [Biblioteca compartilhada](#52-biblioteca-compartilhada) |
| 5.3 | [Extração para microserviço](#53-extração-para-microserviço) |
| 5.4 | [Framework de decisão](#54-framework-de-decisão-para-compartilhamento-de-código) |
| 6 | [Herança, Composição e Duplicação Intencional](#6-herança-composição-e-duplicação-intencional) |
| 6.1 | [Template Method para lógica comum](#61-template-method-para-compartilhar-lógica-comum) |
| 6.2 | [Tight coupling da herança](#62-tight-coupling-introduzido-pela-herança) |
| 6.3 | [Composição como alternativa](#63-composição-como-alternativa) |
| 6.4 | [Duplicação incidental vs. inherente](#64-duplicação-incidental-vs-inherente) |
| 7 | [Tratamento de Exceções](#7-tratamento-de-exceções) |
| 7.1 | [Hierarquia e granularidade de captura](#71-hierarquia-e-granularidade-de-captura) |
| 7.2 | [API pública — checked vs. unchecked](#72-api-pública--checked-vs-unchecked) |
| 7.3 | [Antipadrões de exception handling](#73-antipadrões-de-exception-handling) |
| 7.4 | [Exceções de bibliotecas de terceiros](#74-exceções-de-bibliotecas-de-terceiros) |
| 7.5 | [Exceções em ambientes multithread e async](#75-exceções-em-ambientes-multithread-e-async) |
| 7.6 | [Abordagem funcional com Try (Vavr)](#76-abordagem-funcional-com-try-vavr) |
| 7.7 | [Performance de exception handling](#77-performance-de-exception-handling) |
| 8 | [Extensibilidade e Flexibilidade de APIs](#8-extensibilidade-e-flexibilidade-de-apis) |
| 8.1 | [Design evolutivo: comece simples](#81-design-evolutivo-comece-simples) |
| 8.2 | [Abstraindo dependências de terceiros](#82-abstraindo-dependências-de-terceiros) |
| 8.3 | [Hooks API](#83-hooks-api) |
| 8.4 | [Listener API (Observer Pattern)](#84-listener-api-observer-pattern) |
| 8.5 | [Framework: flexibilidade vs. complexidade](#85-framework-flexibilidade-vs-complexidade) |
| 9 | [Otimização de Performance — Hot Path vs. Premature Optimization](#9-otimização-de-performance--hot-path-vs-premature-optimization) |
| 9.1 | [Quando otimização prematura é um erro](#91-quando-otimização-prematura-é-um-erro) |
| 9.2 | [Princípio de Pareto e identificação do hot path](#92-princípio-de-pareto-e-identificação-do-hot-path) |
| 9.3 | [Configurando threads para SLA](#93-configurando-threads-para-sla) |
| 9.4 | [Detecção de hot path com ferramentas](#94-detecção-de-hot-path-com-ferramentas) |
| 9.5 | [Otimizações para o hot path — cache eager vs. lazy](#95-otimizações-para-o-hot-path--cache-eager-vs-lazy) |
| 9.6 | [Recálculo de impacto e ajuste dos benchmarks](#96-recálculo-de-impacto-e-ajuste-dos-benchmarks) |
| 10 | [Simplicidade vs. Custo de Manutenção de APIs de Configuração](#10-simplicidade-vs-custo-de-manutenção-de-apis-de-configuração) |
| 10.1 | [Exposição direta das settings da lib downstream](#101-exposição-direta-das-settings-da-lib-downstream) |
| 10.2 | [Abstração das settings da lib downstream](#102-abstração-das-settings-da-lib-downstream) |
| 10.3 | [Quando mudança no downstream é um breaking change](#103-quando-mudança-no-downstream-é-um-breaking-change) |
| 10.4 | [Framework de decisão](#104-framework-de-decisão) |
| 11 | [Data e Hora — Tradeoffs de Design](#11-data-e-hora--tradeoffs-de-design) |
| 11.1 | [Conceitos fundamentais](#111-conceitos-fundamentais) |
| 11.2 | [Timezone ≠ UTC offset](#112-timezone--utc-offset) |
| 11.3 | [Testabilidade: injetar Clock](#113-testabilidade-injetar-clock) |
| 11.4 | [Product requirements e scoping](#114-product-requirements-e-scoping) |
| 11.5 | [Representação textual](#115-representação-textual) |
| 11.6 | [Corner cases de calendário e fusos](#116-corner-cases-de-calendário-e-fusos) |
| 11.7 | [Source-of-truth vs. derived data](#117-source-of-truth-vs-derived-data) |
| 12 | [Data Locality e Processamento Big Data](#12-data-locality-e-processamento-big-data) |
| 12.1 | [Mover computação para os dados](#121-mover-computação-para-os-dados) |
| 12.2 | [Particionamento temporal (offline)](#122-particionamento-temporal-offline) |
| 12.3 | [Hash partitioning e sharding](#123-hash-partitioning-e-sharding) |
| 12.4 | [Narrow vs. wide transformation e data shuffling](#124-narrow-vs-wide-transformation-e-data-shuffling) |
| 12.5 | [Broadcast join](#125-broadcast-join) |
| 12.6 | [Disk vs. Memory: Hadoop vs. Spark](#126-disk-vs-memory-hadoop-vs-spark) |
| 13 | [Bibliotecas de Terceiro — Tradeoffs e Armadilhas](#13-bibliotecas-de-terceiro--tradeoffs-e-armadilhas) |
| 13.1 | [Defaults de bibliotecas: assuma responsabilidade total](#131-defaults-de-bibliotecas-assuma-responsabilidade-total) |
| 13.2 | [Modelo de concorrência: blocking vs. async](#132-modelo-de-concorrência-blocking-vs-async) |
| 13.3 | [Testabilidade de bibliotecas externas](#133-testabilidade-de-bibliotecas-externas) |
| 13.4 | [Dependências transitivas e shading](#134-dependências-transitivas-e-shading) |
| 13.5 | [Critérios de seleção e manutenção](#135-critérios-de-seleção-e-manutenção) |
| 14 | [Consistência e Atomicidade em Sistemas Distribuídos](#14-consistência-e-atomicidade-em-sistemas-distribuídos) |
| 14.1 | [At-least-once delivery e idempotência](#141-at-least-once-delivery-e-idempotência) |
| 14.2 | [CQRS: Command Query Responsibility Segregation](#142-cqrs-command-query-responsibility-segregation) |
| 14.3 | [Implementação ingênua de deduplicação](#143-implementação-ingênua-de-deduplicação) |
| 14.4 | [Problemas de atomicidade em contexto distribuído](#144-problemas-de-atomicidade-em-contexto-distribuído) |
| 14.5 | [Tornando a lógica atômica com upsert](#145-tornando-a-lógica-atômica-com-upsert) |
| 15 | [Semântica de Entrega em Sistemas Distribuídos](#15-semântica-de-entrega-em-sistemas-distribuídos) |
| 15.1 | [Arquitetura event-driven e pub-sub](#151-arquitetura-event-driven-e-pub-sub) |
| 15.2 | [Apache Kafka: tópicos, partições, brokers](#152-apache-kafka-tópicos-partições-brokers) |
| 15.3 | [Lógica do producer: acks e consistência vs. disponibilidade](#153-lógica-do-producer-acks-e-consistência-vs-disponibilidade) |
| 15.4 | [Lógica do consumer: semântica de entrega](#154-lógica-do-consumer-semântica-de-entrega) |
| 15.5 | [Effectively exactly-once semantics](#155-effectively-exactly-once-semantics) |
| 15.6 | [Fault tolerance via delivery guarantees](#156-fault-tolerance-via-delivery-guarantees) |
| 16 | [Versionamento e Compatibilidade](#16-versionamento-e-compatibilidade) |
| 16.1 | [Semantic Versioning (SemVer)](#161-semantic-versioning-semver) |
| 16.2 | [Backward vs. forward compatibility](#162-backward-vs-forward-compatibility) |
| 16.3 | [Tipos de compatibilidade em bibliotecas](#163-tipos-de-compatibilidade-em-bibliotecas) |
| 16.4 | [Hyrum's Law: compatibilidade semântica](#164-hyrums-law-compatibilidade-semântica) |
| 16.5 | [Diamond dependency: compartilhada vs. isolada](#165-diamond-dependency-compartilhada-vs-isolada) |
| 16.6 | [Técnicas para gerenciar breaking changes](#166-técnicas-para-gerenciar-breaking-changes) |
| 16.7 | [Bibliotecas internas](#167-bibliotecas-internas) |
| 16.8 | [Versionamento de APIs de rede](#168-versionamento-de-apis-de-rede) |
| 16.9 | [Versionamento de armazenamento de dados](#169-versionamento-de-armazenamento-de-dados) |
| 16.10 | [Separando schemas de API e de armazenamento](#1610-separando-schemas-de-api-e-de-armazenamento) |
| 17 | [Tendências vs. Custo de Manutenção](#17-tendências-vs-custo-de-manutenção) |
| 17.1 | [Dependency Injection: DIY vs. framework](#171-dependency-injection-diy-vs-framework) |
| 17.2 | [Programação Reativa: CompletableFuture vs. Flux](#172-programação-reativa-completablefuture-vs-flux) |
| 17.3 | [Programação Funcional em Linguagem OO](#173-programação-funcional-em-linguagem-oo) |
| 17.4 | [Inicialização Lazy vs. Eager](#174-inicialização-lazy-vs-eager) |

---

## 1 Filosofia de Tradeoffs

Toda decisão de design limita a possibilidade de evoluir em direções alternativas. Quanto mais tempo um sistema vive, mais difícil é reverter decisões estruturais.

**Regra**: Ao tomar qualquer decisão de design, identifique explicitamente os prós e contras de cada direção e o contexto que torna uma preferível à outra.

**Regra**: Meça suas suposições com dados reais antes de escolher entre alternativas de desempenho. Sem dados, a decisão racional não é possível.

> 💡 Nota: O livro estrutura cada capítulo assim — problema num contexto específico → solução alternativa → análise de tradeoffs.

---

## 2 Testes: Unit vs. Integration vs. End-to-End

### 2.1 Decisão de visibilidade para testes

Ao testar um método privado com lógica complexa, há duas abordagens:

1. **Black-box**: testar somente a API pública — menor acoplamento, menor manutenção.
2. **Visibilidade elevada**: tornar o método `public` (com `@VisibleForTesting`) — permite teste direto, mas expõe a API a clientes involuntários.

**Regra**: Prefira tornar o método `package-private` (sem modificador) em vez de `public` para ganhar testabilidade sem expor a API pública completa.

> ⚠ Evite: usar `@VisibleForTesting` em métodos `public` sem documentação clara — clientes tendem a ignorar a anotação e usar o método diretamente.

### 2.2 Proporção entre tipos de teste

| Tipo | Feedback time | Custo de criação | Cobertura holística |
|------|--------------|-----------------|---------------------|
| Unit | Mais rápido | Baixo | Isolada (método/classe) |
| Integration | Médio | Médio | Componentes e suas interações |
| End-to-end | Mais lento | Alto (infra) | Sistema completo |

A pirâmide de testes reflete que sistemas reais devem ter mais unit tests do que integration tests, e mais integration tests do que end-to-end tests.

**Regra**: Use sempre uma combinação de unit e integration tests — cobrir 100% com unit tests deixa o sistema sem garantia das interações entre componentes.

**Regra**: Planeje end-to-end tests desde o início do projeto, como features — não como afterthought. A infra necessária é custosa de criar tardiamente.

> ⚠ Evite: sistemas com apenas unit tests — você terá algoritmos bem testados mas sem garantia de que os componentes se integram corretamente.

---

## 3 Singleton Pattern — Tradeoffs em Contexto Multithreaded

### 3.1 Implementação básica (single-threaded)

```java
public class Singleton {
  private static Singleton instance;
  private Singleton() {}
  public static Singleton getInstance() {
    if (instance == null) {
      instance = new Singleton();
    }
    return instance;
  }
}
```

Funciona corretamente apenas em contexto single-threaded.

### 3.2 Singleton sincronizado (thread-safe, mas lento)

```java
public static synchronized SystemComponent getInstance() {
  if (instance == null) {
    instance = new SystemComponent();
  }
  return instance;
}
```

> ⚠ Evite: usar `synchronized` em todo `getInstance()` em sistemas com alta concorrência — introduz thread contention severa, degradando performance drasticamente (benchmark: ~316 ms vs ~2.6 ms das alternativas).

### 3.3 Double-Checked Locking (recomendado para alta concorrência)

```java
private volatile static SystemComponent instance;

public static SystemComponent getInstance() {
  if (instance == null) {
    synchronized (ThreadSafeSingleton.class) {
      if (instance == null) {
        instance = new SystemComponent();
      }
    }
  }
  return instance;
}
```

A palavra-chave `volatile` é obrigatória para garantir visibilidade entre threads.

**Regra**: Use `volatile` com double-checked locking para singletons compartilhados entre threads — elimina contention pós-inicialização.

### 3.4 Thread Confinement com ThreadLocal

```java
static ThreadLocal<SystemComponent> threadLocalValue =
    ThreadLocal.withInitial(SystemComponent::new);

public static SystemComponent get() {
  return threadLocalValue.get();
}
```

Cada thread possui sua própria instância — elimina contention completamente, ao custo de N instâncias para N threads.

**Regra**: Use `ThreadLocal` quando o estado não precisa ser compartilhado entre threads — remove contention e aumenta performance, mas aumenta complexidade.

### 3.5 Resultados de benchmark (JMH, 100 threads, 50.000 operações)

| Implementação | Tempo médio |
|---|---|
| `synchronized` completo | ~316 ms |
| Thread confinement (ThreadLocal) | ~5.6 ms |
| Double-checked locking | ~2.6 ms |

### 3.6 Alternativas ao Singleton

- **Static initializer**: inicializar na carga da classe — mais simples, mas requer que o estado de init seja conhecido em tempo de carregamento.
- **Dependency Injection**: criar uma única instância e injetá-la nos dependentes — elimina a necessidade do padrão singleton por completo.
- **Enum type**: aproveita o singleton do Java por baixo, thread-safe por design.

**Regra**: Prefira dependency injection a singletons — crie uma instância em um ponto central e injete nos serviços que precisam dela.

> 💡 Nota: Se o código acessa o singleton uma vez e armazena a referência em variável local, as chamadas subsequentes não precisam de `getInstance()` — isso reduz contention no caso sincronizado.

---

## 4 Microservices vs. Monolith — Tradeoffs de Arquitetura

### 4.1 Vantagens de Microservices

**Escalabilidade horizontal**: adicionar instâncias do serviço aumenta throughput em ~N vezes. Monolitos têm limite de scaling vertical (CPU/RAM da máquina).

**Velocidade de desenvolvimento**: equipes independentes evoluem seus serviços sem conflitos de codebase, com tecnologias próprias e deploys independentes.

**Deploy de menor risco**: deploys menores e mais frequentes contêm menos features, são mais fáceis de debugar em caso de bug.

**Regra**: Prefira frequent small releases a large infrequent deploys para reduzir o risco por release.

### 4.2 Complexidades de Microservices

**Service registry obrigatório**: cada microserviço precisa de um cliente de registro que se registra e desregistra automaticamente. Um load balancer deve consultar o registry para rotear tráfego.

**Request tracing necessário**: erros provenientes da integração entre microserviços exigem distributed tracing para rastrear o fluxo entre serviços.

> ⚠ Evite: migrar para microservices sem considerar o custo de infraestrutura — service registry, load balancer, distributed tracing e health checks são requisitos, não opcionais.

### 4.3 Quando escolher Monolito

**Regra**: Se a equipe é pequena e os requisitos de escalabilidade são baixos, prefira arquitetura monolítica — o custo operacional de microservices não se justifica.

> 💡 Nota: Arquiteturas reais são frequentemente híbridas — parte monolito (legacy), parte microservices (novos domínios). A análise de tradeoffs se aplica a qualquer ponto do espectro.

### 4.4 Framework de decisão arquitetural

Para cada escolha de design:
1. Liste prós e contras de cada opção
2. Adicione contexto (tamanho de equipe, SLA, tempo de entrega, requisitos de escala)
3. Responda: qual design é melhor **neste contexto específico**?

**Regra**: Nunca avalie um padrão de arquitetura em abstrato — o contexto determina se ele é adequado ou não.

---

## 5 Compartilhamento de Código — Biblioteca vs. Microserviço vs. Duplicação

### 5.1 Duplicação entre codebases

Quando dois times desenvolvem de forma independente, duplicar código elimina sincronização entre eles. Pela Lei de Amdahl adaptada a times, quanto menor a fração de trabalho que exige sincronização, maior o ganho de velocidade ao adicionar pessoas ao projeto.

**Regra**: Antes de eliminar duplicação entre times independentes, avalie o custo de sincronização que a centralização exigirá — em certos contextos, duplicar preserva autonomia de entrega.

> ⚠ Evite: assumir que duplicação entre codebases independentes é sempre ruim — bug fixes não propagados são um custo real, mas perda de autonomia de time pode ser um custo maior.

### 5.2 Biblioteca compartilhada

Extrair código comum para uma biblioteca centraliza correções de bugs e garante consistência, mas cria uma nova entidade com ciclo de vida próprio (processo de deploy, coding practices, documentação).

**Tradeoffs**:
- Custo fixo de criação amortizado em bibliotecas subsequentes — a segunda biblioteca custa muito menos do que a primeira.
- Requer a mesma stack tecnológica em todos os consumidores.
- Dependências transitivas criam conflitos de versão (problema do diamante): se a biblioteca depende de Guava 27 e o cliente também usa Guava 28 via outra lib, o build tool pode escolher a versão errada, causando `MethodNotFoundError`.

**Regra**: Minimize dependências diretas de uma biblioteca compartilhada — cada dependência propagada a todos os consumidores aumenta o risco de conflito transitivo.

**Regra**: Mantenha documentação separada dos testes — testes cobrem comportamentos, mas não substituem guias de uso e exemplos didáticos.

> ⚠ Evite: dependências desnecessárias em bibliotecas internas — cada dependência se propaga para todos os clientes, dificultando adoção.

### 5.3 Extração para microserviço

Um microserviço expõe a funcionalidade compartilhada via HTTP API, removendo o acoplamento de dependências do cliente. O cliente não importa código — apenas faz chamadas HTTP usando o HTTP client já presente no sistema, evitando o problema de dependências transitivas.

**Tradeoffs operacionais**:

| Aspecto | Detalhe |
|---|---|
| Deploy e operação | Requer processo de deploy, monitoramento, alerting e health checks — custo inicial alto, amortizado com o tempo. |
| Versioning | Métricas por endpoint permitem identificar e deprecar rotas sem uso; mais rastreável do que versioning de library. |
| Escalabilidade | Processamento e consumo de recursos movidos para o microserviço; o cliente escala independentemente. |
| Latência | Cada chamada adiciona o P99 do microserviço à latência observada pelo usuário (latência total = N + M ms). |
| Cascading failures | Indisponibilidade do downstream requer retry com exponential backoff e circuit breaker. |

**Regra**: Implemente retry com exponential backoff para chamadas a microserviços downstream — ex: 1º retry após 1s, 2º após 10s, 3º após 30s.

**Regra**: Use circuit breaker para proteger o sistema quando o serviço downstream está indisponível de forma não-temporária.

**Regra**: Se o P99 do microserviço exceder o SLA do cliente, considere biblioteca (acoplamento em código) ou cache dos resultados como alternativa.

> ⚠ Evite: extrair funcionalidade simples e sem muitas dependências para um microserviço — o custo operacional raramente compensa; prefira biblioteca nesses casos.

### 5.4 Framework de decisão para compartilhamento de código

| Critério | Duplicação | Biblioteca | Microserviço |
|---|---|---|---|
| Autonomia dos times | Alta | Média | Alta |
| Propagação de bug fixes | Não | Sim | Sim |
| Acoplamento de dependências | Nenhum | Alto | Baixo |
| Custo operacional | Baixo | Médio | Alto |
| Evolução independente | Sim | Limitada | Sim |

**Regra**: Se a lógica tem um domínio de negócio próprio e alta complexidade, prefira microserviço. Se a lógica é simples com poucas dependências, prefira biblioteca. Se os times precisam evoluir em direções divergentes, aceite a duplicação.

---

## 6 Herança, Composição e Duplicação Intencional

### 6.1 Template Method para compartilhar lógica comum

O padrão Template Method (via herança) implementa o fluxo principal na classe base e delega apenas a parte variável às subclasses via método abstrato:

```java
public abstract class BaseTraceRequestHandler<T extends TraceRequest> {
  public void processRequest(T trace) {
    if (!processed && !trace.isTraceEnabled()) return;
    if (buffer.size() < bufferSize) buffer.add(createPayload(trace));
    if (buffer.size() == bufferSize) processed = true;
  }
  protected abstract String createPayload(T trace); // subclasse implementa
}
```

**Regra**: Use Template Method quando a estrutura do algoritmo é idêntica entre variantes e apenas um passo concreto difere entre subclasses.

### 6.2 Tight coupling introduzido pela herança

Quando um novo requisito muda o comportamento de apenas uma subclasse (ex: buffer ilimitado para `GraphTraceHandler`), o método compartilhado na base não pode ser alterado sem afetar as demais subclasses. A tentação de usar `instanceof` na base para tratar o caso especial deve ser evitada:

```java
// Antipadrão: parent conhece detalhes de implementação dos filhos
if (trace instanceof GraphTrace) {
  buffer.add(createPayload(trace));
}
```

> ⚠ Evite: usar `instanceof` na classe base para tratar casos específicos de subclasses — vaza conhecimento da subclasse para o pai, quebrando encapsulamento e anulando o benefício da herança.

**Regra**: Se a herança impede evolução independente de subclasses, considere desfazer a abstração (aceitar duplicação) ou migrar para composição.

### 6.3 Composição como alternativa

Separar responsabilidades em interfaces independentes (ex: `PayloadTransformer` + `Buffer`) e injetá-las via construtor (DI) permite combinar qualquer transformação com qualquer estratégia de buffer sem hierarquia de herança.

**Tradeoffs composição vs. herança**:
- Composição: maior flexibilidade para variar dimensões independentes; mais abstrações para o leitor entender.
- Herança: menos abstrações, mas acoplamento implícito entre subclasses via parent.

**Regra**: Prefira composição quando os requisitos das subclasses tendem a variar de forma independente em múltiplas dimensões.

### 6.4 Duplicação incidental vs. inherente

**Duplicação inherente**: dois componentes resolvem o mesmo problema e devem evoluir juntos — abstrair é correto.

**Duplicação incidental**: dois componentes parecem iguais hoje, mas podem evoluir em direções distintas amanhã — abstrair cria acoplamento desnecessário.

**Regra**: Antes de criar abstração para eliminar duplicação, verifique se os dois componentes realmente resolvem o mesmo problema de negócio — se podem evoluir de forma distinta, mantenha-os independentes.

**Regra**: Deixe abstrações emergirem da prática — implemente componentes independentes, observe padrões comuns e só então abstraia. É mais fácil fundir dois conceitos similares do que separar uma abstração prematura.

> ⚠ Evite: criar abstração compartilhada e adaptar todos os clientes a ela só porque o código parece idêntico — similaridade visual não implica equivalência de domínio nem de evolução futura.

---

## 7 Tratamento de Exceções

### 7.1 Hierarquia e granularidade de captura

Em Java, todo exception é `Throwable → Error` (não capturar) | `Exception → Checked | Unchecked`. Stack trace em `Throwable` é essencial para diagnóstico.

**Regra**: Use catch granular por tipo quando o comportamento de tratamento difere por tipo. Use multi-catch (`IOException | InterruptedException`) para reduzir duplicação sem perder informação de tipo.

**Regra**: Capture somente as exceções que o método chamado declara na assinatura — não capture `Exception` genérico quando apenas exceções específicas são esperadas.

> ⚠ Evite: catch-all em `Exception` ou `Throwable` desnecessariamente — você captura `RuntimeException` não declaradas que deveriam propagar para o nível correto da call stack.

### 7.2 API pública — checked vs. unchecked

**Checked**: força o caller a tomar decisão explícita em tempo de compilação — contrato claro, sem surpresas em produção.

**Unchecked**: pode ser declarado na assinatura para documentar pré-condições (`IllegalArgumentException`, `IllegalStateException`) mesmo sem obrigação de captura.

**Regra**: Em APIs públicas, declare checked exceptions nos métodos expostos — o caller conhece o contrato sem ler a implementação.

**Regra**: Para converter checked em unchecked, preserve sempre a causa original.

```java
public void wrapIntoUnchecked() {
  try {
    check();
  } catch (RuntimeException e) {
    throw e;                       // não re-wrap
  } catch (Exception e) {
    throw new RuntimeException(e); // preserva a causa
  }
}
```

> ⚠ Evite: converter checked exceptions para unchecked sistematicamente como solução padrão — esconde o contrato e torna o sistema menos fault-tolerant.

### 7.3 Antipadrões de exception handling

**Swallowing** (empty catch ou apenas `e.printStackTrace()`): exceção capturada mas informação perdida, gerando falhas silenciosas.

**Resource leak**: `close()` após código que pode lançar exceção — nunca executado se a exceção ocorrer. Use `try-with-resources` (AutoCloseable) ou `finally`.

```java
// Correto: try-with-resources
try (CloseableHttpClient client = HttpClients.createDefault()) {
  processRequests(client);
} catch (IOException e) {
  logger.error("Problem", e);
}
```

**Exceções como controle de fluxo**: lançar exceção para bifurcar lógica de negócio (em vez de sinalizar condições excepcionais) gera código complexo e degrada performance. Prefira `Try` ou `Either` nesses casos.

**Regra**: Implemente `AutoCloseable` em objetos que consomem recursos do sistema — permite uso com `try-with-resources`.

> ⚠ Evite: `e.printStackTrace()` em catch blocks — use `logger.error("context", e)` para preservar stack trace e contexto no log de forma rastreável.

### 7.4 Exceções de bibliotecas de terceiros

Expor o tipo de exceção de uma lib no API público cria tight coupling: trocar a lib implica breaking change na assinatura do API.

**Regra**: Crie uma domain-specific exception que encapsula a exceção da lib usando factory methods com private constructor.

```java
public class PersonCatalogException extends Exception {
  private PersonCatalogException(String message, Throwable cause) {
    super(message, cause);
  }
  public static PersonCatalogException getPersonException(String name, Throwable t) {
    return new PersonCatalogException("Problem getting person: " + name, t);
  }
}
```

**Regra**: Passe sempre a `Throwable` original como `cause` da domain exception — stack trace e tipo da causa ficam acessíveis via `getCause()`.

> ⚠ Evite: `throws ThirdPartyException` em interfaces públicas — torna o caller dependente da lib interna; trocar a lib quebra compatibilidade.

### 7.5 Exceções em ambientes multithread e async

**`submit()` + `Future.get()`**: o executor retorna `Future`; chamar `.get()` bloqueia até o resultado ou propaga `ExecutionException` em caso de falha — use este padrão quando o resultado importa.

**`execute()` fire-and-forget**: não retorna `Future`; exceção no worker thread descartada silenciosamente. Registre `UncaughtExceptionHandler` por thread.

```java
ThreadFactory factory = r -> {
  Thread thread = new Thread(r);
  thread.setUncaughtExceptionHandler(
      (t, e) -> logger.error("Exception in thread: " + t, e));
  return thread;
};
ExecutorService pool = Executors.newSingleThreadExecutor(factory);
```

**`CompletableFuture`**: ao fazer bridge de código sync que lança checked exception para async, use `completeExceptionally()` em vez de rethrow — evita stack traces aninhados e não mata o thread.

```java
CompletableFuture<Integer> result = new CompletableFuture<>();
CompletableFuture.runAsync(() -> {
  try {
    result.complete(externalCall());
  } catch (IOException e) {
    result.completeExceptionally(e);
  }
});
return result;
```

**Regra**: Com `execute()` e thread pool de tamanho fixo, registre `UncaughtExceptionHandler` — threads que falham sem handler não são recriadas, esvaziando o pool.

> ⚠ Evite: rethrow como `RuntimeException` dentro de `supplyAsync()` — gera stack traces aninhados `CompletionException → RuntimeException → IOException`; use `completeExceptionally()`.

### 7.6 Abordagem funcional com Try (Vavr)

`Try<T>` encapsula success (valor) ou failure (exceção), permitindo encadear transformações sem try-catch blocks misturados à lógica de negócio.

```java
Try<HttpResponse> response = Try.of(() -> client.execute(httpGet));
return response
    .mapTry(this::extractStringBody)  // mapTry: action que declara checked exception
    .mapTry(this::toEntity)
    .map(this::extractUserId)         // map: action sem checked exception
    .onFailure(ex -> logger.error("Failed", ex))
    .getOrElse("DEFAULT_ID");
```

| Método | Uso |
|---|---|
| `map()` | transforma o valor; lambda não pode lançar checked exception |
| `mapTry()` | transforma com method que declara checked exception |
| `getOrElse(default)` | extrai valor ou retorna default em falha |
| `getOrElseThrow()` | relança a exceção (perde benefícios do Try) |
| `toOption()` | converte para `Option<T>` sem incluir a causa |

**Regra**: Retorne `Try<T>` do método em vez de usar `getOrElse()` quando não há default razoável — deixe o caller decidir o tratamento.

> ⚠ Evite: misturar `Try` com código que lança unchecked exceptions não declaradas — você precisará envolver quase toda chamada em `Try`, tornando o código ilegível. O padrão funcional funciona melhor com APIs que declaram exceções explicitamente.

### 7.7 Performance de exception handling

Resultados JMH (50.000 iterações por operação):

| Estratégia | Tempo médio | Fator vs throw-catch |
|---|---|---|
| Baseline (sem exception) | < 1 ms | — |
| throw-catch | ~100 ms | 1× |
| Try monad | ~100 ms | 1× (idêntico) |
| getStackTrace() | ~750 ms | ~7.5× |
| logger.error (stack trace + appender) | ~3.000 ms | ~30× |

**Regra**: Se você vai relançar uma exceção para um nível superior, não a logue no nível intermediário — ela será logada definitivamente no nível que a capturar.

> ⚠ Evite: usar esses benchmarks como justificativa para evitar exceções onde são necessárias — em sistemas sem requisitos low-latency críticos, o impacto é negligenciável. O custo real está no log, não no throw-catch.

---

## 8 Extensibilidade e Flexibilidade de APIs

### 8.1 Design evolutivo: comece simples

Ao projetar um componente compartilhado, inicie com a implementação mais direta possível, sem pontos de extensão. Adicione extensibilidade incrementalmente baseado em input real dos clientes, não em antecipação especulativa.

**Regra**: Prefira design simples sem extensibilidade a design super genérico especulativo — remover features de uma API pública é uma breaking change; adicionar depois é mais seguro.

> ⚠ Evite: prever todos os casos de uso possíveis antes de ter clientes reais — o risco é introduzir múltiplas camadas de abstração sem benefício prático, dificultando manutenção.

### 8.2 Abstraindo dependências de terceiros

Quando um componente usa uma lib de terceiros diretamente, o cliente fica obrigado a usar a mesma lib. Criar uma interface interna desacopla o componente da implementação específica:

```java
public interface MetricsProvider {
  void incrementSuccess();
  void incrementFailure();
  void incrementRetry();
}
```

Abstrair reduz coupling no componente, mas move complexidade para os clientes — cada cliente precisa implementar a interface para a lib que usa.

**Regra**: Ao abstrair uma lib de terceiro, forneça uma implementação padrão da interface — clientes que usam a lib mais comum usam o default; os que precisam de outra lib implementam a interface.

> ⚠ Evite: expor abstrações sem implementação padrão quando a maioria dos clientes usa a mesma lib — você outsourcia complexidade para os clientes sem benefício real para eles, podendo levá-los a preferir outro componente.

### 8.3 Hooks API

Hooks permitem ao cliente injetar código entre fases do lifecycle do componente, sem que o componente precise prever o caso de uso específico:

```java
public interface HttpRequestHook {
  void executeOnRequest(HttpRequestBase httpRequest);
}

// Injeção via construtor — lista de hooks
public HttpClientExecution(MetricRegistry metricRegistry,
    int maxNumberOfRetries, CloseableHttpClient client,
    List<HttpRequestHook> httpRequestHooks) { ... }
```

**Guarda contra exceções imprevistas**: hooks podem lançar unchecked exceptions — sempre envolva a chamada em try-catch para não interromper o lifecycle principal:

```java
for (HttpRequestHook hook : httpRequestHooks) {
  try {
    hook.executeOnRequest(httpPost);
  } catch (Exception ex) {
    logger.error("Hook threw exception — validate hook logic", ex);
  }
}
```

**Impacto de performance**: hooks síncronos que bloqueiam (I/O, rede) aumentam diretamente a latência do componente. Solução: submeter cada hook a um thread pool dedicado e aguardar todos antes de avançar para a próxima fase (invokeAll):

```java
private final ExecutorService executorService = Executors.newFixedThreadPool(8);

List<Callable<Object>> tasks = new ArrayList<>();
for (HttpRequestHook hook : httpRequestHooks) {
  tasks.add(Executors.callable(() -> {
    try { hook.executeOnRequest(httpPost); }
    catch (Exception ex) { logger.error("Hook error", ex); }
  }));
}
List<Future<Object>> responses = executorService.invokeAll(tasks);
for (Future<Object> r : responses) { r.get(); } // happens-before com próxima fase
```

**Regra**: Ao usar hooks API, sempre guarde contra exceções do código do cliente com try-catch — se a exceção não é fatal para o componente, logue e continue o processamento.

**Regra**: Ao paralelizar hooks em thread pool, ainda existe um happens-before entre a conclusão de todos os hooks e a próxima fase do lifecycle — a latência adicionada é pelo menos igual ao hook mais lento.

> ⚠ Evite: passar objetos de estado mutável e interno (ex: HttpClient configurado para um SLA específico) aos hooks — o código do cliente pode alterar o estado interno, consumindo recursos ou causando falhas imprevisíveis no componente.

### 8.4 Listener API (Observer Pattern)

O listener API (padrão Observer) emite eventos de forma assíncrona — diferente do hooks API, o componente não aguarda a conclusão dos listeners antes de avançar para a próxima fase:

```java
public interface OnRetryListener {
  void onRetry(List<RetryStatus> retryStatus);
}

public class HttpClientExecution {
  private final List<OnRetryListener> retryListeners = new ArrayList<>();
  public void registerOnRetryListener(OnRetryListener listener) {
    retryListeners.add(listener);
  }
}
```

Ao emitir eventos, propague estado via wrapper imutável — o cliente pode modificar uma referência mutável, corrompendo dados de outros listeners:

```java
// ImmutableList.copyOf: não cria cópia de conteúdo, mas lança UnsupportedOperationException
// em qualquer tentativa de modificação (fail-fast explícito)
retryListeners.forEach(l -> l.onRetry(ImmutableList.copyOf(retryStatuses)));
```

**Regra**: Ao propagar estado para listeners ou hooks, use wrapper imutável (`ImmutableList.copyOf()`, `Collections.unmodifiableList()`) — garante fail-fast explícito se o cliente tentar modificar o estado, em vez de falha silenciosa não-determinística.

**Regra**: Se o objeto propagado é imutável por design (campos `final`, value objects), não é necessário criar cópia defensiva — o consumo de memória é substancialmente menor do que copiar N vezes para N listeners.

> ⚠ Evite: propagar referências mutáveis de estado interno para código que você não controla — o cliente pode modificar o estado acidentalmente, introduzindo side effects no componente.

> ⚠ Evite: emitir eventos de alta frequência para N listeners sem considerar back pressure — se os listeners não conseguirem acompanhar o tráfego, podem bloquear ou causar uso excessivo de memória.

### 8.5 Framework: flexibilidade vs. complexidade

| Abordagem | Flexibilidade | Complexidade adicionada |
|---|---|---|
| Design simples (sem extensão) | Nenhuma | Nenhuma |
| Abstração de lib de terceiro sem default | Moderada | Moderada (cada cliente implementa interface) |
| Abstração com implementação default | Moderada | Baixa (apenas quem precisa de outra lib implementa) |
| Hooks API | Alta | Alta (guarda exceções, thread pool, happens-before) |
| Listener API | Alta | Alta (imutabilidade, back pressure, thread pool async) |

**Regra**: Quanto mais flexível a API, maior a complexidade — analise explicitamente este tradeoff antes de escolher a abordagem. Não escolha o máximo de flexibilidade especulativamente.

---

## 9 Otimização de Performance — Hot Path vs. Premature Optimization

### 9.1 Quando otimização prematura é um erro

Sem dados sobre SLA e tráfego esperado, qualquer otimização é "shoot in the dark" — você complica o código sem saber se o ganho existe.

Exemplo: `stream.filter().findAny()` vs `parallelStream()` para 10.000 contas — benchmark JMH mostra desempenho idêntico. A otimização adicionou complexidade sem benefício porque o N real não foi medido.

**Regra**: Não otimize sem dados. Toda otimização antes de medir o desempenho real é prematura e baseada em suposição.

> ⚠ Evite: transformar processamento sequencial em paralelo apenas porque "pode ser mais rápido" — meça primeiro com benchmarks que modelam o tráfego real.

### 9.2 Princípio de Pareto e identificação do hot path

**Pareto no software**: 80% do trabalho é feito por 20% do código. O hot path é a parte executada em quase todo request do usuário.

**Fórmula de impacto de performance**:

```
impacto = requests_por_segundo × p99_latência_ms
```

Exemplo real (word service):
- `word-of-the-day`: 1 rps × 360 ms = 360 → 0.3% do trabalho total
- `word-exists`: 20 rps × 5.000 ms = 100.000 → 99.7% do trabalho total

Conclusão: otimizar `word-of-the-day` (endpoint mais lento) teria impacto mínimo. O hot path é `word-exists`.

**Regra**: Use a fórmula `rps × p99` para priorizar o que otimizar — não use apenas a latência isolada, pois frequência é parte do impacto.

**Regra**: Após qualquer otimização, recalcule a distribuição de impacto. O hot path pode mudar após uma otimização significativa.

### 9.3 Configurando threads para SLA

Dado um SLA de `R` requests/s e latência média `L` ms, o número mínimo de threads necessário:

```
threads = R × (L / 1000)
```

Exemplo: SLA = 10.000 rps, latência média = 50 ms → threads = 10.000 × 0.05 = 500 threads.

Um thread com 50 ms de latência serve apenas `1000 / 50 = 20 rps`. Para 10.000 rps são necessários `10.000 / 20 = 500 threads`.

**Regra**: Configure o número de threads do performance test com base no SLA — um único thread nunca valida o SLA esperado.

### 9.4 Detecção de hot path com ferramentas

**Gatling** (black-box, Scala): simula tráfego real por endpoint e retorna p99 por cenário.

```scala
class WordsSimulation extends Simulation {
  val httpProtocol = http.baseUrl("http://localhost:8080/words")
  val validateScenario = scenario("word-exists")
    .exec(feed(csv("words.csv").random)
      .exec(http("word-exists").get("/word-exists?word=${word}").check(status is 200)))
  setUp(
    wordOfTheDayScenario.inject(constantUsersPerSec(1) during (1 minutes)),
    validateScenario.inject(constantUsersPerSec(20) during (1 minutes))
  ).protocols(httpProtocol)
}
```

**MetricsRegistry (Dropwizard)** (white-box): instrumenta fases internas com timers para identificar a subfase que consome mais tempo.

```java
Timer loadFile = metricRegistry.timer("loadFile");
try (Scanner scanner = loadFile.time(() -> new Scanner(filePath.toFile()))) {
    Timer scan = metricRegistry.timer("scan");
    return scan.time(() -> ...);
}
```

Acessar métricas: `GET /metrics?pretty=true` retorna count e percentis por timer.

**Regra**: Use benchmarks black-box (Gatling) para encontrar o hot path e white-box (MetricsRegistry) para identificar qual subfase interna é o gargalo.

### 9.5 Otimizações para o hot path — cache eager vs. lazy

Após detectar que `word-exists` fazia I/O em arquivo para cada request:

| Estratégia | Descrição | Tradeoff |
|---|---|---|
| Cache eager | Carrega todo o arquivo na inicialização | Usa memória sempre, startup mais lento |
| Cache lazy com eviction | Carrega on demand, evicta por tempo de acesso | Uso de memória proporcional ao tráfego real |

**Implementação com Guava LoadingCache** (cache lazy com eviction):

```java
LoadingCache<String, Boolean> wordExistsCache = CacheBuilder.newBuilder()
    .ticker(ticker)
    .expireAfterAccess(DEFAULT_EVICTION_TIME)   // eviction por tempo de acesso
    .recordStats()
    .build(new CacheLoader<String, Boolean>() {
        @Override
        public Boolean load(@Nullable String word) throws Exception {
            if (word == null) return false;
            return checkIfWordExists(word);     // carregado on demand
        }
    });
```

Resultado: p99 de 5.000 ms → 65 ms (~80× de melhora).

**Regra**: Injete o `ticker` no cache para testabilidade — permite avançar o tempo em testes sem `Thread.sleep()`.

> ⚠ Evite: cache sem eviction para dados que podem crescer indefinidamente — use eviction por tempo ou por tamanho para limitar pressão de memória.

### 9.6 Recálculo de impacto e ajuste dos benchmarks

Após otimização, recalcule a distribuição de impacto:

```
word-exists: 20 rps × 65 ms = 1.300
word-of-the-day: 1 rps × 360 ms = 360
word-of-the-day share: 360 / (1.300 + 360) ≈ 21%
```

O endpoint antes negligenciável agora representa 21% do trabalho — pode valer a pena otimizá-lo depois.

**Ajuste dos benchmarks para cache**: testes com 6 palavras não representam tráfego real de um cache. Use 100+ palavras para representar a distribuição de cache miss real.

**Regra**: Adapte o performance test ao comportamento da solução — um cache precisa de inputs diversificados para validar hit/miss ratio realista.

> 💡 Nota: Otimização não é prematura quando há dados de SLA e benchmarks que modelam o tráfego real — é análise fundamentada antes do deploy.

---

## 10 Simplicidade vs. Custo de Manutenção de APIs de Configuração

### 10.1 Exposição direta das settings da lib downstream

A ferramenta **batch service** passa o YAML de configuração diretamente para o `CloudServiceClientBuilder` — o caller fornece a seção `auth` no mesmo formato que a lib downstream espera.

```yaml
# batch-config.yaml (caller gerencia toda a estrutura)
auth:
  strategy: username-password
  username: user
  password: pass
batch:
  size: 100
```

**Vantagens**:
- Manutenção zero quando a lib adiciona uma nova setting — o raw YAML é passado diretamente
- Sem mapeamento adicional no código do batch service

**Desvantagens**:
- Caller fica acoplado ao formato interno da lib downstream
- Breaking changes na lib propagam diretamente para todos os callers

### 10.2 Abstração das settings da lib downstream

A ferramenta **streaming service** expõe todas as settings sob a seção `streaming` — o usuário não precisa conhecer a estrutura interna da lib downstream.

```yaml
# streaming-config.yaml (formato próprio, sem exposição da lib)
streaming:
  maxTimeMs: 500
  username: user
  password: pass
  connectionTimeout: 1000
```

O `StreamingServiceBuilder` faz o mapeamento programático:

```java
CloudServiceConfiguration cloudConfig = new CloudServiceConfiguration(
    new UsernamePasswordAuthStrategy(
        (String) streamingConfig.get("username"),
        (String) streamingConfig.get("password")),
    (Integer) streamingConfig.get("connectionTimeout"));
```

**Vantagens**: mudanças na lib downstream ficam encapsuladas; usuários não precisam alterar suas configs.

**Desvantagens**: cada nova setting da lib requer mudança de código no streaming service.

### 10.3 Quando mudança no downstream é um breaking change

Cenário: `username-password` strategy é depreciada — usa plain text, insegura. Nova strategy `username-password-hashed` exige password hasheado.

**Batch (exposição direta)**: todos os callers que usam `username-password` recebem `UnsupportedOperationException` ao atualizar a lib. Migração manual obrigatória para todos.

**Streaming (abstração)**: a migração é feita silenciosamente dentro do builder — os usuários da ferramenta não precisam alterar suas configs:

```java
// migração transparente dentro do StreamingServiceBuilder
CloudServiceConfiguration cloudConfig = new CloudServiceConfiguration(
    new UsernamePasswordHashedAuthStrategy(
        (String) streamingConfig.get("username"),
        toHash((String) streamingConfig.get("password"))));  // hash aplicado internamente
```

### 10.4 Framework de decisão

| Cenário | Abordagem recomendada |
|---|---|
| Lib estável e você controla seu ciclo de release | Exposição direta (manutenção zero) |
| Lib externa com breaking changes frequentes | Abstração (protege os callers) |
| N serviços consomem a mesma lib | Abstração (custo centralizado, N callers protegidos) |
| Lib com dezenas/centenas de settings | Exposição direta (mapear tudo é impraticável) |

**Regra**: Se você não controla o ciclo de releases da lib downstream e ela faz breaking changes, abstraia a configuração — o custo de manutenção é amortizado em N callers protegidos.

**Regra**: Se a lib é estável e os callers aceitam conhecer sua estrutura de configuração, passe o raw config diretamente — zero manutenção e zero código adicional.

> 💡 Nota: Decisões técnicas impactam UX. Expor internals de uma lib transfere o custo de migração para os usuários da sua ferramenta; abstrair transfere o custo para você.

---

## 11 Data e Hora — Tradeoffs de Design

### 11.1 Conceitos fundamentais

| Conceito | java.time | Noda Time (.NET) | Descrição |
|---|---|---|---|
| **Instant** | `Instant` | `Instant` | Ponto no tempo independente de fuso; armazenar "quando algo aconteceu" |
| **Duration** | `Duration` | `Duration` | Quantidade exata de tempo decorrido (sem ambiguidade de calendário) |
| **Epoch** | (Unix: 1970-01-01T00:00:00Z) | — | Ponto zero para representar instants como números |
| **LocalDate** | `LocalDate` | `LocalDate` | Data sem hora e sem fuso (ex: "data de entrega") |
| **LocalTime** | `LocalTime` | `LocalTime` | Hora sem data e sem fuso |
| **LocalDateTime** | `LocalDateTime` | `LocalDateTime` | Data + hora sem fuso |
| **Period** | `Period` | `Period` | Intervalo em unidades de calendário (anos, meses, dias) — ambíguo em edge cases |
| **ZonedDateTime** | `ZonedDateTime` | `ZonedDateTime` | Data + hora + IANA timezone |
| **ZoneId** | `ZoneId` | `DateTimeZone` | Timezone IANA (ex: `America/Los_Angeles`) |

Operações válidas:
```
Instant - Instant → Duration
Duration + Duration → Duration
Instant + Duration → Instant
Date + Period → Date   (mas pode haver ambiguidade)
```

> ⚠ Evite: usar `java.util.Date` e `java.util.Calendar` — cheios de armadilhas. Use `java.time` (Java 8+) ou Noda Time (.NET).

### 11.2 Timezone ≠ UTC offset

- **UTC offset**: valor fixo (ex: `-8h`) — não é timezone
- **Timezone (IANA)**: regra que mapeia instants a offsets, muda com DST e decisões políticas
- **Abreviações (PST, BST)**: ambíguas — BST pode ser British Summer Time ou British Standard Time. Use apenas para exibição, nunca para parsing

**Regra**: Use IANA time zone IDs (`ZoneId.of("America/Los_Angeles")`) — nunca use offsets fixos para representar zonas geográficas. Offsets não capturem mudanças de DST.

> ⚠ Evite: confiar em abreviações de timezone para parsing — parse ambíguo é um bug silencioso que aparece apenas algumas horas por ano.

### 11.3 Testabilidade: injetar Clock

Código que chama `Instant.now()` ou `LocalDate.now()` diretamente é impossível de testar deterministicamente.

```java
// ruim — acoplado ao relógio do sistema:
public boolean isWithinOneMinuteOfTarget(Instant target) {
    return Duration.between(Instant.now(), target).abs().toMinutes() < 1;
}

// bom — Clock injetável:
public OneMinuteTarget(@Nonnull Clock clock, @Nonnull Instant target) {
    this.clock = clock;
    ...
}
public boolean isWithinOneMinuteOfTarget() {
    Instant now = clock.instant();
    ...
}
```

Em testes, use `Clock.fixed(someInstant, ZoneOffset.UTC)` para controlar o tempo:

```java
@ParameterizedTest
@ValueSource(ints = {-61, 61})
void outsideTargetInterval(int secondsFromTarget) {
    Instant target = Instant.ofEpochSecond(10000);
    Clock clock = Clock.fixed(target.plusSeconds(secondsFromTarget), ZoneOffset.UTC);
    OneMinuteTarget subject = new OneMinuteTarget(clock, target);
    assertFalse(subject.isWithinOneMinuteOfTarget());
}
```

**Regra**: Injete `Clock` (java.time) em qualquer componente que dependa do tempo atual — permite testes paramétricos precisos sem `Thread.sleep()`.

### 11.4 Product requirements e scoping

Antes de implementar qualquer lógica de data/hora, defina com o product owner:

1. **Qual conceito** está sendo armazenado? (Instant vs LocalDate vs ZonedDateTime)
2. **Qual timezone** é relevante? (do usuário, da entrega, do servidor? — nunca do servidor)
3. **Como aritmética de calendário** é resolvida em edge cases? (ex: "3 meses após 31 de outubro" = ?)

Exemplo de requirement bem especificado:
> "O cliente pode retornar itens se a data atual no timezone do endereço de entrega não for posterior à data de envio + 3 meses. Se mês+3 transborda, usa o primeiro dia do mês seguinte (ex: 31 jan + 3 meses = 1 mai)."

**Regra**: Especifique o timezone e a aritmética de calendário explicitamente nas regras de negócio — ambiguidade em requirements gera bugs que aparecem poucos dias por ano.

> ⚠ Evite: usar o timezone do servidor como padrão — o sistema não deve se comportar diferente dependendo de onde a máquina está hospedada.

### 11.5 Representação textual

| Audiência | Formato recomendado |
|---|---|
| Transmissão/armazenamento entre sistemas | ISO-8601 (`2020-06-07T15:54:23Z`) |
| Exibição ao usuário | Locale-aware formatting da biblioteca |
| Logs/diagnóstico | ISO-8601 com timezone explícito |

**ISO-8601 recomendações**:
- Use separadores de data (`-`) e hora (`:`) para legibilidade
- Use `T` entre data e hora quando o contexto contiver múltiplos valores
- Use `.` (não `,`) como separador de frações de segundo para compatibilidade
- Prefira UTC (`Z`) para transmissão

**Regra**: Para log e transmissão, use sempre ISO-8601 com timezone explícito — evita ambiguidade de parse em diferentes locales.

> ⚠ Evite: `new Date().toString()` — o resultado depende do locale e timezone da JVM, tornando o log inconsistente entre ambientes.

### 11.6 Corner cases de calendário e fusos

**Horário de verão (DST)**:
- **Skipped time**: ao avançar o relógio, horários nessa faixa não existem (ex: 2:30 AM durante spring-forward pode não existir)
- **Ambiguous time**: ao atrasar o relógio, o mesmo horário ocorre duas vezes (ex: 1:30 AM ocorre duas vezes no fall-back)

**Regra**: Defina explicitamente como tratar horários skipped ou ambíguos — `ZonedDateTime.ofStrict()` lança exceção em vez de resolver silenciosamente.

**Aritmética de leap year**:
- "Adicionar 18 anos a 29/fev/2004" → resultado depende da biblioteca e da direção da operação
- Teste explicitamente com datas de Fevereiro 29 + período que resulta em mês sem esse dia

**Mudanças de regras de timezone**:
- Governos mudam regras de DST (ex: Energy Policy Act 2005 nos EUA mudou datas em 2007)
- Dados armazenados como instants UTC são estáveis, mas perdem o timezone local original do usuário

### 11.7 Source-of-truth vs. derived data

Ao armazenar dados de data/hora:

| Tipo | O que armazenar | Exemplo |
|---|---|---|
| Source-of-truth | O que o usuário informou (`LocalDate` + `ZoneId`) | "Reunião em Paris às 9h" |
| Derived data | Instant UTC calculado da source-of-truth | `2023-12-01T08:00:00Z` |

**Por que separar**: se as regras de timezone mudarem, você pode recalcular o derived data a partir da source-of-truth. Se armazenar apenas o Instant UTC, a informação original do usuário é perdida.

**Regra**: Armazene o que o usuário informou como source-of-truth. Derive instants UTC para sorting e queries. Recalcule derivados quando timezone data mudar.

> 💡 Nota: Versione os dados de timezone usados na derivação (`2020a`, `2020b`) para rastrear quando recalcular.

---

## 12 Data Locality e Processamento Big Data

### 12.1 Mover computação para os dados

**Problema**: enviar dados para o código (abordagem padrão) = I/O bound. Para 100 GB de dados, a maior parte do tempo é transferência de rede.

**Data locality**: serializar a função de processamento e enviá-la para o nó onde os dados já estão. O nó executa localmente, retorna apenas o resultado (ex: um número).

```
dados → processamento local → resultado pequeno → rede
```

vs.

```
dados → rede → processamento → resultado
```

**Regra**: Em big data, o bottleneck é I/O de rede/disco. Mova o processamento para os dados em vez de mover os dados para o processamento.

**Tradeoff**: data locality adiciona complexidade (serialização da função, processo dedicado no nó de dados), mas é necessária quando os dados não cabem em um único nó.

### 12.2 Particionamento temporal (offline)

Dados de big data offline devem ser particionados por data para habilitar data locality nas queries temporais:

```
/data/year=2020/month=01/day=15/
```

**Benefícios**:
- Query para um dia específico: acessa uma única partição
- Query para um mês: itera apenas as partições do mês
- Sem esse particionamento: scan completo de todos os dados para qualquer query

**Regra**: Defina granularidade de partição conforme o maior conjunto de dados que cabe em um nó. Se um dia não cabe, particione por hora. Se um ano é suficiente, use apenas year.

> ⚠ Evite: particionamento muito grosseiro (ex: só por ano) — impossibilita queries eficientes por dia e cria partições grandes demais para particionar em múltiplos nós.

### 12.3 Hash partitioning e sharding

Para distribuir dados por `user_id` em N nós:

```
node_id = hash(user_id) % N
```

**Garantia**: todos os eventos do mesmo `user_id` ficam no mesmo nó → data locality para operações por usuário.

**Problema**: ao adicionar um nó (N → N+1), a maioria dos assignments muda:
- Para N=2: IDs {1,3,5,7,9} → nó 1; IDs {2,4,6,8,10} → nó 0
- Para N=3: IDs {3,6,9} → nó 0; IDs {1,4,7,10} → nó 1; IDs {2,5,8} → nó 2
- Apenas IDs {3,6,9} mantiveram o mesmo nó — ~70% dos dados precisam ser migrados

**Solução**: Consistent Hashing — ao adicionar um nó, apenas os dados do nó adjacente precisam ser redistribuídos (~1/N dos dados).

**Regra**: Use consistent hashing em sistemas que precisam escalar elasticamente — naive modulo hashing exige migração massiva de dados ao remover/adicionar nós.

### 12.4 Narrow vs. wide transformation e data shuffling

| Tipo | Descrição | Custo de rede |
|---|---|---|
| **Narrow** | Operação local dentro da partição (filter, map) | Zero |
| **Wide** | Requer dados de múltiplas partições (join, groupBy cross-partition) | Alto — data shuffling |

**Data shuffling**: transferência de dados entre nós para agrupar dados do mesmo partition key no mesmo nó para o reduce.

**Regra**: Minimize wide transformations — cada shuffle adiciona latência de rede proporcional ao volume de dados movido.

> 💡 Nota: Frameworks como Spark otimizam automaticamente o query plan, mas conhecer se sua operação é narrow ou wide ajuda a estruturar o código para reduzir shuffles.

### 12.5 Broadcast join

Quando um dos datasets é significativamente menor que o outro:

1. O dataset **pequeno** é **broadcast** (enviado) para todos os nós que contêm o dataset grande
2. O join é executado localmente em cada nó (data locality do dataset grande)
3. Nenhum shuffle do dataset grande é necessário

**Condição**: o dataset pequeno deve caber na memória de cada nó.

**Spark** (executa broadcast automaticamente se `spark.sql.autoBroadcastJoinThreshold` for excedido, ou explicitamente com `broadcast()`):

```scala
// Spark infere broadcast ou pode ser forçado:
// Analisar o physical plan confirma BroadcastHashJoin vs SortMergeJoin
userData.joinWith(clicks, userData("userId") === clicks("userId"), "inner")
// Physical Plan resultante com broadcast: *BroadcastHashJoin
```

**Regra**: Se um dataset cabe em memória e o outro é grande, use broadcast join — elimina o shuffle do dataset grande, reduzindo latência dramaticamente.

### 12.6 Disk vs. Memory: Hadoop vs. Spark

| Abordagem | I/O por stage | Overhead de disco |
|---|---|---|
| Hadoop (HDFS) | Cada stage lê e escreve disco | 80× mais lento que RAM (HDD), 4× (SSD) |
| Spark (in-memory) | Primeira e última leituras em disco; intermediários em RAM | 2 acessos a disco máximo |

**Preço de armazenamento** (aproximado):
- HDD: $0.05/GB
- SSD: $0.10/GB (~100% mais caro)
- RAM: muito mais caro — use apenas para dados ativos

**Regra**: Para pipelines big data com múltiplos estágios de transformação, prefira processamento em memória (Spark) — o ganho de 4–80× de velocidade justifica o custo em RAM para dados ativos.

> 💡 Nota: Hadoop ainda é adequado para processamento muito esporádico de dados históricos onde custo de armazenamento em disco supera custo de tempo de processamento.

---

## 13 Bibliotecas de Terceiro — Tradeoffs e Armadilhas

### 13.1 Defaults de bibliotecas: assuma responsabilidade total

Bibliotecas geralmente têm defaults convenientes para desenvolvimento, mas perigosos em produção. Exemplo: **OkHttp** sem timeout configurado tem timeout infinito por padrão.

**Cenário de problema**: SLA do serviço = 100 ms. Thread aguarda request upstream por 5.000 ms (default OkHttp). Thread não serve outros requests enquanto espera → degradação de throughput generalizada em cascata.

**Solução**:

```java
OkHttpClient client = new OkHttpClient.Builder()
    .readTimeout(100, TimeUnit.MILLISECONDS)    // alinhado ao SLA
    .connectTimeout(100, TimeUnit.MILLISECONDS)
    .build();
```

**Regra**: Ao importar qualquer biblioteca, leia sua documentação de configuração — nunca assuma que o default é seguro para produção.

**Regra**: Em arquiteturas de microservices, o timeout de um HTTP client deve ser menor que o SLA do serviço que o usa — evita que um serviço lento cause cascading failure no caller.

> ⚠ Evite: "convention over configuration" em produção — convenções reduzem tempo de prototipagem mas ocultam problemas que só se manifestam sob tráfego real.

### 13.2 Modelo de concorrência: blocking vs. async

Código em contexto event-loop ou async (ex: Reactor, Vert.x) não pode chamar código blocking sem dedicar um thread pool separado para isso.

**Blocking → Async** (wrapper via ThreadPoolExecutor):

```java
public WrapIntoAsync(EntityService entityService) {
    this.entityService = entityService;
    executor = new ThreadPoolExecutor(1, 10, 100, TimeUnit.SECONDS,
                                      new LinkedBlockingDeque<>(100));
}
public CompletableFuture<Entity> loadAsync(String id) {
    return CompletableFuture.supplyAsync(() -> entityService.load(id), executor);
}
```

**Async → Blocking** (para código blocking que depende de lib async):

```java
Entity load() throws InterruptedException, ExecutionException, TimeoutException {
    return entityServiceAsync.load().get(100, TimeUnit.MILLISECONDS);  // timeout explícito
}
```

**Regra**: Prefira a versão async de uma biblioteca quando disponível — mesmo em código blocking hoje, migrar para async no futuro é mais fácil do que o contrário.

**Regra**: Ao envolver biblioteca blocking em código async, dimensione o thread pool com base no tráfego esperado — threads bloqueados consomem recursos mesmo sem trabalho útil.

### 13.3 Testabilidade de bibliotecas externas

**Virtual time**: bibliotecas de processamento reativo (Reactor) e de cache (Guava) permitem controlar o tempo em testes sem `Thread.sleep()`.

**Reactor TestScheduler**:
```java
// avança o tempo virtualmente — sem sleep real
testScheduler.advanceTimeBy(10, TimeUnit.SECONDS);
```

**Guava FakeTicker** (para LoadingCache):

```java
FakeTicker fakeTicker = new FakeTicker();
LoadingCache<String, Boolean> cache = CacheBuilder.newBuilder()
    .ticker(fakeTicker)          // ticker injetável = testável
    .expireAfterAccess(Duration.ofMinutes(5))
    .build(...);

fakeTicker.advance(CacheComponent.DEFAULT_EVICTION_TIME);
// agora o cache expira sem esperar 5 minutos reais
```

**Regra**: Antes de adotar uma biblioteca, verifique se ela fornece mecanismo de virtual time / fake time — é sinal de qualidade e reduz drasticamente o tempo de execução dos testes.

**Regra**: Prefira bibliotecas que permitem injetar fakes (ticker, clock, provider) — código de terceiro que você não pode testar é código que você não pode confiar.

> ⚠ Evite: `Thread.sleep()` em unit tests como substituto de virtual time — aumenta o tempo da suite de forma linear e introduz flakiness em máquinas lentas.

### 13.4 Dependências transitivas e shading

Cada biblioteca importada traz suas próprias dependências (transitivas). Problema do diamante: seu código usa Guava 28, a lib A usa Guava 27 — o build tool escolhe uma versão e pode causar `MethodNotFoundError` em runtime.

**Shading**: a biblioteca reembute suas dependências com package prefix próprio, isolando-as do classpath do caller.

```
# sem shading:
com.fasterxml.jackson.databind.ObjectMapper  ← conflito com sua versão do Jackson

# com shading (lib prefixou suas dependências):
com.http.client.com.fasterxml.jackson.databind.ObjectMapper  ← isolado
```

**Tradeoffs**:
- Shading resolve o conflito, mas aumenta o tamanho do jar (cada lib duplica suas dependências)
- Shading é mais viável em libs com poucas dependências transitivas

**Regra**: Ao criar uma biblioteca compartilhada, minimize dependências transitivas — cada dependência propagada para todos os consumers aumenta risco de conflito.

**Regra**: Se você consome uma biblioteca com muitas dependências e não pode usar shading, use um BOM (Bill of Materials) ou `dependencyManagement` para controlar versões transitivas explicitamente.

### 13.5 Critérios de seleção e manutenção

Antes de adotar uma biblioteca de terceiro:

| Critério | Perguntas |
|---|---|
| **Estabilidade** | Tem release estável? Mantida ativamente? Commits recentes? |
| **Licença** | Compatível com uso comercial? GPL pode exigir open source do seu código |
| **Dependências** | Quantas transitivas? Algum conflito com sua stack? |
| **Testabilidade** | Tem virtual time, fakes, integration testing toolkit? |
| **Escalabilidade** | Suporta multi-node? Estado global que impede scaling horizontal? |
| **Segurança** | Histórico de CVEs? Mantida com updates de segurança frequentes? |

**Frameworks vs. bibliotecas**: frameworks (Spring) ditam a estrutura do seu código; bibliotecas servem ao seu código. Frameworks são mais difíceis de remover depois que a codebase cresceu.

**Regra**: Monitore CVEs de todas as dependências (cvedetails.com). Automatize upgrades com ferramentas como Dependabot — segurança é o critério mais urgente.

---

## 14 Consistência e Atomicidade em Sistemas Distribuídos

### 14.1 At-least-once delivery e idempotência

Toda chamada de rede pode falhar por razões arbitrárias: falha da aplicação alvo, partição de rede ou perda do pacote de resposta. Do ponto de vista do caller, um timeout não permite concluir se a operação foi executada ou não.

**At-least-once delivery**: quando o caller faz retry até obter sucesso, a operação será executada uma vez ou mais — nunca zero vezes, mas pode haver duplicatas.

**Idempotência**: uma operação é idempotente se produz o mesmo estado independentemente do número de invocações.

| Tipo | Idempotente? | Exemplo |
|---|---|---|
| GET (leitura) | Sim | `GET /user/123` |
| DELETE por ID | Sim | Deletar item já deletado é no-op |
| POST (produção de dados) | Geralmente não | Enviar e-mail, debitar conta |

**Enviando estado completo vs. delta**: em vez de enviar eventos incrementais ("adicionou 1 livro"), o producer pode enviar o estado completo do agregado ("carrinho = {livro A: qty 2}"). Isso torna os eventos inerentemente idempotentes — a reprocessagem sobrescreve com o mesmo estado.

**Problema de ordering em retries**: se o evento E1 falha e é re-enviado em T3, pode chegar depois do evento E2 enviado em T2. O consumer sobrescreve o estado mais recente com o estado mais antigo. Solução: particionar por `user_id` e garantir ordenação dentro da partição — filas como Apache Kafka e Pulsar oferecem essa garantia.

**Regra**: Projete eventos de produção com estado completo do agregado quando possível — torna o re-envio idempotente sem lógica de deduplicação complexa.

**Regra**: Particione eventos por chave de negócio (ex: `user_id`) e garanta ordenação dentro da partição — evita que retries criem estados inconsistentes por out-of-order delivery.

> ⚠ Evite: enviar apenas deltas ("adicionou N unidades") quando o sistema usa at-least-once delivery — duplicatas de deltas geram estado inconsistente no consumer.

### 14.2 CQRS: Command Query Responsibility Segregation

**CQRS** separa o modelo de escrita (commands) do modelo de leitura (queries), conectados via fila persistente:

```
CartService (write) → Kafka/Pulsar → [UserProfileService, RelationalAnalysisService] (read)
```

**Benefícios**:
- Producer e consumers desacoplados: o producer não precisa antecipar todos os usos futuros
- Cada consumer cria seu próprio modelo de leitura otimizado para seu caso de uso
- Times de consuming services trabalham de forma independente

**Custos e riscos**:
- Dados duplicados em N locais (um por consumer service)
- Muitas chamadas de rede — cada uma pode falhar (retries, at-least-once, partições de rede)
- Out-of-sync entre consumers se deduplicação não for implementada

**Regra**: Em arquiteturas CQRS, implemente deduplicação no consumer side — um evento não-idempotente enviado em duplicata para um consumer pode divergir o estado do sistema inteiro.

### 14.3 Implementação ingênua de deduplicação

O mail service implementa deduplicação salvando o ID de cada request processado:

```java
public class NaiveDeduplicationService {
  private final DbClient dbClient = new DbClient();
  public void executeIfNotDuplicate(String id, Runnable action) {
    boolean present = dbClient.find(id);      // Stage 1: busca
    if (!present) {
      action.run();                           // Stage 2: executa ação
      dbClient.save(id);                      // Stage 3: salva ID
    }
  }
}
```

**Problema de atomicidade**: a lógica tem 3 estágios separados — cada um pode falhar independentemente, criando estados intermediários inconsistentes.

**Cenário de falha**: stage 2 (action.run()) bloqueia por 20 s; o caller tem timeout de 10 s. O caller faz retry antes do ID ser salvo em stage 3. O segundo request não encontra o ID no banco → a ação é executada novamente → email duplicado.

> ⚠ Evite: implementar deduplicação com find-then-save em duas operações separadas — em qualquer contexto com concorrência ou múltiplos nós, há possibilidade de race condition.

### 14.4 Problemas de atomicidade em contexto distribuído

**Single-node context**: mesmo com um único nó, operações bloqueantes em stage 2 permitem que o retry chegue antes do save em stage 3, gerando duplicata.

**Multi-node context**: o load balancer direciona o retry para um nó diferente. Ambos os nós executam find → não encontram o ID → executam a ação. Depois, ambos tentam salvar o ID, mas a ação já foi executada duas vezes.

```
Request 1 → Load Balancer → Instância 1: find(id) = false → executa → salva id
Request 2 → Load Balancer → Instância 2: find(id) = false → executa → salva id
                                                    ↑ race condition ↑
```

A causa raiz: find + execute + save são 3 operações separadas e não atômicas. Qualquer interleaving entre elas pode quebrar a invariante de deduplicação.

**Regra**: Em sistemas distribuídos, toda lógica que lê, processa e escreve estado em etapas separadas é suscetível a race conditions — sempre analise o pior caso de interleaving.

### 14.5 Tornando a lógica atômica com upsert

A solução é reduzir os 3 estágios a 1 operação atômica no banco: **upsert** (insert if not exists, return outcome).

```java
// DbClient expõe:
public boolean findAndInsertIfNeeded(String id);
// retorna true se inseriu (não era duplicata), false se já existia

@Override
public boolean isDuplicate(String id) {
  boolean wasInserted = dbClient.findAndInsertIfNeeded(id);
  return !wasInserted;  // true = duplicata (já existia)
}
```

O upsert é executado atomicamente no banco — não há janela entre o check e o insert onde outra thread pode se intercalar.

**Limitação**: o upsert não executa a ação de negócio como parte da operação. Isso significa:
- Se o upsert marca como processado antes da ação, e a ação falha → o retry é descartado como duplicata → evento perdido
- Solução: usar transações ou transaction logs para rollback do ID em caso de falha

**Regra**: Use upsert (insert-if-absent atômico) para deduplicação em ambientes distribuídos — elimina a race condition entre check e insert.

**Regra**: Combine deduplicação atômica com mecanismos de verificação de corretude (transaction logs, rollback de ID em falha) — deduplicação resolve duplicatas, mas não garante que a ação foi executada com sucesso.

> 💡 Nota: A maioria dos bancos distribuídos (Cassandra, DynamoDB, Redis, PostgreSQL) oferece operações upsert ou conditional write que satisfazem esse requisito.

---

## 15 Semântica de Entrega em Sistemas Distribuídos

### 15.1 Arquitetura event-driven e pub-sub

**Problema da arquitetura request-response direta**: N producers conectados a M consumers criam N×M conexões. Falha de qualquer consumer propaga para todos os producers — tight coupling e single points of failure.

**Solução: pub-sub (publish-subscribe)**: um componente intermediário (fila/event queue) desacopla producers de consumers:

```
Frontend 1 ─┐
Frontend 2 ─┤→ Metrics pub-sub → [Dashboard, Analytics, On-Call]
Database   ─┘
```

**Benefícios da arquitetura event-driven**:
- Producer não precisa conhecer os consumers
- Falha de um consumer não impacta o producer
- A fila persiste eventos enquanto o consumer está offline — **fault tolerance por design**
- Consumers independentes podem escalar separadamente

**N filas independentes**: para evitar single point of failure da própria fila, use N sistemas de fila independentes (metrics pub-sub, logging pub-sub, events pub-sub). Cada um pode ser configurado com SLA e custo diferente.

**Regra**: Use pub-sub para desacoplar producers e consumers — a fila absorve falhas de consumers e picos de tráfego, fornecendo fault tolerance sem coordenação direta entre serviços.

> ⚠ Evite: conexão request-response síncrona quando o producer não precisa da resposta imediata — aumenta coupling, reduz fault tolerance e escalabilidade.

### 15.2 Apache Kafka: tópicos, partições, brokers

**Tópico**: estrutura append-only distribuída via particionamento. Cada tópico tem N partições.

**Offset**: identificador único de um registro dentro de uma partição. Monotonicamente crescente por partição.

**Partition key (chave)**: determina para qual partição o registro vai. Kafka garante que todos os registros com a mesma chave vão para a mesma partição → **ordenação garantida dentro de uma partição**.

**Consumer group**: grupo de consumers que compartilham o processamento de um tópico. Cada partição é atribuída a exatamente um consumer no grupo. Mais consumers que partições → consumers ociosos.

**Replication factor**: número de brokers que guardam cópia de cada partição. Leader atende reads/writes; followers replicam. Falha do leader → um follower assume a liderança.

| Configuração | Impacto |
|---|---|
| N partições | Paralelismo máximo = N (consumers e producers) |
| Replication factor = R | R × mais disco; R × mais tráfego de rede; tolera R-1 falhas de broker |
| Retention time | Eventos mais antigos que o limite são removidos |

**Regra**: Defina o número de partições de um tópico com base em testes de performance antes de criá-lo — adicionar partições depois exige migração custosa.

> ⚠ Evite: replication factor = 1 em produção — não tolera nenhuma falha de broker sem perda de dados.

### 15.3 Lógica do producer: acks e consistência vs. disponibilidade

**Configuração mínima do producer**:
1. `bootstrap-servers`: lista de brokers do cluster
2. `key.serializer`: serializer da chave (ex: `IntegerSerializer`)
3. `value.serializer`: serializer do valor (ex: `StringSerializer`)

**Parâmetro `acks`**: controla quantos brokers devem confirmar recebimento antes do producer considerar o send bem-sucedido.

| acks | Comportamento | Consistência | Disponibilidade |
|---|---|---|---|
| `all` | Aguarda confirmação de todos os brokers no ISR | Alta (sem perda em falha de broker) | Menor (bloqueia se algum broker falhar) |
| `1` | Aguarda confirmação apenas do leader | Média (perda se leader cair antes da replicação) | Maior (um broker basta) |
| `0` | Fire-and-forget, sem esperar confirmação | Mínima (alta chance de perda) | Máxima |

**Retries e ordering**: retries habilitados (default) introduzem possibilidade de out-of-order delivery dentro de uma partição — o batch retido pode chegar depois do batch enviado depois dele. Use `max.in.flight.requests.per.connection=1` para preservar ordering (custo de throughput).

**Regra**: Configure `acks=all` quando consistência é crítica (ex: pagamentos). Use `acks=1` quando disponibilidade é prioritária e alguma perda de dados é aceitável.

**Regra**: Calcule o número de brokers necessários com base no throughput por broker e no replication factor: `brokers = (MB/s_total × replication_factor) / throughput_por_broker`.

### 15.4 Lógica do consumer: semântica de entrega

**Auto-commit** (`enable.auto.commit=true`): offset commitado automaticamente a cada N ms (`auto.commit.interval.ms`, default 5 s). Se o consumer falha antes do auto-commit, outro consumer retoma do último offset commitado → **at-least-once** (até N s × eventos/s de duplicatas possíveis).

**Manual commit síncrono** (`commitSync()`): commit após processamento de cada registro — garante at-least-once sem janela de duplicata de 5 s, mas bloqueia o processamento até o commit completar.

```java
for (ConsumerRecord<Integer, String> record : records) {
  logicProcessing(record);
  try {
    consumer.commitSync();   // bloqueia até commit completo
  } catch (CommitFailedException e) {
    logger.error("commit failed", e);
  }
}
```

**Manual commit assíncrono** (`commitAsync()`): não bloqueia, mas exceções não propagam ao thread principal — use callback para logar falhas.

```java
consumer.commitAsync(
    (offsets, exception) -> {
      if (exception != null)
        logger.error("Commit failed for offsets {}", offsets, exception);
    });
```

**Commit antes do processamento**: at-most-once — evento marcado como processado antes de ser processado. Se o processamento falha, o evento é perdido (não reprocessado).

**Offset reset strategy** (quando não há offset commitado):
- `earliest`: resume do offset 0 → **at-least-once** (pode reprocessar tudo)
- `latest`: resume do offset mais recente → **at-most-once** (eventos anteriores ao crash são perdidos)

| Estratégia | Delivery semantic | Quando usar |
|---|---|---|
| Auto-commit | At-least-once | Dados não críticos, tolerante a duplicatas |
| Manual commit pós-processamento | At-least-once | Dados críticos, sem perda aceitável |
| Commit antes do processamento | At-most-once | Latência crítica, alguma perda aceitável |
| Offset reset = earliest | At-least-once | Sistemas de pagamento, eventos que não podem ser perdidos |
| Offset reset = latest | At-most-once | Sistemas de alertas, dados perecíveis |

**Regra**: Para sistemas de pagamento ou domínios onde a perda de eventos é inaceitável, use commit manual pós-processamento com `auto.offset.reset=earliest`.

**Regra**: Para sistemas de alertas ou monitoramento onde eventos desatualizados têm pouco valor, `auto.offset.reset=latest` reduz processamento desnecessário de backlog.

### 15.5 Effectively exactly-once semantics

**Exactly-once** é difícil de implementar de ponta a ponta. Na prática, sistemas usam **effectively exactly-once**: at-least-once + deduplicação.

**Kafka transactions** (`transactional_id`): o producer inicia uma transação antes de enviar. Em caso de falha, o Kafka faz rollback — o registro não aparece no tópico. Isso elimina duplicatas no nível do Kafka.

**Limitação crítica**: transações do Kafka só cobrem o producer Kafka. Se o evento que disparou o producer veio de outro sistema (HTTP, outro Kafka cluster) com at-least-once delivery, o producer receberá duplicatas e as tratará como eventos independentes — gerando duplicatas na saída mesmo com transações.

```
Client (at-least-once) → Request-A + Request-A-retry → Kafka Producer (exactly-once) → Kafka Topic
                                                         ↑ vê dois eventos diferentes ↑
                                                    → emite dois registros no topic
```

**Regra**: Effectively exactly-once só funciona se **todos os componentes** do pipeline implementam esta semântica — um componente com at-least-once "contamina" todo o fluxo downstream.

> ⚠ Evite: assumir que Kafka transactions garantem exactly-once end-to-end — elas só funcionam dentro dos limites do producer Kafka. Para pipelines complexos com N serviços, exactly-once requer deduplicação em cada estágio.

### 15.6 Fault tolerance via delivery guarantees

**Padrão**: checkout service (50 rps) → Kafka topic → billing service (SLA: 100 rps).

**Cenário de falha**: billing service fica offline por 5 s. Acumulam-se 250 eventos no Kafka topic (50 rps × 5 s). Quando o billing service volta, ele processa:
- 50 rps (tráfego novo do checkout)
- + ~250 rps necessários para esgotar o backlog

Com capacidade de 100 rps e tráfego atual de 50 rps, o billing service tem 50 rps de capacidade livre → precisa de ~5 s extras para consumir o backlog de 250 eventos.

**Condição para fault tolerance funcionar**:
1. A fila persiste eventos durante a indisponibilidade do consumer
2. O consumer usa `auto.offset.reset=earliest` + commit pós-processamento (at-least-once)
3. O SLA do consumer > tráfego do producer (capacidade livre para absorver backlog)

**Mesmo padrão para traffic surges**: se o checkout emite 200 rps temporariamente (acima dos 100 rps que o billing suporta), o excesso é bufferizado no Kafka. Quando o tráfego volta ao normal, o billing processa o backlog com sua capacidade disponível.

**Regra**: Dimensione o SLA do consumer para ser significativamente maior que o throughput do producer — a diferença de capacidade é o "buffer" que determina o tempo de recuperação após falhas ou picos de tráfego.

**Regra**: O consumer deve ter SLA substancialmente acima do producer para absorver picos de tráfego e retomar o processamento de eventos bufferizados sem acumular atraso.

---

## 16 Versionamento e Compatibilidade

### 16.1 Semantic Versioning (SemVer)

Versão SemVer tem três partes: `major.minor.patch`.

| Mudança | Impacto de versão | Garantia |
|---|---|---|
| Breaking change | Novo `major` | Nenhuma compatibilidade garantida |
| Backward-compatible (nova feature) | Novo `minor` | `1.3.x` backward-compatible com `1.2.y` |
| Backward + forward compatible (bug fix) | Novo `patch` | `1.2.4` e `1.2.1` compatíveis em ambas as direções |

**Versões instáveis**:
- `0.x.y`: desenvolvimento inicial; sem garantias de SemVer entre patches
- Prerelease label: `1.4.5-beta.1` — indica instabilidade; sufixo após `-`
- Build metadata: `1.2.3+20210321.af25738` — puramente informacional; sem efeito em precedência

**Regra**: Use prerelease labels (ex: `1.0.0-alpha.1`, `1.0.0-beta.1`) desde o primeiro release público e reserve `0.x.y` apenas para prototipagem precoce — `0.x.y` só funciona bem até `1.0.0` e cria confusão na numeração das versões seguintes.

> 💡 Nota: Build metadata não afeta precedência de versões. Precedência: `major > minor > patch > prerelease` (ausência de prerelease é maior que qualquer prerelease do mesmo `major.minor.patch`).

### 16.2 Backward vs. forward compatibility

| Conceito | Definição | Exemplo |
|---|---|---|
| **Backward compatibility** | Nova versão funciona com informação/código da versão antiga | Java 17 compila código Java 7 |
| **Forward compatibility** | Versão antiga funciona com informação/código da versão nova | Protobuf: código antigo ignora campos novos |

Em APIs de rede, backward compatibility é o padrão — uma request construída em janeiro de 2021 deve continuar funcionando em abril de 2021. Formatos binários como Protocol Buffers e Apache Avro são projetados para suportar ambas as direções.

### 16.3 Tipos de compatibilidade em bibliotecas

Três tipos a analisar para toda mudança em biblioteca compilada:

| Tipo | Definição | Quando quebra |
|---|---|---|
| **Source** | Consumer recompila contra nova versão sem erros | Renomear método, mudar tipo de parâmetro para supertipo (viola `@Override`) |
| **Binary** | Bytecode compilado contra versão antiga executa contra nova sem `NoSuchMethodError` | Mudar tipo de parâmetro de `String` para `Object` — JVM não encontra `displayData(String)` |
| **Semantic** | Comportamento permanece equivalente | Alterar validação de parâmetro; inverter delegação entre overloads quando herança é permitida |

**Casos não óbvios de source incompatibility**:
- Adicionar método a interface sem default implementation: qualquer implementador da interface quebra
- Adicionar método abstrato a abstract class: mesmo efeito
- Renomear parâmetro: não é breaking em Java, mas é breaking em C# (named arguments)

**Binary incompatibility é especialmente perigosa porque**:
1. Aparece apenas em runtime, não em compilação
2. Aparece apenas no code path que chama o método — code paths de error handling (menos testados) são os mais afetados

**Regra**: Para toda mudança na API pública, pergunte explicitamente: há consumer code que quebraria em source? E em binary? Considere a probabilidade e a obscuridade do código afetado antes de classificar como breaking change.

### 16.4 Hyrum's Law: compatibilidade semântica

> "With a sufficient number of users of an API, it does not matter what you promise in the contract: all observable behaviors of your system will be depended on by somebody." — Hyrum Wright

Três categorias de semantic change que exigem atenção especial:

1. **Validação de parâmetros**: afrouxar validação (permitir `null` antes proibido) pode quebrar silenciosamente código que dependia da exceção como mecanismo de validação.
2. **Herança e delegação de overloads**: alterar qual overload chama qual é detalhe de implementação, mas se os métodos podem ser sobrescritos, é efetivamente contrato público.
3. **Performance**: padrão de uso antes eficiente pode se tornar ineficiente após refatoração. Em libs performance-sensitive, pode ser considerado breaking.

**Regra**: Para afrouxar validação, adicione um overload ou método alternativo aceitando o input antes inválido — nunca remova a validação do método existente, pois código que dependia da exceção quebrará silenciosamente.

**Regra**: Documente explicitamente quais behaviors são garantidos e quais são detalhes de implementação — sem isso, Hyrum's Law garante que qualquer behavior será dependido por alguém.

> ⚠ Evite: tratar "não é interface pública" como licença para mudar qualquer implementação livremente quando herança é permitida — toda implementação que pode ser sobrescrita é efetivamente contrato público.

### 16.5 Diamond dependency: compartilhada vs. isolada

**Diamond dependency**: componente A e componente B dependem de versões diferentes de uma mesma lib C. Qual versão é usada?

**Dependências compartilhadas** (padrão na JVM/Maven):
- Toda a aplicação usa uma única versão
- Objetos de tipos da lib passam entre componentes sem conversão
- Custo: se as versões são incompatíveis (major diferente), não há versão que satisfaça ambos

**Dependências isoladas** (fat jar / shading):
- Cada componente tem sua cópia da lib (package prefix próprio via shading)
- Sem conflito de versões
- Custo: N cópias em memória; objetos da mesma lib não são compatíveis entre componentes em linguagens estáticas (tipos de mesmo nome de JARs diferentes são incompatíveis)

**Custo de um major version bump no ecossistema**:
- Toda biblioteca dependente que quer atualizar precisa avaliar se isso também exige major bump na dela
- Quanto mais popular a lib, maior o impacto em cadeia

**Regra**: Use dependências isoladas (shading) quando a lib é usada apenas como detalhe de implementação e nenhum objeto dela aparece na API pública — elimina conflito de versão sem custo para o caller.

**Regra**: Em bibliotecas populares, major version bumps devem ser raros e agrupados — o custo para o ecossistema é proporcional ao número de consumidores diretos e transitivos.

> (Fonte acrescenta: dependências compartilhadas são eficientes mas exigem convergência de versão; isoladas resolvem conflitos mas tornam objetos da mesma lib incompatíveis entre componentes em linguagens estáticas.)

### 16.6 Técnicas para gerenciar breaking changes

**Limitar surface da API pública**:
- Comece com API restrictiva — adicionar é mais seguro do que remover
- Marque partes instáveis com `@Beta` ou colocando em package `internal`
- Use `final` em classes onde herança não é necessária — evita semantic breaking changes via override

**Regra**: Siga a orientação de Josh Bloch: "Design for inheritance, or prohibit it." — se um método pode ser sobrescrito e chama outro overload, documente qual chama qual como parte do contrato público.

**Parâmetros que crescem**: se um construtor ou método acumula parâmetros a cada release, encapsule-os em um tipo próprio — permite adicionar campos sem quebrar callers existentes.

**Bridging release** (release de transição antes do major bump):
```java
// NodaTime 1.4 — transição antes do 2.0
public interface IClock {
    @Obsolete("Use GetCurrentInstant() extension method")
    Instant Now { get; }   // versão antiga marcada obsoleta
}
public static class ClockExtensions {
    public static Instant GetCurrentInstant(this IClock clock) => clock.Now;  // bridge para API nova
}
```

A versão 1.4 é source e binary compatible com 1.3, mas orienta os callers a migrar antes do major bump. Fornece migration path sem downtime forçado.

**Regra**: Agrupe breaking changes planejadas — publique-as juntas em um único major bump. Mantenha documento de breaking changes pendentes desde o início.

**Regra**: Para cada major bump, publique migration guide explícito, incluindo casos sutis.

**Regra**: Para decidir se uma mudança é breaking, identifique o consumer code mais provável que seria afetado. Se exigiria feature obscura da linguagem para quebrar, considere minor bump com documentação transparente.

> ⚠ Evite: major version bump defensivo sempre que houver dúvida — major bumps têm custo alto no ecossistema. Se há evidência de que a mudança não afetará usuários reais, considere minor com documentação.

### 16.7 Bibliotecas internas

Abordagens de versionamento interno:
- **Live at head**: todos os componentes compilam sempre contra a última versão de todas as dependências internas
- **Versioned modules**: módulos com versões semânticas em package manager interno
- **Híbrido**: módulos core versionados, demais componentes em source control compartilhado

**Evolução gradual** (preferível a breaking changes abruptas):
1. Deprecar símbolos que serão removidos (sem remover ainda)
2. Aguardar todos os consumers migrarem para a nova API
3. Remover após "cooling off period" — tempo suficiente para rollbacks
4. Verificar que nenhum código usa os símbolos antes de publicar

**Regra**: Para mudanças em bibliotecas internas, evolua consumer code e biblioteca juntos — garante que tudo continua funcionando e os símbolos antigos vão perdendo uso gradualmente.

**Regra**: Documente o processo de mudanças para todos no time — estratégia de versionamento que ninguém entende cria inconsistência entre times.

### 16.8 Versionamento de APIs de rede

**Client-controlled versioning**: o cliente especifica a versão exata (ex: `1.1`).
- Servidor valida o request conforme a versão especificada
- Servidor retorna apenas campos presentes na versão especificada
- Servidor não modifica campos desconhecidos para a versão do cliente
- Custo: servidor precisa manter implementação de todas as minor versions suportadas

**Server-controlled versioning**: o cliente especifica apenas a versão major (ex: `v1`).
- Servidor pode incluir campos novos no response — cliente deve ignorar campos desconhecidos
- Mais simples de implementar (servidor mantém apenas N major versions)
- **Problema de read-modify-write**: cliente atualiza recurso enviando todos os campos que conhece → campos desconhecidos são sobrescritos como vazios

**Solução para read-modify-write em server-controlled**: patch semantics — cliente especifica explicitamente quais campos está atualizando:

```
Method: PatchPerson
Body:
  resource={id=2, name="Eric"}
  fields="name"   // apenas "name" será atualizado; occupation preservado
```

**Deploy sem downtime**:
1. Deploy canary → monitorar → testar features novas → expandir rollout → publicar nova API

**Regra**: Em client-controlled versioning, automatize desde o início a validação de requests e a remoção de campos da versão especificada — manter isso manualmente não escala.

**Regra**: Em server-controlled versioning, use patch semantics para toda atualização de recurso — sem isso, updates silenciosamente destroem campos que o cliente não conhece.

**Regra**: Não inclua a versão da API no identificador do recurso — clientes de v1 e v2 precisam acessar os mesmos recursos.

**Regra**: Documente a estratégia de versionamento como entregável — clientes precisam de clareza sobre lifecycle, breaking changes e janelas de suporte para planejar suas integrações.

### 16.9 Versionamento de armazenamento de dados

Usando Protocol Buffers como referência (princípios aplicáveis a qualquer formato):

**O que é breaking change em storage?**

| Mudança | Efeito em dados armazenados | Efeito em código gerado |
|---|---|---|
| Renomear campo | Nenhum (binary usa número, não nome) | Breaking (nome muda no código) |
| Remover campo | Campo persiste mas é ignorado | Breaking (referências ao campo quebram) |
| Adicionar campo | Nenhum (backward compatible) | Não breaking |
| Mudar tipo serializado (`int32` → `sint32`) | Dados existentes interpretados diferente | Pode não mudar código gerado |
| Adicionar valor ao enum | Nenhum | Código que trata todos os valores precisa ser atualizado |

> ⚠ Evite: reutilizar número de campo removido para outra finalidade — dados antigos ainda podem conter aquele número e serão interpretados erroneamente. Use `reserved 2;` no schema após remover um campo.

**Migração de dados sem downtime** (migrar campo `icon_png` → `IconCollection`):

1. Planejar e alinhar com stakeholders
2. Adicionar novo campo/mensagem ao schema
3. Código de leitura: ler novo campo se presente, senão ler campo antigo
4. Código de escrita: escrever em ambos os campos
5. Deploy → aguardar estabilização
6. Migration tool: preencher novo campo em registros existentes
7. Código: usar apenas o novo campo
8. Deploy → aguardar estabilização
9. Migration tool: limpar campo antigo
10. Substituir campo antigo por `reserved <número>;` no schema

**Regra**: Nunca execute três versões de código simultâneas sobre os mesmos dados — coordene o deploy para que no máximo duas versões estejam ativas ao mesmo tempo (v_old e v_migration, depois v_migration e v_new).

**Regra**: Reserve números de campo removidos com `reserved N;` no protobuf schema para evitar reutilização acidental.

**Regra**: Para enums que podem crescer, escreva código que preserve valores numéricos desconhecidos em vez de lançar exceção — use strings (MIME types, ISO codes) em vez de enums quando o domínio é extensível.

**Regra**: Prefira mensagens a tipos primitivos para campos que podem evoluir (ex: `IconCollection` em vez de `bytes icon_png`) — facilita adicionar campos secundários sem migração de dados posterior.

### 16.10 Separando schemas de API e de armazenamento

Usar o mesmo schema para API de rede e para armazenamento dá velocidade inicial ao custo de flexibilidade a longo prazo.

**Por que separar**:
- APIs de rede têm clientes de múltiplas versões simultâneas; breaking changes são caras
- Storage schemas precisam evoluir para otimização e migração frequente
- Representação ideal para armazenamento pode diferir da ideal para API (ex: enum no storage, string na API para campos extensíveis)

**Abordagens de transformação**:

| Abordagem | Quando usar | Custo |
|---|---|---|
| Manual (copy-paste-edit) | Início do projeto; schema pequeno | Tedioso; corner cases são fáceis de esquecer |
| Automatizada (tooling interno) | Após experiência manual e corner cases documentados | Tooling complexo; escape hatches necessários |

**Regra**: Comece com transformações manuais e anote todos os corner cases e sua resolução — essas anotações são a base para automação futura e um bom conjunto de test cases.

**Regra**: No tooling automatizado, forneça escape hatches para partes do schema que divergem significativamente — forçar a automação a cobrir tudo cria um tool insustentável.

**Regra**: Revise manualmente o output do tooling nas primeiras N mudanças de schema até que surpresas parem de aparecer — depois, remova as revisões do processo.

---

## 17 Tendências vs. Custo de Manutenção

Antes de adotar qualquer novo framework ou padrão, verifique se o problema que ele resolve é realmente o seu problema principal. Se não for, você importa complexidade sem obter os benefícios prometidos.

**Regra**: Investigue pros e contras de um novo approach antes de migrar. Analise se o problema central que o framework resolve é um problema real e medido na sua aplicação.

### 17.1 Dependency Injection: DIY vs. framework

**DIY DI** (sem framework):
- Toda inicialização de dependências em um único lugar (classe `Application` ou entry point)
- Lifecycle e ordering são explícitos e fáceis de depurar
- Trocar implementações é simples: alterar uma linha no ponto central

```java
public class Application {
  public static void main(String[] args) {
    DbConfiguration dbConfiguration = loadDbConfig();
    InventoryConfiguration inventoryConfiguration = loadInventoryConfig();
    InventoryDb inventoryDb = new InventoryDb(dbConfiguration);
    InventoryService inventoryService = new InventoryService(inventoryDb, inventoryConfiguration);
    inventoryService.prepareInventory();
  }
}
```

**DI Framework (ex.: Spring)**:
- Beans declarados com `@Configuration`, `@Service`, `@Autowired`, `@Scope`
- Container gerencia lifecycle, ordering e injection implicitamente
- `@Scope("request")` cria nova instância por request — mas exige framework web compatível (Spring REST), puxando nova dependência

```java
@Service
@Scope("request")
public class InventoryService {
  @Autowired
  public InventoryService(InventoryDb inventoryDb, InventoryConfiguration cfg) { ... }
}
```

**Problemas do DI framework**:
- Lifecycle e ordering são ocultos — problemas de lifecycle são muito mais difíceis de depurar
- Todas as classes ficam acopladas às anotações do framework
- Lógica de inicialização distribuída pelo codebase (difícil ver o quadro completo)
- Uma dependência puxa outra: `@Scope("request")` exige Spring REST

**Regra**: Use DI framework quando necessitar genuinamente de suas features (gerenciamento de scope complexo, AOP, proxy). Para casos simples ou quando quiser minimizar dependências externas, prefira DIY DI.

**Regra**: Nunca misture instanciação manual com beans gerenciados pelo framework — cria dois mecanismos incompatíveis de lifecycle.

> ⚠ Evite: Adotar DI framework por tendência sem medir se seu problema real exige as features que ele oferece. Um `ServiceFactory` simples pode substituir `@Scope("request")` sem importar todo o Spring.

### 17.2 Programação Reativa: CompletableFuture vs. Flux

Evolução de uma pipeline de processamento: blocking → async → reactive.

**Blocking (Stream API)**:
```java
// Todo processamento no thread caller — single-threaded, blocking
public List<Integer> calculateForUserIds(List<Integer> userIds) {
  return userIds.stream()
      .map(IOService::blockingGet)
      .map(CPUIntensiveTask::calculate)
      .collect(Collectors.toList());
}
```

**CompletableFuture** (async, built-in SDK):
```java
public List<CompletableFuture<Integer>> calculateForUserIds(List<Integer> userIds) {
  return userIds.stream()
      .map(v -> CompletableFuture.supplyAsync(() -> IOService.blockingGet(v))
                    .thenApply(CPUIntensiveTask::calculate))
      .collect(Collectors.toList());
}
// Caller pode bloquear (.get()) ou encadear async — não impõe API ao caller
```

**Reactive (Flux/Reactor)**:
```java
public Flux<Integer> calculateForUserIds(List<Integer> userIds) {
  return Flux.fromIterable(userIds)
      .publishOn(Schedulers.boundedElastic())  // I/O blocking
      .map(IOService::blockingGet)
      .publishOn(Schedulers.parallel())         // CPU intensivo
      .map(CPUIntensiveTask::calculate);
}
// Retornar Flux força todos os callers a migrarem para API reativa
```

**Comparação**:

| Abordagem | Threading | API imposta ao caller | Controle de threads | Thread affinity |
|-----------|-----------|----------------------|---------------------|-----------------|
| Stream | Caller thread, blocking | Não | Total | Fácil |
| CompletableFuture | Pool separado, async | Não (caller escolhe) | Direto via executor explícito | Fácil |
| Flux | Schedulers implícitos | Sim (todos devem usar Flux) | Indireto/complexo | Difícil |

**Problemas do Flux**:
- API vaza para todos os callers: quem retorna `Flux` força migração end-to-end
- Blocking dentro de Flux com hot datasource → risco de bloqueio indefinido
- Caller pode alterar thread pool via `subscribeOn()`, interferindo no seu scheduler
- Thread affinity difícil: I/O (`boundedElastic`) e CPU (`parallel`) não podem compartilhar thread

**Regra**: Adote reactive end-to-end ou não adote. Reactive em um único subcomponente importa a invasividade da API sem o benefício sistêmico.

**Regra**: Para concorrência/paralelismo com dados finitos, prefira `CompletableFuture` — não força o caller a mudar sua API e oferece controle de thread pool via executor explícito.

**Regra**: Ao misturar I/O bloqueante e CPU no Flux, use schedulers separados: `boundedElastic` para I/O, `parallel` para CPU.

> ⚠ Evite: Adotar reactive por tendência quando o caso de uso envolve dados finitos e processamento blocking — `CompletableFuture` resolve com muito menos complexidade e sem invasão de API.

### 17.3 Programação Funcional em Linguagem OO

**Problema com recursão em Java**:
- Cada chamada recursiva aloca um frame na call stack
- ~100.000 elementos → `StackOverflowError`
- Java não tem tail call optimization (TCO)

```java
// PERIGOSO em Java para grandes inputs:
private static <T> T reduceInternal(List<T> values, BinaryOperator<T> reducer, T acc) {
  if (values.isEmpty()) return acc;
  return reduceInternal(getTail(values), reducer, reducer.apply(getHead(values), acc));
  // StackOverflowError para 100k elementos
}
```

**Tail recursion em linguagem funcional (Scala)**:
```scala
@tailrec
def reduce[T](values: List[T], reducer: (T, T) => T, accumulator: T): T = values match {
  case Nil => accumulator
  case head :: tail => reduce(tail, reducer, reducer(head, accumulator))
}
// @tailrec converte recursão em loop no nível do compilador — seguro para qualquer tamanho
```

**Imutabilidade — custos e mitigação**:
- Imutável = thread-safe sem synchronization; estado preenchido na construção, nunca depois
- `final` em Java protege a referência, não o objeto referenciado — não garante imutabilidade
- Custo: novo objeto por modificação → pressão no GC
- Mitigação: structural sharing — nova lista imutável aponta para a cabeça da lista original, compartilhando nós restantes sem cópia

**Regra**: Em Java (e outras linguagens OO não-funcionais), implemente operações sobre coleções potencialmente grandes (reduce, fold) de forma imperativa (for loop) — recursão causa `StackOverflowError` para inputs grandes.

**Regra**: Use construtos funcionais da biblioteca padrão (`Stream.reduce()`, `Optional`) em vez de reimplementá-los recursivamente — as implementações da stdlib são imperativas internamente.

**Regra**: Meça o impacto no GC antes de adotar imutabilidade pervasiva em hot paths de alto throughput — objetos copiados frequentemente criam pressão de coleta.

> ⚠ Evite: Aplicar padrões funcionais sem entender as limitações da linguagem host. Em Java, recursão sem TCO explode a stack para entradas grandes.

### 17.4 Inicialização Lazy vs. Eager

| Abordagem | Startup | Primeiros N requests | Detecção de erros |
|-----------|---------|---------------------|-------------------|
| Lazy | Mais rápido | Impactados (pagam o custo de inicialização) | Tarde — quando o serviço já está operacional |
| Eager | Mais lento | Não impactados | Durante o deployment |

**Lazy**: conexão ao banco e cache populados no primeiro request.
- Benefício: startup mais rápido (útil quando startup time é crítico)
- Custo: os primeiros N requests (N = pool size) pagam o custo de inicialização
- Risco: erros de inicialização surgem tarde, possivelmente após o deployment completo, já afetando usuários

**Eager**: conexão ao banco e cache populados no startup.
- Benefício: requests nunca pagam custo de inicialização; erros aparecem durante o deployment
- Com rolling deployment: nova versão falha antes de substituir a antiga → rollback antes de afetar usuários
- Custo: startup mais lento

**Regra**: Se o SLA tem limite rígido de latência de request, evite inicialização lazy para operações custosas (connection pool, população de cache).

**Regra**: Para deployments com rolling updates, prefira inicialização eager para recursos críticos — erros aparecem antes da versão velha ser totalmente substituída, permitindo rollback sem impacto ao usuário.

**Regra**: Use abordagem híbrida: recursos críticos (conexões DB, caches essenciais) de forma eager; features raramente usadas de forma lazy.
