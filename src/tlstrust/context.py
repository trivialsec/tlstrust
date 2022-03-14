__module__ = 'tlstrust.context'

INVALID_CONTEXT = 'context_type provided is invalid {}'
SOURCE_CCADB = 0
SOURCE_JAVA = 1
SOURCE_ANDROID = 3
SOURCE_LINUX = 4
SOURCE_CERTIFI = 101
SOURCE_RUSSIA = 201
PLATFORM_LINUX = SOURCE_LINUX
PLATFORM_JAVA = SOURCE_JAVA
PLATFORM_PYTHON = SOURCE_CERTIFI
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
PLATFORM_RUSSIA = SOURCE_RUSSIA
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
PYTHON_WINDOWS_SERVER = SOURCE_CCADB
PYTHON_LINUX_SERVER = SOURCE_LINUX
PYTHON_MACOS_SERVER = PLATFORM_APPLE
PYTHON_CERTIFI = SOURCE_CERTIFI
PYTHON_URLLIB = PYTHON_CERTIFI
PYTHON_REQUESTS = PYTHON_URLLIB
PYTHON_DJANGO = PYTHON_URLLIB
SOURCES = {
    'Common Certificate Authority Database (CCADB)': SOURCE_CCADB,
    'Java(TM) SE Runtime Environment': SOURCE_JAVA,
    'Google Trust Services': SOURCE_ANDROID,
    'Linux (Arch)': SOURCE_LINUX,
    'Certifi (Python module for Certificate Authority Certificates)': SOURCE_CERTIFI,
    'MinTsifry Rossii': SOURCE_RUSSIA,
}
PLATFORMS = {
    'Java(TM) SE Runtime Environment': PLATFORM_JAVA,
    'Python 3.10': PLATFORM_PYTHON,
    'Microsoft Windows': PLATFORM_WINDOWS,
    'Apple Devices': PLATFORM_APPLE,
    'Android': PLATFORM_ANDROID,
    'latest Android build': PLATFORM_ANDROID_LATEST,
    'Android 2.2 (Froyo) 2010': PLATFORM_ANDROID2_2,
    'Android 2.3 (Gingerbread) 2010': PLATFORM_ANDROID2_3,
    'Android 3 (Honeycomb) 2011': PLATFORM_ANDROID3,
    'Android 4 (Ice Cream Sandwich) 2011': PLATFORM_ANDROID4,
    'Android 4.4 (KitKat) 2013': PLATFORM_ANDROID4_4,
    'Android 7 (Nougat) 2016': PLATFORM_ANDROID7,
    'Android 8 (Oreo) 2017': PLATFORM_ANDROID8,
    'Android 9 (Pie) 2018': PLATFORM_ANDROID9,
    'Android 10 (Q) 2019': PLATFORM_ANDROID10,
    'Android 11 2020': PLATFORM_ANDROID11,
    'Android 12 2021': PLATFORM_ANDROID12,
    'MinTsifry Rossii': PLATFORM_RUSSIA,
}
BROWSERS = {
    'Mozilla Firefox': BROWSER_FIREFOX,
    'Tor Web Browser': BROWSER_TOR_BROWSER,
    'Chromium Browser': BROWSER_CHROMIUM,
    'Google Chrome': BROWSER_GOOGLE_CHROME,
    'Microsoft Edge': BROWSER_MICROSOFT_EDGE,
    'Brave Browser': BROWSER_BRAVE,
    'Opera Browser': BROWSER_OPERA,
    'Vivaldi Browser': BROWSER_VIVALDI,
    'Amazon Silk': BROWSER_AMAZON_SILK,
    'Samsung Internet': BROWSER_SAMSUNG_INTERNET_BROWSER,
    'Yandex': BROWSER_YANDEX_BROWSER,
    'Apple Safari': BROWSER_SAFARI,
}
LANGUAGES = {
    'Python built-in https module on Windows': PYTHON_WINDOWS_SERVER,
    'Python built-in https module on Linux': PYTHON_LINUX_SERVER,
    'Python built-in https module on Apple': PYTHON_MACOS_SERVER,
    'certifi (Python module)': PYTHON_CERTIFI,
    'urllib (Python module)': PYTHON_URLLIB,
    'requests (Python module)': PYTHON_REQUESTS,
    'Django (Python module)': PYTHON_DJANGO,
}
