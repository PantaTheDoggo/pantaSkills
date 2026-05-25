
# Skill: Agentic Coding with Claude Code — Referência Consolidada

> **Fonte**: Agentic Coding with Claude Code, Eden Marco, Packt, 2025
> **Alvo**: Claude Code, agentic workflows, context engineering
> **Última extração**: 2026-05 (completa)

---

## Índice

| # | Seção |
|---|---|
| 1 | [Context Engineering — Fundamentos](#1-context-engineering--fundamentos) |
| 2 | [Problemas de Contexto Não Gerenciado](#2-problemas-de-contexto-no-gerenciado) |
| 3 | [Hierarquia de Memória de 3 Camadas](#3-hierarquia-de-memria-de-3-camadas) |
| 4 | [Estratégias de Context Engineering no Claude Code](#4-estratgias-de-context-engineering-no-claude-code) |
| 5 | [Context Switching Dinâmico via Hook](#5-context-switching-dinmico-via-hook) |
| 6 | [Sistema de Prompts — Zona Goldilocks](#6-sistema-de-prompts--zona-goldilocks) |
| 7 | [Spec-Driven Design](#7-spec-driven-design) |
| 8 | [Plan Mode](#8-plan-mode) |
| 9 | [Estrutura de Diretório de Memória](#9-estrutura-de-diretrio-de-memria) |
| 10 | [Hierarquia Completa de Memória — 5 Níveis](#10-hierarquia-completa-de-memria--5-nveis) |
| 11 | [Adicionando Entradas de Memória](#11-adicionando-entradas-de-memria) |
| 12 | [Hooks — Tipos e Configuração](#12-hooks--tipos-e-configurao) |
| 13 | [Skills — Slash Commands Customizados](#13-skills--slash-commands-customizados) |
| 14 | [Rewind — Checkpointing e Desfazer](#14-rewind--checkpointing-e-desfazer) |
| 15 | [MCP — Model Context Protocol](#15-mcp--model-context-protocol) |
| 16 | [Plugins — Marketplace e Instalação](#16-plugins--marketplace-e-instalao) |
| 17 | [GitHub Integration — Automação de Workflows](#17-github-integration--automao-de-workflows) |
| 18 | [Agentes Paralelos — Múltiplas Instâncias](#18-agentes-paralelos--mltiplas-instncias) |
| 19 | [Subagents — Configuração e Contexto Isolado](#19-subagents--configurao-e-contexto-isolado) |
| 20 | [Infinite Agentic Loop — Subagentes Paralelos em Escala](#20-infinite-agentic-loop--subagentes-paralelos-em-escala) |
| 21 | [Output Styles — Customização de Formato de Resposta](#21-output-styles--customizao-de-formato-de-resposta) |
| 22 | [Agent Skills — Progressive Disclosure e Composição](#22-agent-skills--progressive-disclosure-e-composio) |
| 23 | [Git Worktrees e Claude Code Desktop](#23-git-worktrees-e-claude-code-desktop) |
| 24 | [Deep Agents — Arquitetura e Características](#24-deep-agents--arquitetura-e-caractersticas) |

---

## 1 Context Engineering — Fundamentos

Context engineering é a evolução natural do prompt engineering: prompts são estáticos, mas o contexto de um agente é dinâmico. O real desafio de engenharia não está na chamada ao LLM, mas no sistema ao redor — o **agent harness** — que gerencia tool calls, loop de execução, erros, guardrails e, principalmente, decide qual contexto enviar ao modelo a cada passo.

Contexto pode vir de múltiplas fontes: instruções do desenvolvedor, entrada do usuário, resultados de ferramentas, e interações anteriores. Em agentes de longa duração, o contexto acumula continuamente, tornando a seleção e compressão críticas.

**Regra**: trate context engineering como disciplina separada de prompt engineering; o harness é onde a maior parte da engenharia real acontece.

---

## 2 Problemas de Contexto Não Gerenciado

Quando o contexto cresce sem controle, surgem três classes de problemas:

| Problema | Descrição |
|---|---|
| **Context poisoning** | Uma alucinação de tool call ou LLM entra no contexto e corrompem outputs futuros |
| **Context confusion** | Contexto irrelevante influencia a resposta mesmo não sendo necessário |
| **Context clash** | Partes do contexto se contradizem, gerando comportamento imprevisível |

Além dos problemas qualitativos, contexto crescente causa: janela excedida, aumento de custo e latência, e degradação progressiva de desempenho.

> ⚠ Evite: deixar o contexto crescer sem estrutura, seleção ou controle em agentes multi-turno.

---

## 3 Hierarquia de Memória de 3 Camadas

Claude Code implementa três camadas de memória persistente:

| Camada | Arquivo | Escopo | Versionado |
|---|---|---|---|
| **Project memory** | `./CLAUDE.md` | Equipe — arquitetura, padrões do projeto | Sim (git) |
| **User memory** | `~/.claude/CLAUDE.md` | Pessoal — preferências e atalhos globais | Não |
| **Dynamic imports** | `@path/to/file.md` | On-demand — carregado via símbolo `@` dentro de qualquer CLAUDE.md | — |

```markdown
# Exemplo de dynamic import em CLAUDE.md
@./context/auth-system.md
@~/global/user/context.md
```

**Regra**: use `@` imports para modularizar contexto por domínio; coloque no CLAUDE.md do nível correto (projeto vs usuário) conforme o escopo desejado.

> ⚠ Evite: usar `>>` em scripts sem checar duplicatas — o CLAUDE.md cresce indefinidamente. Use `grep -qxF` antes de appender.

```bash
add_context() {
  local context_ref="$1"
  grep -qxF "$context_ref" "$CLAUDE_MD" || echo "$context_ref" >> "$CLAUDE_MD"
}
```

---

## 4 Estratégias de Context Engineering no Claude Code

Claude Code aplica quatro estratégias de context engineering:

### 4.1 Write — Memória Persistente

Persistência via hierarquia de três camadas (ver seção 3). Contexto gravado sobrevive entre sessões.

### 4.2 Select — Recuperação Inteligente

Claude varre diretórios automaticamente em busca de arquivos de contexto relevantes. Prioriza arquivos mais recentes e mais frequentemente acessados. Em subpastas, puxa contexto dos diretórios pai mas favorece o mais específico.

Usuários podem adicionar memória persistente via:

```
/memory add Always use descriptive variable names
```

Claude pergunta se a entrada deve ser salva no nível de projeto ou usuário e atualiza o CLAUDE.md correspondente automaticamente.

Antes de editar um arquivo, Claude recupera automaticamente estilo de código existente e funções já presentes. Antes de rodar comandos de terminal, verifica scripts npm existentes e valida caminhos.

### 4.3 Compress — Compressão de Contexto

| Comando | Comportamento |
|---|---|
| `/clear` | Reseta o histórico da conversa atual; preserva project memory e user memory |
| `/compact` | Sumariza a conversa em forma comprimida; mantém decisões-chave, descarta detalhes menores |

**Regra**: use `/compact` quando o contexto acumulou muito mas o trabalho ainda não terminou; use `/clear` quando a direção da conversa ficou ruim ou irrelevante.

### 4.4 Isolate — Subagentes com Contexto Isolado

Cada subagente roda em sua própria janela de contexto isolada, sem herdar o histórico completo do agente principal. O agente principal atua como manager e delega tarefas a especialistas:

```
// Code review agent — focused context
Task(
  description: "Code review",
  prompt: "Review this PR focusing only on security and performance",
  subagent_type: "code-reviewer"
)
```

> 💡 Nota: a sintaxe acima é ilustrativa. Em produção, subagentes são definidos via configuração YAML com frontmatter.

**Regra**: use subagentes para tarefas paralelas ou especializadas; não force o agente principal a fazer tudo de uma vez com todo o contexto disponível.

---

## 5 Context Switching Dinâmico via Hook

Script conectado ao hook `UserPromptSubmit` para carregar contexto baseado em branch Git e conteúdo da query do usuário:

```bash
#!/bin/bash
# context-switcher.sh
CLAUDE_MD="CLAUDE.md"
touch "$CLAUDE_MD"

add_context() {
  local context_ref="$1"
  grep -qxF "$context_ref" "$CLAUDE_MD" || echo "$context_ref" >> "$CLAUDE_MD"
}

# Branch-based context
branch=$(git branch --show-current 2>/dev/null)
case $branch in
  "feature/auth-"*)  add_context "@./context/auth-system.md" ;;
  "feature/payment-"*) add_context "@./context/payment-flow.md" ;;
  "hotfix/"*) add_context "@./context/production-hotfix.md" ;;
esac

# Query-based context
user_input="$1"
if [[ -n "$user_input" ]]; then
  if [[ $user_input == *"database"* || $user_input == *"migration"* ]]; then
    add_context "@./context/database-context.md"
  elif [[ $user_input == *"API"* || $user_input == *"endpoint"* ]]; then
    add_context "@./context/api-context.md"
  fi
fi
```

Configuração do hook em `settings.json`:

```json
{
  "hooks": {
    "UserPromptSubmit": {
      "command": "./scripts/context-switcher.sh \"$PROMPT\"",
      "description": "Dynamically load relevant context based on branch and user query"
    }
  }
}
```

**Regra**: sempre use a função `add_context` com `grep -qxF` para tornar o script idempotente — nunca use `>>` diretamente.

---

## 6 Sistema de Prompts — Zona Goldilocks

Anthropic define a **Goldilocks Zone** como o equilíbrio entre prompts muito específicos e muito vagos.

| Extremo | Problema | Sintoma |
|---|---|---|
| **Muito específico** | Trata o LLM como máquina de estados determinística | Lógica hardcoded, enumeração exaustiva, manutenção custosa, branches rígidos |
| **Muito vago** | Sinal insuficiente para comportamento consistente | Sem guia acionável, assume contexto compartilhado inexistente, limites indefinidos |
| **Meio-termo** | Aproveitado o raciocínio do LLM | Identidade clara, objetivos em vez de prescrições, framework de raciocínio, heurísticas |

**Estrutura de um prompt de nível médio:**

1. **Identidade e escopo claros** — define quem é o agente e o que ele cobre (e o que não cobre)
2. **Empoderar com objetivos, não com regras** — defina a meta; deixe o agente escolher ferramentas
3. **Framework de raciocínio** — passos gerais que funcionam em múltiplos cenários, não lógica de if-else
4. **Princípios como heurísticas** — ex.: "se múltiplas soluções existem, escolha a mais simples"
5. **Limites claros** — ex.: quando escalar para humano, com critério explícito

```
You are a customer support agent for Claude's Bakery.
You specialize in assisting customers with their orders and basic questions.
Use the tools available to you to resolve issues efficiently and professionally.

Response Framework:
1. Identify the core issue
2. Gather necessary context using available tools
3. Provide clear resolution with concrete next steps
4. Confirm satisfaction

Guidelines:
- When multiple solutions exist, choose the simplest one
- For legal issues or health emergencies, call the human assistance tool
```

**Regra**: prefira frameworks de raciocínio a fluxogramas; o LLM aplica princípios gerais a situações novas melhor do que segue scripts rígidos.

> ⚠ Evite: prompts que prescrevem cada passo (hardcoded logic) ou que omitem identidade, escopo e framework de raciocínio — ambos levam a comportamento inconsistente.

---

## 7 Spec-Driven Design

Antes de implementar qualquer funcionalidade, crie um arquivo de especificação que descreve o projeto, casos de uso, requisitos não-funcionais e estrutura de dados. Referencie o spec em cada prompt de implementação usando `@`.

**Workflow:**

1. Ative plan mode (`Shift + Tab`) e selecione um modelo pesado (`/models` → Opus)
2. Descreva o projeto e peça ao Claude para pesquisar e gerar um spec
3. Redirecione o arquivo para `spec/CLAUDE.md` dentro do diretório `memory/`
4. Ao implementar, referencie com `@spec/CLAUDE.md` no prompt

```
Can you please implement the main page grid as specified in the spec file?
@spec/CLAUDE.md
```

Um spec útil inclui: visão geral do projeto, escopo do MVP, modelo de dados, requisitos de UI/UX, arquitetura técnica, user stories e considerações futuras.

**Regra**: use um LLM para ajudar a gerar o spec inicial; isso é um padrão comum — o resultado será mais completo e estruturado do que uma especificação escrita manualmente em pouco tempo.

> ⚠ Evite: iniciar a implementação sem um spec — sem contexto estruturado, Claude produz código inconsistente em sessões longas com múltiplos prompts.

---

## 8 Plan Mode

Plan mode é o modo read-only do Claude Code para pesquisa e planejamento sem nenhuma escrita ou edição de arquivos.

| Ação | Comando |
|---|---|
| Entrar em plan mode | `Shift + Tab` |
| Selecionar modelo | `/models` |
| Sair de plan mode | `Shift + Tab` novamente |

Em plan mode, Claude usa apenas ferramentas de leitura (web search, file read). Nenhuma edição ocorre. Use para:
- Gerar spec antes de implementar
- Explorar o repositório antes de decidir a abordagem
- Pesquisar APIs ou documentação externa

**Regra**: use Opus (ou o modelo de raciocínio mais avançado disponível) em plan mode — a qualidade do plano gerado afeta diretamente a qualidade da implementação subsequente.

> ⚠ Evite: usar plan mode com Haiku ou Sonnet para tarefas complexas de planejamento; use modelos de raciocínio profundo.

---

## 9 Estrutura de Diretório de Memória

Toda memória de longo prazo deve ficar em um único diretório `memory/` dentro do projeto, subdividido por domínio:

```
hookhub/
├── memory/
│   ├── frontend/
│   │   └── CLAUDE.md    ← contexto de frontend
│   └── spec/
│       └── CLAUDE.md    ← especificação do produto
├── app/
└── ...
```

O diretório `memory/` deve ficar **dentro do diretório de trabalho onde Claude Code é aberto**. Se Claude Code for aberto em um diretório pai, referências `@` a arquivos de memória não serão resolvidas.

**Regra**: centralize todo contexto de longo prazo em `memory/`; isso permite reutilização entre sessões e facilita referenciar contextos específicos com `@` em prompts.

> ⚠ Evite: abrir Claude Code no diretório raiz do repositório quando o projeto fica num subdiretório — referências `@` a arquivos de memória não serão resolvidas.

---

## 10 Hierarquia Completa de Memória — 5 Níveis

Claude Code usa uma hierarquia de 5 níveis de memória, carregada de forma cumulativa do nível mais alto ao mais específico. Níveis superiores têm maior prioridade e não podem ser sobrescritos por níveis inferiores.

| Nível | Arquivo | Escopo | Prioridade |
|---|---|---|---|
| 1 — Managed Policy | Sistema (ex: `C:\Program Files\ClaudeCode\CLAUDE.md`) | Org-wide / IT/DevOps | Máxima — não pode ser sobrescrita |
| 2 — User Memory | `~/.claude/CLAUDE.md` | Pessoal, todos os projetos | Alta |
| 3 — Project Memory | `./CLAUDE.md` ou `./.claude/CLAUDE.md` | Equipe, versionado | Média-alta |
| 4 — Project Rules | `./.claude/rules/*.md` | Equipe, versionado | Média (por tópico) |
| 5 — Project Local Memory | `./CLAUDE.local.md` | Pessoal, gitignored | Local override |

**Upward discovery**: ao iniciar, Claude busca arquivos de memória a partir do CWD e sobe em direção à raiz do filesystem. Todos os CLAUDE.md encontrados no caminho são carregados e combinados.

**Lazy loading**: arquivos de memória em subdiretórios abaixo do CWD são carregados somente quando Claude acessa arquivos naquele subdiretório — não são carregados imediatamente ao iniciar.

```
/Users/eden/Desktop/my-company/frontend/   ← CWD
→ Carrega: frontend/CLAUDE.md + my-company/CLAUDE.md + ~/.claude/CLAUDE.md
→ Lazy: backend/CLAUDE.md (carregado só quando backend/ é acessado)
```

**Regra**: use `./.claude/rules/*.md` para separar regras por domínio (segurança, linting, arquitetura) em projetos grandes; use `CLAUDE.local.md` para overrides pessoais sem afetar o time.

> ⚠ Evite: concentrar tudo em um único CLAUDE.md enorme — divida por domínio em `.claude/rules/` para facilitar manutenção e reduzir tokens carregados desnecessariamente.

---

## 11 Adicionando Entradas de Memória

| Método | Uso |
|---|---|
| `# <texto>` no prompt | Claude pede confirmação e armazena no arquivo de memória (projeto ou usuário) |
| `/memory` | Abre o arquivo de memória diretamente no editor para edição manual |
| `/init` | Escaneia o repositório e gera um CLAUDE.md com tech stack, variáveis de ambiente e estrutura |

**Regra**: mantenha arquivos de memória concisos e específicos. Memória excessiva ou vaga desperdiça tokens, confunde o modelo e reduz a qualidade das respostas.

Após adicionar memória, use `/clear` para resetar a conversa e verificar se Claude responde com base na memória armazenada (e não no histórico da conversa).

---

## 12 Hooks — Tipos e Configuração

Hooks são comandos automáticos executados em pontos específicos do workflow do Claude Code.

### Eventos disponíveis

| Evento | Disparo |
|---|---|
| `PreToolUse` | Antes de qualquer tool ser executada |
| `PostToolUse` | Após a execução de uma tool |
| `Notification` | Quando Claude envia notificações |
| `UserPromptSubmit` | Quando o usuário submete um prompt |
| `Stop` | Imediatamente antes de Claude finalizar a resposta |

### Configuração via `/hooks`

1. Abra com `/hooks` e selecione o evento
2. Defina o comando a executar
3. Selecione o escopo: projeto (`.claude/settings.json`) ou usuário

```json
{
  "hooks": {
    "Stop": [
      {
        "matcher": "",
        "hooks": [
          {
            "type": "command",
            "command": "uv run /path/to/play_sound.py"
          }
        ]
      }
    ]
  }
}
```

`"matcher": ""` significa que o hook se aplica a todos os eventos do tipo, sem filtro adicional. Após configurar, reinicie Claude Code para carregar as novas configurações.

**Regra**: mantenha hooks de alta frequência (Stop, PostToolUse) leves — prefira comandos nativos (`afplay sound.wav` no macOS, `aplay` no Linux) a scripts Python com dependências pesadas para evitar latência.

> ⚠ Evite: hooks pesados em eventos de alta frequência; hooks podem bloquear ações, modificar comportamento e disparar subagentes — teste isoladamente antes de ativar.

---

## 13 Skills — Slash Commands Customizados

Skills são prompts reutilizáveis invocados como slash commands (`/nome-da-skill`). São armazenadas como arquivos Markdown com frontmatter YAML.

### Estrutura de arquivos

```
.claude/
└── skills/
    └── commit-code/
        └── SKILL.md
```

### Formato de SKILL.md

```markdown
---
allowed-tools: Bash(git add:*), Bash(git status:*), Bash(git commit:*)
description: Create a git commit
---

## Context
- Current git status: !`git status`
- Current git diff: !`git diff HEAD`
- Current branch: !`git branch --show-current`
- Recent commits: !`git log --oneline -10`

## Your task
Based on the above changes, create a single git commit.
```

- Frontmatter (entre `---`) é avaliado antes do corpo do prompt
- `!``comando``` executa o comando e injeta o output como contexto (padrão RAG: retrieve → generate)
- `$ARGUMENTS` é substituído pelo que o usuário passa após o nome da skill: `/commit-code custom code`
- `allowed-tools` restringe quais ferramentas a skill pode usar (princípio do menor privilégio)

**Regra**: sempre defina `allowed-tools` em skills que executam ações com efeito colateral (git, filesystem, bash); sem restrição, um contexto envenenado pode fazer o agente executar ações não intencionais com acesso total.

> ⚠ Evite: omitir `allowed-tools` no frontmatter de uma skill — sem restrição de tools, contexto envenenado pode fazer o agente executar ações não intencionais com acesso total.

---

## 14 Rewind — Checkpointing e Desfazer

Claude Code cria um checkpoint automático antes de cada edição de arquivo. O rewind permite reverter para qualquer ponto da sessão.

**Invocar**: pressione `Esc × 2` ou use `/rewind`.

### Opções de restauração

| Opção | Efeito |
|---|---|
| Restore code + conversation | Reverte arquivos e histórico da conversa (mais comum) |
| Restore conversation only | Reverte o histórico, mantém as edições de arquivo |
| Restore code only | Reverte arquivos, mantém o histórico da conversa |

- Checkpoints persistem por 30 dias
- Após restaurar apenas o código, o contexto da conversa permanece — é possível re-emitir o prompt com ajustes

### Limitações

- Comandos bash executados pelo Claude não são rastreados (não podem ser revertidos)
- Edições manuais feitas fora do Claude Code não são capturadas
- Não substitui git — é undo local de curto prazo, não histórico permanente

**Regra**: use rewind como rede de segurança para experimentos; quando a mudança for definitivamente indesejada, combine rewind com git para um histórico limpo.

---

## 15 MCP — Model Context Protocol

MCP é uma camada de abstração padronizada que permite que agentes de IA se conectem a ferramentas, fontes de dados e serviços através de uma interface comum. Uma funcionalidade implementada uma vez em um MCP server é reutilizável em qualquer cliente MCP-compatível (Claude Code, Cursor, GitHub Copilot, etc.) sem reimplementação.

### Arquitetura central

| Componente | Papel |
|---|---|
| **MCP Host** | Aplicação de IA com suporte a MCP (ex: Claude Code, Cursor) |
| **MCP Client** | Reside no host; gerencia a comunicação com MCP servers |
| **MCP Server** | Gateway que expõe tools, resources e prompts via protocol MCP |

Um MCP server implementa métodos como `listTools`, `callTool`, `listPrompts`, `getPrompt`, `listResourceTemplates`, e mecanismos de progress notification.

### Escopos de configuração MCP

| Escopo | Config location | Versionado | Compartilhado |
|---|---|---|---|
| **Project-scope** | `.mcp.json` na raiz do projeto | Sim | Sim (equipe) |
| **User-scope** | `~/.claude/settings.json` | Não | Não |
| **Session-scope** | `--mcp-config` flag ou adicionado mid-session | Não | Não |

- **Project-scope**: MCP servers compartilhados com o time; adequado para servidores sem segredos sensíveis.
- **User-scope**: servidores de uso geral disponíveis em todos os projetos (ex: Tavily, Context7).
- **Session-scope**: servidores temporários, experimentais, ou com tokens de curta duração (OAuth, CI/CD).

### Context engineering com MCP

Cada MCP server carregado injeta as definições de suas tools no context window antes de qualquer prompt — consumindo tokens mesmo quando as tools não são necessárias.

**Scoped config**: em vez de um `.mcp.json` geral, crie arquivos separados por tarefa:

```bash
# Usar apenas Tavily (pesquisa) nesta sessão:
claude --mcp-config .mcp.json.tavily

# Forçar uso exclusivo do arquivo especificado (ignora hierarquia user/project):
claude --mcp-config .mcp.json.tavily --strict-mcp-config
```

Com `--strict-mcp-config`, o uso de tokens de MCP pode cair de ~20% para ~2.4% do context window.

**Desabilitar dinamicamente**: dentro de uma sessão, MCP servers podem ser habilitados/desabilitados via CLI sem modificar arquivos de configuração.

**Regra**: sempre escope a configuração MCP para a tarefa em mãos; nunca carregue todos os servidores em todas as sessões. Prefira `--strict-mcp-config` quando a tarefa usa apenas um servidor específico.

> ⚠ Evite: uma única configuração `.mcp.json` genérica que carrega todos os MCP servers em todas as sessões — pode consumir dezenas de milhares de tokens antes do primeiro prompt.

### Limitações do MCP

| Limitação | Descrição |
|---|---|
| **Context pollution** | Definições de todas as tools são pré-carregadas no system prompt; 58 tools podem consumir 55K tokens antes de qualquer mensagem |
| **Ping-pong pattern** | Cada tool call exige um round trip completo: model → execute → result → model. Resultados intermediários acumulam no context |
| **Native tongue problem** | LLMs são treinados em código/linguagem natural, não em tokens de tool-call JSON. Muitas tools ou tools complexas degradam a seleção e o uso correto |
| **Schemas sem intent** | JSON schemas descrevem estrutura, não padrões de uso — quando usar, como usar em contexto, quando não usar |

### CodeMode (alternativa Cloudflare)

Em vez de expor tools diretamente ao LLM, converte as definições MCP em uma TypeScript API e pede ao LLM que gere código contra essa API:

```
Fluxo tradicional MCP:
  tool schemas → LLM gera tokens de tool call → parse → execute → repete

Fluxo CodeMode:
  tool schemas → TypeScript API → LLM escreve código → executa em sandbox → resultado final
```

Vantagem: LLMs têm vasto treinamento em TypeScript real; round trips reduzidos; tools complexas encadeadas em um único bloco de código. O código executa em sandbox isolado que acessa serviços externos apenas através das APIs fornecidas.

**Regra**: ao expor muitas tools ou tools com chamadas encadeadas, considere CodeMode — LLMs escrevem código melhor do que escolhem tool calls diretamente.

---

## 16 Plugins — Marketplace e Instalação

Plugins empacotam slash commands (skills), subagents, MCP servers e hooks em um único primitivo instalável e compartilhável. Eliminam o processo manual de copiar configurações entre projetos.

### Estrutura de um plugin

```
plugin-repo/
└── .claude-plugin/
    ├── marketplace.json   ← registry de plugins disponíveis
    └── plugins/
        └── feature-dev/
            └── .claude-plugin/
                └── plugin.json   ← metadata + componentes do plugin
```

### Comandos de gerenciamento

| Ação | Comando |
|---|---|
| Abrir interface | `/plugin` |
| Adicionar marketplace | `/plugin` → Browse → Add Marketplace → URL do repo ou marketplace.json |
| Instalar plugin | `/plugin` → Browse → selecionar plugin → Install |
| Instalar componente individual | `/plugin` → selecionar plugin → instalar apenas MCP server ou slash command |
| Atualizar plugin | selecionar plugin instalado → Update |

### Segurança de plugins

Antes de instalar qualquer plugin:
1. Abra o `marketplace.json` e localize o campo `source` do plugin.
2. Navegue até o diretório `source` no repositório.
3. Inspecione o `plugin.json` — verifique os agentes, slash commands e hooks que serão instalados.

> ⚠ Evite: instalar plugins sem revisar a implementação — assim como MCP servers, plugins executam código local e podem conter instruções maliciosas no campo `description` de subagents que serão appendadas ao system prompt do agente principal.

**Regra**: trate plugins de fontes desconhecidas com o mesmo nível de cuidado que pacotes npm de terceiros — sempre inspecione o código antes de instalar.

---

## 17 GitHub Integration — Automação de Workflows

Claude Code se integra ao GitHub via GitHub Actions, permitindo que Claude seja invocado em issues e pull requests diretamente no repositório.

### Instalação

Pré-requisitos:
1. GitHub CLI instalado (`brew install gh` ou equivalente para o SO).
2. GitHub CLI autenticado: `gh auth login` (selecione HTTPS, autentique via browser).
3. Claude Code aberto a partir de um diretório com repositório Git conectado ao GitHub.

```bash
# Iniciar instalação dentro do Claude Code:
/install-github-app
```

O processo instala o app Claude no GitHub e cria automaticamente um PR com dois arquivos:
- `.github/workflows/claude.yml` — workflow acionado por `issue_comment`
- `.github/workflows/claude-code-review.yml` — review automático em novos PRs

```yaml
# Estrutura simplificada de claude.yml:
name: Claude Code
on:
  issue_comment:
    types: [created]
jobs:
  claude:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: anthropics/claude-code-action@beta
        with:
          claude_code_oauth_token: ${{ secrets.CLAUDE_CODE_OAUTH_TOKEN }}
```

O token é armazenado como GitHub Actions secret — nunca diretamente no workflow file.

### Uso: resolver issues via @claude

```
@claude, can you fix this
```

Claude cria automaticamente uma branch `claude/issue/<issue-number>`, nunca trabalha direto em main. Você mantém controle total sobre revisar, modificar e dar merge nas mudanças.

**Regra**: revise sempre as mudanças propostas pelo Claude antes de fazer merge — sem contexto suficiente do repositório, Claude pode introduzir breaking changes (ex: renomear variáveis que fazem parte de contratos com APIs externas).

> ⚠ Evite: aceitar PRs gerados pelo Claude sem revisão — agentic workflows automatizam rapidamente mas erram quando falta contexto.

### CLAUDE.md como contexto para issues

Adicione contexto explícito ao repositório antes de acionar Claude em issues complexas:

```bash
# Gerar CLAUDE.md com scan do repositório:
/init
```

Claude escaneia a estrutura do projeto, stack tecnológico e convenções de código, depois gera e commita o `CLAUDE.md`. Com esse contexto disponível, a resolução de issues melhora significativamente porque Claude entende o domínio do projeto.

**Regra**: commite o `CLAUDE.md` no repositório — isso versiona o contexto, compartilha com o time e torna-o disponível em workflows automatizados via GitHub Actions.

---

## 18 Agentes Paralelos — Múltiplas Instâncias

Claude Code suporta múltiplas instâncias simultâneas para paralelizar tarefas independentes no mesmo projeto.

### Quando usar paralelismo

| Adequado para paralelismo | Não adequado para paralelismo |
|---|---|
| Bugs independentes em módulos separados | Feature full-stack (frontend depende do backend) |
| Componentes de UI em arquivos separados | Mudanças no mesmo arquivo |
| Seções independentes de documentação | Refatorações que alteram interfaces compartilhadas |

**Regra**: a eficácia do paralelismo depende de tasks verdadeiramente independentes. Identifique as dependências antes de atribuir tarefas — tasks sequenciais nunca devem ser executadas em paralelo.

### Execução prática

```bash
# Terminal 1:
claude
# Prompt: Improve the visual design of HookCard.
# Modify only: src/components/HookCard.tsx. Do not modify other files.

# Terminal 2:
claude
# Prompt: Redesign the hero section.
# Modify only: src/components/Hero.tsx. Do not modify HookCard.tsx.
```

Cada instância tem acesso de leitura e escrita ao codebase completo. Para evitar conflitos, isole os arquivos que cada agente pode modificar explicitamente no prompt.

> ⚠ Evite: múltiplos agentes modificando o mesmo arquivo — use Git worktrees para isolamento robusto em ambientes de produção (cada agente em seu próprio branch e working directory).

**Especificação como contexto compartilhado**: exporte o plano gerado em plan mode para um arquivo Markdown e persista em `.claude/` — isso garante contexto consistente quando múltiplos agentes trabalham no mesmo projeto.

```bash
# Persitir spec gerada em plan mode:
# Em plan mode (Shift+Tab), gere a spec e instrua Claude a salvar em:
# memory/spec/CLAUDE.md
```

---

## 19 Subagents — Configuração e Contexto Isolado

Subagents são personalidades de IA pré-configuradas às quais o Claude Code principal pode delegar tarefas. Cada subagent tem seu próprio system prompt, seu próprio context window e seu próprio conjunto de tools permitidas.

### Estrutura de arquivos

```
.claude/agents/          ← project-level (versionado, compartilhado)
    code-reviewer.md
~/.claude/agents/        ← user-level (todos os projetos)
    mermaid-diagram.md
```

### Formato de definição

```markdown
---
name: code-reviewer
description: >
  Senior code reviewer. Analyzes changes for bugs, security flaws, and
  convention violations. Invoke after any code modification.
  Use when user says "funny review" or "code review".
tools: Read, Grep, Glob, Bash
model: sonnet
color: yellow
---

You are a meticulous code reviewer for this project...
## Workflow
1. Execute `git diff --staged` to capture changes
...
```

Campos do frontmatter:
- `name` (obrigatório) — identificador único
- `description` (obrigatório) — controla QUANDO o agente principal invoca este subagent E como constrói o prompt para ele
- `tools` — lista de tools permitidas; se omitido, todas as tools ficam disponíveis
- `model` — `inherit` usa o modelo do agente principal; pode especificar `sonnet`, `haiku`, etc.
- `color` — identificação visual no CLI

### Fluxo de contexto

O subagent recebe **apenas o prompt gerado pelo agente principal** — ele não tem acesso ao histórico completo da conversa.

```
Main agent context (acumula com cada turno)
    ↓ gera um prompt para o subagent
Subagent context (fresh, isolado)
    ↓ executa task, retorna resultado condensado
Main agent context (recebe apenas o artefato final)
```

Isso mantém o main context lean: tokens consumidos internamente pelo subagent não se acumulam na conversa principal.

**Regra**: o campo `description` é o mecanismo central de controle — ele instrui tanto QUANDO o agente principal invoca o subagent quanto COMO formula o prompt enviado a ele. Refine a `description` para influenciar a qualidade da delegação.

> ⚠ Evite: tool pollution — provisionar subagents com mais tools do que o necessário. Cada definição de tool adiciona tokens ao context window do subagent e amplia desnecessariamente sua superfície de ação. Aplique o princípio do menor privilégio.

> ⚠ Evite: instalar subagents de fontes não confiáveis sem revisar a `description` — o campo é appendado ao system prompt do agente principal e pode conter instruções maliciosas que executam ações não intencionais na máquina local.

### Execução paralela de subagents

Por padrão, Claude Code pode executar subagents sequencialmente mesmo quando parecem independentes. Para forçar execução paralela, deixe a independência explícita no prompt:

```
# Sequencial (Claude pode serializar):
create 2 funny code reviews of @main.py

# Paralelo explícito (mais provável de executar concorrentemente):
create separate review agents for each file and run them in parallel
```

---

## 20 Infinite Agentic Loop — Subagentes Paralelos em Escala

O padrão Infinite Agentic Loop usa um **high-order prompt** que recebe um prompt como input e gera múltiplos prompts como output, spawning subagents paralelos cada um com sua variação única.

### Estrutura do slash command `/infinite`

```
/infinite @specs/hero.spec.md @src/components/heros/ 6
```

Três inputs via `$ARGUMENTS`:
- `spec_file` — Markdown com a especificação do que implementar
- `output_dir` — diretório onde cada subagent grava seu artefato
- `count` — número de subagents; `"infinite"` para execução contínua

### Fases de execução (orquestradas pelo agente principal)

| Fase | Ação do agente principal |
|---|---|
| **1 — Spec analysis** | Lê e compreende profundamente o spec file |
| **2 — Directory reconnaissance** | Lista arquivos existentes, identifica numeração, analisa evolução das iterações anteriores |
| **3 — Iteration strategy** | Define nomes/números únicos; para count 6-20, lança em batches de 5; para "infinite", lança waves de 3-5 |
| **4 — Parallel execution** | Usa a task tool para spawnar todos os subagents simultaneamente; monitora progresso; lida com falhas |

### Estrutura do prompt de cada subagent

Cada subagent recebe um prompt contendo:
- Spec completo analisado
- Snapshot do `output_dir` no momento do launch (para evitar duplicatas)
- Número/nome de iteração único
- Instrução de unicidade (evitar conceitos já implementados)
- Padrões de qualidade do spec

```
⚠ Token cost: cada subagent consome tokens independentemente.
  6 subagents ≈ 6× o custo de um único agente.
  Monitore o uso ao usar Anthropic API key (não max mode).
```

**Regra**: após spawning paralelo, limpe o context (`/clear`) antes de dar instruções subsequentes — o context principal fica bloated após coordenar múltiplos subagents.

---

## 21 Output Styles — Customização de Formato de Resposta

Output styles substituem partes do system prompt do Claude Code com instruções de formatação específicas, alterando como o modelo estrutura e comunica suas respostas.

### Localização e escopo

| Escopo | Diretório | Aplicação |
|---|---|---|
| **User** | `~/.claude/output-styles/` | Todos os projetos do usuário |
| **Project** | `.claude/output-styles/` | Apenas o projeto atual (sobrepõe user) |

### Formato do arquivo de style

```markdown
---
description: Concise bullet-point responses with direct communication
---

# Communication Style
- Use bullet points for all responses
- Be direct and to the point

# Response Format
- Lead with the answer
- Use nested bullets for hierarchy

# Workflow
Save the HTML file after writing it, ending with .html
OPEN the generated file in the default web browser.
```

A seção `Workflow` embute comportamento automático — Claude executará essas ações sem que o usuário precise repetir a instrução a cada prompt.

### Comandos

```bash
/output-style          # listar e selecionar estilos disponíveis
```

### Como output styles funcionam

Ao selecionar um output style, Claude Code remove suas instruções padrão de software engineering do system prompt e substitui pelo conteúdo do arquivo de style. As capacidades core (file operations, bash) permanecem disponíveis.

### YAML como output style

YAML transforma comunicação de instruções explícitas em estrutura semântica implícita. A hierarquia, indentação, escolha de chaves e ordering carregam significado:

```yaml
# Resposta de Claude com YAML output style ativo:
task: "Fix authentication bug"
fix:
  files_to_modify:
    auth.js:
      scope: "token refresh logic"
      risk: "low"
    middleware.js:
      scope: "validation checks"
      risk: "urgent"
  dependencies: [*flow]
verify:
  tests: ["auth_integration", "token_expiry"]
metadata:
  estimated_time: "2 hours"
  rollback_plan: "revert commits"
```

YAML encoda dependências (parent-child), prioridade (ordering), e escopo (nesting) — em vez de listar passos sequenciais, representa a arquitetura lógica do problema.

**Criação de output style YAML**:

```bash
# Criar .claude/output-styles/yaml-concise.md com:
---
description: Structured YAML responses encoding relationships
---
# Response Format
- All responses must be formatted as valid YAML
- Use hierarchy and nesting to express relationships
- Keep values concise — no full sentences unless necessary
# Tone
- No prose, no filler, no transitional language
```

**Regra**: use output styles para definir o protocolo de comunicação para uma sessão inteira; embuta workflow rules (salvar arquivo, abrir browser) no style para eliminar instruções repetitivas.

> ⚠ Evite: usar output styles com formatos que tornam o output ilegível no terminal (ex: HTML puro) sem também embedar no style a instrução para salvar em arquivo e abrir no browser.

---

## 22 Agent Skills — Progressive Disclosure e Composição

Agent skills empacotam workflows reutilizáveis como unidades estruturadas que o agente pode invocar dinamicamente. Ao contrário de MCP (tools sempre no context) ou CLAUDE.md (sempre carregado), skills usam **progressive disclosure**: apenas o frontmatter é injetado no system prompt permanentemente; o corpo do SKILL.md e scripts auxiliares carregam **somente quando a skill é ativada**.

### Estrutura de arquivo

```
.claude/skills/<nome-da-skill>/
    SKILL.md          ← definição da skill (frontmatter + workflow)
    scripts/
        smart_commit.sh   ← scripts opcionais executáveis pelo agente
```

### Formato de SKILL.md

```markdown
---
name: git-pushing
description: Stage, commit, and push git changes with conventional commit
  messages. Use when user wants to commit and push changes, mentions pushing
  to remote, or asks to save and push their work.
---

# Git Push Workflow
**ALWAYS use the script** - do NOT use manual git commands:
bash skills/git-pushing/scripts/smart_commit.sh
```

O frontmatter entre os delimitadores `---` é a única parte injetada no system prompt em cada request. O restante do arquivo (workflow, scripts) só carrega quando a skill é selecionada pelo agente.

### Progressive disclosure — modelo em 3 fases

1. **Sempre visível**: frontmatter (`name`, `description`) — usado para decisão de invocação
2. **Carga sob demanda**: corpo do SKILL.md (workflow, instruções) — carregado após seleção
3. **Carga condicional**: scripts mencionados no workflow — carregados apenas quando o agente decide executá-los; scripts não usados permanecem fora do context

**Regra**: para alterar quando uma skill é invocada, edite o campo `description` no frontmatter — é o único campo que afeta a seleção. Edições no corpo do SKILL.md (como adicionar trigger phrases em `## When to Use`) não afetam a seleção porque esse conteúdo só carrega após a skill já ter sido escolhida.

### Opções de frontmatter adicionais

| Campo | Efeito |
|---|---|
| `disable-model-invocation: true` | Skill só pode ser invocada via slash command; nunca automaticamente pelo modelo |
| `context: fork` | Executa a skill em um contexto de subagent isolado em vez do main agent thread |
| `agent: Explore` | Especifica o tipo de subagent usado quando `context: fork` está ativo |

### Workflows compostos com scripts

Skills podem encapsular workflows complexos como scripts determinísticos, criando uma composição em camadas: **agente principal → skill → script → Claude CLI**:

```bash
# Script que usa o Claude CLI para gerar mensagem de commit:
commit_msg=$(claude -p "Generate a conventional commit message for: $(git diff --staged --stat)")
git commit -m "$commit_msg"
```

A skill não implica IA internamente — pode conter lógica puramente determinística. Quando o script falha, o agente cai de volta ao comportamento padrão e tenta completar a task via raciocínio base.

**Regra**: skills que caminham por estruturas de diretório funcionam mesmo quando a estrutura declarada em SKILL.md está desatualizada — o agente raciocina sobre o projeto e localiza o arquivo. A única falha irrecuperável é o arquivo literalmente não existir.

> ⚠ Evite: habilitar aprovação automática para skills antes de entender completamente o que elas executam — aprovação automática elimina o checkpoint de revisão humana.

### Comparação: skills vs outros primitivos

| Dimensão | Skills | MCP | Subagents | Slash Commands |
|---|---|---|---|---|
| **Propósito** | Padronizar como tasks são feitas | Conectar a serviços externos | Delegar trabalho isolado | Atalhos do usuário |
| **Execução** | Main agent thread | MCP server (local/remoto) | Contexto de subagent isolado | Main agent thread |
| **Isolamento de contexto** | Compartilha context principal | Execução externa | Totalmente isolado | Compartilha context principal |
| **Scripts** | Sim | Não | Sim | Não |
| **Context efficiency** | Alto (lazy-loading) | Baixo (tools pré-carregadas) | Alto (trabalho offloaded) | Baixo (prompt completo sempre) |
| **Melhor para** | Workflows repetíveis | APIs externas ou services | Tasks de longa duração | Ações rápidas do usuário |

---

## 23 Git Worktrees e Claude Code Desktop

Claude Code Desktop integra o engine do Claude Code diretamente ao aplicativo Claude com dois modos de execução.

### Modos de operação

| Modo | Execução | Configuração |
|---|---|---|
| **Local Worktree** | Tudo na máquina local via Git worktrees | Selecionar pasta do projeto |
| **Cloud (Background Agents)** | Instâncias containerizadas na infraestrutura Anthropic | Autorizar acesso ao repositório GitHub |

Cloud mode: Anthropic clona o repositório, trabalha no código, commita e cria PRs — como qualquer outro desenvolvedor no projeto. Permite múltiplas instâncias paralelas escaláveis.

### Git Worktrees — conceito central

Git Worktrees permitem fazer checkout de múltiplos branches do mesmo repositório em diretórios separados simultaneamente, sem clonar o repositório:

```
repo/
├── hookhub/                  ← branch: project/hookhub (principal)
├── vigilant-fiestel/         ← branch: vigilant-fiestel (worktree 1)
└── zealous-jemison/          ← branch: zealous-jemison (worktree 2)
```

Cada Claude Code instance opera em seu próprio worktree/branch. Commits vão para o branch do worktree, não para o branch principal — o branch principal permanece intocado até o merge explícito.

### Fluxo de trabalho com worktrees paralelos

1. Identifique tasks verdadeiramente independentes (arquivos diferentes, sem dependências)
2. Inicie um Claude Code instance por task, cada um em seu worktree
3. Cada agente commita em seu branch isolado
4. Após conclusão, valide localmente antes de fazer merge
5. Faça merge dos branches no branch-alvo (Claude pode coordenar o processo)
6. Limpe os diretórios de worktree após o merge

```bash
# Merge via Claude Code (ao delegar):
# "Merge all commits to branch project/hookhub"
# Claude cria branch de integração temporária (project/hookhub-merge)
# → resolve conflitos → testa → push para target branch

# Verificar antes de autorizar push:
git fetch && git pull
npm run dev
```

### Quando NÃO usar agentes paralelos

| Situação | Por quê não paralelizar |
|---|---|
| Features tightly coupled (B depende da interface de A) | Agente B consumirá API inexistente; cria discrepâncias |
| Mudanças no mesmo arquivo | Conflitos de merge inevitáveis |
| Migrações de database, mudanças em config compartilhado | Ordering constraints — sequencial é obrigatório |
| Trabalho exploratório / debugging | Incerteza se multiplica; uma sessão focada é mais eficaz |
| Specs tão detalhados para evitar conflitos que consomem mais tempo que o paralelismo economiza | O overhead de coordenação supera o ganho |

**Checklist de desenvolvimento paralelo:**
1. Verificar que cada task opera em arquivos/componentes independentes
2. Especificar o branch correto no prompt de cada agente
3. Testar o resultado merged localmente antes de push para o branch-alvo
4. Limpar diretórios de worktree após merge

**Regra**: comece sequencial; paraleleze somente após confirmar que as tasks não interagem. Git worktrees são o mecanismo de isolamento correto para paralelismo robusto em produção.

> ⚠ Evite: múltiplos agentes no mesmo branch sem worktrees em produção — conflitos de merge são inevitáveis e difíceis de rastrear retroativamente.

### Status line — exibir contexto dinâmico

Claude Code suporta scripts executáveis como status line, recebendo JSON via stdin:

```python
# ~/.claude/statusline.py
import json, sys, os

def get_last_user_prompt(transcript_path):
    if not os.path.exists(transcript_path):
        return "No transcript"
    with open(transcript_path, "r") as f:
        lines = f.read().strip().split("\n")
    for line in reversed(lines):
        try:
            entry = json.loads(line)
            if entry.get("type") == "message" and entry.get("role") == "user":
                content = entry.get("message", {}).get("content", "")
                if not content.startswith("/"):
                    return content[:80]
        except json.JSONDecodeError:
            continue
    return "No prompt"

input_data = json.load(sys.stdin)
style = input_data.get("output_style", "default")
prompt = get_last_user_prompt(input_data.get("transcript_path", ""))
print(f"\033[1;32m[{style}]\033[0m {prompt}")
```

Configuração em `~/.claude/settings.json`:

```json
{
  "statusline": { "type": "command", "command": "uv run ~/.claude/statusline.py" }
}
```

Transcripts ficam em `~/.claude/projects/<project-path>/` como arquivos JSONL; cada linha é um objeto JSON com `type`, `role`, `message`.

---

## 24 Deep Agents — Arquitetura e Características

### Taxonomia de agentes

| Categoria | Exemplos | Característica |
|---|---|---|
| **Shallow agents (ReAct)** | Agentes simples de tool-use | Context acumula a cada turno; adequados para tasks de poucas iterações |
| **Deep Agents** | Claude Code, Devin, LangChain DeepAgents | Long-horizon tasks; execução de minutos/horas; pausam e retomam |
| **Coding agents** | Claude Code, Cursor, Gemini CLI | Subconjunto de Deep Agents especializado em software development |

### Limitação dos shallow agents

O loop ReAct (Reason → Act → Observe) acumula resultados de tool calls no context window. Para tasks complexas, esse acúmulo leva a context rot: contradições, confusão, ruído excessivo — degradação de qualidade antes do limite de tokens.

### O que torna um agente "deep"

Deep Agents implementam quatro capacidades que endereçam o acúmulo de contexto:

**1. Planning tool**
Explícito, implementado como to-do list em Markdown. Em Claude Code: `TodoWrite` (cria/atualiza lista) e `TodoRead` (lê lista). O agente revisa e atualiza o plano entre steps — não blind retry em falhas, mas replanejamento controlado.

**2. Subagents com hierarquia**
O agente principal delega subtasks para subagents especializados, cada um com seu próprio context window. O agente principal recebe apenas o artefato final — os steps intermediários do subagent não poluem o main context.

**3. Filesystem como context engine**
O filesystem resolve o problema de seleção de contexto — o que extrair de um espaço de informação vasto para o context window limitado:

```
[Toda informação disponível] ← filesystem completo
        ↓ glob/grep (seleção precisa)
[Informação selecionada] ← o que o agente puxa para o context
        ↓ deve cobrir completamente
[Informação necessária] ← o que a task realmente precisa
```

Failure modes: under-retrieval (perde informação necessária), over-retrieval (ruído excessivo), misaligned retrieval (busca no lugar errado), context window saturado.

**Regra**: a qualidade de um Deep Agent é limitada pela seleção de contexto — mesmo o melhor modelo retorna resultados incorretos com contexto incompleto ou incorreto.

**4. System prompt abrangente**
Um system prompt eficaz para Deep Agents estabelece identidade e escopo claros, empodera com objetivos (não listas de passos), fornece framework de raciocínio reutilizável (não flowchart), usa heurísticas comprimidas ("escolha sempre a solução mais simples") e mantém eficiência de linguagem.

**Regra**: harness engineering (orquestração e gerenciamento do agente) é onde ocorre a maior parte da inovação em Deep Agents — a inovação está na camada de aplicação, não no modelo base.

> ⚠ Evite: tratar Deep Agents como shallow agents com mais steps — sem planning tool, filesystem e isolamento de contexto via subagents, a execução de long-horizon tasks inevitavelmente degrada.
