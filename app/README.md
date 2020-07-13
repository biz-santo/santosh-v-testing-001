Author: SV
Date: 12/07/2020
Version: 1.0

This is Simple Hello World Python app written in Flask

I have kept all the codes in app folder for simplicity including Dockerfile and kubernetes deployment file.

1.. Git clone this source code

2.. Change to app directory

3.. Tag your docker image (Optional)
    	docker build --tag hello-python:latest .
      
4.. Build docker file
    docker build -f Dockerfile -t hello-python:latest .

5.. Run the Docker Container
      Docker run —publish 8080:5000 —detach -name ee1 hello-python:latest
      
Note: ee1 is just a name, you can replace with any names

6.. Test your Application on Docker
    <server_name or localhost>:port
Note: here port is 8080, you can run step 5 multiple times with different port to create multiple version of same file

7.. Once your application is running on Docker, Now you can run it on K8S

8... Change to app directory and "kubectl apply -f deploy.yaml"

9.. Check number of Pods using commmand "kubectl get pods"

10.. Check number of services using command "kubectl get services"

11.. You can get url address of the service minikube service hello-python --url

12.. You can also expose your application using "kubectl expose deployment/hello-python --type="NodePort" --port 8080"

13.. You can also Check your hello-python app  using command "minikube service my-service"
