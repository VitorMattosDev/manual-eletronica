"""Verificacao de LACUNAS: capitulo-stub referenciado por texto ja publicado.

Uso:
    python ferramentas/verificar-lacunas.py

Motivo de existir: o checklist de push caca `?@`, que e referencia cruzada NAO
resolvida. Mas um capitulo-stub -- aquele cujo corpo e so "(em elaboracao)" --
carrega o rotulo {#sec-cap-NNN} normalmente, entao toda referencia a ele
*resolve*. O render sai limpo, o grep por `?@` da zero, e o buraco continua no
livro publicado: o leitor clica e cai numa pagina vazia.

E o mesmo padrao de `figuras/verificar-figuras.py`: contar <svg> prova que a
figura saiu, nunca que ela esta certa. Aqui, `?@` zero prova que a referencia
resolve, nunca que ela leva a conteudo.

Distingue dois defeitos, que tem causas e correcoes diferentes:

  LACUNA ATRASADA -- stub numerado ABAIXO do maior capitulo ja escrito. E um
      buraco no meio do livro: capitulo que a fila mandava escrever e ficou para
      tras. Falha dura (codigo 1). Foi o que aconteceu com 025, 026, 037 e 038.

  REFERENCIA A CAPITULO FUTURO -- @sec- apontando para stub numerado ACIMA do
      maior escrito. Nao e lacuna: o capitulo ainda nao chegou na fila. Mas
      viola a regra do CLAUDE.md ("@sec- so para rotulos ja escritos; conteudo
      futuro entra como mencao textual"). Aviso, nao falha.

Alem disso, confere a fronteira declarada no ROADMAP.md ("Proximo capitulo:
NNN") contra o menor [ ] da fila.

Sem emoji em print(): quebra no console do Windows (ver CLAUDE.md).
"""

import io
import os
import re
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CAPITULOS = os.path.join(REPO, "capitulos")
ROADMAP = os.path.join(REPO, "ROADMAP.md")

MARCA_STUB = "(em elabora"          # sem acento: nao depende da codificacao
RE_NUM = re.compile(r"^(\d{3})-")
RE_TITULO = re.compile(r"^#\s+(.*?)\s*\{#sec-cap-\d{3}\}", re.M)
RE_PENDENTE = re.compile(r"^- \[ \] (\d{3})", re.M)
RE_FRONTEIRA = re.compile(r"Pr.ximo cap.tulo:\s*\**\s*(\d{3})")

# O console do Windows nao e UTF-8 por padrao e mastiga os acentos dos titulos.
# Reconfigurar evita tanto a mojibake quanto o UnicodeEncodeError.
try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except (AttributeError, ValueError):
    pass


def ler(caminho):
    return io.open(caminho, encoding="utf-8").read()


def carregar_capitulos():
    """{numero: (arquivo, texto, e_stub)} para todo capitulo em disco."""
    caps = {}
    for nome in sorted(os.listdir(CAPITULOS)):
        m = RE_NUM.match(nome)
        if not m or not nome.endswith(".qmd"):
            continue
        texto = ler(os.path.join(CAPITULOS, nome))
        caps[m.group(1)] = (nome, texto, MARCA_STUB in texto)
    return caps


def titulo(texto):
    m = RE_TITULO.search(texto)
    return m.group(1) if m else "(sem titulo)"


def contiguos_ate(caps):
    """Maior M tal que 001..M estao todos escritos."""
    ultimo = None
    for num in sorted(caps):
        if caps[num][2]:
            break
        ultimo = num
    return ultimo


def referencias_a(caps, alvos):
    """{alvo: [(arquivo, linha, texto)]} vindas de capitulos NAO-stub."""
    achados = {n: [] for n in alvos}
    for num in sorted(caps):
        nome, texto, e_stub = caps[num]
        if e_stub:
            continue
        for i, linha in enumerate(texto.split("\n"), start=1):
            for alvo in alvos:
                if "@sec-cap-" + alvo in linha:
                    achados[alvo].append((nome, i, linha.strip()))
    return achados


