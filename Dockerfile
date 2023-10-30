FROM python:3.11

RUN useradd -m user

USER user

WORKDIR /home/user

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY app.py .
COPY config/ /home/user/config/
COPY modules/ /home/user/modules/
COPY static/ /home/user/static/

EXPOSE 8501

CMD ["/home/user/.local/bin/streamlit", "run", "app.py"]