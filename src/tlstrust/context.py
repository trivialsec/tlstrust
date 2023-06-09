__module__ = "tlstrust.context"

INVALID_CONTEXT = "context_type provided is invalid {}"
SOURCE_CCADB = 0
SOURCE_JAVA = 1
SOURCE_ANDROID = 3
SOURCE_RUSTLS = 5
SOURCE_CURL = 6
SOURCE_DART = 7
SOURCE_CERTIFI = 101
SOURCE_RUSSIA = 201
PLATFORM_FEDORA_LINUX = SOURCE_CCADB  # https://src.fedoraproject.org/rpms/ca-certificates/raw/rawhide/f/certdata.txt
PLATFORM_ARCH_LINUX = PLATFORM_FEDORA_LINUX  # https://archlinux.org/packages/core/any/ca-certificates/ Upstream URL: https://src.fedoraproject.org/rpms/ca-certificates
PLATFORM_DEBIAN_LINUX = (
    SOURCE_CCADB  # https://packages.debian.org/en/sid/ca-certificates
)
PLATFORM_UBUNTU_LINUX = PLATFORM_DEBIAN_LINUX  # https://launchpad.net/ca-certificates
PLATFORM_ALPINE_LINUX = (
    SOURCE_CCADB  # https://git.alpinelinux.org/ca-certificates/plain/certdata.txt
)
PLATFORM_CENTOS_LINUX = SOURCE_CCADB  # https://centos.pkgs.org/7/centos-x86_64/ca-certificates-2020.2.41-70.0.el7_8.noarch.rpm.html
PLATFORM_RHEL_LINUX = SOURCE_CCADB  # https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html/security_guide/sec-shared-system-certificates
PLATFORM_OPENBSD = SOURCE_CCADB  # https://pkgsrc.se/security/ca-certificates
PLATFORM_FREEBSD = SOURCE_CCADB  # https://www.freshports.org/security/ca_root_nss/
PLATFORM_JAVA = SOURCE_JAVA
PLATFORM_WINDOWS = SOURCE_CCADB
PLATFORM_APPLE = SOURCE_CCADB
PLATFORM_ANDROID = SOURCE_ANDROID
PLATFORM_ANDROID_LATEST = SOURCE_ANDROID
PLATFORM_ANDROID2_2 = 1302
PLATFORM_ANDROID2_3 = 2302
PLATFORM_ANDROID3 = 303
PLATFORM_ANDROID4 = 304
PLATFORM_ANDROID4_4 = 1304
PLATFORM_ANDROID7 = 307
PLATFORM_ANDROID8 = 308
PLATFORM_ANDROID9 = 309
PLATFORM_ANDROID10 = 310
PLATFORM_ANDROID11 = 311
PLATFORM_ANDROID12 = 312
PLATFORM_ANDROID13 = 313
PLATFORM_ANDROID14 = 314
PLATFORM_RUSSIA = SOURCE_RUSSIA
PLATFORM_ROKU = (
    SOURCE_CCADB  # https://github.com/rokudev/ca-certificate/blob/master/ca-bundle.crt
)
BROWSER_FIREFOX = SOURCE_CCADB
BROWSER_TOR_BROWSER = SOURCE_CCADB
BROWSER_CHROMIUM = SOURCE_CCADB
BROWSER_GOOGLE_CHROME = SOURCE_CCADB
BROWSER_MICROSOFT_EDGE = SOURCE_CCADB
BROWSER_BRAVE = SOURCE_CCADB
BROWSER_OPERA = SOURCE_CCADB
BROWSER_VIVALDI = SOURCE_CCADB
BROWSER_AMAZON_SILK = SOURCE_CCADB
BROWSER_SAMSUNG_INTERNET_BROWSER = SOURCE_CCADB
BROWSER_YANDEX_BROWSER = SOURCE_RUSSIA
BROWSER_SAFARI = SOURCE_CCADB
LANGUAGE_PYTHON_WINDOWS_SERVER = PLATFORM_WINDOWS
LANGUAGE_PYTHON_LINUX_SERVER = SOURCE_CCADB
LANGUAGE_PYTHON_MACOS_SERVER = PLATFORM_APPLE
LANGUAGE_PYTHON_CERTIFI = SOURCE_CERTIFI
LANGUAGE_PYTHON_URLLIB = LANGUAGE_PYTHON_CERTIFI
LANGUAGE_PYTHON_REQUESTS = LANGUAGE_PYTHON_URLLIB
LANGUAGE_PYTHON_DJANGO = LANGUAGE_PYTHON_URLLIB
LANGUAGE_GO_WINDOWS_SERVER = PLATFORM_WINDOWS
LANGUAGE_GO_LINUX_SERVER = SOURCE_CCADB
LANGUAGE_GO_MACOS_SERVER = PLATFORM_APPLE
LANGUAGE_GO_CERTIFI = SOURCE_CERTIFI
LANGUAGE_ERLANG_WINDOWS_SERVER = PLATFORM_WINDOWS
LANGUAGE_ERLANG_LINUX_SERVER = SOURCE_CCADB
LANGUAGE_ERLANG_MACOS_SERVER = PLATFORM_APPLE
LANGUAGE_ERLANG_CERTIFI = SOURCE_CERTIFI
LANGUAGE_RUBY_WINDOWS_SERVER = PLATFORM_WINDOWS
LANGUAGE_RUBY_LINUX_SERVER = SOURCE_CCADB
LANGUAGE_RUBY_MACOS_SERVER = PLATFORM_APPLE
LANGUAGE_RUBY_CERTIFI = SOURCE_CERTIFI
LANGUAGE_NODE_WINDOWS_SERVER = PLATFORM_WINDOWS
LANGUAGE_NODE_LINUX_SERVER = SOURCE_CCADB
LANGUAGE_NODE_MACOS_SERVER = PLATFORM_APPLE
LANGUAGE_NODE_CERTIFI = SOURCE_CERTIFI
LANGUAGE_RUST_WINDOWS_SERVER = PLATFORM_WINDOWS
LANGUAGE_RUST_LINUX_SERVER = SOURCE_CCADB
LANGUAGE_RUST_MACOS_SERVER = PLATFORM_APPLE
LANGUAGE_RUST_RUSTLS = SOURCE_RUSTLS
LANGUAGE_RUST_WEBPKI = SOURCE_RUSTLS
LANGUAGE_ELIXIR_WINDOWS_SERVER = PLATFORM_WINDOWS
LANGUAGE_ELIXIR_LINUX_SERVER = SOURCE_CCADB
LANGUAGE_ELIXIR_MACOS_SERVER = PLATFORM_APPLE
LANGUAGE_ELIXIR_MINT = SOURCE_CURL
LANGUAGE_ELIXIR_PHOENIX_WINDOWS_SERVER = LANGUAGE_ELIXIR_WINDOWS_SERVER
LANGUAGE_ELIXIR_PHOENIX_LINUX_SERVER = LANGUAGE_ELIXIR_LINUX_SERVER
LANGUAGE_ELIXIR_PHOENIX_MACOS_SERVER = LANGUAGE_ELIXIR_MACOS_SERVER
LANGUAGE_CURL = SOURCE_CURL
LANGUAGE_DART = SOURCE_DART
JAVA_SRE = "Java(TM) SE Runtime Environment"
CCADB = "Common Certificate Authority Database (CCADB)"
RUSTLS = "Rustls (curated CCADB)"
GOOGLE_TRUST_SERVICES = "Google Trust Services"
ANDROID = "Android (open source)"
ANDROID_LATEST = "Android (latest Google build)"
ANDROID_FROYO = "Android 2.2 (Froyo) 2010"
ANDROID_GINGERBREAD = "Android 2.3 (Gingerbread) 2010"
ANDROID_HONEYCOMB = "Android 3 (Honeycomb) 2011"
ANDROID_ICE_CREAM_SANDWICH = "Android 4 (Ice Cream Sandwich) 2011"
ANDROID_KITKAT = "Android 4.4 (KitKat) 2013"
ANDROID_NOUGAT = "Android 7 (Nougat) 2016"
ANDROID_OREO = "Android 8 (Oreo) 2017"
ANDROID_PIE = "Android 9 (Pie) 2018"
ANDROID_QUINCE_TART = "Android 10 (Quince Tart) 2019"
ANDROID_RED_VELVET_CAKE = "Android 11 (Red Velvet Cake) 2020"
ANDROID_SNOW_CONE = "Android 12 (Snow Cone) 2021"
ANDROID_TIRAMISU = "Android 13 (Tiramisu) 2022"
ANDROID_UPSIDE_DOWN_CAKE = "Android 14 (Upside Down Cake) 2023"
CURL = "libcurl"
DART = "Dart Native"
LINUX_ARCH = "Linux (Arch)"
LINUX_FEDORA = "Linux (Fedora)"
LINUX_DEBIAN = "Linux (Debian)"
LINUX_UBUNTU = "Linux (Ubuntu)"
LINUX_ALPINE = "Linux (Apline)"
LINUX_CENTOS = "Linux (Centos)"
LINUX_RHEL = "Linux (RHEL)"
OPENBSD = "OpenBSD"
FREEBSD = "FreeBSD"
ROKU = "Roku"
MINTSIFRY_ROSSII = "MinTsifry Rossii"
PYTHON_CERTIFI = "Certifi (Python module for CA Certificates)"
PYTHON = "Python 3.10"
WINDOWS = "Microsoft Windows"
APPLE = "Apple devices"
FIREFOX = "Mozilla Firefox"
TOR = "Tor Web Browser"
CHROMIUM = "Chromium Browser"
CHROME = "Google Chrome"
EDGE = "Microsoft Edge"
BRAVE = "Brave Browser"
OPERA = "Opera Browser"
VIVALDI = "Vivaldi Browser"
SILK = "Amazon Silk"
SAMSUNG = "Samsung Internet"
YANDEX = "Yandex"
SAFARI = "Apple Safari"
PY_WINDOWS = "Python built-in https module on Windows"
PY_LINUX = "Python built-in https module on Linux"
PY_APPLE = "Python built-in https module on Apple"
PY_CERTIFI = "certifi (Python module)"
PY_URLLIB = "urllib (Python module)"
PY_REQUESTS = "requests (Python module)"
PY_DJANGO = "Django (Python module)"
GO_WINDOWS = "Go built-in https module on Windows"
GO_LINUX = "Go built-in https module on Linux"
GO_APPLE = "Go built-in https module on Apple"
GO_CERTIFI = "gocertifi (Go module)"
ERLANG_WINDOWS = "Erlang built-in https module on Windows"
ERLANG_LINUX = "Erlang built-in https module on Linux"
ERLANG_APPLE = "Erlang built-in https module on Apple"
ERLANG_CERTIFI = "certifi (Erlang library)"
RUBY_WINDOWS = "Ruby built-in https module on Windows"
RUBY_LINUX = "Ruby built-in https module on Linux"
RUBY_APPLE = "Ruby built-in https module on Apple"
RUBY_CERTIFI = "certifi (Ruby gem)"
NODE_WINDOWS = "Node.js built-in https module on Windows"
NODE_LINUX = "Node.js built-in https module on Linux"
NODE_APPLE = "Node.js built-in https module on Apple"
NODE_CERTIFI = "certifi (Node.js package)"
RUST_WINDOWS = "Rust using Rustls crate on Windows"
RUST_LINUX = "Rust using Rustls crate on Linux"
RUST_APPLE = "Rust using Rustls crate on Apple"
RUST_RUSTLS = "Rustls (Rust crate) using webpki-roots"
RUST_WEBPKI = "webpki (Rust crate)"
CURL_WINDOWS = "libcurl on Windows"
CURL_LINUX = "libcurl on Linux"
CURL_APPLE = "libcurl on Apple"
ELIXIR_WINDOWS = "Elixir on Windows"
ELIXIR_LINUX = "Elixir on Linux"
ELIXIR_APPLE = "Elixir on Apple"
ELIXIR_MINT = "Mint (elixir package)"
ELIXIR_PHOENIX_WINDOWS = "Phoenix (elixir package) on Windows"
ELIXIR_PHOENIX_LINUX = "Phoenix (elixir package) on Linux"
ELIXIR_PHOENIX_MACOS = "Phoenix (elixir package) on Apple"

