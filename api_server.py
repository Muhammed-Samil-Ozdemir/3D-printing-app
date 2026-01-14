from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
import tempfile
from pydantic import BaseModel
from typing import List
from datetime import date

from urun_db_manager import UrunDataBase
from maliyet_db_manager import MaliyetDataBase
from urun import Urun
from maliyet_hesaplayici import MaliyetHesapla

app = FastAPI(title="Modeline API")


class UrunCreate(BaseModel):
    musteri_adi: str
    agirlik: float
    baski_suresi: float
    basim_zorlugu: str
    malzeme: str
    aciklama: str
    basim_tarihi: date


class UrunOut(UrunCreate):
    filament_maliyet: float
    elektrik_maliyet: float
    baski_maliyet: float
    ham_maliyet: float
    satis_fiyati: float
    kar: float


@app.get("/sabit")
def sabitleri_getir():
    db = MaliyetDataBase()
    try:
        return {
            "filament_kg_maliyet": db.get_filament_kg_maliyet(),
            "saat_basi_kw": db.get_saat_basi_kw(),
            "kwh_fiyat": db.get_kwh_fiyat(),
            "saatlik_baski_ucreti": db.get_saatlik_baski_ucreti(),
            "saatlik_baski_katsayi": db.get_saatlik_baski_katsayi(),
            "sabit_kurulum_ucreti": db.get_sabit_kurulum_ucreti(),
            "kar_orani": db.get_kar_orani(),
        }
    finally:
        db.close()

@app.get("/malzemeler")
def malzeme_listesi():
    db = MaliyetDataBase()
    try:
        return db.get_malzeme_listesi()
    finally:
        db.close()


@app.get("/zorluklar")
def zorluk_listesi():
    db = MaliyetDataBase()
    try:
        return db.get_zorluk_listesi()
    finally:
        db.close()


@app.post("/urun", response_model=int)
def urun_ekle(data: UrunCreate):
    urun = Urun()
    urun.musteri_adi = data.musteri_adi
    urun.agirlik = data.agirlik
    urun.baski_suresi = data.baski_suresi
    urun.basim_zorlugu = data.basim_zorlugu
    urun.malzeme = data.malzeme
    urun.aciklama = data.aciklama
    urun.basim_tarihi = data.basim_tarihi

    db = UrunDataBase()
    try:
        urun_id = db.ekle(urun)
        return urun_id
    finally:
        db.close()

@app.get("/urunler")
def urunleri_getir():
    db = UrunDataBase()
    try:
        urunler, idler = db.get_all()
        sonuc = []
        for urun, uid in zip(urunler, idler):
            sonuc.append({
                "id": uid,
                "musteri_adi": urun.musteri_adi,
                "agirlik": urun.agirlik,
                "baski_suresi": urun.baski_suresi,
                "basim_zorlugu": urun.basim_zorlugu,
                "malzeme": urun.malzeme,
                "aciklama": urun.aciklama,
                "basim_tarihi": urun.basim_tarihi,
                "filament_maliyet": urun.filament_maliyet,
                "elektrik_maliyet": urun.elektrik_maliyet,
                "baski_maliyet": urun.baski_maliyet,
                "ham_maliyet": urun.ham_maliyet,
                "satis_fiyati": urun.satis_fiyati,
                "kar": urun.kar,
            })
        return sonuc
    finally:
        db.close()

@app.delete("/urun/{urun_id}")
def urun_sil(urun_id: int):
    db = UrunDataBase()
    try:
        silinen = db.delete_urun(urun_id)
        if silinen == 0:
            raise HTTPException(status_code=404, detail="Ürün bulunamadı")
        return {"deleted": urun_id}
    finally:
        db.close()

@app.post("/maliyet/hesapla")
def maliyet_hesapla(data: dict):
    zorunlu_alanlar = [
        "agirlik",
        "baski_suresi",
        "malzeme",
        "basim_zorlugu"
    ]

    for alan in zorunlu_alanlar:
        if alan not in data:
            raise HTTPException(
                status_code=400,
                detail=f"Eksik alan: {alan}"
            )

    try:
        agirlik = float(data["agirlik"])
        baski_suresi = float(data["baski_suresi"])
        malzeme = str(data["malzeme"])
        basim_zorlugu = str(data["basim_zorlugu"])
    except Exception:
        raise HTTPException(
            status_code=400,
            detail="Alan tipleri hatalı"
        )

    urun = Urun()
    urun.agirlik = agirlik
    urun.baski_suresi = baski_suresi
    urun.malzeme = malzeme
    urun.basim_zorlugu = basim_zorlugu

    maliyet_db = MaliyetDataBase()
    MaliyetHesapla(urun, maliyet_db)

    return {
        "filament_maliyet": urun.filament_maliyet,
        "elektrik_maliyet": urun.elektrik_maliyet,
        "baski_maliyet": urun.baski_maliyet,
        "ham_maliyet": urun.ham_maliyet,
        "satis_fiyati": urun.satis_fiyati,
        "kar": urun.kar,
    }
    
@app.put("/sabit")
def sabit_guncelle(data: dict):
    db = MaliyetDataBase()
    try:
        db.set_filament_kg_maliyet(data["filament_kg_maliyet"])
        db.set_saat_basi_kw(data["saat_basi_kw"])
        db.set_kwh_fiyat(data["kwh_fiyat"])
        db.set_saatlik_baski_ucreti(data["saatlik_baski_ucreti"])
        db.set_saatlik_baski_katsayi(data["saatlik_baski_katsayi"])
        db.set_sabit_kurulum_ucreti(data["sabit_kurulum_ucreti"])
        db.set_kar_orani(data["kar_orani"])
        return {"status": "ok"}
    finally:
        db.close()

@app.get("/excel")
def excel_al():
    db = UrunDataBase()
    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".xlsx") as f:
            db.excel_cikti_al(f.name)
            return FileResponse(f.name, filename="urunler.xlsx")
    finally:
        db.close()