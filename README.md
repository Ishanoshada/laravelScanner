# Laravel Scanner

![GitHub stars](https://img.shields.io/github/stars/Ishanoshada/laravelScanner?style=social)
![GitHub forks](https://img.shields.io/github/forks/Ishanoshada/laravelScanner?style=social)
![GitHub watchers](https://img.shields.io/github/watchers/Ishanoshada/laravelScanner?style=social)
![GitHub license](https://img.shields.io/github/license/Ishanoshada/laravelScanner)

---


## Overview

Laravel Scanner is a powerful tool designed to identify Laravel installations by scanning for `.env` files. It automates the process of finding Laravel applications, making it useful for security professionals, developers, and system administrators.

## Features

- Quickly identifies Laravel installations from a list of URLs.
- Supports both file-based input and manual URL entry.
- Multithreaded scanning for efficiency.
- User-friendly interface with color-coded output.
- Logs detailed information about discovered Laravel installations.
- [Author: Ishan Oshada](https://github.com/Ishanoshada)

## Getting Started

### Prerequisites

- Python 3.x
- `requests` library (install via `pip install requests`)

### Installation

1. Clone the repository:

```bash
git clone https://github.com/Ishanoshada/laravelScanner.git
```

2. Change to the project directory:

```bash
cd laravelScanner
```

### Usage

#### Scanning from a File

```bash
python main.py -f urls.txt
```

Replace `urls.txt` with the path to your file containing a list of URLs.

#### Manual Scan

```bash
python main.py
```

Follow the prompts to enter URLs manually. Type `done` when finished.

### Example

```bash
python main.py -f sample_urls.txt
```

### Urls.txt

```plaintext
http://excelpsschool.edu.np/
http://offers.code-pages.com/
http://aram-clinic.de/
http://filmentry.londonscreenings.org.uk/
http://timehrm.com/
http://advapa.com.br/
http://api-analytics.blockchain.mn/
http://www.stillunfold.com/
http://www.okutics.com/
http://xeepp.com/
http://www.martindoherty.co.uk/
http://thanks-navi.info/
http://lcci-metin.com/
http://www.uw-woonidee.nl/
http://seoledger.com/
http://www.sluice.ru/
http://marmaristatilim.com/
http://crontosys.com/
http://aajkal.news/
http://www.a-plus-eg.com/
http://www.baburambhattarai.com/
http://www.modnaredakcia.com/
http://finda.in/
```

You can use this list of URLs as an add-on to your `urls.txt` file when running the Laravel Scanner.

**Repository Views** ![Views](https://profile-counter.glitch.me/lavscanner/count.svg)

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your improvements.

## License

This project is licensed under the [MIT License](LICENSE).
