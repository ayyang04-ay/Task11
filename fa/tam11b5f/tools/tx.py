import json, collections, os, glob

JOBS = {
 'fable': 'Anton_e55870a045744a9e932736ae7ca1822f_job_c638eb2d_2026-11-19',
 'opus':  'Anton_e55870a045744a9e932736ae7ca1822f_job_de39df86_2026-11-19',
}
ROOT = '/home/user/Task11/runs'
LABEL = {}  # short hash -> label

def runs():
    out = []
    for model, job in JOBS.items():
        for p in sorted(glob.glob(f'{ROOT}/{job}/transcripts/*.json')):
            b = os.path.basename(p)[:-5]              # attempt_01_aa6a0794
            att = int(b.split('_')[1]); sh = b.split('_')[2]
            tag = ('O' if model == 'opus' else 'F') + str(att)
            out.append(dict(model=model, job=job, attempt=att, short=sh,
                            tag=tag, path=p, base=b,
                            outdir=f'{ROOT}/{job}/outputs/{b}',
                            grading=f'{ROOT}/{job}/grading/{b}.json'))
    out.sort(key=lambda r: (r['model'] != 'opus', r['attempt']))
    return out

def elements(path):
    d = json.load(open(path))['contexts'][0]['conversation']['data']
    for i, e in enumerate(d):
        c = e.get('contents')
        if isinstance(c, str):
            try: c = json.loads(c)
            except Exception: c = [{'type': 'RAW', 'data': c}]
        yield i, e.get('type'), (c if isinstance(c, list) else [c])

def blocks(path):
    """yield (idx, elem_type, block_type, text)"""
    for i, et, cs in elements(path):
        for b in cs:
            if not isinstance(b, dict): continue
            bt = b.get('type')
            txt = b.get('data')
            if txt is None and bt == 'ToolResult':
                parts = []
                for sub in (b.get('content') or []):
                    if isinstance(sub, dict) and isinstance(sub.get('data'), str):
                        parts.append(sub['data'])
                txt = '\n'.join(parts)
            if txt is None:
                txt = json.dumps(b, default=str)
            yield i, et, bt, (txt if isinstance(txt, str) else json.dumps(txt, default=str))

if __name__ == '__main__':
    for r in runs():
        bt = collections.Counter(); think_tot = think_txt = 0; nel = 0
        for i, et, b, t in blocks(r['path']):
            bt[b] += 1
            if b == 'Thinking':
                think_tot += 1
                if t.strip(): think_txt += 1
            nel = max(nel, i)
        print(f"{r['tag']} {r['short']} {r['model']:5s} att{r['attempt']} elems={nel+1} "
              f"thinking={think_txt}/{think_tot} with-text  blocks={dict(bt)}")
