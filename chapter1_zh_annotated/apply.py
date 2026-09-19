import json,sys
d=json.load(open(sys.argv[1]))
lines=open('chapter1_zh_annotated.tex').read().split('\n')
for k,v in d.items():
    lines[int(k)-1]=v
open('chapter1_zh_annotated.tex','w').write('\n'.join(lines))
print("lines replaced:",len(d))
