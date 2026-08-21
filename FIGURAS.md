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
- **Polaridade da fonte: o `+` fica no INÍCIO do caminho.** Vale para `battery1`
  (placa longa = positivo) e para `V` (o `+` desenhado dentro do círculo). Logo
  `(0,0) to[battery1] (0,3)` põe o **positivo embaixo** e o negativo em cima — o
  contrário do que quase todo mundo supõe ao desenhar o trilho de alimentação
  subindo da referência.

  A correção é `invert`, que troca a polaridade **sem** mexer no lado do rótulo:

  ```latex
  \draw (0,0) to[battery1, invert, l_={$9$ V}] (0,4.4);   % + em cima
  ```

  Alternativa equivalente: desenhar o caminho do `+` para o `−`, isto é, de cima
  para baixo. As duas formas dão o mesmo símbolo; `invert` é preferível porque
  preserva a ordem natural de leitura do `\draw`.

  Esta nota estava **errada** até 21/08/2026 (dizia "positivo em cima") e as 20
  pilhas dos capítulos 001 a 014 foram desenhadas de cabeça para baixo por causa
  dela. Nenhuma validação textual pega isso: o SVG sai, a contagem fecha, o
  `?@` não aparece. Só o PNG do `verificar-figuras.py`, olhado com atenção, pega
  — e ainda assim é preciso saber qual placa é a longa. Quando houver dúvida de
  polaridade, renderize um teste isolado com `to[V]`, que desenha `+` e `−`
  explícitos, e use-o como gabarito.
- **`pgfmath` estoura acima de ~16384.** Exponencial de diodo escrita ao natural
  passa de $10^{7}$ e derruba o `pgfplots` — que ainda assim emite um SVG
  quebrado. Ancorar a exponencial no valor máximo:
  `{50*exp((x-0.75)/0.0435)}` em vez de `{1e-6*(exp(x/0.02585)-1)*1000}`.
- **Nada de heredoc do Bash para escrever figura.** O heredoc converte `\\` em
  `\` em silêncio. Usar a ferramenta Write ou script Python em arquivo. Vale
  também para o *script Python passado por heredoc*: um `str.replace` cujo padrão
  contenha `\\` chega ao Python já corrompido e a substituição falha sem explicar
  por quê. Script com `\\` vai por arquivo, ou usa-se a ferramenta Edit.
- **Nomes de variável de `\foreach` colidem com primitivas do TeX.** `\ht` (altura
  de caixa) e `\lg` (logaritmo) são os piores: não dão erro claro, produzem
  `! You can't use 'the character 0' after \the` seguido de uma chuva de
  `Illegal unit of measure`, e o texto do rótulo sai com lixo do tipo
  `0.54E0.54.54E` no meio. Evitar também `\dim`, `\wd`, `\dp`, `\sf`, `\it`, `\tt`.
  Nomes seguros já usados: `\cmp`, `\esp`, `\dsc`, `\pot`, `\yc`, `\xx`, `\ii`.
- **Vírgula decimal dentro de `xticklabels`/`yticklabels` do `pgfplots` é
  separador de lista.** `yticklabels={0, 1, 2, 3, 4, 4,5}` vira sete rótulos e o
  eixo sai com um `4` no lugar do `4,5`. Chavear cada rótulo:
  `yticklabels={{0},{1},{2},{3},{4},{4,5}}`. Como este livro usa vírgula decimal
  em tudo, a armadilha é permanente.
- **`xmode=log` amostra linearmente.** `domain=0.1:1000, samples=200` põe quase
  todos os pontos na década de cima e desenha a curva como uma poligonal grosseira
  à esquerda. Plotar em forma paramétrica sobre o expoente:
  `\addplot[domain=-1:3, samples=240] ({10^x}, {f(10^x)});`
- **Lado do rótulo em componente vertical do `circuitikz`.** Para um caminho
  desenhado **de cima para baixo**, `l=` cai a **leste** e `l_=` a **oeste**; num
  caminho de baixo para cima é o inverso. Consequência prática: rótulo de fonte
  desenhada para cima com `l_=` vai parar **dentro** da malha, em cima das setas
  de corrente. Conferir sempre no PNG do `verificar-figuras.py`.

- **`\\` dentro de `\node` só funciona com `align=` declarado.** Sem
  `align=left` (ou `center`/`right`), o TikZ **ignora** a quebra e emenda as
  linhas num parágrafo só — sem aviso, sem erro. Aconteceu no capítulo 017, num
  nó de anotação em que todos os vizinhos tinham `align=left` e só aquele não
  tinha. Regra: todo nó com `\\` leva `align=`.

- **Dois `axis` do `pgfplots` lado a lado**, sem a biblioteca `calc`:

  ```latex
  \begin{axis}[name=ax1, ...] ... \end{axis}
  \begin{axis}[at={(ax1.right of south east)}, anchor={left of south west}, ...]
  ```

