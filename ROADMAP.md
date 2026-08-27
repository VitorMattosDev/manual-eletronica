# ROADMAP — Manual de Eletrônica

Fila autoritativa de capítulos. Status: `[ ]` pendente, `[~]` em andamento, `[x]` concluído.

Regra: **fatia vertical** — completar todos os capítulos de um volume antes de abrir o próximo; completar uma fase antes da seguinte.

Commit por capítulo: `cap NNN: <título>`, com o status abaixo atualizado **no mesmo commit**.

---

## Estado da fila

| | |
|---|---|
| **Progresso** | 61/104 |
| **Contíguos até** | **061** — sem nenhum buraco no meio do livro |
| **Lacunas abertas** | **nenhuma** |
| **Próximo capítulo: 062** | Drivers de gate e a comutação real |

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

**Volume 10 em andamento** (capítulos 059 a 064, MOSFETs e amplificação): princípio de
funcionamento do JFET e do MOSFET, modo depleção e modo enriquecimento, diodo de corpo,
leitura dos símbolos, a porta como capacitor e a dispersão de $V_{th}$ (059); região ôhmica e
região de saturação, a armadilha de vocabulário em relação ao bipolar, $R_{DS(on)}$, lei
quadrática e seu limite honesto em potência, extração por $\sqrt{I_D}$, $g_m \propto \sqrt{I_D}$
e o modelo de pequenos sinais sem $r_\pi$ (060); as tres perdas de uma chave, cadeia termica,
conversao Ciss/Coss/Crss, patamar de Miller, carga de porta e o compromisso RDS(on) x QG (061).

Convenções que o Volume 10 herda: valor comercial recalculado depois do arredondamento, pior
caso verificado nos dois extremos, `.tikz` com `circuitikz` para esquemático e `pgfplots` para
curva, e **parâmetro de dispositivo entra em projeto só como desigualdade**, nunca como fator
numa conta que decide tensão de saída.

Para confirmar o estado a qualquer momento:

```
python ferramentas/verificar-lacunas.py
```

O histórico de como as lacunas apareceram — sessões que terminaram no meio de um volume e
a sessão seguinte reancorando na fronteira do **volume** em vez do próximo capítulo
pendente — está na lição 11 do `LICOES-MANUAIS.md`, e a trava contra a repetição é o
verificador acima, rodado na abertura de cada sessão.

**Pendência separada, de outra natureza:** os capítulos 033 e 035 usam `@sec-` para
apontar a 065, 069 e 070 — conteúdo do Volume 11, ainda não escrito. Isso viola a regra
de referência cruzada do `CLAUDE.md` e deveria ser menção textual. O verificador lista as
cinco ocorrências como aviso.


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
- [ ] 062 — Drivers de gate e a comutação real — `capitulos/062-drivers-de-gate-e-a-comutacao-real.qmd`
- [ ] 063 — Classes de amplificador: A, B, AB, C e D — `capitulos/063-classes-de-amplificador-a-b-ab-c-e-d.qmd`
- [ ] 064 — Realimentação negativa: ganho, distorção e estabilidade — `capitulos/064-realimentacao-negativa-ganho-distorcao-e.qmd`


### Volume 11 — Amplificadores Operacionais

- [ ] 065 — O amp-op ideal e as regras de ouro — `capitulos/065-o-amp-op-ideal-e-as-regras-de-ouro.qmd`
- [ ] 066 — Amplificador inversor e não inversor — `capitulos/066-amplificador-inversor-e-nao-inversor.qmd`
- [ ] 067 — Somador, subtrator e amplificador de instrumentação — `capitulos/067-somador-subtrator-e-amplificador-de-instrumentacao.qmd`
- [ ] 068 — Integrador, derivador e fontes de corrente — `capitulos/068-integrador-derivador-e-fontes-de-corrente.qmd`
- [ ] 069 — O amp-op real: offset, slew rate, produto ganho-banda e saturação — `capitulos/069-o-amp-op-real-offset-slew-rate-produto-ganho-banda.qmd`
- [ ] 070 — Comparadores, histerese e o gatilho de Schmitt — `capitulos/070-comparadores-histerese-e-o-gatilho-de-schmitt.qmd`
- [ ] 071 — Filtros ativos e osciladores: Wien, relaxação e o 555 — `capitulos/071-filtros-ativos-e-osciladores-wien-relaxacao-e-o-555.qmd`


## Fase 4 — Energia, Interface e Construção


### Volume 12 — Fontes e Gestão de Energia

- [ ] 072 — Transformadores e acoplamento magnético — `capitulos/072-transformadores-e-acoplamento-magnetico.qmd`
- [ ] 073 — Fontes lineares: do transformador ao regulador — `capitulos/073-fontes-lineares-do-transformador-ao-regulador.qmd`
- [ ] 074 — Reguladores integrados: série, LDO e dissipação térmica — `capitulos/074-reguladores-integrados-serie-ldo-e-dissipacao.qmd`
- [ ] 075 — Fontes chaveadas: buck, boost e buck-boost — `capitulos/075-fontes-chaveadas-buck-boost-e-buck-boost.qmd`
- [ ] 076 — Baterias, células e circuitos de carga — `capitulos/076-baterias-celulas-e-circuitos-de-carga.qmd`
- [ ] 077 — Aterramento, malhas de terra, desacoplamento e proteção — `capitulos/077-aterramento-malhas-de-terra-desacoplamento-e.qmd`


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
