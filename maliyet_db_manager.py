from database_interface import Database

class MaliyetDataBase(Database):
    def __init__(self):
        super().__init__()
        self.sabit = "sabit_maliyetler"
        self.malzeme = "malzeme_katsayilari"
        self.zorluk = "zorluk_katsayilari"

    
    def get_filament_kg_maliyet(self):
        return self._get_sabit_deger("filament_kg_maliyet", self.sabit)

    def get_saat_basi_kw(self):
        return self._get_sabit_deger("saat_basi_kw", self.sabit)

    def get_kwh_fiyat(self):
        return self._get_sabit_deger("kwh_fiyat", self.sabit)

    def get_saatlik_baski_ucreti(self):
        return self._get_sabit_deger("saatlik_baski_ucreti", self.sabit)

    def get_saatlik_baski_katsayi(self):
        return self._get_sabit_deger("saatlik_baski_katsayi", self.sabit)

    def get_sabit_kurulum_ucreti(self):
        return self._get_sabit_deger("sabit_kurulum_ucreti", self.sabit)

    def get_kar_orani(self):
        return self._get_sabit_deger("kar_orani", self.sabit)

    def get_malzeme_katsayi(self, malzeme):
        return self._get_katsayi(
            tablo=self.malzeme,
            ad_kolon="malzeme_adi",
            ad_deger=malzeme,
            katsayi_kolon="katsayi"
        )
    
    def get_malzeme_listesi(self):
        return self._get_list(
            tablo=self.malzeme,
            kolon="malzeme_adi"
        )

    def get_zorluk_katsayi(self, zorluk):
        return self._get_katsayi(
            tablo=self.zorluk,
            ad_kolon="zorluk_adi",
            ad_deger=zorluk,
            katsayi_kolon="katsayi"
        )
    
    def get_zorluk_listesi(self):
        return self._get_list(
            tablo=self.zorluk,
            kolon="zorluk_adi"
        )
    
    def set_filament_kg_maliyet(self, deger):
        self._set_sabit_deger("filament_kg_maliyet", deger, self.sabit)

    def set_saat_basi_kw(self, deger):
        self._set_sabit_deger("saat_basi_kw", deger, self.sabit)

    def set_kwh_fiyat(self, deger):
        self._set_sabit_deger("kwh_fiyat", deger, self.sabit)

    def set_saatlik_baski_ucreti(self, deger):
        self._set_sabit_deger("saatlik_baski_ucreti", deger, self.sabit)

    def set_saatlik_baski_katsayi(self, deger):
        self._set_sabit_deger("saatlik_baski_katsayi", deger, self.sabit)

    def set_sabit_kurulum_ucreti(self, deger):
        self._set_sabit_deger("sabit_kurulum_ucreti", deger, self.sabit)

    def set_kar_orani(self, deger):
        self._set_sabit_deger("kar_orani", deger, self.sabit)

    def set_malzeme_katsayi(self, malzeme, katsayi):
        self._set_katsayi(
            tablo=self.malzeme,
            ad_kolon="malzeme_adi",
            ad_deger=malzeme,
            katsayi_kolon="katsayi",
            katsayi=katsayi
        )

    def set_zorluk_katsayi(self, zorluk, katsayi):
        self._set_katsayi(
            tablo=self.zorluk,
            ad_kolon="zorluk_adi",
            ad_deger=zorluk,
            katsayi_kolon="katsayi",
            katsayi=katsayi
        )
