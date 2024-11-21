import json
import os
import sys
from datetime import datetime

class ScriptLogger:
    def __init__(self, log_path="scriptlog.json", log_dir=".", error_level="INFO"):
        # Ensure the log directory exists
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)
        
        self.log_path = os.path.join(log_dir, log_path)
        self.error_level = error_level
        self.date_today = datetime.now().strftime("%Y-%m-%d")
        self.script_name = os.path.basename(sys.argv[0])
        self.log_data = self._load_log()
        
    def _load_log(self):
        if os.path.exists(self.log_path):
            with open(self.log_path, "r") as logfile:
                return json.load(logfile)
        return {}
        
    def _save_log(self):
        with open(self.log_path, "w") as logfile:
            json.dump(self.log_data, logfile, indent=4)
            
    def log_run(self):
        if (self.date_today in self.log_data 
            and self.log_data.get(self.date_today, {}).get("error_level") not in ["ERROR", "CRITICAL"]):
            print("Script has already run with no errors.")
            return             
            
        self.log_data[self.date_today] = {
            "ran_in": self.script_name,
            "ran": True,
            "error_level": self.error_level
        }
        
        self._save_log()
        print(f"Logged today's run with error level: {self.error_level}.")