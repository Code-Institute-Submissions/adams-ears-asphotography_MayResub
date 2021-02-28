 ![](https://github.com/adams-ears/asphotography/blob/master/wireframes/mockup.jpg)

# AS Photography
[Live Site](https://asphotography.herokuapp.com/)
This Project has been designed as a web based application for a photographer to promote work as well as take bookings and include a shopping area for prints or web vouchers. 
The **AS Photography** project will highlight what I have learnt across the full course using the full stack. HTML, CSS, Javascript with the 
addition of the backend language Python and using framework Django to create and develop a fully functioning , responsive web application.

## Contents 
1. [Project](#project)
2. [UX](#ux)\
       - (a) [User Stories](#UserStories)\
       - (b) [Admin Stories](#adminstories)\
       - (c) [Wireframes](#wireframes)
3. [Features](#features)\
       (a) [Development Modification](#devmod)
4. [Technologies](#tech)
5. [Testing](#test)
6. [Deployment](#deploy)\
       - (a) [Step 1- Heroku](#Heroku)\
       - (b) [Step 2 & 3 - AWS](#AWS)\
       - (c) [Step 4 - Django and S3 Connection](#Django)\
       - (d) [Step 5 & 6 - Media & Stripe](#Media)
7. [Credits](#credit)



## Project <a name="project"></a>
My project will be a reflection of what I've learnt from the complete Full Stack Development course. AS Photography is a web based application
to promote work and services for a photographer. Users that come to the site will be able to view the services provided in an interactive manner via
modal cards, contact the photographer directly through a contact form and use the shop to purchase vouchers or prints. The user will be able to sign up 
and make an account where they will be able to view previous orders and shipping details.

The site is made up of five main pages Landing, Account, Services, Contact and Shop. There are another six sub pages from these main five which include 
login, registration, basket, checkout, order confirmation and products. All pages accross the site have a consistent design throughout. 
 
 The five main pages and purpose are as follows: 

- **Landing Page:** Inital page users will see when visiting the website, Photographers logo at the top center with the nav bar beneath.
- **Account Page:** Account page button will be visible on navigation bar with either Login or Register. If registered user will be taken to personalised account page
                    showing order details, bookings and address. If not registered user will be taken to a registration page.
- **Services Page :** The user will see a selection of cards with an image, small descripton of service and a button to learn more. If button is clicked a modal will appear
                    with a full descripton of service along with example gallery.
- **Contact:**  Contact page will be a form with inputs as follows : Name, Email, Phone (optional), Category and Enquiries.
- **Shop:**  The shop will display current available products, the basket will appear next to the navbar with an updating total as products are added.


The six sub pages and purpose are as follows:

- **Login:** The login page will be a subcategory from accounts, showing login requirments e.g Username and email that was used during registration.
- **Registration:** The registration page will be a subcategory from accounts, showing a registration form, once completed the user will be sent to accounts page.
- **Basket:** The basket page will be a subcategory from the shop, also available from the basket icon next to the nav bar. This page will show subtotal of products selected
              and option to go to secure checkout.
- **Checkout:** Secure checkout page will be a subcategory from the basket page, here the user will fill in shipping, billing and card details to confirm purchase.
- **Order Confirmation:** After securely checking out the user will be taken to a order confirmation pagr which will show the unique order ID, shipping details and information on products ordered.
                          The order confirmation page will also be accessible via the accounts page.
- **Products:**  The product page will only be available to admins or the website owner. This will a subcategory from the accounts page, giving the admin 
                 a page where products can be added to the shop, including Name, Value, Product Image and Description.

![Page Structure](https://github.com/adams-ears/asphotography/blob/master/wireframes/Site%20Map%20jpeg.jpg)

## UX <a name="ux"></a>
This site brings the user to sign up and  easily navigate through from landing page to uploading reviews, seeing thier own dedicated profile and reading reviews.  
### User Stories <a name="UserStories"></a>
The users needs:
- The user is able to view previous works by photographer in gallery style setting
- The user is able to navigate through site from portfolio to booking form to print shop easily
- The user is easily able to register an account in order to make bookings with photographers for events, login and out, 
  receive confirmation email, retrieve new password if forgotten and have a unique profile customer
- The user is easily able to contact the photographer through an internal messaging system.
- The user is able view  products in the print shop, individual product details and the overall total in basket at any time whilst in the shop.

### Website Admin/Owner Stories <a name="adminstories"></a>
- View Bookings and Orders
- Email / Message Client
- Add Products
- Edit/Delete Products

### Wireframes <a name="wireframes"></a>

The links below will take you to a PDF of each of the wireframes i have created for this project.

[Desktop Wireframe](https://github.com/adams-ears/asphotography/blob/master/wireframes/Desktop%20MS4%20frame.pdf)

[Mobile Wireframe](https://github.com/adams-ears/asphotography/blob/master/wireframes/Mobile%20MS4%20frame.pdf)


## Features <a name="features"></a>

Here is a list of the features included on the site. Along with possible additions later in order to develop the site:

**Features included:**
- Individual profile pages with ability to view previous orders and shipping information.
- Previous photos by photography displayed in gallery style within modal cards.
- Services found on service page will be in cards which expand with full detail once clicked.
- Responsive design, with all pages working well on desktop, tablet and mobile.
- Pop out calender on contact form for enquiries.
- Shop simple to navigate through, from products to secure checkout.
- Admin will have ability to create, edit and delete products.

**Future features to be included at a later stage:**
- Internal messaging system from user to website owner in order to make bookings and contact photographer directly.
- Directly shareable reviews from profiles to social media including Facebook and Twitter

**Other Feature Mentions**


### Development Modification <a name="devmod"></a>
During the development process, i encounted a few hurdles which left me modifying from original design. One major factor was 
the lack of clarity around the navigation bar, if left without a white background many of the words would be unseen when reducing in size to burger. Another
large factor was the exclusion of vouchers, i decided to go for a more traditional approach toward the shop to show what i had learnt so far in the course.




## Technologies <a name="tech"></a>

Various different technologies have been used throughout my project, they are as follows:

- **Balsamiq** Rapid, effective and fun wireframing software.
- **Github** A cloud-based hosting service that lets you manage Git repositories.
- **Git**  A Distributed Version Control tool that is used to store different versions of a file in a remote or local repository.
- **Gitpod** An online IDE, providing a full working development environment.
- **Bootstrap** A front-end framework for developing responsive and mobile-first websites.
- **Markdown** A lightweight markup language with plain-text formatting syntax.
- **HTML5** Another markup language, predominantly used to structure and present content to the world wide web.
- **CSS3** Cascading style sheet language used in conjunction with HTML to create ontent and style.
- **jQuery** is a JavaScript library designed to simplify HTML DOM tree traversal and manipulation
- **Python** Python is an interpreted, high-level and general purpose programming language
- **Django** is a high-level Python Web framework that encourages rapid development and clean, pragmatic design.
- **Stripe** is a payment processing platform.
- **Heroku** Heroku is a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud.
- **AWS**  allows you to run web and application servers in the cloud to host dynamic websites.
- **S3** Amazon S3 is a service offered by Amazon Web Services that provides object storage through a web service interface.




## Testing <a name="test"></a>

### HTML Validatior
All HTML Valid - Errors found are from Bootstrap classes:
![HTML Validation](https://github.com/adams-ears/asphotography/blob/master/wireframes/HTML.jpg)

### CSS Validatior
Results from CSS validator - No Errors found.
![CSS Validation](https://github.com/adams-ears/asphotography/blob/master/wireframes/CSS.jpg)

### Js Validatior
All Syntax Valid
![JS Validation](https://github.com/adams-ears/asphotography/blob/master/wireframes/JS.jpg)

### Python Validatior
Majority of Syntax is Valid, Migration and core django settings left untouched.


### Browser Compatability
Browser compatability was tested across five different web browsers and these are:

- Google Chrome
- Mozilla Firefox
- Internet Explorer 11
- Safari
- Opera

The web application was desinged using Google Chrome however functions on all browsers mentioned above. 

## Deployment <a name="deploy"></a>
### Step 1 - Heroku <a name="Heroku"></a>

- In order to successfully publish the website to **Heroku** use the following steps :
- Head to the [Heroku](heroku.com) website and signup 
- Once Signed up Select **Create New App** from the New dropdown menu
- Fill in **App-name box**  and select **Region**
- For this project Postgres was selected from **Resources**
- Head back to gitpod and install dj_database_url and psycopg2-binary then freeze to requirements.txt
- Head to settings.py and import dj_database_url
- Comment out original database and replace with dj_database_url.parse(**fill with database url from heroku config variables settings**)
- Run Migrations to new database
- Load in fixtures
- Create superuser
- Remove heroku database config, uncomment default database and commit changes
- Now add if statement to connect to heroku environment varibles and else original
- Add gunicorn as your webserver and freeze to requirements.txt
- Make Procfile to tell heroku to make a web dyno whic will run gunicorn and serve django
- Login to heroku in the terminal
- Temporarily disable collectstatic using DISABLE_COLLECTSTATIC=1 --app **project name**
- Add host name to **Allowed Hosts** in settings.py
- Add, commit and push changes to Github
- Initialise heroku git remote by using heroku git:remote -a **project name**
- Then push to heroku using **git push heroku master**
- Check app has been deployed through link
- Now set to automatically deploy to heroku when you push to Github
- Once on homepage select **Connect to Github** in the **Deployment Method**
- Make sure your Github name is showing and search for the repo name in the search box
- Once found click **Connect**
- **enable automatic deploys**
**Your site will now be published at** https://asphotography.herokuapp.com/.
- Next look up django key gen and add key to heroku config variables
- Go back to settings.py and replace SECRET_KEY setting with a call to get it from the environment
- Set debug to be true only if varible is in environment 
- Push changes

### Step 2 - AWS(S3) <a name="AWS"></a>
- Follow steps to make AWS account
- Choose which storage system to use from services, in this case S3 was chosen
- Create bucket, give it **Name**, select **Region** closet to you
- Uncheck all public access and acknowledge
- Create bucket
- Select bucket and go to properties tab
- Choose **Static webiste hosting**
- Check box **Use bucket to host a website**
- Fill in default values and clock save
- Go to **Permissons Tab**
- Fill in **CORS configurations**
- Go to **Policy Tab** and click generate Policy
- Fill in form accordinly
- Grab **ARN** from bucket permissions tab
- Add statement, generate policy
- Copy policy into **Bucket Policy** editor
- Head to **Access Control List**
- Check box for everyone under **Public Access**

### Step 3 - AWS(IAM)
- Open IAM
- Select **Group** and **Create New Group**
- Name Group and follow the end to **Create**
- Click **Policies** and **Create Policy**
- Go to **Json** tab and import relevant policy
- Include bucket **ARN** from S3 in JSON file under **Resource**
- Click **Review Policy** and give **Name** and **Description** then **Create**
- Head to **Groups** and click your Group
- Click **Attach Policy**, search and select policy you just created and **Attach**
- Head to **Users**
- Add User and give **Programmatic Access**
- Add User to Group
- Click to end and **Create**
- Download and **Save CSV file!!**

### Step 4 - Django and S3 Connection <a name="Django"></a>
- Install Boto3 and Django-storages and freeze
- Add **Storages** to install apps
- Add if statement USE_AWS to communicate with heroku config variables to select correct bucket
- In statement add **AWS_STORAGE_BUCKET_NAME, AWS_S3_REGION_NAME, AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY**
- Head to heroku and add these to config varibles make sure the keys stay secret!! (both keys can be found in CSV)
- Add **USE_AWS = True** and remove **DISABLE_COLLECTSTATIC** from config variables
- Next in if statement in settings.py add **AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazon.com** to tell django where the static files are coming from
- Create a file called **custom_storages.py** and import settings and **S3BotoStorage from storages.backends.s3.boto3**
- Create a custom class which inherits **S3BotoStorage**
- Tell it where to store static files in settings
- Copy to second class for media files
- Go back to settings.py
- Tell it for static file storage to use the file thats just been create and the location is a file called **static**
- Repeat for Media files
- Override static and media urls with **Custom Domain and New Location**
- Add, Commmit and Push will will trigger an auto deply to Heroku 
- Check build log that all static files has been collected successfully
- Head to **S3** to check for static folder with static files

### Step 5 - Media Files <a name="Media"></a>
- Head to **S3** and create a new folder called **Media**
- Grant public read access and Upload files into folder

### Step 6 - Stripe
- Head to Stripe
- Grab API keys
- Add to Heroku config variables
- Go back to **Stripe**, slect **Webhooks** and **Add Endpoint**
- Add **URL** for Heroku app followed by /checkout/wh/
- Recieve all events and **Add Endpoint**
- Reveal webhook sing in secret and add to heroku congif variables
- Make sure they match settings.py

## Credits <a name="credit"></a>

### Content
All design ideas are original content from the developer


### Media
All photos taken by Adam Sears


### Acknowledgements
This has been a great journy and learning experience, i feel very proud to have gotten this far with the support of my mentor Jonathan Munz. His endless
support throughout the course has propelled me to where i am today, being able to problem solve and think logically about the next step but mainly keeping calm and knowing
when to step away for five minutes. I would also like to thank all of the tutors who have assisted me throught the course and the slack community for 
always being there for anyone who needs it!. 

Finally i would like thank my partner for always being there and pushing me to succeed throughout the course! 
