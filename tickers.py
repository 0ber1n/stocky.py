import subprocess
import time
import datetime



def data_dump(ticker_name):
    
    now = datetime.datetime.now()
    one_year_ago = now - datetime.timedelta(days=365)


    period1 = int(one_year_ago.timestamp())
    period2 = int(now.timestamp())

    # Format the URL, converting the integers to strings
    url = f'https://query1.finance.yahoo.com/v7/finance/download/{ticker_name}?period1={period1}&period2={period2}&interval=1d&events=history&includeAdjustedClose=true'
    
    # Define the output file
    output_file = f'stocks/{ticker_name}.csv'

    subprocess.run(["curl", "-o", output_file, url])


all_tickers = [
    "AAPL",  # Apple Inc.
    "MSFT",  # Microsoft Corporation
    "NVDA",  # NVIDIA Corporation
    "TSLA",  # Tesla, Inc.
    "AMZN",  # Amazon.com, Inc.
    "AMD",   # Advanced Micro Devices, Inc.
    "INTC",  # Intel Corporation
    "BAC",   # Bank of America Corporation
    "F",     # Ford Motor Company
    "WBA",   # Walgreens Boots Alliance, Inc.
    "MARA",  # Marathon Digital Holdings, Inc.
    "PLTR",  # Palantir Technologies Inc.
    "GOOGL", # Alphabet Inc. (Class A)
    "GOOG",  # Alphabet Inc. (Class C)
    "ABT",   # Abbott Laboratories
    "JNJ",   # Johnson & Johnson
    "PG",    # Procter & Gamble Company
    "CRM",   # Salesforce, Inc.
    "ADBE",  # Adobe Inc.
    "AXP",   # American Express Company
    "LRCX",  # Lam Research Corporation
    "CAT",   # Caterpillar, Inc.
    "COST",  # Costco Wholesale Corporation
    "QCOM",  # QUALCOMM Incorporated
    "JPM",   # JP Morgan Chase & Co.
    "MS",    # Morgan Stanley
    "ANF",   # Abercrombie & Fitch Company
    "SIRI",  # Sirius XM Holdings Inc.
    "SOFI",  # SoFi Technologies, Inc.
    "WBD",   # Warner Bros. Discovery, Inc.
    "GTES",  # Gates Industrial Corporation plc
    "ET",    # Energy Transfer LP
    "V",     # Visa Inc.
    "MA",    # Mastercard Incorporated
    "NFLX",  # Netflix, Inc.
    "DIS",   # The Walt Disney Company
    "NKE",   # NIKE, Inc.
    "ORCL",  # Oracle Corporation
    "CSCO",  # Cisco Systems, Inc.
    "PFE",   # Pfizer Inc.
    "MRK",   # Merck & Co., Inc.
    "T",     # AT&T Inc.
    "VZ",    # Verizon Communications Inc.
    "KO",    # The Coca-Cola Company
    "XOM",   # Exxon Mobil Corporation
    "CVX",   # Chevron Corporation
    "TSM",   # Taiwan Semiconductor Manufacturing Company Limited
    "SNAP",  # Snap Inc.
    "SQ",    # Block, Inc. (formerly Square, Inc.)
    "RIVN"   # Rivian Automotive, Inc.
]

fifty_tickers = [
    "AAPL",  # Apple Inc.
    "MSFT",  # Microsoft Corporation
    "NVDA",  # NVIDIA Corporation
    "TSLA",  # Tesla, Inc.
    "AMZN",  # Amazon.com, Inc.
    "AMD",   # Advanced Micro Devices, Inc.
    "INTC",  # Intel Corporation
    "BAC",   # Bank of America Corporation
    "F",     # Ford Motor Company
    "WBA",   # Walgreens Boots Alliance, Inc.
    "MARA",  # Marathon Digital Holdings, Inc.
    "PLTR",  # Palantir Technologies Inc.
    "GOOGL", # Alphabet Inc. (Class A)
    "GOOG",  # Alphabet Inc. (Class C)
    "ABT",   # Abbott Laboratories
    "JNJ",   # Johnson & Johnson
    "PG",    # Procter & Gamble Company
    "CRM",   # Salesforce, Inc.
    "ADBE",  # Adobe Inc.
    "AXP",   # American Express Company
    "LRCX",  # Lam Research Corporation
    "CAT",   # Caterpillar, Inc.
    "COST",  # Costco Wholesale Corporation
    "QCOM",  # QUALCOMM Incorporated
    "JPM",   # JP Morgan Chase & Co.
    "MS",    # Morgan Stanley
    "ANF",   # Abercrombie & Fitch Company
    "SIRI",  # Sirius XM Holdings Inc.
    "SOFI",  # SoFi Technologies, Inc.
    "WBD",   # Warner Bros. Discovery, Inc.
    "GTES",  # Gates Industrial Corporation plc
    "ET",    # Energy Transfer LP
    "V",     # Visa Inc.
    "MA",    # Mastercard Incorporated
    "NFLX",  # Netflix, Inc.
    "DIS",   # The Walt Disney Company
    "NKE",   # NIKE, Inc.
    "ORCL",  # Oracle Corporation
    "CSCO",  # Cisco Systems, Inc.
    "PFE",   # Pfizer Inc.
    "MRK",   # Merck & Co., Inc.
    "T",     # AT&T Inc.
    "VZ",    # Verizon Communications Inc.
    "KO",    # The Coca-Cola Company
    "XOM",   # Exxon Mobil Corporation
    "CVX",   # Chevron Corporation
    "TSM",   # Taiwan Semiconductor Manufacturing Company Limited
    "SNAP",  # Snap Inc.
    "SQ",    # Block, Inc. (formerly Square, Inc.)
    "RIVN"   # Rivian Automotive, Inc.
]


