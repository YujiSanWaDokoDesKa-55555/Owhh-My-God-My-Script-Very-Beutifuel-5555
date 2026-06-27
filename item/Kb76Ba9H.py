# item/banners.py
import json
import base64
import re
import hashlib
import os
import sys
import time
import requests

a = "\033[1;30m"
m = "\033[1;31m"
h = "\033[1;32m"
k = "\033[1;33m"
b = "\033[1;34m"
u = "\033[1;35m"
c = "\033[1;36m"
p = "\033[1;37m"
o = "\033[38;5;214m"
r = "\033[0m"

VERSI_TOOLS = "4.9.3"
RAW_USER_DB = "https://raw.githubusercontent.com/AjJwnskanKanskNwndbdoaOsmxmaBdqkNwknaa/XdbSpmPrm/main/user.json"
RAW_VERSI_URL = "https://raw.githubusercontent.com/AjJwnskanKanskNwndbdoaOsmxmaBdqkNwknaa/XdbSpmPrm/main/versi.json"

def get_user_database():
    try:
        session = requests.Session()
        response = session.get(
            "https://api.github.com/repos/"
            "AjJwnskanKanskNwndbdoaOsmxmaBdqkNwknaa/"
            "XdbSpmPrm/contents/user.json",
            headers={"Accept": "application/vnd.github+json", "User-Agent": "Mozilla/5.0"},
            timeout=3
        )
        response.raise_for_status()
        data = response.json()
        return json.loads(base64.b64decode(data["content"]).decode("utf-8"))
    except Exception:
        return None

def jumlah_pengguna():
    try:
        data = get_user_database()
        total = len(data.get("users", []))
        return total
    except Exception:
        return 0

def cek_versi():
    try:
        resp = requests.get(RAW_VERSI_URL, timeout=5)
        if resp.status_code == 200:
            data = resp.json()
            versi_terbaru = data.get("versi", "")
            return VERSI_TOOLS == versi_terbaru
        return True
    except Exception:
        return True

def banner_v1():
    user = jumlah_pengguna()
    versi_valid = cek_versi()
    V = VERSI_TOOLS
    jarak_user = " " * (18 - len(str(user)))
    print(f"""{a}
╭─────────────────────────────────────────────────────────────╮
│\033[1;35m  ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀                                    {a} │
│\033[1;35m  ⠀⠀⠀⠀⠀⠀⢀⣠⣤⠞⢹⡏⠳⣤⣄⡀⠀⠀⠀⠀⠀⠀ {h}┌─┐┌┬┐┌─┐       ┌┐┌┌─┐─┐ ┬┬ ┬┌─┐   {a} │
│\033[1;35m  ⠰⣤⣀⠀⢀⡴⣫⣴⡇⠀⢸⡇⠀⠈⢦⣝⢦⡀⠀⣀⣤⠆ {h}│ │││││ ┬  {m}───{h}  │││├┤ ┌┴┬┘│ │└─┐   {a} │
│\033[1;35m  ⠀⢷⠀⠉⠛⠾⣿⣿⡇⠀⢸⡇⠀⢀⠀⠙⠷⠛⠉⠀⡾⠀ {h}└─┘┴ ┴└─┘       ┘└┘└─┘┴ └─└─┘└─┘   {a} │
│\033[1;35m  ⠀⠘⡄⠀⢠⡀⠀⢿⡇⠀⢸⡇⠀⠈⠉⠀⣀⡄⠀⢠⠃⠀{a}──────────────────────────────────  {a} │
│\033[1;35m  ⠀⠀⢳⡀⠀⣷⠀⠘⡇⠀⢸⡇⡀⢤⣶⣿⠟⠀⢀⡞⠀⠀                                    {a} │
│\033[1;35m  ⠀⠀⠈⣟⣦⠸⡆⠀⠁⠀⢸⡏⠀⢸⠿⠁⠀⣴⣻⠁⠀  {h} ꫝ{p} Author  {m}     : {h}Byexe            {a} │
│\033[1;35m  ⠀⠀⠀⠹⣌⢷⣿⡀⠀⠀⢸⡇⠀⠈⠀⣠⡾⣡⠏⠀⠀⠀ {h} ꫝ{p} Release Date {m}: {h}25 Apr 2026      {a} │
│\033[1;35m  ⠀⠀⠀⠀⠈⠳⣝⠣⡄⠀⢸⡇⠀⢠⠜⣫⠞⠁     {h} ꫝ{p} Version      {m}: {"\033[101m" + h if not versi_valid else h}{V}{r if not versi_valid else ""}{a if not versi_valid else ""}            {a} │
│\033[1;35m  ⠀⠀⠀⠀⠀⠀⠈⠙⠛⢦⣸⡇⡴⠛⠋⠁⠀      {h} ꫝ{p} Users        {m}: {h}{user}{jarak_user}{a}│
│\033[1;35m  ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⠏⠀⠀⠀⠀⠀                                         {a} │
╰─────────────────────────────────────────────────────────────╯""")

