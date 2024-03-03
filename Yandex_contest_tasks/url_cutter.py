"""Encrypts and shortens the link."""


import hashlib


class MarsURLEncoder:
    """Укорачивает ссылку с хешированием: https://ma.rs/<hash>
        где <hash> это захешированная ссылка.
    """
    def __init__(self):
        self.url_dict = {}

    def encode(self, long_url):
        """Кодирует длинную ссылку в короткую вида https://ma.rs/X7NYIol."""
        url_bytes = long_url.encode('utf-8')
        hash_bytes = hashlib.sha256(url_bytes).digest()
        hash_str = hash_bytes.hex()
        encoded_url = hash_str[:8]
        self.url_dict[encoded_url] = long_url
        my_service = 'https://ma.rs/'
        short_url = my_service + encoded_url
        return short_url

    def decode(self, short_url):
        """Декодирует короткую ссылку вида https://ma.rs/X7NYIol в исходную."""
        short_url_split = short_url.split('/')
        long_url = self.url_dict[short_url_split[3]]
        return long_url
