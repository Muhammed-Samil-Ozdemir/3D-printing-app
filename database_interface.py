import mysql.connector

class Database:
    def __init__(self,
                 host="***",
                 user="***",
                 password="***",
                 database="***"):
        
        self.conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database,
            autocommit=True
        )
        self.cursor = self.conn.cursor()

    def close(self):
        self.cursor.close()
        self.conn.close()

    def _get_sabit_deger(self, kolon, tablo):
        self.cursor.execute(
            f"SELECT {kolon} FROM {tablo} WHERE id = 1"
        )
        row = self.cursor.fetchone()
        return row[0] if row else None

    def _set_sabit_deger(self, kolon, deger, tablo):
        self.cursor.execute(
            f"UPDATE {tablo} SET {kolon} = %s WHERE id = 1",
            (deger,)
        )

    def _get_katsayi(self, tablo, ad_kolon, ad_deger, katsayi_kolon):
        self.cursor.execute(
            f"SELECT {katsayi_kolon} FROM {tablo} WHERE {ad_kolon} = %s",
            (ad_deger,)
        )
        row = self.cursor.fetchone()
        return row[0] if row else 1.0

    def _set_katsayi(self, tablo, ad_kolon, ad_deger, katsayi_kolon, katsayi):
        self.cursor.execute(f"""
            INSERT INTO {tablo} ({ad_kolon}, {katsayi_kolon})
            VALUES (%s, %s)
            ON DUPLICATE KEY UPDATE {katsayi_kolon} = VALUES({katsayi_kolon})
        """, (ad_deger, katsayi))

    def _get_list(self, tablo, kolon):
        self.cursor.execute(
            f"SELECT {kolon} FROM {tablo} ORDER BY id ASC"
        )
        rows = self.cursor.fetchall()
        return [row[0] for row in rows]
