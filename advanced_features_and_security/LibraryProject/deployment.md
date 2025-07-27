# Deployment Configuration for HTTPS (Production)

To serve this Django application securely over HTTPS in a production environment:

1. **Install SSL Certificates**
   - Use Let's Encrypt or a commercial provider.
   - For Let's Encrypt with Nginx:
     ```bash
     sudo apt install certbot python3-certbot-nginx
     sudo certbot --nginx
     ```

2. **Update Nginx Configuration**
   Example `/etc/nginx/sites-available/example.com`:
