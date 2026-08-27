# ROADMAP — Manual de Eletrônica

Fila autoritativa de capítulos. Status: `[ ]` pendente, `[~]` em andamento, `[x]` concluído.

Regra: **fatia vertical** — completar todos os capítulos de um volume antes de abrir o próximo; completar uma fase antes da seguinte.

Commit por capítulo: `cap NNN: <título>`, com o status abaixo atualizado **no mesmo commit**.

---

## Estado da fila

| | |
|---|---|
| **Progresso** | 77/104 |
| **Contíguos até** | **077** — sem nenhum buraco no meio do livro |
| **Lacunas abertas** | **nenhuma** |
| **Próximo capítulo: 078** | Sensores: resistivos, capacitivos e ativos (abre o Volume 13 e a Fase 4) |

Fases 1 e 2 completas (Volumes 1 a 7, capítulos 001 a 045) e **Volume 8 completo**
(capítulos 046 a 051): semicondutores, diodo, retificadores, filtro capacitivo, Zener e
diodos especiais.

**Volume 9 completo** (capítulos 052 a 058, transistores bipolares): estrutura e $\beta$ (052);
curvas características, efeito Early, reta de carga e SOA (053); o BJT como chave, $\beta$
forçado, diodo de retorno, tempos de comutação, lado alto com PNP e Darlington (054);
polarização por divisor com resistor de emissor, fórmula exata com Thévenin e estabilidade
térmica (055); emissor comum, transcondutância, impedâncias, distorção, degeneração e efeito
Miller (056); seguidor de emissor, base comum e cascode (057); modelo híbrido-$\pi$, regras de
reflexão, parâmetros $h$ e modelo em alta frequência (058).

**Volume 10 completo** (capítulos 059 a 064, MOSFETs e amplificação): princípio de
funcionamento do JFET e do MOSFET, modo depleção e modo enriquecimento, diodo de corpo,
leitura dos símbolos, a porta como capacitor e a dispersão de $V_{th}$ (059); região ôhmica e
região de saturação, a armadilha de vocabulário em relação ao bipolar, $R_{DS(on)}$, lei
quadrática e seu limite honesto em potência, extração por $\sqrt{I_D}$, $g_m \propto \sqrt{I_D}$
e o modelo de pequenos sinais sem $r_\pi$ (060); as três perdas de uma chave, cadeia térmica,
conversão entre $C_{iss}$/$C_{oss}$/$C_{rss}$, patamar de Miller, carga de porta e o
compromisso $R_{DS(on)} \times Q_G$ (061); a janela de tempo de transição, resistor de porta
assimétrico, acionamento espúrio por $dv/dt$, totem-pole e driver dedicado, bootstrap de lado
alto e tempo morto (062); ângulo de condução, as classes A, B, AB, C e D, distorção de
cruzamento, multiplicador de $V_{BE}$ com acoplamento térmico e a dissipação máxima em 40 % da
potência de saída (063); realimentação negativa como assunto próprio — $A_f = A/(1+A\beta)$, o
ganho de malha $T$, produto ganho-banda constante, as quatro topologias, margem de fase e de
ganho, compensação por polo dominante e a relação entre margem de fase e sobrelevação (064).

**Volume 11 completo** (capítulos 065 a 071, amplificadores operacionais): o dispositivo,
os cinco terminais e o encapsulamento DIP-8, o modelo ideal confrontado com TL072 e LM358, as
duas regras de ouro derivadas de $A_f = A/(1+A\beta)$ com $T \to \infty$ e — o ponto em que o
capítulo insiste — as **três condições** sob as quais elas valem (há realimentação negativa, a
saída não saturou, sobra ganho de malha); curto virtual e terra virtual; $A_{OL}$ como curva e
não como número; o seguidor de tensão; e a distinção entre faixa de modo comum de entrada e
excursão de saída (065); as duas topologias resolvidas com o mesmo procedimento de três linhas,
$A_v = 1 + R_2/R_1$ e $A_v = -R_2/R_1$, a escolha entre elas decidida por impedância de entrada
($Z_{in} = R_1$ exatamente no inversor) e por tensão de modo comum (nula no inversor, o que o
torna a topologia de baixa distorção), **ganho de ruído** $A_R = 1/\beta$ igual nas duas e
responsável pela banda, compensação de corrente de polarização só para entrada bipolar, projeto
completo com tolerância nos dois extremos e amplificador de alimentação simples com ganho
unitário em CC e acoplamentos escalonados (066); o somador inversor com pesos independentes e
o ganho de ruído contando o paralelo de todas as entradas, deslocamento de nível para conversor
A/D, o subtrator com suas duas falhas quantificadas ($Z_{in}$ baixa e desigual; CMRR
$\approx (1+R_2/R_1)/4t$, só 34 dB com 1 %), e o amplificador de instrumentação de três amp-ops
corrigindo as duas — primeiro estágio com ganho $1+2R/R_G$ para a diferença e ganho 1 para o
modo comum —, com a cadeia completa da ponte de Wheatstone, o papel do terminal REF e o caminho
de retorno da corrente de polarização (067); integrador e derivador com as duas correções
obrigatórias ($R_f$ em paralelo com $C$; $R_s$ em série com $C$) e a **regra geométrica da
estabilidade** — taxa de fechamento de 20 dB/déc entre $A_{OL}$ e o ganho de ruído é estável,
40 dB/déc oscila —, mais as três topologias de fonte de corrente controlada por tensão, a
tensão de conformidade e o projeto do laço de 4 a 20 mA com a série E96 (068); o interior do
amp-op dando endereço físico a cada imperfeição, o orçamento de erro em CC dominado por
$V_{OS}$, as **duas** limitações de frequência como coisas independentes — GBW de sinal pequeno
e taxa de subida $SR = I_{cauda}/C_c$ de sinal grande, com $f_{PP} = SR/2\pi V_p$ e o teste de
bancada que as separa —, recuperação de sobrecarga, ruído como densidade espectral com canto
$1/f$ e a comparação obrigatória com o ruído térmico da fonte (069); o comparador como ponte
para o digital, a trepidação de um limiar único diante de sinal lento ou ruidoso, o gatilho de
Schmitt nas duas topologias com os limiares deduzidos a partir dos níveis **reais** de saída, a
histerese como memória de um bit (o mesmo mecanismo do latch SR da Fase 5), comparadores
dedicados com saída em coletor aberto, *wired-AND* e atraso dependente do excesso, e o projeto
completo de um termostato com NTC e LM393 (070); e o fechamento, com o filtro de Sallen-Key em
que **o ganho ajusta o $Q$** ($Q = 1/(3-K)$, e $K=3$ é a fronteira entre filtro e oscilador), o
oscilador de relaxação cujo período $T = 2RC\ln[(1+\beta)/(1-\beta)]$ independe da alimentação,
o 555 por dentro (dois comparadores, báscula RS, transistor de descarga) com astável e
monoestável, e o oscilador de Wien com a exigência de ganho **exatamente 3** e os três
mecanismos de controle automático de amplitude (071).

**Volume 12 completo** (capítulos 072 a 077, fontes e gestão de energia): acoplamento
magnético, indutância mútua $M$ e coeficiente $k = M/\sqrt{L_1L_2}$, com a dispersão
$L_d = (1-k)L$ em série e não transformada; as três relações do transformador ideal e a
reflexão de impedância $Z_{in} = n^2 Z_L$; o modelo real de sete elementos com endereço físico
para cada um e o orçamento de perdas de um 6 VA (80 % de rendimento, meio watt a vazio); a lei
de Faraday na forma de projeto $V_{rms} = 4{,}44\,f\,N\,A_e\,B_{max}$, o joelho de saturação e a
leitura ao contrário que sustenta a fonte chaveada (dobrar $f$ permite metade do núcleo);
regulação como resistência interna em porcentagem, a armadilha do "12 V" que mede 14 V a vazio
e 19,9 V de pico, e por que a etiqueta traz VA e não W (072); a fonte linear completa montada
com números que fecham, o **procedimento de projeto em oito passos que corre da carga para a
rede**, os **dois piores casos opostos e ambos obrigatórios** (rede baixa com carga máxima
aperta o vale e decide $C$; rede alta sem carga aperta a tensão de trabalho e decide o
capacitor de 35 V), a verificação **no vale e nunca na média**, a queda real de 1,0 V por diodo
sob pulsos, o dimensionamento do transformador pela corrente **eficaz** ($I_{rms} \approx
1{,}8\,I_{cc}$), o regulador série discreto que é o não inversor do 066 com um seguidor de
emissor dentro da malha e a referência alimentada pela **saída já regulada**, a limitação de
corrente $I_{lim} = 0{,}6/R_{sc}$ e o alerta sobre limitação a corrente constante, e o calor
como definição da topologia: $P = (V_{in}-V_{out})I$, pior caso térmico oposto ao de tensão, e
46 % de rendimento na fonte inteira (073); o interior do encapsulamento de três pernas com as
três proteções que o discreto não tem (limitação de corrente, SOA, desligamento térmico) e o
alerta de que as duas últimas se manifestam como "defeito"; a **referência bandgap** somando
$V_{BE}$ (coeficiente negativo) com $K V_T \ln n$ (proporcional a $T$) para dar 1,25 V plano, e
por que 1,25 V é um número melhor que os 5,6 V do Zener; o LM317 flutuante com
$V_{out} = 1{,}25(1+R_2/R_1) + I_{ADJ}R_2$, o porquê de $R_1 = 240\ \Omega$ (corrente mínima de
carga resolvida pelo próprio divisor), os diodos $D_1$ e $D_2$, e o mesmo componente como fonte
de corrente $1{,}25/R$; **série e LDO como topologias diferentes** — seguidor de emissor contra
emissor comum — com a **janela de ESR** do capacitor de saída como componente do laço de
controle; a queda da rejeição de ondulação com a frequência (60 dB em 120 Hz, 20 dB em 1 MHz), e
o dimensionamento térmico como o menor de três limites, com os dois erros de arredondamento que
o arruínam (074); a chave mais o indutor no lugar do elemento de passagem linear, com a corrente
de entrada **menor** que a de saída como assinatura da topologia; o **balanço de tensão-segundo**
($\int_0^T v_L\,dt = 0$ em regime) resolvendo as três razões de conversão em duas linhas cada, e
o balanço de carga gêmeo dando $\bar{i_L} = I_{out}$ no buck e $I_{out}/(1-D)$ no boost; qual
lado tem corrente pulsada em cada topologia e o que isso decide; o buck síncrono e o
*shoot-through*; o projeto do indutor por escolha de ondulação (30 % da média) e pela corrente de
**pico**, com $I_{sat}$ 30 a 50 % acima; a ondulação de saída em duas parcelas com a **ESR
dominando** (5,4 mV com cerâmico contra 97 mV com eletrolítico de mesma capacitância); modo
descontínuo como comportamento normal em carga leve; o laço de controle precisando de compensação
porque o filtro $LC$ dá 180° de atraso, e o modo corrente como alternativa de primeira ordem; e o
**laço de comutação** — área $\times\ di/dt$ virando sobretensão real no dreno, com as quatro
regras de layout (075); a bateria como o que **não** é fonte de tensão, com o modelo de três
elementos ($V_{oc}(SoC)$, $R_\Omega$, $R_p \parallel C_p$) e o **ensaio de pulso** que o levanta
com resistor, cronômetro e voltímetro; por que medir tensão sem carga informa quase nada; o que
mAh quer dizer e não quer (depende da corrente e do corte, e não é energia — Wh é), e o C-rate; as
cinco químicas com o formato da curva decidindo se dá para estimar carga pela tensão (LiFePO₄ tem
platô plano demais); o perfil **CC-CV** com pré-carga, os 4,2 V exigindo 1 % de precisão, o
carregar abaixo de 0 °C depositando lítio metálico com a tensão certa, e os critérios alternativos
das outras químicas ($-\Delta V$ em NiMH, flutuação em chumbo-ácido); a proteção de célula única
com **dois** MOSFETs por causa do diodo de corpo; balanceamento em série e o cuidado com paralelo;
e o orçamento de energia em seis passos, com autodescarga como a maior parcela isolada (076); e o
fechamento, com **o terra que não é um nó** (100 nH de trilha e $L\,di/dt$ dando 1 V entre dois
pontos do mesmo terra), a corrente de retorno escolhendo o caminho de **menor indutância** acima
de ~100 kHz — logo abaixo da trilha de ida, porque minimiza a **área do laço** —, as três
topologias de retorno (cadeia errada, estrela abaixo de ~1 MHz, plano contínuo acima) e o
abandono da prática de cortar o plano entre analógico e digital; a malha de terra e as três
soluções (isolar, diferencial, blindagem num extremo só); **desacoplamento como impedância contra
frequência**, com todo capacitor real sendo um V (capacitivo abaixo da ressonância própria,
indutivo acima), a indutância de encapsulamento e de trilha limitando tudo, e a
**antirressonância** que condena a escada clássica de valores em favor de vários 100 nF iguais; e
as quatro proteções de fronteira — PTC, MOSFET de canal P contra inversão (15 mV contra 500 mV),
TVS/MOV em cascata, e diodo de retorno (077).

