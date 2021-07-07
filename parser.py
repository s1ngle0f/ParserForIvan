import requests
from bs4 import BeautifulSoup as bs
import csv
import time

class Cian:
    headers = {
        #'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.152 YaBrowser/21.2.2.101 Yowser/2.5 Safari/537.36'
    }

    def __init__(self):
        self.get_html()

    def get_html(self):
        url = "https://www.cian.ru/cat.php?deal_type=rent&engine_version=2&is_by_homeowner=1&offer_type=flat&region=1&sort=creation_date_desc&type=4"
        with requests.Session() as session:
            response = session.get(url, headers=self.headers)
        return response.text

    def parse_html(self, html):
        squares = []
        addresses = []
        prices = []
        urls = []
        user_database = []
        soup = bs(html, 'lxml')
        main__div = soup.find_all('div', {'class': '_93444fe79c--card--2umme'})
        for data in main__div:
            try:
                href = data.find('a', {'class': '_93444fe79c--link--39cNw'}).get('href')
                #print(href)
                urls.append(href)

                square = data.find('div', {'class': '_93444fe79c--container--JdWD4'}).text.replace(',', '.')
                #print(square)
                squares.append(square)

                address = data.find('div', {'class': '_93444fe79c--labels--1J6M3'}).text.replace(',', '.')
                #print(address)
                addresses.append(address)

                price = data.find_all('div', {'class': '_93444fe79c--container--2h0AF'})[1].text.replace(',', '.')
                prices.append(price)

                user_data = {
                    'square': square,
                    'address': address,
                    'price': price,
                    'href': href
                }

                user_database.append(user_data)
            except:
                continue
        return user_database

    def parseNewest_html(self, html):
        squares = []
        addresses = []
        prices = []
        urls = []
        user_database = []
        soup = bs(html, 'lxml')
        data = soup.find('div', {'class': '_93444fe79c--card--2umme'})
        try:
            href = data.find('a', {'class': '_93444fe79c--link--39cNw'}).get('href')
            #print(href)
            urls.append(href)

            square = data.find('div', {'class': '_93444fe79c--container--JdWD4'}).text.replace(',', '.')
            #print(square)
            squares.append(square)

            address = data.find('div', {'class': '_93444fe79c--labels--1J6M3'}).text.replace(',', '.')
            #print(address)
            addresses.append(address)

            price = data.find_all('div', {'class': '_93444fe79c--container--2h0AF'})[1].text.replace(',', '.')
            prices.append(price)

            user_data = {
                'square': square,
                'address': address,
                'price': price,
                'href': href
            }

            user_database.append(user_data)
        except:
            pass
        return user_database

    def save_csv(self, data):
        with open('data.csv', 'w', encoding="utf-8") as file:
            wrtr = csv.writer(file)
            wrtr.writerow(("Площадь", "Адрес", "Цена", "Ссылка"))
            for i in data:
                wrtr.writerow((i['square'], i['address'], i['price'], i['href']))

class Avito:
    headers = {
        #'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.152 YaBrowser/21.2.2.101 Yowser/2.5 Safari/537.36'
    }

    def __init__(self):
        self.get_html()

    def get_html(self):
        url = "https://www.avito.ru/moskva/kvartiry/sdam/na_dlitelnyy_srok-ASgBAgICAkSSA8gQ8AeQUg?user=1"
        with requests.Session() as session:
            response = session.get(url, headers=self.headers)
        return response.text

    def parse_html(self, html):
        # squares = []
        # addresses = []
        # prices = []
        # urls = []
        user_database = []
        soup = bs(html, 'lxml')
        main__div = soup.find_all('div', {'class': 'iva-item-content-m2FiN'})
        for data in main__div:
            try:
                href = data.find('a', {'class': 'link-link-39EVK link-design-default-2sPEv title-root-395AQ iva-item-title-1Rmmj title-listRedesign-3RaU2 title-root_maxHeight-3obWc'}).get('href')
                #urls.append('https://www.avito.ru' + href)

                square = data.find('h3', {'class': 'title-root-395AQ iva-item-title-1Rmmj title-listRedesign-3RaU2 title-root_maxHeight-3obWc text-text-1PdBw text-size-s-1PUdo text-bold-3R9dt'}).text
                #squares.append(square_local)

                address = data.find('span', {'class': 'geo-address-9QndR text-text-1PdBw text-size-s-1PUdo'}).text
                #squares.append(address_local)

                price = data.find('span', {'class': 'price-text-1HrJ_ text-text-1PdBw text-size-s-1PUdo'}).text
                #squares.append(price_local)

                user_data = {
                    'square': square,
                    'address': address,
                    'price': price,
                    'href': href
                }
                user_database.append(user_data)
            except:

                continue
        return user_database

    def save_csv(self, data):
        # with open('data.csv', 'w') as file:
        #     wrtr = csv.writer(file)
        #     wrtr.writerow(("Имя", "Номер", "Ссылка"))
        #     for i in data:
        #         wrtr.writerow((i['name'], i['phone'], i['href']))
        pass

