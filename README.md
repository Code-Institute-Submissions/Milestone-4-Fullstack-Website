# [Noir Digital](https://milestone-four-noir-digital.herokuapp.com/)

### This site is an ecommerce website selling art prints. A user can also leave a testimonial and request something custom.

[![Build Status](https://travis-ci.org/thestarvingcoder/Milestone-4-Fullstack-Website.svg?branch=master)](https://travis-ci.org/thestarvingcoder/Milestone-4-Fullstack-Website)


#### UX

I created this website to sell graphic design.

**User Story 1:**
John Doe is curious about the purpose of the site. He can read about the reason it was created on the home page.

**User Story 2:**
Jane Doe wants to browse the art. She can do that by clicking "work" in the nav bar.

**User Story 3:**
Jeff Doe wants to read more about a specific art piece. He can do that by clicking on its image in the work page.

**User Story 4:**
Jane Doe wants to login. She can do so by clicking on "login" in the navbar and filling out the following form.

**User Story 5:**
John Doe wants to sign up. She can do so by clicking on "Register" in the navbar and filling out the following form.

**User Story 6:**
Jeff Doe wants to read more about the site. He can do so by clicking "about" in the navbar.

**User Story 7:**
Jerry Doe wants to read about the sites news. He can do so by clicking "news" in the navbar.

**User Story 8:**
Jane Doe wants to buy a logo. She can do so by clicking add on the product and then checking out.

### Wireframes

- [Home Browser](https://milestone-four-noir-digital.s3.us-east-2.amazonaws.com/static/wireframes/Home-Browser.png)
- [Home Phone](https://milestone-four-noir-digital.s3.us-east-2.amazonaws.com/static/wireframes/Home-Phone.png)
- [About Browser](https://milestone-four-noir-digital.s3.us-east-2.amazonaws.com/static/wireframes/About-Browser.png) 
- [About Phone](https://milestone-four-noir-digital.s3.us-east-2.amazonaws.com/static/wireframes/About-Phone.png) 
- [News Browser](https://milestone-four-noir-digital.s3.us-east-2.amazonaws.com/static/wireframes/News-Browser.png) 
- [News Phone](https://milestone-four-noir-digital.s3.us-east-2.amazonaws.com/static/wireframes/News-Phone.png) 
- [Login Browser](https://milestone-four-noir-digital.s3.us-east-2.amazonaws.com/static/wireframes/Login-Browser.png)
- [Login Phone](https://milestone-four-noir-digital.s3.us-east-2.amazonaws.com/static/wireframes/Login-Phone.png) 
- [View All Browser](https://milestone-four-noir-digital.s3.us-east-2.amazonaws.com/static/wireframes/View-all-Browser.png)
- [View All Phone](https://milestone-four-noir-digital.s3.us-east-2.amazonaws.com/static/wireframes/View-all-Phone.png) 
- [Testimonial Browser](https://milestone-four-noir-digital.s3.us-east-2.amazonaws.com/static/wireframes/Testimonial-Browser.png)
- [Testimonial Phone](https://milestone-four-noir-digital.s3.us-east-2.amazonaws.com/static/wireframes/Testimonial-Phone.png) 

### Features

- User is able to view all the art by clicking the "work" on the navbar.

- User is able to login or register by clicking "login/register" on the navbar and filling out the form.

- User is able to read about a specific art piece by clicking its image in the work page. 

- User is able to read a news article by clicking "news" on the navbar and selecting an story.

- User is able to read about the site by clicking on "about" on the navbar.

- User is able to buy a product by clicking "add to cart" and checking out.


#### Technologies Used

- HTML - HTML was used to build the structure of the site.

- CSS - CSS was used to style the site.

- Git - Git was used for version control.

- Bootstrap - The project uses bootstrap for the navbar, modals, and responsiveness.

- jQuery - The project uses JQuery to simplify DOM manipulation.

- Google Fonts - The project uses Google fonts in order to use the Roboto Font.

- Font Awesome - The project uses Font Awesome in order to display various icons for social media and the hamburger menu in mobile view.

- Python - This project uses python to execute the logic.

- Django - Django was used to create the website.

- AWS S3 - AWS was used to store images and other static files using a postgresql database.

#### Testing

Unit Testing was used as well as manual testing using [W3 Validator](https://validator.w3.org/).  I used [Responsinator](https://www.responsinator.com/) to check the responsiveness of my site on various devices.

Automated testing using Jasmine was not used as there is little JavaScript logic in the site. 

Automated testing using unittest was used to test the routes and connected templates. It can be run by typing the following in the terminal.
```
python3 test_run.py
```

##### Manual Testing

Manual testing was done following the user stories mentioned above.


- **Signup a User** - User is able to Signup by clicking Signup on the navbar and filling out the form. They will then be redirected to the home page. 

- **Login a User** - User is able to login by clicking login on the navbar and filling out the form. They will then be redirected to the home page.

#### Deployment to Heroku

**Name: Digital Noir**

**URI:**https://milestone-four-noir-digital.herokuapp.com/

This website was deployed through Heroku directly from the master branch.  The difference between the development version and deployment version are little to none. The database is stored on AWS and is set up through Heroku. Using a Procfile and a requirments.txt file Heroku installs the required software in order to run the site. To get the site to run with Heroku do the following to create the required files.

- **Creating Requirments.txt** - run the following in the terminal.
 ``` 
sudo pip3 freeze --local > requirements.txt
 ```

- **Creating Procfile** - run the following in the terminal.
```
echo web: python > Procfile 
```
- **Login in to Heroku** - Through the terminal you can use to login and to check the app.
```
heroku login
heroku apps
```
 - **Initialize git** - Initialise git and set the remote for Heroku.
```
git init
heroku git:remote -a milestone-four-noir-digital
```
- **Push to Heroku** - Finally push to Heroku.
```
git push heroku master
```
- **Don't Forget!** - In heroku's settings under *Config Vars* set ** DISABLE_COLLECTSTATIC to 1 ** and all other keys to their values.



#### Things to do in the Future

- Create more photos for the work page.

#### Credits

- Specials Thanks to the student slack channels, my mentor and stack overflow.❤️