A ponte que o capítulo 071 montara está fechada: o desacoplamento, invocado dezenas de vezes como
regra de bancada ao longo do manual, ganhou explicação própria no capítulo 077.

O próximo bloco é o **Volume 13** (capítulos 078 a 082), que abre a **Fase 4** e muda o objeto:
em vez de produzir energia, medir o mundo. A pergunta que organiza o volume é a do capítulo 078 —
entre a grandeza física e o número que o programa lê, quantas transformações existem e onde cada
uma introduz erro. Os blocos já estão prontos: amplificador de instrumentação (067), orçamento de
ruído (069) e o terra da ponte de Wheatstone (077).

Convenções que o Volume 11 herda: valor comercial recalculado depois do arredondamento, pior
caso verificado nos dois extremos, `.tikz` com `circuitikz` para esquemático e `pgfplots` para
curva, **parâmetro de dispositivo entra em projeto só como desigualdade**, e a notação $\beta$
para a fração realimentada estabelecida no capítulo 064 (que não é o $\beta$ do bipolar).

Para confirmar o estado a qualquer momento:

```
python ferramentas/verificar-lacunas.py
```

O histórico de como as lacunas apareceram — sessões que terminaram no meio de um volume e
a sessão seguinte reancorando na fronteira do **volume** em vez do próximo capítulo
pendente — está na lição 11 do `LICOES-MANUAIS.md`, e a trava contra a repetição é o
verificador acima, rodado na abertura de cada sessão.

**Pendência encerrada:** os capítulos 033 e 035 apontavam com `@sec-` para a 065, 069 e 070,
que eram conteúdo futuro. Com o Volume 11 escrito, as cinco referências passaram a resolver
para conteúdo real e o verificador não as lista mais.


## Fase 1 — Fundamentos Elétricos


### Volume 1 — A Bancada e o Método

- [x] 001 — O que é eletrônica e o que este manual cobre — `capitulos/001-o-que-e-eletronica-e-o-que-este-manual-cobre.qmd`
- [x] 002 — Segurança elétrica: choque, arco, capacitores carregados e a rede — `capitulos/002-seguranca-eletrica-choque-arco-capacitores.qmd`
- [x] 003 — Grandezas, unidades e ordens de grandeza — `capitulos/003-grandezas-unidades-e-ordens-de-grandeza.qmd`
- [x] 004 — O multímetro: tensão, corrente, resistência e continuidade — `capitulos/004-o-multimetro-tensao-corrente-resistencia-e.qmd`
- [x] 005 — A protoboard, a fonte de bancada e a montagem limpa — `capitulos/005-a-protoboard-a-fonte-de-bancada-e-a-montagem-limpa.qmd`
- [x] 006 — Componentes passivos: identificação, código de cores e tolerância — `capitulos/006-componentes-passivos-identificacao-codigo-de-cores.qmd`
- [x] 007 — Esquemáticos: como ler, como desenhar, como não se perder — `capitulos/007-esquematicos-como-ler-como-desenhar-como-nao-se.qmd`


### Volume 2 — Corrente Contínua: Leis Fundamentais

