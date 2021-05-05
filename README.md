# ENSEMBL REST WEB SERVICE  

**API SPECIFICATIONS**  

**Name** : `/gene_suggest`  
**Method** : GET  
**Description** : Get a list of genome display labels from ensembl database  
**Required Parameters** :  
1. **query**  
   Data Type : string  
   Description : any valid string from the display labels  
2. **species**  
   Data Type : string  
   Description : any valid species name  
3. **limit**  
   Data Type : integer  
   Description : the number of suggestions to return  
  
**DEPLOYMENT**
1. For cloud based deployment various PaaS and IaaS providers support Django app deployment eg:- [Heroku](https://devcenter.heroku.com/articles/deploying-python), [PythonAnywhere](https://help.pythonanywhere.com/pages/DeployExistingDjangoProject/), [Amazon Web Services](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create-deploy-python-django.html) etc.    
2. For now, the application has been hosted on Heroku with free resources. https://ensembl.herokuapp.com/gene_suggest?query=brc&species=gorilla_gorilla&limit=10
4. To view the working application with parameters set to 
   * 'brc', 'gorilla_gorilla' and 10 respectively [click here](https://ensembl.herokuapp.com/gene_suggest?query=brc&species=gorilla_gorilla&limit=10).
   * 'ABC', 'homo_sapiens' and 20 [click here](https://ensembl.herokuapp.com/gene_suggest?query=ABC&species=homo_sapiens&limit=20).
6. For deployment on heroku these steps were followed:    
   * A Procfile with  
     `web: gunicorn ensembl.wsgi --log-file -`  
   * A requirements.txt file with all the requirements, including **gunicorn** and **whitenoise**, specifically required for heroku  
     `pip freeze > requirements.txt`  
   * Updating settings.py with  
     `STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'`  
   * On heroku dashboard create a new app and use Github as Deployment method
   * Connect the repository for the app  
   * Deploy branch, if Automatic Deploys is enabled, Heroku automatically deploys on every push to the branch selected  

**SCALABILITY**
1. Python Django is a robust scalable framework for hosting large applications v/s Python Flask.
2. Use of Django's MVT (Model View Template) and OOPs
3. Use of api/utils.py for encapsulating and re-using common functions
4. use of migrations for easier DB deployment and rollbacks.
5. use of caching in case millions of users are trying to call the same API. It will not query the DB again for the same request parameters, but load from memory.
6. the parameters are modularly coded. caching times are coded in  ensembl/settings.py


**TESTING**  
1. For testing, 5 test cases are written in tests.py to test both valid and invalid inputs which can be automated using jenkins CI/CD for every branch/build.
2. Django object oriented TestCase can't be used as it requires read and write permissions to the database.
