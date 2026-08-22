# LIÇÕES — série Manuais de Ciências

Log acumulado de erros que custaram build vermelho, render quebrado ou retrabalho.
Vale para todos os manuais da série. Entradas novas vão no fim da seção correspondente.

---

## Novas neste manual (Eletrônica)

1. **`circuitikz` precisa entrar em dois lugares.** No `tlmgr install` (local *e*
   CI) **e** no preâmbulo do template da extensão `danmackinlay/tikz`, depois de
   `pgfplots`. Faltando um dos dois, a figura falha em silêncio no HTML e derruba
   o PDF.

2. **`siunitx`: instalar ≠ usar.** Ele entra na lista do `tlmgr` porque é
   dependência do `circuitikz`, mas continua **proibido no corpo do livro** —
   `\qty` e `\SI` quebram o MathJax no HTML. Unidades vão literais no texto:
   `4,7 kΩ`, `230 V`, `50 Hz`, com vírgula decimal.

3. **Valor de componente é conteúdo, não enfeite.** Todo valor em figura ou
   exercício sai de série comercial (E12/E24 para resistores, E6/E12 para
   capacitores). Quando o cálculo teórico cai fora de série, o texto mostra o
   arredondamento para o valor real **e recalcula o efeito** — isso é metade do
   ofício, e a maioria dos livros de eletrônica pula.

4. **Smoke test por caminho de renderização, não por ferramenta.** `circuitikz`,
   `tikz-timing`, `circuits.logic.US` e `pgfplots` são quatro caminhos distintos.
   Testar um TikZ genérico e assumir que os outros funcionam deixa passar a falha
   que só aparece noventa capítulos adiante.

