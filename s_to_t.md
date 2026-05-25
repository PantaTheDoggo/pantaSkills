# Skill: s_to_t — Skill to Teach

> **Propósito**: Ler um arquivo skill seção por seção e gerar um arquivo "teach" — versão didática em prosa curta, projetada para ser convertida em áudio e consumida como audiobook.
> **Golden Rule**: processe uma seção por vez e pare. O usuário limpa o contexto antes da próxima.

---

## Índice

| # | Seção |
|---|---|
| 1 | [Como Invocar](#como-invocar) |
| 2 | [Ponteiro de Progresso](#ponteiro-de-progresso) |
| 3 | [Protocolo de Conversão](#protocolo-de-conversão) |
| 4 | [Regras de Conversão](#regras-de-conversão) |
| 5 | [Tratamento de Código e Equações](#tratamento-de-código-e-equações) |
| 6 | [Linguagem para Áudio](#linguagem-para-áudio) |
| 7 | [Estrutura do Arquivo Teach](#estrutura-do-arquivo-teach) |
| 8 | [Golden Rules](#golden-rules) |
| 9 | [Checklist por Seção](#checklist-por-seção) |
| 10 | [Erros Comuns](#erros-comuns) |

---

## Como Invocar

```
Skill: <caminho-skill.md>
Seção: <número da seção de topo, ex: "3" ou "5">
Teach destino: <caminho-teach.md>
```

A seção informada é sempre uma **seção de topo** do skill (`## 1`, `## 2`, ..., `## N`). Subseções (`### 5.1`, `### 5.2`) são processadas juntas com a seção pai.

Exemplo:
```
Skill: D:\Skillstore\software_mistakes_tradeoffs_skill.md
Seção: 4
Teach destino: D:\Skillstore\software_mistakes_tradeoffs_teach.md
```

Para retomar de onde parou, o agente lê o ponteiro de progresso do teach destino e ignora o campo `Seção:` (usa o `próximo` do ponteiro).

---

## Ponteiro de Progresso

Ao gravar o teach pela primeira vez, insira o bloco abaixo na **primeira linha** do arquivo, antes do título:

```
<!-- AGENTE-PROGRESSO
skill: <caminho absoluto da skill original>
próximo: <número da próxima seção de topo a processar, ex: "5">
última-seção: <última seção gravada no teach, ex: "4. Microservices vs Monolito">
última-linha: <texto literal da última linha não-vazia do teach>
-->
```

**Ciclo de vida**:
1. **Criado** no primeiro `Write`, antes do título.
2. **Atualizado** ao final de cada Passo 5 com a nova seção processada.
3. **Removido** quando a última seção da skill foi convertida.

---

## Protocolo de Conversão

### Passo 0 — Leitura do índice da skill

Leia o bloco `## Índice` da skill com `Read limit: 100` (ou o suficiente para capturar todo o índice).

Identifique:
- A seção alvo (informada pelo usuário ou pelo `próximo` do ponteiro).
- O número da próxima seção de topo (para atualizar o ponteiro).
- O total de seções de topo na skill (para saber quando concluir).

> ⚠ Se a skill contiver um bloco `<!-- AGENTE-PROGRESSO ... -->` (colocado pelo agente k_to_s), **ignore-o completamente**. Ele não é gerenciado pelo s_to_t e não deve ser lido, editado nem removido.

---

### Passo 0.5 — Verificação do ponteiro no arquivo teach

> ⚠ O ponteiro do s_to_t existe **exclusivamente no arquivo teach**. Nunca procure, leia nem edite ponteiros no arquivo skill.

Se o teach destino já existir:
1. `Read` o teach com `limit: 10` para extrair o bloco `<!-- AGENTE-PROGRESSO ... -->`.
2. Use `próximo` em vez do parâmetro `Seção:` informado, caso ambos estejam presentes.
3. Use `última-linha` para fazer append eficiente no Passo 5.

Se o teach não existir: o Passo 1 cria o cabeçalho.

---

### Passo 1 — Cabeçalho do teach (somente na primeira invocação)

Crie o teach com o cabeçalho:

```markdown
# Teach: <Título da Skill, sem o prefixo "Skill:">

Bem-vindo. Este é um material em áudio derivado da skill <nome curto>. Cada faixa cobre um conceito independente. Você pode ouvir em qualquer ordem.

---
```

---

### Passo 2 — Leitura da seção da skill

1. Localize na skill a linha `## <número>. <título>` da seção alvo.
2. Leia desde essa linha até a linha imediatamente anterior à próxima `## <número+1>`.
3. Use `Grep` com `output_mode: content` e `-n` para descobrir as linhas exatas, depois `Read` com `offset` e `limit`.

Inclua todas as subseções (`### N.1`, `### N.2`, ...) da seção.

---

### Passo 3 — Conversão didática

Para cada conceito, regra, padrão ou exemplo encontrado na seção:

1. **Identifique o conceito central** — uma ideia em uma frase.
2. **Identifique o porquê** — qual problema o conceito resolve.
3. **Reescreva em prosa curta**, seguindo as [regras de conversão](#regras-de-conversão).
4. **Substitua código e equações** por narrativa direta — veja [seção 5](#tratamento-de-código-e-equações).
5. **Encadeie parágrafos** com transições explícitas.

Subseções (`### N.1`, `### N.2`) viram parágrafos consecutivos com transição entre eles, **não** novos headings.

---

### Passo 4 — Escrita no teach

A seção convertida vira um capítulo do audiobook, com a estrutura definida em [Estrutura do Arquivo Teach](#estrutura-do-arquivo-teach).

Se o ponteiro contém `última-linha`, use `Edit(old_string=última-linha, new_string=última-linha + "\n\n---\n\n" + novo-capítulo)` para append sem reler o arquivo inteiro. Caso contrário, leia o arquivo e appende ao final.

---

### Passo 5 — Atualização do ponteiro

Edite o bloco `<!-- AGENTE-PROGRESSO ... -->` com:
- `próximo`: número da próxima seção de topo da skill.
- `última-seção`: número e título da seção que acabou de ser gravada.
- `última-linha`: última linha não-vazia do teach após a gravação.

Se esta foi a **última seção** da skill, **remova** o bloco do ponteiro antes do relatório final.

---

### Passo 6 — Parar e reportar

```
✓ Seção <N> convertida → <N_parágrafos> parágrafos, <N_blocos_codigo> blocos de código transformados em prosa.
Arquivo: <caminho do teach>

⏸ PARADO — limpe o contexto e invoque novamente para a Seção <N+1>.
Próximo: "<título da próxima seção>".
```

---

## Regras de Conversão

### O que manter

- Conceito central da seção.
- Definição essencial de cada termo.
- Relação causa-efeito (por que X leva a Y).
- Regras prescritivas (sempre, nunca, prefira).
- Padrões nomeados e a intuição por trás deles.
- Antipadrões com nome.

### O que resumir

- Listas longas de exemplos → cite um ou dois e diga "entre outros".
- Comparações tabulares → escolha as duas ou três dimensões mais importantes e narre em prosa.
- Múltiplas alternativas → enuncie a recomendação e mencione brevemente a alternativa principal.

### O que omitir

- Exceções marginais que não afetam o conceito central.
- Cenários hipotéticos que dependem de visualização.
- Notas de rodapé, referências bibliográficas, links.
- URLs, caminhos de arquivo, nomes de pacotes (salvo quando essenciais).
- Detalhes de sintaxe específica de linguagem que não generalizam.

**Regra**: priorize **conceito** sobre **exceção**. Se a exceção for crítica para entender o conceito, mantenha-a. Caso contrário, omita.

---

## Tratamento de Código e Equações

Blocos de código e equações **nunca aparecem literalmente** no teach. Sempre convertidos em prosa.

### Como converter um bloco de código

1. Pergunte: **o que** este código faz?
2. Pergunte: **qual conceito** ele demonstra?
3. Pergunte: **qual variação ou regra** ele exemplifica?
4. Escreva 1 a 3 frases respondendo essas perguntas.

**Exemplo — recursão**:

Skill original:
```python
def fatorial(n):
    if n == 0:
        return 1
    return n * fatorial(n - 1)
```

Teach:
> Considere a operação de fatorial. Quando o número é zero, o resultado é um. Em qualquer outro caso, multiplicamos o número pelo fatorial do número anterior. A função chama a si mesma com um problema menor a cada passo. Esse é o padrão essencial da recursão.

### Como converter uma equação

1. Identifique o que cada símbolo representa.
2. Enuncie a relação em palavras.
3. Mencione o significado prático, não a forma matemática.

**Exemplo — Lei de Amdahl**:

Skill: `Speedup = 1 / ((1 - P) + P/N)`

Teach:
> A Lei de Amdahl diz que o ganho de paralelizar é limitado pela parte sequencial do programa. Se metade do tempo é paralelizável, mesmo com infinitos processadores o ganho máximo é apenas o dobro. Quanto menor a fração paralelizável, menor o teto do speedup.

### Como converter um comando de shell ou configuração

- Não recite o comando.
- Descreva o **efeito** e a **decisão** que motivou o comando.

**Exemplo**: `git rebase -i HEAD~3` → "É possível reorganizar os últimos três commits de forma interativa, escolhendo combinar, reordenar ou editar cada um."

---

## Linguagem para Áudio

Estas regras moldam **cada frase** do teach.

### Comprimento

- Alvo: 12 a 18 palavras por frase.
- Limite duro: 25 palavras. Acima disso, divida.
- Uma ideia por frase.

### Pontuação

- Vírgula e ponto são pistas de pausa para o sintetizador de voz. Use-as como tal.
- Ponto e vírgula: evite. Substitua por dois períodos.
- Travessões e parênteses: evite. Reorganize a frase.
- Reticências: evite. Soam como hesitação no áudio.

### Vocabulário

- Pronuncie acrônimos por extenso na primeira menção da seção. Exemplo: "API, ou interface de programação".
- Evite siglas obscuras. Se inevitável, soletre.
- Termos técnicos em inglês são aceitos, mas sem aspas nem marcação especial.
- Números importantes para a ideia: por extenso. "Vinte por cento" em vez de "20 por cento".
- Números pouco importantes ou exatos: dígitos. "RFC 7232".

### Conexão

- Conecte parágrafos com transições explícitas: "Em seguida...", "Por outro lado...", "Veja agora um exemplo prático...", "Vamos ao próximo conceito...".
- Reformule perguntas retóricas como afirmações. O áudio não tolera o silêncio reflexivo da leitura.

### Marcação proibida no corpo do teach

- Sem negrito, itálico ou monospace.
- Sem listas com bullets ou numeradas.
- Sem tabelas.
- Sem blocos de código.
- Sem links markdown.
- Sem emojis.
- Sem headings além do `#` de nível 1 que separa capítulos.

Ênfase, quando necessária, é feita pela **escolha das palavras** e pela construção da frase. "Este é o ponto central" funciona; `**Este é o ponto central**` não.

---

## Estrutura do Arquivo Teach

### Estrutura por seção convertida

Cada seção da skill vira um capítulo do teach com cinco partes:

1. **Título** — `# <Número>. <Título narrativo>` (heading nível 1).
2. **Abertura** — uma a três frases enunciando o que o ouvinte vai aprender nesta faixa.
3. **Desenvolvimento** — três a oito parágrafos curtos, cada um com duas a cinco frases. Cada parágrafo cobre uma subideia. Transições explícitas entre parágrafos.
4. **Regras e armadilhas** — um ou dois parágrafos com as regras prescritivas e os erros comuns, narrados como tal. Exemplos: "A regra é a seguinte..." ou "Um equívoco frequente é...".
5. **Fechamento** — uma ou duas frases recapitulando o conceito central da faixa.

### Separadores

Entre capítulos, use `---` em linha própria. Isso sinaliza pausa longa para o renderizador de áudio.

### Formato completo

```markdown
<!-- AGENTE-PROGRESSO
skill: D:\Skillstore\<skill>.md
próximo: 3
última-seção: 2. <título>
última-linha: <última linha do teach>
-->

# Teach: <Título da Skill>

Bem-vindo. Este é um material em áudio derivado da skill <nome>. Cada faixa cobre um conceito independente. Você pode ouvir em qualquer ordem.

---

# 1. <Título narrativo da seção 1>

<abertura>

<desenvolvimento, vários parágrafos>

<regras e armadilhas>

<fechamento>

---

# 2. <Título narrativo da seção 2>

...
```

---

## Golden Rules

1. **Uma seção por vez.** Nunca avance automaticamente para a próxima.
2. **Áudio é o destino.** Tudo que dependa de visualização é proibido no corpo do teach.
3. **Conceito antes de exceção.** Exceção marginal se omite.
4. **Frase curta.** Em caso de dúvida, divida.
5. **Código vira prosa.** Nunca copie o bloco; capture a mensagem.
6. **Equação vira frase.** Sem LaTeX, sem símbolos matemáticos.
7. **Transições explícitas.** O ouvinte não vê parágrafos; precisa de pistas verbais.
8. **Preservar o teach.** Sempre append, nunca sobrescreva capítulos anteriores.
9. **Parar é obrigatório.** Após gravar uma seção, exiba o relatório e aguarde.
10. **Ponteiro é obrigatório.** Crie no primeiro `Write`, atualize a cada Passo 5, remova ao concluir a skill.
11. **Ponteiro exclusivo no teach.** O s_to_t lê e grava ponteiros apenas no arquivo teach. Qualquer `<!-- AGENTE-PROGRESSO -->` no arquivo skill pertence ao k_to_s — ignore-o.

---

## Checklist por Seção

- [ ] Passo 0: índice da skill lido, próxima seção identificada (AGENTE-PROGRESSO da skill ignorado)
- [ ] Passo 0.5: ponteiro lido no arquivo teach (nunca no arquivo skill)
- [ ] Passo 2: seção alvo lida na íntegra (incluindo subseções)
- [ ] Conceito central identificado em uma frase
- [ ] Todos os blocos de código convertidos em prosa
- [ ] Todas as equações reformuladas em palavras
- [ ] Tabelas reformuladas em prosa ou omitidas
- [ ] Listas reformuladas em prosa conectada
- [ ] Frases dentro do alvo de 12 a 18 palavras
- [ ] Nenhuma marcação visual no corpo (negrito, itálico, monospace, bullets, tabelas, blocos de código)
- [ ] Apenas headings de nível 1 entre capítulos
- [ ] Acrônimos expandidos na primeira menção da seção
- [ ] Transições explícitas entre parágrafos
- [ ] Regras prescritivas narradas como "a regra é..."
- [ ] Antipadrões narrados como "um erro comum é..."
- [ ] Fechamento recapitula o conceito central
- [ ] Separador `---` antes do capítulo
- [ ] Ponteiro atualizado com nova posição
- [ ] (Se concluiu a skill) Ponteiro removido
- [ ] Relatório de parada exibido

---

## Erros Comuns

| Erro | Correção |
|---|---|
| Copiar bloco de código no teach | Converter em uma a três frases descrevendo o que o código faz e o conceito que ele demonstra |
| Manter tabela markdown | Reformular como prosa, escolhendo as duas ou três dimensões principais |
| Frase com mais de 25 palavras | Dividir em duas ou mais |
| Manter `**negrito**` ou `*itálico*` | Remover; ênfase é dada pela escolha das palavras |
| Manter \`monospace\` | Remover; o termo técnico aparece em texto normal |
| Avançar várias seções em uma invocação | Proibido. Pare após cada seção e exiba o relatório |
| Incluir URL ou caminho de arquivo | Omitir, salvo quando essencial; se essencial, ler em prosa |
| Acrônimo sem expansão na primeira menção | "API, ou interface de programação..." |
| Pergunta retórica seguida de pausa esperada | Reformular como afirmação |
| Heading de nível 2 ou 3 dentro do teach | Usar apenas `#` de nível 1 entre capítulos; subseções viram parágrafos |
| Manter exceção marginal que confunde o conceito | Omitir ou postergar para o fim do parágrafo de armadilhas |
| Esquecer transição entre parágrafos | Inserir conector explícito ("Em seguida...", "Por outro lado...") |
| Ponto e vírgula, travessão, parênteses | Reescrever a frase sem esses recursos |
| Lista numerada copiada da skill | Reformular como prosa: "Primeiro, ... Em seguida, ... Por fim, ..." |
| Esquecer separador `---` entre capítulos | Inserir sempre antes do próximo `#` |
| Ponteiro não criado no primeiro Write | Inserir bloco `<!-- AGENTE-PROGRESSO ... -->` antes do título |
| Ponteiro não removido ao concluir a skill | Remover o bloco antes do relatório final |
| Reler o arquivo inteiro só para encontrar a última linha | Usar `última-linha` do ponteiro com `Edit(old_string=última-linha, ...)` |
| Ler ou editar o AGENTE-PROGRESSO no arquivo skill | O ponteiro s_to_t existe apenas no teach; o da skill pertence ao k_to_s e deve ser ignorado |
