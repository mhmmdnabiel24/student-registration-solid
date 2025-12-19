import logging
from abc import ABC, abstractmethod

# Konfigurasi logging
logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s - %(message)s"
)

class IValidationRule(ABC):
    """Interface untuk semua aturan validasi registrasi."""

    @abstractmethod
    def validate(self) -> bool:
        """Melakukan validasi dan mengembalikan hasil boolean.

        Returns:
            bool: True jika valid, False jika tidak valid.
        """
        pass


class SksLimitRule(IValidationRule):
    """Aturan validasi batas maksimal SKS."""

    def __init__(self, sks: int):
        """Inisialisasi jumlah SKS mahasiswa.

        Args:
            sks (int): Jumlah SKS yang diambil mahasiswa.
        """
        self.sks = sks

    def validate(self) -> bool:
        """Validasi jumlah SKS.

        Returns:
            bool: True jika SKS <= 24, False jika melebihi.
        """
        if self.sks > 24:
            logging.warning("Validasi SKS gagal: SKS melebihi batas")
            return False
        logging.info("Validasi SKS berhasil")
        return True


class PrerequisiteRule(IValidationRule):
    """Aturan validasi prasyarat mata kuliah."""

    def __init__(self, prerequisite_completed: bool):
        """Inisialisasi status prasyarat.

        Args:
            prerequisite_completed (bool): Status prasyarat.
        """
        self.prerequisite_completed = prerequisite_completed

    def validate(self) -> bool:
        """Validasi prasyarat mata kuliah.

        Returns:
            bool: True jika prasyarat terpenuhi, False jika tidak.
        """
        if not self.prerequisite_completed:
            logging.warning("Validasi prasyarat gagal")
            return False
        logging.info("Validasi prasyarat berhasil")
        return True


class IpkRule(IValidationRule):
    """Aturan validasi IPK minimum."""

    def __init__(self, ipk: float):
        """Inisialisasi nilai IPK.

        Args:
            ipk (float): Nilai IPK mahasiswa.
        """
        self.ipk = ipk

    def validate(self) -> bool:
        """Validasi IPK mahasiswa.

        Returns:
            bool: True jika IPK >= 3.0, False jika tidak.
        """
        if self.ipk < 3.0:
            logging.warning("Validasi IPK gagal")
            return False
        logging.info("Validasi IPK berhasil")
        return True


class RegistrationService:
    """Service untuk mengelola proses registrasi mahasiswa."""

    def __init__(self, rules: list[IValidationRule]):
        """Inisialisasi service dengan daftar aturan validasi.

        Args:
            rules (list[IValidationRule]): Daftar aturan validasi.
        """
        self.rules = rules

    def register(self) -> bool:
        """Menjalankan seluruh aturan validasi.

        Returns:
            bool: True jika semua validasi berhasil, False jika gagal.
        """
        for rule in self.rules:
            if not rule.validate():
                logging.warning("Registrasi mahasiswa gagal")
                return False
        logging.info("Registrasi mahasiswa berhasil")
        return True


# ===== PROGRAM UTAMA =====
if __name__ == "__main__":
    rules = [
        SksLimitRule(22),
        PrerequisiteRule(True),
        IpkRule(3.6)
    ]

    service = RegistrationService(rules)
    service.register()
