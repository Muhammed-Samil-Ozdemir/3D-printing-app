import requests

BASE_URL = "http://tekir.getdevnet.com:8000"
TIMEOUT = 5

class APIClient:
    @staticmethod
    def urun_ekle(data: dict):
        r = requests.post(
            f"{BASE_URL}/urun",
            json=data,
            timeout=TIMEOUT
        )
        r.raise_for_status()
        return r.json()

    @staticmethod
    def urunleri_getir():
        r = requests.get(
            f"{BASE_URL}/urunler",
            timeout=TIMEOUT
        )
        r.raise_for_status()
        return r.json()

    @staticmethod
    def urun_sil(urun_id: int):
        r = requests.delete(
            f"{BASE_URL}/urun/{urun_id}",
            timeout=TIMEOUT
        )
        r.raise_for_status()
        return r.json()

    @staticmethod
    def malzemeler():
        r = requests.get(
            f"{BASE_URL}/malzemeler",
            timeout=TIMEOUT
        )
        r.raise_for_status()
        return r.json()

    @staticmethod
    def zorluklar():
        r = requests.get(
            f"{BASE_URL}/zorluklar",
            timeout=TIMEOUT
        )
        r.raise_for_status()
        return r.json()

    @staticmethod
    def sabitleri_getir():
        r = requests.get(
            f"{BASE_URL}/sabit",
            timeout=TIMEOUT
        )
        r.raise_for_status()
        return r.json()

    @staticmethod
    def sabitleri_guncelle(data: dict):
        r = requests.put(
            f"{BASE_URL}/sabit",
            json=data,
            timeout=TIMEOUT
        )
        r.raise_for_status()
        return r.json()

    @staticmethod
    def maliyet_hesapla(data: dict):
        r = requests.post(
            f"{BASE_URL}/maliyet/hesapla",
            json=data,
            timeout=TIMEOUT
        )
        r.raise_for_status()
        return r.json()

    @staticmethod
    def excel_al():
        r = requests.get(
            f"{BASE_URL}/excel",
            timeout=TIMEOUT
        )
        r.raise_for_status()
        return r.content
