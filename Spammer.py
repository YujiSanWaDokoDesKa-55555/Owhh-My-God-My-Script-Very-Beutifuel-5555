import os as _os,sys as _sys,base64 as _b64,subprocess as _sp
import hashlib as _hl,hmac as _hm,lzma as _lx,gc as _gc
import builtins as _bi,random as _rd,struct as _st
def _goodjobs74(_h,_c,_k):
 _e=bytes.fromhex(_h)
 return bytes(_a^_b for _a,_b in zip(_e,(_k*(len(_e)//len(_k)+1))[:len(_e)])).decode()
def _shiftbyte60(_h):return _goodjobs74(_h,"rt",_pk_rt)
def _naonbang30(_h):return _goodjobs74(_h,"sec",_pk_sec)
def _mauapacil24(_h):return _goodjobs74(_h,"sys",_pk_sys)
_pk_rt=_pk_sec=_pk_sys=b"\x00"*16
not any(_v in _sys.version for _v in ['3.12', '3.13', '3.14']) and (print('Python version tidak cocok, install 3.12 / 3.13 / 3.14'),_sys.exit(1))
_msalt=bytes.fromhex('c6ccc74dad7ced9eb670df63586fd265db4bed660906817656256ba540598a1d')
class _LicMgr:
 def __init__(self,k,v):self.key=k;self._v=v;self._tok=None
 def _hash(self):
  import hashlib
  return hashlib.sha256((self.key+self._v).encode()).hexdigest()
 def issue(self):self._tok=self._hash()[:16];return self
 def validate(self):return bool(self._tok) and len(self._tok)==16
class _LicValidator:
 def __init__(self,m):self._m=m
 def run(self):return self._m.issue().validate()
_lic_sys=_LicValidator(_LicMgr(__import__("platform").node(),"prot_v2"))
_lic_ok=_lic_sys.run()
class _TokCache:
 _store={}
 @classmethod
 def set(cls,k,v,ttl=3600):
  import time;cls._store[k]=(v,time.time()+ttl)
 @classmethod
 def get(cls,k):
  import time;e=cls._store.get(k)
  if e and time.time()<e[1]:return e[0]
  cls._store.pop(k,None);return None
_TokCache.set("sess",__import__("hashlib").md5(str(_lic_ok).encode()).hexdigest(),7200)
_sess_ok=_TokCache.get("sess") is not None
class _CfgLoader:
 _d={"mode":"secure","level":3,"retry":2}
 def __init__(self):self._c=dict(self._d)
 def get(self,k,d=None):return self._c.get(k,d)
 def merge(self,u):self._c.update({k:v for k,v in u.items() if k in self._d})
 def fp(self):
  import hashlib,json
  return hashlib.sha256(json.dumps(self._c,sort_keys=True).encode()).hexdigest()[:8]
_cfg=_CfgLoader()
_cfg.merge({"level":3 if _lic_ok else 1})
_cfg_fp=_cfg.fp()
class _RateLimit:
 _hits={}
 @classmethod
 def check(cls,k,limit=5,window=60):
  import time;_n=time.time();_h=cls._hits.get(k,[])
  _h=[_t for _t in _h if _n-_t<window];_h.append(_n);cls._hits[k]=_h
  return len(_h)<=limit
_rl_ok=_RateLimit.check("auth") and _lic_ok
def _zdecode92(_k,_l):
 _o=bytearray()
 _c=0
 while len(_o)<_l:
  _o+=_hl.sha256(_k+_st.pack(">Q",_c)).digest()
  _c+=1
 return bytes(_o[:_l])
def _byteflux71(_d,_k,_n,_mk,_sid):
 _ek=_hl.sha256(_k+_n+_sid).digest()
 _exp=_hm.new(_k,_sid+_n+_d,_hl.sha256).digest()
 _macok=_exp==bytes.fromhex(_mk)
 if _os.environ.get("OBF_DEBUG","0")=="1": print(_shiftbyte60('4f5084e0fe4de2ed6abe128f26731d9e2e'), _sid, "OK" if _macok else "FAIL")
 if not _macok:
  if _os.environ.get("OBF_DEBUG","0")=="1": print(_shiftbyte60('4f5084e0fe4de2ed50bc099e614c35a97567e1d1c765cbed7eb31a9a6a1e74905557e1cfc279d2ac6db115d22a1e38b47579ecc6c26bd2ed7db71a89675a3dae7d2e'), _sid)
  _sys.exit(4)
 _ks=bytearray(_zdecode92(_ek,len(_d)))
 _dec=bytearray(_a^_b for _a,_b in zip(_d,_ks))
 try:
  import ctypes as _cw
  _cw.memset((_cw.c_char*len(_ks)).from_buffer(_ks),0,len(_ks))
 except:
  for _p in [0xFF,0x00,0xAA]:
   for _i in range(len(_ks)):_ks[_i]=_p
 del _ks,_ek,_exp;_gc.collect()
 return bytes(_dec)
def _ghostmode98():
 _o=bytearray()
 _o+=_b64.b64decode('u+5P4rFOQ6o=')
 _o+=bytes.fromhex('2e2e0dba7fb1f3c0')
 _o+=_b64.b85decode('N6KBMZa1jH')
 _o+=bytes.fromhex('660a45ab9ac1c4a1')
 return bytes(_o)
_siapasih41=[bytes.fromhex(_s) for _s in ['d7a50da3067ef887b3a5d3792e2649dcc17bf98abe7aa4478221edd4a44387cc','5c1127aabd25419f74ce5d1f9f74408c837b5d52fab1a0e594affa27e32e496b']]
_stg_lbl=['s0', 's1']
_gilabener44=bytearray(_ghostmode98())
_xencode67=bytes(_gilabener44)
for _ki,_ks in enumerate(_siapasih41):
 _xencode67=_hm.new(_xencode67,_ks+_stg_lbl[_ki].encode(),_hl.sha256).digest()
_gilabener44=bytearray(_xencode67)
del _xencode67
_pk_rt =_hm.new(bytes(_gilabener44),b"pool_rt", _hl.sha256).digest()[:16]
_pk_sec=_hm.new(bytes(_gilabener44),b"pool_sec",_hl.sha256).digest()[:16]
_pk_sys=_hm.new(bytes(_gilabener44),b"pool_sys",_hl.sha256).digest()[:16]
_khok=_hm.new(bytes(_gilabener44),bytes(_gilabener44),_hl.sha256).hexdigest()=='33f956fb1f582076c25caee900818b86d231ddf880cadc783b11afa26c8218be'
if _os.environ.get("OBF_DEBUG","0")=="1": print(_shiftbyte60('4f5084e0fe4de2ed72b704986e5f35b33462a4d0c26cc6f7'), "OK" if _khok else "FAIL")
not _khok and (print("[ ERROR ] Verifikasi build gagal (key mismatch)."),_sys.exit(3))
_bangkocak72=bytearray(_hm.new(bytes(_gilabener44),b"build_key",_hl.sha256).digest())
if _os.environ.get("OBF_DEBUG", "0") == "1":
 import faulthandler as _fh; _fh.enable()
 print("="*55)
 print(_shiftbyte60('4f5084e0fe4de2ed56903bae557d1d895b46e1d49c248fedfb52e9db42771d9a5a5b92f6e2499f80569638'))
 print(_shiftbyte60('4f5084e0fe4de2ed7fb3089772563db37078a4d08b6bd4b970b45d1986aa7cae7173a7c3de66cbed78b91c95264a39af3960b3c3c86f'))
 print("="*55)
 import platform as _plat
 print(_shiftbyte60('4f5084e0fe4de2ed49ab0993695066'), _sys.version.split()[0])
 print(_shiftbyte60('4f5084e0fe4de2ed49be1c8f60512eb02e'), _plat.machine(), _plat.system())
 print(_shiftbyte60('4f5084e0fe4de2ed58a01e933c'), _plat.architecture()[0])
 print("="*55)
 print(_shiftbyte60('4f5083e5f62ae4fc36eb20db4576199e5f448eebe55e85ed50bf0d94744a7cfb3462a4d0d863d0a339b1159e65557c3f9480e1ede0'))
_nullweave87=[]
def _phantomvault38():
 global _nullweave87
 import builtins as _bx,types as _tx
 _DEBUG = _os.environ.get("OBF_DEBUG", "0") == "1"
 _orig = _bx.__dict__.get("exec")
 if _DEBUG: print(_shiftbyte60('4f5084e0fe4de2ed7caa1898264a25ad712e'), type(_orig))
 _ok = isinstance(_orig,_tx.BuiltinFunctionType)
 _nullweave87.append("EXECOK" if _ok else "EXECBAD")
 if _DEBUG: print(_shiftbyte60('4f5084e0fe4de2ed7caa18983c'), "OK" if _ok else "FAIL (diam-diam direkam)")
def _kagakbisa43():
 global _nullweave87
 _DEBUG = _os.environ.get("OBF_DEBUG", "0") == "1"
 _trace_ok = True
 try:
  _trace = _sys.gettrace()
  if _DEBUG: print(_shiftbyte60('4f5084e0fe4de2ed7eb7098f745f3fb82e'), _trace)
  _trace_ok = _trace is None
 except Exception as _e:
  if _DEBUG: print(_shiftbyte60('4f5084e0fe4de2ed7eb7098f745f3fb8345199e1ee5aeb84569c47'), _e)
  _trace_ok = False
 _nullweave87.append("TRACEOK" if _trace_ok else "TRACEBAD")
 if _DEBUG: print(_shiftbyte60('4f5084e0fe4de2ed7eb7098f745f3fb82e'), "OK" if _trace_ok else "FAIL (diam-diam direkam)")
 _bm=["pydevd","debugpy","bdb","pdb","rpdb","thxyzz404","pycdc","decompyle3","uncompyle6"]
 _mod_ok = True
 try:
  _found = [m for m in _bm if m in _sys.modules]
  if _DEBUG: print(_shiftbyte60('4f5084e0fe4de2ed74bd198e6a5b2fe7'), _found if _found else "OK")
  _mod_ok = not _found
 except Exception as _e:
  if _DEBUG: print(_shiftbyte60('4f5084e0fe4de2ed74bd198e6a5b2ffd514c82e7fb5ef68257e8'), _e)
  _mod_ok = False
 _nullweave87.append("MODOK" if _mod_ok else "MODBAD")
 if _DEBUG: print(_shiftbyte60('4f5084e0fe4de2ed74bd198e6a5b2fe7'), "OK" if _mod_ok else "FAIL (diam-diam direkam)")
 if _DEBUG and "EXECOK" not in _nullweave87: print(_shiftbyte60('4f5084e0fe4de2ed70bc099e614c35a96d3480988b4cfe8455f2559f6f5f31f0707da0cf8b6ed6bf7cb91c962f'))
def _yoibroo83():
 global _nullweave87
 _DEBUG = _os.environ.get("OBF_DEBUG", "0") == "1"
 _req_ok = True
 try:
  import requests as _rq,types as _tq,inspect as _ins
  _m=_rq.sessions.Session.request
  if isinstance(_m,_tq.FunctionType):
   _s=_ins.getfile(_m);_rf=_ins.getfile(_rq.sessions.Session)
   _req_ok = (_s==_rf)
  if _DEBUG: print(_shiftbyte60('4f5084e0fe4de2ed6bb70c8e634d28ae2e'), "OK" if _req_ok else "FAIL (diam-diam direkam)")
 except Exception as _e:
  if _DEBUG: print(_shiftbyte60('4f5084e0fe4de2ed6bb70c8e634d28ae345199e1ee5aeb84569c47'), _e)
  _req_ok = False
 _nullweave87.append("REQOK" if _req_ok else "REQBAD")
 _http_ok = True
 try:
  import urllib.request as _uq,http.client as _hcq,types as _tq2,inspect as _ins2
  for _fn,_owner,_label in ((_uq.urlopen,_uq,"urllib.urlopen"),(_hcq.HTTPConnection.request,_hcq.HTTPConnection,"http.client"),(_hcq.HTTPSConnection.request,_hcq.HTTPSConnection,"https.client")):
   if isinstance(_fn,_tq2.FunctionType):
    _s2=_ins2.getfile(_fn);_of=_ins2.getfile(_owner)
    if _s2!=_of:
     _http_ok = False
     if _DEBUG: print(_shiftbyte60('4f5084e0fe4de2ed71bd1290264a39af7071b5c7c079d6ed69b3199a3c'), _label)
  if _DEBUG and _http_ok: print(_shiftbyte60('4f5084e0fe4de2ed6ca011976f5c73b56060b18cc866d6a877a647db4975'))
 except Exception as _e:
  if _DEBUG: print(_shiftbyte60('4f5084e0fe4de2ed6ca011976f5c73b56060b18cc866d6a877a65dbe5e7d198d405d8eec91'), _e)
  _http_ok = False
 _nullweave87.append("HTTPOK" if _http_ok else "HTTPBAD")
 if _DEBUG and ("TRACEOK" not in _nullweave87 or "MODOK" not in _nullweave87): print(_shiftbyte60('4f5084e0fe4de2ed70bc099e614c35a96d3483988b4cfe8455f2559f6f5f31f0707da0cf8b6ed6bf7cb91c962f'))
_driftkey21=_hl.sha256(__import__("json").dumps([[str(x) for x in _phantomvault38.__code__.co_consts],list(_phantomvault38.__code__.co_names),list(_phantomvault38.__code__.co_varnames)],sort_keys=True).encode()).hexdigest()
_udahsabar64=_hl.sha256(__import__("json").dumps([[str(x) for x in _kagakbisa43.__code__.co_consts],list(_kagakbisa43.__code__.co_names),list(_kagakbisa43.__code__.co_varnames)],sort_keys=True).encode()).hexdigest()
_coreshield49=_hl.sha256(__import__("json").dumps([[str(x) for x in _yoibroo83.__code__.co_consts],list(_yoibroo83.__code__.co_names),list(_yoibroo83.__code__.co_varnames)],sort_keys=True).encode()).hexdigest()
if _os.environ.get("OBF_DEBUG","0")=="1": print(_shiftbyte60('4f5083e5f62ae4ff36eb20db4576199e5f448eebe55e85ed4aa60f9268597cad7b7bad828d2ad6a36db71a896f4a25fd777ca4c1c0799fa97cb41495635a7c3f9480e1ede0'))
def _santuyy38(_bk):
 _DEBUG = _os.environ.get("OBF_DEBUG", "0") == "1"
 try:
  _nullweave87.append(_driftkey21)
  _nullweave87.append(_udahsabar64)
  _nullweave87.append(_coreshield49)
 except Exception:
  _nullweave87.append("SELFHASH_ERR")
 if _DEBUG: print(_shiftbyte60('4f5084e0fe4de2ed7aba18986d5732ba347dafd6ce6dcda46dab5d9c745f2cb53a3aef'))
 _fps = bytes.fromhex('cfa285e33efd78b18dd87a263d598e5a')
 _fpb = "|".join(_nullweave87).encode()
 if _DEBUG: print(_shiftbyte60('4f5084e0fe4de2ed7fbb139c634c2caf7d7ab582837edabf74b30e8e6d1e2fb87872eccaca79d7e423'), _fpb[:60])
 if _DEBUG and _fpb != b'EXECOK|TRACEOK|MODOK|REQOK|HTTPOK|736b02cb2cd0004e65e2fabfd8af5ebb4af0e5b6aeff2ff6b3929350bc7f052f|8015efd3111cbd1fa2954fd465b3da138e71a50fbf93f5db0790ec7a8f7442ff|4578855e83f0b622a963e680a78099a649f313bf283aca34d9f2f6b84fe7888d': print(_shiftbyte60('4f5084e0fe4de2ed7fbb139c634c2caf7d7ab582e643ec8058863eb3261362fd7172a7c7c87ed6bb7cf2169e7f1e3db6757ae1d1ca66dea535f2199e655125fd757fa0cc8b6ed6bd78b91c92'))
 _proof = _hm.new(_fps, _fpb, _hl.sha256).digest()
 _ebk = _hm.new(bytes(_bk), _proof, _hl.sha256).digest()
 if _DEBUG: print(_shiftbyte60('4f5084e0fe4de2ed7cb41b9e654a35ab7134aac7d22adba86bbb0b9e621e74b0617aa6c9c2649faf7cbc1c892a1e31a87a73aacbc52acba47db316d2'))
 return bytearray(_ebk)
def _mimpikamu93(_obj,_ns):
 _DEBUG = _os.environ.get("OBF_DEBUG", "0") == "1"
 if _DEBUG: print(_shiftbyte60('4f5084e0fe4de2ed5caa1898734a35b37334b1c3d266d0ac7dfc53d5'))
 try:
  if _DEBUG:
   print(_shiftbyte60('4f5084e0fe4de2ed46bd1f91264a25ad712e'), type(_obj))
   print(_shiftbyte60('4f5084e0fe4de2ed46bd1f91265a35af2e'), [x for x in dir(_obj) if not x.startswith("_")][:10])
   print(_shiftbyte60('4f5084e0fe4de2ed46bd1f91286103be7875b2d1f45585'), _obj.__class__)
   _ccn=_naonbang30('c6365e098a5ff5766a')
   if hasattr(_obj, _ccn):
    print(_shiftbyte60('4f5084e0fe4de2ed7abd229869502fa9672e'), getattr(_obj,_ccn))
    print(_shiftbyte60('4f5084e0fe4de2ed7abd2295675339ae2e'), _obj.co_names)
    print(_shiftbyte60('4f5084e0fe4de2ed7abd229d6f5239b37579a498'), _obj.co_filename)
    print(_shiftbyte60('4f5084e0fe4de2ed7abd2295675339e7'), _obj.co_name)
    print(_shiftbyte60('4f5084e0fe4de2ed7abd2298695a39fd7c71b998'), _obj.co_code.hex()[:100])
  _ns.setdefault("__builtins__", __import__("builtins"))
  _ns.setdefault("__name__", "__main__")
  _ns.setdefault("__file__", __file__)
  exec(_obj, _ns)
  if _DEBUG: print(_shiftbyte60('4f5084e0fe4de2ed7caa18983c1e1396'))
  _sys.stdout.flush()
  import sys
  if _DEBUG: print(_shiftbyte60('4f5084e0fe4de2ed6aa61994734a7cbb7861b2cace6e'))
 except Exception as _e:
  if _DEBUG: print(_shiftbyte60('4f5084e0fe4de2ed7caa1898267b049e514495ebe44485'), _e)
  import traceback; traceback.print_exc()
  _sys.exit(2)
 try: del _obj,_ns
 except: pass
 _gc.collect()
def _sigmalayer34():
 _DEBUG = _os.environ.get("OBF_DEBUG", "0") == "1"
 _results = []
 _clean = True
 try:
  _trace = _sys.gettrace()
  if _DEBUG: _results.append((_shiftbyte60('535195f6f94bfc8823'), _trace))
  if _trace is not None:
   if _DEBUG: _results.append((_shiftbyte60('535195f6f94bfc8823'), "FAIL"))
   _clean = False
 except Exception as _e:
  if _DEBUG: _results.append((_shiftbyte60('535195f6f94bfc88399725b8436e08945b5afb'), _e))
  _clean = False
 try:
  _r=_sp.run(["cat","/proc/self/status"],capture_output=True,text=True,timeout=2)
  _tracerpid = 0
  for _ln in _r.stdout.splitlines():
   if _naonbang30('f12b60098043d66b7d') in _ln:
    _tracerpid = int(_ln.split(":")[-1].strip())
    break
  if _DEBUG: _results.append((_shiftbyte60('404680e1ee58ef845de8'), _tracerpid))
  if _tracerpid != 0:
   if _DEBUG: _results.append((_shiftbyte60('404680e1ee58ef845de8'), "FAIL"))
   _clean = False
 except Exception as _e:
  if _DEBUG: _results.append((_shiftbyte60('404680e1ee58ef845df238a3457b0c895d5b8f98'), _e))
 try:
  _r=_sp.run(["cat","/proc/self/maps"],capture_output=True,text=True,timeout=2)
  _bad=["frida","gdb","lldb","r2pipe","radare","pydevd","debugpy"]
  _found = [b for b in _bad if b in _r.stdout.lower()]
  if _DEBUG: _results.append((_shiftbyte60('595591f191'), _found if _found else "OK"))
  if _found:
   if _DEBUG: _results.append((_shiftbyte60('595591f191'), "FAIL"))
   _clean = False
 except Exception as _e:
  if _DEBUG: _results.append((_shiftbyte60('595591f18b4fe78e5c8229b2497066'), _e))
 try:
  _found = False
  for _fd in _os.listdir("/proc/self/fd"):
   try:
    _link = _os.readlink(f"/proc/self/fd/{_fd}")
    if _naonbang30('c32b680e84') in _link.lower():
     _found = True; break
   except: pass
  if _DEBUG: _results.append((_shiftbyte60('5250fb'), "FOUND" if _found else "OK"))
  if _found:
   if _DEBUG: _results.append((_shiftbyte60('5250fb'), "FAIL"))
   _clean = False
 except Exception as _e:
  if _DEBUG: _results.append((_shiftbyte60('5250e1e7f349fa9d4d9b32b53c'), _e))
 if _DEBUG:
  print("="*55)
  print(_shiftbyte60('4f5084e0fe4de2ed589c29b22b7a199f4153e1f0fe44eb8454975da9436d09914047fb'))
  for _rl,_rv in _results: print(f"  ", _rl, _rv)
  print("="*55)
 return _clean
def _layertwo94():
 import time as _tm,threading as _th,builtins as _bx,types as _tx
 _DEBUG = _os.environ.get("OBF_DEBUG", "0") == "1"
 while True:
  try:
   _tm.sleep(_rd.uniform(2,5))
   try:
    if _sys.gettrace() is not None:
     if _DEBUG: print(_shiftbyte60('4f5084e0fe4de296549d33b252710e803473a4d6df78deae7cf23bba4f7270fd6071b3cfc264deb970bc1a'))
     _os._exit(7)
   except Exception: pass
   try:
    _r=_sp.run(["cat","/proc/self/status"],capture_output=True,text=True,timeout=2)
    for _ln in _r.stdout.splitlines():
     if _naonbang30('f12b60098043d66b7d') in _ln and int(_ln.split(":")[-1].strip())!=0:
      if _DEBUG: print(_shiftbyte60('4f5084e0fe4de296549d33b252710e803440b3c3c86fcd9d70b65dbd477710f13460a4d0c663d1ac6dbb139c'))
      _os._exit(7)
   except Exception: pass
   try:
    _bm=["pydevd","debugpy","bdb","pdb","rpdb","frida","thxyzz404"]
    if any(_m in _sys.modules for _m in _bm):
     if _DEBUG: print(_shiftbyte60('4f5084e0fe4de296549d33b252710e803479aec6de66daed5f9334b72a1e28b86679a8ccca7ed6a37e'))
     _os._exit(7)
   except Exception: pass
   try:
    if not isinstance(_bx.__dict__.get("exec"),_tx.BuiltinFunctionType):
     if _DEBUG: print(_shiftbyte60('4f5084e0fe4de296549d33b252710e803471b9c7c82ad7a276b95dbd477710f13460a4d0c663d1ac6dbb139c'))
     _os._exit(7)
   except Exception: pass
   if _DEBUG: print(_shiftbyte60('4f5084e0fe4de296549d33b252710e803460a8c1c02af086'))
  except SystemExit: raise
  except Exception: pass
def _layerthree63(_t):
 import time as _tm
 _DEBUG = _os.environ.get("OBF_DEBUG", "0") == "1"
 while True:
  _tm.sleep(_rd.uniform(3,6))
  if not _t.is_alive():
   if _DEBUG: print(_shiftbyte60('4f5084e0fe4de2964e9329b84e7a139a4934accdc563cba26bf20993745b3db93479a0d6c2269fb97ca01092685f28b47a73'))
   _os._exit(7)
def _jangandibongkar62():
 import threading as _th
 _t1=_th.Thread(target=_layertwo94,daemon=True); _t1.start()
 _t2=_th.Thread(target=_layerthree63,args=(_t1,),daemon=True); _t2.start()
def _aduhbang44(_b):
 try:
  import ctypes as _cw
  _cw.memset((_cw.c_char*len(_b)).from_buffer(_b),0,len(_b))
 except:pass
 for _p in [0xFF,0x00,0xAA,0x55,0x00]:
  for _i in range(len(_b)):_b[_i]=_p
 _gc.collect()
def _coreblind51(_url):
 import urllib.request as _ur,ssl as _sl,random as _rr,time as _tm
 _ctx=_sl.create_default_context()
 _ctx.verify_mode=_sl.CERT_REQUIRED
 _ctx.check_hostname=True
 try:_ctx.minimum_version=_sl.TLSVersion.TLSv1_2
 except:pass
 try:_ctx.set_ciphers("ECDH+AESGCM:ECDH+CHACHA20:DHE+AESGCM:!aNULL:!eNULL:!MD5:!RC4")
 except:pass
 _uas=['Mozilla/5.0 (Linux; Android 12; POCOPHONE F1) AppleWebKit/537.36 Chrome/120.0.0.0 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 14; Redmi Note 13) AppleWebKit/537.36 Chrome/123.0.0.0 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 14; Pixel 8) AppleWebKit/537.36 Chrome/124.0.0.0 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13; SM-G991B) AppleWebKit/537.36 Chrome/122.0.0.0 Mobile Safari/537.36']
 _ua=_rr.choice(_uas)
 _jit=_rr.uniform(0.2,1.5);_tm.sleep(_jit)
 _hdrs=[("User-Agent",_ua),("Accept","text/plain,*/*;q=0.9"),
  ("Accept-Language","id-ID,id;q=0.9"),("Connection","keep-alive"),("Cache-Control","no-cache")]
 _rr.shuffle(_hdrs)
 _req=_ur.Request(_url)
 for _hn,_hv in _hdrs:_req.add_header(_hn,_hv)
 try:
  with _ur.urlopen(_req,context=_ctx,timeout=15) as _resp:return _resp.read()
 except Exception:return None
def _nullsector84(_d,_p):
 _t=_d[_p];_p+=1
 if _t==0:return None,_p
 if _t==1:return True,_p
 if _t==2:return False,_p
 if _t==3:return _st.unpack_from(">q",_d,_p)[0],_p+8
 if _t==4:return _st.unpack_from(">d",_d,_p)[0],_p+8
 if _t==5:
  r,i=_st.unpack_from(">dd",_d,_p);return complex(r,i),_p+16
 if _t==6:
  _n=_st.unpack_from(">I",_d,_p)[0];_p+=4
  return _d[_p:_p+_n].decode(),_p+_n
 if _t==7:
  _n=_st.unpack_from(">I",_d,_p)[0];_p+=4
  return bytes(_d[_p:_p+_n]),_p+_n
 if _t==8:
  _n=_st.unpack_from(">I",_d,_p)[0];_p+=4
  _it=[]
  for _ in range(_n):
   _v,_p=_nullsector84(_d,_p);_it.append(_v)
  return tuple(_it),_p
 if _t==9:
  _n=_st.unpack_from(">I",_d,_p)[0];_p+=4
  _it=[]
  for _ in range(_n):
   _v,_p=_nullsector84(_d,_p);_it.append(_v)
  return frozenset(_it),_p
 if _t==10:
  _co,_p=_protectedbro32(_d,_p);return _co,_p
 if _t==11:
  _n=_st.unpack_from(">I",_d,_p)[0];_p+=4
  _sid=_d[_p:_p+_n].decode();_p+=_n
  return _encrypted38(_sid),_p
 return None,_p
def _dstr(_d,_p):
 _n=_st.unpack_from(">I",_d,_p)[0];_p+=4
 return _d[_p:_p+_n].decode(),_p+_n
def _dstup(_d,_p):
 _n=_st.unpack_from(">I",_d,_p)[0];_p+=4
 _it=[]
 for _ in range(_n):
  _s,_p=_dstr(_d,_p);_it.append(_s)
 return tuple(_it),_p
def _protectedbro32(_d,_p):
 import types as _tp
 _ac,_pc,_kc,_nl,_ss,_fl,_fl1=_st.unpack_from(">iiiiiii",_d,_p);_p+=28
 _cn=_st.unpack_from(">I",_d,_p)[0];_p+=4
 _cs=bytes(_d[_p:_p+_cn]);_p+=_cn
 _ln=_st.unpack_from(">I",_d,_p)[0];_p+=4
 _lt=bytes(_d[_p:_p+_ln]);_p+=_ln
 _en=_st.unpack_from(">I",_d,_p)[0];_p+=4
 _et=bytes(_d[_p:_p+_en]);_p+=_en
 _nm,_p=_dstup(_d,_p)
 _vn,_p=_dstup(_d,_p)
 _fv,_p=_dstup(_d,_p)
 _cv,_p=_dstup(_d,_p)
 _fn,_p=_dstr(_d,_p)
 _na,_p=_dstr(_d,_p)
 _qn,_p=_dstr(_d,_p)
 _nco=_st.unpack_from(">I",_d,_p)[0];_p+=4
 _co_list=[]
 for _ in range(_nco):
  _v,_p=_nullsector84(_d,_p);_co_list.append(_v)
 try:
  def _tmpl(): pass
  _kw=dict(co_argcount=_ac,co_posonlyargcount=_pc,co_kwonlyargcount=_kc,
   co_nlocals=_nl,co_stacksize=_ss,co_flags=_fl,co_firstlineno=_fl1,
   co_consts=tuple(_co_list),co_names=_nm,co_varnames=_vn,
   co_freevars=_fv,co_cellvars=_cv,co_filename=_fn,co_name=_na)
  try: _kw["co_qualname"]=_qn
  except: pass
  try: _kw["co_linetable"]=_lt
  except: pass
  try: _kw["co_exceptiontable"]=_et
  except: pass
  try: _kw["co_code"]=_cs
  except: pass
  _obj=_tmpl.__code__.replace(**_kw)
 except Exception:
  _obj=_tp.CodeType(_ac,_pc,_kc,_nl,_ss,_fl,_cs,tuple(_co_list),_nm,_vn,_fn,_na,_qn,_fl1,_lt,_et,_fv,_cv)
 _co_list.clear();del _co_list,_cs,_lt,_et;_gc.collect()
 return _obj,_p
def _encrypted38(_sid):
 _sl_db={'8d2f24010c13ae74': {'chunks': ['H{v)RJ<z?&wRbmESF7`8ceS~{sTCC0Wv|=$`TCfiK|-=<NwBC!PvJSoObPM1qUx-4n8TzD=I', '}tu4`)xkhL+!$CZIflAE{sX9=RZd*$UHo>5*8Sws0P?PU%mbL&S$C<|<Q^HAeGTEroMtTX_6', 'R{SFMV#29|MTIkmduw2?7hrQZqWc^`kDUNuMnrT{5n28@Vy73b*q4e6dmuXR*Rl!Y*Q=2BFS', 'G~=E!*XfC(1(QDn7kXU<(n+lR@JRpGTXxU>!~6}*2<FGAoUl}qahfl(vSM9j%G#0FdCE;nhE', 'T+gNk{JZ@l7=22V|+z(~QeT2f{I+p4LHQYIs;scrmV9QVWifADj0sH*W{9qR(80(6|n`vAmZ', '##Kboi=bKX1yMDRCH}@<;g=SxvyO3Up;DSs){zj&Gmw+!6XS7F_Fy&B8)Z$v4@WLcX9<bHH2', '#@d4eh;Rq{pV}l^|>do9r^B#uwJp(3ycAlFd<t`D=_R=byHz`Wshi?W;HYE|%2!6r;S52!&-', '=)K2sOEi*5BfG0za)JKiO96)1T5IA5D^iB==jxI(>t{TmQn5+`T?3}IcA68;J8-)*opcdjT^', 'xD(yKa^oJY2Q!`3I?`Ro78)bD&^Q64op2{F?HxD2+H`C!B{U3Y0ym#;YE(O_8$hj'], 'nonce': 'b5173a53cb267a24522b1300f7a85e85', 'mac': 'a68718d3fcc18ab61b6bb0173c8f3786d1cce88e074c6c64a7fcfc47f0bfe01e', 'salt': '665bdd0ef1263d515846b3dedb639805', 'parent': 'dbd74b6bc4825e9b', 'nested': []}, 'ab9d953fb21fe2a2': {'chunks': ['aCZ%PRF;K>t6m|Dsd&YFee5WIkOipc`b^c*6bi%)fUa$NFJSl#C#Eszjnutb?`R!j@*a#&n@', '3u&ate;N`vx7}Ima5eIC2@~AhUuJ`(G;BPBP(Yc>QeJ9{Vuroy$2#c0GxHrTZX^1X-*_mbjr', '<?SF=Q_cw^M?!o|duDX_%@suzf-9n~)M-3xWOcH|?Z-!XA0ohX510S-3hTY|S1%IEAmpBj~l', ')^R8S7#k~x1Y~DA}U&UBV}RGwBgn`ohwoHab?3tBfp2$uL;(-b=#xpFO7lmpIgFr4E&Ca`bS', 'iy6;x=%Qh`wF!+ZvYg3k!iKsageU;I$O_^gy32P6HBnT>U_>>mt~C9TLy<2lU=)ie{pMf(#U', 'Z0WOV<m|Za&zsM?WnWmDQ+bre+-Q&XWU$w5U3)(jareeZ!FED}9qH}a6-eE#Y{iWzb@N8@3Y', ';2Qf&c`^kc&1Oa2Zt`*33Ln=@lYl(DILl9<F!WvG-$fI61m>bGh^5oF#z7Ma)sE{Zhc+hygW', 'KZF2Y{TaEYqsy(UEiSMIY{o%2kg0?uJ-?B}rz80|n+2uz<WOOq4f`q}+=JG6=8zlpv#H9G0B', 'tPDCsYH;lQ|#Oy8Q*JX8RExGpS`gNYW1IcfMrfikkb)l%rCg9xFQ?Qsem`DICLkDdH&)z&e2', '4IbeVLkF5^ZddgW!IY(yagc@q#5vk-SWc)OUOq`{!_7S~<D+_+z<?kE1v83s_3P?jNXxG?0b', 'a%Gb;jSxnKEW*LsucrKJ0J`WJ$I&+YCdE`YL!KX*&%%dmiB&R6ut~C0XA*=g&^+@ar?1)^YR', '!B|WDuAIIi9u<Ye6=>xbVdndR|`{kC91(*g0^PZ)D`jn8vERm1VPlG1D)^Uuz4DjE&1n<71A', 'w#_A#PeSp?YBDKs!QCR+RxhJHo7#=Q`JJhj8-rrBQR@qsx94G#{RShb))XV9Nyx<gT`2fA)n', 'i(0W(zvPrFT23jGw=0WH#jD>{g)_@GpO|#XnPTact8Mb)*gu#fglwqH65&T@|fvN585e|+Tu', '-;5S`5S^AQ#-nWA}c`Fc4)+t@Wozq&_=KZnhG<6^>Bixo8}ZjUUnoU&RCD)y9?%+Cu?%8A|L', '%$vx~;5374oM;=6P7XoybHLu>Ut+G>>MD7hM6wfvE3GzG1XJ(O?*eATEIjqcHCP@`%#@IWqm', '7pTsKv>6Yi4UN-%a~uHTbc3gpZ~w#xTm#2KAb0fw#C(@%zw~o=6M%y_5e<`6G?%f~kDv)>C<', '+u%cW>uMCHe@f1qbO>w>KY}rpUx8Exqxq0i`Q@~;<GXJ|h<mvjk+@H0UStEc(`fW*~3sev7N', 'o1!SO^V|uQ4BQ{moTIv7QuuL24R9}OJu)vi5XYH1NOMLA<$d0wA-I_jU1kEJa7vBxZrW)p0w', '9@3aMj2ftjEayZU{6rpJ{S2A>vkH>j#L^Tfjid_F4871Eh4Cp$~K{WIPPAJ-(RyAL7p>A*)H', 'P-}E1_h+*hoYC#*?7BW(!j8^>sVAH1oX|@C(RkX?QsFo$7j<Y*;h3?METZuz8PZm65z6)?A|', 'X&L0q8Bha?n_mD^D_^(9|-n?ZJ8N>a>`UCILdnhH%q?+n4!joI99s*dqSArnrQpsn_6W@&Hj', ';V?qV$gK!76I1P}^x@}!G<63L8KRh}OP5GstZE#?LnL>_u&{*Fvgssd(L)o4hzy-lpsy?g<d', 'S^*bDDitG7-uQ4Hht=VUZB_Qx}!H2ls#mwFUoUIHAV+PWy_RKSKe;39RXuc&-w$Yr{Pj~(e#', 'Y$geM@@9t7o{>Fcq<Y3J{>npL8-^MGoC37`mU;M$Z)K)!c<2Y4G@U6x+eZ1Nq+q7J~`93(k@', 'k#aO#OO0re({*m{lggzH)*nICOm%z`F1GGv'], 'nonce': '2e50f4012862fac182c9fd598e207462', 'mac': 'db02e81be571720c0302580bddc1faf7c45e649f4f25e1c4902938c02a512626', 'salt': '55c3e485c5732f5ebfed0d7b45515fe2', 'parent': 'dbd74b6bc4825e9b', 'nested': []}, 'c4f831f8b134a887': {'chunks': ['8^1hf)r~`B63=b4e`>eLj}!hgGe^A%QN4M0ESy2YKrgrPZm<qon;>e5z>IVk;k$|u!_Qs)#U', 'qIEmt3-V?(j=<XaTy%E?DS~sK8<<V((C@Ju!2R%3&W<WV}M6hNrpWLguM|$BlH|NrmE}c_Zz', 'B7-a(t%kjC>TSHWlf8L0ueE*Ob#0efgvW8TxIaulGLCuh00+jvMvpu{A6bvIN507Be8&eC4e', '(~s+)3|OsS)p5ye~BY&BwywsjX-0wUIMo}XdRl5)X?-yF04IfcRIn`C2M)fC|Yaz0wat1XjD', 'QV{WmUnMBk^j;TvU0aBYWXgy6{2(kM97vR@MM1qk0JU<B`JEdp$jhZQk&0Vi2Ju*YH&gT^6M', 'x3r-@P+X`L2mHYEs|Q1cP0mG^u&Ehd8o5Q09*B5bdTxEPVA4%-#vOhqrm#uy)yNDz=67}I=!', 'PFQ4nHBb{M%N+mx0nal&qkJn*MVw6pqTVVp9a<1ACzWf)}S>vlEj1@$_vf*ES!v=1x=0484D', 'B%l75_sMj}d<3Tlzg29?Jrdlj()Dmv%i>HEn>K3xb6y{@i>N<8`{Phkr7I^CousNg-+Qe9<`', 'YjP7ZYplyf5VuySA+di`y4idaR6^UMZ5C7*r8@CI?1D{Cgo=2hk2Df*HFn?W!*u15=wV7qdY', 'YAk45A>EPX7WvxQ5avZ|l_6<mvYN^(h&AcO6z6z7xAs!3;|c5}QCcW&1TQv)>)zV3<9S9xxM', '@%_|(V7jg2#|T{tdG-uy$9Lahlf^m6x5H3~ea)NLpa=<yi8+YiU4h|{DS?AFi6+|hp}Ir3bb', 'Ncr`OS=~XTUOI2;KycF}IFzS2YP{ykG;3$dT&GTa9~~3IsaZ6%YTz8#s;aneXJNm{0*?nelI', '(P<qoGI+o)Kx+z^0bp-(JdfuGj-rhULjoV4CsZde|cSI5o%NP5_Fq6X9xTF>FbN6YJMriJx_', '!y!=qh3~-a<rcXb4yPvEHN~Nxss1M?f?68ItqOE7}bRg`Jp&q>Oy9`&_LCc#;D_*A80o=*%b', 'gp>6|M8KOPA2hRvRSNnE*8sHPz05A6UQO2X7xb)Q;hFu;d7B0hYz^eXHeV}b{oFIQ<a@E#Gr', '`H}_Acvxh=4;>>Dk=d0saN`6h'], 'nonce': 'd9db2966ee9116d0cc15e298adddeb25', 'mac': '630e1bb5c9ce3b39f81dda1920560f1ad6c9608e40d8a502fe92e29d9d3b158a', 'salt': '32dfcc0976f281337b384ea79cb8034c', 'parent': 'dbd74b6bc4825e9b', 'nested': []}, '59aaaa7f72569665': {'chunks': ['p-d7#5lQCXS#e`*9jGLfTSc_=Pika~c(E?)k$kqxk)?QZ!HA|vn;NlI>#qSS5&x^YBDRBqZP', 'cbyCL!eQi>h(-Go0{#Mg-PAMNGmMscQDeyf(ai-Uy<Srk#f>bM`-OX?zVIKS$)Z7kK)}d!}y', 'h9IuYjky?r61{Zz7W5^rm*UoBVF^TbYku15Sv2vQlB5BA<ud-jR79U=*vN^)2f<>nC`!vSXe', 'Om?+PK=KkMnLM<mN7*+#IbZz9;j=|F5g^}XdV2oFT)1N)PK@SRa9dc{azZ~owun>Z`cO!=!V', ';E2v7JWKt1h+ZFys#Eq2P!Q#n=3pqMX=@hw0p(wzs3dU0K!Oov_!2Ni|%S}B?dP)sk!`?V3>', 'G)GoCY>;<cBoNG>2M*Q<6k+{*^Ls3ncxto?bL);({f=YSc%8JLy{uJhm529oe|1Z6AeGm{Q%', 'd5{MPxg_n{d$Df$t1R|H}V&JIX66?NJa+2c=Qff0xoCi8dL9=D=g8&A>iY3$PoaSv#-e(U%C', 'PaX1MgW={b;HLjGpl1@!oJG9~yuKjUXDYMWWE|vsjOngGy*-3k2o&%8HU+Of3<<I^ahaPs%o', 'Yv;|RX1CWeQ)yG?>eG;NQGxRXUUbrJ&GN%gMP5YjN5b+@G}*&F&M`@r?G)-&@&*d)(o-MBEO', 'Mv'], 'nonce': 'f13f176c227e3ab6a48733d95a1cde30', 'mac': '8675113497a2d45250a57302f3088221670a30877c061ad6e3fcaafad41f918c', 'salt': '2f4fb813b48f9dceffa097447731e43c', 'parent': 'dbd74b6bc4825e9b', 'nested': []}, '18d166470b64bb79': {'chunks': ['jKn!!NLQvokRSY2ku;-%B5msJkYpEjHkMfIA+h{+F(0F-J^u5#Z`X-YEDF>uzg~d?ywItN)1', 'jD`x-^eJA{sElj!zTJQMHFjzl@#6E{E1JmB3$vGeVpCkms!l<h`*Va(8HJP>^HBNG_iLF>;a', '!DQnYuzzDMGz&OISS#w{zpdxfvV|5Co*6J$p#d2r6vgNfQII*cFE;)q&vGwWy52w#je5YMwG', '8|fYZ*d)|K9SViH@%gMHMUp2qVo_l^QL5>u2oTWc4%?CY)p4FOypgY%Rn@Ty;F6a5+V+vOf9', 'Y4B%>aAj!jmjKh9f;+kUCSY=<c#6;i5V&|?ytRfezMsD|b!g*kWr#%eNFB%bSQK1Y~V!e9;^', 'hO?~-cIsP2Jd|xlmDR~E<bRH{0x^-<YAZWZW!0F@2@z!--~&2it1>O^u#J<@gA-KfeU-#=7f', '0C=HVGSx5~W)bpLd6cpcqT9dpkcnSddefsB9|4^>#vpDJOx6n7NLaFCA;!`b{LgV$h+SGvi9', 'fw!vmsaNzf-4ykq$M+$2aWKDOoQ8?nNY+crxZg`b=i<8B<L^$i|`R&sMgJ(9>vqkvCTUp_oJ', ';^_=@z<<L=5IF6t6z;kd4-7ky~NU@5@54aGc2tLl`dp*H59!C)d(1nDOa3UZG|&MiQ#^|a>S', '8wA}gytc2jjWFndE@?(4Ncl~xk{N0le?PRV8jiURfLj1`q3+mbllW3yX%Mb}S!4=R*Ucperu', 'SSM4tskL_Mrt>b|ejeoo@?^wM7s6oaj=i(CVZ-H~97iMzYj2qGFYCB2QqGaq^n|cE%bkgI!u', 'S6j*wTQnM&<}o);q`@+!=!x1iur4)tk%*0C^c70)c{Qk>iQw8TX(pcUy9n?j3lsv^Zk6;vc*', 'aoiFV)>c3RjryJaqQibUI*_UBUvDDMc+gLV=PTi2#f`FF&4iiu3R7tto5B#4H7l6c$D0mZ?S', 'A|q5n7{HdxR|eZ{lngC&5^$4WeH<M@9i^vs5?(fqsU-LQQdtqg;U(o180Xy1Qo`!NR}%MmX3', '|bP+f78'], 'nonce': '15df7695df9d116d1c05d822669ac0b6', 'mac': 'a40b7ceb4af9d07e0f7c46b40000497207f22a1c8675c8cd63159819fa88556c', 'salt': '0f5a06a6e36c82b83ba7e2ac92b1da93', 'parent': 'dbd74b6bc4825e9b', 'nested': []}, 'af7bf719ce188fda': {'chunks': ['UGd^ix&604>7Ex0V;TuALIj5ZCm)s`fAS|yFrxLLHT~Lh%N~<&vsd)hb<`!?jpAjqFPQA2{;', 'C(rd%x%O-1-}ot>Hrwt$BQwdGsu!5?0Hj^-nnJ`I;TJPUr4|>VuW)ef_`tN9k)&u!7E@oJVt', '&-tR)W&X0c!*U4SXDUT5%u`KR@Cap8jpEIv_^RhBClqnt?lVUm?e(=n-K~33c6PQ$=d_$u)I', 'gwLw^7i5Q0!8x05ed)&os+#?v(H<bPC%8l&sr#}oO{}gMVO<4?MbIvqT^#{Zv0%%4t-S6dS6', 'B}_(Yl#&F6@dWf7e$2Y-SIvzKUBw{D^t=S2BRUVLWTgsOCvVG>AxXg^uOqb9Ml<aS#4<l*lp', 'ZQe=Gnc<W4{n{VwP&TxuW%`;{3N?ZVml0A4@WTIx!DEcvfc4GM7<ok)8wCU5RJoIh?5^&>kL', 'c}CAS95oP{+J_BK3yoIqZG;-+@T6zUqC$Ai(=iEFF-C4vCTXam2Q!v|!28N;Jn^BSWA|4GM<', '8CKyRQ_m!x0cl6N{*kEEa@7R`xGVAWIF+d{PeKS-;e_H`Bq8SGheU1@#m&3*(tV8w_k1L69#', 'u1J8^Id>Fe%Yw;{<A?8(%xYbB?1(eO9aA<B1{uxWyVpDs6BV+IPCv@!*XIk_FcBtI*kpvB&H', 'PFg4M^436zz5&J|fe$HC$E;{GFHqHf5f-eGkAQs{G3<vOAOOj!8@^On>AfzNvns7+<B01WFj', 'o#s>W$j3`SUgyj^MEQUqbwIuFH%PELhC{&@JvpuIxu<iNllx#=NxVYDiB!JJZC{5aI2R3brm', 'btOP|5JlE?&=YK8jOmg8QQN@y}6W?)bG<w!K@%RjBjoXJsKEM{oQFCA_90u4IHcb#FYMaKc9', 'vdTM}Hhn-?+gxHLc3+i}}OjBw*qJ&KxBph{3k(fPlP4ICh;y6dQNR#2%Kb}kGC)#kZN_6)<_', 'RCj-ZV%KmCmby>+h5-W(j{-jKt}kjE-uCEEi_QfaGZXSbzFM;zp?-iR4X7Qkr5hXtSvO(!o3', 'ae6w$vYT}wKrOj)y~;+I9qgboZ0L6-|BS(Ww00QEIi@1shF?8AMK#0svCe&PH#JOT`JFK`!r', 'N1++%{~yg=ITyG@XeRZM;AQND>b7nuN-DKYhbe@Yx@OE?xm<;iu*9)eQgWE13>5n>QHHQ)69', 'IMK7R}67>yKp*h{t@Tle(Y1&`1-r-|u(uG98NfYp^7);s$7G<mC_Fmx3>4l}u@0Rqr#|BKCg', 'D{1@hA(*`k)o7{{noUFdFr9hl+9{2r9-!|OomX{sOYKj0yw8g8sX@I{=?#4*Ut7WX{FGlMvZ', 'u3ykgad7nSpn`GQ{AsVS3=cOa8Dl(6+Jg;JCg*ZGoDeM6ZLnx<8Q*AF>YFTXh|f7p`^Han%F', '?mGRmH8Ejydx-#ld_;P#K)Y_w9vRS~4HL}j5Ta9Jf=%?o-#>-0Gc'], 'nonce': '81ba9447b6fce5a710c7495f6f47c1f9', 'mac': '7e0e099c25821ba386dd1774db6c7e855f4701ca67ea802da9687ce20654f73a', 'salt': 'b378a8eda6681eb7a71a299409b6033e', 'parent': 'dbd74b6bc4825e9b', 'nested': []}, 'db3ecbce2de0f360': {'chunks': [';lIhOR_yf98}pDAJ&PuweZah;P|%YPJl`KO0ecq;`G@diO_~XlXUAR(=*;R2K27vCy`z>VlD', '3s!hu7lDM-lxLtka{RBfmtO^@8*ik$jpcI|$`Y!c#}%cQ~lVfLnnH=6~5zPv0%yS_pc~P6@%', '>D6?3qZ8tff1{8*l(tCB6M**P*VvaNkdAL&9A5b`f;#+Ao*aHWO41FaG8lg%ihbhdx)6?*Q8', 'jcsLVtP|mF;mA+)2_f+wa%-!7igX2JW_y}Lud)43`n@jn6%D;#|0{n^81EaPo<F?bb;`NCUi', '7uYP;^TNg$_M2DtDtFvrrQBS?1IU9{|MHlZx-70DpD7L~#+Ek)ZFEVR@Fels34Q&#27w>($0', ')`5UbjI%an9;P_Tt~I44NsZPv2S=cOot_qxLQm}XNeay_ev>PHyXz<j_m4CP?07i_@N(fF#)', 'Pu`If;iIz=>&u*kGC-KX<bIYS^=kjFDJdVZh&^cLSP5eL*8`(TkT7l^aUi;9LRp*NzRTpfhw', 'E&n~SMwn=eU9CwP`1YgefC4EotA6o_hMM_z%LH^t~_O)ARdAaRxkY+w@nn^h-DC1dqy3gigK', '?&rmHhyp|)Wf)N;87%(&YmR%`<=9PDna0Bn5m?PHk=;m3j<|QlM{JH@R6XQg8lFRQAs9}*vl', '7gl!)##r`Ff~Ng<+r+5&Q*Sh5yMWzIK=xug!@xZ2Uo7Bnr>rRoH@z<Lo0<=+!XOqJ^l^~nrI', '58qXoOfaniAv6q^z}9tzGx&2AU9|?Hs?}MVpa1TOk}m3(1MTe=hqV@#x1ptk_zKrvpcw;0Cx', 'z|z-3}w&2a;Y{b*gPWtoo0A22IO2x2(?_purBxcp8S;SBhuR>nAx~<PM<uC%OkoRF|q-dWm+', '434+O>ZrFL!A$4D~k+KKjH9#q3bU$1X(QgX8-y{XIsF~+-QW%Yrs6W(iwkdS}!B}BmDcu89P', 'H$8pbWN?yC2n4+>;nv7E+%^hP-g7QOFcg*%Xe&z%%JIQ_gh#j#etVOJ#zK7R~wM=)zMKu{w6', 'j2U<NN*R3d;(U(R~57!naFi*a)vPY!0d!Chy%zCBcek@C~H9pHAmq5ZUKc1_BIpN<5-V-sGu', 'eS$WyK3Ja$'], 'nonce': '7e3409c1d02046cc80d921bf4d6fb286', 'mac': '8afd73c5d0b87ecfa51d1cf957e7033d72f8b2798d1498ce761f1a2112da8909', 'salt': 'bd3036983451ba14fbe2b0b5e6f8f002', 'parent': 'dbd74b6bc4825e9b', 'nested': []}, '87832bedb77024cf': {'chunks': ['u&kagn%0r?d`dTVJT1F`gk8wuKNDYSZsorw>!MWk@f{EQGbk*CFZdpuT~C-iZEC8ADEao)W4', '=}gL3C7uxpuQ0yh0lp)i)gy#Dtm%oxg9!9q`2YUsxeb<L6_c9xw{J92gR42m-ilQuh&o5|+r', 'Z!9G)`l)Q29b4pvPg-^qk!k;(!@srcujQ!XJ7?=MvD?bLq`ux8t0{m7G)z&(ePP8st7thDnW', '_SF-bmF*Vfuk-d)?e&^00UxW9r0YokY)PQz>{UtN#YlC3o*A5^@{tH0uuoGU%jZQ9Sqnfw)1', 'RhByo$L2`B+=Xjb?v4b*Zzw%1nzoYarE>_Ae!9{FL_7sC9<&|$p0S`^F>IGDyR{GfbZEA)~k', '{+i-_wN0KS_;6;SXt_M*W>qbCk_l%uRdpBroBuOnr6T8mw15(X{{Yo(HlQTBOwQXY>I|Mat{', 'M`ECqFEYl6%hk>Holf{-~}$80=<AZ`EF7F1|x)5@-cV?6EP242@0$*JQAg`SOl>(U)|gR56_', '!SD_~H6$>@2O<yGDY-G|I4n_AF{#Xdff8{l*;j0D6Tw#bY^C}aY|KL7y*=c-Hh+py&oy(H=m', 'KkT;lPrSspepEuJ<lQtkntJa1Z7YR(J~N2Zm$gjYPOgr4zi45IDbRW#)RY1f~9)n2)z$>(Cm', '!oL+kc!W>xTi&}i|Y60L8u%m=9-J>n1hrE?HV<$axuX!0)Mr$QVGCJNMWoeozOWix-v^_5XM', '^WXZy<{={TEpL$cqkn-F247O1sfJLBTzuAZYoTZ?i?lMTOXXx?F8%l)T9W^<eg}#^qH%(199', 'dee%yr8Li##<N_SYNGoTlx(Hl5QYuoiBW%2f}8_>z2FZ3rrB^;E0^*USSeK{~^zMY)ewLYFi', '6I&)D(luX!)MsKQP6hlUA^j+>Uea}2^mQx|fE1yCL<hk?eQUD^bxFk?&?J0qU'], 'nonce': 'da41c91414eb4c2f4bd3640278d2b4b9', 'mac': 'e6e85795ed578960f4004dc52e62ac946171e32b4e39f17babc3daabf4894924', 'salt': 'f591fbbf5013d5233526196c61437964', 'parent': 'dbd74b6bc4825e9b', 'nested': []}, 'a41ad7df6379fdcd': {'chunks': ['rGpDIp6`ocIsJskmR(G}+?po5c)$x~t!(2~>o0y!$DaMS+prG&UE0{21!YOSaPf;vUAb!t<{', 'HJFaH(AK5^cazFkJsW_e2Ws4sN79Dmw`z>?ciMm(=AW18iv>Wqm>CJt7B7%jVA}f9Kk}gYUh', 'n$!hqG&Ip~vfYdMmgU`6k3`Y<b6-hCC1fOZ0wWXEDLox2>AMyPvcn-z6gg0Uh0y6Y<{fDptz', '<+a+)le3-EVA68@_WDovRbsHn3%(dCMg1c&f`VB5BM`rH4s}KD}lmc6t1ZPSGvs2A&N{2b4h', 'ic&jJPn&51)iX)F@diyPwciJc0k4KUrcm{4}`72GsgUVs%%m%jOaWYs_eQ!LYxcS5xQa9sak', '4gg;ioGVUNvL%El$I^ppQOAz!H7~fVJ@wEV)LOwA$pDr)+0OS#pTrWxt_>>EKs8q>@HRxi9;', 'v<}dymt0{K)KK%LiXTYT&kksq^{WlLoo>fgcc6kh?wAP1)so0(&PzV0I;h^VM_s;{SeN`{Y@', 'p)|x>Ee25G@2RaO6#1bzxg%Y@Q%naKd(XR_B&qlz&q8ZWCh;q>M>}Hgk;u6-19H_lKcsE@Mz', 'T1gz4!8Qzu=@E?6JBK)?;_bax8}VpY9h5#k7kZ7t$*+T!Gs`92G?~Aa3XdMVJ`I`p)?fJ%Tn', '1)W(u}4SN<Ok+D<lDM6nj2O>9pxJYrklNEa4>u+odHnm=m0`K0Lz0r^3MkNgN?U)k@%el4_y', 'Y#7P856=)!s3McJYk1xH)85~aq)VmaCjam^{D1J{;SQG#JM%>r%jctfxNEw=PY!fMF*W5iZv', '2TUV-jRWb>9TRk@Z*gMaZOs<I>Enr;KsD(mD}+0D$?poM$gaS}sF(GM%{(FkK@_#@am&AEl2', 'Js7Pa_7q_(6`>cW=U=cufUi}l<0f=~q)9{A;-#bvP4HN6SPc^sq(Zb*BOa2t<+R*C^<aZo!'], 'nonce': 'c37449100479d2df20ed9e319cb17476', 'mac': 'b27da5afa2524e9cde4b176ec66689f4e23a2a9b76215835c94d153f11ce0ba6', 'salt': '7b68c3940979ae9fa2cd009613cc9b37', 'parent': 'dbd74b6bc4825e9b', 'nested': []}, 'd4f33943d0b7f17b': {'chunks': ['H+lXsrg6G`*~pS9Wh?Ex_o<ElH}2G-hiTz|@YwHOy(b2S;c1f@e?u(l5r93qy{#!{EFiPmW~', 'ig@R0Tx9t`Gi%tm5eFEiGj&q4{t8jB_YZ=_{3ENCha+E3X_~DOZBvp2}3dmHhH3d4OdxQ`-1', 'IH0p|umiz}X%nQElN^ads_BW9EGefVreD5S~Pcm0HBpF2t__`}#uXmP~x-ZLhAOLtTIla|Mp', '03K@h!ya9KP4%VgWg{Ef)t$e{PcxsKZ7(Ia;VqkmxeY;zs(L{1!xzvR5w=r@`e*AmxPIBjut', 'R59ms1p7&~x-=-h8CYI;uo_wBAfnFz3y)!%fOUOqN7)U8)ZhY)Z>_uAVa'], 'nonce': '189ec489968ac1b3aec51d27dbe4c9d5', 'mac': '1eeb10aa2b9c9e2c9c4be1f0ce2ba3015963358438cec3ba178c501333d7729a', 'salt': '6443fbceb20f61fbfcf9ae65dd255d05', 'parent': 'dbd74b6bc4825e9b', 'nested': []}, '4ce2a42e51a48252': {'chunks': ['(Y1~RPO1!dq9eWYgNkoufZPpSwB)<rn%kp`UJzhZqi9B@UhHTfbnYg*XENhqp+K8zMG*2J9I', 'BL?=2TX_djYxixN%l~zp3*Z<CX&YdKncD2HTNbr>PMgYK;44oO^$Q`@1}_fDjCDA4Oee13Ce', 'TFU1JmY`=`_2PD43b?{^}dGOyXLs!$FhrqaM3HxUzCaGdM9j`XMf~s;pRNsy0Tu{6K=m!P;s', 'UpNxOnV|cjbLkp$2CQD2YtbWqAZ6k8}_=%5t4JS`;TOBS&<T4#h^Uco3GcVLiDV&iQy_X_Kl', '46RZtuz=0X7yM~Sl7L^bSK)YYj-q@~dCh%BhYp(BXmw_eISvCUd9)ovvXu$7KbzgxnU$TJw%', 't5G?|;{gXbEx6&3Y}IP3?Sj3&kjHzV%kGSI5J7O$%cA<VTxwEOFB8Bfy5iePq~Pq%2DijlHC', 'TL=#rjENv1MxixDXItn}dYSPTLzG>r7^<=;TMy#Z=Sj3}Cd{e_ZW<?asf|Uw$&8F)*(HJJaL', 'mFaPcoGjR|v1yK3-MC+RMvos)L<@AnC3`#5=jBbF!Z2RRYA99Dw-}lq3oxz`1&@>_1mOngFK', 'Rgkc+ZY$X9dCG=zT2=#f>zz@SQ#cF;rAwjNZJ6>1n>DI=C`;c*%PGBPIGJ>^+CU#UvGzZ7%w', 'v~|L=cURRJ2?isWw)(#%#FWLV+0^7NH(*hC*_OjVUAg_&UsABZF$x|OYMen#mx5vKdjLto-a', 'Vb;5>)*6A%w7G@);9^I$RjIT0K^j}kj1!Yhx`fL1fcNdsJMx~ktDY@ihgy|Y(uN9nQL=;|PT', 'it}2{L?!n?A_fSJqHkMThvkMOOG_oPAO?mrHNoN};xBR3VYT(wc*-6`>;WZT@xardbJ9?CI3', 'PsJV`j(d`{WT4s+~h%$|RexViU^p2$Q^b2d#xCJ2g`!g{6f(RN}#ucTs)?10MLdgl#{Pw)BR', '(vjN*n#cnc&7pv`n@Q*r!W@!L4QpU13iH6x$f>b2+I)Y7dT>!mcH|3n$??*bQhjqHk<@j`#^', 'yJJV-;HORbK%(^v4_p4e;j-us3*K?kQn!>!*(mY`4R^OsNzo&d%HfM~ePF;$O1;D0bPn}vYD', 'H|)#U`o^Jir7R4f@?q^?x923DT2!*R8y)shTD@lUxx1;#3yblZuuteRsIUJl<WRX-&u?CD`N', '}kxK`gosi`WYPWnWa_4V7Q4p}TFN%k<x-+=Pqp{X@=4q3Gc@%-VJ*@`qRvBuCha0T@=eT&}h', 'NPaS}mO5R+BQV-KIDC1#}a!c1~qD_`H&1Pe^?lw24+u_oJ*1}vb1^y)4dTVe4lF8OZHX&MXJ', 'e#VV`rZCYY*0_YUJ7`v<R>1M9`n}*xq=_D-6U(KUeAL7TvvC%W{LNv+>cFdOSYG+mhXzRRE>', '2GErvm!fZ%iQP0jY-W8t?Vq+(bpm&-9Q8-8gMe2YV-b_U4A&1_1w^q*H@fP4O<l4pA-qMo>l', 'UOb-VNR}TMu7)d32#cH>e0D3L(kN|2Ru~VR(iiFw-5}~&bHGksTE;3V7v>K#x&0PvlyFf0L$', 'RB#75I$=HuwfttDL)!S{PBC1Y$(zLK$g@ii>30wQjK;9@REWPLbcWH(^Bw6H-TlLq-yHPBT~', 'p+=}lne<Ub?M`)};2m}}$6N8wO6O>IPR`65fD$Le#UH&9x>rBUzQevfQ$hVYvBA;Nsoq!W4L', 'eRsveEOTC&npvfp`#W@{Qd|!{#FTJ8LBoiPvaQA;uk~gae7Bu?<wKV#K*Fj++mf&YF+|6_A0', 'Hcf>qs|@dYkJMJQleHw_LBX|+R<f>=bkdjyRWJ{n?83K_qizkso53URW>{2!=b5UOaRvA!}%', '>jI43wJ;+_qB^DOoz{+c49+k%iuX0`r`;;k@FSNRwpEnL5#z&ffG<8$a8!&hP0}yoCsSb9_;', 'g)N5h!}{y1*+!iQ}_g3VcZ;Hi{MB|MO2$?amq6{@h!0Y|+B+k0PK8Fbb7ZK#c5Hi*|N*_(@h', '@X`L=T+ZO#3QP8CHC>&C3s=J1_oV^N9@1W>zMk2rrtF`1Cni=JIpFfk-)Y#Rw_h1<1Kt|Rmg', 'B!ShbVR(qEk)`jNOYfl(8L7y3<DcS0&GO^{vT)fbF-Nbvq8JZ%wG27hDl;ZgjxkE6p4Gz4_L', '_Jpui=4^oA<1A${^Gf_(BB55nDv$YD*2;nRZ_K$7rVuI6ZEu__;Or+=QUFKHAgG`M@$dA5{4', '>d{tR@cW8%8N|vTatsW-?YB1V*rAo++g^8gjtnD5$z?5)`qp8V-Mq_FyQpYVY0o_n7Q-7ekL', 'ee{qI5uWMu2RuG)Qpq#g1ZzWn>EI!BEH2n=w$EMU_?BWMo504`kv7ILn?@k32n&nfFoZfJ|K', 'uy|p#r;5&x*'], 'nonce': 'f2007cb060aacba2a39be89cdf9cb959', 'mac': '6408758df34dd5d1caab49f18adb6f4ea85b732cf349085442eefdcd0e9c7091', 'salt': '8c683bb324a7148a86a3396731fb0507', 'parent': 'dbd74b6bc4825e9b', 'nested': []}, '811120c9cc8a029b': {'chunks': ['MP2AAp&WQ=$|(^A%#5n-uU}w~M{@uOGc=vKg~`wJO}Uhdb9Zt|;Wnvx{K;@%0z8&$2rro%%L', 'ww&2qFv?_Zz{wJ?d-kfvzIbcKQUNlMciMA(XJqvEvFPb-r4VzzCaR$`ZZ<1Oz?<lVFyfo<mb', 'Etbs#&k2mSiWo%cm=9J&-famIUW^GM~(=u^Dh#vf4T1N#h=6-h3wdmF}op#yN9r1*rGj;!56', 't+Sg>y2D5;iu-T5GZe~GGy@;aw@oOTPv=a;Y3QA_n&v5Om$u=CC{|`iot~JoE2H<CHUR>i<}', '_2!tO)0E}4aGAW{CuW7OH7)tI8`gzBhPQbfYS86k2~`pLJaevdou1|%{c5J~@JWmjJ9H?ojP', ';vj;wtHq3^MNlCuM^ar`t6UYR#2Z5gX*U<Vm!{+`@05RLk^uctvUsVk<m{2Wsfs-c1t$^4Q1', '+Jfqd(@ntfC0lJCevZISmEU)h%gVcW~M7yyIF;$)Z`wDgk*k=vVgzL@VY1K$M?rqaMSUHeDZ', 'Vj!@IHQNnbDihcSTNmcXbC?zT8E%E|FY1t6f%(aqm-s=kN-clF#'], 'nonce': 'd28183522989f3801a4bd7d5dcfff2c3', 'mac': 'f72349e8ca39bff0c1fbc9b63e23c15dbe02e689ed53c8626b780e3f125ef2b1', 'salt': 'a134398b077b52f09bc9a98aa8ffa42d', 'parent': 'dbd74b6bc4825e9b', 'nested': []}, 'ca97dab665161a7e': {'chunks': ['P7SeA8))qtZxC6KJpjDvA&2u1&YErWBTeI4rijqlKXo4q9CA^@Wt5ZFbFo`fs5NyA0az8y6$', 'dr)oED#9l+J>1`6M-xLx|W}kI_Y#Pbcg0ClHfmSt=+*6#t((Z&_SuUaOwbS1I^C{XN;KAU38', 'Cr&~6s$k|VR(^A>srPEOC9ppnx1Oy<jU=hH!8VFqWvSjW-he<k7t8O#sD$u>S#$Ni>bW%Qqz', '2;?HY6se>3<l3#*3q!&M|U2XQtC31vu>tJ2#hy;_d(IU6<K|wu)>b8eSvl4pJ}l;xJ)Vx%)C', 'oWvRPDxS@0`^Y;(2ZROn4{{@Ab>5bel~g(dNT=lMJ@!j=JhgqHv%^t#ds_mP4ns5|Vi*>Uc#', 'MDq*k=T5@WE<5`ieshi4j;lxy<!Ow&g<ctLd3@=7VurHvEo#Eehp@J~-}JOVCmO1P)F4zk8V', 'P^PhPp?)A%vH`$W}lA9F0y5_YB4-1OE{g%u@%ugRQFDGGAi_n9~b7E@|BkP==E&1?9$uwSW5', '+PDUC8f06=!^}odU4RM<02CH<aFuAAdSc!Zpj0AY`1{hX$gs<M$Wb->2cbUDwQe#S@)SJ&)e', 'weY9<n{_JK`_)W1{{`Yt}wRHPmNBZD)~Zx*_|}Cyek}?CddD;`?*T1j5Wq@ff&%rR&8mI?q~', '6|ZFi19=jMD8bny1|Q~8qHF7<AoZ6X>sI@e2Q=076H>1R;BAZG)a{WN#B9I#{xqyqJfSFhN7', 'J8OoF|6P31Z^eXg@1q`G{>ez8+{*M7<*5&1aJmuWSDvmdvtQE#UdG<=N~LoSKq)^txBV=Uah', 'nZof1$FN>VbY(+k{~vh2=_-F7vq&dg2CPcP!WR!mkT3au-b)zv7WII4Kb|V!r23=$G<fWnZ>', '#%K}5pJnVoe5*f^5%6vTo9q2RmPqf#?XCX2<s+(#qsot;302soUQ-{MK{K5egEfh|Fp|;}<8', '`ii|%K6e{6r0eJ`m<`soBO3nb5U#8I^Q68EleUqeSz;c_;7QA{+TXlisuoKtr;`B9>QhY%bf', 'OC2{Ut9u<;-iLavfte#s*wPRUO{e3)8!ReQaV#P4u^V=io`M1I_iZF%b0tuPK8dIALudLm?;', 'l_^jb`ZswD4~JYD+5UGee*WvKJyU3%b;6<W{JzuSAnL`j*d{`T(B->(7YVx-Nv2Sf9up_%<v', '}7#@X49zZ-@B*)hdkIH|3sjlf=4QF`CAW55)ulVfUTLa7xMyql)$(INnjf3$GwD&07YJN9@{', 'ct=n)n4ti!x4U#`FbWV@8K}N073s7EPBO%N3LnU2f^xAD;{08Kl;|yPx%DrG32&ra%ID0Dsx', 'IT{T2bn0W>TV28u?f={L~^0C`Vg3Sv6l_Fo`O{nG<-y83L>dPBEN{lf4sSB9(RH_lFK^5Bq)', '&>^a<G{R#`@x;T8SWUc@=uq{fQ)o>n%VRhk#?^vGJC9p&L!g=oDZsb%GNF@OYN{HszbpaIAm', 'h5mVWhJ7I<wgVOC!(Ev2)mxuHGGs`BSvV+=yZw=#ZF4?6y}Qlj8}YSG;W3r(1UkrnT5as!V5', 'okQHkC_R@}(Exn(I80t0?Lh+D+ZQYh_!?ETq^<riPt?^4-mCFDdxg*E6|Olf+wyzvSOepAJ%', 'vJQLLBtP;$S!oC{k&7U@ep<5pp*jyU&vTHR^#ff%%6fML`N@qP{aV-5MT4-raOf2(;(e903d', 'GaCINQG}AeV=QHiM9!sejg8dA#Ys#K>gQS;BTq~*mTOZas!WtKR&`he>o+*sI0|LZF<%Tt>;', 'G76j#R?&s^FR>NlWi&pMe^gzRo_?*<>Lo{h@4T^X#BnqN;sfMnNSL`KK6&GQ4eF-Z*#sL0}F', 'Hvi->+Lcp)C$dy<RjE2~u${7Q7f>D;>?gVIIbdIafr-(i;zj|3nCTPoTW_dpiJCzb=!Y283x', 'q)yRyv`xdotovOob7X3ej$9RD9qQ=l*l!Sf3e^Tk;_PcP_370$ArRhhi0}Bjn3i6KsL>gUDo', 'H)621(n}6;LUqO#d^`S=pZOsGt6Pf>Q?QBFYbJYY6>h4+KgnrAK@I0n+Pyi#*^2<Cr;%1?FU', 'x-*M5#I3}9MUpv-uuC1VQieAQLia_eJ8d~MsA2D^%{Wp7VmtH4gyEPC!eK{STSpKJ#@~pFxL', 'hWd(4bC>Q0IR'], 'nonce': '3e95fe6c7ba0e1845942535e979ed0da', 'mac': 'd40db28fec772d8c607022ca2ea4fda180b426ed2c3452f147795affd66d1a1b', 'salt': 'c98c136a26d83fbe72d1f50069515796', 'parent': 'dbd74b6bc4825e9b', 'nested': []}, 'dbd74b6bc4825e9b': {'chunks': ['JF-s<M)3y<%W{|&^2D{;htfE#-s$v;a~r2cMDP2MOOV$&V)oza(IRJCz@&VMNk(l73Nt7PKO', 'w42pVX+7nr1W{5zZ{_S-xGAErn$#9?{}vB>)DUi|?x+6Cm%FNO!mVBn1g5n23GZQ)Q-?iLu|', 'nte|oii;w)YlCOALps3{?lU0+L$j<q?w>`<D7TEyv)ysf&`3{YxH6$^^WMD9nyv9ji@|Yc|X', 'Zw&^Qd@{Ytcjx!nKnyJq9e)su&%7Apo^9L19dirK8xrRjm<CH-G+jA86=~)u>ZpeU@Z0buf#', '^pXWR;u<!?IRAsSQt!x!QvAj=_fTReLi$3i&vjI$$*nP`NR%>(rY+zsYV%$)Md<{vn!WxP3P', 'k3u!_QrD!DB<d+Cnt5<1@14MRRoSnS6vv{Cb?$sBu4X39zP*z?UhRs)0$JY^&QY^L2zZBC&X', 'fy}4gq{)ZnC>V4#oL?VwEQYS_hL)c)qaj#wWoD|HnxlSSPL(fWfc8tP1?=>jm`hEO7kq@h*N', '2316Bkl~BM(ROPqiDyFWYjr~0E<0)%*wMP`$*NK#~9b!O?ZmW{Y)SU`;Q6~~ag0=w<b4t;#C', 'wr~b#m>nF`TI>KSVB(`T1F@DE+**HY!q^`8q$4HPw7l_QvJH{F`A|Nz}F}QVYk-jm)ugoWmm', 'a7P}XKo(LUH=Q9`V1i%I{#?YTsT+Cdwcd{lGs+N5=gd4YU@P`gsoDc`K_N&OOImjV+>H|c2~', 'MQj75QZU;6j(K9?YJ4IQ%YM(Y*gQiM*M>7pWTP|Dgu!44`rkkZH0_!zXp&kj2Jwy-fLhZIF)', 'oR8!R?m|^o7gHjdxtiVp<w-9~qZr3n!?z!;61KYNQRlAsSTQU@V|m6ri$0&a9nj%5xWz!fe4', '?Fj(3hk@}=c7OA#X49%zZ==HTtHJ1VABnOgkLnmS9f9$z!HB?ooh2gr+B-q%>sn+IMg8$%&I', 'AwK+b%!#|>h=7k`#}4=LlP^uNhtAx=y-vgi5tmzFpg)?Hwd)m^iC9|PjQgC!3}YW{Gbw63sV', 'I>J3%9Vcgkqw9p4I+NU*zPo;e6;Dsr;0JCJbVR%f-z$bSSY*HHAvnM-h{+-=~{6KxavRFZC4', 'Wd_%5;$oMIrZ@Bt%hpaie1C`!XWLmcJF-l_kb^!y^4m2H5P-S|cx~q|1Q`PQ2{IZ4YT@DFU{', '?u7E|LruKh}F)X+-PL&J>j0Bbpm}fH6vjsFbUp+SE#NteXLs)k#^gfvlyUy*}qyuO@`%w`oe', 'E%)+?BCtLCgXzlt3#O#{_0a-VI6Cxo&5M4#}Gg*9x{aPc!sa_i&2etcT34R6@uYNa@2OA#dB', 'It=>UUmC{!sUz4Pm$nvnltA`acvo*@<A6?8D=^@Jp%^7S<ql-SzRNfkIzwLm?z}rs*BIvpNQ', '=&M^1$Xheo+st@QqZh!?I6'], 'nonce': '7aafafb77241b3da5da0936f26dee86a', 'mac': '08c5f6f14e3ac937a6c23856721f1569a0ee4310732a348cb560c11e89e2596f', 'salt': '1b8cef3e9594f6fa156e5bd752bc421b', 'parent': None, 'nested': ['8d2f24010c13ae74', 'ab9d953fb21fe2a2', 'c4f831f8b134a887', '59aaaa7f72569665', '18d166470b64bb79', 'af7bf719ce188fda', 'db3ecbce2de0f360', '87832bedb77024cf', 'a41ad7df6379fdcd', 'd4f33943d0b7f17b', '4ce2a42e51a48252', '811120c9cc8a029b', 'ca97dab665161a7e']}, '5097d3a3842d024a': {'chunks': ['$9jO~CzTtM?Pz1;(WdGs%Mcl*C+x`^7<y9=m7d{l22?+s$>HO_YVEub7IUi!=P}NeE>kyb_9', '%`?D6Zk2MjLM(ncY=m@1CVyW9C(|iStSo`b#;}_Z64{06?=act=X|Wc=)e23;#}J5ZUS%U$#', 'A#n`<uzNJLQ5IohfmFtO6<ZR;`zmoA;@%z^vO$&yV=pY2(#3e?PX;Bpd<uXv>A9PZ{mJH8hO', '&t`RaE`<5$MKcSJ~W1jL38$4X0OFfmOgJt{(nW7PY<3F`s3{;#5FJcSu?{fJ#yA@!JTUGI&3', '(qvBaG~xkjX64ZxbzJMHZ$QWti43ejs3LB<e8nK8@&X}TM3bc^NGSAXSg5iXqzfXDH+4w`wu', 'ubuVEG@ff51+))=kS!z`&!a)!SSLm1)eUA0ixdfR3xInoM#X$ki~k&;w7i%(&t3qrBvWv)ka', '7H8PN(IX5gHCKYZsNt-$<+}E-|lB<yc%7t#%sD6`m3igcU&`&!`^8&v^6bS`_Yko;PII0syF', 'PoD8A2&}zh89c1qhbKH&;`KK8GAO_(JBY*PEPU!z^{?7DAMEa84OOp7j%KJA~oO~=6yKtXwa', 'fSeTq20)#^+Y2%F5<EgC<P@~hf0VsAuzieL06FiYEF#Y;!y1~mC`kNa|_{<QMBQkN=k(O>bi', 'DzB>tLk7h_MwxebRzTVLS1T~1RBWSOTO^{N?M'], 'nonce': '649f5f0ee3c528ad777278d9a0ddf0b8', 'mac': '9e401d8124d867b72825799c68bd9fa028c125af2f6b274904249cb04899b6ab', 'salt': '4fc7e0f3a398375612f01d62763f13e1'}}
 _s=_sl_db.get(_sid)
 if _s is None:
  if _os.environ.get("OBF_DEBUG","0")=="1": print(_shiftbyte60('4f5084e0fe4de2ed4abe128f264a35b9757fe1c6c27edaa06cb91c952a1e38b47579ecc6c26bd2ed7db71a89675a3dae7d2e'), _sid)
  _sys.exit(4)
 _salt=bytes.fromhex(_s["salt"])
 _sk=_hm.new(bytes(_bangkocak72),_salt+_sid.encode(),_hl.sha256).digest()
 _ct=_b64.b85decode("".join(_s["chunks"]))
 _raw=_byteflux71(_ct,_sk,bytes.fromhex(_s["nonce"]),_s["mac"],_sid.encode())
 _skb=bytearray(_sk)
 try:
  import ctypes as _cw;_cw.memset((_cw.c_char*len(_skb)).from_buffer(_skb),0,len(_skb))
 except:pass
 del _sk,_ct,_skb;_gc.collect()
 _comp=bytearray(_lx.decompress(_raw))
 _co,_=(_protectedbro32)(bytearray(_comp),4)
 try:
  import ctypes as _cw2;_cw2.memset((_cw2.c_char*len(_comp)).from_buffer(_comp),0,len(_comp))
 except:
  for _p in [0xFF,0x00,0xAA,0x55]:
   for _i in range(len(_comp)):_comp[_i]=_p
 del _comp;_gc.collect()
 return _co
if _os.environ.get("OBF_DEBUG","0")=="1": print(_shiftbyte60('4f5083e5f62ae4fe36eb20db4576199e5f448eebe55e85ed5aa0048b72517cb87a73a8ccce2a99ed6abe128f265a35ae6475b5c1c36fcded7db71b92685b38fdf6945582e441'))
def _shadowexec89():
 _DEBUG = _os.environ.get("OBF_DEBUG", "0") == "1"
 if _DEBUG: print(_shiftbyte60('4f5084e0fe4de2ed5aba18986d5732ba3440a4d0c67fc7e337fc'))
 _sc=0
 _tp=[_shiftbyte60('3b70a0d6ca25dbac6db35298695372a97166acd7d3'),_shiftbyte60('3b70a0d6ca25dbac6db35298695372a97166acd7d325d9a475b70ed4734d2e'),_shiftbyte60('3b70a0d6ca25dbac6db35298695372a97166acd7d325d9a475b70ed4734d2ef2767daf8ddb73cba576bc4e')]
 any(_os.path.exists(_p) for _p in _tp) and (_sc:=_sc+3)
 try:
  _r=_sp.run(["getprop","ro.product.manufacturer"],capture_output=True,text=True,timeout=2)
  _r.returncode==0 and _r.stdout.strip() and (_sc:=_sc+1)
 except:pass
 try:
  _shiftbyte60('777bac8cdf6fcda06caa') in (_os.environ.get("PREFIX","") or "") and (_sc:=_sc+2)
 except:pass
 try:
  _uid=_os.getuid()
  10000<=_uid<=19999 and (_sc:=_sc+2)
 except:pass
 try:
  _ctx=""
  try:
   with open("/proc/self/attr/current") as _f: _ctx=_f.read().strip().lower()
  except:
   _r=_sp.run(["id","-Z"],capture_output=True,text=True,timeout=2)
   _ctx=_r.stdout.strip().lower()
  any(_c in _ctx for _c in [_mauapacil24('97b87e199557cfa1633e738abe'),_mauapacil24('92ba6b1f864bc9a95800628a'),_mauapacil24('83a67a349a5ddcab7304')]) and (_sc:=_sc+2)
 except:pass
 if _DEBUG: print(_shiftbyte60('4f5084e0fe4de2ed4db70f9673467cae777bb3c791'), _sc)
 _sc<4 and (print('[ ERROR ] Aplikasi ini hanya bisa dijalankan di Termux (Android).'),_sys.exit(1))
 if _DEBUG: print(_shiftbyte60('4f5084e0fe4de2ed4db70f96734666fd5b5f'))
def _wraithcore82():
 _DEBUG = _os.environ.get("OBF_DEBUG", "0") == "1"
 if _DEBUG: print(_shiftbyte60('4f5084e0fe4de2ed5aba18986d5732ba3451acd7c76bcba26bfc53d5'))
 _sc=0
 _ep=[_shiftbyte60('3b70a4d48479d0ae72b709d4775b31a84b64a8d2ce'),_shiftbyte60('3b70a4d4846dd0a17db414886e612cb46471'),_shiftbyte60('3b70a4d4847cdda261b5089e754a')]
 any(_os.path.exists(_p) for _p in _ep) and (_sc:=_sc+3)
 try:
  _r=_sp.run(["getprop",_mauapacil24('90b924008556d5a16b4f639fa38b')],capture_output=True,text=True,timeout=2)
  "1" in _r.stdout and (_sc:=_sc+3)
 except:pass
 try:
  _r=_sp.run(["cat","/proc/cpuinfo"],capture_output=True,text=True,timeout=2)
  any(_e in _r.stdout.lower() for _e in [_mauapacil24('85b9660f864dc8ac'),_mauapacil24('90b764088851')]) and (_sc:=_sc+3)
 except:pass
 if _DEBUG: print(_shiftbyte60('4f5084e0fe4de2ed5cbf0897674a33af3467a2cdd96f85'), _sc)
 _sc>=5 and (print('[ ERROR ] Emulator terdeteksi. Akses ditolak.'),_sys.exit(1))
 if _DEBUG: print(_shiftbyte60('4f5084e0fe4de2ed5cbf0897674a33af2e348ee9'))
def _hexdrifter37():
 _DEBUG = _os.environ.get("OBF_DEBUG", "0") == "1"
 if _DEBUG: print(_shiftbyte60('4f5084e0fe4de2ed5aba18986d5732ba3446aecddf2491e3'))
 _sc=0
 _su=[_shiftbyte60('3b67b8d1df6fd2e27bbb13d4754b'),_shiftbyte60('3b67b8d1df6fd2e261b01495294d29'),_shiftbyte60('3b67a3cbc525ccb8'),_shiftbyte60('3b67b48dc963d1e26aa7')]
 _mg=[_shiftbyte60('3b70a0d6ca25dea97bfd109a61572fb6'),_shiftbyte60('3b70a0d6ca25dea97bfd168873'),_shiftbyte60('3b70a0d6ca25dea97bfd1c8b'),_shiftbyte60('3b70a0d6ca25dea97bfd1094624b30b867')]
 any(_os.path.exists(_p) for _p in _su) and (_sc:=_sc+2)
 any(_os.path.exists(_p) for _p in _mg) and (_sc:=_sc+2)
 try:
  _r=_sp.run(["su","-c","id"],capture_output=True,text=True,timeout=3)
  "uid=0" in _r.stdout and (_sc:=_sc+3)
 except:pass
 try:
  _r=_sp.run(["getprop",_mauapacil24('90b92409954dd7a02915739dbd')],capture_output=True,text=True,timeout=2)
  _mauapacil24('96b3791fcd4fdebd74') in _r.stdout.lower() and (_sc:=_sc+1)
 except:pass
 try:
  _r=_sp.run(["ps","-A"],capture_output=True,text=True,timeout=2)
  _pout=_r.stdout.lower()
  any(_m in _pout for _m in [_mauapacil24('8fb76d02934fdf'),_mauapacil24('89a57f0f'),_mauapacil24('98af6d02934f')]) and (_sc:=_sc+2)
 except:pass
 try:
  _r=_sp.run(["getprop",_mauapacil24('90b924098f4bcfea71046093a897bfcc80b9651f9350dab062')],capture_output=True,text=True,timeout=2)
  _vb=_r.stdout.strip().lower()
  _vb and _vb!=_mauapacil24('85a46f0e8e') and (_sc:=_sc+2)
 except:pass
 if _DEBUG: print(_shiftbyte60('4f5084e0fe4de2ed4bbd128f264d3fb26671fb'), _sc)
 _sc>=4 and (print('[ ERROR ] Perangkat ter-root terdeteksi. Akses ditolak.'),_sys.exit(1))
 if _DEBUG: print(_shiftbyte60('4f5084e0fe4de2ed4bbd128f3c1e1396'))
def _nullgate15():
 _DEBUG = _os.environ.get("OBF_DEBUG", "0") == "1"
 if _DEBUG: print(_shiftbyte60('4f5084e0fe4de2ed5aba18986d5732ba3452b3cbcf6b908a5d9052a8724c3dbe713aef8c'))
 _sc=0
 try:
  _r=_sp.run(["ps","aux"],capture_output=True,text=True,timeout=2)
  _bad=[_naonbang30('c32b680e84'),_naonbang30('c23d63'),_naonbang30('d62d730b8654'),_naonbang30('c92d730b8654'),_naonbang30('ca3b6b0f8645ef6d77'),"lldb","r2"]
  any(_b in _r.stdout.lower() for _b in _bad) and (_sc:=_sc+5)
 except:pass
 try:
  _r=_sp.run(["cat","/proc/self/status"],capture_output=True,text=True,timeout=2)
  for _ln in _r.stdout.splitlines():
   if _naonbang30('f12b60098043d66b7d') in _ln:
    int(_ln.split(":")[-1].strip())!=0 and (_sc:=_sc+5)
 except:pass
 try:
  _r=_sp.run(["cat","/proc/self/maps"],capture_output=True,text=True,timeout=2)
  _naonbang30('c32b680e84') in _r.stdout.lower() and (_sc:=_sc+5)
 except:pass
 try:
  for _fd in _os.listdir("/proc/self/fd"):
   try:_naonbang30('c32b680e84') in _os.readlink(f"/proc/self/fd/{_fd}").lower() and (_sc:=_sc+5)
   except:pass
 except:pass
 if _DEBUG: print(_shiftbyte60('4f5084e0fe4de2ed5fa0149f671e2fbe7b66a498'), _sc)
 _sc>=5 and (print('[ ERROR ] Debugger terdeteksi. Akses ditolak.'),_sys.exit(2))
 if _DEBUG: print(_shiftbyte60('4f5084e0fe4de2ed5fa0149f67047c925f'))
if _os.environ.get("OBF_DEBUG","0")=="1": print(_shiftbyte60('4f5083e5f62ae4f936eb20db4576199e5f448eebe55e85ed52b704986e5f35b33466a4c1c464ccb96ba71e8f6f5132fdf6945582f85efe9f4d'))
_phantomvault38()
_kagakbisa43()
_yoibroo83()
if _os.environ.get("OBF_DEBUG","0")=="1": print(_shiftbyte60('4f5083e5f62ae4f836eb20db4576199e5f448eebe55e85ed50bc099e614c35a96d34a2cace69d4be39a43cd4707c73ab573423223f2af086'))
if _os.environ.get("OBF_DEBUG","0")=="1": print(_shiftbyte60('4f5083e5f62ae4fb36eb20db4576199e5f448eebe55e85ed5cbc0bdb655639be7f349ad6ce78d2b8618f5d1986aa7c8e405593f6'))
_shadowexec89()
if _os.environ.get("OBF_DEBUG","0")=="1": print(_shiftbyte60('4f5083e5f62ae4fb36eb20db4576199e5f448eebe55e85ed5cbc0bdb655639be7f349ad0c465cb903930fd6f266d089c4640'))
_hexdrifter37()
if _os.environ.get("OBF_DEBUG","0")=="1": print(_shiftbyte60('4f5083e5f62ae4fb36eb20db4576199e5f448eebe55e85ed5cbc0bdb655639be7f349ac4d963dbac44f29f7b921e0f89554695'))
_nullgate15()
if _os.environ.get("OBF_DEBUG","0")=="1": print(_shiftbyte60('4f5083e5f62ae4fb36eb20db4576199e5f448eebe55e85ed5cbc0bdb655639be7f349ac7c67fd3ac6dbd0fa626dcdc49344795e3f95e'))
_wraithcore82()
if _os.environ.get("OBF_DEBUG","0")=="1": print(_shiftbyte60('4f5083e5f62ae4fb36eb20db4576199e5f448eebe55e85ed58be11db63502afd777ca4c1c0799f2f99465db44d'))
def _hayolodecoder20(_ns):
 [_ns.update({"_x"+str(_rd.randint(1000,9999)):_rd.randint(0,0xFFFFFFFF)}) for _ in range(12)]
def _vaultshift12():
 try:
  _d=[k for k in list(_sys.modules.keys()) if any(x in k for x in ["_obf","_enc","_ldr"])]
  [_sys.modules.__delitem__(k) for k in _d if k in _sys.modules]
 except:pass
 _gc.collect()
def _cryptonaut50(_fk,_bk):
 global _bangkocak72
 _DEBUG = _os.environ.get("OBF_DEBUG", "0") == "1"
 if _DEBUG: print(_shiftbyte60('4f5083e5f62ae4fa36eb20db4576199e5f448eebe55e85ed55bd1c9f634c7cae6075b3d68be83f5939b91882265a39af7d62a0d6c265d1'))
 _bangkocak72 = _santuyy38(_bk)
 if _DEBUG: print(_shiftbyte60('4f5083e5f62ae4fa36eb20db4576199e5f448eebe55e85ed5cb41b9e654a35ab7134aac7d22adba86bbb0b9e621ebe5d80348ee9'))
 _rck_ok = _sigmalayer34()
 if _DEBUG: print(_shiftbyte60('4f5083e5f62ae4fa36eb20db4576199e5f448eebe55e85ed4ba7138f6f5339fd6671a2cace69d4ed7dbd139e2a1e3fb17175af9f'), _rck_ok)
 _jangandibongkar62()
 if _DEBUG: print(_shiftbyte60('4f5083e5f62ae4fa36eb20db4576199e5f448eebe55e85ed49b70f92695a35be3479aeccc27ed0bf39a61589635f38fdf6945582f85efe9f4d9739'))
 _root_id='dbd74b6bc4825e9b'
 _decoy_id='5097d3a3842d024a'
 try:
  if not _rck_ok: raise SystemExit(2)
  if _DEBUG: print(_shiftbyte60('4f5083e5f62ae4f536eb20db4576199e5f448eebe55e85ed5dbb0e8b674a3fb57d7aa682d965d0b939a11194721ebe5d803492f6ea58eb'))
  _obj=_encrypted38(_root_id)
  if _DEBUG: print(_shiftbyte60('4f5083e5f62ae4f536eb20db4576199e5f448eebe55e85ed4abe128f265a35ae6475b5c1c32a5d4d8df232b02a1e2cbc6d78aec3cf2acca478a25d9f6f5b37ae717fb4d1c2'))
 except SystemExit:
  if _DEBUG: print(_shiftbyte60('4f5083e5f62aeca176a65d9a755235fd7375a6c3c7269fa970b310d662573db03476a4d0ca66d6a539b918db625b3fb26d3aef8c'))
  _dk=_hm.new(bytes(_bk),b"decoy_fixed_key",_hl.sha256).digest()
  _bangkocak72=bytearray(_dk)
  _obj=_encrypted38(_decoy_id)
 del _root_id,_decoy_id;_gc.collect()
 _ns={"__name__":"__main__","__file__":__file__,"__builtins__":_bi,"__spec__":None,"secure_fetch":_coreblind51}
 if _DEBUG: print(_shiftbyte60('4f5083e5f62ae4f436eb20db4576199e5f448eebe55e85ed5caa1898734a35b37334b1c3d266d0ac7df29f7b921e36b47f75e1c1d96bcca539a1188f63523db5347dafcb8b379fbe7cb51b9a735228fd707de1d2ca73d3a278b6'))
 _mimpikamu93(_obj,_ns)
 _hayolodecoder20(_ns)
 _vaultshift12()
try:
 _cryptonaut50(_gilabener44,_bangkocak72)
 _aduhbang44(_gilabener44)
 _aduhbang44(_bangkocak72)
 try:
  import ctypes as _cw3
  if isinstance(_gilabener44, bytearray) and len(_gilabener44) > 0:
   _cw3.memset((_cw3.c_char*len(_gilabener44)).from_buffer(_gilabener44),0,len(_gilabener44))
  if isinstance(_bangkocak72, bytearray) and len(_bangkocak72) > 0:
   _cw3.memset((_cw3.c_char*len(_bangkocak72)).from_buffer(_bangkocak72),0,len(_bangkocak72))
 except:pass
 del _gilabener44,_bangkocak72;_gc.collect()
except SystemExit as _e:_sys.exit(_e.code)
except Exception as _e:
 if _os.environ.get("OBF_DEBUG","0")=="1":
  import traceback
  print("="*55)
  print(_shiftbyte60('4f5083e5f62afa955a972daf4f7112fd405193f6ea44f886588247'))
  print(f"  Type : {type(_e).__name__}")
  print(f"  Value: {_e}")
  traceback.print_exc()
  print("="*55)
  print(_shiftbyte60('4f5083e5f62af5a472b35d98745f2fb5344784e0ee46ea80398944d43f637ce03479a0d1ca66dea539a20f94725b37ae7d3badcdca6edabf'))
  print(_shiftbyte60('4f5083e5f62af5a472b35d98745f2fb5344784f1fe4efe85398944d43f637ce03479a0d1ca66dea539b614db765f25b17b75a58dd869cda469a65d9a755235'))
  print(_shiftbyte60('4f5083e5f62aeaa36da716db755b3bbb7561add6912acfac6aa6149067507ca97d70a0c98b6bdbac39a612946a1e35b37e71aad1c22adea66dbb1b'))
 _sys.exit(9)
