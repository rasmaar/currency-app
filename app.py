import requests
import os
from dotenv import load_dotenv

load_dotenv()

# ==========================================
# DATA NAMA NEGARA DAN KODE MATA UANG
# ==========================================
currency_names = {
    "USD": "Amerika Serikat",
    "EUR": "Uni Eropa",
    "GBP": "Inggris",
    "JPY": "Jepang",
    "IDR": "Indonesia",
    "SGD": "Singapura",
    "MYR": "Malaysia",
    "THB": "Thailand",
    "PHP": "Filipina",
    "VND": "Vietnam",
    "KRW": "Korea Selatan",
    "CNY": "China",
    "HKD": "Hong Kong",
    "TWD": "Taiwan",
    "INR": "India",
    "PKR": "Pakistan",
    "BDT": "Bangladesh",
    "LKR": "Sri Lanka",
    "NPR": "Nepal",
    "AUD": "Australia",
    "NZD": "Selandia Baru",
    "CAD": "Kanada",
    "MXN": "Meksiko",
    "BRL": "Brasil",
    "ARS": "Argentina",
    "CLP": "Chile",
    "COP": "Kolombia",
    "PEN": "Peru",
    "UYU": "Uruguay",
    "BOB": "Bolivia",
    "PYG": "Paraguay",
    "VES": "Venezuela",
    "ZAR": "Afrika Selatan",
    "NGN": "Nigeria",
    "KES": "Kenya",
    "GHS": "Ghana",
    "UGX": "Uganda",
    "TZS": "Tanzania",
    "MAD": "Maroko",
    "EGP": "Mesir",
    "DZD": "Aljazair",
    "TND": "Tunisia",
    "LYD": "Libya",
    "ETB": "Etiopia",
    "RUB": "Rusia",
    "UAH": "Ukraina",
    "PLN": "Polandia",
    "CZK": "Republik Ceko",
    "HUF": "Hungaria",
    "RON": "Rumania",
    "BGN": "Bulgaria",
    "HRK": "Kroasia",
    "RSD": "Serbia",
    "CHF": "Swiss",
    "SEK": "Swedia",
    "NOK": "Norwegia",
    "DKK": "Denmark",
    "ISK": "Islandia",
    "TRY": "Turki",
    "AED": "Uni Emirat Arab",
    "SAR": "Arab Saudi",
    "QAR": "Qatar",
    "KWD": "Kuwait",
    "BHD": "Bahrain",
    "OMR": "Oman",
    "JOD": "Yordania",
    "ILS": "Israel",
    "IRR": "Iran",
    "IQD": "Irak",
    "AFN": "Afghanistan",
    "KHR": "Kamboja",
    "LAK": "Laos",
    "MMK": "Myanmar",
    "BND": "Brunei",
    "MOP": "Makau",
    "FJD": "Fiji",
    "PGK": "Papua Nugini",
    "CRC": "Kosta Rika",
    "GTQ": "Guatemala",
    "HNL": "Honduras",
    "NIO": "Nikaragua",
    "PAB": "Panama",
    "DOP": "Republik Dominika",
    "JMD": "Jamaika",
    "TTD": "Trinidad dan Tobago",
    "BBD": "Barbados",
    "BSD": "Bahama",
    "CUP": "Kuba",

    # Tambahan lengkap
    "ALL": "Albania",
    "AMD": "Armenia",
    "ANG": "Antillen Belanda",
    "AOA": "Angola",
    "AWG": "Aruba",
    "AZN": "Azerbaijan",
    "BAM": "Bosnia dan Herzegovina",
    "BIF": "Burundi",
    "BMD": "Bermuda",
    "BWP": "Botswana",
    "BYN": "Belarus",
    "BZD": "Belize",
    "CDF": "Republik Demokratik Kongo",
    "CVE": "Cape Verde",
    "DJF": "Djibouti",
    "ERN": "Eritrea",
    "FKP": "Kepulauan Falkland",
    "GEL": "Georgia",
    "GHS": "Ghana",
    "GIP": "Gibraltar",
    "GMD": "Gambia",
    "GNF": "Guinea",
    "GYD": "Guyana",
    "HTG": "Haiti",
    "KGS": "Kyrgyzstan",
    "KMF": "Komoro",
    "KYD": "Kepulauan Cayman",
    "KZT": "Kazakhstan",
    "LBP": "Lebanon",
    "LRD": "Liberia",
    "LSL": "Lesotho",
    "MDL": "Moldova",
    "MGA": "Madagaskar",
    "MKD": "Makedonia Utara",
    "MNT": "Mongolia",
    "MRU": "Mauritania",
    "MUR": "Mauritius",
    "MVR": "Maladewa",
    "MWK": "Malawi",
    "MZN": "Mozambik",
    "NAD": "Namibia",
    "RWF": "Rwanda",
    "SCR": "Seychelles",
    "SDG": "Sudan",
    "SHP": "Saint Helena",
    "SLE": "Sierra Leone",
    "SOS": "Somalia",
    "SRD": "Suriname",
    "SSP": "Sudan Selatan",
    "STN": "Sao Tome dan Principe",
    "SYP": "Suriah",
    "SZL": "Eswatini",
    "TJS": "Tajikistan",
    "TMT": "Turkmenistan",
    "TOP": "Tonga",
    "UZS": "Uzbekistan",
    "VUV": "Vanuatu",
    "WST": "Samoa",
    "XAF": "Afrika Tengah",
    "XCD": "Karibia Timur",
    "XOF": "Afrika Barat",
    "XPF": "Polinesia Prancis",
    "YER": "Yaman",
    "ZMW": "Zambia",
    "ZWL": "Zimbabwe"
}

# ==========================================
# HEADER
# ==========================================
print("=" * 50)
print("      APLIKASI KURS MATA UANG DUNIA")
print("         Menggunakan REST API")
print("=" * 50)

# ==========================================
# AMBIL DATA API
# ==========================================
try:
    API_URL = os.getenv("API_URL")
    BASE = os.getenv("BASE_CURRENCY")

    response = requests.get(f"{API_URL}/{BASE}")
    data = response.json()
except:
    print("Tidak dapat terhubung ke API.")
    exit()

# ==========================================
# TAMPILKAN LIST MATA UANG
# ==========================================
print("\nDaftar Mata Uang Tersedia:\n")

for code in sorted(data["rates"].keys()):
    negara = currency_names.get(code, "Belum Ditambahkan")
    print(f"{code:<5} - {negara}")

# ==========================================
# INPUT USER
# ==========================================
print("\n" + "=" * 50)

from_currency = input("Masukkan kode mata uang asal   : ").upper()
to_currency = input("Masukkan kode mata uang tujuan : ").upper()

try:
    amount = float(input("Masukkan nominal uang          : "))
except:
    print("Nominal harus berupa angka.")
    exit()

# ==========================================
# AMBIL DATA BERDASARKAN MATA UANG
# ==========================================
try:
    response = requests.get(
    f"{API_URL}/{from_currency}"
)
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

asal_negara = currency_names.get(from_currency, from_currency)
tujuan_negara = currency_names.get(to_currency, to_currency)

# ==========================================
# OUTPUT
# ==========================================
print("\n" + "=" * 50)
print("               HASIL KONVERSI")
print("=" * 50)

print(f"Negara Asal      : {asal_negara}")
print(f"Negara Tujuan    : {tujuan_negara}")
print(f"Kurs             : 1 {from_currency} = {rate:.4f} {to_currency}")
print(f"Nominal Awal     : {amount:.2f} {from_currency}")
print(f"Hasil Konversi   : {result:.2f} {to_currency}")

print("=" * 50)