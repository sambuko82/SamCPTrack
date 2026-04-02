#!/usr/bin/python
# << CODE BY HUNX04
# << MAU RECODE ??? IZIN DULU LAH,  MINIMAL TAG AKUN GITHUB MIMIN YANG MENGARAH KE AKUN INI, LEBIH GAMPANG SI PAKE FORK
# << KALAU DI ATAS TIDAK DI IKUTI MAKA AKAN MENDAPATKAN DOSA KARENA MIMIN GAK IKHLAS
# “Wahai orang-orang yang beriman! Janganlah kamu saling memakan harta sesamamu dengan jalan yang batil,” (QS. An Nisaa': 29). Rasulullah SAW juga melarang umatnya untuk mengambil hak orang lain tanpa izin.

# IMPORT MODULE

import json
import requests
import time
import os
import phonenumbers
from phonenumbers import carrier, geocoder, timezone
from sys import stderr

Bl = '\033[30m'  # VARIABLE BUAT WARNA CUYY
Re = '\033[1;31m'
Gr = '\033[1;32m'
Ye = '\033[1;33m'
Blu = '\033[1;34m'
Mage = '\033[1;35m'
Cy = '\033[1;36m'
Wh = '\033[1;37m'


# utilities

# decorator for attaching run_banner to a function
def is_option(func):
    def wrapper(*args, **kwargs):
        run_banner()
        return func(*args, **kwargs)

    return wrapper


# FUNCTIONS FOR MENU
@is_option
def IP_Track():
    ip = input(f"{Wh}\n Enter IP target : {Gr}")  # INPUT IP ADDRESS
    if not ip.strip():
        print(f"{Re}\n [!] IP address cannot be empty!")
        return
    print()
    print(f' {Wh}============= {Gr}SHOW INFORMATION IP ADDRESS {Wh}=============')
    try:
        req_api = requests.get(f"http://ipwho.is/{ip}", timeout=15)  # API IPWHOIS.IS
        req_api.raise_for_status()
        ip_data = req_api.json()
    except requests.exceptions.Timeout:
        print(f"{Re}\n [!] Request timed out. Check your internet connection.")
        return
    except requests.exceptions.RequestException as e:
        print(f"{Re}\n [!] Network error: {e}")
        return
    if not ip_data.get("success", True):
        print(f"{Re}\n [!] Invalid IP address or API error: {ip_data.get('message', 'Unknown error')}")
        return
    time.sleep(1)
    lat = ip_data.get('latitude', 0)
    lon = ip_data.get('longitude', 0)
    print(f"{Wh}\n IP target       :{Gr}", ip)
    print(f"{Wh} Type IP         :{Gr}", ip_data.get("type", "-"))
    print(f"{Wh} Country         :{Gr}", ip_data.get("country", "-"))
    print(f"{Wh} Country Code    :{Gr}", ip_data.get("country_code", "-"))
    print(f"{Wh} City            :{Gr}", ip_data.get("city", "-"))
    print(f"{Wh} Continent       :{Gr}", ip_data.get("continent", "-"))
    print(f"{Wh} Continent Code  :{Gr}", ip_data.get("continent_code", "-"))
    print(f"{Wh} Region          :{Gr}", ip_data.get("region", "-"))
    print(f"{Wh} Region Code     :{Gr}", ip_data.get("region_code", "-"))
    print(f"{Wh} Latitude        :{Gr}", lat)
    print(f"{Wh} Longitude       :{Gr}", lon)
    print(f"{Wh} Maps            :{Gr}", f"https://www.google.com/maps/@{lat},{lon},8z")
    print(f"{Wh} EU              :{Gr}", ip_data.get("is_eu", "-"))
    print(f"{Wh} Postal          :{Gr}", ip_data.get("postal", "-"))
    print(f"{Wh} Calling Code    :{Gr}", ip_data.get("calling_code", "-"))
    print(f"{Wh} Capital         :{Gr}", ip_data.get("capital", "-"))
    print(f"{Wh} Borders         :{Gr}", ip_data.get("borders", "-"))
    flag = ip_data.get("flag", {})
    print(f"{Wh} Country Flag    :{Gr}", flag.get("emoji", "-"))
    connection = ip_data.get("connection", {})
    print(f"{Wh} ASN             :{Gr}", connection.get("asn", "-"))
    print(f"{Wh} ORG             :{Gr}", connection.get("org", "-"))
    print(f"{Wh} ISP             :{Gr}", connection.get("isp", "-"))
    print(f"{Wh} Domain          :{Gr}", connection.get("domain", "-"))
    tz = ip_data.get("timezone", {})
    print(f"{Wh} ID              :{Gr}", tz.get("id", "-"))
    print(f"{Wh} ABBR            :{Gr}", tz.get("abbr", "-"))
    print(f"{Wh} DST             :{Gr}", tz.get("is_dst", "-"))
    print(f"{Wh} Offset          :{Gr}", tz.get("offset", "-"))
    print(f"{Wh} UTC             :{Gr}", tz.get("utc", "-"))
    print(f"{Wh} Current Time    :{Gr}", tz.get("current_time", "-"))


