# Etapa de construcción del frontend
FROM node:16-alpine AS frontend
WORKDIR /app
COPY ./applications/SIP_application/client/package.json .

RUN npm cache clean --force
RUN npm install -g npm@6
RUN npm install
COPY ./applications/SIP_application/client .
RUN npm run build

# Etapa de construcción del backend
FROM python:3.8-alpine
WORKDIR /app
COPY --from=frontend /app/build /app/static
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . .
CMD ["python3", "web2py.py"]