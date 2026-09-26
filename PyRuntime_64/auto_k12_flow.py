#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Auto ChatGPT K-12 Teacher Workspace Creator & Verifier
Standalone automated flow using DrissionPage + temp.tf + K12Verifier
"""

import os
import sys
import time
import json
import re
import random
import string
import urllib.request
from DrissionPage import Chromium, ChromiumOptions

# Pastikan output unbuffered agar log selalu realtime
try:
    sys.stdout.reconfigure(line_buffering=True)
except Exception:
    pass

# Import existing K12Verifier safely
try:
    from script import K12Verifier
except ImportError:
    K12Verifier = None

import requests

TEMP_TF_ACCOUNT_API = "https://temp.tf/api/account?providers=high.edu.pl,outlook.com,hotmail.com,gmail.com&dot=1&plus=1"
TEMP_TF_CHECK_API = "https://temp.tf/api/check"

def get_temp_edu_email():
    """Dapatkan email .edu atau outlook dari temp.tf"""
    print("[1/6] Mengambil email .edu resmi dari temp.tf...", flush=True)
    res = requests.get(TEMP_TF_ACCOUNT_API, headers={"User-Agent": "Mozilla/5.0"}, timeout=15)
    data = res.json()
    email = data.get("email")
    if not email:
        raise RuntimeError("Gagal mendapatkan email dari temp.tf")
    print(f"      [+] Email diperoleh: {email}", flush=True)
    return email

def poll_temp_tf_otp(email, max_wait=90, delay=3):
    """Memantau inbox temp.tf untuk mendapatkan 6-digit kode OTP OpenAI"""
    print(f"[4/6] Menunggu kode OTP verifikasi OpenAI di temp.tf (maks {max_wait}s)...", flush=True)
    start = time.time()
    while time.time() - start < max_wait:
        time.sleep(delay)
        try:
            res = requests.post(TEMP_TF_CHECK_API, json={"email": email, "wait": False}, headers={"User-Agent": "Mozilla/5.0"}, timeout=10)
            if res.status_code == 200:
                data = res.json()
                messages = data.get("data", [])
                for msg in messages:
                    subject = str(msg.get("subject", "")).lower()
                    raw_body = msg.get("body", "") or msg.get("text", "") or msg.get("html", "")
                    clean_body = re.sub(r'<style.*?</style>', '', raw_body, flags=re.DOTALL)
                    clean_body = re.sub(r'<[^>]+>', ' ', clean_body)
                    
                    if any(k in subject or k in clean_body.lower() for k in ["openai", "chatgpt", "verification code", "verify", "code"]):
                        match = re.search(r'code to continue:?\s*(\b\d{6}\b)', clean_body, re.IGNORECASE)
                        if match:
                            print(f"\n      [+] KODE OTP OPENAI DITEMUKAN: {match.group(1)}", flush=True)
                            return match.group(1)
                        
                        match2 = re.search(r'verification code:?\s*(\b\d{6}\b)', clean_body, re.IGNORECASE)
                        if match2:
                            print(f"\n      [+] KODE OTP OPENAI DITEMUKAN: {match2.group(1)}", flush=True)
                            return match2.group(1)
                        
                        codes = re.findall(r'\b\d{6}\b', clean_body)
                        if codes:
                            print(f"\n      [+] KODE OTP DITEMUKAN: {codes[-1]}", flush=True)
                            return codes[-1]
        except Exception:
            pass
        print(".", end="", flush=True)
    print()
    return None

def generate_strong_password():
    chars = string.ascii_letters + string.digits
    core = "".join(random.choices(chars, k=10))
    return f"TeacherK12!{core}#2026"

def run_flow():
    print("=" * 60, flush=True)
    print("  AUTO CHATGPT K-12 TEACHER ONBOARDING (STANDALONE FLOW)", flush=True)
    print("  Menggunakan temp.tf (.edu) + DrissionPage Anti-Detection", flush=True)
    print("=" * 60, flush=True)

    # 1. Email & Password
    email = get_temp_edu_email()
    password = generate_strong_password()
    print(f"[2/6] Password disiapkan: {password}", flush=True)

    # 2. Browser Startup
    print("[3/6] Membuka browser DrissionPage (Stealth Mode)...", flush=True)
    co = ChromiumOptions()
    co.auto_port()
    turnstile_ext = r"d:\FREELANCE\grok-register\turnstilePatch"
    if os.path.isdir(turnstile_ext):
        co.add_extension(turnstile_ext)

    browser = Chromium(co)
    tab = browser.latest_tab

    try:
        # Buka ChatGPT K-12 Login / Signup entrypoint
        target_url = "https://chatgpt.com/auth/login/?next=%2Fk12-verification"
        tab.get(target_url)
        time.sleep(3)

        # Cari input email dengan retry
        email_input = None
        for _ in range(12):
            email_input = tab.ele('tag:input@type=email', timeout=1) or tab.ele('tag:input@name=email', timeout=1) or tab.ele('tag:input', timeout=1)
            if email_input:
                break
            time.sleep(1)

        if email_input:
            email_input.clear()
            email_input.input(email)
            time.sleep(1)

            # Klik continue
            continue_btn = tab.ele('tag:button@type=submit', timeout=2) or tab.ele('text:Continue', timeout=2)
            if continue_btn:
                continue_btn.click()
                time.sleep(3)
        else:
            print("[-] Input email tidak ditemukan di halaman.", flush=True)

        # Cek jika diminta password atau langsung OTP
        pwd_inp = tab.ele('tag:input@type=password', timeout=2)
        if pwd_inp:
            print("      [+] Memasukkan password akun...", flush=True)
            pwd_inp.input(password)
            time.sleep(1)
            btn = tab.ele('tag:button@type=submit', timeout=2) or tab.ele('text:Continue', timeout=2)
            if btn:
                btn.click()
                time.sleep(3)

        # Tangani OTP dari OpenAI
        otp = poll_temp_tf_otp(email, max_wait=75)
        if otp:
            # Cari input OTP di halaman
            otp_inputs = tab.eles('tag:input')
            for inp in otp_inputs:
                if inp.attr("type") in ["text", "number"] or inp.attr("autocomplete") == "one-time-code" or inp.attr("name") == "code":
                    inp.input(otp)
                    time.sleep(1)
                    break
            
            # Submit OTP
            otp_btn = tab.ele('tag:button@type=submit', timeout=2) or tab.ele('text:Continue', timeout=2)
            if otp_btn:
                print("      [+] Menyerahkan kode OTP...", flush=True)
                otp_btn.click()
                time.sleep(3)
        else:
            print("[!] OTP belum terdeteksi otomatis. Silakan cek inbox temp.tf jika ada jeda.", flush=True)

        # Cek apakah ada langkah Onboarding / Profil (Name & Age)
        print("\n[5/6] Memeriksa tahapan profil pendidik & navigasi ke K-12...", flush=True)
        for _ in range(15):
            curr_url = tab.url
            if "about-you" in curr_url or tab.ele('tag:input@name=name', timeout=1):
                print("      [+] Terdeteksi form 'About you' (Nama & Usia Pengajar)...", flush=True)
                name_inp = tab.ele('tag:input@name=name', timeout=2)
                if name_inp:
                    first_names = ["James", "Robert", "John", "Michael", "David", "Richard", "Thomas", "Charles"]
                    last_names = ["Miller", "Smith", "Johnson", "Williams", "Brown", "Davis", "Wilson", "Anderson"]
                    t_name = f"{random.choice(first_names)} {random.choice(last_names)}"
                    name_inp.input(t_name)
                    print(f"          Nama: {t_name}", flush=True)
                
                age_inp = tab.ele('tag:input@name=age', timeout=2)
                if age_inp:
                    t_age = str(random.randint(30, 48))
                    age_inp.input(t_age)
                    print(f"          Usia: {t_age}", flush=True)
                
                time.sleep(1)
                about_btn = tab.ele('tag:button@type=submit', timeout=2) or tab.ele('text:Continue', timeout=2)
                if about_btn:
                    about_btn.click()
                    print("          Form profil disubmit.", flush=True)
                    time.sleep(3)
                break
            elif "k12-verification" in curr_url:
                break
            time.sleep(1)

        # Pantau status redirect ke k12-verification atau sheerid
        print("      [+] Memantau tombol verifikasi dan tautan SheerID...", flush=True)
        sheerid_url = None
        for step in range(25):
            time.sleep(2)
            
            # Cek semua tab browser
            for t in browser.get_tabs():
                if "sheerid.com/verify" in t.url:
                    sheerid_url = t.url
                    print(f"\n[+] BERHASIL MENDETEKSI URL SHEERID: {sheerid_url}", flush=True)
                    break
            
            if sheerid_url:
                break

            # Cek jika ada tombol verifikasi status di tab saat ini
            verify_btn = tab.ele('text:Verify status', timeout=1) or tab.ele('text:Verify', timeout=1)
            if verify_btn:
                print("      [+] Mengklik tombol 'Verify status'...", flush=True)
                verify_btn.click()
                time.sleep(3)

            # Cek juga tautan <a> dengan link sheerid
            for a in tab.eles('tag:a'):
                href = a.attr('href') or ""
                if "sheerid.com/verify" in href:
                    sheerid_url = href
                    print(f"\n[+] BERHASIL MENDETEKSI LINK SHEERID: {sheerid_url}", flush=True)
                    break

            if sheerid_url:
                break

        # 3. Eksekusi K12Verifier
        if sheerid_url and K12Verifier:
            print("\n[6/6] Menjalankan modul K12Verifier dengan temp.tf (.edu)...", flush=True)
            verifier = K12Verifier(sheerid_url, use_temp_email=True, manual_email=email)
            result = verifier.verify()
            print("\nHASIL VERIFIKASI AKHIR:", flush=True)
            print(json.dumps(result, indent=2), flush=True)
        else:
            print(f"\n[Status] Halaman browser saat ini: {tab.url}", flush=True)

        # Simpan akun ke file output terpisah
        out_file = os.path.join(os.path.dirname(__file__), "created_k12_accounts.txt")
        with open(out_file, "a", encoding="utf-8") as f:
            f.write(f"{email}----{password}----{time.strftime('%Y-%m-%d %H:%M:%S')}\n")
        print(f"\n[+] Kredensial akun tersimpan aman di: {out_file}", flush=True)
        print(f"    Email   : {email}", flush=True)
        print(f"    Password: {password}", flush=True)

    finally:
        time.sleep(3)
        try:
            browser.quit()
        except Exception:
            pass

if __name__ == "__main__":
    run_flow()