- **`\addplot` de preenchimento rouba a entrada da legenda.** Um
  `\addplot[draw=none, fill=...] {f(x)} \closedcycle;` posto antes das curvas conta
  como plot e desloca **todas** as `\addlegendentry` em um: a legenda passa a mostrar
  a cor errada em cada rótulo. O sintoma é traiçoeiro porque o gráfico está certo e só
  a legenda mente. Marcar sempre o preenchimento com `forget plot`. Pago no
  capítulo 028 (`028-quadrado`).

- **Acento em modo matemático estoura com `! Please use \mathaccent`.** `V_{\mathrm{méd}}`
  não compila; `V_{|V|_{\text{méd}}}` sim, porque `\text` volta ao modo texto. Vale para
  qualquer subscrito com "média", "máx", "mín", "núcleo". Pago no capítulo 028.

- **`v^>=` e `l=` caem do MESMO lado no `circuitikz`.** O acento circunflexo em `v^`
  não significa "do outro lado do rótulo": significa o lado padrão, que é o mesmo do
  `l=`. Resultado: rótulo do componente em cima do rótulo da tensão. A combinação certa
  é `l=` com `v_>=` (componente horizontal) ou `l=` com `v_>=` (vertical desenhado de
  cima para baixo, que joga a tensão para oeste). Pago no capítulo 029 (`029-soma`).

- **`xlabel` com `axis lines=middle` vai para a ponta do eixo**, não para baixo do
  gráfico, e colide com a curva e com as anotações que estiverem à direita. Em painéis
  empilhados a solução é tirar o `xlabel` do `axis` e pôr um `\node` avulso abaixo do
  último painel. Pago nos capítulos 030 e 031.

- **Não desenhar dados "à mão" em cm dentro de uma `tikzpicture` que contém `axis`.**
  A área útil de um `axis` é menor que o `width=` declarado (rótulos e ticks comem a
  diferença), então qualquer coordenada em centímetros calculada por regra de três
  **não** alinha com os dados. Sintoma: pulsos que deveriam cair no pico da senoide
  ficam alguns graus adiantados, e os trechos entre eles aparecem com falhas. A saída é
  descrever a forma como função e deixá-la no próprio `\addplot`.

- **Pulso estreito sem singularidade.** Para desenhar corrente pulsada (entrada de
  fonte chaveada), a tentação é `cos(x)*abs(cos(x))^30` — que estoura em $x=90°$,
  porque `^` no `pgfmath` é `exp(n*ln(...))` e `ln(0)` não existe. A forma segura é
  `cos(x)*exp(-26*(1-abs(cos(x))))`: mesmo perfil, sem log de zero, e o argumento da
  exponencial fica em $[-26, 0]$. Pago no capítulo 032 (`032-distorcao`).

- **Barra de anotação horizontal atravessa o diagrama.** Marcar "trechos" com linhas
  grossas semitransparentes por cima de um unifilar cobre fiação e símbolos. Levá-las
  para **abaixo** de todo o desenho e rotular cada uma na ponta. Pago no capítulo 032
  (`032-instalacao`).

- **Circuito e gráfico na mesma figura:** `\begin{tikzpicture}` (não
  `circuitikz`) contendo um `\begin{scope}` com o circuito e, ao lado, um
  `\begin{axis}[at={(8.4cm,0cm)}, anchor=south west, ...]`. Dentro do `scope` do
  circuito, `to[R]`, `to[battery1]` etc. continuam funcionando porque o pacote já
  está carregado. Usado nos capítulos 017 e 020.

## Largura das figuras

O PNG de conferência é montado com `varwidth=17cm`: o que passar disso aparece
**cortado no PNG** e sai largo demais na página do livro. Figura de três ou quatro
painéis não cabe numa linha — dispor em **duas linhas de dois** (`xshift` +
`yshift`), como na redução da rede escada do capítulo 012.

Ordem de grandeza medida no Volume 3: **três painéis de circuito com rótulos não
cabem** (o terceiro sumiu em `018-ponte` e o quarto em `018-transformacao`). Dois
painéis de até ~7 cm cada é o teto seguro. O sintoma é discreto — o painel
simplesmente não aparece no PNG, sem erro do LaTeX —, então conte a largura antes:
maior `xshift` + largura do último painel + folga dos rótulos.

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
| 031 | Medidor de consumo de tomada mostrando W, VA e FP da mesma carga | pendente |
| 032 | Capacitor de motor (*motor run*) com a plaqueta legível e o resistor de descarga | pendente |
| 032 | Banco de capacitores automático aberto, com os degraus e os contatores | pendente |
| 083 | Junta de solda boa × fria × com excesso | pendente |
| 085 | Componentes SMD nos encapsulamentos comuns (0805, SOT-23, QFN) | pendente |
