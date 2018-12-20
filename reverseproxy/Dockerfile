FROM nginx:alpine
RUN apk update && apk --update add redis
RUN mkdir -p /tmp
COPY nginx.conf /etc/nginx/nginx.conf
CMD ["nginx", "-g", "daemon off;"]

