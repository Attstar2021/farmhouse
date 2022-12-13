<h1 align="center">Farmhouse Hotels </h1>

[View the live project here.](https://dream-farmhouse.herokuapp.com/)

This is a hotel booking website website for a small community who wants to have friends online to bring positivity and enjoyment in their lives. It is designed to be responsibe and accessible on a range of devices, making it easy to navigate for potential users and partners.



## User Experience (UX)

![1 (2)](https://user-images.githubusercontent.com/91749477/205432312-15bbdbb5-f4ee-46ed-963e-276673af6de5.jpg)

   ### User stories

  #### First Time Visitor Goals

        1. As a First Time Visitor, I want to easily understand the main purpose of the site and learn more about my commuinty.
        2. As a First Time Visitor, I want to be able to easily navigate throughout the site to find content seamlessly which would 
        be easy to access.
        3. As a First Time Visitor, I want to look for popular profiles to stay in with trends.
        4. As a First Time Visitor, I want to have easy to signup procedure so that, I can create a new account to access all the
        features for signed up users



![4 (2)](https://user-images.githubusercontent.com/91749477/205432347-ea41efda-18dd-4e81-81c1-a0a8edd9a82c.jpg)


![2 (2)](https://user-images.githubusercontent.com/91749477/205432359-7afd2167-42d8-451f-93e9-78ddf29163f2.jpg)

   #### Returning Visitor Goals

        1. As a Returning Visitor user, I want to sign in to the app so that I can access functionality for logged in users
        2.  As a Returning Visitor, I want to stay updated with online friends.
        3. As a Returing Visitor, I want to keep my favorite people so that I can check theirs comments and
         posts through filter options.
        4. As a Returning Visitor, I want to find the their views and thoughts about other places and things.
        5. As a Returning Visitor, I want to find community links.


![3 (2)](https://user-images.githubusercontent.com/91749477/205432363-6bf63bed-7b1f-420c-a14a-cca80176c9c0.jpg)


   
   #### Frequent User Goals
        1.As a Frequent User, I want to check to see what comments I got.
        2. As a Frequent User, I want to check if there are any new intersting posts from anyone easily on top without 
         scrolling through old posts.
        3. As a Frequent User, I want to  create posts so that I can share my thoughts and  with the online community.
        4.  As a Frequent User, I want to view the details of a single post so that I can learn more about it
        

-   ### Design
-   
    -   #### Colour Scheme
        -   The two main colours used are yellow and green.
        -   
    -   #### Typography
        -   The DM Sans font is the main font used throughout the whole website with Sans Serif as the fallback font in case for any reason the font isn't being imported into the site correctly. DM Sans is a clean font, so it is attractive and appropriate.

*   ### Wireframes

    ####  Home Page Wireframe - 
    
    - Main Page
   
![wireframe (2)](https://user-images.githubusercontent.com/91749477/205432409-7f88467a-9bf4-4252-977b-bda54a0a1e4d.png)

   - Sign in & Sign up
   
     
 
 ![sign in screen (2)](https://user-images.githubusercontent.com/91749477/205432455-5dfaa5e4-6151-42c5-ac74-f0f12ffeac01.png)

![sign up screen (2)](https://user-images.githubusercontent.com/91749477/205432461-1284e13a-e183-462f-b55f-0cae24e7c3dc.png)


 ####  Mobile Wireframe 
   - Main Page
    -

   ![mobile (3)](https://user-images.githubusercontent.com/91749477/205433873-23c2918a-6ba3-4dc9-8c89-c5dc4857f493.png)

   
   - Sign in & Sign up
    
![mobile signin (2)](https://user-images.githubusercontent.com/91749477/205432475-e3196884-fce4-4fe9-995b-c660af081a00.png) ![m signup (2)](https://user-images.githubusercontent.com/91749477/205432486-82bb990c-8d80-48d7-bb46-64220f276c0d.png)


## Features

-   Responsive on all device sizes

-   Interactive elements

## Technologies Used

### Languages Used

-   [HTML5](https://en.wikipedia.org/wiki/HTML5)
-   [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
-   [JAVASCRIPT](https://en.wikipedia.org/wiki/JavaScript)
-   [PYTHON](https://en.wikipedia.org/wiki/Python_(programming_language))
-   [POSTGRESQL](https://en.wikipedia.org/wiki/PostgreSQL)

### Frameworks, Libraries & Programs Used

1. [ReactJS:](https://en.wikipedia.org/wiki/React_(JavaScript_library)) 
 - React was use as a front-end JavaScript library for building user interfaces based on UI components.
2. [Django REST Framework:](https://en.wikipedia.org/wiki/Django_(web_framework))
 - DRF was used for back-end API.
4. [ElephentSQL:](https://www.elephantsql.com/)
 -  Elephant was used for SQL queries to create, read, update and delete data directly from my web browser.
5. [ReactBootstrap 4.4.1:](https://getbootstrap.com/docs/4.4/getting-started/introduction/)
 - Bootstrap was used to assist with the responsiveness and styling of the website.  
6. [Hover.css:](https://ianlunn.github.io/Hover/)
 - Hover.css was used on the Social Media icons in the footer to add the float transition while being hovered over.    
7. [Google Fonts:](https://fonts.google.com/)
 - Google fonts were used to import the 'Titillium Web' font into the style.css file which is used on all pages throughout the project.     
8. [Font Awesome:](https://fontawesome.com/)
 - Font Awesome was used on all pages throughout the website to add icons for aesthetic and UX purposes.    
9. [Git](https://git-scm.com/)
 - Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.
10. [GitHub:](https://github.com/)
 - GitHub is used to store the projects code after being pushed from Git
11. [Cloudinary:](https://en.wikipedia.org/wiki/Cloudinary)
 - Cloudinary was used for to upload images and to store, manage, manipulate, and deliver for websites and apps.
12. [JustinMind:](https://en.wikipedia.org/wiki/Justinmind_(software))
 - justinMind was used to make wireframes for this project.
13. [Wix:](https://en.wikipedia.org/wiki/Wix.com)
  - Wix was use to make logo for this website
14. [favicon.io:](https://favicon.io/favicon-converter/)
  -  Favicon.io was used to create favicon for this website.


## Testing

![lighthouse s (2)](https://user-images.githubusercontent.com/91749477/205432554-204f3b46-e175-4283-a75e-02819d0141e6.png)


### Known Bugs

While making this projects many bugs and Errors I've found here are some worth mentioning.

1. There was an error about existing posts forlder, I did force migration of it only using "python manage.py migrate posts"
2. NavBar issue i used fluid class to sort this out.
3. Navlink wiring I debug all code and import linked folder correctly
4. error in playing app in web browser. Error "user_not_found" I change allowed host setting in setting.py in api repo.

![error3 (2)](https://user-images.githubusercontent.com/91749477/205432578-44e9fd0c-3882-472f-bd60-b4eccf517e53.png)

5. Site was resticted so because CORS setting in api repo

### Bugs left unfix

![lighthouse m (2)](https://user-images.githubusercontent.com/91749477/205432530-2bfb74aa-ab4c-4238-8024-3361f2887e99.png)

1. On Mobile site is taking longer then desktop

## Deployment

### GitHub Pages

The project was deployed to GitHub Pages using the following steps...

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/)
2. At the top of the Repository (not top of page), locate the "Settings" Button on the menu.
    - Alternatively Click [Here](https://raw.githubusercontent.com/) for a GIF demonstrating the process starting from Step 2.
3. Scroll down the Settings page until you locate the "GitHub Pages" Section.
4. Under "Source", click the dropdown called "None" and select "Master Branch".
5. The page will automatically refresh.
6. Scroll back down through the page to locate the now published site [link](https://github.com) in the "GitHub Pages" section.


### Heroku

1. Log into Heroku and go to the Dashboard, Click “New” then Click “Create new app” then select "create a new app"

2. Give your app a name and select the region closest to you, then click “Create app”.

3. Open the Settings tab and Add a Config Var DATABASE_URLfrom ElephantSQL, SECRET_KEY from env.py file of your repo and CLOUDINARY_URL from Cloudinary.

4. Open the Deploy tab and in the Deployment method section, search for your repo and click Connect

5. You can click  Enable Automatic Deploys or Manual deploy and then click Deploy Branch.

6. when log showing a successful build then your app ready and deployed.

7. Open app button and your back-end API for this project is up and running


## Credits

### Code

The basic code and theme of the application is influenced by Code Institute's walkthrough project "Moments"

### Media

1. [Pixbay](https://pixabay.com)
2. [code Institute](https://codeinstitute.net/)

### Acknowledgements

With Thanks and regards to Code Institute for getting me this far from it's excellant modules content, its Tutor Assistance team for all help and dedications and my mentor Rohit for his expertise, guidance and support.
