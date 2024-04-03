FROM python:3.9

WORKDIR /app

COPY requirements.txt .

ENV FILE_NAME="small_word_list.txt"

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["sh", "-c", "python3 main.py $FILE_NAME"]
