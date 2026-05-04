import requests
import os
import argparse
from dotenv import load_dotenv

load_dotenv()

# ==========================================
# ARGUMENT CLI
# ==========================================
parser = argparse.ArgumentParser(description="Aplikasi Kurs Mata Uang (CLI)")
parser.add_argument("--from_currency", required=True, help="Mata uang asal (contoh: USD)")
parser.add_argument("--to_currency", required=True, help="Mata uang tujuan (contoh: IDR)")
parser.add_argument("--amount", type=float, required=True, help="Nominal uang")

args = parser.parse_args()

from_currency = args.from_currency.upper()
to_currency = args.to_currency.upper()
amount = args.amount

# ==========================================
# LOAD ENV
# ==========================================
API_URL = os.getenv("API_URL")

if not API_URL:
    print("API_URL tidak ditemukan di .env")
    exit()

# ==========================================
# AMBIL DATA API
# ==========================================
try:
    response = requests.get(f"{API_URL}/{from_currency}")
    data = response.json()
except:
    print("Gagal mengambil data API.")
    exit()

# ==========================================
# VALIDASI
# ==========================================
if "rates" not in data:
    print("Kode mata uang asal tidak valid.")
    exit()

if to_currency not in data["rates"]:
    print("Kode mata uang tujuan tidak ditemukan.")
    exit()

# ==========================================
# KONVERSI
# ==========================================
rate = data["rates"][to_currency]
result = amount * rate

# ==========================================
# OUTPUT
# ==========================================
print("=" * 50)
print("        HASIL KONVERSI (CLI)")
print("=" * 50)
print(f"Dari           : {from_currency}")
print(f"Ke             : {to_currency}")
print(f"Kurs           : 1 {from_currency} = {rate:.4f} {to_currency}")
print(f"Nominal        : {amount}")
print(f"Hasil          : {result:.2f}")
print("=" * 50)