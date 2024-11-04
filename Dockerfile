FROM python:3.9

WORKDIR /views

COPY . /views

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8501

CMD ["streamlit", "run", "main.py"]