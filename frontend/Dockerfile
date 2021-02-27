FROM node:14-alpine as web-builder
WORKDIR /usr/src/rit-sse-website
RUN apk add yarn
COPY package.json ./
COPY yarn.lock ./
RUN yarn install --frozen-lockfile
ENV NODE_ENV production
ARG REACT_APP_HOST
ENV REACT_APP_HOST $REACT_APP_HOST
ARG REACT_APP_API_HOST
ENV REACT_APP_API_HOST $REACT_APP_API_HOST
COPY . .
RUN yarn build

FROM alpine:3.13.2
WORKDIR /var/www/html
RUN addgroup -g 1000 -S www-data \
    && adduser -u 1000 -D -S -G www-data www-data
RUN apk add nginx
COPY ./nginx.conf /etc/nginx/
COPY --from=web-builder /usr/src/rit-sse-website/build ./
CMD ["/usr/sbin/nginx","-g","daemon off;"]