- [x] 008 — Carga, corrente e o modelo de condução — `capitulos/008-carga-corrente-e-o-modelo-de-conducao.qmd`
- [x] 009 — Tensão, potencial e referência (terra) — `capitulos/009-tensao-potencial-e-referencia-terra.qmd`
- [x] 010 — Resistência, resistividade e a Lei de Ohm — `capitulos/010-resistencia-resistividade-e-a-lei-de-ohm.qmd`
- [x] 011 — Potência, energia e dissipação térmica — `capitulos/011-potencia-energia-e-dissipacao-termica.qmd`
- [x] 012 — Associação série e paralelo — `capitulos/012-associacao-serie-e-paralelo.qmd`
- [x] 013 — As Leis de Kirchhoff — `capitulos/013-as-leis-de-kirchhoff.qmd`
- [x] 014 — Divisores de tensão e de corrente — `capitulos/014-divisores-de-tensao-e-de-corrente.qmd`


### Volume 3 — Análise de Circuitos

- [x] 015 — Análise nodal — `capitulos/015-analise-nodal.qmd`
- [x] 016 — Análise de malhas — `capitulos/016-analise-de-malhas.qmd`
- [x] 017 — Superposição e linearidade — `capitulos/017-superposicao-e-linearidade.qmd`
- [x] 018 — Teoremas de Thévenin e Norton — `capitulos/018-teoremas-de-thevenin-e-norton.qmd`
- [x] 019 — Máxima transferência de potência e casamento — `capitulos/019-maxima-transferencia-de-potencia-e-casamento.qmd`
- [x] 020 — Fontes reais, resistência interna e carregamento do circuito — `capitulos/020-fontes-reais-resistencia-interna-e-carregamento-do.qmd`


### Volume 4 — Capacitores, Indutores e Transitórios

- [x] 021 — Campo elétrico e capacitância — `capitulos/021-campo-eletrico-e-capacitancia.qmd`
- [x] 022 — O capacitor real: tipos, ESR e tensão de trabalho — `capitulos/022-o-capacitor-real-tipos-esr-e-tensao-de-trabalho.qmd`
- [x] 023 — Campo magnético e indutância — `capitulos/023-campo-magnetico-e-indutancia.qmd`
- [x] 024 — O indutor real e a energia armazenada — `capitulos/024-o-indutor-real-e-a-energia-armazenada.qmd`
- [x] 025 — Transitórios RC: carga, descarga e constante de tempo — `capitulos/025-transitorios-rc-carga-descarga-e-constante-de-tempo.qmd`
- [x] 026 — Transitórios RL e circuitos RLC no domínio do tempo — `capitulos/026-transitorios-rl-e-circuitos-rlc-no-dominio-do-tempo.qmd`


## Fase 2 — Corrente Alternada e Sinais


### Volume 5 — Fundamentos de Corrente Alternada

- [x] 027 — Do CC ao CA: a senoide e seus parâmetros — `capitulos/027-do-cc-ao-ca-a-senoide-e-seus-parametros.qmd`
- [x] 028 — Valor médio, valor eficaz (RMS) e o que o multímetro realmente mede — `capitulos/028-valor-medio-valor-eficaz-rms-e-o-que-o-multimetro.qmd`
- [x] 029 — Fasores e números complexos aplicados — `capitulos/029-fasores-e-numeros-complexos-aplicados.qmd`
- [x] 030 — Reatância e impedância — `capitulos/030-reatancia-e-impedancia.qmd`
- [x] 031 — Potência ativa, reativa e aparente — `capitulos/031-potencia-ativa-reativa-e-aparente.qmd`
- [x] 032 — Fator de potência e correção — `capitulos/032-fator-de-potencia-e-correcao.qmd`


### Volume 6 — Filtros e Resposta em Frequência

- [x] 033 — Filtro RC passa-baixas e frequência de corte — `capitulos/033-filtro-rc-passa-baixas-e-frequencia-de-corte.qmd`
- [x] 034 — Filtro RC passa-altas e acoplamento — `capitulos/034-filtro-rc-passa-altas-e-acoplamento.qmd`
- [x] 035 — Diagramas de Bode: ganho e fase — `capitulos/035-diagramas-de-bode-ganho-e-fase.qmd`
- [x] 036 — Filtros LC e ordem do filtro — `capitulos/036-filtros-lc-e-ordem-do-filtro.qmd`
- [x] 037 — Ressonância série e paralela — `capitulos/037-ressonancia-serie-e-paralela.qmd`
- [x] 038 — Fator de qualidade, largura de banda e seletividade — `capitulos/038-fator-de-qualidade-largura-de-banda-e-seletividade.qmd`


