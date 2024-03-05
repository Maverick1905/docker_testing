FROM python:3.9-alpine
WORKDIR /app
COPY Requirements.txt .
COPY app.py .
RUN pip install -r Requirements.txt
CMD ["app.py"]
EXPOSE 8080
ENTRYPOINT [ "python" ]
