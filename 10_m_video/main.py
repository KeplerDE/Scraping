import requests
import json


def get_data():

    cookies = {
        '__lhash_': 'c3b0a5b045904aaf165ae5bacae7d91a',
        'MVID_AB_PDP_CHAR': '2',
        'MVID_AB_SERVICES_DESCRIPTION': 'var4',
        'MVID_ACTOR_API_AVAILABILITY': 'true',
        'MVID_BLACK_FRIDAY_ENABLED': 'true',
        'MVID_CART_AVAILABILITY': 'true',
        'MVID_CATALOG_STATE': '1',
        'MVID_CITY_ID': 'CityCZ_975',
        'MVID_CREDIT_AVAILABILITY': 'true',
        'MVID_CRITICAL_GTM_INIT_DELAY': '3000',
        'MVID_FILTER_CODES': 'true',
        'MVID_FILTER_TOOLTIP': '1',
        'MVID_FLOCKTORY_ON': 'true',
        'MVID_GEOLOCATION_NEEDED': 'true',
        'MVID_GIFT_KIT': 'true',
        'MVID_GLC': 'true',
        'MVID_GLP': 'true',
        'MVID_GTM_ENABLED': '011',
        'MVID_IMG_RESIZE': 'true',
        'MVID_INIT_DATA_OFF': 'true',
        'MVID_IS_NEW_BR_WIDGET': 'true',
        'MVID_KLADR_ID': '7700000000000',
        'MVID_LAYOUT_TYPE': '1',
        'MVID_LP_HANDOVER': '0',
        'MVID_LP_SOLD_VARIANTS': '3',
        'MVID_MCLICK': 'true',
        'MVID_MINDBOX_DYNAMICALLY': 'true',
        'MVID_MINI_PDP': 'true',
        'MVID_MOBILE_FILTERS': 'true',
        'MVID_MULTIOFFER': 'true',
        'MVID_NEW_ACCESSORY': 'true',
        'MVID_NEW_DESKTOP_FILTERS': 'true',
        'MVID_NEW_LK_CHECK_CAPTCHA': 'true',
        'MVID_NEW_LK_OTP_TIMER': 'true',
        'MVID_NEW_MBONUS_BLOCK': 'true',
        'MVID_PROMO_CATALOG_ON': 'true',
        'MVID_REGION_ID': '1',
        'MVID_REGION_SHOP': 'S002',
        'MVID_SERVICES': '111',
        'MVID_SERVICES_MINI_BLOCK': 'var2',
        'MVID_TIMEZONE_OFFSET': '3',
        'MVID_WEBP_ENABLED': 'true',
        'MVID_WEB_SBP': 'true',
        'SENTRY_ERRORS_RATE': '0.1',
        'SENTRY_TRANSACTIONS_RATE': '0.5',
        '_ym_uid': '1671734305129492882',
        '_ym_d': '1671734305',
        'tmr_lvid': '99bf97b35958a096c748cf8045c41e67',
        'tmr_lvidTS': '1671734307510',
        'gdeslon.ru.__arc_domain': 'gdeslon.ru',
        'gdeslon.ru.user_id': '1021aef7-5875-45f7-b0ee-6959a369d02a',
        'flocktory-uuid': '7abf8f4e-4115-4f99-a326-bdcdd11db91a-7',
        'advcake_track_id': 'fe1cec6c-6ed6-30ef-5bb0-5c1ad931a0e9',
        'advcake_session_id': 'fb3ead64-0c32-333f-4f3e-9edc0d1a8168',
        'uxs_uid': 'd4ebc4f0-8227-11ed-9f9b-d30b4e001776',
        'afUserId': 'af50916b-24b6-45f0-b805-0bbb85f80438-p',
        'AF_SYNC': '1671734312756',
        'MVID_GUEST_ID': '22076151921',
        'MVID_VIEWED_PRODUCTS': '',
        'wurfl_device_id': 'generic_web_browser',
        'MVID_CALC_BONUS_RUBLES_PROFIT': 'true',
        'NEED_REQUIRE_APPLY_DISCOUNT': 'true',
        'MVID_CART_MULTI_DELETE': 'true',
        'PROMOLISTING_WITHOUT_STOCK_AB_TEST': '2',
        'MVID_GET_LOCATION_BY_DADATA': 'DaData',
        'PRESELECT_COURIER_DELIVERY_FOR_KBT': 'false',
        'HINTS_FIO_COOKIE_NAME': '1',
        'searchType2': '2',
        'COMPARISON_INDICATOR': 'false',
        'MVID_NEW_OLD': 'eyJjYXJ0IjpmYWxzZSwiZmF2b3JpdGUiOnRydWUsImNvbXBhcmlzb24iOnRydWV9',
        'MVID_OLD_NEW': 'eyJjb21wYXJpc29uIjogdHJ1ZSwgImZhdm9yaXRlIjogdHJ1ZSwgImNhcnQiOiB0cnVlfQ==',
        '__zzatgib-w-mvideo': 'MDA0dC0cTApcfEJcdGswPi17CT4VHThHKHIzd2UsWDZXIQocNmdzFRtnYClGG1t3KBArDGUTD2dcbFB2Tlk/ayAVQVssEzpxR2NCRipUDR4SGjhmIWNIYSBLVU1/FhoXfmwqUgsPXkNJc3kbN1ddHBEkWA4hPwtpW1Y0ZxUbQEgYL0tueTA8bCBjS1woSlpOdRdgSkMrNhZGRhxyM3c/awgiGVETKl94R1drZVVCODFnDE9PTRIW+Gt2iQ==',
        '__zzatgib-w-mvideo': 'MDA0dC0cTApcfEJcdGswPi17CT4VHThHKHIzd2UsWDZXIQocNmdzFRtnYClGG1t3KBArDGUTD2dcbFB2Tlk/ayAVQVssEzpxR2NCRipUDR4SGjhmIWNIYSBLVU1/FhoXfmwqUgsPXkNJc3kbN1ddHBEkWA4hPwtpW1Y0ZxUbQEgYL0tueTA8bCBjS1woSlpOdRdgSkMrNhZGRhxyM3c/awgiGVETKl94R1drZVVCODFnDE9PTRIW+Gt2iQ==',
        'cfidsgib-w-mvideo': 'oAkj+zpmSj5t0mhgAYh5bm5sU7buxGRs1ENR6Ynupdfit+gZeE9CCg+JBePSXZt6+gNoxfE/YEQYenuQzdmjO1wuykmuC/wKnleo4A04GwzT+ftPYnoMhNgHjle1/UcK6Grp/rtiC3Ns59Q0VVV3Fa2qCmvSbvV0u/a5',
        'cfidsgib-w-mvideo': 'oAkj+zpmSj5t0mhgAYh5bm5sU7buxGRs1ENR6Ynupdfit+gZeE9CCg+JBePSXZt6+gNoxfE/YEQYenuQzdmjO1wuykmuC/wKnleo4A04GwzT+ftPYnoMhNgHjle1/UcK6Grp/rtiC3Ns59Q0VVV3Fa2qCmvSbvV0u/a5',
        'gsscgib-w-mvideo': 'sc0grt9okBqdQELBvPHX8z43Hy2nDTURqmKho0jxlLR5lrZbHwhXyBTujl2vhl0tDHy7TqluE16hh1lBq4xcCX5QWCIX4wKML0dJvattrPAmcxjosXpeTbXthrH7kJ5IVziAN+ftBNwJ2SgG8I0BDoTytz1+YPzZsKqcAlOZd3Hh5v27m/htMOuMKzj5MyE0Ai7Jk+WAWuYekeTj7XLrPwzzSICtKZtGnPSFojM1tJRAyHWHoauiMPxKNL/qV+Tdlw==',
        'gsscgib-w-mvideo': 'sc0grt9okBqdQELBvPHX8z43Hy2nDTURqmKho0jxlLR5lrZbHwhXyBTujl2vhl0tDHy7TqluE16hh1lBq4xcCX5QWCIX4wKML0dJvattrPAmcxjosXpeTbXthrH7kJ5IVziAN+ftBNwJ2SgG8I0BDoTytz1+YPzZsKqcAlOZd3Hh5v27m/htMOuMKzj5MyE0Ai7Jk+WAWuYekeTj7XLrPwzzSICtKZtGnPSFojM1tJRAyHWHoauiMPxKNL/qV+Tdlw==',
        'deviceType': 'desktop',
        'fgsscgib-w-mvideo': 'SXpVa9435a97d6f27fafbe13b732f913767f4622',
        'fgsscgib-w-mvideo': 'SXpVa9435a97d6f27fafbe13b732f913767f4622',
        'cfidsgib-w-mvideo': 'cruo7CKbw/b6akwAyXFd2LcJAFOf56XBKYGmzWGU9PnIYRQHGMhYjJM3yi6f/hfeH6sz6BereWRTk8EznP/eNw1RVlirJo9DrYV6HOXLOe6M/jTtUDOd4MpB9V/bNlGhoCV2+Fz0KIMb6do8DSIdt+83f/fqQ1j0uNH+',
        '__js_p_': '630,3600,0,1,0',
        '__jhash_': '322',
        '__jua_': 'Mozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F108.0.0.0%20Safari%2F537.36',
        '__hash_': 'fd6530ff9fb7b60e0e21391833d9e242',
        'BIGipServericerock-prod': '3187989514.20480.0000',
        'bIPs': '-957002303',
        'mindboxDeviceUUID': 'a72558fa-6052-4e2a-aae3-b931b91d285c',
        'directCrm-session': '%7B%22deviceGuid%22%3A%22a72558fa-6052-4e2a-aae3-b931b91d285c%22%7D',
        'popmechanic_sbjs_migrations': 'popmechanic_1418474375998%3D1%7C%7C%7C1471519752600%3D1%7C%7C%7C1471519752605%3D1',
        '_sp_ses.d61c': '*',
        '_gid': 'GA1.2.269817027.1671871643',
        '_ym_isad': '2',
        '_ga': 'GA1.2.946872466.1671734305',
        'SMSError': '',
        'authError': '',
        'tmr_detect': '0%7C1671871648171',
        '_sp_id.d61c': 'c58c231c-4154-4760-a471-86eeeedbccf0.1671734305.2.1671871677.1671735236.49ffafd7-12f0-4e00-b9e9-137afdcaa044.0b5ed1d0-f002-4725-af0d-782d3c26cf52.47c0e322-67ce-40f1-ac00-dc6b76b6bfd2.1671871642389.25',
        '_ga_CFMZTSS5FM': 'GS1.1.1671871642.2.1.1671871697.0.0.0',
        '_ga_BNX5WPP3YK': 'GS1.1.1671871642.2.1.1671871697.5.0.0',
        'MVID_ENVCLOUD': 'prod2',
    }

    headers = {
        'authority': 'www.mvideo.ru',
        'accept': 'application/json',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'baggage': 'sentry-transaction=%2F,sentry-public_key=1e9efdeb57cf4127af3f903ec9db1466,sentry-trace_id=3e4cfb0079234bab8b02b5e22f1523e3,sentry-sample_rate=0.5',
        # 'cookie': '__lhash_=c3b0a5b045904aaf165ae5bacae7d91a; MVID_AB_PDP_CHAR=2; MVID_AB_SERVICES_DESCRIPTION=var4; MVID_ACTOR_API_AVAILABILITY=true; MVID_BLACK_FRIDAY_ENABLED=true; MVID_CART_AVAILABILITY=true; MVID_CATALOG_STATE=1; MVID_CITY_ID=CityCZ_975; MVID_CREDIT_AVAILABILITY=true; MVID_CRITICAL_GTM_INIT_DELAY=3000; MVID_FILTER_CODES=true; MVID_FILTER_TOOLTIP=1; MVID_FLOCKTORY_ON=true; MVID_GEOLOCATION_NEEDED=true; MVID_GIFT_KIT=true; MVID_GLC=true; MVID_GLP=true; MVID_GTM_ENABLED=011; MVID_IMG_RESIZE=true; MVID_INIT_DATA_OFF=true; MVID_IS_NEW_BR_WIDGET=true; MVID_KLADR_ID=7700000000000; MVID_LAYOUT_TYPE=1; MVID_LP_HANDOVER=0; MVID_LP_SOLD_VARIANTS=3; MVID_MCLICK=true; MVID_MINDBOX_DYNAMICALLY=true; MVID_MINI_PDP=true; MVID_MOBILE_FILTERS=true; MVID_MULTIOFFER=true; MVID_NEW_ACCESSORY=true; MVID_NEW_DESKTOP_FILTERS=true; MVID_NEW_LK_CHECK_CAPTCHA=true; MVID_NEW_LK_OTP_TIMER=true; MVID_NEW_MBONUS_BLOCK=true; MVID_PROMO_CATALOG_ON=true; MVID_REGION_ID=1; MVID_REGION_SHOP=S002; MVID_SERVICES=111; MVID_SERVICES_MINI_BLOCK=var2; MVID_TIMEZONE_OFFSET=3; MVID_WEBP_ENABLED=true; MVID_WEB_SBP=true; SENTRY_ERRORS_RATE=0.1; SENTRY_TRANSACTIONS_RATE=0.5; _ym_uid=1671734305129492882; _ym_d=1671734305; tmr_lvid=99bf97b35958a096c748cf8045c41e67; tmr_lvidTS=1671734307510; gdeslon.ru.__arc_domain=gdeslon.ru; gdeslon.ru.user_id=1021aef7-5875-45f7-b0ee-6959a369d02a; flocktory-uuid=7abf8f4e-4115-4f99-a326-bdcdd11db91a-7; advcake_track_id=fe1cec6c-6ed6-30ef-5bb0-5c1ad931a0e9; advcake_session_id=fb3ead64-0c32-333f-4f3e-9edc0d1a8168; uxs_uid=d4ebc4f0-8227-11ed-9f9b-d30b4e001776; afUserId=af50916b-24b6-45f0-b805-0bbb85f80438-p; AF_SYNC=1671734312756; MVID_GUEST_ID=22076151921; MVID_VIEWED_PRODUCTS=; wurfl_device_id=generic_web_browser; MVID_CALC_BONUS_RUBLES_PROFIT=true; NEED_REQUIRE_APPLY_DISCOUNT=true; MVID_CART_MULTI_DELETE=true; PROMOLISTING_WITHOUT_STOCK_AB_TEST=2; MVID_GET_LOCATION_BY_DADATA=DaData; PRESELECT_COURIER_DELIVERY_FOR_KBT=false; HINTS_FIO_COOKIE_NAME=1; searchType2=2; COMPARISON_INDICATOR=false; MVID_NEW_OLD=eyJjYXJ0IjpmYWxzZSwiZmF2b3JpdGUiOnRydWUsImNvbXBhcmlzb24iOnRydWV9; MVID_OLD_NEW=eyJjb21wYXJpc29uIjogdHJ1ZSwgImZhdm9yaXRlIjogdHJ1ZSwgImNhcnQiOiB0cnVlfQ==; __zzatgib-w-mvideo=MDA0dC0cTApcfEJcdGswPi17CT4VHThHKHIzd2UsWDZXIQocNmdzFRtnYClGG1t3KBArDGUTD2dcbFB2Tlk/ayAVQVssEzpxR2NCRipUDR4SGjhmIWNIYSBLVU1/FhoXfmwqUgsPXkNJc3kbN1ddHBEkWA4hPwtpW1Y0ZxUbQEgYL0tueTA8bCBjS1woSlpOdRdgSkMrNhZGRhxyM3c/awgiGVETKl94R1drZVVCODFnDE9PTRIW+Gt2iQ==; __zzatgib-w-mvideo=MDA0dC0cTApcfEJcdGswPi17CT4VHThHKHIzd2UsWDZXIQocNmdzFRtnYClGG1t3KBArDGUTD2dcbFB2Tlk/ayAVQVssEzpxR2NCRipUDR4SGjhmIWNIYSBLVU1/FhoXfmwqUgsPXkNJc3kbN1ddHBEkWA4hPwtpW1Y0ZxUbQEgYL0tueTA8bCBjS1woSlpOdRdgSkMrNhZGRhxyM3c/awgiGVETKl94R1drZVVCODFnDE9PTRIW+Gt2iQ==; cfidsgib-w-mvideo=oAkj+zpmSj5t0mhgAYh5bm5sU7buxGRs1ENR6Ynupdfit+gZeE9CCg+JBePSXZt6+gNoxfE/YEQYenuQzdmjO1wuykmuC/wKnleo4A04GwzT+ftPYnoMhNgHjle1/UcK6Grp/rtiC3Ns59Q0VVV3Fa2qCmvSbvV0u/a5; cfidsgib-w-mvideo=oAkj+zpmSj5t0mhgAYh5bm5sU7buxGRs1ENR6Ynupdfit+gZeE9CCg+JBePSXZt6+gNoxfE/YEQYenuQzdmjO1wuykmuC/wKnleo4A04GwzT+ftPYnoMhNgHjle1/UcK6Grp/rtiC3Ns59Q0VVV3Fa2qCmvSbvV0u/a5; gsscgib-w-mvideo=sc0grt9okBqdQELBvPHX8z43Hy2nDTURqmKho0jxlLR5lrZbHwhXyBTujl2vhl0tDHy7TqluE16hh1lBq4xcCX5QWCIX4wKML0dJvattrPAmcxjosXpeTbXthrH7kJ5IVziAN+ftBNwJ2SgG8I0BDoTytz1+YPzZsKqcAlOZd3Hh5v27m/htMOuMKzj5MyE0Ai7Jk+WAWuYekeTj7XLrPwzzSICtKZtGnPSFojM1tJRAyHWHoauiMPxKNL/qV+Tdlw==; gsscgib-w-mvideo=sc0grt9okBqdQELBvPHX8z43Hy2nDTURqmKho0jxlLR5lrZbHwhXyBTujl2vhl0tDHy7TqluE16hh1lBq4xcCX5QWCIX4wKML0dJvattrPAmcxjosXpeTbXthrH7kJ5IVziAN+ftBNwJ2SgG8I0BDoTytz1+YPzZsKqcAlOZd3Hh5v27m/htMOuMKzj5MyE0Ai7Jk+WAWuYekeTj7XLrPwzzSICtKZtGnPSFojM1tJRAyHWHoauiMPxKNL/qV+Tdlw==; deviceType=desktop; fgsscgib-w-mvideo=SXpVa9435a97d6f27fafbe13b732f913767f4622; fgsscgib-w-mvideo=SXpVa9435a97d6f27fafbe13b732f913767f4622; cfidsgib-w-mvideo=cruo7CKbw/b6akwAyXFd2LcJAFOf56XBKYGmzWGU9PnIYRQHGMhYjJM3yi6f/hfeH6sz6BereWRTk8EznP/eNw1RVlirJo9DrYV6HOXLOe6M/jTtUDOd4MpB9V/bNlGhoCV2+Fz0KIMb6do8DSIdt+83f/fqQ1j0uNH+; __js_p_=630,3600,0,1,0; __jhash_=322; __jua_=Mozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F108.0.0.0%20Safari%2F537.36; __hash_=fd6530ff9fb7b60e0e21391833d9e242; BIGipServericerock-prod=3187989514.20480.0000; bIPs=-957002303; mindboxDeviceUUID=a72558fa-6052-4e2a-aae3-b931b91d285c; directCrm-session=%7B%22deviceGuid%22%3A%22a72558fa-6052-4e2a-aae3-b931b91d285c%22%7D; popmechanic_sbjs_migrations=popmechanic_1418474375998%3D1%7C%7C%7C1471519752600%3D1%7C%7C%7C1471519752605%3D1; _sp_ses.d61c=*; _gid=GA1.2.269817027.1671871643; _ym_isad=2; _ga=GA1.2.946872466.1671734305; SMSError=; authError=; tmr_detect=0%7C1671871648171; _sp_id.d61c=c58c231c-4154-4760-a471-86eeeedbccf0.1671734305.2.1671871677.1671735236.49ffafd7-12f0-4e00-b9e9-137afdcaa044.0b5ed1d0-f002-4725-af0d-782d3c26cf52.47c0e322-67ce-40f1-ac00-dc6b76b6bfd2.1671871642389.25; _ga_CFMZTSS5FM=GS1.1.1671871642.2.1.1671871697.0.0.0; _ga_BNX5WPP3YK=GS1.1.1671871642.2.1.1671871697.5.0.0; MVID_ENVCLOUD=prod2',
        'referer': 'https://www.mvideo.ru/noutbuki-planshety-komputery-8/planshety-195/f/tolko-v-nalichii=da',
        'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'sentry-trace': '3e4cfb0079234bab8b02b5e22f1523e3-90d23c204dc12a43-1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
        'x-set-application-id': 'ac624c47-6157-4934-985d-d7ee6cb005e3',
    }

    params = {
        'categoryId': '195',
        'offset': '0',
        'limit': '24',
        'filterParams': 'WyJ0b2xrby12LW5hbGljaGlpIiwiIiwiZGEiXQ==',
        'doTranslit': 'true',
    }

    response = requests.get('https://www.mvideo.ru/bff/products/listing', params=params, cookies=cookies,
                            headers=headers).json()
    print(response)
    # failed response
    # failed response Ex requests.exceptions.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
    # print(response)
    # products_ids = response.get('body').get('products')
    #
    # with open('1_products.json', 'w', encoding='utf-8') as file:
    #     json.dump(products_ids, file, indent=4, ensure_ascii=False)
    #
    # print(products_ids)


def main():
    get_data()


if __name__ == '__main__':
    main()


#