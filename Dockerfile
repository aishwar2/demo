# Production-grade lightweight Nginx Alpine container
FROM nginx:alpine

LABEL maintainer="aishwar2"
LABEL description="CI/CD automated test website container"

# Remove default static files
RUN rm -rf /usr/share/nginx/html/*

# Copy website assets
COPY index.html /usr/share/nginx/html/
COPY assets/ /usr/share/nginx/html/assets/

# Copy custom nginx configuration
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Expose standard HTTP port
EXPOSE 80

# Health check to ensure nginx is serving traffic
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
  CMD wget --quiet --tries=1 --spider http://localhost/ || exit 1

# Start nginx in foreground
CMD ["nginx", "-g", "daemon off;"]