def fronteira_roadmap():
    """(declarada no ROADMAP, menor [ ] real)."""
    if not os.path.exists(ROADMAP):
        return None, None
    texto = ler(ROADMAP)
    m = RE_FRONTEIRA.search(texto)
    pendentes = RE_PENDENTE.findall(texto)
    return (m.group(1) if m else None), (min(pendentes) if pendentes else None)


def bloco_referencias(alvos, achados, caps):
    for alvo in alvos:
        refs = achados[alvo]
        if not refs:
            continue
        print("  cap %s -- %s" % (alvo, titulo(caps[alvo][1])))
        print("           %d referencia(s):" % len(refs))
        for nome, linha, txt in refs:
            if len(txt) > 94:
                txt = txt[:91] + "..."
            print("      capitulos/%s:%d" % (nome, linha))
            print("          %s" % txt)
        print()


def main():
    caps = carregar_capitulos()
    escritos = sorted(n for n in caps if not caps[n][2])
    stubs = sorted(n for n in caps if caps[n][2])

    if not escritos:
        print("nenhum capitulo escrito ainda; nada a verificar.")
        return 0

    maior_escrito = max(escritos)
    contig = contiguos_ate(caps)

    atrasados = [n for n in stubs if n < maior_escrito]
    futuros = [n for n in stubs if n > maior_escrito]

    print("capitulos em disco: %d   escritos: %d   stubs: %d"
          % (len(caps), len(escritos), len(stubs)))
    print("contiguos ate.....: %s" % contig)
    print("maior escrito.....: %s" % maior_escrito)
    print()

    # ---------- defeito 1: lacuna atrasada ----------
    if atrasados:
        print("=== LACUNAS ATRASADAS (%d) ===" % len(atrasados))
        print("Stub numerado abaixo do maior capitulo escrito: buraco no meio do livro.")
        for n in atrasados:
            print("  %s  %s" % (n, titulo(caps[n][1])))
        print()

        achados = referencias_a(caps, atrasados)
        total = sum(len(v) for v in achados.values())
        if total:
            print("--- CONTRATOS JA PUBLICADOS (%d) ---" % total)
            print("Texto ja no ar que promete conteudo destes capitulos.")
            print("Quem for escreve-los tem de honrar cada linha abaixo.")
            print()
            bloco_referencias(atrasados, achados, caps)
    else:
        print("=== LACUNAS ATRASADAS ===")
        print("  nenhuma: os capitulos escritos formam um bloco contiguo.")
        print()

    # ---------- defeito 2: referencia a capitulo futuro ----------
    achados_fut = referencias_a(caps, futuros)
    total_fut = sum(len(v) for v in achados_fut.values())
    print("=== REFERENCIA A CAPITULO FUTURO (%d) ===" % total_fut)
    if total_fut:
        print("AVISO -- nao e lacuna, mas viola a regra do CLAUDE.md:")
        print("  '@sec- so para rotulos ja escritos; conteudo futuro entra como")
        print("   mencao textual (\"assunto do Volume 11\"), nunca @sec-'.")
        print("O link resolve e leva a uma pagina vazia. Nao falha a verificacao;")
        print("corrigir trocando o @sec- por mencao textual.")
        print()
        bloco_referencias(futuros, achados_fut, caps)
    else:
        print("  nenhuma.")
        print()

    # ---------- fronteira ----------
    declarada, menor_pendente = fronteira_roadmap()
    print("=== FRONTEIRA ===")
    print("  menor [ ] no ROADMAP..........: %s" % (menor_pendente or "(nenhum)"))
    print("  'Proximo capitulo' declarado..: %s" % (declarada or "(nao declarado)"))
    if declarada and menor_pendente and declarada != menor_pendente:
        print("  AVISO: divergem. O ROADMAP aponta para %s, mas o menor pendente e %s."
              % (declarada, menor_pendente))
    elif not declarada:
        print("  AVISO: o ROADMAP nao declara 'Proximo capitulo'.")
    print()

    if atrasados:
        print("RESULTADO: FALHA -- %d lacuna(s) atrasada(s): %s."
              % (len(atrasados), ", ".join(atrasados)))
        print("Fechar esses capitulos, ou aceitar a lacuna conscientemente e")
        print("declara-la no ROADMAP antes de seguir para o volume seguinte.")
        return 1

    print("RESULTADO: OK -- nenhuma lacuna atrasada.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
