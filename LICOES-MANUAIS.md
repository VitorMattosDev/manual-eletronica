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
  Evitar em scripts; em conteúdo de arquivo UTF-8 é seguro.

---

## Específicas de manual de linguagem de programação (Python)

- Blocos de código são cerca estática ` ```python `, nunca célula ` ```{python} ` —
  evita kernel no runner, cache de `freeze` não revisado e execução de código do
  livro no CI.
- Saída colada precisa ser saída real de um venv limpo. Não quebra o build; quebra
  o leitor.
- Dunder (`__init__`) e asterisco (`*args`) fora de crase viram formatação Markdown;
  `snake_case` fora de crase vira subscrito no PDF.
