import os
import toml

class Config:
    """Handles loading and retrieving configuration settings."""
    
    def __init__(self, config_path="configs/config.toml"):
        self.config_path = config_path
        self.config = self._load_config()

    def _load_config(self):
        """Loads and parses the TOML configuration file."""
        if not os.path.exists(self.config_path):
            raise FileNotFoundError(f"Configuration file not found: {self.config_path}")

        try:
            return toml.load(self.config_path)
        except Exception as e:
            raise RuntimeError(f"Error parsing TOML file: {e}")

    def get(self, section, key, default=None):
        """Retrieves a configuration value."""
        return self.config.get(section, {}).get(key, default)

# Example usage:
if __name__ == "__main__":
    config = Config()
    print("App Name:", config.get("general", "app_name"))
    print("Training Epochs:", config.get("training", "epochs"))