### Volume 7 — Sinais, Ruído e Instrumentação

- [x] 039 — Sinais periódicos, forma de onda e ciclo de trabalho — `capitulos/039-sinais-periodicos-forma-de-onda-e-ciclo-de-trabalho.qmd`
- [x] 040 — Fourier na prática: harmônicos e largura de banda — `capitulos/040-fourier-na-pratica-harmonicos-e-largura-de-banda.qmd`
- [x] 041 — O decibel e as escalas logarítmicas — `capitulos/041-o-decibel-e-as-escalas-logaritmicas.qmd`
- [x] 042 — Ruído: térmico, de disparo e interferência externa — `capitulos/042-ruido-termico-de-disparo-e-interferencia-externa.qmd`
- [x] 043 — O osciloscópio: base de tempo, ganho vertical e gatilho — `capitulos/043-o-osciloscopio-base-de-tempo-ganho-vertical-e.qmd`
- [x] 044 — Pontas de prova, compensação e artefatos de medição — `capitulos/044-pontas-de-prova-compensacao-e-artefatos-de-medicao.qmd`
- [x] 045 — Gerador de funções e ensaio de resposta em frequência — `capitulos/045-gerador-de-funcoes-e-ensaio-de-resposta-em.qmd`


## Fase 3 — Semicondutores e Eletrônica Analógica


### Volume 8 — Diodos e Aplicações

- [x] 046 — Semicondutores, dopagem e a junção PN — `capitulos/046-semicondutores-dopagem-e-a-juncao-pn.qmd`
- [x] 047 — O diodo real: curva, queda direta e modelos — `capitulos/047-o-diodo-real-curva-queda-direta-e-modelos.qmd`
- [x] 048 — Retificadores de meia onda e de onda completa — `capitulos/048-retificadores-de-meia-onda-e-de-onda-completa.qmd`
- [x] 049 — Filtragem capacitiva e ondulação — `capitulos/049-filtragem-capacitiva-e-ondulacao.qmd`
- [x] 050 — Diodo Zener e regulação por referência — `capitulos/050-diodo-zener-e-regulacao-por-referencia.qmd`
- [x] 051 — LEDs, fotodiodos e diodos especiais: Schottky, TVS e varicap — `capitulos/051-leds-fotodiodos-e-diodos-especiais-schottky-tvs-e.qmd`


### Volume 9 — Transistores Bipolares

- [x] 052 — O transistor bipolar: estrutura e funcionamento — `capitulos/052-o-transistor-bipolar-estrutura-e-funcionamento.qmd`
- [x] 053 — Curvas características e regiões de operação — `capitulos/053-curvas-caracteristicas-e-regioes-de-operacao.qmd`
- [x] 054 — O BJT como chave: corte, saturação e acionamento de cargas — `capitulos/054-o-bjt-como-chave-corte-saturacao-e-acionamento-de.qmd`
- [x] 055 — Polarização: divisor de base, resistor de emissor e estabilidade térmica — `capitulos/055-polarizacao-divisor-de-base-resistor-de-emissor-e.qmd`
- [x] 056 — Emissor comum: ganho, impedâncias e limitações — `capitulos/056-emissor-comum-ganho-impedancias-e-limitacoes.qmd`
- [x] 057 — Coletor comum e base comum — `capitulos/057-coletor-comum-e-base-comum.qmd`
- [x] 058 — Modelo de pequenos sinais e análise em CA — `capitulos/058-modelo-de-pequenos-sinais-e-analise-em-ca.qmd`


### Volume 10 — MOSFETs e Amplificação

