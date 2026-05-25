<!-- AGENTE-PROGRESSO
skill: D:\Skillstore\solutions_architect_handbook_skill.md
próximo: 2
última-seção: 1. O Significado da Arquitetura de Solução
última-linha: Ignorar os requisitos não-funcionais é o erro mais caro e mais comum.
-->

# Teach: Solutions Architect's Handbook

Bem-vindo. Este é um material em áudio derivado da skill Solutions Architect's Handbook. Cada faixa cobre um conceito independente. Você pode ouvir em qualquer ordem.

---

# 1. O Significado da Arquitetura de Solução

Nesta faixa, você vai entender o que é a arquitetura de solução. Vamos cobrir as responsabilidades de quem a define, os requisitos que ela deve considerar e os princípios que guiam soluções em nuvem. Ao final, você terá o mapa mental para todos os outros tópicos deste material.

A arquitetura de solução estabelece as fundações de qualquer sistema antes que qualquer código seja escrito. Ela define os blocos de construção da implementação e orienta cada decisão técnica que vem depois. A regra é: definir a arquitetura deve sempre ser o primeiro passo.

O profissional responsável por isso é o arquiteto de solução. Ele analisa os requisitos funcionais e define os não-funcionais. Avalia tecnologias por meio de provas de conceito e protótipos. Seleciona a melhor estratégia dentro das restrições de custo, prazo e regulatório. Mentoria o time durante o desenvolvimento e garante a operabilidade do sistema após o lançamento.

O arquiteto de solução sempre avalia em qual cenário está trabalhando. Se o sistema já existe e precisa de melhoria, a prioridade é minimizar o impacto no ambiente atual. A pergunta central é: vale mais rearquitetar ou reconstruir do zero? Se uma reconstrução entrega resultado melhor com menor custo, esse é o caminho certo. Para sistemas novos, há liberdade maior de escolha tecnológica desde o início.

Além dos requisitos funcionais, o arquiteto deve endereçar os requisitos não-funcionais. Eles não são funcionalidades visíveis ao usuário, mas determinam como o sistema se comporta sob pressão. Entre os mais críticos estão a recuperação de desastres, a segurança e conformidade, a alta disponibilidade e a escalabilidade. Um erro comum é tratar esses requisitos como opcionais. Eles têm impacto amplo no projeto e, se ignorados nas fases iniciais, comprometem a entrega.

Definir critérios de sucesso é igualmente importante. Esses critérios devem ser medidos em duas dimensões. A dimensão qualitativa cobre o feedback do usuário e a análise de sentimento sobre o produto. A dimensão quantitativa mede latência, tempo de carregamento e métricas de negócio como volume de vendas. Para a escolha de tecnologia, siga quatro passos. Primeiro, valide todos os requisitos. Depois, crie um protótipo funcional. Avalie agilidade, velocidade e segurança. Por fim, escolha o que simplifica a implementação sem comprometer os requisitos. A regra é preferir construir internamente a depender de ferramentas de terceiros.

Ao trabalhar com nuvem, é preciso entender os quatro modelos principais. Infraestrutura como serviço delega ao cliente o sistema operacional, o runtime e a aplicação. Plataforma como serviço deixa com o cliente apenas os dados e a lógica de negócio. Software como serviço transfere tudo ao fornecedor, e o cliente apenas usa o produto. Funções como serviço, também chamado de serverless, exige do cliente apenas o código da função.

Em seguida, a arquitetura nativa de nuvem vai além dos modelos. Ela foca em escala sob demanda, design distribuído e operações automatizadas. A regra central é: nunca tente recuperar uma instância com falha. Substitua-a automaticamente. A recuperação e a escalabilidade devem ser garantidas por integração contínua e infraestrutura como código.

Uma boa arquitetura de solução também controla o orçamento. Ela reduz incertezas ao fornecer guias de prioridade e detalhes de cada componente ao time. Investir bem na estimativa inicial poupa muito retrabalho ao longo do projeto.

Para fechar esta faixa: a arquitetura de solução define as fundações do sistema antes do desenvolvimento. O arquiteto é responsável por requisitos, tecnologia, execução e operabilidade pós-lançamento. Ignorar os requisitos não-funcionais é o erro mais caro e mais comum.