5. **Heredoc do Bash come a barra dupla.** Escrever `.tex`/`.qmd` por
   `cat > arquivo <<'EOF'` transforma `\\` em `\`. Em LaTeX isso é catastrófico e
   *silencioso*: `\\` de quebra de linha some, `\begin` vindo de string Python
   vira `\b` (backspace, `U+0008`) e o erro que aparece — "Runaway argument",
   "Missing `\begin{document}`" — aponta para o pacote errado. Custou uma
   investigação inteira do `tikztimingtable`, que estava perfeito. **Regra:
   conteúdo com `\\` vai pela ferramenta Write ou por script Python em arquivo,
   nunca por heredoc.** Barra simples (`\draw`, `\usepackage`) sobrevive.

6. **`pgfmath` estoura em ~16384.** Curva de diodo escrita ao natural
   (`1e-6*(exp(x/0.02585)-1)*1000`) passa de $10^{7}$ dentro do domínio e o
   pgfplots morre com "Missing number, treated as zero" + "Illegal unit of
   measure" — e ainda assim **emite um SVG**, então a contagem de `<svg>` não
   pega. Reescrever a exponencial ancorada no valor máximo:
   `{50*exp((x-0.75)/0.0435)}` desenha a mesma curva sem nunca passar de 50.

7. **`=` dentro de rótulo do `circuitikz` quebra o `pgfkeys`.**
   `to[R, l=$R = 470\,\Omega$]` é lido como duas chaves e produz erro de `$`
   desbalanceado. Sempre chavear o valor: `l={$R = 470\,\Omega$}`.

8. **Polaridade se confere, não se adivinha.** `(0,0) to[battery1] (0,3)` põe a
   placa longa (o **positivo**) no *fim* do caminho, ou seja, em cima. Já
   `to[V=...]` desenhado de baixo para cima põe o `+` embaixo. Convenções
   diferentes no mesmo pacote: desenhar um teste lado a lado e olhar custa dois
   minutos e evita um esquemático errado impresso em 104 capítulos.

9. **Contar `<svg>` prova que a figura saiu, não que ela está certa.** Rótulo
   sobreposto, seta invertida e curva estourando o eixo passam por toda a
   validação textual. Por isso existe `figuras/verificar-figuras.py`: extrai os
   blocos `{.tikz}` do capítulo, compila com o preâmbulo real e rasteriza para
   PNG. Rodar antes do commit de qualquer capítulo com figura — foi o que pegou
   `$R$` colidindo com `$V_R$` e `LED` colidindo com `$V_\mathrm{LED}$` no
   capítulo 001.

10. **Emoji nos títulos das seções fixas some no PDF — e tudo bem.** `🧪` e `🔥`
    renderizam no HTML e são descartados em silêncio no caminho LaTeX (sem
    caixinha de glifo faltante, sem erro). O título sai "Laboratório" e "Onde
    Queima", só com um espaço a mais. Comportamento **aceito**: não vale trocar a
    toolchain para lualatex por causa disso.

11. **A emenda entre sessões engole capítulos, e nenhuma validação pega.**
    Custou quatro capítulos neste manual — 025, 026 (fim do Volume 4) e 037, 038
    (fim do Volume 6) —, descobertos só quando o Volume 7 já estava publicado.

    O histórico mostra a mesma forma duas vezes: a sessão escreveu 021→024 e
    acabou; a seguinte começou em **027**, o primeiro capítulo do Volume 5. A
    sessão escreveu 033→036 e acabou; a seguinte começou em **039**, o primeiro
    capítulo do Volume 7. O Volume 5 (027→032) foi o único que coube inteiro numa
    sessão, e é o único sem buraco. **Toda lacuna caiu numa emenda de sessão, e
    toda retomada reancorou numa fronteira de volume — número redondo — em vez do
    próximo capítulo pendente.**

    Quatro coisas falharam juntas, e nenhuma delas é sobre eletrônica:

    - O `/clear` obrigatório entre capítulos faz toda sessão começar fria.
    - O passe de bastão existia, mas só em prosa, no último parágrafo do capítulo
      anterior ("o @sec-cap-025 junta resistor e capacitor..."). Ninguém lê o
      rodapé do capítulo anterior ao abrir sessão.
    - `**Progresso: 41/104**` é **contagem, não fronteira**: lê-se igual com os 41
      contíguos ou esburacados.
    - **O checklist era cego.** Ele caça `?@` — referência não resolvida. Mas
      referência a capítulo-stub *resolve*, porque o stub carrega o rótulo
      `{#sec-cap-NNN}`. Render limpo, `grep` zero, buracos intactos, e o leitor
      clicando para cair numa página "(em elaboração)".

    É a lição 9 noutro eixo: contar `<svg>` prova que a figura saiu, não que ela
    está certa; `?@` zero prova que a referência resolve, não que ela leva a
    conteúdo. **Toda validação que confirma forma precisa de uma irmã que confirme
    substância.**

    O que fica, e vale para qualquer manual da série:

    - **Abrir sessão pelo menor `[ ]` da fila**, nunca pelo primeiro capítulo do
      volume que o usuário nomeou. Se o usuário pedir um volume com lacuna atrás,
      dizer **antes** de escrever — a decisão de pular é dele.
    - **O ROADMAP declara fronteira, não só contagem**: contíguos até, lacunas
      abertas, próximo capítulo. Sessão que termina no meio de um volume atualiza
      esse bloco antes de encerrar.
    - **`ferramentas/verificar-lacunas.py`** mecaniza a checagem: acha todo
      capítulo-stub numerado abaixo do maior escrito, lista os **contratos** —
      cada `@sec-` de texto já publicado que promete aquele conteúdo — e falha com
      código 1. Entrou no checklist de push.
    - Corolário achado pelo próprio script: `@sec-` apontando para capítulo
      **futuro** tem o mesmo sintoma para o leitor (link que resolve numa página
      vazia) e viola a regra de referência cruzada. É defeito de outra natureza —
      o script reporta como aviso, separado das lacunas.

---

## CI / GitHub Actions (`publish.yml`)

- **`chrome-headless-shell`, não `chromium`.** Passo `quarto install
  chrome-headless-shell` *antes* do render/publish — sem ele o grafo mermaid do
  `index.qmd` trava o render do PDF no runner Ubuntu. Visto em Matemática, Física
  e todos os manuais seguintes.

- **Passo "Preparar TeX" — sequência definitiva** (causa raiz de 4 builds
  vermelhos no manual de Economia):
  1. `tlmgr update --self` **antes** de qualquer `tlmgr install` — o TeX Live 2026
     aborta os installs em silêncio sem isso.
  2. Nunca mascarar o install com `|| true`.
  3. Binários do TinyTeX são **symlinks**: detectar com `command -v pdflatex` ou
     `find` **sem** `-type f` (com `-type f` o resultado vem vazio e `$TEXBIN`
     resolve para `.`).
  4. Exportar o bin com `echo "$TEXBIN" >> "$GITHUB_PATH"` **e** criar symlinks de
     `pdflatex`, `latex`, `dvisvgm`, `kpsewhich` em `/usr/local/bin` como reserva.
  5. Falhar alto: verificar com `kpsewhich standalone.cls`,
     `kpsewhich pgfplots.sty`, `dvisvgm --version`.

- **Bootstrap do `gh-pages`** (uma vez, antes do primeiro push):
  ```
  git push origin $(git commit-tree $(git hash-object -t tree /dev/null) -m 'init gh-pages'):refs/heads/gh-pages
  ```
  `quarto-actions/publish@v2` aborta com erro circular se o branch não existir, e
  `quarto publish gh-pages --no-render` se recusa a criá-lo.

---

## Figuras TikZ

- Usar a extensão `danmackinlay/tikz` **com patches locais**. **Nunca** `quarto add`
  nem `quarto update` nela — baixa o upstream sem patches e quebra a renderização.
- `_quarto.yml`: filtro `danmackinlay/tikz` **antes** de `quarto`;
  `tikz: svg-engine: dvisvgm`.
- Sintaxe: `div ::: {#fig-nome}` + bloco `{.tikz}` com `%%| filename:` e `%%| alt:`;
  legenda antes do `:::`; referência via `@fig-nome`.
- O template **sempre** carrega `pgfplots` — toda figura depende dele, mesmo uma
  seta simples. Nunca redefinir.
- Estilos (`curva`, `destaque`, `auxiliar`, `eixo`, `ponto`, `vetor`) e cores
  (`manualblue`, `manualred`, `manualgreen`, `manualyellow`, `manualgray`) vêm do
  template — usar direto.
- **Bloqueio de PATH (falha TikZ mais comum):** `quarto install tinytex` não
  adiciona o bin do TinyTeX ao PATH da sessão. Sintoma: figura falha em silêncio,
  `tikz.lua` erra com `imgdata nil` por volta da linha 587. Prefixar o bin antes de
  qualquer render/preview. Windows: `$HOME/AppData/Roaming/TinyTeX/bin/windows`;
  Linux/macOS: `~/.TinyTeX/bin/<plataforma>`.
- Toolchain local: `quarto install tinytex` + correção de PATH +
  `tlmgr install standalone pgf pgfplots dvisvgm xcolor amsmath amsfonts`.

---

## Quarto / autoria

- **Marcador SCSS em `styles.css`:** se listado em `theme:` (ex.:
  `theme: [cosmo, styles.css]`), o Quarto ≥ 1.9 trata como camada SCSS e exige
  `/*-- scss:rules --*/` na primeira linha. Omitir quebra o render inteiro com erro
  de *layer boundary*. Evitar comentário CSS contendo `*/` logo após o marcador.
- **`lang: pt`** no nível raiz do `_quarto.yml`, não aninhado em `book:`.
- **Stubs antes do render:** em projeto `book`, `quarto render arquivo.qmd` falha
  com "Book chapter not found" se qualquer capítulo do `_quarto.yml` não existir em
  disco. Ao registrar um `part:`, criar os stubs de todos os seus capítulos.
- **Crossrefs:** nunca usar `@sec-`, `@fig-`, `@tbl-` apontando para capítulos ou
  volumes ainda não escritos — rótulo não resolvido vira `?@sec-x` no HTML e no PDF.
  Conteúdo futuro entra como menção textual.
- **PDF:** sempre renderizar localmente antes do push — o caminho LaTeX quebra em
  coisas que o HTML aceita em silêncio.
- **Notação LaTeX:** `^{*}` e não `^\*` (a segunda quebra o PDF).
- **Substituição em massa nos `.qmd`:** Python com `str.replace` (literal), não
  `sed`, quando o texto contiver `\`, `*` ou `^` — o `sed` interpreta metacaractere
  e corrompeu todos os superescritos de um manual. `grep -c` deu contagem enganosa
  na verificação.
- **CSL da ABNT:** baixar com `curl -fsSL` (falha em erro HTTP em vez de salvar
  página de erro); verificar com `head -n 3` e `grep -c "<style"`. Se falhar,
  relatar em vez de substituir silenciosamente por outra CSL.

---

## Claude Code / higiene de sessão

- **Commits no Windows:** flags `-m "..."` simples. Nunca here-string do PowerShell
  (`@'...'@`) dentro do Bash — o `@` vaza para a mensagem do commit.
- **Write exige Read prévio:** se o arquivo foi alterado por fora (bash/heredoc), a
  ferramenta Write recusa com "File has not been read yet". Não misturar edição por
  heredoc com ferramentas de arquivo sem um Read no meio.
- **Avisos inofensivos, nunca investigar:** `LF will be replaced by CRLF` (git no
  Windows) e "Node.js 20 is deprecated" (Actions).
- **Emoji em `print()` de Python:** quebra na codificação do console do Windows.
  Evitar em scripts; em conteúdo de arquivo UTF-8 é seguro. Acento também sai
  mastigado (`Transit\xf3rios`) se o script não reconfigurar a saída — abrir com
  `sys.stdout.reconfigure(encoding="utf-8", errors="replace")` dentro de um
  `try/except`, como faz `ferramentas/verificar-lacunas.py`.
- **O que não estiver em arquivo não sobrevive ao `/clear`.** O `/clear` entre
  capítulos é obrigatório, então toda decisão, dívida ou próximo passo tem de
  aterrissar no `ROADMAP.md`, no `CLAUDE.md` ou num script antes de a sessão
  terminar. Handoff escrito em prosa no fim do capítulo anterior **não** é estado:
  ninguém o lê ao abrir sessão. Ver a lição 11.

---

## Específicas de manual de linguagem de programação (Python)

- Blocos de código são cerca estática ` ```python `, nunca célula ` ```{python} ` —
  evita kernel no runner, cache de `freeze` não revisado e execução de código do
  livro no CI.
- Saída colada precisa ser saída real de um venv limpo. Não quebra o build; quebra
  o leitor.
- Dunder (`__init__`) e asterisco (`*args`) fora de crase viram formatação Markdown;
  `snake_case` fora de crase vira subscrito no PDF.
