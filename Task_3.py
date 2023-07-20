PES2022 = int(input("O'yin hajmini MB da kiriting:"))
Internet = int(input("Internet tezligini MB da kiriting:"))

downloaded_size = 0
i = 0
while downloaded_size < PES2022:
    i += 1

    downloaded_size += Internet
    if downloaded_size > PES2022:
        downloaded_size = PES2022

    percent = round(downloaded_size * 100 / PES2022)
    print(f"{i} sekund o'tdi. {PES2022} MB dan {downloaded_size} MB yuklab olindi ({percent}%)")
