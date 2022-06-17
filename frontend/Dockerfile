FROM node:16.15.0
WORKDIR /code/frontend

COPY package.json package-lock.json ./
RUN npm install
RUN npm install react-scripts@5.0.1 -g
COPY . /code/frontend
EXPOSE 3000