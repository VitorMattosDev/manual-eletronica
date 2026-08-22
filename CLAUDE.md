# CLAUDE.md — Manual de Eletrônica

Regras operacionais desta base. Leia inteiro antes do primeiro comando de cada sessão.

---

## Identidade

Livro Quarto (HTML + PDF) em português do Brasil, publicado no GitHub Pages via
GitHub Actions. 104 capítulos, 16 volumes, 5 fases. Parte da série *Manuais de Ciências*.

**Fronteira superior:** o manual termina na porta lógica e na máquina de estados.
ULA completa, banco de registradores, ISA, pipeline, cache e hierarquia de memória
pertencem ao futuro Manual de Arquitetura de Computadores. O capítulo 104 é a
dobradiça explícita entre os dois.

**Fronteira com o Manual de Física:** Física **deriva**, Eletrônica **dimensiona**.
Lá se demonstra a lei de Ohm; aqui se escolhe o resistor, calcula-se a dissipação
e verifica-se se o encapsulamento aguenta.

**Ambiente do leitor:** bancada modesta — multímetro, protoboard, fonte ajustável,
ferro de solda, kit de passivos e discretos. Osciloscópio a partir do Volume 7,
sempre com variante simulada (ngspice/LTspice, Falstad) como plano B.

---

## Seções fixas obrigatórias em TODO capítulo

1. `## 🧪 Laboratório` — roteiro prático executável, **iniciado por lista de
   material explícita** (componentes com valores, instrumentos, quantidades). O
   leitor precisa saber, antes de ler o roteiro, se consegue fazer o experimento
   hoje. Instrumento caro exige variante simulada marcada como tal.
2. `## 🔥 Onde Queima` — modos de falha: o que destrói o componente, o que estoura
   o cálculo, ou onde o instrumento mente. Em capítulo teórico, é o erro de
   raciocínio clássico (ignorar impedância da fonte, confundir pico com RMS,
   esquecer a carga da ponta de prova).

---

## Bootstrap da toolchain (início de sessão, autônomo)

1. `quarto install tinytex`
2. **Corrigir o PATH da sessão.** `quarto install tinytex` **não** adiciona o bin
   do TinyTeX ao PATH. Sem isso as figuras TikZ falham em silêncio e `tikz.lua`
   estoura com `imgdata nil` por volta da linha 587.
   - Windows: `$HOME/AppData/Roaming/TinyTeX/bin/windows`
   - Linux/macOS: `~/.TinyTeX/bin/<plataforma>`
   - Se `tlmgr` não aparecer no PATH, localize com `find` antes de prosseguir.
3. `tlmgr update --self`
4. `tlmgr install standalone pgf pgfplots dvisvgm xcolor amsmath amsfonts circuitikz tikz-timing siunitx`

---

## Figuras

### Regras herdadas

- Extensão `danmackinlay/tikz` **com patches locais**. **Nunca** rodar `quarto add`
  ou `quarto update` nela — baixa o upstream sem patches e quebra a renderização.
- Em `_quarto.yml`: filtro `danmackinlay/tikz` **antes** de `quarto`;
  `tikz: svg-engine: dvisvgm`.
- Sintaxe: `div ::: {#fig-nome}` + bloco `{.tikz}` com `%%| filename:` e `%%| alt:`;
  legenda antes do `:::`; referência com `@fig-nome`.
- O template **sempre** carrega `pgfplots` — toda figura depende dele, mesmo uma
  seta simples. Nunca redefinir.
- Estilos (`curva`, `destaque`, `auxiliar`, `eixo`, `ponto`, `vetor`) e cores
  (`manualblue`, `manualred`, `manualgreen`, `manualyellow`, `manualgray`) vêm do
  template. Usar direto, nunca redefinir.

### Regras novas deste manual

- Adicionar ao preâmbulo do template: `\usepackage{circuitikz}`,
  `\usepackage{tikz-timing}`, `\usetikzlibrary{circuits.logic.US}`.
  `circuitikz` vem **depois** de `pgfplots`.
- Ferramenta por tipo de figura:

  | Tipo | Ferramenta |
  |---|---|
  | esquemático de circuito | `circuitikz` |
  | forma de onda / cronograma digital | `tikz-timing` |
  | porta lógica, bloco digital | `circuits.logic.US` |
  | curva característica, Bode, resposta no tempo | `pgfplots` |
  | diagrama conceitual | TikZ puro |