@is_option
def phoneGW():
    User_phone = input(
        f"\n {Wh}Enter phone number target {Gr}Ex [+6281xxxxxxxxx] {Wh}: {Gr}")  # INPUT NUMBER PHONE
    if not User_phone.strip():
        print(f"{Re}\n [!] Phone number cannot be empty!")
        return
    default_region = "ID"  # DEFAULT NEGARA INDONESIA

    try:
        parsed_number = phonenumbers.parse(User_phone, default_region)  # VARIABLE PHONENUMBERS
    except phonenumbers.NumberParseException as e:
        print(f"{Re}\n [!] Invalid phone number format: {e}")
        return
    region_code = phonenumbers.region_code_for_number(parsed_number)
    jenis_provider = carrier.name_for_number(parsed_number, "en")
    location = geocoder.description_for_number(parsed_number, "id")
    is_valid_number = phonenumbers.is_valid_number(parsed_number)
    is_possible_number = phonenumbers.is_possible_number(parsed_number)
    formatted_number = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
    formatted_number_for_mobile = phonenumbers.format_number_for_mobile_dialing(parsed_number, default_region,
                                                                                with_formatting=True)
    number_type = phonenumbers.number_type(parsed_number)
    timezone1 = timezone.time_zones_for_number(parsed_number)
    timezoneF = ', '.join(timezone1)

    print(f"\n {Wh}========== {Gr}SHOW INFORMATION PHONE NUMBERS {Wh}==========")
    print(f"\n {Wh}Location             :{Gr} {location}")
    print(f" {Wh}Region Code          :{Gr} {region_code}")
    print(f" {Wh}Timezone             :{Gr} {timezoneF}")
    print(f" {Wh}Operator             :{Gr} {jenis_provider}")
    print(f" {Wh}Valid number         :{Gr} {is_valid_number}")
    print(f" {Wh}Possible number      :{Gr} {is_possible_number}")
    print(f" {Wh}International format :{Gr} {formatted_number}")
    print(f" {Wh}Mobile format        :{Gr} {formatted_number_for_mobile}")
    print(f" {Wh}Original number      :{Gr} {parsed_number.national_number}")
    print(
        f" {Wh}E.164 format         :{Gr} {phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.E164)}")
    print(f" {Wh}Country code         :{Gr} {parsed_number.country_code}")
    print(f" {Wh}Local number         :{Gr} {parsed_number.national_number}")
    if number_type == phonenumbers.PhoneNumberType.MOBILE:
        print(f" {Wh}Type                 :{Gr} This is a mobile number")
    elif number_type == phonenumbers.PhoneNumberType.FIXED_LINE:
        print(f" {Wh}Type                 :{Gr} This is a fixed-line number")
    else:
        print(f" {Wh}Type                 :{Gr} This is another type of number")


@is_option
def TrackLu():
    username = input(f"\n {Wh}Enter Username : {Gr}")
    if not username.strip():
        print(f"{Re}\n [!] Username cannot be empty!")
        return
    results = {}
    social_media = [
        {"url": "https://www.facebook.com/{}", "name": "Facebook"},
        {"url": "https://www.twitter.com/{}", "name": "Twitter"},
        {"url": "https://www.instagram.com/{}", "name": "Instagram"},
        {"url": "https://www.linkedin.com/in/{}", "name": "LinkedIn"},
        {"url": "https://www.github.com/{}", "name": "GitHub"},
        {"url": "https://www.pinterest.com/{}", "name": "Pinterest"},
        {"url": "https://www.tumblr.com/{}", "name": "Tumblr"},
        {"url": "https://www.youtube.com/{}", "name": "Youtube"},
        {"url": "https://soundcloud.com/{}", "name": "SoundCloud"},
        {"url": "https://www.snapchat.com/add/{}", "name": "Snapchat"},
        {"url": "https://www.tiktok.com/@{}", "name": "TikTok"},
        {"url": "https://www.behance.net/{}", "name": "Behance"},
        {"url": "https://www.medium.com/@{}", "name": "Medium"},
        {"url": "https://www.quora.com/profile/{}", "name": "Quora"},
        {"url": "https://www.flickr.com/people/{}", "name": "Flickr"},
        {"url": "https://www.twitch.tv/{}", "name": "Twitch"},
        {"url": "https://www.dribbble.com/{}", "name": "Dribbble"},
        {"url": "https://www.ello.co/{}", "name": "Ello"},
        {"url": "https://www.producthunt.com/@{}", "name": "Product Hunt"},
        {"url": "https://www.telegram.me/{}", "name": "Telegram"},
        {"url": "https://www.weheartit.com/{}", "name": "We Heart It"}
    ]
    print(f"\n {Wh}Checking {Gr}{len(social_media)}{Wh} platforms, please wait...")
    for site in social_media:
        url = site['url'].format(username)
        try:
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                results[site['name']] = url
            elif response.status_code == 404:
                results[site['name']] = f"{Ye}Not found{Wh}"
            else:
                results[site['name']] = f"{Ye}Status {response.status_code}{Wh}"
        except requests.exceptions.Timeout:
            results[site['name']] = f"{Re}Timeout{Wh}"
        except requests.exceptions.RequestException:
            results[site['name']] = f"{Re}Error checking{Wh}"

    print(f"\n {Wh}========== {Gr}SHOW INFORMATION USERNAME {Wh}==========")
    print()
    for site, url in results.items():
        print(f" {Wh}[ {Gr}+ {Wh}] {site} : {Gr}{url}")


