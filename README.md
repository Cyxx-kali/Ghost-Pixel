# Ghost-Pixel

> A CLI Steganography tool for hiding secret messages inside images.

![Ghost Pixel Banner](https://img.shields.io/badge/GHOST--PIXEL-Made%20by%20Cyxx-magenta?style=for-the-badge)

**Ghost-Pixel** allows you to securely hide text messages within PNG images using Least Significant Bit (LSB) steganography. It is a lightweight, command-line interface tool built for simplicity and privacy.

## Features

-   **Hide Messages**: Embed secret text into PNG images without noticeable visual changes.
-   **Reveal Messages**: Extract hidden text from encoded images.
-   **CLI Interface**: Simple and intuitive command-line usage.
-   **Cross-Platform**: Works on Windows, macOS, and Linux.

## Tech Stack

-   **Python 3.x**
-   **Stegano**: For the steganography logic (LSB).
-   **Click**: For building the Command Line Interface.
-   **Colorama**: For colored terminal output.

## Installation

1.  **Clone the Repository**

    ```bash
    git clone https://github.com/yourusername/ghost-pixel.git
    cd ghost-pixel
    ```

2.  **Install Dependencies**

    It is recommended to use a virtual environment.

    ```bash
    pip install -r requirements.txt
    ```

## Usage

Run the tool using `python main.py`.

### Hide a Message

Hide a secret message inside a carrier image.

```bash
python main.py hide --image input.png --message "Top Secret Message" --output secret.png
```

*   `--image` / `-i`: Path to the source image (must be PNG).
*   `--message` / `-m`: The text message to hide.
*   `--output` / `-o`: (Optional) The output filename. Defaults to `secret.png`.

### Reveal a Message

Extract and display the hidden message from an encoded image.

```bash
python main.py reveal --image secret.png
```

*   `--image` / `-i`: Path to the encoded image.

### Help

To see the list of available commands:

```bash
python main.py --help
```

## Disclaimer

This tool is for educational purposes only. Use it responsibly.

## License

Distributed under the MIT License. See `LICENSE` for more information.

---
**Developed by Cyxx**
