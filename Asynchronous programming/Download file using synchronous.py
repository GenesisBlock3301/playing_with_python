import asyncio
import os
import urllib.request


async def downloading_coroutine(url):
    # A coroutine to download specific url
    request = urllib.request.urlopen(url)
    file_name = os.path.basename(url)

    with open(file_name,'wb') as file_handle:
        while True:
            chunk = request.read(1024)
            if not chunk:
                break
            file_handle.write(chunk)
    msg = f"Finished the downloading {file_name}"
    return msg

async def main(urls):
    """
    create a group of coroutins and waits for them to finish.
    :return:
    """

    coroutines = [downloading_coroutine(url) for url in urls]

    completed , pending = await asyncio.wait(coroutines)
    print(completed,pending)
    for i in completed:
        print(i.result())
if __name__ == '__main__':
    import time
    start = time.time()
    urls = ["http://www.irs.gov/pub/irs-pdf/f1040.pdf",
            "http://www.irs.gov/pub/irs-pdf/f1040a.pdf",
            "http://www.irs.gov/pub/irs-pdf/f1040ez.pdf",
            "http://www.irs.gov/pub/irs-pdf/f1040es.pdf",
            "http://www.irs.gov/pub/irs-pdf/f1040sb.pdf"]
    event_loop = asyncio.get_event_loop()
    try:
        event_loop.run_until_complete(main(urls))
    finally:
        event_loop.close()
    end = time.time()
    print("Finished time",end-start)