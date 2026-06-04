import configparser

class Config:
    def __init__(self, file_name):
        self.file_name = file_name
        self.config = configparser.ConfigParser()

    def load(self):
        try:
            self.config.read(self.file_name)
        except Exception as e:
            return f"Error loading config: {e}"


class DatabaseConfig(Config):
    def __init__(self, file_name):
        super().__init__(file_name)
        self.db_settings = {}

    def load_db_config(self):
        self.load()

        if "DATABASE" not in self.config:
            return "Missing DATABASE section!"

        required_keys = ["host", "port", "user", "password"]

        for key in required_keys:
            if key not in self.config["DATABASE"]:
                return f"Missing key: {key}"

        self.db_settings = {
            "host": self.config["DATABASE"]["host"],
            "port": int(self.config["DATABASE"]["port"]),
            "user": self.config["DATABASE"]["user"],
            "password": self.config["DATABASE"]["password"]
        }

        return self.db_settings


db_config = DatabaseConfig("db.ini")

result = db_config.load_db_config()

if isinstance(result, dict):
    print("Database Configuration Loaded:")
    for key, value in result.items():
        print(f"{key}: {value}")
else:
    print(result)