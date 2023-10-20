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

### urls/Urls.txt

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

### Envdata.log

```plaintext
##################################################
URL : http://vimuktisanstha.org//.env
APP_NAME=Laravel
APP_ENV=local
APP_KEY=base64:bRxqlMC9e3vPy/EnY/KyX7CQRkPDp9KoeG9rZXHr6Qk=
APP_DEBUG=false
APP_URL=http://localhost

LOG_CHANNEL=stack
LOG_LEVEL=debug

DB_CONNECTION=mysql
DB_HOST=127.0.0.1
DB_PORT=3306
DB_DATABASE=u567663563_vimukti
DB_USERNAME=u567663563_vimukti
DB_PASSWORD=1n;:2asD2$@Y

BROADCAST_DRIVER=log
CACHE_DRIVER=file
FILESYSTEM_DRIVER=local
QUEUE_CONNECTION=sync
SESSION_DRIVER=file
SESSION_LIFETIME=120

MEMCACHED_HOST=127.0.0.1

REDIS_HOST=127.0.0.1
REDIS_PASSWORD=null
REDIS_PORT=6379

MAIL_MAILER=smtp
MAIL_HOST=mailhog
MAIL_PORT=1025
MAIL_USERNAME=null
MAIL_PASSWORD=null
MAIL_ENCRYPTION=null
MAIL_FROM_ADDRESS=null
MAIL_FROM_NAME="${APP_NAME}"

AWS_ACCESS_KEY_ID=
AWS_SECRET_ACCESS_KEY=
AWS_DEFAULT_REGION=us-east-1
AWS_BUCKET=
AWS_USE_PATH_STYLE_ENDPOINT=false

PUSHER_APP_ID=
PUSHER_APP_KEY=
PUSHER_APP_SECRET=
PUSHER_APP_CLUSTER=mt1

MIX_PUSHER_APP_KEY="${PUSHER_APP_KEY}"
MIX_PUSHER_APP_CLUSTER="${PUSHER_APP_CLUSTER}"

RECAPTCHA_SECRET=6LfVpeUbAAAAAHn8lQIOzG1tQjkoDDzsT8WQJB6c
RECAPTCHA_SITEKEY=6LfVpeUbAAAAAJnvBQ6HAzaAgTgdPxyim6c8Yz9P

RAZOR_KEY=rzp_live_xwzhAeWwtGya5N
RAZOR_SECRET=2yXRAlgr2Iq7wtlgZEVBoGgC 
##################################################
###
...See more
```

**Repository Views** ![Views](https://profile-counter.glitch.me/lavscanner/count.svg)

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your improvements.

## License

This project is licensed under the [MIT License](LICENSE).
