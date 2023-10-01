**Book Give Away - Installation Guide**

1. **Clone the Project**:
   ```
   git clone https://github.com/giorgitchanturidze/book_giveaway.git
   ```

2. **Setup Environment Variables**:
   - Duplicate `.sample-env` as `.env`.
   - Generate a secret key from [here](https://djecrety.ir/) and update the `.env` file.

3. **Build and Start Services with Docker**:
   ```
   docker-compose up -d --build
   ```

4. **Initialize Admin Account**:
   ```
   docker-compose exec web python manage.py createsuperuser
   ```

Congratulations, the installation is complete!