- [x] 059 — JFET e MOSFET: princípio de funcionamento — `capitulos/059-jfet-e-mosfet-principio-de-funcionamento.qmd`
- [x] 060 — Curvas, região ôhmica e região de saturação — `capitulos/060-curvas-regiao-ohmica-e-regiao-de-saturacao.qmd`
- [x] 061 — O MOSFET como chave de potência: RDS(on), efeito Miller e dissipação — `capitulos/061-o-mosfet-como-chave-de-potencia-rds-on-efeito.qmd`
- [x] 062 — Drivers de gate e a comutação real — `capitulos/062-drivers-de-gate-e-a-comutacao-real.qmd`
- [x] 063 — Classes de amplificador: A, B, AB, C e D — `capitulos/063-classes-de-amplificador-a-b-ab-c-e-d.qmd`
- [x] 064 — Realimentação negativa: ganho, distorção e estabilidade — `capitulos/064-realimentacao-negativa-ganho-distorcao-e.qmd`


### Volume 11 — Amplificadores Operacionais

- [x] 065 — O amp-op ideal e as regras de ouro — `capitulos/065-o-amp-op-ideal-e-as-regras-de-ouro.qmd`
- [x] 066 — Amplificador inversor e não inversor — `capitulos/066-amplificador-inversor-e-nao-inversor.qmd`
- [x] 067 — Somador, subtrator e amplificador de instrumentação — `capitulos/067-somador-subtrator-e-amplificador-de-instrumentacao.qmd`
- [x] 068 — Integrador, derivador e fontes de corrente — `capitulos/068-integrador-derivador-e-fontes-de-corrente.qmd`
- [x] 069 — O amp-op real: offset, slew rate, produto ganho-banda e saturação — `capitulos/069-o-amp-op-real-offset-slew-rate-produto-ganho-banda.qmd`
- [x] 070 — Comparadores, histerese e o gatilho de Schmitt — `capitulos/070-comparadores-histerese-e-o-gatilho-de-schmitt.qmd`
- [x] 071 — Filtros ativos e osciladores: Wien, relaxação e o 555 — `capitulos/071-filtros-ativos-e-osciladores-wien-relaxacao-e-o-555.qmd`


## Fase 4 — Energia, Interface e Construção


### Volume 12 — Fontes e Gestão de Energia

- [x] 072 — Transformadores e acoplamento magnético — `capitulos/072-transformadores-e-acoplamento-magnetico.qmd`
- [x] 073 — Fontes lineares: do transformador ao regulador — `capitulos/073-fontes-lineares-do-transformador-ao-regulador.qmd`
- [x] 074 — Reguladores integrados: série, LDO e dissipação térmica — `capitulos/074-reguladores-integrados-serie-ldo-e-dissipacao.qmd`
- [x] 075 — Fontes chaveadas: buck, boost e buck-boost — `capitulos/075-fontes-chaveadas-buck-boost-e-buck-boost.qmd`
- [x] 076 — Baterias, células e circuitos de carga — `capitulos/076-baterias-celulas-e-circuitos-de-carga.qmd`
- [x] 077 — Aterramento, malhas de terra, desacoplamento e proteção — `capitulos/077-aterramento-malhas-de-terra-desacoplamento-e.qmd`


### Volume 13 — Interface com o Mundo Físico

- [ ] 078 — Sensores: resistivos, capacitivos e ativos — `capitulos/078-sensores-resistivos-capacitivos-e-ativos.qmd`
- [ ] 079 — Condicionamento de sinal e a cadeia de medição — `capitulos/079-condicionamento-de-sinal-e-a-cadeia-de-medicao.qmd`
- [ ] 080 — Conversão analógico-digital: amostragem, quantização e aliasing — `capitulos/080-conversao-analogico-digital-amostragem-quantizacao.qmd`
- [ ] 081 — Conversão digital-analógica e PWM — `capitulos/081-conversao-digital-analogica-e-pwm.qmd`
- [ ] 082 — Atuadores: relés, solenoides e motores CC — `capitulos/082-atuadores-reles-solenoides-e-motores-cc.qmd`


### Volume 14 — Da Bancada ao Circuito Real

