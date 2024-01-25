FROM python:3
COPY dice.py /dice.py
CMD ["python", "/dice.py"]