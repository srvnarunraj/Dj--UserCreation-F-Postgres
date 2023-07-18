# Signup & Login Application using POSTGRES DB


- <b>Step 1 :</b> Initial Setup of the Project 

- <b>Step 2 :</b> Add the DB Configuration in the settings.py 
         
         - DB : MrDB
         - Schema : registrations

  Query for Table Creation
  
            CREATE TABLE registrations."users" (
                username character varying(15) NOT NULL PRIMARY KEY DEFAULT '',
                password text,
                firstname character varying(15),
                age numeric(3),
                status character varying(10)
            );


  Settings.py
        
            'Postgres_Config' :{
                'ENGINE': 'django.db.backends.postgresql_psycopg2', 
                'NAME': 'MrDB',
                'USER': 'postgres',
                'PASSWORD': 'admin',
                'HOST': 'localhost',
                'PORT': '5432',
                'OPTIONS': {
                    'options': '-c search_path=registrations',
                },
            },
            
         
- <b>Step 3 :</b> Setup the Flask Project,setup routes

              app = Flask(__name__)
              ...

              @app.route('/login', methods=['POST'])
              def login():
                # Get Creds
                username = request.json.get('username')
                password = request.json.get('password')
                cursor,conn = getcursor()

              ...
              ...
              if __name__ == '__main__':
                app.run()
              

            
- <b>Step 4 :</b>  Write Queries & Methods for Insertion and Fetching in the Flask Under the routes

- <b>Step 5 :</b>  Pass input values of the HTML Page from views to the urls where the Flask Project is running

          if request.method == 'POST':       
            URL = 'http://127.0.0.1:5000/login'
            param =  {
                'username' : request.POST['username'],
                'password' : request.POST['password']
            } 
            try:
                response = requests.post(URL,json=param,timeout=300)
                data = response.text
 
After Configuration in urls.py run the project