SHORT_LOOKUP = {
    JAVA_SRE: "Java SE",
    CCADB: "CCADB",
    RUSTLS: "Rust",
    CURL: "libcurl",
    DART: "Dart",
    GOOGLE_TRUST_SERVICES: "Google",
    ANDROID: "Android FOSS",
    ANDROID_LATEST: "Android latest",
    ANDROID_FROYO: "Android 2.2",
    ANDROID_GINGERBREAD: "Android 2.3",
    ANDROID_HONEYCOMB: "Android 3",
    ANDROID_ICE_CREAM_SANDWICH: "Android 4",
    ANDROID_KITKAT: "Android 4.4",
    ANDROID_NOUGAT: "Android 7",
    ANDROID_OREO: "Android 8",
    ANDROID_PIE: "Android 9",
    ANDROID_QUINCE_TART: "Android 10",
    ANDROID_RED_VELVET_CAKE: "Android 11",
    ANDROID_SNOW_CONE: "Android 12",
    ANDROID_TIRAMISU: "Android 13",
    ANDROID_UPSIDE_DOWN_CAKE: "Android 14",
    LINUX_ARCH: "Arch Linux",
    LINUX_FEDORA: "Fedora",
    LINUX_DEBIAN: "Debian",
    LINUX_UBUNTU: "Ubuntu",
    LINUX_ALPINE: "Alpine",
    LINUX_CENTOS: "Centos",
    LINUX_RHEL: "RHEL",
    OPENBSD: "OpenBSD",
    FREEBSD: "FreeBSD",
    MINTSIFRY_ROSSII: "Russian",
    ROKU: "Roku",
    PYTHON_CERTIFI: "Certifi",
    WINDOWS: "Windows",
    APPLE: "Apple",
    FIREFOX: "Firefox",
    TOR: "Tor",
    CHROMIUM: "Chromium",
    CHROME: "Chrome",
    EDGE: "Edge",
    BRAVE: "Brave",
    OPERA: "Opera",
    VIVALDI: "Vivaldi",
    SILK: "Silk",
    SAMSUNG: "Samsung",
    YANDEX: "Yandex",
    SAFARI: "Safari",
    PY_WINDOWS: "Python on Windows",
    PY_LINUX: "Python on Linux",
    PY_APPLE: "Python on Apple",
    PY_CERTIFI: "certifi",
    PY_URLLIB: "urllib",
    PY_REQUESTS: "requests",
    PY_DJANGO: "Django",
    ERLANG_WINDOWS: "Erlang on Windows",
    ERLANG_LINUX: "Erlang on Linux",
    ERLANG_APPLE: "Erlang on Apple",
    ERLANG_CERTIFI: "erlang-certifi",
    GO_WINDOWS: "Go on Windows",
    GO_LINUX: "Go on Linux",
    GO_APPLE: "Go on Apple",
    GO_CERTIFI: "gocertifi",
    RUBY_WINDOWS: "Ruby on Windows",
    RUBY_LINUX: "Ruby on Linux",
    RUBY_APPLE: "Ruby on Apple",
    RUBY_CERTIFI: "ruby-certifi",
    NODE_WINDOWS: "Node.js on Windows",
    NODE_LINUX: "Node.js on Linux",
    NODE_APPLE: "Node.js on Apple",
    NODE_CERTIFI: "node-certifi",
    RUST_WINDOWS: "Rust on Windows",
    RUST_LINUX: "Rust on Linux",
    RUST_APPLE: "Rust on Apple",
    RUST_RUSTLS: "Rustls crate",
    RUST_WEBPKI: "Web PKI crate",
    CURL_WINDOWS: "libcurl on Windows",
    CURL_LINUX: "libcurl on Linux",
    CURL_APPLE: "libcurl on Apple",
    ELIXIR_MINT: "elixir-mint",
    ELIXIR_WINDOWS: "Elixir on Windows",
    ELIXIR_LINUX: "Elixir on Linux",
    ELIXIR_APPLE: "Elixir on Apple",
    ELIXIR_PHOENIX_WINDOWS: "Elixir Phoenix on Windows",
    ELIXIR_PHOENIX_LINUX: "Elixir Phoenix on Linux",
    ELIXIR_PHOENIX_MACOS: "Elixir Phoenix on Apple",
}
SOURCES = {
    CCADB: SOURCE_CCADB,
    RUSTLS: SOURCE_RUSTLS,
    JAVA_SRE: SOURCE_JAVA,
    GOOGLE_TRUST_SERVICES: SOURCE_ANDROID,
    PY_CERTIFI: SOURCE_CERTIFI,
    MINTSIFRY_ROSSII: SOURCE_RUSSIA,
    CURL: SOURCE_CURL,
}
STORES = {
    JAVA_SRE: SOURCE_JAVA,
    CCADB: SOURCE_CCADB,
    RUSTLS: SOURCE_RUSTLS,
    GOOGLE_TRUST_SERVICES: SOURCE_ANDROID,
    ANDROID_FROYO: PLATFORM_ANDROID2_2,
    ANDROID_GINGERBREAD: PLATFORM_ANDROID2_3,
    ANDROID_HONEYCOMB: PLATFORM_ANDROID3,
    ANDROID_ICE_CREAM_SANDWICH: PLATFORM_ANDROID4,
    ANDROID_KITKAT: PLATFORM_ANDROID4_4,
    ANDROID_NOUGAT: PLATFORM_ANDROID7,
    ANDROID_OREO: PLATFORM_ANDROID8,
    ANDROID_PIE: PLATFORM_ANDROID9,
    ANDROID_QUINCE_TART: PLATFORM_ANDROID10,
    ANDROID_RED_VELVET_CAKE: PLATFORM_ANDROID11,
    ANDROID_SNOW_CONE: PLATFORM_ANDROID12,
    ANDROID_TIRAMISU: PLATFORM_ANDROID13,
    ANDROID_UPSIDE_DOWN_CAKE: PLATFORM_ANDROID14,
    PY_CERTIFI: SOURCE_CERTIFI,
    MINTSIFRY_ROSSII: SOURCE_RUSSIA,
    CURL: SOURCE_CURL,
    DART: SOURCE_DART,
}
PLATFORMS = {
    JAVA_SRE: PLATFORM_JAVA,
    WINDOWS: PLATFORM_WINDOWS,
    APPLE: PLATFORM_APPLE,
    LINUX_ARCH: PLATFORM_ARCH_LINUX,
    LINUX_FEDORA: PLATFORM_FEDORA_LINUX,
    LINUX_DEBIAN: PLATFORM_DEBIAN_LINUX,
    LINUX_UBUNTU: PLATFORM_UBUNTU_LINUX,
    LINUX_ALPINE: PLATFORM_ALPINE_LINUX,
    LINUX_CENTOS: PLATFORM_CENTOS_LINUX,
    LINUX_RHEL: PLATFORM_RHEL_LINUX,
    OPENBSD: PLATFORM_OPENBSD,
    FREEBSD: PLATFORM_FREEBSD,
    ANDROID: PLATFORM_ANDROID,
    ANDROID_LATEST: PLATFORM_ANDROID_LATEST,
    ANDROID_FROYO: PLATFORM_ANDROID2_2,
    ANDROID_GINGERBREAD: PLATFORM_ANDROID2_3,
    ANDROID_HONEYCOMB: PLATFORM_ANDROID3,
    ANDROID_ICE_CREAM_SANDWICH: PLATFORM_ANDROID4,
    ANDROID_KITKAT: PLATFORM_ANDROID4_4,
    ANDROID_NOUGAT: PLATFORM_ANDROID7,
    ANDROID_OREO: PLATFORM_ANDROID8,
    ANDROID_PIE: PLATFORM_ANDROID9,
    ANDROID_QUINCE_TART: PLATFORM_ANDROID10,
    ANDROID_RED_VELVET_CAKE: PLATFORM_ANDROID11,
    ANDROID_SNOW_CONE: PLATFORM_ANDROID12,
    ANDROID_TIRAMISU: PLATFORM_ANDROID13,
    ANDROID_UPSIDE_DOWN_CAKE: PLATFORM_ANDROID14,
    MINTSIFRY_ROSSII: PLATFORM_RUSSIA,
    ROKU: PLATFORM_ROKU,
}
BROWSERS = {
    FIREFOX: BROWSER_FIREFOX,
    TOR: BROWSER_TOR_BROWSER,
    CHROMIUM: BROWSER_CHROMIUM,
    CHROME: BROWSER_GOOGLE_CHROME,
    EDGE: BROWSER_MICROSOFT_EDGE,
    BRAVE: BROWSER_BRAVE,
    OPERA: BROWSER_OPERA,
    VIVALDI: BROWSER_VIVALDI,
    SILK: BROWSER_AMAZON_SILK,
    SAMSUNG: BROWSER_SAMSUNG_INTERNET_BROWSER,
    YANDEX: BROWSER_YANDEX_BROWSER,
    SAFARI: BROWSER_SAFARI,
}
LANGUAGES = {
    PY_WINDOWS: LANGUAGE_PYTHON_WINDOWS_SERVER,
    PY_LINUX: LANGUAGE_PYTHON_LINUX_SERVER,
    PY_APPLE: LANGUAGE_PYTHON_MACOS_SERVER,
    PY_CERTIFI: LANGUAGE_PYTHON_CERTIFI,
    PY_URLLIB: LANGUAGE_PYTHON_URLLIB,
    PY_REQUESTS: LANGUAGE_PYTHON_REQUESTS,
    PY_DJANGO: LANGUAGE_PYTHON_DJANGO,
    GO_WINDOWS: LANGUAGE_GO_WINDOWS_SERVER,
    GO_LINUX: LANGUAGE_GO_LINUX_SERVER,
    GO_APPLE: LANGUAGE_GO_MACOS_SERVER,
    GO_CERTIFI: LANGUAGE_GO_CERTIFI,
    ERLANG_WINDOWS: LANGUAGE_ERLANG_WINDOWS_SERVER,
    ERLANG_LINUX: LANGUAGE_ERLANG_LINUX_SERVER,
    ERLANG_APPLE: LANGUAGE_ERLANG_MACOS_SERVER,
    ERLANG_CERTIFI: LANGUAGE_ERLANG_CERTIFI,
    RUBY_WINDOWS: LANGUAGE_RUBY_WINDOWS_SERVER,
    RUBY_LINUX: LANGUAGE_RUBY_LINUX_SERVER,
    RUBY_APPLE: LANGUAGE_RUBY_MACOS_SERVER,
    RUBY_CERTIFI: LANGUAGE_RUBY_CERTIFI,
    NODE_WINDOWS: LANGUAGE_NODE_WINDOWS_SERVER,
    NODE_LINUX: LANGUAGE_NODE_LINUX_SERVER,
    NODE_APPLE: LANGUAGE_NODE_MACOS_SERVER,
    NODE_CERTIFI: LANGUAGE_NODE_CERTIFI,
    RUST_WINDOWS: LANGUAGE_RUST_WINDOWS_SERVER,
    RUST_LINUX: LANGUAGE_RUST_LINUX_SERVER,
    RUST_APPLE: LANGUAGE_RUST_MACOS_SERVER,
    RUST_RUSTLS: LANGUAGE_RUST_RUSTLS,
    RUST_WEBPKI: LANGUAGE_RUST_WEBPKI,
    CURL_WINDOWS: LANGUAGE_CURL,
    CURL_LINUX: LANGUAGE_CURL,
    CURL_APPLE: LANGUAGE_CURL,
    ELIXIR_WINDOWS: LANGUAGE_ELIXIR_WINDOWS_SERVER,
    ELIXIR_LINUX: LANGUAGE_ELIXIR_LINUX_SERVER,
    ELIXIR_APPLE: LANGUAGE_ELIXIR_MACOS_SERVER,
    ELIXIR_MINT: LANGUAGE_ELIXIR_MINT,
    ELIXIR_PHOENIX_WINDOWS: LANGUAGE_ELIXIR_PHOENIX_WINDOWS_SERVER,
    ELIXIR_PHOENIX_LINUX: LANGUAGE_ELIXIR_PHOENIX_LINUX_SERVER,
    ELIXIR_PHOENIX_MACOS: LANGUAGE_ELIXIR_PHOENIX_MACOS_SERVER,
    DART: LANGUAGE_DART,
}
ALL_DISTINCT = {**STORES, **PLATFORMS, **LANGUAGES, **BROWSERS, **SOURCES}
