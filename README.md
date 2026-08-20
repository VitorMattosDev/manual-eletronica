# Manual de Eletrônica

Livro aberto sobre eletrônica, da carga elétrica à máquina de estados finita.
Parte da série **Manuais de Ciências**. Escrito em português do Brasil, publicado
em HTML e PDF via Quarto + GitHub Pages.

**104 capítulos · 16 volumes · 5 fases.**

O manual termina na porta lógica e na máquina de estados. Unidade lógica e
aritmética completa, conjunto de instruções, pipeline e hierarquia de memória
pertencem ao Manual de Arquitetura de Computadores — o capítulo 104 é a dobradiça
entre os dois.

## Estrutura

| Fase | Volumes | Capítulos |
|---|---|---|
| 1 — Fundamentos Elétricos | 1–4 | 001–026 |
| 2 — Corrente Alternada e Sinais | 5–7 | 027–045 |
| 3 — Semicondutores e Eletrônica Analógica | 8–11 | 046–071 |
| 4 — Energia, Interface e Construção | 12–14 | 072–087 |
| 5 — Eletrônica Digital | 15–16 | 088–104 |

Fila completa em [`ROADMAP.md`](ROADMAP.md).

## Bootstrap

### 1. Extensão TikZ (obrigatório antes de qualquer render)

Copiar `_extensions/danmackinlay/tikz/` de um manual existente da série (ou do
`figuras-tikz-kit.zip`). É uma versão **patchada localmente** — nunca rodar
`quarto add` ou `quarto update` nela.

Depois, acrescentar ao preâmbulo do template, **depois** de `pgfplots`:

```latex
\usepackage{circuitikz}
\usepackage{tikz-timing}
\usetikzlibrary{circuits.logic.US}
```

### 2. Toolchain LaTeX

```bash
quarto install tinytex
# corrigir o PATH da sessao — quarto install NAO faz isso:
#   Windows:      $HOME/AppData/Roaming/TinyTeX/bin/windows
#   Linux/macOS:  ~/.TinyTeX/bin/<plataforma>
tlmgr update --self
tlmgr install standalone pgf pgfplots dvisvgm xcolor amsmath amsfonts circuitikz tikz-timing siunitx
```

### 3. Branch `gh-pages` (uma vez, antes do primeiro push)

```bash
git push origin $(git commit-tree $(git hash-object -t tree /dev/null) -m 'init gh-pages'):refs/heads/gh-pages
```

Sem isso o `quarto-actions/publish@v2` aborta com erro circular.

### 4. Render

```bash
quarto render --to html
quarto render --to pdf
```

## Convenções

Detalhadas em [`CLAUDE.md`](CLAUDE.md), [`FIGURAS.md`](FIGURAS.md) e
[`LICOES-MANUAIS.md`](LICOES-MANUAIS.md). As principais:

- Todo capítulo tem `## 🧪 Laboratório` (com lista de material) e `## 🔥 Onde Queima`.
- Unidades literais com vírgula decimal: `4,7 kΩ`. `siunitx` não é usado no texto.
- Todo valor de componente é comercial real (E12/E24).
- Commit por capítulo: `cap NNN: <título>`, com o `ROADMAP.md` atualizado no mesmo commit.

## Licença

Texto sob CC BY-SA 4.0. Código de exemplo sob MIT.