class DomClick:
    headers = {
        #'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.152 YaBrowser/21.2.2.101 Yowser/2.5 Safari/537.36'
    }

    def __init__(self):
        self.get_html()

    def get_html(self):
        url = "https://domclick.ru/search?address=1d1463ae-c80f-4d19-9331-a1b68a85b553&limit=10&sort=price&sort_dir=asc&deal_type=rent&ne=56.528355%2C40.011284&sw=54.692732%2C34.990532"
        with requests.Session() as session:
            response = session.get(url, headers=self.headers)
        print(response.text)
        return response.text

    def parse_html(self, html):
        squares = []
        addresses = []
        prices = []
        urls = []
        user_database = []
        soup = bs(html, 'lxml')
        main__div = soup.find_all('a', {'class': '_12VP9'})
        for data in main__div:
            try:
                href = data.find('a', {'class': '_12VP9'}).get('href')
                #print(href)
                urls.append(href)

                square = data.find('div', {'class': 'property-1p6vt'}).text
                #print(square)
                squares.append(square)

                address = data.find('div', {'class': 'address-1fFcT'}).text
                #print(address)
                addresses.append(address)

                price = data.find('div', {'class': 'cardHeader-1k9XZ'}).text
                #prices.append(price)

                user_data = {
                    'square': square,
                    'address': address,
                    'price': price,
                    'href': href
                }

                user_database.append(user_data)
            except:
                continue
        return user_database

    def save_csv(self, data):
        # with open('data.csv', 'w') as file:
        #     wrtr = csv.writer(file)
        #     wrtr.writerow(("Имя", "Номер", "Ссылка"))
        #     for i in data:
        #         wrtr.writerow((i['name'], i['phone'], i['href']))
        pass

class Yandex:
    headers = {
        #'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.152 YaBrowser/21.2.2.101 Yowser/2.5 Safari/537.36'
    }

    def __init__(self):
        self.get_html()

    def get_html(self):
        url = "https://realty.yandex.ru/moskva/snyat/kvartira/bez-posrednikov/?bottomLatitude=55.544996&leftLongitude=36.795339&rgid=227292&rightLongitude=38.495473&topLatitude=55.968207&zoom=11&sort=AREA"
        with requests.Session() as session:
            response = session.get(url, headers=self.headers)
        return response.text

    def parse_html(self, html):
        squares = []
        addresses = []
        prices = []
        urls = []
        user_database = []
        soup = bs(html, 'lxml')
        main__div = soup.find_all('div', {'class': 'OffersSerpItem__info'})
        for data in main__div:
            try:
                href = data.find('a', {'class': 'Link Link_js_inited Link_size_m Link_theme_islands SerpItemLink OffersSerpItem__link'}).get('href')
                #print(href)
                urls.append(href)

                square = data.find('h3', {'class': 'OffersSerpItem__title'}).text
                #print(square)
                squares.append(square)

                address = data.find('div', {'class': 'OffersSerpItem__address'}).text
                #print(address)
                addresses.append(address)

                price = data.find('div', {'class': 'Price OffersSerpItem__price'}).text
                #prices.append(price)

                user_data = {
                    'square': square,
                    'address': address,
                    'price': price,
                    'href': href
                }

                user_database.append(user_data)
            except:
                continue
        return user_database

    def save_csv(self, data):
        # with open('data.csv', 'w') as file:
        #     wrtr = csv.writer(file)
        #     wrtr.writerow(("Имя", "Номер", "Ссылка"))
        #     for i in data:
        #         wrtr.writerow((i['name'], i['phone'], i['href']))
        pass

def main():
    UB = []
    avito = Cian()
    while True:
        html = avito.get_html()
        result = avito.parseNewest_html(html)
        if len(UB) > 0:
            if UB[0]['href'] != result[0]['href']:
                UB.insert(0, result[0])
                for i in UB:
                    print(i['square'], ' ||| ', i['address'], ' ||| ', i['price'], ' ||| ', i['href'])
        else:
            UB.append(result[0])
            for i in UB:
                print(i['square'], ' ||| ', i['address'], ' ||| ', i['price'], ' ||| ', i['href'])

        avito.save_csv(result)
        print("OK")
        time.sleep(300)

if __name__ == '__main__':
    main()