import sys, re
sys.path.insert(0,'/home/user/Task11/fa/tam11b5f/tools')
import tx
def scan(pattern, tags=None, kinds=('Thinking','Text','ToolUse'), ctx=160, limit=40):
    pat=re.compile(pattern, re.I)
    for r in tx.runs():
        if tags and r['tag'] not in tags: continue
        hits=[]
        for i,et,bt,t in tx.blocks(r['path']):
            if bt not in kinds: continue
            for m in pat.finditer(t):
                a=max(0,m.start()-ctx); b=min(len(t),m.end()+ctx)
                hits.append((i,bt,' '.join(t[a:b].split())))
        print(f"\n==== {r['tag']} {r['short']}  hits={len(hits)}")
        for i,bt,s in hits[:limit]:
            print(f"  [{i} {bt}] ...{s}")
        if len(hits)>limit: print(f"  ... {len(hits)-limit} more")
if __name__=='__main__':
    tags=sys.argv[2].split(',') if len(sys.argv)>2 and sys.argv[2]!='-' else None
    kinds=tuple(sys.argv[3].split(',')) if len(sys.argv)>3 else ('Thinking','Text','ToolUse')
    scan(sys.argv[1], tags, kinds)
