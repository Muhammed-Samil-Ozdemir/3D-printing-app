from database_interface import Database
from urun import Urun
from maliyet_hesaplayici import MaliyetHesapla
import pandas as pd

class UrunDataBase(Database):
    def __init__(self):
        super().__init__()
        self.tablo = "urunler"


    def ekle(self, urun: Urun):
        MaliyetHesapla(urun)
        self.cursor.execute(f"""
            INSERT INTO {self.tablo} (
                musteri_adi, agirlik, baski_suresi,
                basim_zorlugu, malzeme,
                aciklama, basim_tarihi,
                filament_maliyet, elektrik_maliyet,
                baski_maliyet, ham_maliyet,
                satis_fiyati, kar
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (
            urun.musteri_adi,
            urun.agirlik,
            urun.baski_suresi,
            urun.basim_zorlugu,
            urun.malzeme,
            urun.aciklama,
            urun.basim_tarihi,
            
            
            urun.filament_maliyet,
            urun.elektrik_maliyet,
            urun.baski_maliyet,
            urun.ham_maliyet,
            urun.satis_fiyati,
            urun.kar
        ))
        self.conn.commit()
        try:
            return self.cursor.lastrowid
        except AttributeError:
            return None

    def get_all(self):
        self.cursor.execute(f"SELECT * FROM {self.tablo}")
        rows = self.cursor.fetchall()
        urunler = []
        id_listesi = []
        for row in rows:
            id_listesi.append(row[0])
            urun = Urun()
            urun.musteri_adi = row[1]
            urun.agirlik = row[2]
            urun.baski_suresi = row[3]
            urun.basim_zorlugu = row[4]
            urun.malzeme = row[5]
            urun.aciklama = row[6]
            urun.basim_tarihi = row[7]
            urun.filament_maliyet = row[8]
            urun.elektrik_maliyet = row[9]
            urun.baski_maliyet = row[10]
            urun.ham_maliyet = row[11]
            urun.satis_fiyati = row[12]
            urun.kar = row[13]
            urunler.append(urun)
        return urunler, id_listesi

    def delete_urunler(self, id_listesi):
        self.cursor.executemany(
            f"DELETE FROM {self.tablo} WHERE id=%s",
            [(i,) for i in id_listesi]
        )
        self.conn.commit()

    def delete_urun(self, id):
        self.cursor.execute(
            f"DELETE FROM {self.tablo} WHERE id=%s",
            (id,)
        )
        self.conn.commit()
        return self.cursor.rowcount

    def get_by_id(self, id):
        self.cursor.execute(
            f"SELECT * FROM {self.tablo} WHERE id=%s",
            (id,)
        )
        row = self.cursor.fetchone()
        if not row:
            return None
        urun = Urun()
        urun.musteri_adi = row[1]
        urun.agirlik = row[2]
        urun.baski_suresi = row[3]
        urun.basim_zorlugu = row[4]
        urun.malzeme = row[5]
        urun.aciklama = row[6]
        urun.basim_tarihi = row[7]
        urun.filament_maliyet = row[8]
        urun.elektrik_maliyet = row[9]
        urun.baski_maliyet = row[10]
        urun.ham_maliyet = row[11]
        urun.satis_fiyati = row[12]
        urun.kar = row[13]
        return urun, row[0]

    def update_urun(self, id, urun: Urun):
        # Yeniden maliyeti hesapla (eğer alanlar değiştiyse)
        MaliyetHesapla(urun)
        self.cursor.execute(f"""
            UPDATE {self.tablo} SET
                musteri_adi=%s,
                agirlik=%s,
                baski_suresi=%s,
                basim_zorlugu=%s,
                malzeme=%s,
                aciklama=%s,
                basim_tarihi=%s,
                filament_maliyet=%s,
                elektrik_maliyet=%s,
                baski_maliyet=%s,
                ham_maliyet=%s,
                satis_fiyati=%s,
                kar=%s
            WHERE id=%s
        """, (
            urun.musteri_adi,
            urun.agirlik,
            urun.baski_suresi,
            urun.basim_zorlugu,
            urun.malzeme,
            urun.aciklama,
            urun.basim_tarihi,
            urun.filament_maliyet,
            urun.elektrik_maliyet,
            urun.baski_maliyet,
            urun.ham_maliyet,
            urun.satis_fiyati,
            urun.kar,
            id
        ))
        self.conn.commit()
        return self.cursor.rowcount

    def excel_cikti_al(self, dosya_yolu):
        urunler, _ = self.get_all()
        data = []
        for urun in urunler:
            data.append({
                "Müşteri Adı": urun.musteri_adi,
                "Ağırlık (g)": urun.agirlik,
                "Baskı Süresi (saat)": urun.baski_suresi,
                "Basım Zorluğu": urun.basim_zorlugu,
                "Malzeme": urun.malzeme,
                "Açıklama": urun.aciklama,
                "Basım Tarihi": urun.basim_tarihi,
                "Filament Maliyeti": urun.filament_maliyet,
                "Elektrik Maliyeti": urun.elektrik_maliyet,
                "Baskı Maliyeti": urun.baski_maliyet,
                "Ham Maliyet": urun.ham_maliyet,
                "Satış Fiyatı": urun.satis_fiyati,
                "Kar": urun.kar
            })
        
        df = pd.DataFrame(data)
        df.to_excel(dosya_yolu, index=False)
