# Trailblazers: COVID-19 VOLUNTEERS
This project **aims** to tackle **COVID-19 crisis**. Due to sudden outbreak of Coronavirus disease, the number of cases is rising at alarming rate. ***We need more of doctors, nurses, assistance workers and paramedics***. India can produce **1.5 lakhs young doctors** if the ***final year medical students*** are authorized to practice. In this *project we are going to direct a route to medical students, whether they are in college, hostels or their homes, they will be able to reach their nearest **COVID-19 Testing Sites***. This project is done using [Python], [Flask], [Django], [HTML], [CSS] and [Geo-location]. We are coming up with this project so as to address the shortage of doctors, nurses, assiatance workers and paramedics. 
[The link to the article where the need of this project is mentioned](https://economictimes.indiatimes.com/industry/healthcare/biotech/healthcare/how-mci-can-save-the-country-tough-covid-19-battle-can-only-be-won-by-our-young-doctors-and-nurses/articleshow/74822637.cms?from=mdr)

This is the form which we have used to take responses (data) of the medical students. https://form.jotform.com/200894710430449  


## INSTALLATION: 
Installed latest version of **Python** from this link [https://www.python.org/downloads/]. Upgrade pip version, if not done by using ['python -m pip install –upgrade pip’] command for windows.
### Packages to be installed
 - clone the `requirements.txt` file from the repository
 
 - execute the command (for windows user).
     ```html
      pip install -r requirements.txt 
     ````
       
 ### Used Packages already installed in IDE **Pycharm** 
  - mentioned in the file `packages`
  
 ## Solution to the errors:
  - In any case if error occurs while execution, the reason and how to solve them is mentioned in a readme file `Errors occurred`
  
 ### Necessary Warnings:
   - The email id used for sending mail after execution of program should have following measures otherwise error may occur:
     1. The email id should be added to enviornment variable in a variable name `EMAIL_USER` and `App password` in `EMAIL_PASS` as used in code
     2. Turn on `less secure app` settings from given link.
     3. Create an `App password` which will be added in enviornmemt variable
  
 ## Execution of Project :
   - clone the files `new_template`, `final_html`, `emails` from the repository
   - In CLI firstly go into the directory where project files are present 
   - Then execute the following command
      -  For Windows and Linux users
           ```python
              python new_template.py
           ````
      - For Mac Users:
          ```python
             python3 new_template.py
          ````
          (if the version of installed python is 3)
  ## Process:
   - As the code is executed, it will send mail to all thode final year medical students whose email-ids are collected.
   - This mail holds the link to the application form and dataset of all COVID-19 Testing-centres in Inida.
   - Student will fill up their details in the form. Form contains location of all the testing centres in their respective states, they will be able to select the location which is most convenient for them to reach and work.
   - For sample purpose we have mentioned only three states(Maharashtra, Uttar Pradesh, Jammu & Kashmir) and their testing centres in the form. 
   - Their response or details will be send to the server of testing center, whichever has been preferred by the students.
   - This way assistance in various means telemedicine, nurses, junior doctors can be fulfilled
   - Medical students will be able to contribute and serve their duties to save the nation.
      
   ## Demo and Execution of project :
   - [To see the working of project click here](https://drive.google.com/open?id=1pkEcsJEUzPTZcC9xJkmPKA5PYdL06YHi)
        
   ## Output received at hospitals server 
   - When hospital of these state are selected by student, automatic responses will be sent to those hospitals which they selected, as per these emails ids:
   1.	Uttar Pradesh:- rajneeshsharma@zhcet.ac.in
   2.	Jammu and Kashmir :- vivekrajs3999@gmail.com
   3.	Maharashtra:- viditaagrawal77@gmail.com

      
        
