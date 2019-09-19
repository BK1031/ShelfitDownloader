# Shelfit Downloader

Edtech is a company that offers a platform to private schools for students to access digital textbooks. They claim to make implementation of ebooks simpler for schools. This platform is known as Shelfit.

## Why Shelfit Sucks
- We are forced to use the Shelfit Reader website
- This website is often glitchy and laggy
- It requires a constant internet connection
- The Shelfit Reader mobile apps barely ever work properly, and downloading books through the app almost always fails

Textbooks shouldn't be so expensive, and should be more accessible to students. This repository contains a simple Python project which downloads the pages from a Shelfit Ebook.

## Getting Started

You're going to want to create a `secret.py` file and add your password like so:
```python
password = "@Vcs1031"
```
This project relies on Selenium for Python, so make sure you have that installed. Replace the existing chromedriver directory with your installation directory.

```python
driver = webdriver.Chrome(r'/Users/bharat/chromedriver')
```

Then replace the existing email address with your own (obviously).

```python
elem.send_keys("bharat.kathi@warriorlife.net")
```

## Running the Program

Before you run the program for the first time, make sure to set the `bookID`, `startPage`, and `lastPage` variables accordingly.

You can locate the `bookID` in the address bar when you open a book in the Shelfit Reader website.

https://reader.shelfit.com/active_textbooks/`bookID`

***Note: You must own the book you are trying to download***

So if you want to download a book that you don't own, get someone else who does own that book to enter in their login information.

## Compiling a PDF

Once you have run the program for your desired book, you should have a bunch of pictures saved in your project directory. Currently, there is no functionality to automatically compile these pictures into one PDF *(PR's are always welcome!)*.

### Windows PDF Generation

 I don't use a windows computer, so I have no idea, but please let me know if you find a simple solution.

### MacOS PDF Generation

1. Select all the photos, and open with Preview.
2. Go to the print console (Cmd+P)
3. Select `Open in Preview`
    - You can also use the `Save as PDF` option, but this doesn't always work for larger books (1000+ pages)
4. A new PDF document should have opened up with all the pages combined. Simply save this where ever you want, and you're good to go!

## License

[![License](http://img.shields.io/:license-mit-blue.svg?style=flat-square)](http://badges.mit-license.org)

**[MIT license](http://opensource.org/licenses/mit-license.php)**  
Copyright 2019 © <a href="http://github.com/BK1031" target="_blank">Bharat Kathi</a>