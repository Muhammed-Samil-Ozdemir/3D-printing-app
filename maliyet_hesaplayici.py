from urun import Urun
from maliyet_db_manager import MaliyetDataBase

class MaliyetHesapla:
    def __init__(self, urun: Urun, maliyet_db: MaliyetDataBase):
        self.maliyet_db = maliyet_db

        urun.filament_maliyet = (
            (urun.agirlik / 1000) *
            self.maliyet_db.get_filament_kg_maliyet() *
            self.maliyet_db.get_malzeme_katsayi(urun.malzeme)
        )

        urun.elektrik_maliyet = (
            urun.baski_suresi *
            self.maliyet_db.get_saat_basi_kw() *
            (self.maliyet_db.get_kwh_fiyat() / 10)
        )

        urun.baski_maliyet = (
            urun.baski_suresi *
            self.maliyet_db.get_saatlik_baski_ucreti() *
            self.maliyet_db.get_saatlik_baski_katsayi() *
            self.maliyet_db.get_zorluk_katsayi(urun.basim_zorlugu)
        )

        urun.ham_maliyet = (
            urun.filament_maliyet +
            urun.elektrik_maliyet +
            urun.baski_maliyet +
            self.maliyet_db.get_sabit_kurulum_ucreti()
        )

        urun.satis_fiyati = urun.ham_maliyet * (
            1 + (self.maliyet_db.get_kar_orani() / 100)
        )

        urun.kar = urun.satis_fiyati - urun.ham_maliyet
