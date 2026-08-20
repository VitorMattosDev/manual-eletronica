# PROMPT INICIAL — Manual de Eletrônica

> Cole este arquivo inteiro na primeira mensagem do Claude Code, dentro do diretório
> `C:\Users\Usuario\Desktop\MANUAIS\manual-eletronica` (repositório vazio ou recém-criado).
> Modelo recomendado para esta sessão: **opus**.

---

## 0. Contexto e autorização

Você vai construir o **Manual de Eletrônica**, mais um volume da série *Manuais de Ciências*: livro Quarto (HTML + PDF), em português do Brasil, publicado no GitHub Pages via GitHub Actions. O padrão é o mesmo dos manuais de Matemática, Física, Química, Economia, Segurança da Informação, Linux e Python.

**Você está pré-autorizado** a criar e editar arquivos, criar figuras, rodar comandos de validação e fazer commits por capítulo **sem pedir aprovação**. Só pare se encontrar um erro verdadeiramente bloqueante — e, nesse caso, relate o erro em vez de contornar silenciosamente.

Esta sessão termina quando o **capítulo 001** estiver escrito, renderizado, validado e commitado, com o deploy verde no GitHub Pages.

---

## 1. Identidade do manual

- **Ênfase:** eletrônica do zero até a lógica digital — teoria elétrica, corrente alternada, semicondutores, analógica, energia, construção física e digital. É o **pré-requisito** do futuro Manual de Arquitetura de Computadores.
- **Fronteira superior (importante):** o manual **termina na porta lógica e na máquina de estados**. ULA completa, banco de registradores, ISA, pipeline, cache e hierarquia de memória **não** entram aqui — são do manual de arquitetura. O capítulo 104 é explicitamente a dobradiça entre os dois.
- **Fronteira com o Manual de Física:** Física **deriva**, Eletrônica **dimensiona**. Lá se demonstra a lei de Ohm a partir do modelo de condução; aqui se escolhe o resistor, calcula a dissipação e verifica se o encapsulamento aguenta.
- **Escala:** 104 capítulos, 16 volumes, 5 fases.
- **Ambiente de referência do leitor:** bancada modesta — multímetro, protoboard, fonte ajustável, ferro de solda, kit de componentes passivos e discretos. Osciloscópio a partir do Volume 7 (indicar alternativa por placa de som ou osciloscópio USB quando possível). Simulação em **ngspice/LTspice** e **Falstad** como complemento, nunca como substituto do laboratório.

### Seções fixas obrigatórias em **todo** capítulo

1. **`## 🧪 Laboratório`** — roteiro prático executável, iniciado por uma **lista de material explícita** (componentes com valores, instrumentos, quantidade). O leitor precisa saber, antes de ler o roteiro, se consegue fazer o experimento hoje. Quando o experimento exigir instrumento caro, ofereça a variante simulada como plano B, marcada como tal.
2. **`## 🔥 Onde Queima`** — modos de falha do tópico: o que destrói o componente, o que estoura o cálculo, ou onde o instrumento mente. Nos capítulos teóricos, é o erro de raciocínio clássico (ignorar impedância da fonte, confundir valor de pico com RMS, esquecer a resistência da ponta de prova).

---

## 2. Estrutura completa (vai integral para o `ROADMAP.md`)

### Fase 1 — Fundamentos Elétricos (001–026)

**Volume 1 — A Bancada e o Método (001–007)**
1. O que é eletrônica e o que este manual cobre
2. Segurança elétrica: choque, arco, capacitores carregados e a rede
3. Grandezas, unidades e ordens de grandeza
4. O multímetro: tensão, corrente, resistência e continuidade
5. A protoboard, a fonte de bancada e a montagem limpa
6. Componentes passivos: identificação, código de cores e tolerância
7. Esquemáticos: como ler, como desenhar, como não se perder

**Volume 2 — Corrente Contínua: Leis Fundamentais (008–014)**
8. Carga, corrente e o modelo de condução
9. Tensão, potencial e referência (terra)
10. Resistência, resistividade e a Lei de Ohm
11. Potência, energia e dissipação térmica
12. Associação série e paralelo
13. As Leis de Kirchhoff
14. Divisores de tensão e de corrente

**Volume 3 — Análise de Circuitos (015–020)**
15. Análise nodal
16. Análise de malhas
17. Superposição e linearidade
18. Teoremas de Thévenin e Norton
19. Máxima transferência de potência e casamento
20. Fontes reais, resistência interna e carregamento do circuito

