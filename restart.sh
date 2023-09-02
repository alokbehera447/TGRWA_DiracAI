sudo systemctl restart gunicorn
sudo systemctl daemon-reload
sudo systemctl restart gunicorn.socket gunicorn.service
sudo nginx -t && sudo systemctl restart nginx
sudo systemctl start postgresql
sudo systemctl enable postgresql
sudo systemctl restart redis.service
sudo systemctl start daphne.service









