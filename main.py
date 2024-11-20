from syftbox.lib import Client
import os
from pathlib import Path
import re


def get_model_file(path: Path):
    model_files = []
    entries = os.listdir(path)
    pattern = r"^pretrained_mnist_label_[0-9]\.pt$"

    for entry in entries:
        if re.match(pattern, entry):
            model_files.append(entry)

    return model_files if model_files else None
    

if __name__ == "__main__":
    client = Client.load()

    # Create Private Directory
    public_folder = client.my_datasite / "public"
    model_files = get_model_file(public_folder)

    if not model_files:
        print("[Pretraied Model Local]: No model files found in Public Folder.")
        print("Kindly go to apis/pretrained_model_local/pretrained_models")
        print(f"Pick a model file and copy it to the public folder (datasites/{client.email}/public)")
    else:
        print(f"[Pretrained Model Local]: Found model files: {model_files} in Public Folder.")