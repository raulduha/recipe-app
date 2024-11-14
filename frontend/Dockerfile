# Usa una imagen de Node.js
FROM node:18-alpine

# Configura el directorio de trabajo
WORKDIR /app

# Copia y instala las dependencias
COPY package.json yarn.lock ./
RUN yarn install

# Copia el código fuente
COPY . .

# Compila la aplicación
RUN yarn build

# Usa una imagen de servidor para servir los archivos estáticos
FROM nginx:alpine
COPY --from=0 /app/build /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