**Volume 4 — Capacitores, Indutores e Transitórios (021–026)**
21. Campo elétrico e capacitância
22. O capacitor real: tipos, ESR e tensão de trabalho
23. Campo magnético e indutância
24. O indutor real e a energia armazenada
25. Transitórios RC: carga, descarga e constante de tempo
26. Transitórios RL e circuitos RLC no domínio do tempo

### Fase 2 — Corrente Alternada e Sinais (027–045)

**Volume 5 — Fundamentos de Corrente Alternada (027–032)**
27. Do CC ao CA: a senoide e seus parâmetros
28. Valor médio, valor eficaz (RMS) e o que o multímetro realmente mede
29. Fasores e números complexos aplicados
30. Reatância e impedância
31. Potência ativa, reativa e aparente
32. Fator de potência e correção

**Volume 6 — Filtros e Resposta em Frequência (033–038)**
33. Filtro RC passa-baixas e frequência de corte
34. Filtro RC passa-altas e acoplamento
35. Diagramas de Bode: ganho e fase
36. Filtros LC e ordem do filtro
37. Ressonância série e paralela
38. Fator de qualidade, largura de banda e seletividade

**Volume 7 — Sinais, Ruído e Instrumentação (039–045)**
39. Sinais periódicos, forma de onda e ciclo de trabalho
40. Fourier na prática: harmônicos e largura de banda
41. O decibel e as escalas logarítmicas
42. Ruído: térmico, de disparo e interferência externa
43. O osciloscópio: base de tempo, ganho vertical e gatilho
44. Pontas de prova, compensação e artefatos de medição
45. Gerador de funções e ensaio de resposta em frequência

### Fase 3 — Semicondutores e Eletrônica Analógica (046–071)

**Volume 8 — Diodos e Aplicações (046–051)**
46. Semicondutores, dopagem e a junção PN
47. O diodo real: curva, queda direta e modelos
48. Retificadores de meia onda e de onda completa
49. Filtragem capacitiva e ondulação
50. Diodo Zener e regulação por referência
51. LEDs, fotodiodos e diodos especiais: Schottky, TVS e varicap

**Volume 9 — Transistores Bipolares (052–058)**
52. O transistor bipolar: estrutura e funcionamento
53. Curvas características e regiões de operação
54. O BJT como chave: corte, saturação e acionamento de cargas
55. Polarização: divisor de base, resistor de emissor e estabilidade térmica
56. Emissor comum: ganho, impedâncias e limitações
57. Coletor comum e base comum
58. Modelo de pequenos sinais e análise em CA

**Volume 10 — MOSFETs e Amplificação (059–064)**
59. JFET e MOSFET: princípio de funcionamento
60. Curvas, região ôhmica e região de saturação
61. O MOSFET como chave de potência: RDS(on), efeito Miller e dissipação
62. Drivers de gate e a comutação real
63. Classes de amplificador: A, B, AB, C e D
64. Realimentação negativa: ganho, distorção e estabilidade

**Volume 11 — Amplificadores Operacionais (065–071)**
65. O amp-op ideal e as regras de ouro
66. Amplificador inversor e não inversor
67. Somador, subtrator e amplificador de instrumentação
68. Integrador, derivador e fontes de corrente
69. O amp-op real: offset, slew rate, produto ganho-banda e saturação
70. Comparadores, histerese e o gatilho de Schmitt
71. Filtros ativos e osciladores: Wien, relaxação e o 555

### Fase 4 — Energia, Interface e Construção (072–087)

**Volume 12 — Fontes e Gestão de Energia (072–077)**
72. Transformadores e acoplamento magnético
73. Fontes lineares: do transformador ao regulador
74. Reguladores integrados: série, LDO e dissipação térmica
75. Fontes chaveadas: buck, boost e buck-boost
76. Baterias, células e circuitos de carga
77. Aterramento, malhas de terra, desacoplamento e proteção

**Volume 13 — Interface com o Mundo Físico (078–082)**
78. Sensores: resistivos, capacitivos e ativos
79. Condicionamento de sinal e a cadeia de medição
80. Conversão analógico-digital: amostragem, quantização e aliasing
81. Conversão digital-analógica e PWM
82. Atuadores: relés, solenoides e motores CC

**Volume 14 — Da Bancada ao Circuito Real (083–087)**
83. Soldagem: técnica, ferramentas e retrabalho
84. Do esquemático ao layout de PCB
85. Fabricação, montagem e componentes SMD
86. Integridade de sinal, EMI e compatibilidade eletromagnética
87. Depuração de placa: método, medição e falhas típicas

### Fase 5 — Eletrônica Digital (088–104)

