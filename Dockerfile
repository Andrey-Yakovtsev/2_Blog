FROM python:3.8.2

WORKDIR /app

COPY req.txt ./

RUN pip install -r req.txt

COPY . .

RUN chmod +x entrypoint.sh

EXPOSE 5000

ENTRYPOINT ["./entrypoint.sh"]

CMD ["python", "app.py"]