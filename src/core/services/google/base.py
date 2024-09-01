class GoogleServiceManager:
    def __init__(self, service_account_key_path: str, scopes: list[str]):
        self.service_account_key_path = service_account_key_path
        self.scopes = scopes
        self.creds = self._load_credentials()
        self.aiogoogle = None

    def _load_credentials(self):
        import json
        import os
        from aiogoogle.auth.creds import ServiceAccountCreds

        if os.path.exists(self.service_account_key_path):
            with open(self.service_account_key_path, "r") as file:
                service_account_key = json.load(file)
            return ServiceAccountCreds(scopes=self.scopes, **service_account_key)
        else:
            raise FileNotFoundError(
                f"Service account key file '{self.service_account_key_path}' not found."
            )