def banner_v2():
    user = jumlah_pengguna()
    versi_valid = cek_versi()
    V = VERSI_TOOLS
    jarak_user = " " * (16 - len(str(user)))
    print(f"""{a}
╭─────────────────────────────────────────────────────────────╮
│\033[1;35m  ⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀                                    {a}│
│\033[1;35m  ⠀⣿⣦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣾⡟                                    {a}│
│\033[1;35m  ⠀⢹⣿⣿⣿⣦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣾⣿⣿⣿⠇  {h}┌─┐┌┬┐┌─┐       {h}┌┐┌┌─┐─┐ ┬┬ ┬┌─┐  {a}│
│\033[1;35m  ⠀⠸⣿⣿⣿⣿⣿⣿⣶⣀⠀⠀⠀⠀⣠⣶⣿⣿⣿⣿⣿⣿⠀  {h}│ │││││ ┬  {m}───  {h}│││├┤ ┌┴┬┘│ │└─┐  {a}│
│\033[1;35m  ⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⣄⠙⠻⣿⣿⣿⣿⣿⣿⡇⠀  {h}└─┘┴ ┴└─┘       {h}┘└┘└─┘┴ └─└─┘└─┘  {a}│
│\033[1;35m  ⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⣄⠙⠻⢿⣿⣿⡃⠀ {a}────────────────────────────────── {a}│
│\033[1;35m⠀  ⠀⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣤⣀⠙⠻⠀⠀                                    {a}│
│\033[1;35m⠀⠀  ⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⡿⣿⣷⡤⠀⠀   {h}ꫝ{p} Author       {m}:{h} Byexe           {a}│
│\033[1;35m⠀⠀⠀  ⢻⣿⣿⣀⠙⠻⣿⣿⣿⣿⣿⡿⠇⠈⣰⣿⣿⠇⠀⠀   {h}ꫝ{p} Release Date {m}:{h} 25 Apr 2026     {a}│
│\033[1;35m⠀⠀⠀⠀  ⠀⠙⠿⣿⣷⣶⣾⣿⣿⣷⣶⣶⣼⠟⠋⠀⠀⠀⠀   {h}ꫝ{p} Version      {m}: {"\033[101m" + h if not versi_valid else h}{V}{r if not versi_valid else ""}{a if not versi_valid else ""}          {a} │
│\033[1;35m⠀⠀⠀⠀⠀⠀  ⠀⠈⠙⠿⣿⣿⣿⣿⠟⠉⠀⠀⠀⠀⠀⠀ ⠀  {h}ꫝ{p} Users        {m}: {h}{user}{jarak_user}{a}│
│\033[1;35m⠀⠀⠀⠀⠀⠀⠀⠀  ⠀⠀⠈⠙⠋⠁⠀⠀⠀⠀                                         {a}│
╰─────────────────────────────────────────────────────────────╯""")

