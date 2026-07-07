# SSL Setup Documentation

## Current Deployment

The application is currently deployed using HTTP because no custom domain is available.

The application is accessible via the EC2 Public IP address.

## Production SSL Setup

If a domain becomes available, the following steps should be performed:

1. Purchase or configure a domain.
2. Point the domain's DNS A record to the EC2 Public IP.
3. Install Certbot on the server.
4. Obtain a free SSL certificate from Let's Encrypt.
5. Configure NGINX to use the SSL certificate.
6. Redirect all HTTP traffic to HTTPS.

## Example Commands

```bash
sudo apt install certbot python3-certbot-nginx
sudo certbot --nginx -d domain-name.com
```

I used HTTP due to the absence of a custom domain.