@is_option
def showIP():
    try:
        response = requests.get('https://api.ipify.org/', timeout=10)
        response.raise_for_status()
        show_ip = response.text
    except requests.exceptions.Timeout:
        print(f"{Re}\n [!] Request timed out. Check your internet connection.")
        return
    except requests.exceptions.RequestException as e:
        print(f"{Re}\n [!] Network error: {e}")
        return

    print(f"\n {Wh}========== {Gr}SHOW INFORMATION YOUR IP {Wh}==========")
    print(f"\n {Wh}[{Gr} + {Wh}] Your IP Address : {Gr}{show_ip}")
    print(f"\n {Wh}==============================================")


# OPTIONS
options = [
    {
        'num': 1,
        'text': 'IP Tracker',
        'func': IP_Track
    },
    {
        'num': 2,
        'text': 'Show Your IP',
        'func': showIP

    },
    {
        'num': 3,
        'text': 'Phone Number Tracker',
        'func': phoneGW
    },
    {
        'num': 4,
        'text': 'Username Tracker',
        'func': TrackLu
    },
    {
        'num': 0,
        'text': 'Exit',
        'func': exit
    }
]


def clear():
    # for windows
    if os.name == 'nt':
        _ = os.system('cls')
    # for mac and linux
    else:
        _ = os.system('clear')


def call_option(opt):
    if not is_in_options(opt):
        raise ValueError('Option not found')
    for option in options:
        if option['num'] == opt:
            if 'func' in option:
                option['func']()
            else:
                print('No function detected')


def execute_option(opt):
    while True:
        try:
            call_option(opt)
            input(f'\n{Wh}[ {Gr}+ {Wh}] {Gr}Press enter to continue')
            main()
            break
        except ValueError as e:
            print(e)
            time.sleep(2)
            break
        except KeyboardInterrupt:
            print(f'\n{Wh}[ {Re}! {Wh}] {Re}Exit')
            time.sleep(2)
            exit()


def option_text():
    text = ''
    for opt in options:
        text += f'{Wh}[ {opt["num"]} ] {Gr}{opt["text"]}\n'
    return text


def is_in_options(num):
    for opt in options:
        if opt['num'] == num:
            return True
    return False


def option():
    # BANNER TOOLS
    clear()
    stderr.writelines(f"""
       ________               __      ______                __  
      / ____/ /_  ____  _____/ /_    /_  __/________ ______/ /__
     / / __/ __ \/ __ \/ ___/ __/_____/ / / ___/ __ `/ ___/ //_/
    / /_/ / / / / /_/ (__  ) /_/_____/ / / /  / /_/ / /__/ ,<   
    \____/_/ /_/\____/____/\__/     /_/ /_/   \__,_/\___/_/|_| 

              {Wh}[ + ]  C O D E   B Y  H U N X  [ + ]
    """)

    stderr.writelines(f"\n\n\n{option_text()}")


def run_banner():
    clear()
    time.sleep(1)
    stderr.writelines(f"""{Wh}
         .-.
       .'   `.          {Wh}--------------------------------
       :g g   :         {Wh}| {Gr}GHOST - TRACKER - IP ADDRESS {Wh}|
       : o    `.        {Wh}|       {Gr}@CODE BY HUNXBYTS      {Wh}|
      :         ``.     {Wh}--------------------------------
     :             `.
    :  :         .   `.
    :   :          ` . `.
     `.. :            `. ``;
        `:;             `:'
           :              `.
            `.              `.     .
              `'`'`'`---..,___`;.-'
        """)
    time.sleep(0.5)


def main():
    clear()
    option()
    time.sleep(1)
    try:
        opt = int(input(f"{Wh}\n [ + ] {Gr}Select Option : {Wh}"))
        execute_option(opt)
    except ValueError:
        print(f'\n{Wh}[ {Re}! {Wh}] {Re}Please input number')
        time.sleep(2)
        main()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print(f'\n{Wh}[ {Re}! {Wh}] {Re}Exit')
        time.sleep(2)
        exit()
