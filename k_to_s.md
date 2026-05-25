# Skill: k_to_s — Knowledge to Skill

> **Propósito**: Ler um livro ou documento (PDF, EPUB ou TXT) capítulo a capítulo e gerar ou enriquecer um arquivo skill consolidado, minimalista e sem repetição.
> **Golden Rule**: processe um capítulo por vez e pare. O usuário limpa o contexto antes do próximo.

---

## Índice

| # | Seção |
|---|---|
| 1 | [Como Invocar](#como-invocar) |
| 2 | [Ponteiro de Progresso](#ponteiro-de-progresso) |
| 3 | [Protocolo de Leitura](#protocolo-de-leitura) |
| 4 | [Modo Agregador](#modo-agregador) |
| 5 | [Regras de Extração](#regras-de-extração) |
| 6 | [Formato do Arquivo Skill Gerado](#formato-do-arquivo-skill-gerado) |
| 7 | [Golden Rules](#golden-rules) |
| 8 | [Checklist por Capítulo](#checklist-por-capítulo) |

---

## Como Invocar

### Modo Normal — gerar ou expandir um skill

O agente lê um capítulo da fonte e acrescenta ao skill destino (cria se não existir).

**PDF**:
```
PDF: <caminho.pdf>
Capítulo: <número>
Skill destino: <caminho-skill.md>
```

**EPUB**:
```
EPUB: <caminho.epub>
Capítulo: <número>
Skill destino: <caminho-skill.md>
```
Requer: `pip install ebooklib beautifulsoup4` e `epub_chapter_extractor.py` na pasta do projeto.

**TXT**:
```
TXT: <caminho.txt>
Linhas: <início>-<fim>     (opcional — omitir lê o arquivo inteiro)
Skill destino: <caminho-skill.md>
```
`Linhas` define o trecho a tratar como "capítulo". Para arquivos pequenos (≤ 500 linhas), omitir e ler tudo.

---

### Modo Agregador — integrar nova fonte a skill existente

O agente lê o capítulo, compara com o conteúdo já presente na skill e classifica cada conceito como **redundante**, **inédito** ou **complementar inédito**. A presença de `Skill existente:` (em vez de `Skill destino:`) ativa este modo.

```
Fonte: <caminho.pdf|epub|txt>
Capítulo: <número>           (para TXT: pode ser "Linhas: start-end")
Skill existente: <caminho-skill.md>
```

Exemplos:
```
Fonte: D:\Livros\clean_arch.epub
Capítulo: 4
Skill existente: D:\Skillstore\clean_architecture_skill.md
```

```
Fonte: D:\Notas\anotacoes_curso.txt
Linhas: 1-300
Skill existente: D:\Skillstore\python_skill.md
```

---

## Ponteiro de Progresso

Ao gravar o skill pela primeira vez, insira o bloco abaixo na **primeira linha** do arquivo, antes do título:

```
<!-- AGENTE-PROGRESSO
fonte: <caminho absoluto da fonte>
próximo: <posição exata: "página 45" | "capítulo 12 (entry 324)" | "linha 480">
último-heading: <último ## ou ### presente no skill, ex: "## 3 GDScript">
última-linha: <texto literal da última linha não-vazia do skill>
-->
```

**Campos do ponteiro**:
- `fonte` — caminho da fonte processada (para conferência).
- `próximo` — posição exata de onde retomar sem varrer o documento: página (PDF), entry/capítulo (EPUB) ou linha (TXT).
- `último-heading` — heading `##` ou `###` da última seção gravada no skill.
- `última-linha` — texto literal da última linha não-vazia do skill. Permite fazer append via `Edit(old_string=última-linha, ...)` sem ler o arquivo inteiro.

**Ciclo de vida do ponteiro**:
1. **Criado** na primeira invocação, inserido antes do título: `Edit(old_string="# Skill:", new_string="<!-- AGENTE-PROGRESSO\n...\n-->\n\n# Skill:")`.
2. **Atualizado** ao final de cada Passo 5 com a nova posição e nova última linha.
3. **Removido** quando toda a fonte foi processada: `Edit` apaga o bloco `<!-- AGENTE-PROGRESSO\n...\n-->` antes do relatório final.

---

## Protocolo de Leitura

Os passos 3 em diante são idênticos para todos os formatos e modos. Os passos 1 e 2 variam pela ferramenta de leitura.

### Tabela de ferramentas por formato

| Etapa | PDF | EPUB | TXT |
|---|---|---|---|
| Reconhecimento inicial | `Read` páginas 1–5 | Bash: `epub_chapter_extractor.py --list` | `Read` primeiras 50 linhas |
| Ler capítulo | `Read` com `pages` | Bash: `--chapter N -o _cap_tmp.txt` + `Read _cap_tmp.txt` | `Read` com `offset`/`limit` |
| Limpar | — | Bash: `del _cap_tmp.txt` | — |

---

### Passo 0 — Leitura do Índice da Fonte

Execute **sempre**, em toda invocação (primeiro ou N-ésimo capítulo).

**Objetivo**: ter o mapa completo da fonte para inferir, durante os Passos 3–4, se um conceito do capítulo atual pertence retroativamente a uma seção anterior já gravada no skill, ou se é inédito absoluto.

| Formato | Ação |
|---|---|
| PDF | `Read` com `pages: "1-5"` (índice geralmente nas primeiras páginas) |
| EPUB | Bash: `python epub_chapter_extractor.py livro.epub --list` |
| TXT | `Read` com `limit: 50` |

Ao classificar conceitos nos Passos 3–4, use este mapa para decidir:
- Tema coberto em capítulo **anterior** ao atual → o conceito pode caber retroativamente em seção existente do skill.
- Tema ausente de todos os capítulos anteriores → candidato a inédito absoluto.

---

### Passo 0.5 — Verificação do Ponteiro de Progresso

Execute se o skill destino já existe.

1. `Read` o skill com `limit: 10` para verificar se há um bloco `<!-- AGENTE-PROGRESSO ... -->`.
2. Se o bloco existir:
   - Extraia `próximo` — use no Passo 2 para saber de onde retomar a leitura na fonte (pule o Passo 1 de reconhecimento inicial).
   - Extraia `última-linha` — use no Passo 5 para fazer append eficiente sem ler o arquivo inteiro.
3. Se não existir (skill sem ponteiro): siga o fluxo normal; crie o ponteiro ao final do Passo 5.

---

### Passo 1 — Reconhecimento inicial (somente no primeiro capítulo/trecho)

Identifique e registre no cabeçalho do skill destino:

- Título do livro/documento e autor (se houver)
- Estrutura de capítulos ou seções
- Linguagem/tecnologia alvo (se técnico)
- Público-alvo declarado pelo autor

Cabeçalho no skill:

```markdown
# Skill: <Título> — Referência Consolidada

> **Fonte**: <Título>, <Autor>, <Edição/Ano>
> **Alvo**: <linguagem, framework ou domínio>
> **Última extração**: <data YYYY-MM>

---
```

**PDF**: `Read` com `pages: "1-5"`.

**EPUB**: Bash `python epub_chapter_extractor.py livro.epub --list`.

**TXT**: `Read` com `limit: 50` para ler as primeiras linhas e entender a estrutura.

---

### Passo 2 — Leitura do capítulo ou trecho indicado

**PDF**:
1. `Read` o capítulo com `pages: "X-Y"`. Para capítulos longos, leia em blocos de até 20 páginas.

**EPUB**:
1. Bash: `python epub_chapter_extractor.py livro.epub --chapter N --output _cap_tmp.txt`
2. `Read _cap_tmp.txt`
3. Bash: `del _cap_tmp.txt`

**TXT**:
1. `Read` o arquivo completo, ou `Read` com `offset` e `limit` se `Linhas: start-end` foi informado.
   - `offset` = `início - 1`, `limit` = `fim - início + 1`.
2. Para arquivos grandes sem linha especificada: leia as primeiras 500 linhas e informe o usuário que o restante será processado na próxima invocação.

---

### Passo 3 — Extração

Extraia apenas:

- Procedimentos concretos ("como fazer X")
- Regras e boas práticas explícitas no texto
- Padrões nomeados pelo autor (design patterns, antipatterns com nome)
- Avisos e antipadrões descritos explicitamente
- Exemplos de código canônicos (não os ilustrativos intermediários)

Ignore:
- Anedotas, histórias, introduções contextuais
- Repetições de conceitos já no skill destino
- Opiniões sem embasamento técnico prático

---

### Passo 4 — Classificação por seção existente

Para cada conceito extraído:

1. Procure na skill destino por termos-chave do conceito.
2. Se uma seção existente cobre o tema → **agregue** o conteúdo inédito nessa seção (append após o último parágrafo).
3. Se nenhuma seção existente cobre o tema → marque como **inédito absoluto**.

**Regra**: só crie nova seção para inéditos absolutos. Conteúdo que cabe em seção existente é sempre agregado a ela, nunca duplicado em nova seção.

---

### Passo 5 — Escrita no skill e atualização do índice

1. **Conteúdo agregado**: se o ponteiro contém `última-linha`, use `Edit(old_string=última-linha, new_string=última-linha + "\n\n" + novo-conteúdo)` para append sem ler o arquivo inteiro. Caso contrário, leia a seção alvo e appende após o último parágrafo.
2. **Inédito absoluto**: crie `## Nova Seção — <Título>` continuando a numeração existente do skill (último número + 1). **Nunca** use numeração de capítulo (N.1, N.2) como estrutura de heading da skill.
3. Releia o arquivo completo e reconstrua o `## Índice` do zero (todos os `##` e `###` presentes).
4. **Atualizar o ponteiro**: edite o bloco `<!-- AGENTE-PROGRESSO ... -->` no topo do skill com os novos valores:
   - `próximo`: próxima posição a processar na fonte (página, entry ou linha seguinte ao trecho atual).
   - `último-heading`: heading `##` ou `###` mais recente do skill após a gravação.
   - `última-linha`: última linha não-vazia do skill após a gravação.

   Se o skill foi criado nesta invocação (não existia), insira o bloco antes do título usando `Edit(old_string="# Skill:", new_string="<!-- AGENTE-PROGRESSO\nfonte: ...\npróximo: ...\núltimo-heading: ...\núltima-linha: ...\n-->\n\n# Skill:")`.

Âncoras Markdown: minúsculas, espaços → `-`, remover caracteres especiais (exceto `-`), `—` → `--`.

---

### Passo 6 — Parar e reportar (Modo Normal)

```
✓ Capítulo <N> extraído → <N_conceitos> conceitos, <N_exemplos> exemplos de código.
Arquivo: <caminho>

⏸ PARADO — limpe o contexto e invoque novamente para o Capítulo <N+1>.
Próximo: "<título do próximo capítulo>".
```

> **Nota sobre o índice**: sempre reescreva o bloco `## Índice` por completo. Nunca faça append de linhas individuais.

Se esta foi a **última seção** da fonte (não há mais conteúdo procedimental a extrair): remova o bloco `<!-- AGENTE-PROGRESSO ... -->` do skill com `Edit` antes de exibir o relatório final.

---

## Modo Agregador

O modo agregador integra conhecimento novo de uma fonte a uma skill já existente, sem criar duplicatas nem perder nuance.

### Classificação de conceitos

Para cada conceito extraído do capítulo, aplique:

| Classificação | Critério | Ação |
|---|---|---|
| **Redundante** | O conceito já está na skill com grau de detalhe equivalente | Descartar; registrar no relatório |
| **Inédito** | O conceito não existe em nenhuma seção da skill | Adicionar como nova entrada na seção do capítulo |
| **Complementar inédito** | O conceito existe na skill mas a nova fonte acrescenta perspectiva ou detalhe ausente | Acrescentar na seção existente com marcador `> (Fonte acrescenta: ...)` |

### Como determinar a classificação

1. Para cada conceito extraído, pesquise na skill por termos-chave.
2. Se não houver match → **Inédito**.
3. Se houver match:
   - Verifique se o novo texto acrescenta detalhe, exemplo, restrição ou perspectiva ausente.
   - Se não acrescenta nada → **Redundante**.
   - Se acrescenta algo concreto → **Complementar inédito**.

### Protocolo do modo agregador

**Passo A** — Leia o capítulo da fonte (igual Passos 1 e 2 do protocolo normal).

**Passo B** — Leia **todo o conteúdo** da skill existente.

**Passo C** — Extraia conceitos do capítulo (igual Passo 3 do protocolo normal).

**Passo D** — Classifique e aja:

- **Redundantes**: apenas registre no relatório; não modifique a skill.

- **Complementares inéditos**: localize a seção existente correspondente na skill e appende imediatamente após o último parágrafo dessa seção:
  ```
  > (Fonte "<nome-do-arquivo>" acrescenta: <detalhe novo, 1–2 frases>)
  ```

- **Inéditos absolutos** (sem seção existente que cubra o tema): crie `## Nova Seção — <Título>` continuando a numeração do índice da skill (último número + 1). **Nunca** use numeração de capítulo (N.1, N.2) como heading da skill.

**Passo E** — Reconstrua o `## Índice` por completo.

**Passo F** — Exiba o relatório de parada do modo agregador:

```
✓ Capítulo <N> analisado — <nome-do-arquivo-fonte>
  Redundantes descartados : X
  Inéditos adicionados    : Y  (→ seção "...")
  Complementares integrados: Z  (→ seções: "...", "...")

Arquivo: <caminho da skill>

⏸ PARADO — limpe o contexto e invoque novamente para o Capítulo <N+1>.
```

### Regras específicas do modo agregador

- Nunca remova ou reescreva conteúdo já existente na skill.
- Um conceito só é **redundante** se o detalhe presente na skill for **equivalente ou superior** ao da nova fonte. Em caso de dúvida, classifique como complementar.
- O marcador `> (Fonte acrescenta: ...)` é sempre append — nunca substitui o texto original.
- Se a nova fonte contradizer o conteúdo existente na skill, classifique como **complementar inédito** e indique a divergência: `> (Fonte "<nome>" diverge: <descrição da divergência>)`.

---

## Regras de Extração

### O que incluir

| Tipo | Critério de inclusão |
|---|---|
| Procedimento | Autor descreve etapas concretas e replicáveis |
| Boa prática | Autor usa linguagem prescritiva: "deve", "sempre", "nunca", "prefira" |
| Padrão nomeado | Autor dá um nome ao padrão (ex.: "Strategy Pattern", "Guard Clause") |
| Antipadrão | Autor descreve explicitamente o que evitar e por quê |
| Exemplo de código | Autor apresenta como forma canônica ou "correta" |

### O que excluir

- Conteúdo já presente no skill destino (mesmo que com palavras diferentes)
- Definições triviais que qualquer praticante conhece
- Exemplos usados apenas para ilustrar um erro, sem mostrar a correção
- Conteúdo fora do escopo técnico (prefácio, agradecimentos, notas bibliográficas)

---

## Formato do Arquivo Skill Gerado

### Conteúdo agregado a seção existente

Appende diretamente após o último parágrafo da seção relevante:

```markdown
<Descrição direta, 1–3 frases. Fonte: o que o autor afirma, não inferência.>

```<linguagem>
# exemplo canônico do autor
```

**Regra**: <enunciado prescritivo direto>

> ⚠ Evite: <antipadrão>

> (Fonte "<nome>" acrescenta: <detalhe novo>)    ← apenas no modo agregador
```

### Nova seção (inédito absoluto)

Cria `## <Título>` continuando a numeração do índice:

```markdown
## <Título da Nova Seção>

<Descrição direta, 1–3 frases.>

```<linguagem>
# exemplo canônico do autor
```

**Regra**: <enunciado prescritivo direto>

> ⚠ Evite: <antipadrão>
```

**Regras de formatação**:
- `**Regra**:` para boas práticas prescritivas
- `> ⚠ Evite:` para antipadrões
- `> 💡 Nota:` para observações de contexto (uso com moderação)
- `> (Fonte "..." acrescenta: ...)` para complementos do modo agregador
- `> (Fonte "..." diverge: ...)` para contradições do modo agregador
- Sem emojis decorativos fora desses marcadores
- Máximo 3 níveis de heading (`##`, `###`, `####`)
- Blocos de código sempre com linguagem declarada

---

## Golden Rules

1. **Um capítulo por vez.** Nunca avance automaticamente para o próximo.
2. **Fonte única.** Extraia apenas o que está no documento. Não complemente com conhecimento externo.
3. **Sem repetição.** Deduplique antes de escrever; no modo agregador, classifique antes de agir.
4. **Minimalismo.** Se um conceito cabe em uma frase, não use um parágrafo.
5. **Parar é obrigatório.** Após gravar, exiba o relatório e aguarde. Nunca continue em silêncio.
6. **Preservar o skill.** Use append; nunca sobrescreva seções existentes sem verificar conflito.
7. **EPUB: limpar temporários.** Sempre apague `_cap_tmp.txt` após ler o conteúdo.
8. **Agregador: não destruir.** O modo agregador só acrescenta. Nunca remove nem reescreve conteúdo existente.
9. **Agregador: dúvida → complementar.** Se a classificação for ambígua entre redundante e complementar, prefira complementar.
10. **Agregação tem prioridade.** Sempre verifique se o conteúdo cabe em seção existente antes de criar uma nova. Nova seção só para inédito absoluto.
11. **Sem renumeração de capítulo.** Nunca use `N.1`, `N.2` como numeração de headings da skill. Se uma nova seção for necessária, continue a numeração própria da skill (último número + 1).
12. **Ponteiro é obrigatório.** Crie no primeiro `Write`, atualize em cada Passo 5, remova ao concluir a fonte. Nunca deixe o skill sem ponteiro durante o processamento, nem com ponteiro após terminar.

---

## Checklist por Capítulo

### Modo Normal

- [ ] Passo 0: índice da fonte lido (TOC) — mapa de capítulos em contexto
- [ ] Passo 0.5: ponteiro lido (se skill existe) — `próximo` e `última-linha` extraídos
- [ ] Capítulo/trecho lido na íntegra a partir da posição `próximo`
  - PDF: todas as páginas do intervalo com `Read`
  - EPUB: `_cap_tmp.txt` gerado, lido e apagado
  - TXT: arquivo lido com `Read` (com `offset`/`limit` se `Linhas:` foi informado)
- [ ] Somente procedimentos e boas práticas extraídos (sem narrativa)
- [ ] Índice da fonte consultado para decidir inserção retroativa vs. inédito absoluto
- [ ] Cada conceito verificado contra seções existentes da skill antes de escrever
- [ ] Conteúdo agregável inserido na seção existente correspondente (append via `última-linha`)
- [ ] Nova seção criada apenas para inédito absoluto, continuando numeração da skill
- [ ] Exemplos de código são os canônicos, não os intermediários
- [ ] Antipadrões marcados com `> ⚠ Evite:`
- [ ] Nenhum heading com prefixo de capítulo (N.1, N.2) foi criado na skill
- [ ] `## Índice` reconstruído por completo
- [ ] Ponteiro atualizado com nova posição (`próximo`), `último-heading` e `última-linha`
- [ ] (Se conclusão) Ponteiro removido do skill antes do relatório final
- [ ] Relatório exibido com próximo capítulo indicado

### Modo Agregador (itens adicionais)

- [ ] Skill existente lida na íntegra antes de classificar
- [ ] Cada conceito classificado (redundante / inédito / complementar inédito)
- [ ] Inéditos adicionados na seção correta (nova ou existente do capítulo)
- [ ] Complementares integrados com marcador `> (Fonte "..." acrescenta: ...)`
- [ ] Divergências marcadas com `> (Fonte "..." diverge: ...)`
- [ ] Nenhum conteúdo existente removido ou reescrito
- [ ] Relatório do modo agregador exibido com contagens por categoria

---

## Erros Comuns

| Erro | Correção |
|---|---|
| Avançar capítulo sem parar | Proibido. Pare sempre após gravar um capítulo |
| Incluir opiniões informais como regras | Só inclua se o autor usa linguagem prescritiva explícita |
| Duplicar conceito com outra redação | Deduplique; amplie entrada existente se houver detalhe novo |
| Criar `## Capítulo N` para conteúdo já coberto | Verifique seções existentes; agregue, não duplique |
| Usar numeração N.1/N.2 como heading da skill | Proibido. Nova seção segue a numeração da skill, não do capítulo |
| Gerar skill vazio por não encontrar "regras" | Todo capítulo técnico tem procedimentos; releia com foco em verbos de ação |
| Completar com conhecimento externo | Proibido. Skill deve refletir a fonte, não o conhecimento do agente |
| Sobrescrever skill inteiro | Use append por seção; nunca destrua conteúdo anterior |
| (EPUB) Não apagar `_cap_tmp.txt` | Sempre execute `del _cap_tmp.txt` após ler o temporário |
| (Agregador) Classificar como redundante com dúvida | Em caso de dúvida, classifique como complementar inédito |
| (Agregador) Reescrever seção existente em vez de appendar | O marcador `> (Fonte acrescenta: ...)` é sempre append |
| (TXT grande, sem Linhas:) Tentar ler tudo de uma vez | Leia as primeiras 500 linhas e informe o usuário para definir `Linhas:` na próxima invocação |
| Pular leitura do índice da fonte | Execute sempre o Passo 0 (leitura do TOC) em toda invocação, não só na primeira |
| Não criar o ponteiro no primeiro Write | Insira `<!-- AGENTE-PROGRESSO ... -->` antes do título ao criar o skill |
| Não atualizar o ponteiro após gravar | Atualize `próximo`, `último-heading` e `última-linha` ao final de todo Passo 5 |
| Deixar o ponteiro no skill ao concluir | Remova o bloco `<!-- AGENTE-PROGRESSO ... -->` antes do relatório quando a fonte estiver esgotada |
| Ler o arquivo inteiro só para encontrar a última linha | Use `última-linha` do ponteiro; append com `Edit(old_string=última-linha, ...)` |