- **Smoke test das quatro categorias antes do capítulo 001.** Não escrever
  capítulo nenhum sem os quatro SVGs confirmados no `_book`.
- Fotografia (componentes reais, encapsulamentos, instrumentos, soldagem): imagem
  embutida, não TikZ. Acumular pendências em `FIGURAS.md`.

---

## Notação e valores

- **`siunitx` proibido no corpo do livro** — quebra o MathJax no HTML. Está
  instalado apenas como dependência do `circuitikz`. Instalar ≠ usar.
- Unidades literais: `10 kΩ`, `4,7 µF`, `230 V`, `50 Hz`. Em modo matemático,
  `\Omega`, `\mu`, `\times`.
- **Vírgula decimal** em todo o livro.
- **Todo valor de componente é valor comercial real** (E12/E24 para resistores,
  E6/E12 para capacitores). Nada de 3,7 kΩ ou 137 nF. Cálculo fora de série:
  mostrar o arredondamento e **recalcular o efeito**.
- Tolerância e faixa aparecem sempre que o resultado depender delas.
- `^{*}` e nunca `^\*` (a segunda forma quebra o PDF).
- Capítulos 002, 048, 072, 073 e 075: bloco `.callout-warning` explícito antes de
  qualquer roteiro.

---

## Convenções Quarto

- `lang: pt` no **nível raiz** do `_quarto.yml`, não aninhado em `book:`.
- `styles.css` em `theme:` é camada SCSS no Quarto ≥ 1.9: primeira linha
  **obrigatoriamente** `/*-- scss:rules --*/`. Sem isso o render inteiro morre com
  erro de *layer boundary*. Evitar comentário CSS com `*/` logo após o marcador.
- **Stubs antes de renderizar.** `quarto render` falha com "Book chapter not found"
  se qualquer capítulo do `_quarto.yml` não existir em disco. Ao registrar um
  `part:`, criar imediatamente os stubs de todos os capítulos dele.
- **Referências cruzadas:** `@sec-`, `@fig-`, `@tbl-` só para rótulos **já
  escritos** (mesmo volume ou anterior). Conteúdo futuro entra como menção textual
  ("assunto do Volume 11"), nunca `@sec-`. Rótulo não resolvido vira `?@sec-x`.
- **Renderizar o PDF localmente antes de cada push.** O caminho LaTeX quebra em
  coisas que o HTML aceita calado.
