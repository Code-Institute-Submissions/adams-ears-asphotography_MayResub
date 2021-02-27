 ![]()

# AS Photography
[Live Site]()
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
6. [Deployment](#deploy)
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

![Page Structure]()

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

[Desktop Wireframe]()

[Mobile Wireframe]()


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


## Testing <a name="test"></a>

### HTML Validatior
All HTML Valid - No Errors Found:
![HTML Validation]()

### CSS Validatior
Results from CSS validator - No Errors found.
![CSS Validation]()

### Js Validatior
All Syntax Valid
![JS Validation]()

### Python Validatior
All Syntax Valid
![Python Validation]()

### Browser Compatability
Browser compatability was tested across five different web browsers and these are:

- Google Chrome
- Mozilla Firefox
- Internet Explorer 11
- Safari
- Opera

The game was desinged using Google Chrome however functions on all browsers mentioned above. 

### Other testing


## Deployment <a name="deploy"></a>
In order to successfully publish the website to **Heroku** use the following steps :
- Head to the [Heroku](heroku.com) website and signup 
- Once Signed up Select **Create New App** from the New dropdown menu
- Fill in **App-name box**  and select **Region**
- Once on homepage select **Connect to Github** in the **Deployment Method**
- Make sure your Github name is showing and search for the repo name in the search box
- Once found click **Connect**
**Your site will now be published at** https://reviewsic-ms3.herokuapp.com/.

-Environment variables can be amended in settings from main page and then select Reveal Config Vars

## Credits <a name="credit"></a>

### Content
All design ideas are original content from the developer


### Media


### Acknowledgements

