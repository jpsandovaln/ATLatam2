<h1>Machine Learning App with Docker</h1>
Follow this readme to put the machine learning app into a docker container. Feel free to optimize the docker instructions inside DOCKERFILE, docker-compose.yml and other files.

<h2>- Docker Installation on Windows(Oct-2021)</h2>

To use docker and docker-compose we need to install docker desktop from the bellow link.
We should follow the installation instructions and check if our machine meets the specified requirements described in the page.

https://docs.docker.com/desktop/windows/install/

We need to have our windows updated to avoid problems with docker:
"Docker only supports Docker Desktop on Windows for those versions of Windows 10 that are still within Microsoft’s servicing timeline".

BIOS-level hardware virtualization support must be enabled in the BIOS settings. If your computer does not have this feature activated, the installer will ask you to let it enable virtualization, you must allow it.

The installation wizard will ask you to enable WLS (Windows Linux Kernel Subsystem) or  to Enable Hyper-V Windows Features.
For WLS installation, wizard will tell you to download it from microsoft page
https://docs.microsoft.com/en-us/windows/wsl/install-manual#step-4---download-the-linux-kernel-update-package

When Docker installation is completed it could ask you to restart your PC to apply user permission settings, click restart.
Once docker is ready you can follow the Quick Start Guide to verify everything is ok.

**********************************************************************************

<h2>- Dockerize Machine Learning App</h2>

The machine learning module contain the necessary files to dockerize it, this files are:

**DOCKERFILE**, where we define the list of commands to prepare an OS where our app is going to run, install required dependencies, copy the necessary files to run our application and commands to start up our application. In other words where we define an image of the application.

**docker-compose.yml**, where we specify the services we are going to use and what images we will use to build his services, how this services will interact and other options.

**requirements.txt**, where all dependencies used to build the image specified in the DOCKERFILE are listed.

As well as the necessary configurations in the settings.py file.

To mount the image of the machine learning app and the postgres db image we open a CDM at this level (where those files are) and run the next command:

**docker-compose up -d --build**

We will se how the services are created (postgres, machine learning app and default network to allow communication between services)

Now we should have our postgres service listening at 5432 port and machine learning app at 8000 port.

To use our dockerized application we need to make django migrations to the data base and apply this migrations. We do this by runing the following commands:

**docker-compose run app python manage.py makemigrations**

**docker-compose run app python manage.py migrate**

Here we specify to docker compose to run in the app service (app was the name we define for this service in docker-compose.yml) the command to start up the Django Development Server (the one we use at this time when writing this document).

After this, the machine learning app should be running inside a container and available for us to consuming its functionalities. 
