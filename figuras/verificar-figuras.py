"""Verificacao VISUAL das figuras de um capitulo.

Uso:
    python figuras/verificar-figuras.py capitulos/001-....qmd

Extrai todos os blocos ```{.tikz}``` do .qmd, monta um unico documento
standalone com o MESMO preambulo da extensao danmackinlay/tikz, compila com
pdflatex e rasteriza para PNG (PyMuPDF). O PNG resultante pode ser aberto —
ou lido por um agente — para conferir o que nenhum grep pega: rotulo
sobreposto, polaridade invertida, seta apontando para o lado errado, curva
estourando o eixo.

Motivo de existir: `quarto render` pode terminar sem erro e ainda assim
produzir figura errada. Contagem de <svg> prova que a figura *saiu*; nao prova
que ela esta *certa*.

Requer o bin do TinyTeX no PATH (ver CLAUDE.md).
"""

import io
import os
import re
import subprocess
import sys
import tempfile

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LUA = os.path.join(REPO, "_extensions", "danmackinlay", "tikz", "tikz.lua")


def preambulo():
    """Le o preambulo direto do template da extensao, para nao divergir dele."""
    lua = io.open(LUA, encoding="utf-8").read()
    m = re.search(r"conf\.tex_template_content or \[\[(.*?)\]\]\)", lua, re.S)
    if not m:
        raise SystemExit("nao achei o template embutido em tikz.lua")
    tpl = m.group(1).split("$additional-packages$")[0]
    return tpl.replace(
        r"\documentclass[border=4pt]{standalone}",
        r"\documentclass[border=6pt,varwidth=17cm]{standalone}",
    )


def blocos(qmd_path):
    qmd = io.open(qmd_path, encoding="utf-8").read()
    saida = []
    for b in re.findall(r"```\{\.tikz\}\n(.*?)```", qmd, re.S):
        m = re.search(r"%%\| filename:\s*(\S+)", b)
        nome = m.group(1) if m else "sem-filename"
        corpo = "\n".join(l for l in b.split("\n") if not l.startswith("%%|"))
        saida.append((nome, corpo))
    return saida


def main():
    if len(sys.argv) < 2:
        raise SystemExit(__doc__)
    qmd_path = sys.argv[1]

    figs = blocos(qmd_path)
    print("blocos {.tikz} encontrados:", len(figs))
    if not figs:
        return

    partes = [preambulo(), "\n", r"\begin{document}", "\n"]
    for nome, corpo in figs:
        partes.append(r"\par\noindent\texttt{" + nome.replace("_", r"\_") + r"}\par\medskip")
        partes.append("\n" + corpo + "\n")
        partes.append(r"\par\bigskip" + "\n")
    partes.append(r"\end{document}" + "\n")

    workdir = tempfile.mkdtemp(prefix="verif-figuras-")
    tex = os.path.join(workdir, "verif.tex")
    io.open(tex, "w", encoding="utf-8", newline="\n").write("".join(partes))

    r = subprocess.run(
        ["pdflatex", "-interaction=nonstopmode", "verif.tex"],
        cwd=workdir, capture_output=True, text=True, errors="replace",
    )
    pdf = os.path.join(workdir, "verif.pdf")
    if not os.path.exists(pdf):
        for linha in r.stdout.split("\n"):
            if linha.startswith("!"):
                print("ERRO LaTeX:", linha)
        raise SystemExit("pdflatex nao gerou PDF — ver " + workdir)

    for linha in r.stdout.split("\n"):
        if linha.startswith("!"):
            print("AVISO LaTeX:", linha)

    import fitz  # PyMuPDF

    doc = fitz.open(pdf)
    destino = os.path.join(workdir, "verif.png")
    doc[0].get_pixmap(dpi=170).save(destino)
    print("PNG para conferencia visual:")
    print("   ", destino)


if __name__ == "__main__":
    main()