**Volume 15 — Lógica Digital: da Chave à Porta (088–095)**
88. Do analógico ao digital: níveis, margens de ruído e o sinal binário
89. Sistemas de numeração e representação binária
90. Álgebra booleana e as portas fundamentais
91. Portas com diodos, portas com transistores e a família TTL
92. A família CMOS: funcionamento, consumo e interface entre famílias
93. Circuitos combinacionais: multiplexadores, decodificadores e comparadores
94. Simplificação: formas canônicas e mapas de Karnaugh
95. Aritmética binária em hardware: somadores e a ULA elementar

**Volume 16 — Sequencial, Memória e a Ponte para o Computador (096–104)**
96. Realimentação digital: o latch SR
97. Flip-flops D e JK e o conceito de borda
98. O clock, temporização, setup e hold
99. Registradores e deslocadores
100. Contadores síncronos e assíncronos
101. Máquinas de estado finito: Moore e Mealy
102. Memórias: célula SRAM, DRAM e não voláteis
103. Lógica programável: CPLD, FPGA e a descrição de hardware
104. Da porta lógica ao processador: a fronteira com a arquitetura

---

## 3. Bootstrap da toolchain (fazer **antes** de qualquer coisa)

Execute autonomamente, na ordem:

1. `quarto install tinytex`
2. **Corrija o PATH da sessão** — `quarto install tinytex` **não** adiciona o `bin` do TinyTeX ao PATH. Sem isso, as figuras TikZ falham em silêncio e o `tikz.lua` estoura com `imgdata nil` por volta da linha 587.
   - Windows: `$HOME/AppData/Roaming/TinyTeX/bin/windows`
   - Linux/macOS: `~/.TinyTeX/bin/<plataforma>`
   - Se `tlmgr` não estiver no PATH depois da instalação, localize-o com `find` antes de prosseguir.
3. `tlmgr update --self`
4. `tlmgr install standalone pgf pgfplots dvisvgm xcolor amsmath amsfonts circuitikz tikz-timing siunitx`
   - `circuitikz` e `tikz-timing` são **novidade deste manual** — esquemáticos e diagramas de temporização.
   - `siunitx` entra aqui **apenas** como dependência do `circuitikz`; **não** use `\qty`/`\SI` no corpo do livro (ver §5).
5. Baixe a CSL da ABNT com `curl -fsSL` (nunca `-O` simples — precisa falhar em erro HTTP, não salvar uma página de erro):
   `https://raw.githubusercontent.com/citation-style-language/styles/master/associacao-brasileira-de-normas-tecnicas.csl`
   Verifique com `head -n 3` e `grep -c "<style"`. Se falhar, **relate** — não substitua por outra CSL.

---

## 4. Figuras TikZ — regras herdadas e as novas

### Herdadas (valem em todos os manuais)

- Use a extensão `danmackinlay/tikz` **com os patches locais** (do `figuras-tikz-kit.zip` / `FIGURAS.md`). **Nunca** rode `quarto add` ou `quarto update` nela — baixa o upstream sem os patches e quebra a renderização.
- Arquivos em `_extensions/danmackinlay/tikz/`. No `_quarto.yml`: filtro `danmackinlay/tikz` **antes** de `quarto`; `tikz: svg-engine: dvisvgm`.
- Sintaxe: `div ::: {#fig-nome}` + bloco `{.tikz}` com `%%| filename:` e `%%| alt:`; legenda antes do `:::`; referência com `@fig-nome`.
- O template **sempre** carrega `pgfplots` — toda figura depende dele, mesmo uma seta simples. Nunca redefina.
- Estilos predefinidos (`curva`, `destaque`, `auxiliar`, `eixo`, `ponto`, `vetor`) e cores (`manualblue`, `manualred`, `manualgreen`, `manualyellow`, `manualgray`) vêm do template — use direto, nunca redefina.

### Novas, específicas deste manual

- **Adicione ao preâmbulo do template da extensão:** `\usepackage{circuitikz}`, `\usepackage{tikz-timing}` e `\usetikzlibrary{circuits.logic.US}`. Convivem com `pgfplots` sem conflito, mas a ordem importa: `circuitikz` **depois** de `pgfplots`.
- **Divisão de ferramenta por tipo de figura:**
  - esquemático de circuito → `circuitikz` (ambiente `circuitikz`, coordenadas em `to[R=$R_1$]`)
  - forma de onda / cronograma digital → `tikz-timing`
  - porta lógica e diagrama de blocos digital → `circuits.logic.US`
  - curva característica, Bode, resposta no tempo → `pgfplots`
  - diagrama conceitual → TikZ puro
