import os
import platform
import subprocess
import urllib.request

from tqdm import tqdm


def install_ffmpeg():
    system = platform.system()

    if system == "Darwin":
        # macOS
        subprocess.run(["brew", "update"], check=False)
        subprocess.run(["brew", "install", "ffmpeg"], check=False)
    elif system == "Linux":
        # Linux
        subprocess.run(["sudo", "apt-get", "update"], check=False)
        subprocess.run(["sudo", "apt-get", "install", "-y", "ffmpeg"], check=False)
    elif system == "Windows":
        # Windows
        urls = [
            "https://huggingface.co/Politrees/RVC_resources/resolve/main/tools/ffmpeg/ffmpeg.exe?download=true",
            "https://huggingface.co/Politrees/RVC_resources/resolve/main/tools/ffmpeg/ffplay.exe?download=true",
            "https://huggingface.co/Politrees/RVC_resources/resolve/main/tools/ffmpeg/ffprobe.exe?download=true",
        ]
        for url in urls:
            filename = os.path.basename(url.split("?")[0])
            with tqdm(unit="B", unit_scale=True, unit_divisor=1024, desc=filename) as t:
                def progress_hook(count, block_size, total_size):
                    t.total = total_size
                    t.update(block_size)

                urllib.request.urlretrieve(url, filename, reporthook=progress_hook)
    else:
        print(f"Unsupported OS: {system}")

def main():
    install_ffmpeg()

if __name__ == "__main__":
    main()
