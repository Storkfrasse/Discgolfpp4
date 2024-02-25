# **Discgolf booking**

Discgolf is my big hobby and i made this site to spread the sport. The site is targeted at the prospective players who is looking for an new sport to try out

Welcome to Discgolf <a href="https://https://storkfrasse.github.io/Discgolf/index.html" target="_blank" rel="noopener">Discgolf</a>


# Contents

* [**User Experience UX**](<#user-experience-ux>)
    *  [User Stories](<#user-stories>)
    * [Site Structure](<#site-structure>)
    * [Design Choices](<#design-choices>)
    *  [Typography](<#typography>)
    *  [Colour Scheme](<#colour-scheme>)
* [**Features**](<#features>)
    * [**Home**](<#navigation-menu>)
         * [Navigation menu](<#navigation-menu>)
         * [Gallery](<#gallery>)
         * [Footer](<#footer>)
    * [**Contact**](<#contact-us>)
       * Contact details
       * Location map
       * Design Query form
    * [**Future Features**](<#future-features>)
* [**Technologies Used**](<#technologies-used>)
* [**Testing**](<#testing>)
* [**Deployment**](<#deployment>)
* [**Credits**](<#credits>)
    * [**Content**](<#content>)
    * [**Media**](<#media>)
*  [**Acknowledgements**](<#acknowledgements>)


# User Experience

## User Stories

* As a user I want to be able to navigate through the whole site smoothly.
* As a user I want to understand the purpose of the site upon loading it.
* As a user I want to see picture of Discgolf.
* As a user I want to know the history of Discgolf.
* As a user I want to know how to get better on Discgolf.

[Back to top](<#contents>)


## Site Structure

Discgolf has three pages. The [home page](index.html) is the default loading page, [gallery](gallery.html) and [contact](contact.html) pages are all accessible primarily from the navigation menu.


[Back to top](<#contents>)
## Design Choices

 * ### Typography
      The fonts chosen were 'Oswald' for the headings and 'Lato' for the body text.  
     *  'Oswald' was chosen for the headings because i thought i was the best as a heading font. it bold and looks good
      * 'Lato' is used for the body text as it provides a nice contrast to the cursive whilst being easy to read for all.

 * ### Colour Scheme
      I used black and white as a colour scheme for Discgolf. i want to keep it simpel and easy for the eyes. 




[Back to top](<#contents>)
# Features

I want Discgolf to be a inviting website for the user, with an easy navigation menu, easy to look around and you can allways press Discgolf header to get back to the home page. 

## Existing Features  
  * ### Navigation Menu

    * Sited at the top of all the pages in the site, it is fully responsive and contains links to the pages of the site.
    * The logo is clickable with a link back to the home page for enhanced UX.

![Navigation bar image](assets/readme-images/dropdownnavbar.jpg)
[Back to top](<#contents>)

  * ### Gallery

      * Is the second page. located under the navigation menu.
      * A responsively styled grid of images that show a few picture when i'v been out playing. 

![Gallery image](assets/readme-images/gallery.jpg)
[Back to top](<#contents>)


* ### Footer
    
    * Contains social media links. The links open in other tabs.
    * The link are there for the educational side of this project. They would be fixed with the right information if this site was deployed outside of this project.
    
![Footer image](assets/readme-images/footer.jpg)
[Back to top](<#contents>)



* ### Contact

    * It is a simpel contact form, the idea is that the user can put in information and a message with ideas so we can keep in touch.

![Contact page image](assets/readme-images/contact.jpg)
[Back to top](<#contents>)


## Future Features 

* To put more information about courses
* To put in a page for all the different discs, how all the numbers on the disc make it fly diffrent.

[Back to top](<#contents>)

# Technologies Used
* [HTML5](https://html.spec.whatwg.org/) - provides the content and structure for the website.
* [CSS](https://www.w3.org/Style/CSS/Overview.en.html) - provides the styling.
* [Gitpod](https://www.gitpod.io/#get-started) - used to deploy the website.
* [Github](https://github.com/) - used to host and edit the website.

[Back to top](<#contents>)

# Testing

Please refer to [**_here_**](TESTING.md) for the testing results.

[Back to top](<#contents>)

# Deployment

### **To deploy the project**
The site was deployed to GitHub pages. The steps to deploy a site are as follows:
  1. In the GitHub repository, navigate to the **Settings** tab.
  2. Once in Settings, navigate to the **Pages** tab on the left hand side.
  3. Under **Source**, select the branch to **master**, then click **save**.
  4. Once the master branch has been selected, the page will be automatically refreshed with a detailed ribbon display to indicate the successful deployment.

![GitHub pages deployed image](assets/readme-images/deploy.png)

  The live link to the Github repository can be found here - https://github.com/Storkfrasse/Discgolf

### **To fork the repository on GitHub**
A copy of the GitHub Repository can be made by forking the GitHub account. This copy can be viewed and changes can be made to the copy without affecting the original repository. Take the following steps to fork the repository;
1. Log in to **GitHub** and locate the [repository](https://github.com/EwanColquhoun/wawaswoods).
2. On the right hand side of the page inline with the repository name is a button called **'Fork'**, click on the button to create a copy of the original repository in your GitHub Account.
![GitHub forking process image](assets/readme-images/forking.png)

### **To create a local clone of this project**
The method from cloning a project from GitHub is below:

1. Under the repository’s name, click on the **code** tab.
2. In the **Clone with HTTPS** section, click on the clipboard icon to copy the given URL.
![Cloning image](assets/readme-images/clone.png)
3. In your IDE of choice, open **Git Bash**.
4. Change the current working directory to the location where you want the cloned directory to be made.
5. Type **git clone**, and then paste the URL copied from GitHub.
6. Press **enter** and the local clone will be created.


(HEROKU DEPLOYMENT)

### **To deploy the project**
The site was deployed to Heroku pages. The steps to deploy a site are as follows:
  1. On the Heroku page, click on **New**, then create a new app.
  ![Heroku page create new app](assets/readme-image/createnew.jpg)<br>
  2. Then a new window will pop up. Create a name for the deployment, and change location (Europe in my case).<br>
  ![Heroku New app](assets/readme-image/setupname.jpg)<br>
  3. Then click **Create app**.
  4. Once it's created, you will be sent to the page for deployment.
  5. In the deployment page, you will go to **Settings**.
  6. Once in Settings, you will need to add Vars (If you need.). Then you need to **Add buildpack** and add Heroku/python and Heroku/nodejs.<br>
  ![Heroku settings](assets/readme-image/settings.jpg)<br>
  7. Back to deployment. You want to use deployment method **GitHub** and connect to your repository. And search for your project.
  8. At last, you can use manual deploy and click **Deploy Branch**.<br>
  ![GitHub pages deployed image](assets/readme-image/deploy.jpg)

  The live link to the Heroku repository can be found here - https://dashboard.heroku.com/apps/pp3-shadows <br>
  The live link to the GitHub repository can be found here - https://github.com/Storkfrasse/PP3

### **To fork the repository on GitHub**
A copy of the GitHub Repository can be made by forking the GitHub account. This copy can be viewed and changes can be made to the copy without affecting the original repository. Take the following steps to fork the repository;
1. Log in to **GitHub** and locate the [repository](https://github.com/Storkfrasse/PP3).
2. On the right-hand side of the page in line with the repository name is a button called **'Fork'**, click on the button to create a copy of the original repository in your GitHub Account.

### **To create a local clone of this project**
The method for cloning a project from GitHub is below:

1. Under the repository’s name, click on the **code** tab.
2. In the **Clone with HTTPS** section, click on the clipboard icon to copy the given URL.
1. Go to [Codeanywhere](https://app.codeanywhere.com) Log in with GitHub
2. Press the **+** New Workspace 
3. Paste the link.
4. Press **enter** and the local clone will be created.

[Back to top](#contents)


[Back to top](<#contents>)

# Credits
### Content

* The font came from [Google Fonts](https://fonts.google.com/).
* The icons came from [Font Awesome](https://fontawesome.com/).
* The text in the home pages is from [Google](https://google.com).


### Media
* The photos all came from me and my friends
* The photos were compressed using [Compressor](https://compressor.io/).
* The picture on the contact page is from [Google picture search](https://google.com)

[Back to top](<#contents>)

# Acknowledgements
The site was completed as a Portfolio 1 Project piece for the Full Stack Software Developer (e-Commerce) Diploma at the [Code Institute](https://codeinstitute.net/). As such I would like to thank my mentor [Precious Ijege](https://www.linkedin.com/in/precious-ijege-908a00168/),

Michael Sjö 2023.

[Back to top](<#contents>)