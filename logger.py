from datetime import datetime
from config import LOG_FILE



def log(message):

    date = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )


    text = f"{date} - {message}"


    print(text)


    with open(
        LOG_FILE,
        "a",
        encoding="utf-8"
    ) as file:

        file.write(text + "\n")