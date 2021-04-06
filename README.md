#testSeleniumFinance

####Quick Start Guide

1. Setting up a virtual environment

    After cloning the project, go to the project folder using the terminal and type the following command:
    
    ```
    python3 -m venv venv
    ```
    
    now activate the environment:
    
    ```
    source venv/bin/activate
    ```

2. Django must be installed, along with all required modules and third-party libraries
    
    Type the following command:
    
    ```
   pip3 install -r requirements.txt
   ``` 
      
   Now you need to activate redis, open a second terminal and write the following commands:
   
   ```
   sudo nano /etc/redis/redis.conf
   ```
      
    Inside the file, find the **supervised** directive. This directive allows you to declare an init system for running 
    Redis as a service, giving you more control over how it works. The **supervised** directive is set to **no** 
    by default. Since you are running Ubuntu, which uses the systemd init system, change the value to **systemd**:
    
    ```
    # If you run Redis from upstart or systemd, Redis can interact with your
    # supervision tree. Options:
    #   supervised no      - no supervision interaction
    #   supervised upstart - signal upstart by putting Redis into SIGSTOP mode
    #   supervised systemd - signal systemd by writing READY=1 to $NOTIFY_SOCKET
    #   supervised auto    - detect upstart or systemd method based on
    #                        UPSTART_JOB or NOTIFY_SOCKET environment variables
    # Note: these supervision methods only signal "process is ready."
    #       They do not enable continuous liveness pings back to your supervisor.
    supervised systemd
   ```
      
    This is the only change you need to make to the Redis config file at the moment, so save and close it when you're 
    done editing. Restart the Redis service for the changes to the config file to take effect:
    
    ```
   sudo systemctl restart redis.service
   ```   
   
   Verify that the Redis service is running and active, enter the following command:
   
   ```
    sudo systemctl status redis
   ```
      
    If it starts without errors, when you enter this command, you should get something like the following:
    
    ```
   ● redis-server.service - Advanced key-value store
   Loaded: loaded (/lib/systemd/system/redis-server.service; enabled; vendor preset: enabled)
   Active: active (running) since Wed 2018-06-27 18:48:52 UTC; 12s ago
   Docs: http://redis.io/documentation,
           man:redis-server(1)
   Process: 2421 ExecStop=/bin/kill -s TERM $MAINPID (code=exited, status=0/SUCCESS)
   Process: 2424 ExecStart=/usr/bin/redis-server /etc/redis/redis.conf (code=exited, status=0/SUCCESS)
   Main PID: 2445 (redis-server)
    Tasks: 4 (limit: 4704)
   CGroup: /system.slice/redis-server.service
           └─2445 /usr/bin/redis-server 127.0.0.1:6379
   ```
   
   Here you can see that the Redis service is running and already activated, i.e. it is configured to start at server 
   boot.
   
   
3. Migrations to the database

    Type the command in the terminal:
    ```
    python3 manage.py migrate
    ```
4. Create superuser

    Enter the following command to create a superuser:
    
    ```
   python3 manage.py createsuperuser
   ```
    
    then enter the requested data
 
8. Server start

    Enter the following command in terminal:
    
    ```
   python3 manage.py runserver
   ```   
   
   Now you need to activate celery, to do this open a second terminal and enter the following command:
   
   ```
   celery -A configs worker -l info
   ```
    
    Fine! Project is ready to use.

      

