    import requests
    import pandas as pd
    url = "https://finfo-api.vndirect.com.vn/v4/stock_prices"


    # Initialize an empty dataframe to store the data

    tickers = ["ITD", "ELC", "ST8", "SAM", "DXG", "NLG", "HDG", "KBC", "DIG", "NAF", "KDC", "LAF", "PAN", "DBC", "VCF"]
    for ticker in tickers:
        page = 1
        all_data = pd.DataFrame()
        while page < 100:
            params = {
                "sort": "date",
                "q": f"code:{ticker}~date:gte:2018-01-01~date:lte:2023-09-30",
                "size": "15",
                "page": str(page)
            }

            headers = {
                "Content-Type": "application/json",
                "Referer": "https://dstock.vndirect.com.vn/",
                "Sec-Ch-Ua": '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
                "Sec-Ch-Ua-Mobile": "?0",
                "Sec-Ch-Ua-Platform": '"Linux"',
                "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
            }

            response = requests.get(url, params=params, headers=headers)

            if response.status_code == 200:
                print("Success get prices on page", page, "for code ", ticker)
                data = response.json()
                df = pd.DataFrame(data['data'])
                # Append the data to the dataframe
                all_data = pd.concat([all_data, df], ignore_index=True)

            else:
                print(f"Failed to fetch data. Status code: {response.status_code}")

            page += 1

        # Save the dataframe to a CSV file
        all_data.to_csv(f'{ticker}.csv', index=False)
