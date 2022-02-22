# SummaryAnnotatorTool

Summary Annotation Tool created @IRLab, DAIICT. 

This tool can be used to take user feedback for machine generated summaries. This tool presents the annotator with a News Tile, a Reference summary and a Machine generated summary and expects annotator to give his feedback on following aspects. 
  
  1. Grammatical Correctness
  2. Arrangement of sentences/Flow of information 
  3. Text Quality 
  4. Conciseness 
  5. Exhaustiveness 
  6. Overall Rating (subjective to the annotator)
  
Technologies: 
  1. Python3 
  2. Django 
  3. Postgres
  
To run this project: 

  0. clone the repo and go to intended location 
  
      `cd ~ | git clone https://github.com/TarangRanpara/SummaryAnnotatorTool.git | cd SummaryAnnotatorTool`
      
  1. update the system: 
  
      `sudo apt update`
  
  2. install the required packages 
  
      `sudo apt install python3-pip python3-dev libpq-dev postgresql postgresql-contrib nginx curl`
  
  3. connect to postgresql database 
      
      `sudo -u postgres psql`
      
  4. create postgresql DB 
  
      `CREATE DATABASE annotation_tool;`
      
  5. create postgresql user 
      
      `CREATE USER tarang WITH PASSWORD 'tarang@1998';`
      
  6. set encoding 
  
      `ALTER ROLE tarang SET client_encoding TO 'utf8';`
      
  7. prevent it from reading uncommited transcations 
      
      `ALTER ROLE tarang SET default_transaction_isolation TO 'read committed';`
      
  8. set the timezone 
  
      `ALTER ROLE tarang SET timezone TO 'UTC';`

  9. Grant all privileges to the user 
      
      `GRANT ALL PRIVILEGES ON DATABASE annotation_tool TO tarang;`
  
  10. make python environment 
      
      `python3 -m venv venv`
      
  11. perform installation of the required libs 
      
      `pip install -r requirements.txt`
      
  13. make DB Migrations
  
      `python3 manage.py makemigrations`
      `python3 manage.py migrate`
      
  14. collect static files
      
      `python3 manage.py collectstatic`
      
  13. populate the DB from CSV - do the allocation to your users (new/existing)
      
      `python3 tool_utils.py help`
      
      and choose from one of the below options to perform some utility functions. 
      
          1. bulk_entry [csv_file_name]
          2. bulk_allocate [username] [email] [password] [n]
          3. bulk_allocate_to_existing [username] [n]
          4. export [filename]
          5. work_status
          6. help


  14. Deploy it using gunicorn and nginx. 
      (reference: https://www.codewithharry.com/blogpost/django-deploy-nginx-gunicorn)
          
          
