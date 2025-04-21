pip install -r requirements.txt ---> to download all packages
py manage.py makemigrations
py manage.py migrate
py manage.py scrape_review
py manage.py runserver


1)Run The 'py manage.py scrape_reviews' after mgrations to load the reviews and product and saving them into db.
2) /createUser -> Creating the user with payload as json data (POST)
3) /login_customer -> login customer returns JWT(expires in 1Day) (POST)
4) /add_customer_review adding reviews of customer (POST)
5) /get_all_user_reviews/customer_id getting all reviews of customer (GET)
6) /edit_user_rating edit customer ratings (PUT)
7) /delete_user_rating/review_id deleting customer reviews (DELETE) 
8) /get_product_along_reviews/product_id get product along with reviews (GET)