- **Smoke test obrigatório antes do capítulo 001:** renderize **uma figura de cada uma das quatro** primeiras categorias acima (circuitikz, tikz-timing, circuits.logic.US, pgfplots) e confirme que os quatro SVGs saíram no `_book`. Não escreva capítulo nenhum antes disso. É exatamente o tipo de falha que só aparece no PDF depois de vinte capítulos escritos.
- **Fotografia:** componentes reais, encapsulamentos, instrumentos e soldagem são conteúdo dependente de foto. Use imagem embutida (`.png`/`.jpg`), não TikZ. Registre no `FIGURAS.md` a lista de fotos pendentes por capítulo em vez de improvisar desenho ruim.

---

## 5. Notação e valores — regras deste domínio

- **`siunitx` está proibido no corpo do livro** (quebra o MathJax no HTML). Escreva as unidades literalmente, com espaço fino não separável: `10 kΩ`, `4,7 µF`, `230 V`, `50 Hz`. Em modo matemático use `\Omega`, `\mu`, `\times`.
- **Vírgula decimal** em todo o livro (padrão brasileiro): `4,7 kΩ`, não `4.7 kΩ`.
- **Todo valor de componente em esquemático e exercício deve ser um valor comercial real**, das séries E12/E24 para resistores e E6/E12 para capacitores. Nada de resistor de 3,7 kΩ ou capacitor de 137 nF. Quando o cálculo der um valor fora de série, **mostre o arredondamento para o valor comercial e recalcule o efeito** — isso é metade do ofício.
- **Tolerância e faixa** aparecem sempre que o resultado depender delas. Um divisor com resistores de 5 % não entrega tensão exata, e o leitor precisa ver isso escrito.
- Use `^{*}` e nunca `^\*` em superescritos (a segunda forma quebra o PDF).
- Nos capítulos que envolvem rede elétrica, alta tensão ou capacitores de fonte (002, 048, 072, 073, 075), abra com um **bloco de aviso explícito** (callout `.warning`) antes de qualquer roteiro.

---

## 6. Convenções Quarto (herdadas — não repita erros antigos)

