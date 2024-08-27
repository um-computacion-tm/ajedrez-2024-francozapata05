FROM python:3-alpine

RUN apk add --no-cache git
RUN git clone https://github.com/um-computacion-tm/ajedrez-2024-francozapata05.git

WORKDIR /ajedrez-2024-francozapata05

RUN pip install -r requirements.txt

CMD ["sh", "-c", "coverage run -m unittest && coverage report -m && python -m main.main"]

# docker buildx build -t ajedrez . -- no-cache
# docker run -i ajedrez

# docker ps --> muestra cuales son las imagenes de Docker que se están ejecutando
# docker -a --> muestra todas las imagenes
