# job_task

Starting app:
1. Go to app directory and start venv: source /var/app/venv/bin/activate
2. start an app: flask run --host=127.0.0.1 --port=5000
3. Go to karolisrimkus.tech to check how is everything working

Additional tasks:

1. Setup free domain with SSL

I had not used domain name in Hostinger so I just configured DNS for VPS and then with certbot installed free SSL via Let's Encrypt

2. Create redirect: /google should redirect to google.com
   
I implemented this in two ways: first, by adding a route in the Flask backend, and second, by configuring the redirect directly in the VPS (Nginx) server settings.

3. Set up git for your assignment

Coded all Flask app on my VS code studio and then pushed everything to GitHub

4. Create automated GitHub Action deployment to VPS

I attempted this, but it failed due to an error saying deployment requires payment. I had set up SSH keys, with the public key installed on the VPS and the private key stored as a secret in GitHub, as well documented deployment file.

5. Implement frontend input validation

For checkboxes, I used the required attribute. For numeric inputs, I wrote a small JavaScript script to validate that only numbers were entered and to check the length.

6. Add a progress bar showing completion status

I wrote a function to calculate the current survey step and displayed a progress bar using a styled <div>.

7. Ensure responsive design for mobile/desktop

I used Tailwind CSS, which provides built-in responsive utilities, and added custom styles to improve mobile phone usability.

8. Create a survey design mockup
missing this one

9. Prepare frontend to send survey data to '/api/survey'

    I created in the back end to collect all data in json

10. Save user progress in cookies or storage
    Misssing this one
