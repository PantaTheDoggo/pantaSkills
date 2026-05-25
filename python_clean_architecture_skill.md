# Skill: Clean Architecture with Python — Referência Consolidada

> **Fonte**: Clean Architecture with Python, Sam Keen, Packt Publishing, Junho 2025
> **Alvo**: Python, arquitetura de software, design patterns
> **Última extração**: 2026-05

---

## Índice

| # | Seção |
|---|---|
| 1 | [Capítulo 1 — Clean Architecture Essentials: Transforming Python Development](#capítulo-1--clean-architecture-essentials-transforming-python-development) |
| 1.1 | [Dependency Rule](#11-dependency-rule) |
| 1.2 | [As Quatro Camadas (Onion Architecture)](#12-as-quatro-camadas-onion-architecture) |
| 1.3 | [Separation of Concerns (SoC)](#13-separation-of-concerns-soc) |
| 1.4 | [Benefits of Clean Architecture](#14-benefits-of-clean-architecture) |
| 1.5 | [Screaming Architecture](#15-screaming-architecture) |
| 1.6 | [Implementando em Python: ABCs](#16-implementando-em-python-abcs) |
| 1.7 | [Implementando em Python: Protocols](#17-implementando-em-python-protocols) |
| 1.8 | [Considerações Python-específicas](#18-considerações-python-específicas) |
| 2 | [Capítulo 2 — SOLID Foundations: Building Robust Python Applications](#capítulo-2--solid-foundations-building-robust-python-applications) |
| 2.1 | [SRP — Single Responsibility Principle](#21-srp--single-responsibility-principle) |
| 2.2 | [OCP — Open-Closed Principle](#22-ocp--openclosed-principle) |
| 2.3 | [ISP — Interface Segregation Principle](#23-isp--interface-segregation-principle) |
| 2.4 | [LSP — Liskov Substitution Principle](#24-lsp--liskov-substitution-principle) |
| 2.5 | [DIP — Dependency Inversion Principle](#25-dip--dependency-inversion-principle) |
| 3 | [Capítulo 3 — Type-Enhanced Python: Strengthening Clean Architecture](#capítulo-3--type-enhanced-python-strengthening-clean-architecture) |
| 3.1 | [Type Hinting como Ferramenta Arquitetural](#31-type-hinting-como-ferramenta-arquitetural) |
| 3.2 | [Leveraging Python's Typing System](#32-leveraging-pythons-typing-system) |
| 3.3 | [Automated Static Type-Checking Tools](#33-automated-static-type-checking-tools) |
| 4 | [Capítulo 4 — Domain-Driven Design: Crafting the Core Business Logic](#capítulo-4--domain-driven-design-crafting-the-core-business-logic) |
| 4.1 | [DDD: Conceitos Fundamentais](#41-ddd-conceitos-fundamentais) |
| 4.2 | [Implementando Entidades em Python](#42-implementando-entidades-em-python) |
| 4.3 | [Aggregates e Factory Pattern](#43-aggregates-e-factory-pattern) |
| 4.4 | [Independência do Domain Layer](#44-independência-do-domain-layer) |
| 5 | [Capítulo 5 — The Application Layer: Orchestrating Use Cases](#capítulo-5--the-application-layer-orchestrating-use-cases) |
| 5.1 | [Papel da Application Layer](#51-papel-da-application-layer) |
| 5.2 | [Error Handling com Result Types](#52-error-handling-com-result-types) |
| 5.3 | [Implementando Use Case Interactors](#53-implementando-use-case-interactors) |
| 5.4 | [Request e Response Models](#54-request-e-response-models) |
| 5.5 | [Separação de Serviços Externos via Ports](#55-separação-de-serviços-externos-via-ports) |
| 6 | [Capítulo 6 — The Interface Adapters Layer: Controllers and Presenters](#capítulo-6--the-interface-adapters-layer-controllers-and-presenters) |
| 6.1 | [Papel da Interface Adapters Layer](#61-papel-da-interface-adapters-layer) |
| 6.2 | [Controllers em Python](#62-controllers-em-python) |
| 6.3 | [Enforcing Boundaries via OperationResult](#63-enforcing-boundaries-via-operationresult) |
| 6.4 | [Presenters e o Humble Object Pattern](#64-presenters-e-o-humble-object-pattern) |
| 7 | [Capítulo 7 — The Frameworks and Drivers Layer: External Interfaces](#capítulo-7--the-frameworks-and-drivers-layer-external-interfaces) |
| 7.1 | [Posição e Responsabilidade da Camada](#71-posição-e-responsabilidade-da-camada) |
| 7.2 | [Frameworks versus Drivers — Distinção](#72-frameworks-versus-drivers--distinção) |
| 7.3 | [Application Composition — Composição da Aplicação](#73-application-composition--composição-da-aplicação) |
| 7.4 | [Framework Adapter — UI com Click (ClickCli)](#74-framework-adapter--ui-com-click-clickcli) |
| 7.5 | [Implementando Interações de Usuário](#75-implementando-interações-de-usuário) |
| 7.6 | [Domain Insights via Implementação de UI — Inbox Pattern](#76-domain-insights-via-implementação-de-ui--inbox-pattern) |
| 7.7 | [Database Adapters — Implementação de Repository](#77-database-adapters--implementação-de-repository) |
| 7.8 | [Gerenciamento de Instanciação — Config e Factory](#78-gerenciamento-de-instanciação--config-e-factory) |
| 7.9 | [Integração de Serviços Externos — SendGrid](#79-integração-de-serviços-externos--sendgrid) |
| 7.10 | [Application Bootstrapping — Container e Composition Root](#710-application-bootstrapping--container-e-composition-root) |
| 8 | [Capítulo 8 — Implementing Test Patterns with Clean Architecture](#capítulo-8--implementing-test-patterns-with-clean-architecture) |
| 8.1 | [Fundamentos de Testes em Clean Architecture](#81-fundamentos-de-testes-em-clean-architecture) |
| 8.2 | [Testes Unitários por Camada](#82-testes-unitários-por-camada) |
| 8.3 | [Testing Across Architectural Boundaries](#83-testing-across-architectural-boundaries) |
| 8.4 | [Tools and Patterns for Test Maintenance](#84-tools-and-patterns-for-test-maintenance) |
| 9 | [Capítulo 9 — Adding Web UI: Clean Architecture's Interface Flexibility](#capítulo-9--adding-web-ui-clean-architectures-interface-flexibility) |
| 9.1 | [Interface Flexibility — Adição Puramente Aditiva](#91-interface-flexibility--adição-puramente-aditiva) |
| 9.2 | [Parallel Interface Implementations](#92-parallel-interface-implementations) |
| 9.3 | [Common Interface Boundary Violations](#93-common-interface-boundary-violations) |
| 9.4 | [Web-Specific Presenters](#94-web-specific-presenters) |
| 9.5 | [Presenters versus Template-based Formatting](#95-presenters-versus-template-based-formatting) |
| 9.6 | [Managing Web-Specific State](#96-managing-web-specific-state) |
| 9.7 | [Form Handling and Validation](#97-form-handling-and-validation) |
| 9.8 | [Flask Application Factory](#98-flask-application-factory) |
| 9.9 | [Routes e Templates](#99-routes-e-templates) |
| 10 | [Capítulo 10 — Implementing Observability: Monitoring and Verification](#capítulo-10--implementing-observability-monitoring-and-verification) |
| 10.1 | [Observation Points in Clean Architecture](#101-observation-points-in-clean-architecture) |
| 10.2 | [Avoiding Framework Coupling in Logging](#102-avoiding-framework-coupling-in-logging) |
| 10.3 | [Structured Logging Patterns](#103-structured-logging-patterns) |
| 10.4 | [Cross-Boundary Request Tracing](#104-cross-boundary-request-tracing) |
| 10.5 | [Fitness Functions — Verifying Layer Structure](#105-fitness-functions--verifying-layer-structure) |
| 10.6 | [Fitness Functions — Enforcing Dependency Rules](#106-fitness-functions--enforcing-dependency-rules) |
| 11 | [Capítulo 11 — Legacy to Clean: Refactoring Python for Maintainability](#capítulo-11--legacy-to-clean-refactoring-python-for-maintainability) |
| 11.1 | [Análise Arquitetural Preliminar](#111-análise-arquitetural-preliminar) |
| 11.2 | [Alinhamento com Stakeholders](#112-alinhamento-com-stakeholders) |
| 11.3 | [Domain Analysis — Event Storming](#113-domain-analysis--event-storming) |
| 11.4 | [Staged Implementation Roadmap](#114-staged-implementation-roadmap) |
| 11.5 | [Abordagens de Execução da Transformação](#115-abordagens-de-execução-da-transformação) |
| 11.6 | [Navegando a Transformação In-Flight](#116-navegando-a-transformação-in-flight) |
| 11.7 | [Análise do Sistema Legado](#117-análise-do-sistema-legado) |
| 11.8 | [Stage 1 — Estabelecendo Fronteiras de Domínio](#118-stage-1--estabelecendo-fronteiras-de-domínio) |
| 11.9 | [Stage 2 — Interface Layer Implementation](#119-stage-2--interface-layer-implementation) |
| 11.10 | [Stage 3 — Integration Strategy: Feature Flags e Adapter Pattern](#1110-stage-3--integration-strategy-feature-flags-e-adapter-pattern) |
| 11.11 | [Stage 4 — Optimization](#1111-stage-4--optimization) |
| 12 | [Capítulo 12 — Your Clean Architecture Journey: Next Steps](#capítulo-12--your-clean-architecture-journey-next-steps) |
| 12.1 | [Python como Plataforma para Clean Architecture](#121-python-como-plataforma-para-clean-architecture) |
| 12.2 | [Clean Architecture em Sistemas API-First](#122-clean-architecture-em-sistemas-api-first) |
| 12.2.1 | [Request Models como Contratos Públicos](#1221-request-models-como-contratos-públicos) |
| 12.2.2 | [Tradeoff Pydantic — Separação Estrita vs. Pragmatismo](#1222-tradeoff-pydantic--separação-estrita-vs-pragmatismo) |
| 12.2.3 | [ADR — Documentando Decisões Arquiteturais](#1223-adr--documentando-decisões-arquiteturais) |
| 12.3 | [Arquiteturas Orientadas a Eventos](#123-arquiteturas-orientadas-a-eventos) |
| 12.3.1 | [Domain Events como Cidadãos de Primeira Classe](#1231-domain-events-como-cidadãos-de-primeira-classe) |
| 12.3.2 | [Anti-pattern: Entidade Publicando Eventos Diretamente](#1232-anti-pattern-entidade-publicando-eventos-diretamente) |
| 12.3.3 | [Padrão Limpo: Use Case como Publisher](#1233-padrão-limpo-use-case-como-publisher) |
| 12.4 | [Liderança Arquitetural](#124-liderança-arquitetural) |
| 12.4.1 | [Traduzindo Benefícios Técnicos para Valor de Negócio](#1241-traduzindo-benefícios-técnicos-para-valor-de-negócio) |
| 12.4.2 | [Padrões de Resistência e Respostas](#1242-padrões-de-resistência-e-respostas) |
| 12.4.3 | [Comunidades de Prática](#1243-comunidades-de-prática) |

---

## Capítulo 1 — Clean Architecture Essentials: Transforming Python Development

### 1.1 Dependency Rule

A regra fundamental de Clean Architecture: dependências de código-fonte devem apontar **somente para dentro**, em direção a políticas de maior nível.

- Camadas internas **não conhecem** camadas externas.
- Camadas externas **dependem e se adaptam** às camadas internas.
- Mudanças em detalhes externos (banco de dados, UI, frameworks) não afetam a lógica de negócio central.

**Regra**: Nunca importe de uma camada externa dentro de uma camada interna; a dependência deve sempre apontar para o centro.

---

### 1.2 As Quatro Camadas (Onion Architecture)

Clean Architecture se organiza em círculos concêntricos; dependências fluem apenas para dentro:

#### 1.2.1 Entities (núcleo)

Objetos de negócio fundamentais que existiriam mesmo sem software. Encapsulam regras de negócio enterprise-wide. Sem dependências de camadas externas.

#### 1.2.2 Use Cases

Orquestram o fluxo de dados de/para Entities. Representam como o sistema é utilizado para um cenário específico (ex.: `CreateTask`, `CompleteTask`). Contêm regras de negócio específicas da aplicação.

#### 1.2.3 Interface Adapters

Tradutores entre Use Cases e agências externas. Inclui controllers (HTTP), presenters (formatação para exibição) e gateways (transformação para persistência). Permite desacoplar de frameworks.

#### 1.2.4 Frameworks and Drivers (camada mais externa)

Ferramentas, frameworks e mecanismos de entrega que rodam o sistema, mas não são centrais à lógica de negócio. Ex.: Django, Flask, psycopg2, smtplib. Camada mais volátil — tecnologias mudam aqui sem afetar o núcleo.

**Regra**: Nunca coloque lógica de negócio na camada de Frameworks and Drivers.

> ⚠ Evite: Importar frameworks (Django ORM, SQLAlchemy models, Flask) dentro de Entities ou Use Cases.

---

### 1.3 Separation of Concerns (SoC)

**Regra**: Mantenha juntos os elementos que mudam pelo mesmo motivo; separe os que mudam por motivos diferentes.

A arquitetura deve ser a primeira decisão: determinar como dividir o sistema antes de escolher tecnologias.

> 💡 Nota: SoC é o mecanismo que permite trocar um framework por outro sem reescrever a lógica de negócio.

---

### 1.4 Benefits of Clean Architecture

| Benefício | Descrição |
|---|---|
| **Testabilidade** | Lógica de negócio testável sem subir banco de dados ou servidor web |
| **Flexibilidade tecnológica** | Troca de framework ou banco sem alterar Use Cases/Entities |
| **Agility de longo prazo** | Codebase mais fácil de entender e modificar à medida que cresce |
| **Documentação viva** | Estrutura de diretórios revela propósito do sistema, não suas ferramentas |

---

### 1.5 Screaming Architecture

**Regra**: Ao olhar para a estrutura do projeto, ela deve "gritar" seu propósito (ex.: "loja online"), não seu framework (ex.: "aplicação Django").

A arquitetura é uma forma de documentação: novos membros do time devem conseguir identificar as Use Cases do sistema apenas pela estrutura de arquivos/módulos.

---

### 1.6 Implementando em Python: ABCs

Use `abc.ABC` e `@abstractmethod` para definir interfaces nas camadas internas e forçar implementação nas camadas externas.

```python
from abc import ABC, abstractmethod

class Notifier(ABC):                   # camada interna — interface
    @abstractmethod
    def send_notification(self, message: str) -> None:
        pass

class EmailNotifier(Notifier):         # camada externa — implementação
    def send_notification(self, message: str) -> None:
        print(f"Sending email: {message}")

class NotificationService:             # depende da abstração, não da implementação
    def __init__(self, notifier: Notifier):
        self.notifier = notifier

    def notify(self, message: str) -> None:
        self.notifier.send_notification(message)
```

**Regra**: Use `Notifier` (ABC) como tipo nas assinaturas de Use Cases/Services; nunca referencie `EmailNotifier` ou `SMSNotifier` diretamente no núcleo.

---

### 1.7 Implementando em Python: Protocols

Python 3.8+ oferece `typing.Protocol` para structural subtyping: o objeto satisfaz a interface por ter os métodos corretos, sem herança explícita (duck typing com type hinting).

```python
from typing import Protocol

class Notifier(Protocol):              # interface estrutural — sem herança obrigatória
    def send_notification(self, message: str) -> None: ...

class SMSNotifier:                     # não herda de Notifier, mas satisfaz o protocolo
    def send_notification(self, message: str) -> None:
        print(f"Sending SMS: {message}")

class NotificationService:
    def __init__(self, notifier: Notifier):  # type hint ainda funciona
        self.notifier = notifier
```

**Regra**: Prefira Protocols quando quiser duck typing com type safety e evitar hierarquias de classe rígidas. Prefira ABCs quando o codebase já tem tradição de herança explícita.

> 💡 Nota: O livro usa ABCs nos exemplos por maior prevalência em codebases existentes, mas os princípios são idênticos com Protocols.

---

### 1.8 Considerações Python-específicas

#### 1.8.1 Abstrações sobre stdlib

**Regra**: Não use `smtplib`, `logging`, ou outras bibliotecas padrão diretamente em Use Cases. Crie uma abstração (ABC ou Protocol) e injete a implementação.

> ⚠ Evite: `import smtplib` dentro de um Use Case — isso cria dependência implícita de detalhe de infraestrutura.

#### 1.8.2 Manter a Dependency Rule

Python não tem modificadores de acesso; todos os pacotes são efetivamente públicos. A Dependency Rule deve ser mantida por disciplina e, idealmente, por ferramentas de lint (ex.: `import-linter`).

#### 1.8.3 Escala progressiva

Clean Architecture é um espectro, não uma escolha binária:

1. Projetos pequenos: separar lógica de negócio (`models.py`) de apresentação (`views.py`) e usar DI básica já aplica os princípios.
2. Projetos médios: introduzir módulos separados para Entities e Use Cases.
3. Projetos grandes: estrutura completa com todas as quatro camadas em diretórios dedicados.

**Regra**: Aplique somente os padrões que ofereçam valor claro para o tamanho e contexto do projeto. Evite over-engineering em projetos pequenos.

---

## Capítulo 2 — SOLID Foundations: Building Robust Python Applications

Os princípios SOLID operam principalmente ao nível de módulo e formam a fundação para a Clean Architecture. Aplicados corretamente, produzem componentes fracamente acoplados e altamente coesos, que são mais fáceis de testar, modificar e estender.

### 2.1 SRP — Single Responsibility Principle

Cada módulo de software deve ter **uma e somente uma razão para mudar**. SRP não significa "fazer apenas uma coisa", mas ter uma única fonte de mudança.

#### 2.1.1 Identificando e separando responsabilidades

Sinais de violação:
- Grupos de métodos operam sobre subconjuntos diferentes dos dados da classe
- A classe tem mais de uma razão para mudar

Refatoração: separar `User` (entidade pura) de serviços de aplicação:

```python
class User:                        # entidade: gerencia apenas dados de usuário
    def __init__(self, user_id: str, username: str, email: str):
        self.user_id = user_id
        self.username = username
        self.email = email

class PostManager:                 # responsabilidade: criar e gerenciar posts
    def create_post(self, user: User, content: str):
        post = {"id": self.generate_post_id(), "user_id": user.user_id,
                "content": content, "likes": 0}
        return post
    def generate_post_id(self): pass

class TimelineService:             # responsabilidade: lógica de timeline
    def get_timeline(self, user: User) -> list: pass

class ProfileManager:              # responsabilidade: atualizações de perfil
    def update_profile(self, user: User, new_username: str = None, new_email: str = None):
        if new_username:
            user.username = new_username
        if new_email:
            user.email = new_email
```

**Regra**: Separe classes quando puder identificar mais de uma razão independente para elas mudarem.

> ⚠ Evite: Entidades com métodos de aplicação embutidos (ex.: `User.create_post`, `User.get_timeline`) — viola SRP e o conceito de entidade da Clean Architecture.

#### 2.1.2 SRP e testabilidade

Classes com responsabilidade única têm menos dependências e casos de borda; o teste é direto e sem setup complexo.

**Regra**: Se um teste requer mocks extensos ou setup complexo, provavelmente a classe viola SRP.

#### 2.1.3 Equilibrando SRP

> 💡 Nota: Over-aplicar SRP gera explosão de classes minúsculas, tornando o sistema mais difícil de entender. O princípio é sobre razões de mudança, não sobre número de ações executadas.

---

### 2.2 OCP — Open-Closed Principle

Software deve ser **aberto para extensão, fechado para modificação**: adicionar comportamento novo via código novo, sem alterar código existente. Implementado em Python via classes abstratas e polimorfismo.

```python
from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self): pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi * self.radius ** 2

class AreaCalculator:
    def calculate_area(self, shape: Shape):
        return shape.area()          # nunca precisa ser modificado

# Nova forma adicionada sem tocar em AreaCalculator:
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    def area(self):
        return 0.5 * self.base * self.height
```

**Regra**: Módulos centrais devem depender de abstrações. Novas variantes implementam a abstração; o módulo central permanece fechado à modificação.

> ⚠ Evite: `isinstance()` em cadeia dentro de funções centrais para desviar comportamento por tipo concreto — viola OCP.

---

### 2.3 ISP — Interface Segregation Principle

Interfaces devem ser **estreitas e específicas para cada cliente**; nenhuma classe deve ser forçada a implementar métodos que não usa.

```python
from abc import ABC, abstractmethod

class MediaPlayable(ABC):
    @abstractmethod
    def play_media(self, file: str) -> None: pass
    @abstractmethod
    def stop_media(self) -> None: pass

class LyricsDisplayable(ABC):
    @abstractmethod
    def display_lyrics(self, file: str) -> None: pass

class VideoFilterable(ABC):
    @abstractmethod
    def apply_video_filter(self, filter: str) -> None: pass

class MusicPlayer(MediaPlayable, LyricsDisplayable):
    def play_media(self, file: str) -> None: ...
    def stop_media(self) -> None: ...
    def display_lyrics(self, file: str) -> None: ...

class VideoPlayer(MediaPlayable, VideoFilterable):
    def play_media(self, file: str) -> None: ...
    def stop_media(self) -> None: ...
    def apply_video_filter(self, filter: str) -> None: ...

class BasicAudioPlayer(MediaPlayable):
    def play_media(self, file: str) -> None: ...
    def stop_media(self) -> None: ...
```

**Regra**: Prefira múltiplas interfaces estreitas a uma interface ampla; clientes implementam apenas as interfaces relevantes à sua funcionalidade.

> ⚠ Evite: Métodos com `raise NotImplementedError` em classes concretas — sinal de que a interface é larga demais (violação de ISP).

---

### 2.4 LSP — Liskov Substitution Principle

Qualquer subclasse deve poder **substituir sua classe base sem quebrar o programa ou violar o contrato** estabelecido pela base. Subclasses podem estender o contrato, mas não reduzi-lo ou alterá-lo.

Antipadrão — herança is-a incorreta:

```python
class Vehicle:
    def consume_fuel(self, distance: float) -> None:
        fuel_consumed = distance / 10
        self._fuel_level -= fuel_consumed

class ElectricCar(Vehicle):        # viola LSP: muda a semântica de "fuel"
    def consume_fuel(self, distance: float) -> None:
        energy_consumed = distance / 5
        self._fuel_level -= energy_consumed
```

Correção — composição com abstração:

```python
from abc import ABC, abstractmethod

class PowerSource(ABC):
    def __init__(self, capacity: float):
        self._capacity = capacity
        self._level = capacity
    def level(self) -> float:
        return self._level
    @abstractmethod
    def consume(self, distance: float) -> float: pass

class FuelTank(PowerSource):
    def consume(self, distance: float) -> float:
        fuel_consumed = distance / 10
        if self._level - fuel_consumed < 0:
            raise ValueError("Not enough fuel")
        self._level -= fuel_consumed
        return fuel_consumed

class Battery(PowerSource):
    def consume(self, distance: float) -> float:
        energy_consumed = distance / 5
        if self._level - energy_consumed < 0:
            raise ValueError("Not enough charge")
        self._level -= energy_consumed
        return energy_consumed

class Vehicle:
    def __init__(self, power_source: PowerSource):
        self._power_source = power_source
    def power_level(self) -> float:
        return self._power_source.level()
    def drive(self, distance: float) -> float:
        return self._power_source.consume(distance)
```

**Regra**: Quando uma subclasse não pode honrar o contrato da base sem alterar a semântica dos métodos, use composição em vez de herança.

> ⚠ Evite: Modelar relacionamentos is-a literais quando o comportamento subjacente é fundamentalmente diferente — resulta em designs frágeis com saídas incorretas silenciosas.

---

### 2.5 DIP — Dependency Inversion Principle

**Módulos de alto nível não devem depender de módulos de baixo nível. Ambos devem depender de abstrações.** A inversão essencial: o **módulo de alto nível define a abstração**; módulos de baixo nível a implementam.

Antipadrão:

```python
class UserEntity:
    def __init__(self, user_id: str):
        self.database = MySQLDatabase()    # dependência direta — violação de DIP
    def save(self):
        self.database.insert("users", {"id": self.user_id})
```

Correção com Dependency Injection via construtor:

```python
from abc import ABC, abstractmethod

class DatabaseInterface(ABC):              # abstração definida pelo módulo de alto nível
    @abstractmethod
    def insert(self, table: str, data: dict): pass

class UserEntity:
    def __init__(self, user_id: str, database: DatabaseInterface):
        self.user_id = user_id
        self.database = database           # injeta abstração, não implementação
    def save(self):
        self.database.insert("users", {"id": self.user_id})

class MySQLDatabase(DatabaseInterface):
    def insert(self, table: str, data: dict):
        print(f"Inserting {data} into {table} table in MySQL")

class PostgreSQLDatabase(DatabaseInterface):
    def insert(self, table: str, data: dict):
        print(f"Inserting {data} into {table} table in PostgreSQL")
```

**Regra**: Injete dependências via construtor (ou outro ponto de injeção explícito). Nunca instancie implementações concretas dentro de módulos de alto nível.

#### 2.5.1 DIP e testabilidade

```python
class MockDatabase(DatabaseInterface):
    def __init__(self):
        self.inserted_data = []
    def insert(self, table: str, data: dict):
        self.inserted_data.append((table, data))

mock_db = MockDatabase()
user = UserEntity("test_user", mock_db)
user.save()
assert mock_db.inserted_data == [("users", {"id": "test_user"})]
```

**Regra**: Se um módulo de alto nível é difícil de testar sem infraestrutura real, provavelmente viola DIP.

#### 2.5.2 DIP na Clean Architecture

DIP é o mecanismo concreto para implementar a Dependency Rule: camadas internas definem interfaces (abstrações); camadas externas as implementam. A direção das abstrações sempre aponta para dentro.

---

## Capítulo 3 — Type-Enhanced Python: Strengthening Clean Architecture

### 3.1 Type Hinting como Ferramenta Arquitetural

Type hints são metadados opcionais introduzidos via PEP 484 (Python 3.5). Não alteram o comportamento em runtime, mas tornam interfaces e dependências explícitas, habilitando análise estática.

Benefícios em contexto de Clean Architecture:
- **Interfaces claras**: contratos explícitos entre camadas documentados no código
- **Dependency inversion**: tipos abstratos (ABC/Protocol) anotados nas assinaturas forçam dependência de abstrações
- **Testabilidade**: hints facilitam criação de mocks conformes à interface esperada
- **Manutenibilidade**: documentação viva que não desatualiza como comentários

**Regra**: Anote parâmetros e retornos em todos os limites entre camadas arquiteturais para tornar contratos explícitos e detectáveis por ferramentas estáticas.

> ⚠ Evite: `Any` dentro do próprio código — sua presença sinaliza necessidade de refatoração para tipos específicos.

---

### 3.2 Leveraging Python's Typing System

#### 3.2.1 Basic Type Hinting

```python
def process_order(items: list[str], quantities: list[int]) -> dict[str, int]:
    return {item: quantity for item, quantity in zip(items, quantities)}
```

> 💡 Nota: Python 3.9+ suporta `list[str]` diretamente; Python < 3.9 requer `from typing import List` e `List[str]`.

#### 3.2.2 Sequence — Flexibilidade em Coleções

`Sequence[T]` aceita qualquer tipo sequencial (list, tuple, custom) sem comprometer LSP ou OCP.

```python
from typing import Sequence

def calculate_total(items: Sequence[float]) -> float:
    return sum(items)

calculate_total([1.0, 2.0, 3.0])   # Works with list
calculate_total((4.0, 5.0, 6.0))   # Works with tuple
```

**Regra**: Prefira `Sequence[T]` a `list[T]` em assinaturas quando não precisar de mutabilidade — permite qualquer sequência sem violar LSP.

#### 3.2.3 Union e Optional

`Union[A, B]` (ou `A | B` em Python 3.10+) e `Optional[A]` (atalho para `Union[A, None]`) modelam valores com múltiplos tipos possíveis em limites de camada.

```python
from typing import Union, Optional

def process_input(data: Union[str, int]) -> str:
    return str(data)

def find_user(user_id: Optional[int] = None) -> Optional[str]:
    if user_id is None:
        return None
    return "User found"

# Python 3.10+ syntax:
def process_input_v2(data: str | int) -> str:
    return str(data)
```

#### 3.2.4 Literal Types

`Literal` restringe um parâmetro a um conjunto fixo de valores — checkers estáticos detectam valores inválidos antes do runtime.

```python
from typing import Literal

LogLevel = Literal["DEBUG", "INFO", "WARNING", "ERROR"]

def set_log_level(level: LogLevel) -> None:
    print(f"Setting log level to {level}")

set_log_level("DEBUG")     # válido
set_log_level("CRITICAL")  # type checker flageia como erro
```

**Regra**: Use `Literal` em parâmetros que aceitam apenas valores específicos (status, log levels, flags de configuração) — erros de valor são detectados em análise estática, não em runtime.

#### 3.2.5 Type Aliases

Type aliases simplificam anotações complexas e melhoram a legibilidade sem criar novos tipos.

```python
UserDict = dict[str, str]
UserList = list[UserDict]

def process_users(users: UserList) -> None:
    for user in users:
        print(f"Processing user: {user['name']}")
```

#### 3.2.6 NewType

`NewType` cria tipos nominalmente distintos — previne mistura acidental de valores semanticamente diferentes com o mesmo tipo primitivo.

```python
from typing import NewType

UserId = NewType('UserId', int)
ProductId = NewType('ProductId', int)

def process_order(user_id: UserId, product_id: ProductId) -> None:
    print(f"Processing order for User {user_id} and Product {product_id}")

user_id = UserId(1)
product_id = ProductId(1)
process_order(user_id, product_id)   # correto
# process_order(product_id, user_id) # type error: tipos trocados
```

**Regra**: Use `NewType` para IDs e conceitos de domínio que compartilham o mesmo tipo primitivo mas têm semântica diferente — previne erros silenciosos de mistura de valores.

---

### 3.3 Automated Static Type-Checking Tools

#### 3.3.1 mypy CLI

```bash
pip install mypy
mypy user_service.py
# user_service.py:9: error: Argument 1 to "get_user" has incompatible type "str"; expected "int"  [arg-type]
```

mypy reporta arquivo, linha e categoria do erro. Sem erros: `Success: no issues found`.

#### 3.3.2 Configurando mypy

```ini
# mypy.ini (na raiz do projeto)
[mypy]
ignore_missing_imports = True
strict_optional = True
warn_redundant_casts = True
warn_unused_ignores = True
warn_return_any = True
warn_unreachable = True
```

Para adoção gradual — ignorar módulos legados:

```ini
[mypy.legacy_module]
ignore_errors = True

[mypy.some_package.*]
ignore_errors = True
```

#### 3.3.3 mypy em Pipelines CI/CD

```yaml
# GitHub Actions
name: Python Type Check and Test
on: [push, pull_request]
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2
    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: '3.13'
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install mypy pytest
    - name: Run mypy
      run: mypy .
    - name: Run tests
      run: pytest
```

**Regra**: Execute mypy em todo push, em validação de PRs, antes de merges na branch principal e antes de deploys para staging/produção.

#### 3.3.4 IDE: Pylance no VS Code

Pylance (motor: pyright) provê feedback em tempo real de erros de tipo enquanto o código é escrito. Instalar via VS Code Marketplace.

**Regra**: Configure Pylance + VS Code Problems tab como primeira linha de detecção — erros são corrigidos no momento da escrita, não na revisão de PR.

#### 3.3.5 Estratégia de Adoção Gradual

1. Reunir o time para formular plano de adoção
2. Exigir type hints para todo código novo
3. Configurar mypy para ignorar módulos legados via `[mypy.module]` `ignore_errors = True`
4. Criar tarefas de manutenção progressiva para adicionar hints ao código existente, priorizando caminhos críticos

---

## Capítulo 4 — Domain-Driven Design: Crafting the Core Business Logic

### 4.1 DDD: Conceitos Fundamentais

DDD fornece os padrões táticos para implementar o Domain layer da Clean Architecture. Os componentes DDD populam a camada mais interna:

| Componente | Definição |
|---|---|
| **Entity** | Objeto definido por identidade persistente — permanece o mesmo mesmo que atributos mudem |
| **Value Object** | Objeto imutável definido por atributos, não por identidade — dois objetos com mesmos atributos são iguais |
| **Domain Service** | Operação stateless que envolve múltiplas entidades ou lógica que não pertence a uma única entidade |
| **Bounded Context** | Fronteira conceitual onde um modelo de domínio específico se aplica; contextos interagem via interfaces bem definidas |
| **Ubiquitous Language** | Vocabulário compartilhado entre desenvolvedores e especialistas de domínio, usado consistentemente no código, testes e conversas |

**Regra**: Analise os requisitos de negócio e defina a ubiquitous language **antes** de escrever qualquer código. Modele o domínio completamente antes de implementar.

> ⚠ Evite: Iniciar a implementação antes de compreender as regras de negócio — resulta em modelos frágeis que não refletem a realidade do domínio.

---

### 4.2 Implementando Entidades em Python

#### 4.2.1 Entity Base Class com dataclass

Use `@dataclass` com UUID gerado automaticamente como identidade. Implemente `__eq__` por ID (não por atributos) e `__hash__` baseado no ID.

```python
from dataclasses import dataclass, field
from uuid import UUID, uuid4

@dataclass
class Entity:
    id: UUID = field(default_factory=uuid4, init=False)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, type(self)):
            return NotImplemented
        return self.id == other.id

    def __hash__(self) -> int:
        return hash(self.id)
```

**Regra**: Nunca compare entidades por atributos — identidade é sempre pelo ID. Duas entidades com os mesmos atributos mas IDs diferentes são entidades distintas.

#### 4.2.2 Value Objects com frozen dataclass e Enum

Value objects são imutáveis: use `@dataclass(frozen=True)` ou `Enum`. Encapsule comportamentos de domínio dentro deles.

```python
from enum import Enum
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone

class TaskStatus(Enum):
    TODO = "TODO"
    IN_PROGRESS = "IN_PROGRESS"
    DONE = "DONE"

class Priority(Enum):
    LOW = 1
    MEDIUM = 2
    HIGH = 3

@dataclass(frozen=True)
class Deadline:
    due_date: datetime

    def __post_init__(self):
        if self.due_date < datetime.now(timezone.utc):
            raise ValueError("Deadline cannot be in the past")

    def is_overdue(self) -> bool:
        return datetime.now(timezone.utc) > self.due_date

    def time_remaining(self) -> timedelta:
        return max(timedelta(0), self.due_date - datetime.now(timezone.utc))

    def is_approaching(self, warning_threshold: timedelta = timedelta(days=1)) -> bool:
        return timedelta(0) < self.time_remaining() <= warning_threshold
```

**Regra**: Use value objects no lugar de primitivos (`str`, `int`) para conceitos de domínio — previne primitive obsession e adiciona type safety e comportamento.

> ⚠ Evite: `task.status = "Finished"` com strings brutas — use `TaskStatus.DONE`; strings permitem valores inválidos e comparações case-sensitive.

#### 4.2.3 Encapsulando Regras de Negócio na Entidade

Regras que se aplicam diretamente à entidade (invariants) devem ser métodos da própria entidade.

```python
from dataclasses import dataclass, field
from typing import Optional

@dataclass
class Task(Entity):
    title: str
    description: str
    due_date: Optional[Deadline] = None
    priority: Priority = Priority.MEDIUM
    status: TaskStatus = field(default=TaskStatus.TODO, init=False)

    def start(self) -> None:
        if self.status != TaskStatus.TODO:
            raise ValueError("Only tasks with 'TODO' status can be started")
        self.status = TaskStatus.IN_PROGRESS

    def complete(self) -> None:
        if self.status == TaskStatus.DONE:
            raise ValueError("Task is already completed")
        self.status = TaskStatus.DONE

    def is_overdue(self) -> bool:
        return self.due_date is not None and self.due_date.is_overdue()
```

**Regra**: Encapsule na entidade somente regras que envolvem exclusivamente seus próprios atributos. Regras que envolvem múltiplas entidades ou dados externos pertencem a domain services ou use cases.

#### 4.2.4 Domain Services

Operações stateless que não pertencem a uma única entidade são implementadas como domain services.

```python
class TaskPriorityCalculator:
    @staticmethod
    def calculate_priority(task: Task) -> Priority:
        if task.is_overdue():
            return Priority.HIGH
        elif task.due_date and task.due_date.time_remaining() <= timedelta(days=2):
            return Priority.MEDIUM
        else:
            return Priority.LOW
```

**Regra**: Domain services são stateless; não guardam estado entre chamadas. Se a lógica envolve múltiplos objetos de domínio, coloque-a em um domain service, não em nenhuma das entidades envolvidas.

---

### 4.3 Aggregates e Factory Pattern

#### 4.3.1 Aggregate

Um aggregate é um cluster de objetos de domínio tratado como uma única unidade para mudanças de dados. O **aggregate root** é a única entidade do cluster acessível externamente.

```python
from dataclasses import dataclass, field
from typing import Optional
from uuid import UUID

@dataclass
class Project(Entity):
    name: str
    description: str = ""
    _tasks: dict[UUID, Task] = field(default_factory=dict, init=False)

    def add_task(self, task: Task) -> None:
        self._tasks[task.id] = task

    def remove_task(self, task_id: UUID) -> None:
        self._tasks.pop(task_id, None)

    def get_task(self, task_id: UUID) -> Optional[Task]:
        return self._tasks.get(task_id)

    @property
    def tasks(self) -> list[Task]:
        return list(self._tasks.values())
```

**Regra**: Toda operação que afeta múltiplos objetos dentro do aggregate deve passar pelo aggregate root — nunca modifique membros internos diretamente do código externo.

> 💡 Nota: Aggregates devem ser o menor possível enquanto ainda mantêm consistência. Aggregates muito grandes exigem paginação ou lazy loading.

#### 4.3.2 Factory Pattern em Python

Em Python, `@dataclass` já gera `__init__` suficiente para criação simples. Use alternativas idiomáticas antes de criar uma factory standalone:

- **Class method como construtor alternativo** — para criar objetos com configurações predefinidas:

```python
@dataclass
class Task(Entity):
    # ... atributos ...

    @classmethod
    def create_urgent_task(cls, title: str, description: str, due_date: Deadline):
        return cls(title, description, due_date, Priority.HIGH)
```

- **`__post_init__`** — para validação complexa na criação:

```python
    def __post_init__(self):
        if not self.title.strip():
            raise ValueError("Task title cannot be empty")
        if len(self.description) > 500:
            raise ValueError("Task description cannot exceed 500 characters")
```

- **Standalone factory** — use quando há: grafo complexo de objetos, injeção de dependências externas, ou criação polimórfica baseada em condições de runtime:

```python
class TaskFactory:
    def __init__(self, user_service, project_repository):
        self.user_service = user_service
        self.project_repository = project_repository

    def create_task_in_project(self, title: str, description: str,
                               project_id: UUID, assignee_id: UUID) -> Task:
        project = self.project_repository.get_by_id(project_id)
        assignee = self.user_service.get_user(assignee_id)
        task = Task(title, description)
        task.project = project
        task.assignee = assignee
        if project.is_high_priority() and assignee.is_manager():
            task.priority = Priority.HIGH
        project.add_task(task)
        return task
```

---

### 4.4 Independência do Domain Layer

#### 4.4.1 Abstract Repository no Domain Layer

O Domain layer define a **interface** de persistência; camadas externas implementam. A abstração pertence ao domínio — não à infraestrutura.

```python
# todo_app/domain/repositories/task_repository.py
from abc import ABC, abstractmethod

class TaskRepository(ABC):
    @abstractmethod
    def save(self, task: Task): pass

    @abstractmethod
    def get(self, task_id: str) -> Task: pass
```

```python
# todo_app/domain/services/task_service.py
class TaskService:
    def __init__(self, task_repository: TaskRepository):
        self.task_repository = task_repository

    def create_task(self, title: str, description: str) -> Task:
        task = Task(title, description)
        self.task_repository.save(task)
        return task

    def mark_task_as_complete(self, task_id: str) -> Task:
        task = self.task_repository.get(task_id)
        task.complete()
        self.task_repository.save(task)
        return task
```

```python
# infrastructure/persistence/sqlite_task_repository.py
class SQLiteTaskRepository(TaskRepository):
    def __init__(self, db_connection):
        self.db = db_connection

    def save(self, task: Task): ...
    def get(self, task_id: str) -> Task: ...
```

**Regra**: A direção de dependência é sempre para dentro: Infrastructure depende da abstração do Domain; Domain não conhece Infrastructure. Para trocar SQLite por PostgreSQL, crie `PostgreSQLTaskRepository` — o Domain layer não muda.

> ⚠ Evite (antipadrões de violação da Dependency Rule):
> - `db: DbConnection` como atributo de uma entidade
> - `ui: UiComponent` injetado em um aggregate
> - `self.db.update(self)` chamado dentro de um método de entidade

#### 4.4.2 Refatorando para Pureza de Domínio

Remova efeitos colaterais (envio de email, notificações) de entidades; use abstrações no Domain layer, com implementações em camadas externas.

```python
# Antes — viola SRP e domain purity
class Task(Entity):
    def mark_as_complete(self):
        self.status = TaskStatus.DONE
        self.send_completion_email()  # efeito colateral no domínio

# Depois — entidade pura + abstração de notificação
class Task(Entity):
    def mark_as_complete(self):
        self.status = TaskStatus.DONE  # apenas estado de domínio

class TaskCompleteNotifier(ABC):
    @abstractmethod
    def notify_completion(self, task): pass

# Implementado na camada externa:
class EmailTaskCompleteNotifier(TaskCompleteNotifier):
    def notify_completion(self, task):
        print(f"Sending email: Task '{task.title}' has been completed.")
```

**Regra**: Entidades não enviam emails, não atualizam UI, não fazem logging de infraestrutura. Qualquer efeito colateral externo deve ser movido para uma abstração no domínio e implementado em camada externa.

#### 4.4.3 Estratégias de Manutenção da Pureza

1. Revisar código regularmente com foco em violações da Dependency Rule
2. Refatorar continuamente à medida que o entendimento do domínio evolui
3. Resistir ao uso de features de framework dentro do Domain layer
4. Preferir explicitness: tornar dependências e comportamentos explícitos no código
5. Usar padrões DDD (entities, value objects, aggregates) para manter o foco do domínio

---

## Capítulo 5 — The Application Layer: Orchestrating Use Cases

### 5.1 Papel da Application Layer

A Application layer é uma camada fina que coordena objetos de domínio e serviços externos para executar use cases concretos. Atua como mediador entre o Domain layer e as camadas externas, mantendo a Dependency Rule.

Responsabilidades:

| Responsabilidade | Descrição |
|---|---|
| **Use case orchestration** | Coordena objetos de domínio, gerencia sequência de operações, garante aplicação das regras de negócio |
| **Error handling/validation** | Valida input antes de chegar ao domínio; captura e traduz erros de domínio em respostas consistentes |
| **Transaction management** | Garante atomicidade de operações; gerencia rollbacks em caso de falha |
| **Boundary translation** | Converte formatos externos em formatos de domínio e vice-versa |

**Regra**: A Application layer esconde detalhes de infraestrutura do domínio e complexidades de domínio das interfaces externas. Exponha apenas o necessário por interfaces cuidadosamente projetadas.

> ⚠ Evite: `except Exception:` genérico junto com erros de domínio esperados — o tratamento global de erros pertence às camadas externas, não à Application layer.

---

### 5.2 Error Handling com Result Types

Em vez de depender exclusivamente de exceções, use o padrão Result: encapsule sucesso ou falha em um objeto tipado, tornando ambos os caminhos explícitos na assinatura da função.

```python
from enum import Enum
from dataclasses import dataclass
from typing import Optional, Any
from typing import Self

class ErrorCode(Enum):
    NOT_FOUND = "NOT_FOUND"
    VALIDATION_ERROR = "VALIDATION_ERROR"

@dataclass(frozen=True)
class Error:
    code: ErrorCode
    message: str
    details: Optional[dict[str, Any]] = None

    @classmethod
    def not_found(cls, entity: str, entity_id: str) -> Self:
        return cls(code=ErrorCode.NOT_FOUND,
                   message=f"{entity} with id {entity_id} not found")

    @classmethod
    def validation_error(cls, message: str) -> Self:
        return cls(code=ErrorCode.VALIDATION_ERROR, message=message)

@dataclass(frozen=True)
class Result:
    value: Any = None
    error: Optional[Error] = None

    @property
    def is_success(self) -> bool:
        return self.error is None

    @classmethod
    def success(cls, value: Any) -> Self:
        return cls(value=value)

    @classmethod
    def failure(cls, error: Error) -> Self:
        return cls(error=error)
```

Uso dentro de um use case:

```python
try:
    project = find_project(project_id)
    task = create_task(task_details)
    project.add_task(task)
    notify_stakeholders(task)
    return Result.success(TaskResponse.from_entity(task))
except ProjectNotFoundError:
    return Result.failure(Error.not_found("Project", str(project_id)))
except ValidationError as e:
    return Result.failure(Error.validation_error(str(e)))
```

**Regra**: Use Result como tipo de retorno de todos os use cases; captura apenas erros de domínio esperados. Erros inesperados propagam naturalmente para as camadas externas.

---

### 5.3 Implementando Use Case Interactors

#### 5.3.1 Estrutura de um Use Case

Use `@dataclass(frozen=True)` para o use case; injete dependências como atributos; exponha um único método público `execute` que retorna `Result`.

```python
from dataclasses import dataclass
from typing import Optional
from uuid import UUID

@dataclass(frozen=True)
class CompleteTaskUseCase:
    task_repository: TaskRepository

    def execute(self, task_id: UUID, completion_notes: Optional[str] = None) -> Result:
        try:
            task = self.task_repository.get(task_id)
            task.complete(notes=completion_notes)
            self.task_repository.save(task)
            return Result.success({
                "id": str(task.id),
                "status": "completed",
                "completion_date": task.completed_at.isoformat()
            })
        except TaskNotFoundError:
            return Result.failure(Error.not_found("Task", str(task_id)))
        except ValidationError as e:
            return Result.failure(Error.validation_error(str(e)))
```

**Regra**: Um use case implementa uma única operação de negócio. Injete dependências pelo construtor; nunca instancie implementações concretas dentro do use case.

#### 5.3.2 Interfaces Definidas pela Application Layer

A Application layer define suas próprias interfaces (ABCs) para repositórios e serviços. Camadas externas as implementam.

```python
from abc import ABC, abstractmethod

class TaskRepository(ABC):
    @abstractmethod
    def get(self, task_id: UUID) -> Task: pass

    @abstractmethod
    def save(self, task: Task) -> None: pass

    @abstractmethod
    def delete(self, task_id: UUID) -> None: pass

class NotificationService(ABC):
    @abstractmethod
    def notify_task_assigned(self, task_id: UUID) -> None: pass

    @abstractmethod
    def notify_task_completed(self, task: Task) -> None: pass
```

Implementação concreta (camada externa):

```python
class MongoDbTaskRepository(TaskRepository):
    def __init__(self, client: MongoClient):
        self.tasks = client.task_management.tasks

    def get(self, task_id: UUID) -> Task:
        document = self.tasks.find_one({"_id": str(task_id)})
        if not document:
            raise TaskNotFoundError(task_id)
        # ... conversão document -> Task
```

**Regra**: Defina as interfaces de dependência na Application layer, não na camada de infraestrutura. A direção de controle pertence ao núcleo.

#### 5.3.3 Use Cases com Operações Complexas

Para operações que coordenam múltiplas entidades ou serviços, injete todos os repositórios e serviços necessários:

```python
@dataclass(frozen=True)
class CompleteProjectUseCase:
    project_repository: ProjectRepository
    task_repository: TaskRepository
    notification_service: NotificationService

    def execute(self, project_id: UUID, completion_notes: Optional[str] = None) -> Result:
        try:
            project = self.project_repository.get(project_id)
            for task in project.incomplete_tasks:
                task.complete()
                self.task_repository.save(task)
                self.notification_service.notify_task_completed(task)
            project.mark_completed(notes=completion_notes)
            self.project_repository.save(project)
            return Result.success({
                "id": str(project.id),
                "status": project.status,
                "completion_date": project.completed_at,
                "task_count": len(project.tasks),
                "completion_notes": project.completion_notes,
            })
        except ProjectNotFoundError:
            return Result.failure(Error.not_found("Project", str(project_id)))
        except ValidationError as e:
            return Result.failure(Error.validation_error(str(e)))
```

**Regra**: Múltiplas operações coordenadas dentro de um use case podem ser estendidas para suportar transacionalidade (salvar estado inicial e rollback em falha) sem alterar a interface pública.

---

### 5.4 Request e Response Models

#### 5.4.1 Request Models

Request models capturam e validam dados de entrada antes de chegar ao use case; convertem tipos externos (strings) em tipos de domínio (UUIDs).

```python
@dataclass(frozen=True)
class CompleteProjectRequest:
    project_id: str
    completion_notes: Optional[str] = None

    def __post_init__(self) -> None:
        if not self.project_id.strip():
            raise ValidationError("Project ID is required")
        if self.completion_notes and len(self.completion_notes) > 1000:
            raise ValidationError("Completion notes cannot exceed 1000 characters")

    def to_execution_params(self) -> dict:
        return {
            'project_id': UUID(self.project_id),
            'completion_notes': self.completion_notes
        }
```

**Regra**: Use `__post_init__` para validação e `to_execution_params` para conversão de tipos. O use case recebe dados já validados e nos tipos corretos do domínio.

#### 5.4.2 Response Models

Response models convertem entidades de domínio em estruturas adequadas para consumo externo, controlando o que é exposto e em que formato.

```python
@dataclass(frozen=True)
class CompleteProjectResponse:
    id: str
    status: str
    completion_date: str
    task_count: int
    completion_notes: Optional[str]

    @classmethod
    def from_entity(cls, project: Project) -> 'CompleteProjectResponse':
        return cls(
            id=str(project.id),
            status=project.status,
            completion_date=project.completed_at,
            task_count=len(project.tasks),
            completion_notes=project.completion_notes,
        )
```

Use case usando request e response models juntos:

```python
@dataclass(frozen=True)
class CompleteProjectUseCase:
    project_repository: ProjectRepository
    task_repository: TaskRepository
    notification_service: NotificationService

    def execute(self, request: CompleteProjectRequest) -> Result:
        try:
            params = request.to_execution_params()
            project = self.project_repository.get(params["project_id"])
            project.mark_completed(notes=params["completion_notes"])
            # ... demais operações
            self.project_repository.save(project)
            return Result.success(CompleteProjectResponse.from_entity(project))
        except ProjectNotFoundError:
            return Result.failure(Error.not_found("Project", str(params["project_id"])))
        except ValidationError as e:
            return Result.failure(Error.validation_error(str(e)))
```

**Regra**: Request models usam `to_execution_params` (inbound: externo → domínio); Response models usam `from_entity` (outbound: domínio → externo). O use case trabalha exclusivamente com tipos de domínio entre esses dois pontos.

> 💡 Nota: A camada de Interface Adapters pode transformar o response model para JSON (HTTP), texto (CLI) ou payload de fila sem alterar o use case.

---

### 5.5 Separação de Serviços Externos via Ports

#### 5.5.1 Ports — Interfaces de Capacidade

Ports são ABCs que definem exatamente as capacidades que a Application layer precisa de serviços externos, sem especificar implementação.

```python
class NotificationPort(ABC):
    @abstractmethod
    def notify_task_completed(self, task: Task) -> None: pass
```

Use case dependendo do port:

```python
@dataclass
class SetTaskPriorityUseCase:
    task_repository: TaskRepository
    notification_service: NotificationPort  # depende da interface, não da implementação

    def execute(self, request: SetTaskPriorityRequest) -> Result:
        try:
            params = request.to_execution_params()
            task = self.task_repository.get(params['task_id'])
            task.priority = params['priority']
            self.task_repository.save(task)
            if task.priority == Priority.HIGH:
                self.notification_service.notify_task_high_priority(task)
            return Result.success(TaskResponse.from_entity(task))
        except ValidationError as e:
            return Result.failure(Error.validation_error(str(e)))
```

**Regra**: Prefira `NotificationPort` (ABC definido pela Application layer) a `NotificationService` concreto. O use case não conhece se a notificação é email, SMS ou Slack.

#### 5.5.2 Adapter Pattern para Serviços de Terceiros

Quando um serviço externo tem interface diferente da esperada pelo port, crie um adapter:

```python
class ModernNotificationService:
    def send_notification(self, payload: dict) -> None: ...

class ModernNotificationAdapter(NotificationPort):
    def __init__(self, modern_service: ModernNotificationService):
        self._service = modern_service

    def notify_task_completed(self, task: Task) -> None:
        self._service.send_notification({
            "type": "TASK_COMPLETED",
            "taskId": str(task.id)
        })
```

**Regra**: Use o Adapter Pattern para integrar serviços de terceiros ou gerenciar upgrades de serviços sem modificar use cases existentes.

#### 5.5.3 Serviços Opcionais

Para integrações opcionais ou específicas de ambiente, use um dicionário de serviços opcionais com execução condicional:

```python
@dataclass(frozen=True)
class TaskManagementUseCase:
    task_repository: TaskRepository
    notification_service: NotificationPort
    _optional_services: dict[str, Any] = field(default_factory=dict)

    def register_service(self, name: str, service: Any) -> None:
        self._optional_services[name] = service

    def complete_task(self, task_id: UUID) -> Result:
        try:
            task = self.task_repository.get(task_id)
            task.complete()
            self.task_repository.save(task)
            self.notification_service.notify_task_completed(task)
            if analytics := self._optional_services.get('analytics'):
                analytics.track_task_completion(task.id)
            if audit := self._optional_services.get('audit'):
                audit.log_task_completion(task.id)
            return Result.success(TaskResponse.from_entity(task))
        except ValidationError as e:
            return Result.failure(Error.validation_error(str(e)))
```

**Regra**: Dependências core (repositórios, notification port) são explícitas no construtor; integrações opcionais ficam em `_optional_services` e são verificadas com o walrus operator antes de serem chamadas.

---

## Capítulo 6 — The Interface Adapters Layer: Controllers and Presenters

### 6.1 Papel da Interface Adapters Layer

A Interface Adapters layer é o conjunto de tradutores entre o núcleo da aplicação (Domain + Application layers) e as preocupações externas (web frameworks, CLI, filas de mensagens). Mantém a Dependency Rule garantindo que mudanças em interfaces externas não afetem a lógica de negócio.

Responsabilidades por fluxo:

| Fluxo | Responsabilidade |
|---|---|
| **Inbound** | Converter requests externos em formatos da Application layer; validar dados antes de chegarem aos use cases |
| **Outbound** | Transformar resultados dos use cases em formatos adequados para a interface consumidora |

Distinção entre Interface Adapters layer e Application layer:

| Aspecto | Application layer | Interface Adapters layer |
|---|---|---|
| Tipos usados | Domain-specific (entidades, VOs) | Interface-specific (primitivos, view models) |
| Foco | Coordenação de regras de negócio | Coordenação de interfaces externas |
| Transformação | Domínio ↔ use case formats | Use case formats ↔ formatos externos |

Componentes principais e fluxo de interação:
1. Requests externos chegam pelos **Controllers**
2. Controllers coordenam com **Use Cases**
3. Use cases retornam resultados por interfaces definidas
4. **Presenters** formatam resultados em **View Models**
5. Views consomem os dados formatados

Princípios de design de interface:
- **Dependency Rule**: adapters dependem de interfaces da Application layer; Application layer nunca depende de adapters
- **SRP**: cada adapter tem um tipo de transformação — controller cuida de input, presenter cuida de output
- **ISP**: interfaces estreitas e específicas por cliente (ex.: interfaces separadas para criação, conclusão e consulta de tasks)

**Regra**: A Interface Adapters layer define interfaces de presenter; a Application layer define interfaces de use case e repositório. Nenhuma das duas depende de implementações concretas.

---

### 6.2 Controllers em Python

Controllers aceitam input externo como primitivos, validam e transformam em request models, coordenam execução do use case e retornam `OperationResult` formatado pelo presenter.

```python
@dataclass
class TaskController:
    create_use_case: CreateTaskUseCase  # Application layer interface (duck typing)
    presenter: TaskPresenter            # Interface Adapters layer ABC

    def handle_create(
        self,
        title: str,
        description: str
    ) -> OperationResult[TaskViewModel]:
        try:
            request = CreateTaskRequest(title=title, description=description)
            result = self.create_use_case.execute(request)
            if result.is_success:
                view_model = self.presenter.present_task(result.value)
                return OperationResult.succeed(view_model)
            error_vm = self.presenter.present_error(
                result.error.message, str(result.error.code.name))
            return OperationResult.fail(error_vm.message, error_vm.code)
        except ValueError as e:
            error_vm = self.presenter.present_error(str(e), "VALIDATION_ERROR")
            return OperationResult.fail(error_vm.message, error_vm.code)
```

**Regra**: Controllers recebem apenas primitivos (`str`, `int`) do mundo externo; use cases recebem apenas request models validados. A fronteira de validação é o controller.

> ⚠ Evite: instanciar use cases ou presenters dentro do controller (`self.use_case = TaskUseCase(SqliteTaskRepository())`) — cria acoplamento forte, impede troca de implementações e dificulta testes.

#### 6.2.1 Independência do Controller

Um controller limpo **não contém**:
- Imports de web frameworks (FastAPI, Flask, Django)
- Preocupações de banco de dados ou storage
- Instanciação direta de dependências
- Conhecimento de implementações concretas de views

> ⚠ Evite:
> ```python
> class WebTaskController:
>     def __init__(self, app: FastAPI):
>         self.app = app
>         self.use_case = CreateTaskUseCase()  # violação dupla
>     async def handle_create(self, request: Request):
>         return JSONResponse(status_code=201, content={"task": result})
> ```
> A lógica de expor o controller via HTTP pertence ao Frameworks layer (Cap. 7), não ao controller.

> 💡 Nota: Para use cases simples, Python duck typing é suficiente (qualquer classe com método `execute` satisfaz o contrato); para presenters com contratos complexos, use ABC formal. Ambos mantêm a Dependency Rule.

---

### 6.3 Enforcing Boundaries via OperationResult

`OperationResult[T]` é o mecanismo de boundary crossing do Interface Adapters layer: encapsula sucesso (com view model tipado) ou falha (com `ErrorViewModel`), tornando ambos os caminhos explícitos no tipo de retorno.

```python
@dataclass
class OperationResult(Generic[T]):
    _success: Optional[T] = None
    _error: Optional[ErrorViewModel] = None

    @classmethod
    def succeed(cls, value: T) -> 'OperationResult[T]':
        return cls(_success=value)

    @classmethod
    def fail(cls, message: str, code: Optional[str] = None) -> 'OperationResult[T]':
        return cls(_error=ErrorViewModel(message, code))
```

Uso no Frameworks layer (ex.: CLI):

```python
result = app.task_controller.handle_create(title, description)
if result.is_success:
    task = result.success
    print(f"{task.status_display} [{task.priority_display}] {task.title}")
    return 0
print(result.error.message)
return 1
```

**Regra**: Use `OperationResult[T]` no retorno de todos os métodos de controller — diferentemente de `Result` da Application layer, `OperationResult` carrega view models (não entidades de domínio), pois já cruzou a fronteira de apresentação.

#### 6.3.1 Fluxo de transformação de dados

O fluxo completo dentro de `handle_create`:
1. Input externo (primitivos) → `CreateTaskRequest` (validação)
2. Request model → execução do use case (tipos de domínio)
3. Resultado de domínio → `TaskViewModel` (via presenter, caso sucesso)
4. Erro de domínio → `ErrorViewModel` (via presenter, caso falha)
5. Erro de validação → `ErrorViewModel` (capturado antes do use case)

**Regra**: Nunca retorne entidades de domínio ou `Result` do Application layer diretamente para o Frameworks layer — passe sempre por um presenter para obter um view model.

#### 6.3.2 Quando um Adapter na Interface layer não é necessário

Adapters são necessários quando há conversão de formato entre camadas. Se a camada externa pode implementar diretamente a interface definida pela camada interna, sem conversão, um adapter intermediário é desnecessário:

```python
# Application layer define a interface
class TaskRepository(ABC):
    @abstractmethod
    def get(self, task_id: UUID) -> Task: pass

# Infrastructure implementa diretamente — sem adapter intermediário
class SqliteTaskRepository(TaskRepository):
    def get(self, task_id: UUID) -> Task: ...
```

**Regra**: Pergunte: "Esta interação requer conversão de formato entre camadas?" Se a camada externa pode implementar a interface diretamente, não crie um adapter.

---

### 6.4 Presenters e o Humble Object Pattern

#### 6.4.1 Humble Object Pattern

O padrão Humble Object separa lógica de apresentação (testável) da view (difícil de testar) em dois componentes:
- **View ("humble")**: exibe dados pré-formatados, sem lógica, difícil de testar diretamente
- **Presenter**: contém toda a lógica de formatação, facilmente testável em isolamento

```python
# View humble — sem lógica, apenas exibe
def display_task(task_vm: TaskViewModel):
    print(f"{task_vm.status_display} [{task_vm.priority_display}] {task_vm.title}")
    if task_vm.due_date_display:
        print(f"Due: {task_vm.due_date_display}")
```

Toda decisão de formatação (como exibir status, datas, prioridades) vive no presenter, não na view.

> 💡 Nota: Para APIs Python que servem JSON para um frontend JavaScript, a necessidade de presenter pode ser mínima. Presenters robustos são mais valiosos em aplicações full-stack Python ou quando múltiplas interfaces (CLI, web, API) compartilham a mesma lógica de formatação.

#### 6.4.2 Presenter Interface e View Models

A interface ABC do presenter é definida na Interface Adapters layer:

```python
class TaskPresenter(ABC):
    @abstractmethod
    def present_task(self, task_response: TaskResponse) -> TaskViewModel:
        pass

    @abstractmethod
    def present_error(self, error_msg: str, code: Optional[str] = None) -> ErrorViewModel:
        pass
```

`TaskViewModel` é o data carrier entre presenter e view — apenas primitivos, tudo pré-formatado, imutável:

```python
@dataclass(frozen=True)
class TaskViewModel:
    id: str
    title: str
    description: str
    status_display: str       # pré-formatado
    priority_display: str     # pré-formatado
    due_date_display: Optional[str]   # pré-formatado
    project_display: Optional[str]
    completion_info: Optional[str]
```

**Regra**: View models usam apenas tipos primitivos (`str`, `int`, `bool`, `Optional[str]`), são imutáveis (`frozen=True`) e incluem apenas dados necessários para exibição. Views nunca recebem entidades de domínio.

#### 6.4.3 Implementando Concrete Presenters

Concrete presenters são implementados no Frameworks layer (ou na infraestrutura de interface), mas seguem a interface ABC do Interface Adapters layer:

```python
class CliTaskPresenter(TaskPresenter):
    def present_task(self, task_response: TaskResponse) -> TaskViewModel:
        return TaskViewModel(
            id=str(task_response.id),
            title=task_response.title,
            description=task_response.description,
            status_display=self._format_status(task_response.status),
            priority_display=self._format_priority(task_response.priority),
            due_date_display=self._format_due_date(task_response.due_date),
            project_display=self._format_project(task_response.project_id),
            completion_info=self._format_completion_info(
                task_response.completion_date, task_response.completion_notes)
        )

    def _format_due_date(self, due_date: Optional[datetime]) -> str:
        if not due_date:
            return "No due date"
        is_overdue = due_date < datetime.now(timezone.utc)
        date_str = due_date.strftime("%Y-%m-%d")
        return f"OVERDUE - Due: {date_str}" if is_overdue else f"Due: {date_str}"

    def present_error(self, error_msg: str, code: Optional[str] = None) -> ErrorViewModel:
        return ErrorViewModel(message=error_msg, code=code)
```

**Regra**: Cada interface (CLI, web, API) cria seu próprio concrete presenter. Toda lógica de formatação específica da interface fica no presenter concreto — os use cases e domain objects permanecem inalterados ao adicionar novas interfaces.

---

## Capítulo 7 — The Frameworks and Drivers Layer: External Interfaces

### 7.1 Posição e Responsabilidade da Camada

A Frameworks and Drivers layer é a camada mais externa — contém "os detalhes" do sistema: UI, banco de dados, frameworks e serviços externos. Todas as dependências apontam para dentro; camadas internas nunca conhecem esta camada.

Componentes externos gerenciados aqui:
- Interfaces de usuário (CLI, web, endpoints de API)
- Sistemas de banco de dados (drivers como sqlite3; frameworks como SQLAlchemy)
- Serviços externos e APIs de terceiros
- Sistemas de arquivo e interações com dispositivos

Benefícios da posição estratégica:
- **Framework independence**: lógica de negócio permanece ignorante de escolhas específicas de framework
- **Easy testing**: dependências externas substituídas por test doubles sem alterar núcleo
- **Flexible evolution**: detalhes de implementação mudam sem afetar camadas internas
- **Clear boundaries**: interfaces explícitas definem como preocupações externas interagem com o sistema

**Regra**: Mantenha todas as escolhas de implementação (SQLite/PostgreSQL, Click/Typer, SendGrid/AWS SES) confinadas nesta camada. O núcleo da aplicação nunca conhece essas escolhas.

---

### 7.2 Frameworks versus Drivers — Distinção

**Frameworks** (Flask, FastAPI, Click, SQLAlchemy) impõem seu próprio fluxo de controle e arquitetura. Requerem o conjunto completo de componentes da Interface Adapters layer: controllers, presenters e view models.

**Drivers** (sqlite3, requests, smtplib) fornecem serviços de baixo nível sem impor estrutura. Requerem apenas:
- Um port/interface definido na Application layer
- Uma implementação concreta na Frameworks and Drivers layer

```python
# Framework — requer stack completo da Interface Adapters layer
@app.route("/tasks", methods=["POST"])
def create_task():
    result = task_controller.handle_create(
        title=request.json["title"],
        description=request.json["description"]
    )
    return task_presenter.present(result)

# Driver — implementa diretamente o port da Application layer
class SQLiteTaskRepository(TaskRepository):
    def save(self, task: Task) -> None:
        self.connection.execute(
            "INSERT INTO tasks (id, title) VALUES (?, ?)",
            (str(task.id), task.title)
        )
```

**Regra**: Para integrar um framework, crie controllers e presenters na Interface Adapters layer. Para integrar um driver, implemente diretamente o port definido pela Application layer.

---

### 7.3 Application Composition — Composição da Aplicação

A composição da aplicação tem três aspectos que trabalham juntos:

| Aspecto | Responsabilidade |
|---|---|
| **Configuration management** | Lê settings por ambiente; controla seleção de framework e driver |
| **Component factories** | Criam implementações configuradas das interfaces; gerenciam ciclo de vida |
| **Main entry point** | Orquestra startup; serve como composition root onde dependências são montadas |

**Regra**: A composição acontece em um único lugar (composition root). O business logic nunca instancia suas próprias dependências concretas.

---

### 7.4 Framework Adapter — UI com Click (ClickCli)

O adapter de UI isola o framework (Click) do resto da aplicação. Recebe a instância de `Application` por injeção de dependência; nunca instancia componentes internos diretamente.

```python
class ClickCli:
    def __init__(self, app: Application):
        self.app = app
        self.current_projects = []

    def run(self) -> int:
        try:
            while True:
                self._display_projects()
                self._handle_selection()
        except KeyboardInterrupt:
            click.echo("\nGoodbye!", err=True)
            return 0
```

Uso do controller no handler de exibição:

```python
def _display_task_menu(self, task_id: str) -> None:
    result = self.app.task_controller.handle_get(task_id)
    if not result.is_success:
        click.secho(result.error.message, fg="red", err=True)
        return
    task = result.success
    click.clear()
    click.echo(f"Status:   {task.status_display}")
    click.echo(f"Priority: {task.priority_display}")
```

**Regra**: Código específico de framework (Click, Flask) permanece contido dentro do adapter. O adapter nunca contém lógica de negócio — apenas tradução de I/O e delegação para controllers.

> ⚠ Evite: Instanciar use cases ou presenters dentro do adapter (`self.use_case = TaskUseCase(SqliteRepository())`) — cria acoplamento forte e impede troca de implementações.

---

### 7.5 Implementando Interações de Usuário

O handler de seleção valida e normaliza input antes de processar; mantém separação entre parsing de input e lógica de negócio:

```python
def _handle_selection(self) -> None:
    selection = click.prompt(
        "\nSelect a project or task (e.g., '1' or '1.a')",
        type=str, show_default=False
    ).strip().lower()
    if selection == "np":
        self._create_new_project()
        return
    try:
        if "." in selection:
            project_num, task_letter = selection.split(".")
            self._handle_task_selection(int(project_num), task_letter)
        else:
            self._handle_project_selection(int(selection))
    except (ValueError, IndexError):
        click.secho("Invalid selection. Use '1' for project or '1.a' for task.",
                    fg="red", err=True)
```

Criação delegada ao controller (sem lógica de negócio no adapter):

```python
def _create_new_project(self) -> None:
    name = click.prompt("Project name", type=str)
    description = click.prompt("Description (optional)", type=str, default="")
    result = self.app.project_controller.handle_create(name, description)
    if not result.is_success:
        click.secho(result.error.message, fg="red", err=True)
```

**Regra**: O framework adapter faz parsing e normalização de input; os use cases contêm as regras de negócio. Nunca misture lógica de negócio com lógica de apresentação no adapter.

---

### 7.6 Domain Insights via Implementação de UI — Inbox Pattern

A implementação de UI pode revelar insights sobre o modelo de domínio. Quando a UI exige lógica condicional excessiva (ex.: tratamento especial de tarefas com e sem projeto), isso sinaliza que o modelo de domínio precisa ser refinado.

Insight: tarefas sempre pertencem a projetos no modelo mental dos usuários. Um projeto "Inbox" serve como container default.

Mudanças em cascata por camada (Domain → Application → Adapter):

```python
# 1. Domain Layer — novo invariante
class ProjectType(Enum):
    REGULAR = "REGULAR"
    INBOX = "INBOX"

@dataclass
class Project(Entity):
    name: str
    description: str = ""
    project_type: ProjectType = field(default=ProjectType.REGULAR)

    @classmethod
    def create_inbox(cls) -> "Project":
        return cls(
            name="INBOX",
            description="Default project for unassigned tasks",
            project_type=ProjectType.INBOX
        )

@dataclass
class Task(Entity):
    title: str
    description: str
    project_id: UUID  # obrigatório — não mais Optional
```

```python
# 2. Application Layer — regra de negócio centralizada
class ProjectRepository(ABC):
    @abstractmethod
    def get_inbox(self) -> Project: pass

@dataclass
class CreateTaskUseCase:
    task_repository: TaskRepository
    project_repository: ProjectRepository

    def execute(self, request: CreateTaskRequest) -> Result:
        params = request.to_execution_params()
        project_id = params.get("project_id")
        if not project_id:
            project_id = self.project_repository.get_inbox().id
        # ...
```

```python
# 3. Framework Adapter — simplifica após refinamento do domínio
def _create_task(self) -> None:
    title = click.prompt("Task title", type=str)
    description = click.prompt("Description", type=str)
    project_id = None
    if click.confirm("Assign to a specific project?", default=False):
        project_id = self._select_project()
    result = self.app.task_controller.handle_create(
        title=title, description=description, project_id=project_id
    )
```

**Regra**: Quando a implementação de uma interface revela complexidade acidental (lógica condicional excessiva no adapter), investigue se o modelo de domínio precisa ser refinado. Refine começando pelo Domain layer e propagando para fora.

> 💡 Nota: Clean Architecture isola mudanças técnicas nas bordas, mas mudanças de modelo de domínio requerem modificação sistemática através das camadas — com caminhos claros e sem efeitos colaterais inesperados.

---

### 7.7 Database Adapters — Implementação de Repository

Drivers de banco de dados implementam diretamente a interface de repository definida na Application layer. Complexidade de serialização permanece isolada na implementação concreta:

```python
class FileTaskRepository(TaskRepository):
    def __init__(self, data_dir: Path):
        self.tasks_file = data_dir / "tasks.json"
        self._ensure_file_exists()

    def get(self, task_id: UUID) -> Task:
        tasks = self._load_tasks()
        for task_data in tasks:
            if UUID(task_data["id"]) == task_id:
                return self._dict_to_task(task_data)
        raise TaskNotFoundError(task_id)

    def save(self, task: Task) -> None:
        # serialização JSON isolada aqui
        ...
```

O código de domínio usa qualquer implementação de forma idêntica:

```python
task = repository.get(task_id)
task.complete()
repository.save(task)
```

**Regra**: A complexidade de serialização/desserialização (JSON, SQL, ORM) fica isolada na implementação concreta do repository. O código de domínio nunca conhece o formato de armazenamento. Trocar SQLite por PostgreSQL exige apenas um novo adapter — o Domain layer não muda.

---

### 7.8 Gerenciamento de Instanciação — Config e Factory

`Config` lê variáveis de ambiente para determinar qual implementação criar; `create_repositories` factory instancia as implementações corretas:

```python
class Config:
    DEFAULT_REPOSITORY_TYPE = RepositoryType.MEMORY

    @classmethod
    def get_repository_type(cls) -> RepositoryType:
        repo_type_str = os.getenv(
            "TODO_REPOSITORY_TYPE",
            cls.DEFAULT_REPOSITORY_TYPE.value
        )
        try:
            return RepositoryType(repo_type_str.lower())
        except ValueError:
            raise ValueError(f"Invalid repository type: {repo_type_str}")

    @classmethod
    def get_sendgrid_api_key(cls) -> str:
        return os.getenv("TODO_SENDGRID_API_KEY", "")

    @classmethod
    def get_notification_email(cls) -> str:
        return os.getenv("TODO_NOTIFICATION_EMAIL", "")
```

```python
def create_repositories() -> Tuple[TaskRepository, ProjectRepository]:
    repo_type = Config.get_repository_type()
    if repo_type == RepositoryType.FILE:
        data_dir = Config.get_data_directory()
        task_repo = FileTaskRepository(data_dir)
        project_repo = FileProjectRepository(data_dir)
        project_repo.set_task_repository(task_repo)
        return task_repo, project_repo
    elif repo_type == RepositoryType.MEMORY:
        task_repo = InMemoryTaskRepository()
        project_repo = InMemoryProjectRepository()
        project_repo.set_task_repository(task_repo)
        return task_repo, project_repo
    raise ValueError(f"Invalid repository type: {repo_type}")
```

**Regra**: `Config` lê variáveis de ambiente; factories instanciam implementações. Factories retornam interfaces abstratas — clientes nunca conhecem o tipo concreto criado.

---

### 7.9 Integração de Serviços Externos — SendGrid

O adapter de serviço externo implementa o port definido pela Application layer. Erros de serviço não devem interromper operações de negócio:

```python
class SendGridNotifier(NotificationPort):
    def __init__(self) -> None:
        self.api_key = Config.get_sendgrid_api_key()
        self.notification_email = Config.get_notification_email()
        self._init_sg_client()

    def notify_task_completed(self, task: Task) -> None:
        if not (self.client and self.notification_email):
            return
        try:
            message = Mail(
                from_email=self.notification_email,
                to_emails=self.notification_email,
                subject=f"Task Completed: {task.title}",
                plain_text_content=f"Task '{task.title}' has been completed."
            )
            self.client.send(message)
        except Exception:
            pass  # logar o erro; não interromper operações de negócio
```

**Regra**: Adicionar ou trocar um serviço externo (SendGrid → AWS SES) requer apenas criar um novo adapter e alterar o wiring em `create_application`. O Application layer e os use cases não mudam.

> ⚠ Evite: Deixar exceções de serviços externos propagarem para o use case — devem ser tratadas e logadas no adapter.

---

### 7.10 Application Bootstrapping — Container e Composition Root

O `Application` container agrega todas as dependências e conecta use cases a controllers via `__post_init__`:

```python
@dataclass
class Application:
    task_repository: TaskRepository
    project_repository: ProjectRepository
    notification_service: NotificationPort
    task_presenter: TaskPresenter
    project_presenter: ProjectPresenter

    def __post_init__(self):
        self.create_task_use_case = CreateTaskUseCase(
            self.task_repository, self.project_repository)
        self.complete_task_use_case = CompleteTaskUseCase(
            self.task_repository, self.notification_service)
        self.get_task_use_case = GetTaskUseCase(self.task_repository)
        self.task_controller = TaskController(
            create_use_case=self.create_task_use_case,
            complete_use_case=self.complete_task_use_case,
            get_use_case=self.get_task_use_case,
            presenter=self.task_presenter,
        )
```

Factory function que cria a aplicação completa:

```python
def create_application(
    notification_service: NotificationPort,
    task_presenter: TaskPresenter,
    project_presenter: ProjectPresenter,
) -> Application:
    task_repository, project_repository = create_repositories()
    notification_service = create_notification_service()
    return Application(
        task_repository=task_repository,
        project_repository=project_repository,
        notification_service=notification_service,
        task_presenter=task_presenter,
        project_presenter=project_presenter,
    )
```

Entry point (`main.py`) — composition root completo:

```python
def main() -> int:
    try:
        app = create_application(
            notification_service=NotificationRecorder(),
            task_presenter=CliTaskPresenter(),
            project_presenter=CliProjectPresenter(),
        )
        cli = ClickCli(app)
        return cli.run()
    except KeyboardInterrupt:
        print("\nGoodbye!")
        return 0
    except Exception as e:
        print(f"Error: {str(e)}", file=sys.stderr)
        return 1

if __name__ == "__main__":
    sys.exit(main())
```

**Regra**: `main.py` é o único lugar onde todas as dependências concretas são instanciadas (composition root). Para trocar de interface (CLI → web), substitua `ClickCli(app)` por um adapter web que usa o mesmo `create_application`.

> 💡 Nota: Tratamento de `KeyboardInterrupt` e `Exception` no top-level é responsabilidade do composition root — não das camadas internas.

---

## Capítulo 8 — Implementing Test Patterns with Clean Architecture

### 8.1 Fundamentos de Testes em Clean Architecture

Clean Architecture transforma testes de um desafio técnico complexo em verificação direta. Fronteiras explícitas entre camadas guiam o que testar e como isolar cada componente.

**Testing Pyramid** — distribuição ideal de tipos de teste:
- **Base (larga)**: testes unitários rápidos que verificam componentes em isolamento
- **Meio**: testes de integração que verificam interações entre componentes
- **Topo (pequeno)**: poucos testes end-to-end para fluxos críticos de usuário

**Regra**: Construa confiança no sistema principalmente por testes unitários e de integração focados; minimize testes end-to-end lentos e frágeis.

#### 8.1.1 Testes como Feedback Arquitetural

Testes são clientes do código. Se um teste é difícil de escrever ou exige setup complexo, isso indica necessidade de melhoria no código de produção.

- Setup complexo → componentes acoplados que deveriam estar separados
- Testes difíceis de escrever → fronteira arquitetural ausente ou violada
- Mocks extensos → possível violação de SRP

**Regra**: Use dificuldade de teste como sinal de alerta arquitetural. Testes difíceis revelam violações antes que se tornem profundamente enraizadas no codebase.

---

### 8.2 Testes Unitários por Camada

#### 8.2.1 Testing Domain Entities — Padrão AAA

O padrão **Arrange-Act-Assert** alinha naturalmente com os limites do Domain layer:

```python
def test_task_completion_captures_completion_time():
    # Arrange
    task = Task(
        title="Test task",
        description="Test description",
        project_id=UUID('12345678-1234-5678-1234-567812345678'),
    )
    # Act
    task.complete()
    # Assert
    assert task.completed_at is not None
    assert (datetime.now() - task.completed_at) < timedelta(seconds=1)
```

**Regra**: Testes de entidades de domínio não devem precisar de conexões a banco de dados, serviços de notificação, autenticação ou estado externo. Se precisam, a entidade viola a pureza do domain layer.

Comparação: entidade com dependências diretas (antipadrão) versus entidade pura (Clean Architecture):

```python
# Antipadrão — testa regra de domínio simples mas exige setup de infra
def test_new_task_priority_antipattern():
    db_connection = create_database_connection()
    notification_service = create_notification_service()
    task = Task(title="Test task", description="Test description")
    saved_task = task.db.get_task(task.id)
    assert saved_task['priority'] == Priority.MEDIUM

# Clean Architecture — foco exclusivo na regra de negócio
def test_new_task_priority():
    task = Task(
        title="Test task",
        description="Test description",
        project_id=UUID('12345678-1234-5678-1234-567812345678')
    )
    assert task.priority == Priority.MEDIUM
```

> ⚠ Evite: Entidades que instanciam `Database()` ou `NotificationService()` no `__init__` — forçam setup de infraestrutura em cada teste de domínio.

#### 8.2.2 Test Double Tools em Python

`unittest.mock.Mock` cria objetos que registram chamadas e retornam valores pré-configurados:

```python
from unittest.mock import Mock

mock_repo = Mock()
mock_repo.get.return_value = some_task
mock_repo.get(123)                         # retorna some_task
mock_repo.get.assert_called_once()         # verifica que foi chamado exatamente uma vez
print(mock_repo.get.call_args)             # argumentos passados
print(mock_repo.get.call_count)            # número de chamadas
```

Mocks servem a dois propósitos:
- Controlar o comportamento de dependências (garantir que um repositório retorne uma task específica)
- Verificar como o código interage com essas dependências (garantir que `save()` foi chamado exatamente uma vez)

#### 8.2.3 Testing Use Case Orchestration

Use cases dependem de interfaces abstratas, não de implementações concretas. Mocks substituem implementações sem modificar o código do use case:

```python
def test_successful_task_completion():
    # Arrange
    task = Task(
        title="Test task",
        description="Test description",
        project_id=UUID('12345678-1234-5678-1234-567812345678'),
    )
    task_repo = Mock()
    task_repo.get.return_value = task
    notification_service = Mock()

    use_case = CompleteTaskUseCase(
        task_repository=task_repo,
        notification_service=notification_service
    )
    request = CompleteTaskRequest(task_id=str(task.id))

    # Act
    result = use_case.execute(request)

    # Assert
    assert result.is_success
    task_repo.save.assert_called_once_with(task)
    notification_service.notify_task_completed.assert_called_once_with(task)
```

**Regra**: Assertions de testes de use case verificam **orquestração** (sequência correta de operações), não lógica de negócio. A lógica de negócio é verificada nos testes de entidades.

#### 8.2.4 Testing Interface Adapters

Foco: verificar tradução correta entre formatos externos e o núcleo da aplicação. Mocke use cases e foque apenas na lógica de transformação.

```python
def test_controller_converts_string_id_to_uuid():
    task_id = "123e4567-e89b-12d3-a456-426614174000"
    complete_use_case = Mock()
    complete_use_case.execute.return_value = Result.success(
        TaskResponse.from_entity(
            Task(title="Test Task", description="Test Description",
                 project_id=UUID('12345678-1234-5678-1234-567812345678'))
        )
    )
    presenter = Mock(spec=TaskPresenter)   # spec enforces interface contract

    controller = TaskController(
        complete_use_case=complete_use_case,
        presenter=presenter,
    )

    controller.handle_complete(task_id=task_id)

    complete_use_case.execute.assert_called_once()
    called_request = complete_use_case.execute.call_args[0][0]
    assert isinstance(called_request.task_id, UUID)
```

**Regra**: Use `Mock(spec=TaskPresenter)` para criar mocks estritos que respeitam a interface definida — chamadas a métodos inexistentes levantam `AttributeError`, detectando violações de contrato.

```python
# Diferença entre mock loose e mock strict
loose_mock = Mock()
loose_mock.non_existent_method()     # funciona silenciosamente — pode esconder bugs

strict_mock = Mock(spec=TaskPresenter)
strict_mock.non_existent_method()    # levanta AttributeError — captura violações
```

Teste de presenter para formatação de datas:

```python
def test_presenter_formats_completion_date():
    completion_time = datetime(2024, 1, 15, 14, 30, tzinfo=timezone.utc)
    task = Task(
        title="Test Task",
        description="Test Description",
        project_id=UUID('12345678-1234-5678-1234-567812345678')
    )
    task.complete()
    task.completed_at = completion_time    # override para teste determinístico
    task_response = TaskResponse.from_entity(task)
    presenter = CliTaskPresenter()

    view_model = presenter.present_task(task_response)

    expected_format = "2024-01-15 14:30"
    assert expected_format in view_model.completion_info
```

---

### 8.3 Testing Across Architectural Boundaries

Testes de integração verificam que implementações concretas funcionam corretamente juntas, complementando os testes unitários que verificaram a lógica via mocks.

#### 8.3.1 Estratégia de Testes de Integração

Foque em **key boundary crossings** — especialmente aqueles envolvendo persistência ou serviços externos:

```python
@pytest.fixture
def repository(tmp_path):
    return FileTaskRepository(data_dir=tmp_path)

def test_repo_handles_project_task_relationships(tmp_path):
    task_repo = FileTaskRepository(tmp_path)
    project_repo = FileProjectRepository(tmp_path)
    project_repo.set_task_repository(task_repo)

    project = Project(name="Test Project", description="Testing relationships")
    project_repo.save(project)
    task = Task(title="Test Task", description="Testing relationships",
                project_id=project.id)
    task_repo.save(task)

    loaded_project = project_repo.get(project.id)

    assert len(loaded_project.tasks) == 1
    assert loaded_project.tasks[0].title == "Test Task"
```

Verificando garantia de infraestrutura (inbox):

```python
def test_repository_automatically_creates_inbox(tmp_path):
    initial_repo = FileProjectRepository(tmp_path)
    initial_inbox = initial_repo.get_inbox()
    assert initial_inbox.name == "INBOX"
    assert initial_inbox.project_type == ProjectType.INBOX

    new_repo = FileProjectRepository(tmp_path)

    persisted_inbox = new_repo.get_inbox()
    assert persisted_inbox.id == initial_inbox.id
    assert persisted_inbox.project_type == ProjectType.INBOX
```

Teste de use case com persistência real e notificações mockadas:

```python
def test_task_creation_with_persistence(tmp_path):
    task_repo = FileTaskRepository(tmp_path)
    project_repo = FileProjectRepository(tmp_path)
    project_repo.set_task_repository(task_repo)

    use_case = CreateTaskUseCase(
        task_repository=task_repo,
        project_repository=project_repo,
        notification_service=Mock()    # mock apenas o que não é relevante aqui
    )

    result = use_case.execute(CreateTaskRequest(
        title="Test Task",
        description="Integration test"
    ))

    assert result.is_success
    created_task = task_repo.get(UUID(result.value.id))
    assert created_task.project_id == project_repo.get_inbox().id
```

**Regra**: Em testes de integração, use implementações reais apenas para a fronteira sendo verificada; mantenha mocks para preocupações não relacionadas. Confie na cobertura dos testes unitários para a lógica de negócio.

---

### 8.4 Tools and Patterns for Test Maintenance

#### 8.4.1 Estrutura de Arquivos de Teste

Organize testes espelhando a arquitetura da aplicação:

```
tests/
    domain/
        entities/
            test_task.py
            test_project.py
        value_objects/
            test_deadline.py
    application/
        use_cases/
            test_task_use_cases.py
    interfaces/
        test_controllers.py
        test_presenters.py
    infrastructure/
        test_repositories.py
```

**Regra**: Testes em `tests/domain/` não devem importar de `application/` ou `interfaces/`. Se um import se torna necessário, ele sinaliza violação da Dependency Rule no código de produção.

#### 8.4.2 Parameterized Testing

Use `@pytest.mark.parametrize` para verificar comportamento sob múltiplas condições sem duplicar código de teste:

```python
@pytest.mark.parametrize(
    "request_data,expected_behavior",
    [
        (
            {"title": "Test Task", "description": "Basic creation"},
            {"project_type": ProjectType.INBOX, "priority": Priority.MEDIUM}
        ),
        (
            {"title": "Project Task", "description": "With project",
             "project_id": "project-uuid"},
            {"project_type": ProjectType.REGULAR, "priority": Priority.MEDIUM}
        ),
    ],
    ids=["basic-task", "project-task"]
)
def test_task_creation_scenarios(request_data, expected_behavior):
    task_repo = Mock(spec=TaskRepository)
    project_repo = FileProjectRepository(tmp_path)
    use_case = CreateTaskUseCase(
        task_repository=task_repo,
        project_repository=project_repo
    )

    result = use_case.execute(CreateTaskRequest(**request_data))

    assert result.is_success
    created_task = result.value
    if expected_behavior["project_type"] == ProjectType.INBOX:
        assert UUID(created_task.project_id) == project_repo.get_inbox().id
    assert created_task.priority == expected_behavior["priority"]
```

**Regra**: Use o parâmetro `ids` para nomear cenários — falhas reportam `test_task_creation_scenarios[basic-task]` em vez de `test_task_creation_scenarios[0]`, identificando o problema imediatamente.

#### 8.4.3 Organizing Test Fixtures com conftest.py

Coloque fixtures nos diretórios de teste correspondentes à camada que servem:

```python
# tests/conftest.py — fixtures disponíveis para todos os testes
@pytest.fixture
def sample_task_data():
    return {
        "title": "Test Task",
        "description": "Sample task for testing",
        "project_id": UUID('12345678-1234-5678-1234-567812345678'),
    }

# tests/domain/conftest.py — fixtures da camada de domínio
@pytest.fixture
def domain_task(sample_task_data):
    return Task(**sample_task_data)

# tests/application/conftest.py — fixtures da camada de aplicação
@pytest.fixture
def mock_task_repository(domain_task):
    repo = Mock(spec=TaskRepository)
    repo.get.return_value = domain_task
    return repo

# tests/interfaces/conftest.py — fixtures da camada de interfaces
@pytest.fixture
def task_controller(mock_task_repository, mock_notification_port):
    return TaskController(
        create_use_case=CreateTaskUseCase(
            task_repository=mock_task_repository,
            project_repository=Mock(spec=ProjectRepository),
            notification_service=mock_notification_port
        ),
        presenter=Mock(spec=TaskPresenter)
    )
```

**Regra**: Estruture fixtures para espelhar o dependency injection de produção. Um teste que precisa de entidades de domínio e repositórios deve residir na camada Application ou superior — a localização do arquivo reforça a Dependency Rule.

#### 8.4.4 Managing Time in Tests — freezegun

`freezegun` controla o tempo em testes sem modificar a lógica de domínio:

```bash
pip install freezegun
```

```python
from freezegun import freeze_time

def test_task_deadline_approaching():
    with freeze_time("2024-01-14 12:00:00"):
        task = Task(
            title="Time-sensitive task",
            description="Testing deadlines",
            project_id=UUID('12345678-1234-5678-1234-567812345678'),
            due_date=Deadline(datetime(2024, 1, 15, 12, 0, tzinfo=timezone.utc))
        )

    notification_service = Mock(spec=NotificationPort)
    use_case = CheckDeadlinesUseCase(
        task_repository=Mock(spec=TaskRepository),
        notification_service=notification_service,
        warning_threshold=timedelta(days=1)
    )

    with freeze_time("2024-01-14 13:00:00"):
        result = use_case.execute()

    assert result.is_success
    notification_service.notify_task_deadline_approaching.assert_called_once()
```

**Regra**: Use `freeze_time` para testar lógica dependente de tempo. Entidades e use cases continuam usando `datetime` reais; apenas a percepção do tempo atual é afetada — sem alterar os limites arquiteturais.

#### 8.4.5 Exposing State Dependencies — pytest-random-order

Dependências ocultas de estado ou ordem de execução mascaram violações arquiteturais. Execute testes em ordem aleatória para expô-las:

```bash
pip install pytest-random-order
```

```ini
# pytest.ini
[pytest]
addopts = --random-order
```

Para reproduzir uma falha:

```bash
pytest --random-order-seed=123456
```

**Regra**: Execute testes em ordem aleatória em todo ambiente de CI. Se um teste falha apenas em certas ordens, há estado global implícito que deve ser explicitado nas interfaces ou isolado por fixture.

#### 8.4.6 Accelerating Test Execution — pytest-xdist

`pytest-xdist` paraleliza execução de testes usando múltiplos CPUs:

```bash
pip install pytest-xdist
```

```ini
# pytest.ini
[pytest]
addopts = --random-order -n auto
```

Para testes com estado compartilhado inevitável:
- `@pytest.mark.serial` — força execução sequencial
- `@pytest.mark.resource_group('global-cache')` — agrupa testes que usam o mesmo recurso

**Regra**: Combine `--random-order` e `-n auto` para máxima confiabilidade e velocidade. Testes que não toleram paralelismo sinalizam estado global que provavelmente indica violação arquitetural.

---

## Capítulo 9 — Adding Web UI: Clean Architecture's Interface Flexibility

### 9.1 Interface Flexibility — Adição Puramente Aditiva

Adicionar uma nova interface (web, mobile, API) em uma aplicação com Clean Architecture correta é uma mudança **puramente aditiva**: nenhum código existente precisa ser modificado — nem entidades, nem use cases, nem a CLI já existente.

**Regra**: Se adicionar uma nova interface exige refatorar use cases ou entidades, a Dependency Rule foi violada em algum ponto anterior.

> ⚠ Evite: Aplicações onde adicionar uma interface web dispara alterações em cascata no Domain layer — sinal de que lógica de negócio vazou para as bordas.

---

### 9.2 Parallel Interface Implementations

CLI e Web compartilham o mesmo `Application` container (documentado em 7.10). Cada interface fornece suas próprias implementações concretas de presenters ao invocar `create_application`:

```python
# cli_main.py — interface CLI
app = create_application(
    notification_service=NotificationRecorder(),
    task_presenter=CliTaskPresenter(),
    project_presenter=CliProjectPresenter(),
)
cli = ClickCli(app)

# web_main.py — interface Web
app_container = create_application(
    notification_service=create_notification_service(),
    task_presenter=WebTaskPresenter(),
    project_presenter=WebProjectPresenter(),
)
web_app = create_web_app(app_container)
```

O núcleo da aplicação (repositories, use cases, controllers) é idêntico em ambas as interfaces. Cada interface adiciona apenas seus adapters específicos na borda do sistema.

**Regra**: Para cada nova interface, forneça implementações concretas dos presenters e passe-as para `create_application`. O núcleo nunca sabe qual interface está ativa.

---

### 9.3 Common Interface Boundary Violations

#### 9.3.1 Anti-padrão: Código de Framework em Controllers

Controllers na Interface Adapters layer nunca devem importar frameworks específicos (Click, Flask) para formatar respostas:

```python
# Anti-padrão: Click dentro do controller
def handle_create(self, request_data: dict) -> dict:
    result = self.create_use_case.execute(request_data)
    if result.is_success:
        return {"message": click.style(f"Created: {result.value.title}", fg="green")}
    return {"error": click.style(str(e), fg="red")}
```

Esse controller depende simultaneamente da Application layer (inward) e da Frameworks layer (outward), quebrando a Dependency Rule.

#### 9.3.2 Correto: Controller Interface-Agnóstico

```python
def handle_create(self, title: str, description: str) -> OperationResult:
    try:
        request = CreateTaskRequest(title=title, description=description)
        result = self.create_use_case.execute(request)
        if result.is_success:
            view_model = self.presenter.present_task(result.value)
            return OperationResult.succeed(view_model)
        error_vm = self.presenter.present_error(
            result.error.message, str(result.error.code.name)
        )
        return OperationResult.fail(error_vm.message, error_vm.code)
    except ValueError as e:
        error_vm = self.presenter.present_error(str(e), "VALIDATION_ERROR")
        return OperationResult.fail(error_vm.message, error_vm.code)
```

**Regra**: Controllers aceitam tipos Python simples (`str`, `int`), delegam toda formatação ao presenter abstrato e retornam `OperationResult` agnóstico de interface.

> ⚠ Evite: Qualquer `import click` ou `import flask` dentro da Interface Adapters layer.

---

### 9.4 Web-Specific Presenters

`WebTaskPresenter` implementa a mesma interface `TaskPresenter` que `CliTaskPresenter`, mas formata dados para exibição HTML:

```python
class WebTaskPresenter(TaskPresenter):
    def present_task(self, task_response: TaskResponse) -> TaskViewModel:
        return TaskViewModel(
            id=task_response.id,
            title=task_response.title,
            description=task_response.description,
            status_display=task_response.status.value,
            priority_display=task_response.priority.name,
            due_date_display=self._format_due_date(task_response.due_date),
            project_display=task_response.project_id,
            completion_info=self._format_completion_info(
                task_response.completion_date,
                task_response.completion_notes
            ),
        )

    def _format_due_date(self, due_date: Optional[datetime]) -> str:
        if not due_date:
            return ""
        is_overdue = due_date < datetime.now(timezone.utc)
        date_str = due_date.strftime("%Y-%m-%d")
        return f"Overdue: {date_str}" if is_overdue else date_str
```

O template recebe apenas strings pré-formatadas; não contém lógica de domínio:

```html
<span class="badge {% if 'overdue' in task.due_date_display %}bg-danger{% else %}bg-info{% endif %}">
    {{ task.due_date_display }}
</span>
```

**Regra**: Toda lógica de formatação (comparações de data, status overdue, conversão de enum) fica no presenter. Templates fazem apenas checagens de string simples sobre valores já formatados.

O presenter é testável sem Flask:

```python
def test_web_presenter_formats_overdue_date():
    past_date = datetime.now(timezone.utc) - timedelta(days=1)
    task_response = TaskResponse(id="123", title="Test", ..., due_date=past_date)
    view_model = WebTaskPresenter().present_task(task_response)
    assert "Overdue" in view_model.due_date_display
    assert past_date.strftime("%Y-%m-%d") in view_model.due_date_display
```

---

### 9.5 Presenters versus Template-based Formatting

Frameworks como Flask/Django permitem embutir formatação diretamente em templates:

```html
<!-- Anti-padrão: lógica de domínio no template -->
<span class="badge {% if task.due_date < now() %}bg-danger{% else %}bg-info{% endif %}">
    {{ task.due_date.strftime("%Y-%m-%d") }}
    {% if task.due_date < now() %}(Overdue){% endif %}
</span>
```

Esse padrão vaza lógica de negócio (comparações de data, regras de overdue) para a camada de exibição.

**Regra**: Reconheça onde decisões de negócio estão vazando para templates e extraia-as para presenters dedicados. Templates devem tratar dados como strings e booleans já preparados, nunca como objetos de domínio.

> 💡 Nota: A regra aplica-se independente do framework — vale para Jinja2, Django templates, React components ou qualquer outra camada de exibição.

---

### 9.6 Managing Web-Specific State

#### 9.6.1 Anti-padrão: Entidade Acessando Estado Web

```python
# Anti-padrão: entidade depende de web session
class Task:
    def complete(self, web_app_container):
        self.completed_by = web_app_container.user.id  # violação
        self.completed_at = datetime.now()
```

Consequências: testes exigem mock de sessão web; adicionar nova interface obriga alterar entidades; bugs de sessão propagam pelo Domain layer.

#### 9.6.2 Correto: Route Handler como Boundary

```python
# todo_app/infrastructure/web/routes.py
@bp.route("/")
def index():
    app = current_app.config["APP_CONTAINER"]
    show_completed = request.args.get("show_completed", "false").lower() == "true"
    result = app.project_controller.handle_list()
    if not result.is_success:
        error = project_presenter.present_error(result.error.message)
        flash(error.message, "error")
        return redirect(url_for("todo.index"))
    return render_template("index.html", projects=result.success,
                           show_completed=show_completed)
```

O route handler extrai estado web (query params, sessão) e passa apenas dados agnósticos para o núcleo. Flash messages e redirects ficam nesta camada externa.

**Regra**: Route handlers são a fronteira onde preocupações web (HTTP, sessão, cookies, flash) são gerenciadas. Entidades e use cases recebem apenas tipos Python simples.

---

### 9.7 Form Handling and Validation

Fluxo de validação em Clean Architecture:

1. **Route layer** extrai inputs web: URL params (`project_id`), campos de form (`request.form["title"]`), valores opcionais com default (`None` para campos vazios)
2. **Controller** recebe tipos Python simples; coordena use cases
3. **Domain layer** valida via regras de entidade e use cases; retorna `Result`
4. **Route layer** converte resultado em resposta web (flash + redirect)

```python
@bp.route("/projects/new", methods=["GET", "POST"])
def new_project():
    if request.method == "POST":
        name = request.form["name"]
        app = current_app.config["APP_CONTAINER"]
        result = app.project_controller.handle_create(name)
        if not result.is_success:
            error = project_presenter.present_error(result.error.message)
            flash(error.message, "error")
            return redirect(url_for("todo.index"))
        project = result.success
        flash(f'Project "{project.name}" created successfully', "success")
        return redirect(url_for("todo.index"))
    return render_template("project_form.html")
```

**Regra**: Validação de negócio vive no Domain layer (entidades e use cases). A route layer coleta input e apresenta feedback — nunca duplica regras de validação.

> 💡 Nota: Validação client-side (WTForms, JavaScript) pode espelhar regras de domínio para UX responsiva, mas deve ser uma camada fina — a fonte de verdade é sempre o Domain layer.

---

### 9.8 Flask Application Factory

`create_web_app` cria e configura a aplicação Flask sem conter lógica de negócio:

```python
# todo_app/infrastructure/web/app.py
def create_web_app(app_container: Application) -> Flask:
    flask_app = Flask(__name__)
    flask_app.config["SECRET_KEY"] = "dev"  # trocar em produção
    flask_app.config["APP_CONTAINER"] = app_container
    from . import routes
    flask_app.register_blueprint(routes.bp)
    return flask_app
```

`web_main.py` é o composition root da interface web:

```python
def main():
    app_container = create_application(
        notification_service=create_notification_service(),
        task_presenter=WebTaskPresenter(),
        project_presenter=WebProjectPresenter(),
    )
    web_app = create_web_app(app_container)
    web_app.run(debug=True)
```

**Regra**: O `Application` container é criado primeiro (núcleo agnóstico de interface) e depois passado ao `create_web_app` (adapter Flask). Flask nunca instancia componentes do núcleo diretamente.

---

### 9.9 Routes e Templates

Routes web e handlers CLI seguem o mesmo padrão arquitetural — diferem apenas no mecanismo de entrega:

| Aspecto | CLI | Web |
|---|---|---|
| Coleta de input | `click.prompt` | `request.form`, URL params |
| Chamada ao controller | idêntica | idêntica |
| Resposta em sucesso | `click.echo` | `flash` + `redirect` |
| Resposta em erro | `click.secho(fg="red")` | `flash("error")` + `redirect` |

Templates trabalham exclusivamente com ViewModels pré-formatados; não acessam repositories, use cases ou a camada HTTP:

```html
{% for project in projects %}
<div class="card mb-4">
    <div class="card-header">
        <h2 class="card-title h5 mb-0">{{ project.name }}</h2>
    </div>
</div>
{% endfor %}
```

**Regra**: Templates referenciam apenas atributos de ViewModels (strings, booleans pré-calculados). Nunca passem objetos de domínio diretamente para templates.


---

## Capítulo 10 — Implementing Observability: Monitoring and Verification

### 10.1 Observation Points in Clean Architecture

As fronteiras explícitas de camadas criam pontos naturais de observação; cada transição de camada fornece visibilidade específica:

- Web interface — rastreia requests recebidos e suas transformações
- Use cases — monitora operações de negócio e seus resultados
- Domain entities — captura mudanças de estado e aplicação de regras
- Infrastructure — mede utilização de recursos e interações externas

**Regra**: Trate monitoring como extensão estrutural da arquitetura, não como cross-cutting concern.

---

### 10.2 Avoiding Framework Coupling in Logging

Web frameworks (ex.: Flask) oferecem `app.logger`, mas usá-lo cria dependência outward: camadas internas precisariam importar o objeto Flask — violação direta da Dependency Rule.

> ⚠ Evite: `app.logger.info(...)` em use cases ou entidades.

**Regra**: Use `logging.getLogger(__name__)` (módulo padrão Python) em qualquer camada interna; a configuração do handler/formatter fica exclusivamente na camada de Infrastructure.

```python
# todo_app/application/use_cases/task_use_cases.py
import logging
logger = logging.getLogger(__name__)

@dataclass
class CreateTaskUseCase:
    task_repository: TaskRepository
    project_repository: ProjectRepository

    def execute(self, request: CreateTaskRequest) -> Result:
        logger.info(
            "Creating new task",
            extra={"context": {
                "title": request.title,
                "project_id": request.project_id
            }},
        )
        # ... implementation ...
```

---

### 10.3 Structured Logging Patterns

Toda configuração de logging (formatters, handlers, destinos) reside no Infrastructure layer (`todo_app/infrastructure/logging/config.py`). Separar `app.log` (JSON estruturado) de `access.log` (HTTP framework) mantém limites arquiteturais.

#### 10.3.1 JsonFormatter

```python
# todo_app/infrastructure/logging/config.py
class JsonFormatter(logging.Formatter):
    def __init__(self, app_context: str):
        super().__init__()
        self.app_context = app_context
        self.encoder = JsonLogEncoder()

    def format(self, record: logging.LogRecord) -> str:
        log_data = {
            "timestamp": datetime.now(timezone.utc),
            "level": record.levelname,
            "logger": record.name,
            "message": record.getMessage(),
            "app_context": self.app_context,
        }
        context = {}
        for key, value in record.__dict__.items():
            if key == "context":
                context = value
                break
        if context:
            log_data["context"] = context
        return self.encoder.encode(log_data)
```

> 💡 Nota: Use o namespace `context` dentro do parâmetro `extra` para evitar colisões com atributos internos do `LogRecord`.

#### 10.3.2 configure_logging com dictConfig

```python
def configure_logging(app_context: Literal["CLI", "WEB"]) -> None:
    log_dir = Path("logs")
    log_dir.mkdir(exist_ok=True)
    config = {
        "formatters": {
            "json": {"()": JsonFormatter, "app_context": app_context},
            "standard": {"format": "%(message)s"},
        },
        "handlers": {
            "app_file": {
                "class": "logging.FileHandler",
                "filename": log_dir / "app.log",
                "formatter": "json",
            },
            "access_file": {
                "class": "logging.FileHandler",
                "filename": log_dir / "access.log",
                "formatter": "standard",
            },
        },
        "loggers": {
            "todo_app": {"handlers": ["app_file"], "level": "INFO"},
            "werkzeug": {
                "handlers": ["access_file"],
                "level": "INFO",
                "propagate": False,
            },
        },
    }
```

**Regra**: Chame `configure_logging()` no ponto de entrada da aplicação, antes de qualquer outra inicialização (`web_main.py` ou `cli_main.py`).

---

### 10.4 Cross-Boundary Request Tracing

Para correlacionar logs através de múltiplas camadas, gere um `trace_id` único por request e inclua-o em todas as entradas de log.

#### 10.4.1 Gerenciamento de Trace ID com ContextVar

```python
# todo_app/infrastructure/logging/trace.py
from contextvars import ContextVar
from uuid import uuid4

trace_id_var: ContextVar[Optional[str]] = ContextVar("trace_id", default=None)

def get_trace_id() -> str:
    current = trace_id_var.get()
    if current is None:
        current = str(uuid4())
        trace_id_var.set(current)
    return current

def set_trace_id(trace_id: Optional[str] = None) -> str:
    new_id = trace_id or str(uuid4())
    trace_id_var.set(new_id)
    return new_id
```

> 💡 Nota: `ContextVar` oferece armazenamento thread-safe que funciona também em contextos async.

#### 10.4.2 Flask Middleware para Trace ID

```python
# todo_app/infrastructure/web/middleware.py
def trace_requests(flask_app):
    @flask_app.before_request
    def before_request():
        trace_id = request.headers.get("X-Trace-ID") or None
        g.trace_id = set_trace_id(trace_id)

    @flask_app.after_request
    def after_request(response):
        response.headers["X-Trace-ID"] = g.trace_id
        return response
```

**Regra**: Nenhuma alteração é necessária no código de application ou domain para propagar trace IDs — o `JsonFormatter` já inclui o `trace_id_var` em cada entrada de log automaticamente.

---

### 10.5 Fitness Functions — Verifying Layer Structure

Fitness functions são testes automatizados que verificam propriedades arquiteturais, detectando architectural drift antes que comprometa o sistema.

```python
class ArchitectureConfig:
    LAYER_HIERARCHY = ["domain", "application", "interfaces", "infrastructure"]

def test_source_folders(self):
    src_path = Path("todo_app")
    folders = {f.name for f in src_path.iterdir() if f.is_dir()}

    for layer in ArchitectureConfig.LAYER_HIERARCHY:
        self.assertIn(layer, folders, f"Missing {layer} layer folder")

    unexpected = folders - set(ArchitectureConfig.LAYER_HIERARCHY)
    self.assertEqual(
        unexpected,
        set(),
        f"Unexpected folders found: {unexpected}"
    )
```

**Regra**: Execute `pytest tests/architecture` no pipeline de CI para capturar criação de novas pastas fora da estrutura esperada.

---

### 10.6 Fitness Functions — Enforcing Dependency Rules

Use o módulo `ast` do Python para analisar imports e verificar que a Dependency Rule não é violada (camadas internas não importam de camadas externas).

```python
def test_domain_layer_dependencies(self):
    domain_path = Path("todo_app/domain")
    violations = []

    for py_file in domain_path.rglob("*.py"):
        with open(py_file) as f:
            tree = ast.parse(f.read())

        for node in ast.walk(tree):
            if isinstance(node, (ast.Import, ast.ImportFrom)):
                module = node.names[0].name
                if module.startswith("todo_app."):
                    layer = module.split(".")[1]
                    if layer in ["infrastructure", "interfaces", "application"]:
                        violations.append(
                            f"{py_file.relative_to(domain_path)}: "
                            f"Domain layer cannot import from {layer} layer"
                        )

    self.assertEqual(violations, [], "Dependency Rule Violations: " + ", ".join(violations))
```

> ⚠ Evite: Qualquer import em `todo_app/domain/` que referencie `todo_app.infrastructure`, `todo_app.interfaces` ou `todo_app.application`.

**Regra**: Replique testes análogos para cada camada, verificando que nenhuma importa de camada mais externa do que deveria segundo a hierarquia: domain → application → interfaces → infrastructure.

---

## Capítulo 11 — Legacy to Clean: Refactoring Python for Maintainability

### 11.1 Análise Arquitetural Preliminar

Antes de engajar stakeholders, conduza uma análise técnica focada nos problemas que podem ser comunicados em termos de impacto de negócio. O objetivo não é documentar tudo, mas identificar violações-chave.

Elementos de uma análise preliminar:

- **Architectural inventory**: identifique componentes principais e suas interações.
- **Dependency mapping**: esboce fluxos de dependência que revelam circular dependencies e framework coupling.
- **Framework penetration assessment**: exemplifique onde código de framework penetrou na lógica de negócio.
- **Domain logic dispersion**: identifique onde regras de negócio estão fragmentadas no codebase.

**Regra**: Traduza problemas técnicos em impacto de negócio (ex.: "para mudar o cálculo de preço, modificamos 7 lugares em 3 módulos diferentes") antes de apresentar a stakeholders.

> ⚠ Evite: Diagramar cada relação na fase preliminar — detalhe excessivo atrasa o alinhamento com stakeholders sem acrescentar valor real.

---

### 11.2 Alinhamento com Stakeholders

Envolva os stakeholders certos de acordo com a escala da transformação:

- Engineering teams: detalhes técnicos e restrições de implementação
- Product owners: prioridades de negócio e validação de valor arquitetural
- Operations personnel: deployment e confiabilidade
- End users: pain points relacionados à estabilidade e entrega de features

Estabeleça métricas baseline antes de iniciar:

| Categoria | Exemplos de métricas |
|---|---|
| Maintenance | Tempo em bug fixes, lead time de feature delivery |
| Quality | Defect rates, test coverage, static analysis scores |
| Team | Developer onboarding time, deployment frequency |
| Business | Customer satisfaction, feature adoption rates |

**Regra**: Defina métricas antes de começar a transformação — elas são a linguagem para demonstrar progresso para stakeholders não-técnicos.

---

### 11.3 Domain Analysis — Event Storming

Event storming é a técnica mais valiosa para identificar fronteiras arquiteturais em sistemas legados. Participantes usam sticky notes coloridos que mapeiam diretamente para camadas de Clean Architecture:

| Cor | Artefato | Camada de Clean Architecture |
|---|---|---|
| Laranja | Domain Events (ex.: *Order Placed*) | Domain — Entities |
| Azul | Commands (ex.: *Process Payments*) | Application — Use Cases |
| Roxo | Business Rules | Domain — independente de externos |

Outras técnicas colaborativas:
- **Domain Storytelling**: stakeholders narram workflows-chave.
- **Context Mapping**: identifica system boundaries e integration points.

**Regra**: Use event storming para revelar boundaries naturais — separações com padrões de mudança diferentes (ex.: Order vs. Payment) indicam pontos de separação arquitetural.

---

### 11.4 Staged Implementation Roadmap

A transformação ocorre em quatro estágios progressivos:

#### 11.4.1 Foundation Stage

Crie entidades de domínio limpas e interfaces de repositórios/serviços **ao lado** das implementações existentes. Estabelece o target architecture sem alterar o sistema em produção.

#### 11.4.2 Interface Stage

Implemente adapters que fazem ponte entre o núcleo limpo e as preocupações externas: repository implementations para databases existentes, service adapters para integrações de terceiros, controllers que traduzem entre frameworks e domínio.

#### 11.4.3 Integration Stage

Migre funcionalidade existente para a nova arquitetura de forma incremental — feature por feature ou domain por domain. Substitua direct database access por repository implementations, hard-coded business rules por domain services.

#### 11.4.4 Optimization Stage

Refine com base em experiência real: performance em repositories, expansão de test coverage, error handling e resilience patterns. Remova gradualmente feature flags e decomissione legacy code paths.

**Regra**: Trate a transformação como melhoria contínua, não como evento único. Defina métricas de "bom o suficiente" para evitar perfeccionismo interminável.

---

### 11.5 Abordagens de Execução da Transformação

| Abordagem | Descrição | Quando usar |
|---|---|---|
| **Dedicated iterations** | Sprints exclusivas para trabalho arquitetural | Componentes que precisam de mudanças significativas mas que cabem em 1-2 iterações |
| **Parallel tracks** | Time dedicado à arquitetura enquanto outros continuam features | Transformações que se estendem por múltiplos quarters |
| **Opportunity-based** | Melhoria arquitetural integrada ao trabalho de features em áreas relacionadas | Componentes menos críticos ou raramente alterados |

**Regra**: Combine abordagens com base em prioridades de negócio — componentes críticos merecem esforço dedicado; áreas menos alteradas podem evoluir por oportunidade.

---

### 11.6 Navegando a Transformação In-Flight

Durante a transformação, o sistema conterá mistura de abordagens antiga e nova. Para cada componente em transformação, planeje:

- **Parallel operation strategy**: como implementações antiga e nova coexistirão
- **Verification approach**: métodos para confirmar equivalência funcional
- **Cutover criteria**: condições claras para troca para a nova implementação
- **Rollback procedures**: mecanismos de segurança se problemas emergirem

**Regra**: Feature flags são o mecanismo de cutover preferido — permitem habilitar a nova implementação seletivamente e reverter instantaneamente se problemas surgirem.

> ⚠ Evite: "Big bang release" — implementar Clean Architecture completa em isolamento antes de integrar. O sistema de produção evolui durante esse tempo, criando conflitos complexos.

---

### 11.7 Análise do Sistema Legado

Sintomas que indicam problemas arquiteturais em sistemas legados:

- Uma mudança simples em lógica de cálculo requer modificações em múltiplos arquivos.
- Adicionar um novo método de pagamento leva semanas em vez de dias.
- Novos desenvolvedores precisam de meses para se tornarem produtivos.
- Deployments causam efeitos colaterais inesperados em áreas não relacionadas.

Violações típicas identificadas na análise (exemplo de Flask app legada):

```python
# order_system/app.py — violações em um único handler:
@app.route('/orders', methods=['POST'])
def create_order():
    data = request.get_json()
    conn = sqlite3.connect('orders.db')          # infrastructure direta
    product = conn.execute('SELECT ...').fetchone()  # SQL no handler
    total_price = product['price'] * quantity    # lógica de negócio misturada
    payment_result = requests.post(              # HTTP call externo direto
        'https://payment-gateway.example.com/process', ...)
    conn.execute('INSERT INTO orders ...')       # persistência no handler
```

Violações identificadas:
- **Boundary violations**: handler cruza múltiplas fronteiras (web + business logic + infrastructure)
- **Missing domain model**: Order e Product existem apenas como dicts e registros de banco
- **Dependency inversion ausente**: dependências diretas de infraestrutura em vez de abstrações
- **Interface separation ausente**: sem fronteiras claras entre camadas

---

### 11.8 Stage 1 — Estabelecendo Fronteiras de Domínio

Comece pela Domain layer — a fundação estável em torno da qual as camadas externas serão reconstruídas.

#### 11.8.1 Entities e Value Objects

```python
# order_system/domain/entities/order.py
class OrderStatus(Enum):
    CREATED = "CREATED"
    PAID = "PAID"
    FULFILLING = "FULFILLING"
    SHIPPED = "SHIPPED"
    DELIVERED = "DELIVERED"
    CANCELED = "CANCELED"

@dataclass
class OrderItem:
    product_id: UUID
    quantity: int
    price: float

    @property
    def total_price(self) -> float:
        return self.price * self.quantity

@dataclass
class Order:
    customer_id: UUID
    items: List[OrderItem] = field(default_factory=list)
    id: UUID = field(default_factory=uuid4)
    status: OrderStatus = OrderStatus.CREATED
    created_at: datetime = field(default_factory=lambda: datetime.now())
    updated_at: Optional[datetime] = None

    @property
    def total_price(self) -> float:
        return sum(item.total_price for item in self.items)

    def mark_as_paid(self) -> None:
        if self.status != OrderStatus.CREATED:
            raise ValueError(f"Cannot mark as paid: order is {self.status.value}")
        self.status = OrderStatus.PAID
        self.updated_at = datetime.now()
```

```python
# order_system/domain/entities/product.py
@dataclass
class Product:
    name: str
    price: float
    stock: int
    id: UUID = field(default_factory=uuid4)

    def decrease_stock(self, quantity: int) -> None:
        if quantity <= 0:
            raise ValueError("Quantity must be positive")
        if quantity > self.stock:
            raise ValueError(f"Insufficient stock: requested {quantity}, available {self.stock}")
        self.stock -= quantity
```

**Regra**: Mova validações de estado (ex.: "cannot mark non-CREATED order as PAID") para dentro das entidades — *tell, don't ask*.

#### 11.8.2 Abstract Repositories e Services

```python
# order_system/domain/repositories/order_repository.py
class OrderRepository(ABC):
    @abstractmethod
    def save(self, order: Order) -> None: ...
    @abstractmethod
    def get_by_id(self, order_id: UUID) -> Optional[Order]: ...
    @abstractmethod
    def get_by_customer(self, customer_id: UUID) -> List[Order]: ...

# order_system/domain/services/payment_service.py
@dataclass
class PaymentResult:
    success: bool
    error_message: Optional[str] = None

class PaymentService(ABC):
    @abstractmethod
    def process_payment(self, order: Order) -> PaymentResult: ...
```

**Regra**: Defina interfaces de repositório e serviço no Domain layer — o domínio declara o que precisa, sem conhecer implementações concretas.

#### 11.8.3 Estratégias de Integração Incremental

| Estratégia | Descrição |
|---|---|
| **Adapter pattern** | Adapters fazem ponte entre componentes legados e novas entidades de domínio — coexistência sem disrupção |
| **Parallel implementation** | Nova funcionalidade implementada ao lado do legado, com feature flags controlando qual implementação atende cada request |
| **Strangler Fig pattern** | Substitua incrementalmente partes da aplicação legada mantendo as mesmas interfaces externas |
| **Shadow mode** | Proxy duplica requests para nova implementação; resultados comparados com legado sem afetar usuários |

**Regra**: Antes de qualquer mudança arquitetural, estabeleça uma suíte de testes de regressão que capture o comportamento atual do sistema — essa é a rede de segurança da transformação.

---

### 11.9 Stage 2 — Interface Layer Implementation

#### 11.9.1 Repository Adapters

```python
# order_system/infrastructure/repositories/sqlite_order_repository.py
class SQLiteOrderRepository(OrderRepository):
    def save(self, order: Order) -> None:
        conn = sqlite3.connect(self.db_path)
        try:
            cursor = conn.cursor()
            if self._order_exists(conn, order.id):
                # SQL update operation
                ...
            else:
                # SQL insert operation
                ...
            conn.commit()
        except Exception as e:
            conn.rollback()
            raise RepositoryError(f"Failed to save order: {str(e)}")
        finally:
            conn.close()
```

O adapter implementa a interface limpa (`OrderRepository`) enquanto encapsula os detalhes do schema existente — traduz entre domain entities e registros relacionais.

#### 11.9.2 Use Cases

```python
# order_system/application/use_cases/create_order.py
@dataclass
class CreateOrderRequest:
    customer_id: UUID
    items: List[Dict[str, Any]]

@dataclass
class CreateOrderUseCase:
    order_repository: OrderRepository
    product_repository: ProductRepository
    payment_service: PaymentService

    def execute(self, request: CreateOrderRequest) -> Order:
        order = Order(customer_id=request.customer_id)
        for item_data in request.items:
            product_id = UUID(item_data['product_id'])
            quantity = item_data['quantity']
            # inventory validation ...
            product.decrease_stock(quantity)
            self.product_repository.update(product)

        payment_result = self.payment_service.process_payment(order)
        if not payment_result.success:
            raise ValueError(f"Payment failed: {payment_result.error_message}")
        order.mark_as_paid()
        self.order_repository.save(order)
        return order
```

**Regra**: O use case depende de interfaces abstratas (`OrderRepository`, `PaymentService`), nunca de implementações concretas — isso é DIP em ação.

#### 11.9.3 Controllers como Camada de Tradução

```python
# order_system/interfaces/controllers/order_controller.py
@dataclass
class OrderController:
    create_use_case: CreateOrderUseCase

    def handle_create_order(self, request_data: Dict[str, Any]) -> Dict[str, Any]:
        try:
            customer_id = UUID(request_data['customer_id'])
            request = CreateOrderRequest(customer_id=customer_id, items=request_data['items'])
            order = self.create_use_case.execute(request)
            return {'order_id': str(order.id), 'status': order.status.value}
        except ValueError as e:
            # exception logic ...
```

**Regra**: O controller não referencia Flask, HTTP status codes ou JSON formatting — essas são preocupações do framework boundary, não do controller.

---

### 11.10 Stage 3 — Integration Strategy: Feature Flags e Adapter Pattern

```python
# Modified route in order_system/app.py
@app.route('/orders', methods=['POST'])
def create_order():
    data = request.get_json()
    if not data or 'customer_id' not in data or 'items' not in data:
        return jsonify({'error': 'Missing required fields'}), 400
    try:
        if app.config.get('USE_CLEAN_ARCHITECTURE', False):
            result = order_controller.handle_create_order(data)
            return jsonify(result), 201
        else:
            # original implementation remains here
            ...
    except ValidationError as e:
        return jsonify({'error': str(e)}), 400
    except SystemError:
        return jsonify({'error': 'Internal server error'}), 500
```

Padrões-chave desta integração:

- **Feature flag control**: `USE_CLEAN_ARCHITECTURE` alterna entre implementações, permitindo migração gradual de tráfego.
- **Consistent interfaces**: ambas as implementações produzem formatos de resposta idênticos — transição transparente para o usuário.
- **Incremental migration**: o código legado permanece funcional como fallback.
- **Exception translation**: exceções de domínio são mapeadas para respostas HTTP na fronteira do framework.

**Regra**: A configuração de dependency injection (instanciação de repositórios, serviços, use cases e controllers) deve ocorrer no startup da aplicação, no edge do sistema — nunca dentro de controllers ou use cases.

> ⚠ Evite: Substituir o handler legado inteiramente em uma única mudança. Use o Strangler Fig pattern — substitua incrementalmente mantendo as mesmas interfaces externas.

---

### 11.11 Stage 4 — Optimization

A fase de otimização não tem receitas fixas. Princípios:

- Remova feature flags gradualmente à medida que implementações limpas se provam estáveis em produção.
- Decomissione code paths legados após validação completa.
- Priorize otimizações que entregam maior valor de negócio — não busque perfeição arquitetural por si mesma.
- Defina métricas de "bom o suficiente" para encerrar a fase de otimização.

---

## Capítulo 12 — Your Clean Architecture Journey: Next Steps

### 12.1 Python como Plataforma para Clean Architecture

Python reduz o custo de implementação de Clean Architecture sem sacrificar seus benefícios:

- **Duck typing**: interfaces informais sem herança explícita; contratos definidos por comportamento.
- **Type hints**: documentação executável de fronteiras arquiteturais; verificáveis com mypy/pyright.
- **ABCs (`abc.ABC`)**: contratos formais para ports e gateways sem overhead de linguagens estáticas.
- **Dataclasses**: entidades de domínio e value objects sem boilerplate de `__init__`, `__eq__`, `__repr__`.

**Regra**: Use ABCs para definir ports da Application Layer; use Protocols para dependências opcionais ou quando a herança formal seria excessiva.

---

### 12.2 Clean Architecture em Sistemas API-First

#### 12.2.1 Request Models como Contratos Públicos

Em sistemas API-first, o request model da Application Layer torna-se parte do contrato público. O método `to_execution_params()` (convenção usada na CLI) não existe no contexto de API — os parâmetros chegam já validados pelo framework.

```python
@router.post("/tasks", response_model=TaskResponse)
async def create_task(request: CreateTaskRequest, use_case: CreateTaskUseCase = Depends()):
    result = use_case.execute(CreateTaskParams(title=request.title, description=request.description))
    if result.is_failure:
        raise HTTPException(status_code=400, detail=str(result.error))
    return TaskResponse.from_domain(result.value)
```

**Regra**: O route handler é responsável apenas por mapear o request HTTP para os params do use case e mapear o resultado para a resposta HTTP — sem lógica de negócio.

#### 12.2.2 Tradeoff Pydantic — Separação Estrita vs. Pragmatismo

Pydantic pode ser usado em camadas internas (violando a Dependency Rule ao importar uma lib de terceiro no domain) ou apenas na Interface Adapters Layer (separação estrita). O autor documenta ambas as abordagens como válidas dependendo do contexto.

> ⚠ Evite: usar Pydantic `BaseModel` diretamente como entidade de domínio — isso acopla a lógica de negócio a um framework de serialização.

#### 12.2.3 ADR — Documentando Decisões Arquiteturais

Quando pragmatismo exige desvio da separação estrita, documente com um ADR (Architecture Decision Record):

```markdown
# ADR-001: Use Pydantic in Application Layer

## Status: Accepted

## Context
API-first system; all inputs arrive as HTTP requests validated by Pydantic.
Duplicating validation logic in pure domain models adds overhead without benefit.

## Decision
Allow Pydantic BaseModel in Application Layer request/response models only.
Domain entities remain pure Python dataclasses.

## Consequences
- Faster development; single validation point.
- Application Layer carries a Pydantic dependency; replaceable only with effort.
```

**Regra**: Todo desvio deliberado da Dependency Rule deve ser documentado em um ADR com contexto, decisão e consequências explícitas.

---

### 12.3 Arquiteturas Orientadas a Eventos

#### 12.3.1 Domain Events como Cidadãos de Primeira Classe

Domain events representam fatos de negócio que ocorreram. Devem ser definidos no Domain Layer como dataclasses imutáveis.

```python
@dataclass(frozen=True)
class TaskCompletedEvent:
    task_id: str
    completed_at: datetime
    user_id: str
```

#### 12.3.2 Anti-pattern: Entidade Publicando Eventos Diretamente

```python
# ANTI-PATTERN
class Task:
    def complete(self, kafka_publisher):  # viola Dependency Rule
        self.status = "completed"
        kafka_publisher.publish(TaskCompletedEvent(...))
```

> ⚠ Evite: passar publishers de infraestrutura para entidades de domínio. Isso acopla o domain layer à infraestrutura e impossibilita testes unitários puros.

#### 12.3.3 Padrão Limpo: Use Case como Publisher

```python
# Application Layer — port abstrato
class EventPublisher(ABC):
    @abstractmethod
    def publish(self, event: DomainEvent) -> None: ...

# Use case orquestra sem conhecer o broker
class CompleteTaskUseCase:
    def __init__(self, repo: TaskRepository, publisher: EventPublisher):
        self._repo = repo
        self._publisher = publisher

    def execute(self, task_id: str) -> OperationResult:
        task = self._repo.get(task_id)
        task.complete()  # entidade apenas muda estado
        self._repo.save(task)
        self._publisher.publish(TaskCompletedEvent(task_id=task.id, ...))
        return OperationResult.success()

# Frameworks & Drivers Layer — implementação concreta
class KafkaEventPublisher(EventPublisher):
    def publish(self, event: DomainEvent) -> None:
        self._kafka_client.send(topic=event.__class__.__name__, value=asdict(event))
```

**Regra**: Entidades de domínio apenas mudam estado. Use cases orquestram persistência e publicação de eventos via ports abstratos. Implementações concretas de brokers vivem exclusivamente na camada mais externa.

---

### 12.4 Liderança Arquitetural

#### 12.4.1 Traduzindo Benefícios Técnicos para Valor de Negócio

| Benefício Técnico | Valor de Negócio |
|---|---|
| Testabilidade isolada | Ciclos de feedback mais curtos; menos bugs em produção |
| Separação de concerns | Onboarding mais rápido de novos desenvolvedores |
| Independência de frameworks | Flexibilidade para trocar tecnologias sem reescrever regras de negócio |
| Dependency Rule explícita | Menor custo de manutenção a longo prazo |

**Regra**: Ao apresentar Clean Architecture para stakeholders não-técnicos, comece com impacto no negócio — velocidade, custo e risco — não com princípios de design.

#### 12.4.2 Padrões de Resistência e Respostas

| Resistência comum | Resposta recomendada |
|---|---|
| "É abstrato demais" | Mostre um exemplar concreto no codebase da equipe |
| "É overhead demais" | Quantifique o custo atual de mudanças sem a arquitetura |
| "Não temos tempo" | Proponha adoção incremental — um módulo novo por vez |
| "Não vai funcionar aqui" | Identifique um problema real atual e resolva com CA como prova |

**Regra**: Introduza Clean Architecture via **exemplares** — módulos novos construídos com a arquitetura correta, coexistindo com o legado. Permita que a qualidade visível convença a equipe.

> 💡 Nota: Não tente converter a equipe pela teoria. Um único módulo bem-construído faz mais do que horas de apresentação.

#### 12.4.3 Comunidades de Prática

Comunidades de prática (CoPs) são grupos internos voluntários que compartilham aprendizado sobre um domínio técnico. Para propagação de Clean Architecture:

- Sessões regulares de revisão de código com foco em fronteiras arquiteturais.
- Biblioteca interna de exemplares e ADRs — referência viva, não documentação estática.
- Retrospectivas arquiteturais periódicas para avaliar desvios e atualizar decisões.

**Regra**: Documente decisões arquiteturais pragmáticas em ADRs e mantenha-os versionados junto ao código — são a memória institucional da arquitetura.

**Regra**: Trate a transformação como refinamento contínuo, não como projeto com data de conclusão. A arquitetura melhora incrementalmente conforme o sistema evolui.