def banner_v3():
    user = jumlah_pengguna()
    versi_valid = cek_versi()
    V = VERSI_TOOLS
    jarak_user = " " * (14 - len(str(user)))
    print(f"""{a}
╭─────────────────────────────────────────────────────────────╮
│\033[1;35m ⠀⣣⡀⠀⠀⠀⠀⠹⣦⣀⠀⠀⠀⠀⢠⡀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡄                                  {a}│
│\033[1;35m⠀⠀⠸⣷⣄⠀⠀⠀⠀⠹⣿⣷⣄⡐⣄⠀⢳⡀⠀⠀⠀⠀⠀⠀⢀⣾⠁                                  {a}│
│\033[1;35m ⠀⠀⢿⣿⣦⠀⠀⢤⣄⠘⣿⣿⣿⣾⣷⣼⣿⡀⠀⠀⠀⠀⣠⣿⡇⠀ {h}┌─┐┌┬┐┌─┐       {h}┌┐┌┌─┐─┐ ┬┬ ┬┌─┐ {a}│
│\033[1;35m ⠀⠀⠈⢿⣿⣷⡀⠀⠛⣿⣿⣿⡿⠿⣿⣿⣿⣧⠀⠀⠀⣴⣿⡿⠀⠀ {h}│ │││││ ┬  {m}───  {h}│││├┤ ┌┴┬┘│ │└─┐ {a}│
│\033[1;35m⠀⠈⠳⣦⣤⣙⣿⣿⣆⠠⢤⣿⣿⣇⠀⠘⣿⡟⡝⠀⢀⣾⣿⣋⣤⡴⠊ {h}└─┘┴ ┴└─┘       {h}┘└┘└─┘┴ └─└─┘└─┘ {a}│
│\033[1;35m ⠀⠀⠈⠙⠻⠿⢿⣿⣧⡀⠉⢻⣿⣷⣶⣿⠗⠀⣠⣿⣿⠿⠟⠁⠀⠀{a} ──────────────────────────────── {a}│
│\033[1;35m ⠀⠀⠀⠀⠀⠒⠺⠿⠛⠛⠀⢸⣿⣿⣍⣀⠀⠐⠛⠻⠓⠀⠀⠀⠀⠀⠀⠀                                {a}│
│\033[1;35m⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣷⠶⣄⠀⠀⠀⠀⠀ ⠀   {h}ꫝ{p} Author       {m}:{h} Byexe         {a}│
│\033[1;35m⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⡏⢿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀   {h}ꫝ{p} Release Date {m}:{h} 25 Apr 2026   {a}│
│\033[1;35m⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⡿⠙⠀⠀⠀⠀⠀⠀⠀⠀   {h}ꫝ{p} Version      {m}: {"\033[101m" + h if not versi_valid else h}{V}{r if not versi_valid else ""}{a if not versi_valid else ""}        {a} │
│\033[1;35m⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀ ⠀  {h}ꫝ{p} Users        {m}: {h}{user}{jarak_user}{a}│
│\033[1;35m ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀                          {a}│
│\033[1;35m ⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡴⠟⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀                             {a}│
│\033[1;35m ⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀                       {a}│
╰─────────────────────────────────────────────────────────────╯""")

def banner_v4():
    user = jumlah_pengguna()
    versi_valid = cek_versi()
    V = VERSI_TOOLS
    jarak_user = " " * (17 - len(str(user)))
    print(f"""{a}
╭─────────────────────────────────────────────────────────────╮
│\033[1;35m         ⠀⠀⠀⠀⠀⠀⢠⡀                                            {a}│
│\033[1;35m  ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣷⠀                                            {a}│
│\033[1;35m ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀                      {a}│
│\033[1;35m⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⠟⢹⣿⠀⠀⠀⣧⠀⠀⠀⠀⠀⠀ {h}┌─┐┌┬┐┌─┐       {h}┌┐┌┌─┐─┐ ┬┬ ┬┌─┐   {a}│⠀
│\033[1;35m⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⠏⠀⠘⣿⠀⠀⠀⣿⣇⠀⠀⠀⠀⠀⠀{h}│ │││││ ┬  {m}───  {h}│││├┤ ┌┴┬┘│ │└─┐   {a}│
│\033[1;35m     ⠀⠀⣼⣿⣿⠃⠀⠀⢀⣿⠀⠀⠀⣿⣿⡄⠀⠀⠀⠀⠀{h}└─┘┴ ┴└─┘       {h}┘└┘└─┘┴ └─└─┘└─┘   {a}│
│\033[1;35m⠀⠀⡆⠀⠀⠀⣼⣿⣿⠇⠀⠀⠀⢸⠇⠀⠀⣸⣿⣿⣧⠀⠀⠀⠀{a} ────────────────────────────────   {a}│
│\033[1;35m⠀⠀⣧⠀⠀⢰⣿⣿⡿⠀⠀⠀⢀⠎⠀⠀⣰⣿⣿⣿⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀                            {a}│
│\033[1;35m⠀⠀⣿⣆⠀⣼⣿⣿⡇⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣦⣴⠀⠀ {h}ꫝ{p} Author       {m}:{h} Byexe            {a}│
│\033[1;35m⠀⠀⣿⣿⣆⣿⣿⣿⡇⠀⠀⠀⠀⢀⣾⣿⠿⠟⠛⠿⣿⣿⣿⣿⠀⠀⠀{h}ꫝ{p} Release Date {m}:{h} 25 Apr 2026      {a}│
│\033[1;35m⠀⠀⢹⣿⣿⣿⣿⣿⡇⠀⠀⠀⢠⣿⠟⠁⠀⠀⠀⠀⢸⣿⣿⡿⠀⠀ {h}ꫝ{p} Version      {m}: {"\033[101m" + h if not versi_valid else h}{V}{r if not versi_valid else ""}{a if not versi_valid else ""}        {a}    │
│\033[1;35m⠀⠀⠀⢿⣿⣿⣿⣿⣷⠀⠀⠀⣾⠏⠀⠀⠀⠀⠀⠀⢸⣿⣿⠇⠀⠀⠀{h}ꫝ{p} Users        {m}: {h}{user}{jarak_user}{a}│
│\033[1;35m⠀⠀⠀⠈⠻⣿⣿⣿⣿⡄⠀⢰⡏⠀⠀⠀⠀⠀⠀⢀⣾⣿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀                       {a}│
│\033[1;35m ⠀⠀⠀⠀⠈⠻⣿⣿⣷⡀⠸⠀⠀⠀⠀⠀⠀⣠⡿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀                       {a}│
│\033[1;35m  ⠀⠀⠀⠀⠀⠀⠉⠛⠃⠀⠀⠀⠀⠀⠐⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀                       {a}│
╰─────────────────────────────────────────────────────────────╯""")

