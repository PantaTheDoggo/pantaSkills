# Skill: PDF-to-Skill Agent — Extração de Conhecimento de Livros

> **Propósito**: Ler um livro em PDF capítulo a capítulo e gerar um arquivo skill consolidado, minimalista e sem repetição, lendo exclusivamente o que está no PDF.
> **Golden Rule**: processe um capítulo por vez e pare. O usuário limpa o contexto antes do próximo.

---

## Índice

| # | Seção |
|---|---|
| 1 | [Como Invocar](#como-invocar) |
| 2 | [Protocolo de Leitura](#protocolo-de-leitura) |
| 3 | [Regras de Extração](#regras-de-extração) |
| 4 | [Formato do Arquivo Skill Gerado](#formato-do-arquivo-skill-gerado) |
| 5 | [Golden Rules](#golden-rules) |
| 6 | [Checklist por Capítulo](#checklist-por-capítulo) |

---

## Como Invocar

O usuário informa:

```
PDF: <caminho-do-arquivo.pdf>
Capítulo: <número ou título>
Skill destino: <nome-do-arquivo-skill.md>   (omitido = criar novo baseado no título do livro)
```

Exemplo de invocação:

```
PDF: D:\Livros\clean_code.pdf
Capítulo: 3
Skill destino: D:\Skillstore\clean_code_skill.md
```

Se `Skill destino` já existir, o agente **acrescenta** a seção nova sem duplicar conteúdo já presente.

---

## Protocolo de Leitura

### Passo 1 — Reconhecimento inicial (somente no capítulo 1)

Antes de extrair conteúdo, leia as **primeiras páginas** do PDF para identificar:

- Título do livro e autor
- Estrutura de capítulos (sumário/índice)
- Linguagem/tecnologia alvo (se técnico)
- Público-alvo declarado pelo autor

Registre no cabeçalho do arquivo skill destino:

```markdown
# Skill: <Título do Livro> — Referência Consolidada

> **Fonte**: <Título>, <Autor>, <Edição/Ano>
> **Alvo**: <linguagem, framework ou domínio>
> **Última extração**: <data YYYY-MM>

---
```

### Passo 2 — Leitura do capítulo indicado

1. Leia o capítulo completo usando a tool `Read` com `pages` correspondentes.
2. Se o PDF for grande, leia em blocos de até 20 páginas, progredindo sequencialmente dentro do capítulo.
3. Não avance para o próximo capítulo — pare ao final do atual.

### Passo 3 — Extração

Após ler, extraia apenas:

- Procedimentos concretos ("como fazer X")
- Regras e boas práticas explícitas no texto
- Padrões de código ou design patterns nomeados pelo autor
- Avisos e antipadrões descritos explicitamente
- Exemplos de código relevantes (apenas os canônicos, não os ilustrativos intermediários)

Ignore:
- Anedotas, histórias e introduções contextuais
- Repetições de conceitos já no skill destino
- Opiniões sem embasamento técnico prático

### Passo 4 — Escrita no skill destino

Adicione uma seção `## Capítulo N — <Título do Capítulo>` ao arquivo skill destino com o conteúdo extraído.

### Passo 5 — Parar e reportar

Após gravar, exiba:

```
✓ Capítulo <N> extraído → <N_conceitos> conceitos, <N_exemplos> exemplos de código.
Arquivo: <caminho do skill destino>

⏸ PARADO — limpe o contexto e invoque novamente para o Capítulo <N+1>.
Próximo: "<título do próximo capítulo>" (páginas <X>–<Y>).
```

Não continue automaticamente. Aguarde nova invocação do usuário.

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
- Conteúdo fora do escopo técnico do capítulo (prefácio, agradecimentos, notas bibliográficas)

### Deduplicação

Antes de adicionar qualquer conceito:

1. Pesquise no arquivo skill destino existente por termos-chave do conceito.
2. Se o conceito já existir, verifique se o novo capítulo acrescenta detalhe novo.
3. Se sim, **amplie a entrada existente** com uma nota `> (Cap. N acrescenta: ...)`.
4. Se não, descarte.

---

## Formato do Arquivo Skill Gerado

Cada seção de capítulo segue esta estrutura mínima:

```markdown
## Capítulo N — <Título>

### <Tema Principal 1>

<Descrição direta, 1–3 frases. Fonte: o que o autor afirma, não inferência.>

```<linguagem>
# exemplo canônico do autor, se houver
```

**Regra**: <enunciado prescritivo direto>

> ⚠ Evite: <antipadrão, se mencionado>

---

### <Tema Principal 2>
...
```

**Regras de formatação**:
- Use `**Regra**:` para boas práticas prescritivas
- Use `> ⚠ Evite:` para antipadrões
- Use `> 💡 Nota:` para observações de contexto (uso com moderação)
- Sem emojis decorativos fora desses marcadores
- Máximo 3 níveis de heading (`##`, `###`, `####`)
- Listas não numeradas para conjuntos sem ordem; numeradas para sequências de passos
- Blocos de código sempre com linguagem declarada (` ```python `, ` ```bash `, etc.)

---

## Golden Rules

1. **Um capítulo por vez.** Nunca avance automaticamente para o próximo.
2. **Fonte única.** Extraia apenas o que está no PDF. Não complemente com conhecimento externo.
3. **Sem repetição.** Deduplique antes de escrever.
4. **Minimalismo.** Se um conceito cabe em uma frase, não use um parágrafo.
5. **Parar é obrigatório.** Após gravar o capítulo, exiba o relatório e aguarde nova invocação. Nunca continue em silêncio.
6. **Preservar o skill destino.** Use append, nunca sobrescreva seções existentes sem verificar conflito.

---

## Checklist por Capítulo

Antes de escrever no skill destino, confirme cada item:

- [ ] Capítulo lido na íntegra (todas as páginas do intervalo)
- [ ] Somente procedimentos e boas práticas extraídos (sem narrativa)
- [ ] Deduplicação feita contra o arquivo skill destino
- [ ] Exemplos de código são os canônicos do autor, não os intermediários
- [ ] Antipadrões identificados e marcados com `> ⚠ Evite:`
- [ ] Seção `## Capítulo N — <Título>` adicionada ao skill destino
- [ ] Relatório de parada exibido ao usuário com próximo capítulo indicado

---

## Erros Comuns

| Erro | Correção |
|---|---|
| Avançar capítulo sem parar | Proibido. Pare sempre após gravar um capítulo |
| Incluir opiniões informais do autor como regras | Só inclua se o autor usa linguagem prescritiva explícita |
| Duplicar conceito com outra redação | Deduplique; amplie entrada existente se houver detalhe novo |
| Gerar skill vazio por não encontrar "regras" | Todo capítulo técnico tem procedimentos; releia com foco em verbos de ação |
| Completar com conhecimento externo | Proibido. Skill deve refletir o livro, não o conhecimento geral do agente |
| Sobrescrever skill destino inteiro | Use append por seção; nunca destrua conteúdo anterior |
