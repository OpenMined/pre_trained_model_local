from syftbox.lib import Client
import random
import os
from pathlib import Path
import shutil

AVAILABLE_MODELS = list(Path("./pretrained_models").glob("*.pt"))


def copy_random_pretrained_model(path: Path) -> None:
    # check if there is any pretrained model in the path
    pretrained_entries = list(Path(path).rglob("pretrained_mnist_label_*.pt"))
    if len(pretrained_entries) > 0:
        print(f"Pretrained model already exists at '{pretrained_entries[0]}'")
        return

    # get a random pretrained model
    src_path = random.choice(AVAILABLE_MODELS)
    target_path = path / src_path.name
    print(f"Copying pretrained model to '{target_path}'")
    # copy the random entry to the path
    shutil.copy2(src_path, path)


if __name__ == "__main__":
    client = Client.load()

    # Create Private Directory
    private_path = Path(client.my_datasite) / "private"
    os.makedirs(private_path, exist_ok=True)

    # Copy a Randon Pretrained Model to private
    copy_random_pretrained_model(private_path)