- [ ] 083 — Soldagem: técnica, ferramentas e retrabalho — `capitulos/083-soldagem-tecnica-ferramentas-e-retrabalho.qmd`
- [ ] 084 — Do esquemático ao layout de PCB — `capitulos/084-do-esquematico-ao-layout-de-pcb.qmd`
- [ ] 085 — Fabricação, montagem e componentes SMD — `capitulos/085-fabricacao-montagem-e-componentes-smd.qmd`
- [ ] 086 — Integridade de sinal, EMI e compatibilidade eletromagnética — `capitulos/086-integridade-de-sinal-emi-e-compatibilidade.qmd`
- [ ] 087 — Depuração de placa: método, medição e falhas típicas — `capitulos/087-depuracao-de-placa-metodo-medicao-e-falhas-tipicas.qmd`


## Fase 5 — Eletrônica Digital


### Volume 15 — Lógica Digital: da Chave à Porta

- [ ] 088 — Do analógico ao digital: níveis, margens de ruído e o sinal binário — `capitulos/088-do-analogico-ao-digital-niveis-margens-de-ruido-e-o.qmd`
- [ ] 089 — Sistemas de numeração e representação binária — `capitulos/089-sistemas-de-numeracao-e-representacao-binaria.qmd`
- [ ] 090 — Álgebra booleana e as portas fundamentais — `capitulos/090-algebra-booleana-e-as-portas-fundamentais.qmd`
- [ ] 091 — Portas com diodos, portas com transistores e a família TTL — `capitulos/091-portas-com-diodos-portas-com-transistores-e-a.qmd`
- [ ] 092 — A família CMOS: funcionamento, consumo e interface entre famílias — `capitulos/092-a-familia-cmos-funcionamento-consumo-e-interface.qmd`
- [ ] 093 — Circuitos combinacionais: multiplexadores, decodificadores e comparadores — `capitulos/093-circuitos-combinacionais-multiplexadores.qmd`
- [ ] 094 — Simplificação: formas canônicas e mapas de Karnaugh — `capitulos/094-simplificacao-formas-canonicas-e-mapas-de-karnaugh.qmd`
- [ ] 095 — Aritmética binária em hardware: somadores e a ULA elementar — `capitulos/095-aritmetica-binaria-em-hardware-somadores-e-a-ula.qmd`


### Volume 16 — Sequencial, Memória e a Ponte para o Computador

- [ ] 096 — Realimentação digital: o latch SR — `capitulos/096-realimentacao-digital-o-latch-sr.qmd`
- [ ] 097 — Flip-flops D e JK e o conceito de borda — `capitulos/097-flip-flops-d-e-jk-e-o-conceito-de-borda.qmd`
- [ ] 098 — O clock, temporização, setup e hold — `capitulos/098-o-clock-temporizacao-setup-e-hold.qmd`
- [ ] 099 — Registradores e deslocadores — `capitulos/099-registradores-e-deslocadores.qmd`
- [ ] 100 — Contadores síncronos e assíncronos — `capitulos/100-contadores-sincronos-e-assincronos.qmd`
- [ ] 101 — Máquinas de estado finito: Moore e Mealy — `capitulos/101-maquinas-de-estado-finito-moore-e-mealy.qmd`
- [ ] 102 — Memórias: célula SRAM, DRAM e não voláteis — `capitulos/102-memorias-celula-sram-dram-e-nao-volateis.qmd`
- [ ] 103 — Lógica programável: CPLD, FPGA e a descrição de hardware — `capitulos/103-logica-programavel-cpld-fpga-e-a-descricao-de.qmd`
- [ ] 104 — Da porta lógica ao processador: a fronteira com a arquitetura — `capitulos/104-da-porta-logica-ao-processador-a-fronteira-com-a.qmd`


---

## Marcos

- [ ] Bootstrap da toolchain (tinytex + PATH + tlmgr incluindo circuitikz e tikz-timing)
- [ ] Extensão `danmackinlay/tikz` copiada com patches locais e preâmbulo ajustado
- [ ] Smoke test das 4 categorias de figura (circuitikz, tikz-timing, circuits.logic.US, pgfplots)
- [ ] Branch `gh-pages` criado
- [ ] Primeiro deploy verde no GitHub Pages
- [ ] Volume 1 completo
- [ ] Fase 1 completa
