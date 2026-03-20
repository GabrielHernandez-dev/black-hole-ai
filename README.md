# 🤖 Local AI Setup — Docker + Ollama + Open WebUI

A fully local, private AI assistant running on your own machine — no cloud, no subscriptions, no data leaving your PC. Includes desktop shortcuts to launch and stop the AI in one click, plus a utility to customize the icon.

Built with [Ollama](https://ollama.com) + [Open WebUI](https://github.com/open-webui/open-webui) + [Mistral 7B](https://mistral.ai/).

---

## ✨ Features

- 🔒 **100% local & private** — conversations never leave your machine
- ⚡ **GPU-accelerated** — runs on NVIDIA GPUs via CUDA
- 🌐 **Beautiful web interface** — Open WebUI in your browser
- 🚀 **One-click launch & stop** — two `.bat` shortcuts for your desktop
- 🎨 **Custom icon support** — convert any PNG to `.ico` for your shortcuts

---

## 🖥️ Requirements

- Windows 10/11
- [Docker Desktop](https://www.docker.com/products/docker-desktop/) installed and running
- [Ollama](https://ollama.com) installed
- NVIDIA GPU with 8GB+ VRAM (tested on RTX 3060 Ti)
- NVIDIA drivers + [CUDA Toolkit](https://developer.nvidia.com/cuda-downloads)
- Python 3.x + Pillow (only needed for the icon converter)

> ⚠️ No GPU? Remove `--gpus all` and use image `ghcr.io/open-webui/open-webui:main` instead. It will run on CPU but slower.

---

## 🚀 Installation

### 1. Pull the model

```bash
ollama pull mistral
```

### 2. Launch Open WebUI with Docker

```bash
docker run -d ^
  --restart always ^
  -p 127.0.0.1:3000:8080 ^
  --gpus all ^
  -v open-webui:/app/backend/data ^
  --name open-webui ^
  ghcr.io/open-webui/open-webui:cuda
```

> `-p 127.0.0.1:3000:8080` ensures the interface is only accessible from your own machine. No one on your network or the internet can reach it.

### 3. Copy the shortcuts to your desktop

- `lanzar_ia.bat` — starts the container and opens the browser
- `stop_ai.bat` — stops the container when you're done

### 4. First launch

Go to `http://localhost:3000`, create a local account, select **mistral** as your model, and start chatting.

---

## 📁 Files

| File | Description |
|------|-------------|
| `lanzar_ia.bat` | Starts Open WebUI and opens the browser |
| `stop_ai.bat` | Stops the Docker container |
| `convertir_a_ico.py` | Converts a PNG image to a Windows `.ico` icon |

---

## 🎨 Custom Icon (optional)

To use a custom icon for your `.bat` shortcuts:

1. Place your PNG image in the same folder as `convertir_a_ico.py`
2. Edit the filename in the script:
```python
archivo_entrada = "your_image.png"
archivo_salida = "your_image.ico"
```
3. Install Pillow if needed:
```bash
pip install Pillow
```
4. Run it:
```bash
python convertir_a_ico.py
```
5. Right-click your shortcut → Properties → Change Icon → select the `.ico`

---

## 🔄 Other Models

```bash
ollama pull llama3.1      # Great all-rounder
ollama pull gemma2        # Strong creative writing
ollama pull qwen2.5       # Good at code too
ollama pull deepseek-r1   # Reasoning-focused
```

---

## 🔐 Security

| Threat | Status |
|--------|--------|
| Internet access | ✅ Blocked |
| Local network (WiFi) | ✅ Blocked |
| Data sent to cloud | ✅ Never |

Verify your setup:
```bash
docker inspect open-webui | findstr HostIp
# Expected: "HostIp": "127.0.0.1"
```

---

## 📄 License

MIT — use it, fork it, build on it.

---

*Made with curiosity in Gran Canaria 🌋*
