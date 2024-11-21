from pathlib import Path

from syftbox.lib import Client

SCRIPT_DIR = Path(__file__).parent.absolute()

if __name__ == "__main__":
    client = Client.load()
    public_dir = Path(client.my_datasite) / "public"
    model_files = list(public_dir.glob("pretrained_mnist_label_*.pt"))

    if not len(model_files):
        print(f"No pre-trained model files found in {public_dir}.")
        print(f"Kindly copy one or more from '{SCRIPT_DIR / "pretrained_models"}' and place them in your public folder.")
        exit(0)

    print("Found pre-trained model(s):")
    for p in model_files:
        print(f"- {p}")