- **Substituição em massa nos `.qmd`:** Python com `str.replace` (literal). Nada de
  `sed` quando houver `\`, `*` ou `^` — já corrompeu superescritos em outro manual.
  `grep -c` dá contagem enganosa na verificação.
- CSL da ABNT: baixar com `curl -fsSL` (falha em erro HTTP em vez de salvar página
  de erro). Verificar com `head -n 3` e `grep -c "<style"`. Falhou? **Relatar**, não
  substituir por outra CSL.

---

## CI

Ver `.github/workflows/publish.yml`. Pontos que já causaram build vermelho:

- `quarto install chrome-headless-shell` **antes** do render/publish.
- `tlmgr update --self` **antes** de qualquer `tlmgr install`.
- Nunca mascarar install com `|| true`.
- Binários do TinyTeX são symlinks: `find` **sem** `-type f`.
- Exportar bin via `$GITHUB_PATH` **e** symlinks em `/usr/local/bin`.
- Verificar com `kpsewhich` + `dvisvgm --version`.

**Bootstrap do `gh-pages`** (uma vez, antes do primeiro push):

```
git push origin $(git commit-tree $(git hash-object -t tree /dev/null) -m 'init gh-pages'):refs/heads/gh-pages
```

Sem isso o `quarto-actions/publish@v2` aborta com erro circular, e
`quarto publish gh-pages --no-render` se recusa a criar o branch.

---

## Fluxo de trabalho

**Abertura de sessão — primeiro comando, sempre:** ler o bloco "Estado da fila"
do `ROADMAP.md` e rodar `python ferramentas/verificar-lacunas.py`. O capítulo a
escrever é o **menor `[ ]` da fila**, nunca o primeiro capítulo do volume que o
usuário nomeou. Se o usuário pedir um volume cujos anteriores têm lacuna,
**dizer isso antes de escrever**, não no relatório final — a decisão de pular é
dele, e ele precisa tomá-la com a informação na mão. Já custou quatro capítulos
(ver a lição 11 do `LICOES-MANUAIS.md`).

**Fatia vertical:** completar todos os capítulos de um volume antes de abrir o
próximo; completar a Fase 1 antes da Fase 2. **A regra vale entre sessões, não só
dentro de uma.** Sessão que acabar no meio de um volume atualiza o bloco "Estado
da fila" do `ROADMAP.md` — contíguos até, lacunas abertas, próximo capítulo —
antes de encerrar. O `/clear` apaga a conversa; o que não estiver em arquivo
não sobrevive.

**Por capítulo:** escrever → `quarto render --to html` → validação rápida →
commit `cap NNN: <título>` com o status do `ROADMAP.md` atualizado **no mesmo commit**.

**Validação rápida** (sem abrir o HTML): contar `<svg` no `_book` contra o número
de blocos `{.tikz}` nos `.qmd`; `grep` por `?@` e `[?]` órfãos. Atenção: `?@` zero
prova que a referência **resolve**, nunca que ela leva a conteúdo — capítulo-stub
carrega o rótulo `{#sec-cap-NNN}` e resolve normalmente, com o leitor caindo numa
página vazia. Quem pega isso é `ferramentas/verificar-lacunas.py`.

**Verificação visual das figuras** (capítulo com figura, antes do commit):
`python figuras/verificar-figuras.py capitulos/NNN-....qmd` → gera um PNG com
todas as figuras do capítulo, compiladas com o preâmbulo real. Contar `<svg`
prova que a figura saiu, **nunca** que ela está certa: rótulo sobreposto, seta
invertida e polaridade trocada passam ilesos por toda a validação textual.

**Checklist antes de cada push:**

1. `quarto render --to html` (livro inteiro)
2. `grep -roE '\?@[a-zA-Z0-9_-]+' _book --include=*.html` → zero resultados
3. `<svg` no `_book` × blocos `{.tikz}` nos `.qmd` — pega figura que falhou calada
4. `python ferramentas/verificar-lacunas.py` → sem lacuna atrasada (código 0), ou
   lacuna aceita conscientemente e **declarada** no bloco "Estado da fila" do
   `ROADMAP.md`. Pega o buraco no meio do livro, que o item 2 não pega.
5. nenhuma citação crua `@chave` no HTML
6. renderizar o PDF localmente
7. após push: `gh run watch <id> --exit-status`; URL do Pages retornando 200 em
   `curl -s -o /dev/null -w "%{http_code}"`

**Higiene:** `/clear` entre capítulos, `/compact` perto de 80 % de contexto.
`sonnet` para tarefa mecânica, `opus` para escrever capítulo.

**Autonomia:** escrita de arquivos, criação de figuras, comandos de validação e
commits por capítulo estão **pré-aprovados**. Parar apenas em erro bloqueante real,
e nesse caso **relatar** em vez de contornar.

---

## Armadilhas de ambiente

- Commits no Windows: `-m "..."` simples. Nunca here-string do PowerShell
  (`@'...'@`) dentro do Bash — o `@` vaza para a mensagem.
- **Heredoc do Bash converte `\\` em `\` em silêncio.** Nunca escrever `.tex`,
  `.qmd` ou script Python com `\\` por `cat > arquivo <<'EOF'`. O estrago é
  invisível e o erro do LaTeX aponta para o lugar errado (`\begin` virando
  `U+0008`, "Runaway argument" acusando pacote inocente). Conteúdo com barra
  dupla vai pela ferramenta Write ou por script Python em arquivo. Barra simples
  (`\draw`, `\usepackage`) sobrevive.
- A ferramenta Write exige Read prévio se o arquivo foi alterado por fora
  (bash/heredoc). Não misturar heredoc com ferramentas de arquivo sem Read no meio.
- Ignorar sem investigar: `LF will be replaced by CRLF`; "Node.js 20 is deprecated".
- Sem emoji dentro de `print()` de script Python — quebra no console do Windows.
  Em conteúdo de arquivo UTF-8 é seguro.
