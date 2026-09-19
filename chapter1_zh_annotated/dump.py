import sys,re
a,b=int(sys.argv[1]),int(sys.argv[2])
lines=open('chapter1_zh_annotated.tex').read().split('\n')
skip=re.compile(r"^\s*(\\draw|\\fill|\\node|\\coordinate|\\path|\\clip|\\foreach|\\begin\{tikzpicture|\\end\{tikzpicture|\\begin\{scope|\\end\{scope|\\useasboundingbox|%)")
for i in range(a-1,min(b,len(lines))):
    l=lines[i]
    if l.strip() and not skip.match(l) and re.search(r"[A-Za-z]{3}",l):
        print(f"{i+1}|{l}")
