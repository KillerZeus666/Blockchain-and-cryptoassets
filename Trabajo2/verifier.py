#!/usr/bin/env python3
import json as J, hashlib as H, sys as S

D="dataset_128.txt"
P="proof.json"

def h(b): return H.sha256(b).digest()
def rd(p):
    with open(p,"r",encoding="utf-8") as f:
        return [x.strip() for x in f if x.strip()]

def root(ws):
    lv=[h(w.encode("utf-8")) for w in ws]
    while len(lv)>1:
        lv=[h(lv[i]+lv[i+1]) for i in range(0,len(lv),2)]
    return lv[0]

def hx(s):
    if not isinstance(s,str) or len(s)!=64: return None
    try: return bytes.fromhex(s)
    except: return None

def ok(leaf,path,r):
    cur=h(leaf.encode("utf-8"))
    if not isinstance(path,list) or len(path)!=7: return False
    for st in path:
        if not (isinstance(st,list) and len(st)==2): return False
        a,b=st
        sa=(a=="SELF"); sb=(b=="SELF")
        if sa==sb: return False
        if sa:
            rb=hx(b); 
            if rb is None: return False
            cur=h(cur+rb)
        else:
            ra=hx(a); 
            if ra is None: return False
            cur=h(ra+cur)
    return cur==r

def main():
    try:
        ws=rd(D)
        if len(ws)!=128 or len(set(ws))!=128:
            print("INVALID"); return 1
        r=root(ws)  
        with open(P,"r",encoding="utf-8") as f:
            pr=J.load(f)
        leaf=pr.get("leaf"); path=pr.get("path")
        if not isinstance(leaf,str) or leaf not in ws:
            print("INVALID"); return 1
        print("VALID" if ok(leaf,path,r) else "INVALID")
        return 0
    except:
        print("INVALID"); return 1

if __name__=="__main__":
    S.exit(main())
