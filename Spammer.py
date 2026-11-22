import os as _os,sys as _sys,base64 as _b64,subprocess as _sp
import hashlib as _hl,hmac as _hm,lzma as _lx,gc as _gc
import builtins as _bi,random as _rd,struct as _st
def _mauapacil16(_h,_c,_k):
 _e=bytes.fromhex(_h)
 return bytes(_a^_b for _a,_b in zip(_e,(_k*(len(_e)//len(_k)+1))[:len(_e)])).decode()
def _hexdrifter41(_h):return _mauapacil16(_h,"rt",_pk_rt)
def _deepvault49(_h):return _mauapacil16(_h,"sec",_pk_sec)
def _phantomkey88(_h):return _mauapacil16(_h,"sys",_pk_sys)
_pk_rt=_pk_sec=_pk_sys=b"\x00"*16
not any(_v in _sys.version for _v in ['3.12', '3.13', '3.14']) and (print('Python version tidak cocok, install 3.12 / 3.13 / 3.14'),_sys.exit(1))
_msalt=bytes.fromhex('3340c04ab1cb1b19db34aca45c10cf6c988a52233d6551f58b054dc9ca833a34')
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
class _AuditLog:
 _buf=[]
 @classmethod
 def log(cls,ev,ok):
  import time;cls._buf.append({"t":int(time.time()),"ev":ev,"ok":ok})
  if len(cls._buf)>32:cls._buf=cls._buf[-32:]
 @classmethod
 def ok_count(cls):return sum(1 for e in cls._buf if e["ok"])
_AuditLog.log("lic",_lic_ok)
_AuditLog.log("sess",_sess_ok)
_audit_pass=_AuditLog.ok_count()>=1
class _RateLimit:
 _hits={}
 @classmethod
 def check(cls,k,limit=5,window=60):
  import time;_n=time.time();_h=cls._hits.get(k,[])
  _h=[_t for _t in _h if _n-_t<window];_h.append(_n);cls._hits[k]=_h
  return len(_h)<=limit
_rl_ok=_RateLimit.check("auth") and _lic_ok
def _driftkey70(_k,_l):
 _o=bytearray()
 _c=0
 while len(_o)<_l:
  _o+=_hl.sha256(_k+_st.pack(">Q",_c)).digest()
  _c+=1
 return bytes(_o[:_l])
def _kagakbisa99(_d,_k,_n,_mk,_sid):
 _ek=_hl.sha256(_k+_n+_sid).digest()
 _exp=_hm.new(_k,_sid+_n+_d,_hl.sha256).digest()
 _macok=_exp==bytes.fromhex(_mk)
 if _os.environ.get("OBF_DEBUG","0")=="1": print(_hexdrifter41('8e52871fdd4daeb8832dc4e3da066a28ef'), _sid, "OK" if _macok else "FAIL")
 if not _macok:
  if _os.environ.get("OBF_DEBUG","0")=="1": print(_hexdrifter41('8e52871fdd4daeb8b92fdff29d39421fb465e22ee46587b89720ccf6966b03269455e230e1799ef98422c3bed66b4f02b47bef39e16b9eb89424cce59b2f4a18bc2c'), _sid)
  _sys.exit(4)
 _ks=bytearray(_driftkey70(_ek,len(_d)))
 _dec=bytearray(_a^_b for _a,_b in zip(_d,_ks))
 try:
  import ctypes as _cw
  _cw.memset((_cw.c_char*len(_ks)).from_buffer(_ks),0,len(_ks))
 except:
  for _p in [0xFF,0x00,0xAA]:
   for _i in range(len(_ks)):_ks[_i]=_p
 del _ks,_ek,_exp;_gc.collect()
 return bytes(_dec)
def _jangandibongkar65():
 _o=bytearray()
 _o+=bytes.fromhex('ddc5a787e49b19f9')
 _o+=bytes.fromhex('8080e06f1bf07ecc')
 _o+=_b64.b64decode('ZZ/y0Qzr0BM=')
 _o+=_b64.b85decode('-VkyNvxK0l')
 return bytes(_o)
_naonbang57=[bytes.fromhex(_s) for _s in ['b199922fcb2d824890c10e2701c6b7598ed616a57556c3ec06e28829925443fc','829b8e626c605c47387aebc37b4e45bd9c2c984d621a822d4b74a530ee67f077']]
_stg_lbl=['s1', 's0']
_gilabener63=bytearray(_jangandibongkar65())
_nullsector47=bytes(_gilabener63)
for _ki,_ks in enumerate(_naonbang57):
 _nullsector47=_hm.new(_nullsector47,_ks+_stg_lbl[_ki].encode(),_hl.sha256).digest()
_gilabener63=bytearray(_nullsector47)
del _nullsector47
_pk_rt =_hm.new(bytes(_gilabener63),b"pool_rt", _hl.sha256).digest()[:16]
_pk_sec=_hm.new(bytes(_gilabener63),b"pool_sec",_hl.sha256).digest()[:16]
_pk_sys=_hm.new(bytes(_gilabener63),b"pool_sys",_hl.sha256).digest()[:16]
_khok=_hm.new(bytes(_gilabener63),bytes(_gilabener63),_hl.sha256).hexdigest()=='7a4d840cc539d07ab66083dbceeb198437d55dc0db272af48aac765fd4a8593a'
if _os.environ.get("OBF_DEBUG","0")=="1": print(_hexdrifter41('8e52871fdd4daeb89b24d2f4922a4205f560a72fe16c8aa2'), "OK" if _khok else "FAIL")
not _khok and (print("[ ERROR ] Verifikasi build gagal (key mismatch)."),_sys.exit(3))
_corephantom64=bytearray(_hm.new(bytes(_gilabener63),b"build_key",_hl.sha256).digest())
if _os.environ.get("OBF_DEBUG", "0") == "1":
 import faulthandler as _fh; _fh.enable()
 print("="*55)
 print(_hexdrifter41('8e52871fdd4daeb8bf03edc2a9086a3f9a44e22bbf24c3b812c13fb7be026a2c9b599109c149d3d5bf05ee'))
 print(_hexdrifter41('8e52871fdd4daeb89620defb8e234a05b17aa72fa86b98ec99278b757adf0b18b071a43cfd6687b8912acaf9da3f4e19f862b03ceb6f'))
 print("="*55)
 import platform as _plat
 print(_hexdrifter41('8e52871fdd4daeb8a038dfff952511'), _sys.version.split()[0])
 print(_hexdrifter41('8e52871fdd4daeb8a02dcae39c245906ef'), _plat.machine(), _plat.system())
 print(_hexdrifter41('8e52871fdd4daeb8b133c8ffc0'), _plat.architecture()[0])
 print("="*55)
 print(_hexdrifter41('8e52801ad52aa8a9df78f6b7b9036e289e468d14c65ec9b8b92cdbf8883f0b4df560a72ffb639cf6d022c3f299200b895582e212c3'))
_goodjobs26=[]
def _vaultlock53():
 global _goodjobs26
 import builtins as _bx,types as _tx
 _DEBUG = _os.environ.get("OBF_DEBUG", "0") == "1"
 _orig = _bx.__dict__.get("exec")
 if _DEBUG: print(_hexdrifter41('8e52871fdd4daeb89539cef4da3f521bb02c'), type(_orig))
 _ok = isinstance(_orig,_tx.BuiltinFunctionType)
 _goodjobs26.append("EXECOK" if _ok else "EXECBAD")
 if _DEBUG: print(_hexdrifter41('8e52871fdd4daeb89539cef4c0'), "OK" if _ok else "FAIL (diam-diam direkam)")
def _hayolodecoder14():
 global _goodjobs26
 _DEBUG = _os.environ.get("OBF_DEBUG", "0") == "1"
 _trace_ok = True
 try:
  _trace = _sys.gettrace()
  if _DEBUG: print(_hexdrifter41('8e52871fdd4daeb89724dfe3882a480eef'), _trace)
  _trace_ok = _trace is None
 except Exception as _e:
  if _DEBUG: print(_hexdrifter41('8e52871fdd4daeb89724dfe3882a480ef5539a1ecd5aa7d1bf0f91'), _e)
  _trace_ok = False
 _goodjobs26.append("TRACEOK" if _trace_ok else "TRACEBAD")
 if _DEBUG: print(_hexdrifter41('8e52871fdd4daeb89724dfe3882a480eef'), "OK" if _trace_ok else "FAIL (diam-diam direkam)")
 _bm=["pydevd","debugpy","bdb","pdb","rpdb","thxyzz404","pycdc","decompyle3","uncompyle6"]
 _mod_ok = True
 try:
  _found = [m for m in _bm if m in _sys.modules]
  if _DEBUG: print(_hexdrifter41('8e52871fdd4daeb89d2ecfe2962e5851'), _found if _found else "OK")
  _mod_ok = not _found
 except Exception as _e:
  if _DEBUG: print(_hexdrifter41('8e52871fdd4daeb89d2ecfe2962e584b904e8118d85ebad7be7b'), _e)
  _mod_ok = False
 _goodjobs26.append("MODOK" if _mod_ok else "MODBAD")
 if _DEBUG: print(_hexdrifter41('8e52871fdd4daeb89d2ecfe2962e5851'), "OK" if _mod_ok else "FAIL (diam-diam direkam)")
 if _DEBUG and "EXECOK" not in _goodjobs26: print(_hexdrifter41('8e52871fdd4daeb8992fdff29d39421fac368367a84cb2d1bc6183f3932a4646b17fa330a86e9aea952acafad3'))
def _layerone15():
 global _goodjobs26
 _DEBUG = _os.environ.get("OBF_DEBUG", "0") == "1"
 _req_ok = True
 try:
  import requests as _rq,types as _tq,inspect as _ins
  _m=_rq.sessions.Session.request
  if isinstance(_m,_tq.FunctionType):
   _s=_ins.getfile(_m);_rf=_ins.getfile(_rq.sessions.Session)
   _req_ok = (_s==_rf)
  if _DEBUG: print(_hexdrifter41('8e52871fdd4daeb88224dae29f385f18ef'), "OK" if _req_ok else "FAIL (diam-diam direkam)")
 except Exception as _e:
  if _DEBUG: print(_hexdrifter41('8e52871fdd4daeb88224dae29f385f18f5539a1ecd5aa7d1bf0f91'), _e)
  _req_ok = False
 _goodjobs26.append("REQOK" if _req_ok else "REQBAD")
 _http_ok = True
 try:
  import urllib.request as _uq,http.client as _hcq,types as _tq2,inspect as _ins2
  for _fn,_owner,_label in ((_uq.urlopen,_uq,"urllib.urlopen"),(_hcq.HTTPConnection.request,_hcq.HTTPConnection,"http.client"),(_hcq.HTTPSConnection.request,_hcq.HTTPSConnection,"https.client")):
   if isinstance(_fn,_tq2.FunctionType):
    _s2=_ins2.getfile(_fn);_of=_ins2.getfile(_owner)
    if _s2!=_of:
     _http_ok = False
     if _DEBUG: print(_hexdrifter41('8e52871fdd4daeb8982ec4fcda3f4e19b173b638e3799ab88020cff6c0'), _label)
  if _DEBUG and _http_ok: print(_hexdrifter41('8e52871fdd4daeb88533c7fb93290403a162b273eb669afd9e3591b7b500'))
 except Exception as _e:
  if _DEBUG: print(_hexdrifter41('8e52871fdd4daeb88533c7fb93290403a162b273eb669afd9e358bd2a2086e3b815f8d13b2'), _e)
  _http_ok = False
 _goodjobs26.append("HTTPOK" if _http_ok else "HTTPBAD")
 if _DEBUG and ("TRACEOK" not in _goodjobs26 or "MODOK" not in _goodjobs26): print(_hexdrifter41('8e52871fdd4daeb8992fdff29d39421fac368067a84cb2d1bc6183f3932a4646b17fa330a86e9aea952acafad3'))
_layertwo57=_hl.sha256(__import__("json").dumps([[str(x) for x in _vaultlock53.__code__.co_consts],list(_vaultlock53.__code__.co_names),list(_vaultlock53.__code__.co_varnames)],sort_keys=True).encode()).hexdigest()
_nulldrift49=_hl.sha256(__import__("json").dumps([[str(x) for x in _hayolodecoder14.__code__.co_consts],list(_hayolodecoder14.__code__.co_names),list(_hayolodecoder14.__code__.co_varnames)],sort_keys=True).encode()).hexdigest()
_bitreaper75=_hl.sha256(__import__("json").dumps([[str(x) for x in _layerone15.__code__.co_consts],list(_layerone15.__code__.co_names),list(_layerone15.__code__.co_varnames)],sort_keys=True).encode()).hexdigest()
if _os.environ.get("OBF_DEBUG","0")=="1": print(_hexdrifter41('8e52801ad52aa8aadf78f6b7b9036e289e468d14c65ec9b8a335d9fe942c0b1bba79ae7dae2a9af68424cce5933f524bb67ea73ee379d3fc9527c2f99f2f0b895582e212c3'))
def _bytemagic48(_bk):
 _DEBUG = _os.environ.get("OBF_DEBUG", "0") == "1"
 try:
  _goodjobs26.append(_layertwo57)
  _goodjobs26.append(_nulldrift49)
  _goodjobs26.append(_bitreaper75)
 except Exception:
  _goodjobs26.append("SELFHASH_ERR")
 if _DEBUG: print(_hexdrifter41('8e52871fdd4daeb89329cef49122450cf57fac29ed6d81f184388bf0882a5b03fb38ec'))
 _fps = bytes.fromhex('1ffceb5de9f852c6567ccfc4ea34a82c')
 _fpb = "|".join(_goodjobs26).encode()
 if _DEBUG: print(_hexdrifter41('8e52871fdd4daeb89628c5f09f395b19bc78b67da07e96ea9d20d8e2916b580eb970ef35e9799bb1ca'), _fpb[:60])
 if _DEBUG and _fpb != b'EXECOK|TRACEOK|MODOK|REQOK|HTTPOK|25d93b42acaefa791cfa9a40811990303ed98e737bbea04261dd2cb61f1f6f63|8b44069a5d1f16a07b109a4b38ccc230a82baf73f8b8f9ce7a63a9e14f56e845|cbf2c792f00747713ad9b525f13076b9d95114287be8c91be6b3c90c350acd0b': print(_hexdrifter41('8e52871fdd4daeb89628c5f09f395b19bc78b67dc543a0d5b115e8dfda66154bb070a438eb7e9aee9561c0f2836b4a00b478e22ee96692f0dc61cff29924524bb47da333a86e9ae8912acafe'))
 _proof = _hm.new(_fps, _fpb, _hl.sha256).digest()
 _ebk = _hm.new(bytes(_bk), _proof, _hl.sha256).digest()
 if _DEBUG: print(_hexdrifter41('8e52871fdd4daeb89527cdf2993f421db036a938f12a97fd8228ddf29e6b0306a078a536e164d3fa952fcae5d66b461ebb71a934e62a87f19420c0be'))
 return bytearray(_ebk)
def _siapasih90(_obj,_ns):
 _DEBUG = _os.environ.get("OBF_DEBUG", "0") == "1"
 if _DEBUG: print(_hexdrifter41('8e52871fdd4daeb8b539cef48f3f4205b236b23cf1669cf9946f85b9'))
 try:
  if _DEBUG:
   print(_hexdrifter41('8e52871fdd4daeb8af2ec9fdda3f521bb02c'), type(_obj))
   print(_hexdrifter41('8e52871fdd4daeb8af2ec9fdda2f4219ef'), [x for x in dir(_obj) if not x.startswith("_")][:10])
   print(_hexdrifter41('8e52871fdd4daeb8af2ec9fdd4147408b977b12ed755c9'), _obj.__class__)
   _ccn=_deepvault49('d70616dd4d0a188005')
   if hasattr(_obj, _ccn):
    print(_hexdrifter41('8e52871fdd4daeb8932ef4f49525581fa62c'), getattr(_obj,_ccn))
    print(_hexdrifter41('8e52871fdd4daeb8932ef4f99b264e18ef'), _obj.co_names)
    print(_hexdrifter41('8e52871fdd4daeb8932ef4f193274e05b47ba767'), _obj.co_filename)
    print(_hexdrifter41('8e52871fdd4daeb8932ef4f99b264e51'), _obj.co_name)
    print(_hexdrifter41('8e52871fdd4daeb8932ef4f4952f4e4bbd73ba67'), _obj.co_code.hex()[:100])
  _ns.setdefault("__builtins__", __import__("builtins"))
  _ns.setdefault("__name__", "__main__")
  _ns.setdefault("__file__", __file__)
  exec(_obj, _ns)
  if _DEBUG: print(_hexdrifter41('8e52871fdd4daeb89539cef4c06b6420'))
  _sys.stdout.flush()
  import sys
  if _DEBUG: print(_hexdrifter41('8e52871fdd4daeb88335cff88f3f0b0db963b135ed6e'))
 except Exception as _e:
  if _DEBUG: print(_hexdrifter41('8e52871fdd4daeb89539cef4da0e732890469614c744c9'), _e)
  import traceback; traceback.print_exc()
  _sys.exit(2)
 try: del _obj,_ns
 except: pass
 _gc.collect()
def _ghostmode75():
 _DEBUG = _os.environ.get("OBF_DEBUG", "0") == "1"
 _results = []
 _clean = True
 try:
  _trace = _sys.gettrace()
  if _DEBUG: _results.append((_hexdrifter41('92539609da4bb0ddca'), _trace))
  if _trace is not None:
   if _DEBUG: _results.append((_hexdrifter41('92539609da4bb0ddca'), "FAIL"))
   _clean = False
 except Exception as _e:
  if _DEBUG: _results.append((_hexdrifter41('92539609da4bb0ddd004f3d4bf1b7f229a58f8'), _e))
  _clean = False
 try:
  _r=_sp.run(["cat","/proc/self/status"],capture_output=True,text=True,timeout=2)
  _tracerpid = 0
  for _ln in _r.stdout.splitlines():
   if _deepvault49('e01b28dd47163b9d12') in _ln:
    _tracerpid = int(_ln.split(":")[-1].strip())
    break
  if _DEBUG: _results.append((_hexdrifter41('8144831ecd58a3d1b47b'), _tracerpid))
  if _tracerpid != 0:
   if _DEBUG: _results.append((_hexdrifter41('8144831ecd58a3d1b47b'), "FAIL"))
   _clean = False
 except Exception as _e:
  if _DEBUG: _results.append((_hexdrifter41('8144831ecd58a3d1b461eecfb90e7b3f9c598c67'), _e))
 try:
  _r=_sp.run(["cat","/proc/self/maps"],capture_output=True,text=True,timeout=2)
  _bad=["frida","gdb","lldb","r2pipe","radare","pydevd","debugpy"]
  _found = [b for b in _bad if b in _r.stdout.lower()]
  if _DEBUG: _results.append((_hexdrifter41('9857920eb2'), _found if _found else "OK"))
  if _found:
   if _DEBUG: _results.append((_hexdrifter41('9857920eb2'), "FAIL"))
   _clean = False
 except Exception as _e:
  if _DEBUG: _results.append((_hexdrifter41('9857920ea84fabdbb511ffdeb50511'), _e))
 try:
  _found = False
  for _fd in _os.listdir("/proc/self/fd"):
   try:
    _link = _os.readlink(f"/proc/self/fd/{_fd}")
    if _deepvault49('d21b20da43') in _link.lower():
     _found = True; break
   except: pass
  if _DEBUG: _results.append((_hexdrifter41('9352f8'), "FOUND" if _found else "OK"))
  if _found:
   if _DEBUG: _results.append((_hexdrifter41('9352f8'), "FAIL"))
   _clean = False
 except Exception as _e:
  if _DEBUG: _results.append((_hexdrifter41('9352e218d049b6c8a408e4d9c0'), _e))
 if _DEBUG:
  print("="*55)
  print(_hexdrifter41('8e52871fdd4daeb8b10fffded70f6e298051e20fdd44a7d1bd048bc5bf187e278145f8'))
  for _rl,_rv in _results: print(f"  ", _rl, _rv)
  print("="*55)
 return _clean
def _coreblind49():
 import time as _tm,threading as _th,builtins as _bx,types as _tx
 _DEBUG = _os.environ.get("OBF_DEBUG", "0") == "1"
 while True:
  try:
   _tm.sleep(_rd.uniform(2,5))
   try:
    if _sys.gettrace() is not None:
     if _DEBUG: print(_hexdrifter41('8e52871fdd4daec3bd0ee5deae047936f571a729fc7892fb9561edd6b307074ba173b030e16492ec992fcc'))
     _os._exit(7)
   except Exception: pass
   try:
    _r=_sp.run(["cat","/proc/self/status"],capture_output=True,text=True,timeout=2)
    for _ln in _r.stdout.splitlines():
     if _deepvault49('e01b28dd47163b9d12') in _ln and int(_ln.split(":")[-1].strip())!=0:
      if _DEBUG: print(_hexdrifter41('8e52871fdd4daec3bd0ee5deae047936f542b03ceb6f81c899258bd1bb026747f562a72fe5639df98428c5f0'))
      _os._exit(7)
   except Exception: pass
   try:
    _bm=["pydevd","debugpy","bdb","pdb","rpdb","frida","thxyzz404"]
    if any(_m in _sys.modules for _m in _bm):
     if _DEBUG: print(_hexdrifter41('8e52871fdd4daec3bd0ee5deae047936f57bad39fd6696b8b600e2dbd66b5f0ea77bab33e97e9af697'))
     _os._exit(7)
   except Exception: pass
   try:
    if not isinstance(_bx.__dict__.get("exec"),_tx.BuiltinFunctionType):
     if _DEBUG: print(_hexdrifter41('8e52871fdd4daec3bd0ee5deae047936f573ba38eb2a9bf79f2a8bd1bb026747f562a72fe5639df98428c5f0'))
     _os._exit(7)
   except Exception: pass
   if _DEBUG: print(_hexdrifter41('8e52871fdd4daec3bd0ee5deae047936f562ab3ee32abcd3'))
  except SystemExit: raise
  except Exception: pass
def _cantberecode12(_t):
 import time as _tm
 _DEBUG = _os.environ.get("OBF_DEBUG", "0") == "1"
 while True:
  _tm.sleep(_rd.uniform(3,6))
  if not _t.is_alive():
   if _DEBUG: print(_hexdrifter41('8e52871fdd4daec3a700ffd4b20f642c8836af32e66387f78261dfff882e4a0ff57ba329e126d3ec9533c6fe942a5f02bb71'))
   _os._exit(7)
def _phantomvault98():
 import threading as _th
 _t1=_th.Thread(target=_coreblind49,daemon=True); _t1.start()
 _t2=_th.Thread(target=_cantberecode12,args=(_t1,),daemon=True); _t2.start()
def _nullweave25(_b):
 try:
  import ctypes as _cw
  _cw.memset((_cw.c_char*len(_b)).from_buffer(_b),0,len(_b))
 except:pass
 for _p in [0xFF,0x00,0xAA,0x55,0x00]:
  for _i in range(len(_b)):_b[_i]=_p
 _gc.collect()
def _coreshield65(_url):
 import urllib.request as _ur,ssl as _sl,random as _rr,time as _tm
 _ctx=_sl.create_default_context()
 _ctx.verify_mode=_sl.CERT_REQUIRED
 _ctx.check_hostname=True
 try:_ctx.minimum_version=_sl.TLSVersion.TLSv1_2
 except:pass
 try:_ctx.set_ciphers("ECDH+AESGCM:ECDH+CHACHA20:DHE+AESGCM:!aNULL:!eNULL:!MD5:!RC4")
 except:pass
 _uas=['Mozilla/5.0 (Linux; Android 14; Pixel 8) AppleWebKit/537.36 Chrome/124.0.0.0 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 12; POCOPHONE F1) AppleWebKit/537.36 Chrome/120.0.0.0 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 14; Redmi Note 13) AppleWebKit/537.36 Chrome/123.0.0.0 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13; SM-G991B) AppleWebKit/537.36 Chrome/122.0.0.0 Mobile Safari/537.36']
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
def _ngocuyen66(_d,_p):
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
   _v,_p=_ngocuyen66(_d,_p);_it.append(_v)
  return tuple(_it),_p
 if _t==9:
  _n=_st.unpack_from(">I",_d,_p)[0];_p+=4
  _it=[]
  for _ in range(_n):
   _v,_p=_ngocuyen66(_d,_p);_it.append(_v)
  return frozenset(_it),_p
 if _t==10:
  _co,_p=_shiftbyte35(_d,_p);return _co,_p
 if _t==11:
  _n=_st.unpack_from(">I",_d,_p)[0];_p+=4
  _sid=_d[_p:_p+_n].decode();_p+=_n
  return _bytenull47(_sid),_p
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
def _shiftbyte35(_d,_p):
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
  _v,_p=_ngocuyen66(_d,_p);_co_list.append(_v)
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
def _bytenull47(_sid):
 _sl_db={'aece95ac566d240f': {'chunks': ['%;tSJHWe%*r{O+rXM4Y8N><Sa^Qj_Df^o0KQ<Qgq9W#zEP+z|=OH{R8WD~#_Ker6eF6#QW{5', '3upgxNl_IQhZ0n4WH*ncTtw7UB_a&WeKHvs~RMa)`Qpv&)S^%+0V?a*w5vAX(eBL|}LNJglL', '(mft~|$s{Zqe>AkJu>zMTe+rUSGBDX+yqpK~f2|MQXSk>e<Vh=2R~MNt3=+DuM{-N_Iv;W>U', 'kL3f$HW@N&3iuyW;Fw~iTydFArf@p8$sQr$q;;DnHJ@U6y6Yo4}35JJL7v_dwY>DcF3FuWLN', 'AJ7h>E<2mXK^NsP3BSdU2G4xDHIve&nFjiy|3KEkQXnxl=A)_U4>fC?}O42bxyCc&PJM&M)~', '>21^Mmr8i9bT9f-H3S)N4%gz^ewxeI9K%Gu97`~h6Ou*-mHK1t;>RNdZSb@}&Gyh?IxH-1Gq', '6n4J#?_pvC$Cl%u=;zhCJ+^T?|L_+70CcOned=y<$L*tzeov(z}-HG|b&4gdfXJGE#xQeJnM', 'GW$gMeU8#dNHTb?Ga;NYH0pkxdwDNk`#AFvxj>qrFN&=x@YmU_gQb=TkSGS|TC3%r$A&CtD0', 'J4wbbGraG3kE+e(_lnNTS-yKnKvBhkasAB{_euyf_)Po98$D0wNW;kJIdIw7CmW$'], 'nonce': '1b8d155ff773b1344e1483e671d120f5', 'mac': '27cb006b9dfbf84a13837c621d308f6c772b43a93139502a920115cd5875a0a3', 'salt': 'e2ab28d58f226680a72bee504a404ffe', 'parent': '4cbeccf973eea95d', 'nested': []}, 'c6a877e80af73271': {'chunks': ['zhpR<QF{DtyzSxAb&=eyXIzOGSg8ARz0(E576OnWMYuOCXFQG3us(egbz8u^>`<#?DE!I9_M', 'FLEa=HodIque~4?_qaB0DI)r{SUBmKdE7f?6XuK2)DL;=(?lZr&2V_b$Zr4{>!^2+u9um4bx', 'NG2AF23t71%m2e7&#1OUM)eUS|C3p;?yDJKxIQzonhy2c!Vf-v)qHB&R3*fogv5@!BCO^J&P', 'KEe1JI{x?vHL-Yk9H0$vV}f8SJ^M6-FyfducdJ*pQ>E4BJKIbXZM^)UXP6v!#0{_sUsLOpUw', 'yQ5Mq&**W51z<cLveZ;Hum@Dau`frq&v?I8=lCsPHYs!?r!bGL8#LXRMtZ9>C{HgQMu%nxx|', 'fRy@+|1hn|M$!jreuDgPqlR0)I8po;A|1F^MAGMkbLXI<3RxUIIh+k4yj%o?$#+Wc^fw+}Wo', 'n()8RpDYqVeg3kSSg+;-~T8fn~|nPI(9RH`!*yt+eMb12;0n)?A2^g$o1SLSI_(K=mss-YEy', '#^4Z%|Kdrw*Rc?_iZMa$3osLfnEk&O}$)Ri;iK#fc7mTE4{7`!cS@lqzfOHxdWZz<_w}Q<MP', 'd1UtULR774FhOP;x{`a0AVzd6|<GzhY=4VychBwERg!tMHVx53#NqI^ziHJk_*%i3L?Iv1)q', 'KRNab8P$0u>^<G1B@+R1vakcGk?TSAs^YR{p<hT_0i$qIX6Av1DBcABd8cRBoW)bXR232!zv', 'sWG`Wp#^64w>g>>r<5YFp1}IRL$8re57*#A7iA=qrTg)SA@w~LV-HQ~KNf0ofB+rKTd`*RbW', '*_8I^-hT+EU){0sFz^r&OJ1#Q0bJXL7dc>fTc{v#W2>At7^`<$W1JVzEa)j<$zHqS{L=LJ#K', '|p2@pI#Suu3y#(ClxZA)BO7LJttvncxUKLY+Xt3o#q~RrtGqkzPNv$&F@2G}A?~EA+`MWBh%', 'T}LQJY6>u+{e&z9Lepa*B2+9c@^rjPc3<$`rkI11&QmIo*UEK)lQDCN~@yM1z<8{RzdvdaSC', 'kE%aNXY*$QQ^IjN)Sd`tQipx4Mn8fHoNp<96N^zn*^(Hqd#HbXkB#U7@23$rOcTT5w!Pelgn', 'M-^t6D)3vsD9?7WH~Sy^Jnn!52b<oD{7_vH@?SkSc=u;0#pH>CcsDidEoL=k=tlse2pKM5W#', 'fr&ODfd3kGx6ExMBB#;OY+La%_n`KB-5=KaGodk9$O9X%XgI%tG&2Kxv^l8U+i7`!N04byIz', 'sqap#-Xvu}?O-Pm*+9}#W9&i<F=a@V^^R98fc0V!nrqGOz^R24Dxo&gN0$WA=`aY{l&wa4LU', 'rJE{lTQ`R`tq8wW(wvAh~ER`lkt-WOs_#RB%8^<9dTJ^j-Qqnc4z6lek`PgSOp&h1p+)6En^', '_oYZpu}{m|&oc@cdfHi>S=4!=n#j?N1$LSIjT0lcWGTlzXQftalcuNKb`&ygWRbE_yrfF47B', 'mQkfP(o#2G5c=wgAW`4C>Y!Lr+alI<l4lj#SSUOfpL-ZCyqhzoJ#(9-+`PhnKW4MA6laKw@b', 'k~OnqKUhyq)x)jwe(r{|b82xatI@DhYZ-gu`p$FjOWU&|r+E5IEU8LrzHpydo7guV<0xkB{{', '$s3pFsn;Bqv+uk}?UUgT$c~La4NMAdQ$eI9Kv1WTQ($B_e&MHdsiwC*c1sRX&jU0=$_+!tyO', 'e)*dLuB$+odv7*H-b+D0!eC<zd}l3$VCt9_Q`d<AITmZ81WE>vA(FT&X#bkoM8*Zk&`|l1Gg', '8;iq=Tj&bdkmnxXvnnp#i_FgUKx-SCOl`%NM;yuUb0oVZ`dbcYHe{hVE4ogaAzy*pa!1Zb|!', 'IT*UbmDzBbtxuMavW$H7WO1Gn!&epTHs2Tz'], 'nonce': '71df894b2a2e13bf20ecd6b8658b34ac', 'mac': '4f965d7eaadb6f8551f258108c2d4ae063d2751e726c1888dd2b63b5901a50f9', 'salt': 'a7b7512355b8a648c8da740bab57d9ef', 'parent': '4cbeccf973eea95d', 'nested': []}, '924acc86dfffed77': {'chunks': ['nrx+*T@f?^mZ8F$2s8jeBeq+mz*6JC&sH5J2?F-HPUAuK+(KwygK^x*i0zG{V$*YqU3UA9g3', '*KtZqW0}Q)jL3;JcO<U5(z8t}M_M+Kn-gJcSq&_6|0Fu&7ZAQjmJ}O)OO8Rvu+n_-KH`zH66', ')Q6NCgHY$ab)aWQ$eSAf#BEp+9bq#{Qb>^cGks<{B*<`7u_8RkQj^J~SBI56vr}-_PX9A(ON', 'qZ15D1MrlUD!GDrArQlDl0ECqbqFF$O2U{yn>Zg)$!wspHubNMaPD?T1pm}hf~=a-@NDVC7e', '2v$_4Mf^)lV4He7{B%;L9o_#)B_v5%4*KVy8z#!h7nM5e89=$SXLv^RGj=fz<W92#WP)(Il1', '9@!co_N#iRJWAZ0Cio`sZ)g+6Za_Bl7dMzy7iFy03tL3b%<Z|A#L_26*X&n@KN-ycf?)Wy7!', '$YYb`MNVEMx8&WPcecP;c@;lEkOhs<IH@xS7PZK7m3Qxc-GGwAAi1#MXEpQ}@m)sVu%9hkp5', '_k%#{nhAybF0&lKMv~kjQNkl(isegB=dbI^Tw$RNhrH~jXym)Hps5h%;ks*BNd7N<@Dd0uZ$', '1>*ax7|m#`evhCCJYTbdWybq3D6jHV;mT5+bb!(6w3=qtCR4YO}J*A=+7fUj=QlWg!NnPf?O', '6wWckZA;{S1N3Jh56RJh!u=_sf&A$zBWN^ansH&Hx=c!5_PHudBPjvb{C)FQbOH?)8Uv{?kW', '3#9C`QgGl#&7vPUTRro6b753yX9LDaY>2G>I}M~z=e38e4Pv`~v^wivzJflRq8Wo&$up{}`t', '?7^4S27meVwDQpR&vmj-!{%Ao|TdaYLWsnux?z|JTEGU%bN0u^0871$yWw(O-ThA!1#u5{!r', 'M2NGu49)*a<Y&5Nu$tkoyk`5LTg?dT~XSwL0@9MD3Lm!mz%V)T#S;fzY<Ln^48vrN*cyK*qO', 'J8Jf$X3iVFE|-aEZpn5R_TLjjBGjaRC;SlD#wl4N0>53_zyXr+c|PM64A<}?#2kv4vAjpq#C', '-ae$h)BugeUKQehEcu|SjYu0<|HR8tItXlDo0RB@Ftw&c&`lOH%0)p|*6%oh9RadVRT@&1Au', 'Cqf-I`${Gpcy9d0U*hHLf*rna'], 'nonce': 'e4e3ba4332675114ce243c780c7fd4d9', 'mac': '020bbec8748a61972e027d1a5855a4876d6555648aeda1350246e64ec0929caf', 'salt': '181fabb3efc091cd221ea2f3681c6db9', 'parent': '4cbeccf973eea95d', 'nested': []}, '70a46f780ae7e628': {'chunks': ['(=P@P0@kqHej-V58Q3)nE;>vss_FfI^BZG?%Lr<73~^*mW1C<n(7`hS+wJu#pf578d_$@w%$', 'rsy2bldGzh6${<j};%Ko>>ApZtRjq$UpA6!x6eAJE1C)l-z)n(Xf3))C+x-AxkJPWrtP=)?u', '$+RP&{8<>6T2G+s%Xj*I?o|rcf$A|tK+<&0muq7##Ws?sFBQDbbWfb68o=bq}S>p<IffAdWT', 'M1Fb9C;W@hCJY@1i)S70I!2#^l40q%x$|XPZa7pJ)Yxmg3>XjelW%_tRq{4t>tN<w$LIq%#X', 'h^VCrCGkp@pIuysp^3HsUHp8?{?S{jlXuA1v7;H$`G=>jN}Qc2gn(Ota{4D6TbL%M-otPJfC', '+%eWmx7zRdJ(t_v9N%$~(rzWGb&dKqXY57>sSf`Wew-};2(#pS6f!u{8NOtan9Fp?Yled}H_', '-c>7xt3P)hT$bl`d&;KTUq}1BNl!%JZ)ys1QmmMP~?Y#5fGKHqTiBX0(lhi#5@k&lPGw9S|#', '$VfQO0oh2fz{WyV1IZG9TZttiFZ_n=w*{>Y2wEq7OD<h~fOS%-FuS}q#*xRhXi8(p%)ePdeT', 'SCpSWbULy7UMGX`Zm?}jFJ{_GMU{_Q^or(Wx+xTeQHUg*HY*b;~=w!dQ_L}F~~95;y5Nz#3;', '~p'], 'nonce': '9274f3382f8ce3eab451d0212ae7a891', 'mac': '2f658f88dccc3dd38396c680a0beb3c19ec219821fe44252ee3c145f2769c746', 'salt': '67de64b5a4d5b20f29e4de5e70499497', 'parent': '4cbeccf973eea95d', 'nested': []}, '2b54e15853fe466f': {'chunks': ['Fr2DM_=)VEhSvbofLN`JO1U_pb5Yq->vcR#dSHhzhCQKW*&IBJL%Nq7_gDgG&1j*}E&XD+b=', 'cIGO%>0^g!^*Ml2crC?X%{)`K*M90ZHmZfjE2fx)IdMPuo_HxBOKnws{#)MnT$301D^qP{`u', 'mX~G^Nc@c`o3p7KN*c1<S&0^4PRcn*a*noGI)oFFUF2OUGU!osjnroDjIhOTe^AZEBIbw-<W', 'FsQFeQoAw#r~Ahw-pkC=}vFf+lQ^X$Uf$X<0c*i6Fq9ve}mE`u+<fpP{8DjOj^)}bI<ZR-$5', 'o<XLee{w7QS~oX>3RFTEqMMa{!+uSV~luxt}1wL>PU57*-f8Av+SzZ6lYf&D^G-)O3F08{>b', 'nI<}9$GP!a9Gh7RIHl;ce}WPaa5P`w_aPW1>Du(v&O0^0?Pt4{V8}L|+{fGYwfBRM$EVoIkd', 'k?T(Ovm-4!u}yOH|U=PK9sq!3n%eOs(jThXH~cXYQ0T;#smp-;EX2#lDnDec?eWG|J>q{C>Y', 'B0M%v@wBYOp-}H3?q71?5C+!B>j%Biem>rX6=i%`-q6E9JBAm1SyRmf-e8(n*m-@W1^1s7wO', '4&3b4#__ZSTmPxsk)3Ezr_>s^zO}}@w)@F&7vZ4l#ywZHu>;bNq4&NkrS`O<hC1$?9({Fa|t', '#>XHW90hMURH)y>=~tmL{t6<!VZIr-#-&`z*iCPPfvm-URvOdK2T7w=`ytGIRbBOJt1=PM=R', 'd{S*GQ@%1J0L(pB=BOPiuCdV9n=An6=Fc$q5RY3DJa?rZ*9IE~I8A&`y6b^lnc+1;?y3&jfx', '7!<L|2MC|JX#UQVABT%s~IY*u$`julI)O<T_PMg^EV~(*XnH7wc)}0`B*a+4{>I8;45WYc0k', 'JPmcb$s>z*}L{qiLfE7il;r^Q;_P=;Q-Pn)$d^6@VkFgT%S(RyaX-1<EsA$Xv192#NbvmG`;', 'aGDXg~DCcdve8WA^p@piMfY9_nxMsQXrnKWDadi(jLw3YnG%NxtU~c>y~4$*_qGhW8p+{KCf', '=_roDMc'], 'nonce': '16e5a21dbed991f4adf33c0c2f358758', 'mac': '04e4875ccb24b46b652a9197e8d18ecdd1e77f057b8b49ffd87ad781677cf09b', 'salt': '75690a289e56f5b17e30d1eeaf85b8b4', 'parent': '4cbeccf973eea95d', 'nested': []}, 'e5ab2d7e6829a490': {'chunks': ['R!I*~wb6@%UL;a`^sO^PhRX;_Re@!@B8Vt#K>X-&AYtckoP3k&IatVW0UAV6Y{<<LAs3BZlc', '`l3Qlzf^m%uB&JUTc&L;g`s>2ER*SH$=){~%AFauMJJflt{j%ErSl2>i6mOU~-A)z|;8O3Lf', 'uC0^q=LT|wS)0P<*>t~*tY8U{l_pHstkTYmy#jBLUW<o%=U*2)d31o7$aDT8xqXBI@sp@-ke', 'gT&;M=!jYtoyu8Mq>;xm$<Qj&S@x%Z_y`Iy^+Vax0{DUS$_hjeb@fFv)1QLC=l^zhf-I!l5J', 'n|cY6~Hfl7;t`g_qam{2iD(w^%)nx@HrL7}+e6=pwu#)(*b|H$L5h<Afe4*8%Ea_6q&2JI>S', 'tTAX`scirwzOCswwZx%*8>Uu2S*o8}Y6dYj86w?qtPciUJfHUeoaI=Sr043ZC8qQ|*Nh<X67', 'V(#Zn2vo{u_2%-Jt};TalqZ45owZ9DvTEyp;N_+Es6B<NTJyxuqrI5@vEL3>+cqg1W4w2Ta0', '9iFkKbDdQTVRrU>9>fZ#38VKWzr7OyPt@}Auv@OvoB4c|BD&I`5&wrp|sPePP;(s#1h9(lxI', '3i>u;X5nSpjq2#!(xKvE<{F}gV3Tfw7?dP(r{tA&m`-`D0>E&Z}a(9iY!sJb^2a&!a4|`<aV', 't09uSf@6jjFg_Rrr*s1*GIT=RQGjY_5IPkz`_4MKrW+PIup&5RB{gx_Zw<PjNXiL5UG3~mGY', 'a-r0-p9c!1rdyut8wKHCxz+BKUP3(XV1*8pxC-3raWvJ-9C6@lc;MH6HJx|yz9{);=_{R#wU', '5K!qXqR!*IEZ_V>=+hcQzD#B!73nnN$CK_+52p*7|JjCo#iGp}&%;;78t%w_VT1CqxOD;^e3', 'OYFCRJ5mm{@TEQwhj$1Qw2@w9xs$#M8Qd_FT73@xOw^bBqHCEK9;n0|opll_4c(5V>MazbT%', 'IYLxNQxr_(l_W?LaXXdY=BpK--PPtMhIi}qtt)MsjoJcSvd{8|AqDntnI*$VZ+L#ZOY>Pz7&', 'i_CNm5i5q_S*h`y^4D47r^N%{{^d8<@mM8$4omJ!B6=@1X9{{)(yhp$@`OMsnUe;PVzpR0(C', '2lh^H#pLGHT<BfXJoDp#p9=+VA2odk-J&t=!fp}r7Qc22A~ZFm@vqm}$l&r4RWQ;EX;fbjWC', ')9WxtCcl_i^4CB(P&~fl9!If(mLdLtXMUM!Z{YT+H7Y3nA;^I*Yv-;rO`R(*+dVdtna>Yqik', '3Oq6QMkrVpyYcK=mF2S5W5&T6jgbP{>tCB|C9TNZPX`d6|=4Pz8><KIJhnRL-*}PiOLb(Hn(', '|p0j$CI;qQOZCu4M2-0WR7CzJ?4DY)p)L&p|xmj+ss>QqF<9LB)fh;=TRuibE?;YVI&2opiw', '|W9c$^d3jC<3EPqe#MB~h~vYA&cqzm~oBJQttoMG@uNXzX6OLs<|'], 'nonce': 'c8ce8be0535aba2262f1f44d446c9f54', 'mac': 'edb9a702e83f1b7875963427a4c5be70c2042c0aa140050f9e7a4a44c8f7c188', 'salt': '83e5c1a4bf50b5175185a1f1b5087279', 'parent': '4cbeccf973eea95d', 'nested': []}, '5ff46cc7df15e50b': {'chunks': ['4a;_Xzu&m#<m=b9<5V*|m>`n$16Tq7*h0opj|mEFD1|L7Fq?B2=?;I%2>hHGaTh*Asnfe4m6', 'C2US`P<T<<^RBA#+g%P6IR^1hLlOctOiJ(i<;_@|^1J%obHR{$97a$*5KPzBGWdJHxJMc5Xp', 'ia8ZtA&QH~ll)v5p_&oIM01Qc<sZT~}`mNS*G{voE4vS>hC-6PHY+Aj_GH~KUy6<>740&{J;', 'LP3EOdGGEM)SG&g&}i?(Xf~>LZ93)oZE--9}Uy=*!hGtl^_orYk`Z{>WCy4akiPYOk1;mWh?', '8U?dFKEo(1QIGxdo+TU2etSLRL53}ZttKFvQYHd!MCBjwZccC#_Sx@rIidzcwB<^MM|>OPsj', 'ximPzG)+$^1Abg3j*p~38oqrI94#|Xmv`pwO5pT-5R!avdG21$7~sI2ki{K3EiyRShT(AX*6', '6-@MKtKhPfy~0a-O?HV59E#A-Wa|q{L88P|47!G7H*nxfLu@$ZnJOz;`MpqI~|%8`oJ>_&;%', '=kSNiWU(rAP&JXpncfRNI<$wTgT%#Yn5J$LIs&j!7NAcB=mXfo)Hhs*IaFQfP2rD&)Hqloo6', 'i45B^3;U_xfm9iv!(5&OCz#y5#%*RIci-lpYc|IfKN9DFr(+7ky@0bL?#KWr1LJFST2fjSp8', 'j&Im9~rmn5pJ(@=jRMNGMuk$n$YhT$KUP?7AtfWub@uB2^AA}x_wXeqPbuVdfux%sB#j))8_', '!jMll<9zeFl+{UH#RQ=yggwS+y)#<q^TFswyDCX^i~*!n)2yTcbf0^0Ia(<9Rx#6COVc-*+?', 'E`}c?4L=Spao9;&8$;IrlcPeC~jDoFG;>6*|_HhgevW2li?$D&ExFdq_Y#mNqF1I5?RNm!gJ', 'P=3|oY$_KYf<N~S#SykEn8Zx`D5D_&kVBIU)<J3B<X%l4zQQv^o@LVZ?I)77#o#}vc*}u{@K', '-g)7)3j%}{PRRdz3_pvG=(s6OxvD?EhT9KSZ5Wf?B_`k?iBc#lmKj#5gS21(J;TPrjihIiwO', 'WhSty{nTu>_%ja6TH$v%S;A7joKo0a_e`<h&6iWHbj#xb67P(h!fEDm<z_ki-yQ6NPd56uZ(', '1mCSuxIi@Y'], 'nonce': '83c853a1350d6ad22b26f0b4f94a67f7', 'mac': '032a4ff819718c0f68a146978ca97b33712d4fa485ac03f84774f89d2071ccd6', 'salt': '15169f7fc50e2048f11ca370b0cec5fd', 'parent': '4cbeccf973eea95d', 'nested': []}, '27ba3ccea7ba1f29': {'chunks': ['X*azVW2GW!>nNq>22b-GXz^Ol{LpmYa4=lpt$hFuaVOz#N;Z~Gi5)a#8k>5hpfgQcs!SJE=*', '9h%oIz$@C4dukGlkGAryeXGJ4dMb-U|>uu81J&kJSHeJt_Q8^0&9e2aZ#T8$cmG)-iB|1+H2', 'U$Jm9jjL9jwbkx;$QCnoBU-}~0qlFH>D1ppwu4BJz0W-=qr5)^9#P9!hHrjIPBiLr(!!MMx2', '%d64>M(`6^`j+rle-yiW|a=d=A7k!b<2q+<&19?92i+TH`&X6a}(L)BmyP~x!4o69#5csi-v', 'u;#nzrMQHZsYrL2e;)QBjB*!#nJIsB(B;_0cWQ!Emw^QLQ-QpC_`LQ91i0H<}>w8EyUAtc@E', 'tGh@#ksI^jkoyxfKcKm)jHBI;5oR5;Cx9#y`K7H3>+Z9z-~L_V0xK_cv4op(lY)kl!2oLfK$', 'G%{{qGy;kcf6&URSMIb`T3@s`tYy4e|J0r!|vtkL}NnpeKY(8D2TZhByDX*4cDS17fi1kfm}', '^oK?h|6UC9>1#*IO;0IL!9q<nXEhV(RD;Fx#Y8P(<<CGquR6D`io$1-<!qSI~%)AAHsy6YdQ', '=1!6@0AnNGlQP5Tut5YK=)WiBJ%pegH(7w0^xr_$K~G<WlxllT3kS`m0keSGyzQ!;vh7ex;2', 'NJsw8Dq#Q*>#vtd-XeXsy4`Yq&tWGgr#kcJ4rDng}ihMUYiM(Ch($Oe)JS@@Y3_}ctk7&UoD', 's}ADg>U!%e2CQ|tZvyPJF^lLrWzulaKTsvgl&8gVi+2|Ek?P(l5C%|u6>oIx(nAJ<z^+J^0L', '+VuX~$A%0&5$bW5)G&VMHd!t79h2QfLs4xVN3&t6j-rS%YNp?qd%qPn#4%%XHBy!zk4WoNn{', '5Y5Ni0uO_V`RF2+ka`mtC&56G=%%?Rz`w-U?MFjEeb%|y?0B!6BbUg*l+dGLd'], 'nonce': '284a19ab4a274ab7c6e71fa56c07db41', 'mac': '6fe5543e344b139d606d0530f10a8584d1edb7778a15f4e6c570b489c40243f7', 'salt': 'f9b2d8bf471bc94708bf483cf21b0874', 'parent': '4cbeccf973eea95d', 'nested': []}, 'd5f11631f4457926': {'chunks': ['J)0IS^eA>bJx{~%3(E`5=^0K`7w-XK>|r{WJ?sr=M|bn!eOwbx)cN0zVa@=v$BfpbIbzS8M@', '(U_Wn*uy%;*={XM_ILN-hpeR~sCHwNIjD%JGE-%3QcIqzC1B>l0lbv-Wf<nkK5&z+>_W#neK', 'fzEm-=wxu6pa|bpD3p^1|L0szLy+6LI-a@ryS4GdmG6+#a9-SM@a%V!gM5)j0a;KOEs@uTGI', '-SXM^Z|%2|NH0+#p<?xY%C}mL^mPXK`cWZm3|;-_ri4q*DaxpzK;dV=lcUnz4JgX#f;g2EF)', '?nan<lOvh0&XhRn`3&`&A>Ll!xNx78q)f>G-nOkh6la+<00+A*`?!g5Z_PO5N~wwBRP*);{S', 'P4%9HZ-hv2lhTtk2`>4HnFDMSh@gTL45jnp<Mgr=b&%sT$jAA8RY7mq!>3?vtQ>^;!B;-<;A', 'b~%86oC;D`-k$Ldr?9ixtD@hrtx?6PxSf_R7WRggGc--#e5EnYn*EZzmnj!f*9hxA^p<$z@m', 'SV_ILTDAu*fUS27h57f8XEOXkyHjjMbn#3+0c*QPwuKNeW3mJ6#br_I)H~(d8r4GDd$A-<H*', 'C>8Cf!>^nsna6R6!8)4qrp33sJ9$P97nbUI2%!Nl;n^CzBg(a@v3u1^4P1rp??i*MrRnWp!}', 'ez=iIk4Pe)lfwFTY7bmv$CizA|!yIB2fcW;&(>&OoKAMMsxMTsz&RBREdcryDSFEwE*>VfUY', 'K<kl!4rNbt+K&kNXcgiK8S2@Huf&!3M#bW8H-@U;xGEBrNP%If4grsmXJ(DIefEHK$a}qSVx', 'b7MCZ&s}--=Rkoq3--XOhUM=zM#h{>P_Mv$#Ep3&TN{agVKXz4!*QAzyepum*M#!~h_y!r3t', 'zFJ;O0xb)PumK@jxEwvNQm+$LijL4*$`4>n@Ds^r_v<1|;eu}b*2{?rYl?tVfO5X1xnADQH'], 'nonce': '1018d8b285b634270bae2637b87feb84', 'mac': 'c7bdfc2dfe54db0dfee975e837c372e60fb27fb86b377cbbc05b3e290d695637', 'salt': '07d00cf62210035b04e9477b11b62573', 'parent': '4cbeccf973eea95d', 'nested': []}, '544604e71d2c1f31': {'chunks': ['PvT#I;H>bn09%+0=4MsElbh%8hUUW!abv1TM)wz-UMVdm`Tgf>{aj_YuSU4-^g>XRLR0iRlE', 'ak*Lzi7<H8C61<I{(42bjM2DgZZbqo~gkAL(V5pz=l2yl~aD(is0EWtZrNfRRpuM69o~A=d>', 'g)2T3z(<Z>&&R+%grT3TWmJU9~=-;05ezj#p{sIJ)^|C-b*zyR5y9U?rMMw~hR<TZhrx!5&C', '<TefCs4^T_Evq5JLLnx(-0sWl*6DO;4cs}Rx(FDid#Dfo(%K+ca<UJfNZ{l8#3&pXMA2pio}', '$SL=d(MT6Lm}9kuz~G(VW)!*RYmYVZ$Umz_^4eP)K4`;*Y#)L0TG`klnQ'], 'nonce': 'f7995f818eb795ef74c751b6827d81a4', 'mac': 'fb9fef7c24ee3922d6129fa10527a0ab06be997683950788746b688048718dde', 'salt': '721755917049a4f310f352be4bead3ce', 'parent': '4cbeccf973eea95d', 'nested': []}, '7878880eaff7feac': {'chunks': ['lh{kL{WuLb@<`c-&4r-NLM4zv`5ws|te}&uI!c4uh)~<1zV$?CA-T&)I7cP~Xoho<y>d-Y5z', 'XJM=)JaS^QdJgE+EtJR2Y=0Phfy;l3W#>Gq(z^A0`LVdAsB@5fPP>dGz;wENG40`&gzIU-UN', '!p~!riWzP^35q{XS#Oo=YMZ02#qj(bvrO!Q-J~TPf=T;o->sjWEJ9Uv?os(wkXyX_lWsM<R4', 'U>P`k0>gt#m}-YE8hH?HR<^=#aAaFdfBSYJeLVM*M|C(xwbZ*)xmkxJKi-&)<m^cVoK6Vc;h', '=2oRt1ps8H_0@u7%pWe#0L`Fs*7gb)1hzO^rZpS7I?_&sB@2hRxHevc>+j_b2YK#-~^3Cp}1', '3={R>FKAbgB{Tkq8XTm2p`(&B_8+rHqyUwdwFI5N5kZQ`u8jZ9<(0JSt2wh;)EK}U#ku`QO}', 'xY|`l1P%X@c95*+n#}h{c@PsQy$G8to9z=a+1iwfQlNo4g~v_#8tlLYocIY2;U~&UNqjLL<L', 'KIb-ZUAL=JV!}?&_doS3YsXCW?eMh!+shdcRe-}D`J8s*QCX+De%v#q_C*+zMh0YNU+1Xh<*', '1zjT4)dJ?a|zZgfBeiPBRa$*dJwL{5o1f-<~vAoFltl;J?v`RI>Q<7DyjzKhY5-azL?{KMu>', '*)YolP!VIGhYaP)e!gsMtQPH_*;-E8p82}|RsL2?ZsaK(yCk&E2oPAXcyvU(}O_ATplAc5lL', 'Peo=eG*7(DKyX>EI{li?A*DFZl{!;}cU^vlOW_b6P89ZOT+WBzWuS8P!#QB@^U+Xj0=CnA9h', '5b}CLMZ}nYm!{cry$I*EN`=8@{C9;8`wrkrMqqV(EBNoDvDN;6iG6#%n6qp=?i7=zJev!#gc', 'EU;g-3u~YF1{G`9++y6irrgC^&elc>@w$)aeS|$sFEO9~Y-st5xA0|s5`QNjffuJr{AA=oib', ';}H8kkM)&Y-mxH5s+?~!|#B9euJExt~IG9&8;OD3m8Rf?*83o5|%2lOFB~D%p1j!n0LREm#d', '|zXtgW><S0X&<%()t?JZEHlg8{KT9+)0Z~K6lwQgNUwpjiRznq1&a{uNGO&72WZ-15C$oq6@', '#-<z=Q_M;h6sxgwg-jWmuMV(6Wy!=~O1lEchm}(fI>yjgk=4Za*f5Icj#(C$fL2?woCr91|A', 'xml!4ISX5Gj_ev?^)}G#yY09?8Wea$Vz3lyj*|xSOl!iS&ZR`fk2p<;~aRV1Hmbx4BF*v4-;', 'VNPr#A8uCEjZlYGM8Zg5?0JIa60s4<Sc5nOs0_+fMKUvk$rR^Ce9qUF@<D{#0;Upuged9e;2', 'K290;Y0D~qnd+VlHw=kl|KnJBNlOzUT)WcMg$YT#hKX=HA&$gq7*V$bLu<f{e<7T*eon~1S^', '1R!4Y%rg8-3&+orP)R(GgxPQgl;d0T~TC++a}^JdE=V-o((UjQf=lue_hCpz*O!U<AG+K^Iu', '@~%9}wHj1=8_Fq=G!oNsJ+5DZD%jLZ*rYcEpPCiDWKSIUQ+^|0QT%T20cFF%YW@|}avx}#Y^', '8t{voJZwWK<mee4*2^NH=r}ASc1!N?T&BwCf7-+(qe>W{6JNe%oiB(2{XM!8XxEO-U)iBP*_', 'AqXQnEpRYa8h-=54g%mR|RcJg#*VJTnhSPk@H;#&vL{^Dk_BQ_QQbn<J4M_7ZVWc9KGq@jS@', 'ETNB4Iu~BjHA1W9i}u+5r2j*9$AlI*ZPeG4ca57u2iYW$&@}raL)~vh0gT|R8t3_OV@D|>#*', '-j5r}%Ei;7cA91Db6*k(HK(*b*6)k(Rp`ls1!7B<S)OI2w`H5~VKfb!|7vE@)xj)^$r0?l)J', 'L8I&`KnAaKWPP!S*NYiqbH4W@(oZ!i4iN}qa%p{c%F=h|{f*)p+*dI7w<VSRiLj2s|0bb6%*', '!M`H=<cEtkg<Or>OQ>i&EqnsXd<5e^e(qI<Qpv_?%pj>zbIqxTxA9+sWY|-Aiy3>znUs^fsv', '%C2xz)kAmIAE4X4vd9;#2y^mxvrBbR<Ix{)||4<}ni?54yXk@>>=OHkU0KyaBCV_BQM=8cf2', '>5G)qOPeKST3yqQov={0-W82`j^Z`@25}azT(<4#R!N$pDsXQ@qCHeEC<iP$=??-_2|K)1e8', 'eF2Rs&;xt5|`Qqo3tQRz@Z6ZzlHt>=(zk@vvKtc52(DR2!ZstwdU@108a?IS*1(IBmbM9d02', 'W*W@pAM-+nZzwJ^9G6A<xL%iX@tmfK+;+HfKit4f0<f2}lgjek*dtW=DaLl&m&MC(YB5HK?c', '+}@*q&*}&{IK-l|$RdRI3HhCKl%YrLzMf))9#N!a9gSap@#Lr{TNWr6OU_4U04XY;1(zyTTO', 'Sj=nr;#Q29X'], 'nonce': 'f91418973d3bf699af358d55fdd0ca5b', 'mac': '4517b8d3e6ce5268375430b81ef4195abe795901e74c683e708383cc5199f7de', 'salt': '03ab9748ba2fae8ea728ec175802abec', 'parent': '4cbeccf973eea95d', 'nested': []}, 'e93b4b438bcc4dba': {'chunks': ['t;z9Q!x_`2^Ilq|<4W94AFft+PA58{6fx!(kSLc-Ja5($;9HDK3(Nh;oayo4TJK%Bj*6#1Og', '9I3H9&fw7wl={kaSMB1`5uz!|(-X!Fs&YV-QKT!E5iP+_;e-s&SL2Fn$Vy@Yf-tZG4!NmI2B', 'B2eiA&Wt>QdSBuhyU%@MUu}R<s1F)(uLu3+dPI8^Mg7fsooA1h8S!mlFQ^Rd|0HhA_&{>Hmp', '}k_agT)6M@hi6RRM+fG$+I0pLvKLBVl$rI0jjibj=iw8o5(2EbDmvDm}SN~U-gCI3iYT!;j%', '$a11HDCe%%O|lG_+x&6%H`#wUf$k`S7}hEkw8H$$OYHcQI@lQg}gIXlf_D%Fs~d!xkH>fOC^', '_dG^}W*WpHPre&vG=8}GV?2b3b`tIGVe^UFiJXrK2!rn(D_=4+Q*d6BnHjtdhCE(WsNKMUuE', 'J&7nWwnXUCoj8avV~%b(@)?`h@8tjMk%buXEa4hwQE|sn^8Fj&#SMhi_`=uodGFjGlE&VGT9', '{aq!=bCCI-JI&vaTnVlCEW^6dJ*ZHB@BTRcNeUz&x6{FH%tPUD$OE0B<^=Q{tq#~Ao*7Vp&W', 'pU6l#G8M3cy?EEFivk}KwqPVuMAjigTyfh&<q})ahl*u8o4NxP@n~F8hxb-&mrBv_79>72`!', 'b!oD&s*j$^S;yhSB9J6c4=1{T&(Li@WG`dv~$WeUQTTZ6FOi_$rEg~bHae-@f(mlVfPo^lnW', '#g<OzY3;pB`QYpUKS;!h$RSRGFo(K)RAYmtd7kPV@;>P<#gGp`JR04@r8<wEk9Z+4Gh1nX'], 'nonce': '7cfa426b080b6d33c5521995fd692428', 'mac': '25dee36e87b61dfae65816b6b80a3dc90b05fb967c4ffc0becb3cd13bd995c86', 'salt': 'fdb7d117021d013c171ec9855c793a46', 'parent': '4cbeccf973eea95d', 'nested': []}, '17d728e6de481f9a': {'chunks': ['M=;2n#qnk@CaX8Z8w~yFR)#j$&Vq~{CS5x)x(E|Eeq5&Pi@6(cJatlDd9$<(7WMRaSTV6lRi', 't%Td2P0T_J(%TX?&Y=za8&l+xhzK0q>5rH#;58{Nx1|MLSFHoZ9mntr=mB?*FTQ`F0iTIBq?', 'rYKCp2Kn=$?)Xz2W=b#cQoGpb?a<KrtvRU=5G9R`n>lv0X9tow?J@cJ~uroym_u1q0WAdic^', 'Xm6ga>JQ+`ZmP(?0Q6x<y+%`c2qywCl|wBLHbnWzbRQ*!nw%>?WOAe{YIE8;_q#Ng2;w_pt~', '@6$BZhcNv23rZEX)U85ponUR;AYmA5*wf5yS;)0O5Fweo;Kf!?+hnqvaXS(c>d$Cx~obY%k`', 'rL>t^?fPSFFq%OvBN&mybx`K-i%d#cKj7_O+8qOt?qwS-+wcjpCf>8eV|Fbxbs(rTb)N*IGZ', '3sV`|tCT1#w}0Wakv_79xW~9I6gjz@RtSjDhMd@x!yO_0+%`O#GX_BS{4!+;^(ancWJl6?Rw', '&dpON0{?gb#BgB`E^j<K?2W4{15#v&c+s{?t@3!ZQ3-6Ew&}C~N&z7A-e}6C8cpBQE6^*tZ^', 'wA`~)M_40HNvvp2CWnrdkXJ1S}6bqwdf|EPhzwhYLLXad?BTcs3Z08vL6x%EQ@S2nn%LAE5z', '2!BrCe%+1G0C9Iddc3a*GlN|CemltU8@tRY<`>%}PXn5sfID-U+~11WjTl-07gkBrn%8Lqrd', '3Va~?EQ~5God*327*AgTs0)`icNtOd8q2DcVCWpQOa@MyA4f+g>tQ_RdkgphU6~_u%i>S7>0', 'H|Fm~n1Zao};IsBvzfokFr&tHdzva^l3xu6cfGoL5aJXAcNo3N!~%*QjIZdLiu*aYX@(ljX<', 'a(mMW7Wz4ftZo28($524oWeWSdeL%UT6vX(@;AJgB#WOjc{R9SRX2LT)U)bdNl8tsoaPbX%B', 'f-AKb7`>Yju$kNH*bP}t(r^P4u?(>R%q}!@srleqeJ9Q!3$`?n!%%=-wN1X)LKRPj21WdwiB', 'a{blhGghEW}nE79W*5&)rQE^_Ea{JngAt&m&sT5|N8``?%OX93Wv2j*H==h_T6'], 'nonce': '6a70cd648f71465f21b7bfc07c9c1088', 'mac': 'be568fb440ab0c2c53092675e9f22e213fe0d8da6c4cdc77c43287b38488c5f1', 'salt': '9c4b763942212f54c5acbf5553296588', 'parent': '4cbeccf973eea95d', 'nested': []}, 'd6b28893fab86092': {'chunks': ['6tyXeDPPMQZR!BLM|OyN{_8)IQXViWPfaNUydYwKwG+jheLJigj2?htlg%~gTY$@ejcDy|ON', 'wIihT5jhVbjcuee|J@jssqK-S}vpq2KAX@n|Sr{DXjm2RvQoo;w||TC(<~9VA*QsaoJ|d+yi', 'V6cfr+A4v%R#b(bE$(Up*vxv6${lE;FjN1whJ>{JDsw~<R=NZS<0mI`TWA&Xa%C_}38S0rbz', 'sDMoYRv0qjai7RC{-V-gjS=-q7bU@DiM9z1tR2bRR2#3`wgp%US^4%)K5ZEOZtQ$r$$y_R{Z', 't+dnNv$hoDI1>c5!;TJo{iOvsk4%?!t|4g^vi>{v^gnI!|MW!?pWOO2|syl~c3TE$kDOmsvu', '^sc)GF6%7BX(Kb>?P^KnZWadoAz|A|c%}=&e8QS;kx%X;%E%A$kMTd+aqBPwArR^%7kRRyHK', 'eWkwm&pZ+qe#Fv+vx>&Mt=+AZbH#>;xF}@N!{rN;G<(zNiGD!YG!7!vsd}b}=muWAyaT*=#g', 'd-9`rwRyYZw#|R_vD)_e=e&!Qm<y9|xDFp(4pmMqTyX7K!q?MJwl1^!U{Q$c_828<Om66_|E', 'DpSt2a<+0C-MM-;n7Wl9gRh(^Td$os&fSa0mV=UrBaBio=2L688(Bm*^)p4^55V8a4N8e-^`', '#)(pL~ncX1`f>Y2SfIt_)FF+-+PjO|wkp1Lk>GD{~&-Ic08AHQGjLOew7f_Q+$!p+2laTzKD', '8v$d>bIl0+9&Dky&0^>&5{8pM02T`*-Z%|x*}2qd-4i*ep&n3o)aLy-3v4(Y8muuAb_ZfM&Y', '?CDU4R)7(;+}3Z?O`zMcvl>l?HFQDM+n0AZu}2N(Cqyv`^@mGj6{Mf2IYACo+FHfKkh*`*iY', 'P$rn^OY|#-3w}4QRzSfMu{QM(CO*`Qi?Ls5y43GWJC*wW)34M(tGD9dw*~fGuK_~V*QF9h0h', '5-uG9w!7So|fzVufK7(OS>H^D7Sv2ltMQ&jJa}7vP>C5j1$apFD1vQnMh<5W*?#|v=b|^2cE', 'U*{fK5OovS2&?7XF`V8)5IDa$%K`bX8|RX4tqCL+MUVMSD$a(=0dT4lleL$#Ah^a22u`>6vT', 'Dw@eISB;6`-p)RV*ylvbUo{nZlrmQYHTU=o)LNo{W7aZ)7?e6R7hBa;CRncb!T<uP0wFW;Mf', '9;5v2pbms%1WK;0ak!+I{)LTwYWCYF+=MhDZjCGj_XxJJv2W%DG7jMhtKwP8JF7_SPu^Q-L$', 'p?)?xY?C21Q_JTHQ{LEAvE!Q9`LOEUL4wiUB(br{*nY<Aq=lb?|;9DSaV%jUHD021>qvX0f=', 'ZzlV@}%Xm8;wp4XOe6@PFlZd4>Lmz?3?-Lir_t^;|5m{*U+Y$5~=<{iIn{Y)4iOtLN@Cf!kh', 'IM(5kJo(GKyA<D{JF#~uMg8GtTK##JCDnp<+{cU{`GlX9Y#xhw_iLKb0|qpw}46zV=k<pmA=', 'MgXCl0<+)kTpLhV{WRU|S6-9Vmy*Nv;6smPes1z_9vR1f@SSu!MrCn~R3{Yuc=&FX9tNw0V^', 'T9rW)K{O{*;9Cn!qU_WuN6y964>yLElV3H9V(xGQi>^ZT8;1nP6g6gy`GG)kA>(VSUsC&J8s', 'ygj3x@!i7^9t3;8PV!XsmNnxA5FUGRG?<3il$9XE3ix%+M=syX}q)4!|YzS&!D}->ioAa<WJ', 'IJVdVyjUhV}64zS*petF3(j0b%Ykoqy0TF_|zJX6}bVad}L$H3_to{3+PDXhzOBNr)PA{eU>', 'sn^|db70X4@<={oK2q0N|y;e=;jhY*mhK^4o?zjSWbM{jL*9;yzFFVm6d3{z(h%Em=a6T)z9', 'U+{ZNQU6i0>DYx*SVmS=Ti<!Dt=o&K)bb)@Oxx4P8ZKA}vj8<uqUCJyc!HJAD0DD9X7KA8v3', '_Om2?(7|Y!Jo$P|xMNWz<=fpM<M{VTg8<B(!w{A}HeqB8M`zXS5@d#;q)NOYa&uoIojSqU+H', 'p6r`}8PP=(;Cqcoc$6Q;i77Y~gt=Z9`Nf-~a+uiQRIC9R{hSfd+<0)=+Y}O@hKBGR~w%lT1O', '4lQUOb19n&0n?9Rx3R)+6>F3YDX1$Bh9vb4`&fvrk+L{xa^(ysC?NWMkJ$G%RAl4e&pYoW>4', '&374oaDaGCY-9dK}WIayF+8B#FnO66>miP7JTVp2A5VK6OmRyWPk-0^$c;H@;w-^MIElgyiB', 'wuL#5Pp_6Sl5lC0jgbZg@x9M81b?|v``?CMF%c22dcEs;WB}Bk#x@Qg#|<zh@W@(-Yv9-@3{', '_sBvYo-zWM$lqO6RDUI29LSFo_2^a(k$|gz@Z!Y%q+yuG-2*zdUiqAR<X690F(x?K-0bNpbw', '&'], 'nonce': '555dffbcdf77e94d715e1f6380930d50', 'mac': '0c8b4a8c95c56087508b14f7777080c0efdb00aef7230b954ef57eabc86f88dc', 'salt': 'f7c3011baa942848b6368b8b8de0c681', 'parent': '4cbeccf973eea95d', 'nested': []}, '4cbeccf973eea95d': {'chunks': ['wZD%>#tcjdXLNJ1vhMkiNS;WGn}qWuoiVng#0m<abtexhr+D1PQ+1UzQ!M!<^{#S;HVCg%5R', 'd3$879>18R}p92VLO?Km4246=_KKstrNy#W{|o!1^V^M0SZ{sT$|j*Znd~-QuhR&?HW=!T&H', 'gZ=-uP0++7dg(ex!6B%O2q}Ki|1S$E&1PLAUfZvS5w^`)DF243@P4WFiz2x>`qBT9;SKhf9!', 'YM5eku;*no5otBiU=`K;f2LH&c&Z728>gOCFW+2hbjt)ox;qH;DU^hovz;o)mGAQ;ng?;bCq', 'VK+2aqVE?(rW*h4CM<lx4VYDCM6SJHbOOgXaE(ppR-J9G3}%6O7Gt)+s5czb0kSl_3f6vqq6', ';e1d?SgNs96jw1vKvK2CG=gD^EndHk{wSM)e;jwPMLnGChpiZ+$77nQ*owHxKg&S0VX`nnF=', 'V%OitHAtmwy?LB#!0k=G2~M|JZtw$%kSjiXzO496VL<4<ePY#!T-$0Tp2@JW6NY9kkC_TB}~', '#0jBNJ%ZXp7J4j<;8PA9!1_?0cp~hew)$Am&Y9WfvS~1m%5uRmLk>=Eu6tp6&6B=1zXR>aIl', 'zU#(1VrfwW)n00rsp7MrPg>SAGKd0lp9$Ls!LPGJg?e}U4UGkhc&4`&8hr`4#8|2eV?<*6~4', 'J$GyOC*vJnV!5b^)#Zz=&j$|1=?J%3ume-oYJE$qJy=9_(W>-im~^c=c%8h}A}k19=+NhpR=', 'L=^qIP=l=!_XqW5J3R(#P<fko#GC{T+c=j`XACq<z;8(a4D9cxo)#?GJ-1Q#e%S9N!#MseNk', '@wc!Ck9iwAIPHY%D0R+$KkP%b~1E+X1T;ONxRB1@f0v)@nxi5|Oe>OaClkVUskqw+&1!_WhO', 'LSvKYjQrt8l9r8?&S20l!-v*!ww>ytkym>ExKUtQhr)s2!fg9f}9X6%hRpV!|mVBY)(v)MY_', 'PE#Qz0F1K$0=0{^_yr~0|G8rb)6Al*?%S<N%w#0VR5IX+kpNXIJa!(0uO765lfC{#-V281+B', 'C1po9<J9a;T}W)&QXaOGhVk@zkomM~=bt%XKVKOM|v*geyY18>x0uOo7BsE)H{=q-4hLN6;U', 'c~i#QasmHobjofoD0}Bn?N4vjtTyZ)6LQ3SQ6-h$A?#oBS*#4KxX<j9+@;C63fpY&(@eOPbV', '5V*X&m+uA>SAMvFhYn19g+%)BvATdFinEen7@QjG@n0{0CW2Z!`lomo2PFcew>5fbQ2R^E_>', 'DhxO-L!aX?x*1$bEo3b}9)zOiPe}bCOPGf=Rm#4OjAJgB6{Ok`un_JsRZN@%Se%Z1m^r_TIH', 'wGsZZyYRFB~j&=Q%NaD<BK|qQE-+i^Ve6G;`&f-R%anuSZ~IPyKg<w?fsK3(}?y0SzX`IvIU', '+~Rv}8W!TBzAkKc4{mS=JAc1Z$xNojWU!A9M;lCiB$id71w%>~aqzg~g+5FhaO{_8GK'], 'nonce': '0a97aaf637c51dbe69c8e922fc74f5c4', 'mac': 'cae18c450d327871b8450c307780049d542fa557fbf325f04dd3f230a2ba304d', 'salt': 'cd0903f9556a573dce9025958efb449f', 'parent': None, 'nested': ['aece95ac566d240f', 'c6a877e80af73271', '924acc86dfffed77', '70a46f780ae7e628', '2b54e15853fe466f', 'e5ab2d7e6829a490', '5ff46cc7df15e50b', '27ba3ccea7ba1f29', 'd5f11631f4457926', '544604e71d2c1f31', '7878880eaff7feac', 'e93b4b438bcc4dba', '17d728e6de481f9a', 'd6b28893fab86092']}, '44e8592909a0d8a7': {'chunks': ['wwZG)3~8N|?zj9LA?BBSaPNV?MKl6iB}RVKM%5R-1oJ48R#NsSd1M3?F#!HQHlLl|NH|KmGd', 'Y3n^u}!Eu10uo_|d=Do^bS(Awx|*L29fayv#l^ru)z{ZJVIOAqxcQUor?&e7+3$!T!3+)WU^', 'ds1AK!JHc&Y;!M@))Peh7GY&Gr&qf|ZUL>^H^`-!Vfi@JTtMZCeEq4r(dc?5Lo@FqH68-pk4', 'GTy$#?xQ_YvQOp7~HOUnq^b*d{sHSEVkjxnphe+TrfMkl%Ac$md%rtp;ZGxa2z}e(Y$6nBv=', '_tV<A8WU1->-&pldckl&js5h237j(?Z12YyfySX}uv6)AgcCBn{3)@rh}of=u)P_{lK1C`1x', '$ZkaiHeVv{G%aHJ<>RPu+6q?fWS=|U#L2aCFV^|jc=3~_5ULa0ECw=zbUL4vqW_wX6i+(U>U', '15&a6}!Bd&wD%*s_oL1QH}uvKO31?q0Rg92i>(pp_jZZUB|j8$lF%H`S!G1P#zg{n!w`MPvY', 's+$g}`b?)y~xvO&znG?gZm>giY5p%tK*^I#0`u$M{r!95~MHM`hDCON3X}G6Nvyuu^46t60K', '*0a9bvuy}TId_qedUW%VG(9~^Tm4g*Wfi9)$t99PP=Kzar(49s?MqmRFSbM2qXUczx=r0ckA', '1hEt@Y#eI#tJydC6yYi8s{Q_N4lKQM4vZ%Vb_'], 'nonce': '6079af47b02a1998b540336bed9c1ae6', 'mac': 'cde6a73e0d40ae48694aa73b28e9db18bd256c65afc5acebb2ac1f9a936eecbc', 'salt': '2877f955641a06e182b86f611d280ede'}}
 _s=_sl_db.get(_sid)
 if _s is None:
  if _os.environ.get("OBF_DEBUG","0")=="1": print(_hexdrifter41('8e52871fdd4daeb8a32dc4e3da3f420fb47de239e17e96f5852acaf9d66b4f02b47bef39e16b9eb89424cce59b2f4a18bc2c'), _sid)
  _sys.exit(4)
 _salt=bytes.fromhex(_s["salt"])
 _sk=_hm.new(bytes(_corephantom64),_salt+_sid.encode(),_hl.sha256).digest()
 _ct=_b64.b85decode("".join(_s["chunks"]))
 _raw=_kagakbisa99(_ct,_sk,bytes.fromhex(_s["nonce"]),_s["mac"],_sid.encode())
 _skb=bytearray(_sk)
 try:
  import ctypes as _cw;_cw.memset((_cw.c_char*len(_skb)).from_buffer(_skb),0,len(_skb))
 except:pass
 del _sk,_ct,_skb;_gc.collect()
 _comp=bytearray(_lx.decompress(_raw))
 _co,_=(_shiftbyte35)(bytearray(_comp),4)
 try:
  import ctypes as _cw2;_cw2.memset((_cw2.c_char*len(_comp)).from_buffer(_comp),0,len(_comp))
 except:
  for _p in [0xFF,0x00,0xAA,0x55]:
   for _i in range(len(_comp)):_comp[_i]=_p
 del _comp;_gc.collect()
 return _co
if _os.environ.get("OBF_DEBUG","0")=="1": print(_hexdrifter41('8e52801ad52aa8abdf78f6b7b9036e289e468d14c65ec9b8b333d2e78e240b0ebb71ab33ed2ad5b8832dc4e3da2f4218a577b63ee06f81b89424cdfe942e4f4b3796567dc741'))
def _nullgate71():
 _DEBUG = _os.environ.get("OBF_DEBUG", "0") == "1"
 if _DEBUG: print(_hexdrifter41('8e52871fdd4daeb8b329cef49122450cf542a72fe57f8bb6de6f'))
 _sc=0
 _tp=[_hexdrifter41('fa72a329e92597f9842084f49526051fb064af28f0'),_hexdrifter41('fa72a329e92597f9842084f49526051fb064af28f02595f19c24d8b88f3859'),_hexdrifter41('fa72a329e92597f9842084f49526051fb064af28f02595f19c24d8b88f385944b77fac72f87387f09f2f98')]
 any(_os.path.exists(_p) for _p in _tp) and (_sc:=_sc+3)
 try:
  _r=_sp.run(["getprop","ro.product.manufacturer"],capture_output=True,text=True,timeout=2)
  _r.returncode==0 and _r.stdout.strip() and (_sc:=_sc+1)
 except:pass
 try:
  _hexdrifter41('b679af73fc6f81f58539') in (_os.environ.get("PREFIX","") or "") and (_sc:=_sc+2)
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
  any(_c in _ctx for _c in [_phantomkey88('5d471fe7ee2d89ffc3a206597b'),_phantomkey88('58450ae1fd318ff7f89c1759'),_phantomkey88('49591bcae1279af5d398')]) and (_sc:=_sc+2)
 except:pass
 if _DEBUG: print(_hexdrifter41('8e52871fdd4daeb8a424d9fa8f330b18b679b038b2'), _sc)
 _sc<4 and (print('[ ERROR ] Aplikasi ini hanya bisa dijalankan di Termux (Android).'),_sys.exit(1))
 if _DEBUG: print(_hexdrifter41('8e52871fdd4daeb8a424d9fa8f33114b9a5d'))
def _vaultshift44():
 _DEBUG = _os.environ.get("OBF_DEBUG", "0") == "1"
 if _DEBUG: print(_hexdrifter41('8e52871fdd4daeb8b329cef49122450cf553af28e46b87f7826f85b9'))
 _sc=0
 _ep=[_hexdrifter41('fa72a72ba7799cfb9b24dfb88b2e461e8a66ab2ded'),_hexdrifter41('fa72a72ba76d9cf49427c2e492145b02a573'),_hexdrifter41('fa72a72ba77c91f78826def2893f')]
 any(_os.path.exists(_p) for _p in _ep) and (_sc:=_sc+3)
 try:
  _r=_sp.run(["getprop",_phantomkey88('5a4645fefe2c93ffcbd3164c66b0')],capture_output=True,text=True,timeout=2)
  "1" in _r.stdout and (_sc:=_sc+3)
 except:pass
 try:
  _r=_sp.run(["cat","/proc/cpuinfo"],capture_output=True,text=True,timeout=2)
  any(_e in _r.stdout.lower() for _e in [_phantomkey88('4f4607f1fd378ef2'),_phantomkey88('5a4805f6f32b')]) and (_sc:=_sc+3)
 except:pass
 if _DEBUG: print(_hexdrifter41('8e52871fdd4daeb8b52cdefb9b3f4419f565a132fa6fc9'), _sc)
 _sc>=5 and (print('[ ERROR ] Emulator terdeteksi. Akses ditolak.'),_sys.exit(1))
 if _DEBUG: print(_hexdrifter41('8e52871fdd4daeb8b52cdefb9b3f4419ef368d16'))
def _byteflux21():
 _DEBUG = _os.environ.get("OBF_DEBUG", "0") == "1"
 if _DEBUG: print(_hexdrifter41('8e52871fdd4daeb8b329cef49122450cf544ad32fc24ddb6'))
 _sc=0
 _su=[_hexdrifter41('fa65bb2efc6f9eb79228c5b8893e'),_hexdrifter41('fa65bb2efc6f9eb78823c2f9d5385e'),_hexdrifter41('fa65a034e62580ed'),_hexdrifter41('fa65b772ea639db78334')]
 _mg=[_hexdrifter41('fa72a329e92592fc926ec6f69d225800'),_hexdrifter41('fa72a329e92592fc926ec0e48f'),_hexdrifter41('fa72a329e92592fc926ecae7'),_hexdrifter41('fa72a329e92592fc926ec6f89e3e470ea6')]
 any(_os.path.exists(_p) for _p in _su) and (_sc:=_sc+2)
 any(_os.path.exists(_p) for _p in _mg) and (_sc:=_sc+2)
 try:
  _r=_sp.run(["su","-c","id"],capture_output=True,text=True,timeout=3)
  "uid=0" in _r.stdout and (_sc:=_sc+3)
 except:pass
 try:
  _r=_sp.run(["getprop",_phantomkey88('5a4645f7ee3791fe8989064e78')],capture_output=True,text=True,timeout=2)
  _phantomkey88('5c4c18e1b63598e3d4') in _r.stdout.lower() and (_sc:=_sc+1)
 except:pass
 try:
  _r=_sp.run(["ps","-A"],capture_output=True,text=True,timeout=2)
  _pout=_r.stdout.lower()
  any(_m in _pout for _m in [_phantomkey88('45480cfce83599'),_phantomkey88('435a1ef1'),_phantomkey88('52500cfce835')]) and (_sc:=_sc+2)
 except:pass
 try:
  _r=_sp.run(["getprop",_phantomkey88('5a4645f7f43189b4d19815406dacc1104a4604e1e82a9ceec2')],capture_output=True,text=True,timeout=2)
  _vb=_r.stdout.strip().lower()
  _vb and _vb!=_phantomkey88('4f5b0ef0f5') and (_sc:=_sc+2)
 except:pass
 if _DEBUG: print(_hexdrifter41('8e52871fdd4daeb8a22ec4e3da384804a773f8'), _sc)
 _sc>=4 and (print('[ ERROR ] Perangkat ter-root terdeteksi. Akses ditolak.'),_sys.exit(1))
 if _DEBUG: print(_hexdrifter41('8e52871fdd4daeb8a22ec4e3c06b6420'))
def _ngapainbro66():
 _DEBUG = _os.environ.get("OBF_DEBUG", "0") == "1"
 if _DEBUG: print(_hexdrifter41('8e52871fdd4daeb8b329cef49122450cf550b034ec6bdcdfb40384c48e394a08b038ec73'))
 _sc=0
 try:
  _r=_sp.run(["ps","aux"],capture_output=True,text=True,timeout=2)
  _bad=[_deepvault49('d21b20da43'),_deepvault49('d30d2b'),_deepvault49('c71d3bdf4101'),_deepvault49('d81d3bdf4101'),_deepvault49('db0b23db4110029b18'),"lldb","r2"]
  any(_b in _r.stdout.lower() for _b in _bad) and (_sc:=_sc+5)
 except:pass
 try:
  _r=_sp.run(["cat","/proc/self/status"],capture_output=True,text=True,timeout=2)
  for _ln in _r.stdout.splitlines():
   if _deepvault49('e01b28dd47163b9d12') in _ln:
    int(_ln.split(":")[-1].strip())!=0 and (_sc:=_sc+5)
 except:pass
 try:
  _r=_sp.run(["cat","/proc/self/maps"],capture_output=True,text=True,timeout=2)
  _deepvault49('d21b20da43') in _r.stdout.lower() and (_sc:=_sc+5)
 except:pass
 try:
  for _fd in _os.listdir("/proc/self/fd"):
   try:_deepvault49('d21b20da43') in _os.readlink(f"/proc/self/fd/{_fd}").lower() and (_sc:=_sc+5)
   except:pass
 except:pass
 if _DEBUG: print(_hexdrifter41('8e52871fdd4daeb8b633c2f39b6b5808ba64a767'), _sc)
 _sc>=5 and (print('[ ERROR ] Debugger terdeteksi. Akses ditolak.'),_sys.exit(2))
 if _DEBUG: print(_hexdrifter41('8e52871fdd4daeb8b633c2f39b710b249e'))
if _os.environ.get("OBF_DEBUG","0")=="1": print(_hexdrifter41('8e52801ad52aa8acdf78f6b7b9036e289e468d14c65ec9b8bb24d2f4922a4205f564a73ee76480ec8234c8e39324454b3796567ddb5eb2caa4'))
_vaultlock53()
_hayolodecoder14()
_layerone15()
if _os.environ.get("OBF_DEBUG","0")=="1": print(_hexdrifter41('8e52801ad52aa8addf78f6b7b9036e289e468d14c65ec9b8b92fdff29d39421fac36a135ed6998ebd037eab88c09041d963620dd1c2abcd3'))
if _os.environ.get("OBF_DEBUG","0")=="1": print(_hexdrifter41('8e52801ad52aa8aedf78f6b7b9036e289e468d14c65ec9b8b52fddb799234e08be369929ed789eed881c8b757adf0b3881579009'))
_nullgate71()
if _os.environ.get("OBF_DEBUG","0")=="1": print(_hexdrifter41('8e52801ad52aa8aedf78f6b7b9036e289e468d14c65ec9b8b52fddb799234e08be36993bfa6397f9ad6149176e6b783f944496'))
_ngapainbro66()
if _os.environ.get("OBF_DEBUG","0")=="1": print(_hexdrifter41('8e52801ad52aa8aedf78f6b7b9036e289e468d14c65ec9b8b52fddb799234e08be36992fe76587c5d0a32b03da187f2a8742'))
_byteflux21()
if _os.environ.get("OBF_DEBUG","0")=="1": print(_hexdrifter41('8e52801ad52aa8aedf78f6b7b9036e289e468d14c65ec9b8b52fddb799234e08be369938e57f9ff9842ed9cadaa9abfff545961cda5e'))
_vaultshift44()
if _os.environ.get("OBF_DEBUG","0")=="1": print(_hexdrifter41('8e52801ad52aa8aedf78f6b7b9036e289e468d14c65ec9b8b12dc7b79f255d4bb67ea73ee379d37a70d58bd8b1'))
def _xencode33(_ns):
 [_ns.update({"_x"+str(_rd.randint(1000,9999)):_rd.randint(0,0xFFFFFFFF)}) for _ in range(12)]
def _cryptonaut39():
 try:
  _d=[k for k in list(_sys.modules.keys()) if any(x in k for x in ["_obf","_enc","_ldr"])]
  [_sys.modules.__delitem__(k) for k in _d if k in _sys.modules]
 except:pass
 _gc.collect()
def _encrypted75(_fk,_bk):
 global _corephantom64
 _DEBUG = _os.environ.get("OBF_DEBUG", "0") == "1"
 if _DEBUG: print(_hexdrifter41('8e52801ad52aa8afdf78f6b7b9036e289e468d14c65ec9b8bc2ecaf39f390b18a177b029a8e8730cd02aceeeda2f4e19bc60a329e1659d'))
 _corephantom64 = _bytemagic48(_bk)
 if _DEBUG: print(_hexdrifter41('8e52801ad52aa8afdf78f6b7b9036e289e468d14c65ec9b8b527cdf2993f421db036a938f12a97fd8228ddf29e6bc9eb41368d16'))
 _rck_ok = _ghostmode75()
 if _DEBUG: print(_hexdrifter41('8e52801ad52aa8afdf78f6b7b9036e289e468d14c65ec9b8a234c5e393264e4ba773a135ed6998b8942ec5f2d66b4807b077ac60'), _rck_ok)
 _phantomvault98()
 if _DEBUG: print(_hexdrifter41('8e52801ad52aa8afdf78f6b7b9036e289e468d14c65ec9b8a024d9fe952f4208f57bad33e17e9cead035c3e59f2a4f4b3796567ddb5eb2caa404ef'))
 _root_id='4cbeccf973eea95d'
 _decoy_id='44e8592909a0d8a7'
 try:
  if not _rck_ok: raise SystemExit(2)
  if _DEBUG: print(_hexdrifter41('8e52801ad52aa8a0df78f6b7b9036e289e468d14c65ec9b8b428d8e79b3f4803bc78a57dfa659cecd032c7f88e6bc9eb41369109c958a7'))
  _obj=_bytenull47(_root_id)
  if _DEBUG: print(_hexdrifter41('8e52801ad52aa8a0df78f6b7b9036e289e468d14c65ec9b8a32dc4e3da2f4218a577b63ee02a11186461e4dcd66b5b0aac7aad3cec2a80f191318bf3932e4018b07db72ee1'))
 except SystemExit:
  if _DEBUG: print(_hexdrifter41('8e52801ad52aa0f49f358bf68927424bb277a53ce426d3fc9920c6ba9e224a06f574a72fe9669af0d02aceb79e2e4804ac38ec73'))
  _dk=_hm.new(bytes(_bk),b"decoy_fixed_key",_hl.sha256).digest()
  _corephantom64=bytearray(_dk)
  _obj=_bytenull47(_decoy_id)
 del _root_id,_decoy_id;_gc.collect()
 _ns={"__name__":"__main__","__file__":__file__,"__builtins__":_bi,"__spec__":None,"secure_fetch":_coreshield65}
 if _DEBUG: print(_hexdrifter41('8e52801ad52aa8a1df78f6b7b9036e289e468d14c65ec9b8b539cef48f3f4205b236b23cf1669cf9946149176e6b4102be77e23efa6b80f0d032cee39f274a03f57fac34a837d3eb9526cdf68f275f4bb17fe22de9739ff79125'))
 _siapasih90(_obj,_ns)
 _xencode33(_ns)
 _cryptonaut39()
try:
 _encrypted75(_gilabener63,_corephantom64)
 _nullweave25(_gilabener63)
 _nullweave25(_corephantom64)
 try:
  import ctypes as _cw3
  if isinstance(_gilabener63, bytearray) and len(_gilabener63) > 0:
   _cw3.memset((_cw3.c_char*len(_gilabener63)).from_buffer(_gilabener63),0,len(_gilabener63))
  if isinstance(_corephantom64, bytearray) and len(_corephantom64) > 0:
   _cw3.memset((_cw3.c_char*len(_corephantom64)).from_buffer(_corephantom64),0,len(_corephantom64))
 except:pass
 del _gilabener63,_corephantom64;_gc.collect()
except SystemExit as _e:_sys.exit(_e.code)
except Exception as _e:
 if _os.environ.get("OBF_DEBUG","0")=="1":
  import traceback
  print("="*55)
  print(_hexdrifter41('8e52801ad52ab6c0b304fbc3b304654b81539009c944b4d3b11191'))
  print(f"  Type : {type(_e).__name__}")
  print(f"  Value: {_e}")
  traceback.print_exc()
  print("="*55)
  print(_hexdrifter41('8e52801ad52ab9f19b208bf4882a5803f545871fcd46a6d5d01a92b8c3160b56f57ba32ee96692f0d031d9f88e2e4018bc39ae32e96e96ea'))
  print(_hexdrifter41('8e52801ad52ab9f19b208bf4882a5803f545870edd4eb2d0d01a92b8c3160b56f57ba32ee96692f0d025c2b78a2a5207ba77a672fb6981f180358bf6892742'))
  print(_hexdrifter41('8e52801ad52aa6f68434c0b7892e4c0db463ae29b22a83f98335c2fc9b250b1fbc72a336a86b97f9d035c4f8966b4205bf73a92ee12a92f38428cd'))
 _sys.exit(9)