def banner_v5():
    user = jumlah_pengguna()
    versi_valid = cek_versi()
    V = VERSI_TOOLS
    jarak_user = " " * (16 - len(str(user)))
    print(f"""{a}
╭─────────────────────────────────────────────────────────────╮
│\033[1;35m ⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⣀⣀⣀⣀⣀⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣀⣀⠀⠀⠀⠀⠀⠀                         {a}│
│\033[1;35m ⠀⠀⠀⠀⣠⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⣄⠀⠀                         {a}│
│\033[1;35m ⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀                  {a}│
│\033[1;35m ⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀                        {a}│
│\033[1;35m ⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⠀⠀                       {a}│
│\033[1;35m ⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⠿⠿⠿⠿⠿⠿⠛⠻⠉⠀⠀⠀                        {a}│
│\033[1;35m ⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡁⠀⠀{h}┌─┐┌┬┐┌─┐       {h}┌┐┌┌─┐─┐ ┬┬ ┬┌─┐      {a}│
│\033[1;35m ⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠻⣿⣿⣿⣿⣿⣿⣿⣇⠀⠀{h}│ │││││ ┬  {m}───  {h}│││├┤ ┌┴┬┘│ │└─┐      {a}│
│\033[1;35m ⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⡁⠀⢹⣿⣿⣿⣿⣿⣿⣿⠀⠀{h}└─┘┴ ┴└─┘       {h}┘└┘└─┘┴ └─└─┘└─┘      {a}│
│\033[1;35m ⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⠀⠀⢻⣿⣿⣿⣿⣿⣿⡇⠀{a} ────────────────────────────────     {a}│
│\033[1;35m ⠀⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠻⣿⣿⣿⣿⡿⠀ ⠀⠀                                    {a}│
│\033[1;35m ⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠈⠙⠛⠋⠀⠀    ⠀ {h}ꫝ{p} Author       {m}:{h} Byexe           {a}│
│\033[1;35m   ⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  {h}ꫝ{p} Release Date {m}:{h} 25 Apr 2026     {a}│
│\033[1;35m ⠀⠀⠸⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  {h}ꫝ{p} Version      {m}: {"\033[101m" + h if not versi_valid else h}{V}{r if not versi_valid else ""}{a if not versi_valid else ""}        {a}   │
│\033[1;35m ⠀ ⠀⠹⣿⣿⣿⣿⣿⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀      {h}ꫝ{p} Users        {m}: {h}{user}{jarak_user}{a}│
│\033[1;35m⠀⠀⠀⠀⠘⠻⣿⣿⡿⠟⠀⠀⠀⠀⠀⠀ ⠀                {a}│
╰─────────────────────────────────────────────────────────────╯""")