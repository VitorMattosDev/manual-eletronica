# FIGURAS.md — Manual de Eletrônica

## Regra zero

A extensão `_extensions/danmackinlay/tikz/` é **patchada localmente**. Nunca rodar
`quarto add danmackinlay/tikz` nem `quarto update` nela: baixa o upstream sem os
patches e quebra a renderização de todas as figuras do livro.

Se o diretório estiver vazio, copie de um manual existente da série
(ou do `figuras-tikz-kit.zip`) **antes** de qualquer render.

## Ajuste do preâmbulo (específico deste manual)

No template da extensão, acrescentar — **depois** da linha que carrega `pgfplots`:

```latex
\usepackage{circuitikz}
\usepackage{tikz-timing}
\usetikzlibrary{circuits.logic.US}
```

A ordem importa: `circuitikz` depois de `pgfplots`. E lembrar que o template
**sempre** carrega `pgfplots`, mesmo para uma seta simples — não redefinir.

**Feito** (extensão copiada do manual de Python e patchada em 20/08/2026). Além
dos três `\usepackage`, o template ganhou:

```latex
\ctikzset{logic ports=ieee, resistors/scale=0.8, capacitors/scale=0.8}
\tikzset{
  logica/.style={
    circuit logic US,
    circuit symbol unit=13pt,
    circuit symbol size=width 2 height 2,
    every circuit symbol/.style={thick, draw=black, fill=white},
    thick,
  },
}
```

O estilo `logica` existe porque as portas de `circuits.logic.US` saem minúsculas
no tamanho padrão (uma AND + NOT dava 23 pt de altura, ilegível). Usar sempre
`\begin{tikzpicture}[logica]` em diagrama de portas — nunca redefinir tamanho de
porta capítulo a capítulo.

## Ferramenta por tipo de figura

| Tipo de figura | Ferramenta | Volumes típicos |
|---|---|---|
| Esquemático de circuito | `circuitikz` | 1–14 |
| Forma de onda, cronograma digital | `tikz-timing` | 7, 15, 16 |
| Porta lógica, diagrama de blocos digital | `circuits.logic.US` | 15, 16 |
| Curva característica, Bode, resposta no tempo | `pgfplots` | 4–11 |
| Diagrama conceitual, fluxo, mapa mental | TikZ puro | todos |
| Componente real, encapsulamento, instrumento, solda | **foto** (`.png`/`.jpg`) | 1, 14 |

## Sintaxe padrão

```
::: {#fig-divisor}

```{.tikz}
%%| filename: divisor-tensao
%%| alt: Divisor de tensão com dois resistores em série alimentado por fonte CC

\begin{circuitikz}
  \draw (0,0) to[V=$V_\mathrm{in}$] (0,3)
              to[R=$R_1$] (3,3)
              to[R=$R_2$, v=$V_\mathrm{out}$] (3,0) -- (0,0);
\end{circuitikz}
```

Divisor de tensão com dois resistores em série.

:::
```

Referência no texto: `@fig-divisor`.

## Estilos e cores do template

Usar direto, nunca redefinir: `curva`, `destaque`, `auxiliar`, `eixo`, `ponto`,
`vetor`; `manualblue`, `manualred`, `manualgreen`, `manualyellow`, `manualgray`.

## Valores nas figuras

Todo valor de componente desenhado é **valor comercial real** (E12/E24 para
resistores, E6/E12 para capacitores). Nada de 3,7 kΩ ou 137 nF. Vírgula decimal
e unidade literal: `4,7 kΩ`, nunca `\SI{4.7}{\kilo\ohm}` — `siunitx` está
instalado só como dependência do `circuitikz` e **não é usado** no corpo do livro.

## Armadilhas de sintaxe já pagas

- **`=` dentro de rótulo do `circuitikz`** quebra o `pgfkeys`: `l=$R = 470\,\Omega$`
  vira duas chaves e estoura com erro de `$`. Chavear sempre:
  `l={$R = 470\,\Omega$}`.
- **Rótulo e tensão no mesmo lado se sobrepõem.** Em componente horizontal, `l=`
  fica em cima e `v_>=` embaixo; em componente vertical, `l_=` de um lado e
  `v^>=` do outro. Testar visualmente, não supor.
- **Polaridade da pilha:** `(0,0) to[battery1] (0,3)` põe o **positivo em cima**
  (placa longa no fim do caminho). Já `to[V=...]` de baixo para cima põe o `+`
  **embaixo**. Convenções diferentes no mesmo pacote.
- **`pgfmath` estoura acima de ~16384.** Exponencial de diodo escrita ao natural
  passa de $10^{7}$ e derruba o `pgfplots` — que ainda assim emite um SVG
  quebrado. Ancorar a exponencial no valor máximo:
  `{50*exp((x-0.75)/0.0435)}` em vez de `{1e-6*(exp(x/0.02585)-1)*1000}`.
- **Nada de heredoc do Bash para escrever figura.** O heredoc converte `\\` em
  `\` em silêncio. Usar a ferramenta Write ou script Python em arquivo.

## Smoke test obrigatório

Antes de escrever o capítulo 001, renderizar **uma figura de cada uma das quatro
primeiras categorias** da tabela acima e confirmar os quatro SVGs no `_book`.
São quatro caminhos de renderização distintos: testar só um TikZ genérico deixa
passar a falha que só aparece no Volume 15, com noventa capítulos escritos.

**Feito em 20/08/2026** — os quatro caminhos estão confirmados. O arquivo do teste
ficou guardado em `figuras/smoke-test.qmd` (não faz parte do livro; não está
listado no `_quarto.yml`). Reaproveitar sempre que a toolchain mudar: nova versão
de Quarto, de TeX Live, ou troca de máquina.

## Verificação visual (obrigatória em capítulo com figura)

```
python figuras/verificar-figuras.py capitulos/NNN-....qmd
```

Extrai os blocos `{.tikz}` do capítulo, compila com o **mesmo** preâmbulo da
extensão e rasteriza tudo num PNG para conferência a olho.

Isso não é luxo: contar `<svg>` no `_book` prova que a figura **saiu**, nunca que
ela está **certa**. Rótulo sobreposto, seta invertida, polaridade trocada e curva
estourando o eixo passam ilesos por toda a validação textual do checklist. No
capítulo 001 essa verificação pegou `$R$` colidindo com `$V_R$` e `LED` colidindo
com `$V_\mathrm{LED}$` — duas figuras que o `quarto render` aceitou sem uma única
advertência.

## Armadilha de PATH (a falha mais comum)

`quarto install tinytex` **não** adiciona o bin do TinyTeX ao PATH da sessão.
Sintoma: a figura falha em silêncio e `tikz.lua` erra com `imgdata nil` por volta
da linha 587.

- Windows: `$HOME/AppData/Roaming/TinyTeX/bin/windows`
- Linux/macOS: `~/.TinyTeX/bin/<plataforma>`

Prefixar o PATH antes de qualquer `render` ou `preview`.

---

## Fila de fotos pendentes

Acumular aqui, por capítulo, toda figura que dependa de fotografia. Não improvisar
desenho ruim em TikZ para conteúdo fotográfico.

| Cap | Foto necessária | Status |
|---|---|---|
| 004 | Multímetro com as escalas em destaque | pendente |
| 005 | Protoboard: trilhas internas e montagem limpa × montagem confusa | pendente |
| 006 | Cartela de resistores, capacitores e indutores reais por encapsulamento | pendente |
| 083 | Junta de solda boa × fria × com excesso | pendente |
| 085 | Componentes SMD nos encapsulamentos comuns (0805, SOT-23, QFN) | pendente |
