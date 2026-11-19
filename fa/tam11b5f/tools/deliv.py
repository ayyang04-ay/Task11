import sys, glob, os
sys.path.insert(0,'/home/user/Task11/fa/tam11b5f/tools')
import tx
def mds():
    out=[]
    for r in tx.runs():
        c=[p for p in glob.glob(r['outdir']+'/*.md') if 'README' not in os.path.basename(p)]
        assert len(c)==1, (r['tag'], c)
        out.append((r, c[0]))
    return out
if __name__=='__main__':
    for r,p in mds():
        n=sum(1 for _ in open(p))
        w=len(open(p).read().split())
        print(f"{r['tag']} {r['short']} {os.path.basename(p):38s} lines={n:4d} words={w}")