- `lang: pt` no **nível raiz** do `_quarto.yml`, não aninhado em `book:`.
- `styles.css` listado em `theme:` é tratado como camada SCSS pelo Quarto ≥ 1.9: **a primeira linha do arquivo deve ser** `/*-- scss:rules --*/`. Sem isso, o render inteiro morre com erro de "layer boundary". Evite comentário CSS contendo `*/` logo após o marcador.
- **Stubs antes de renderizar:** em projeto `book`, `quarto render` falha com "Book chapter not found" se qualquer capítulo listado no `_quarto.yml` não existir em disco. Ao registrar um bloco `part:`, crie imediatamente os stubs de **todos** os capítulos dele (`# Título` + `*(em elaboração)*`).
- **Referências cruzadas:** `@sec-`, `@fig-` e `@tbl-` **só** para rótulos já escritos (mesmo volume ou anterior). Referência a conteúdo futuro é **menção textual** ("assunto do Volume 11"), nunca `@sec-`. Rótulo não resolvido vira `?@sec-x` no HTML e no PDF.
- **Renderize o PDF localmente antes de cada push.** O caminho LaTeX quebra em coisas que o HTML aceita calado.
- **Substituições em massa nos `.qmd`:** use Python com `str.replace` (literal). Nada de `sed` quando o texto tiver `\`, `*` ou `^` — o `sed` interpreta metacaractere e já corrompeu superescritos em outro manual. `grep -c` dá contagem enganosa na verificação.

---

## 7. CI — `publish.yml`

- Passo `quarto install chrome-headless-shell` **antes** do render/publish (sem ele o grafo mermaid do `index.qmd` trava o PDF no runner Ubuntu).
- Passo "Preparar TeX", nesta sequência exata:
  1. `tlmgr update --self` **antes** de qualquer `tlmgr install` — o TeX Live 2026 aborta os installs em silêncio se você pular isso.
  2. **Nunca** mascare o install com `|| true`.
  3. Binários do TinyTeX são **symlinks**: detecte com `command -v pdflatex` ou `find` **sem** `-type f` (com `-type f` o resultado vem vazio e `$TEXBIN` vira `.`).
  4. Exporte o bin com `echo "$TEXBIN" >> "$GITHUB_PATH"` **e** crie symlinks de `pdflatex`, `latex`, `dvisvgm`, `kpsewhich` em `/usr/local/bin` como reserva.
  5. Falhe alto: verifique com `kpsewhich standalone.cls`, `kpsewhich pgfplots.sty`, `kpsewhich circuitikz.sty`, `dvisvgm --version`.
- **Bootstrap do `gh-pages` (uma vez, antes do primeiro push):**
  ```
  git push origin $(git commit-tree $(git hash-object -t tree /dev/null) -m 'init gh-pages'):refs/heads/gh-pages
  ```
  O `quarto-actions/publish@v2` aborta com erro circular se o branch não existir, e `quarto publish gh-pages --no-render` se recusa a criá-lo.

---

## 8. Arquivos a criar na raiz

- `CLAUDE.md` — regras de toolchain + instruções de sessão (tudo das seções 3 a 7 deste prompt, condensado)
- `ROADMAP.md` — fila autoritativa dos 104 capítulos com status
- `PROMPT-INICIAL.md` — este arquivo
- `LICOES-MANUAIS.md` — log de lições, começando com as três regras novas abaixo
- `FIGURAS.md` — convenções TikZ/circuitikz + lista de fotos pendentes
- `README.md` — incluindo o comando de bootstrap do `gh-pages`

### Entradas iniciais do `LICOES-MANUAIS.md` (novas, não existiam nos manuais anteriores)

1. **`circuitikz` precisa entrar em dois lugares:** no `tlmgr install` (local e CI) **e** no preâmbulo do template da extensão `danmackinlay/tikz`, depois de `pgfplots`. Faltando um dos dois, a figura falha em silêncio no HTML e derruba o PDF.
2. **`siunitx` continua proibido no corpo do texto**, mas passa a ser instalado como dependência do `circuitikz`. Instalar ≠ usar. Unidades vão literais no texto.
3. **Valor de componente é conteúdo, não enfeite:** todo valor em figura ou exercício sai de série comercial (E12/E24), e o arredondamento do cálculo teórico para o valor real é parte da explicação.

---

## 9. Fluxo de trabalho

**Estratégia de fatia vertical:** complete todos os capítulos de um volume antes de abrir o próximo; complete a Fase 1 antes da Fase 2.

**Por capítulo:** escrever → `quarto render --to html` → validação rápida → commit `cap NNN: <título>` com o status do `ROADMAP.md` atualizado **no mesmo commit**.

**Validação rápida por capítulo** (sem abrir o HTML): contar `<svg` no `_book` contra o número de blocos `{.tikz}` nos `.qmd`; `grep` por `?@` e `[?]` órfãos.

**Checklist completo antes de cada push:**
1. `quarto render --to html` (livro inteiro)
2. `grep -roE '\?@[a-zA-Z0-9_-]+' _book --include=*.html` → deve retornar zero
3. contar `<svg` no `_book` contra o número de blocos `{.tikz}` — pega figura que falhou calada
4. confirmar que não restou citação crua `@chave` no HTML
5. renderizar o PDF localmente
6. depois do push: `gh run watch <id> --exit-status` e `curl -s -o /dev/null -w "%{http_code}"` na URL do Pages → 200

**Higiene de sessão:** `/clear` entre capítulos; `/compact` ao chegar perto de 80 % de contexto. Use `sonnet` para tarefas mecânicas (atualizar `_quarto.yml`, criar stubs) e `opus` para escrever capítulo.

**Armadilhas de ambiente:**
- Commits no Windows: use `-m "..."` simples. Nunca here-string do PowerShell (`@'...'@`) dentro do Bash — o `@` vaza para a mensagem.
- A ferramenta Write exige Read prévio se o arquivo foi alterado por fora (bash/heredoc). Não misture edição por heredoc com ferramentas de arquivo sem um Read no meio.
- Ignore sem investigar: `LF will be replaced by CRLF` e "Node.js 20 is deprecated".
- Sem emoji dentro de `print()` de script Python — quebra no console do Windows. Em conteúdo de arquivo UTF-8 é seguro.

---

## 10. Ordem desta sessão

1. Bootstrap da toolchain (§3) — incluindo `circuitikz` e `tikz-timing`
2. Esqueleto do repositório: `_quarto.yml` com as 5 fases e 16 volumes, extensão TikZ com o preâmbulo ajustado, `styles.css` com o marcador SCSS, CSL da ABNT, `publish.yml`
3. **Stubs dos 104 capítulos** antes de qualquer render
4. Arquivos de raiz (§8)
5. Bootstrap do `gh-pages`
6. **Smoke test das quatro categorias de figura** — só prossiga com os quatro SVGs confirmados
7. `index.qmd` com o grafo mermaid de pré-requisitos e a apresentação do manual
8. **Capítulo 001** completo, com `🧪 Laboratório` e `🔥 Onde Queima`
9. Checklist completo (§9), push, e verificação do deploy verde

Comece pelo passo 1.
