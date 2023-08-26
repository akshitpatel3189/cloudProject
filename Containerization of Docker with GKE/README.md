# Containerization of Docker with GKE

This project is almost the same as a Containerization with Docker project but I run this project with the use of Google Kubernetes Engine (GKE).


# Technology

**Programming language:** Node Js, Terraform script<br />
**Cloud services:** GKE, Artifact Registry repository, Google Cloud Run, Google Cloud Storage, Cloud Source Repository<br />


# Description:

In this project, I have built two simple microservices from Containerization with the Docker project. Then I create a CI/CD pipeline that deploys the service to GKE. In GKE you will have to create a persistent volume that should be accessed by both containers to store and retrieve file data. You can use GCP services such as Cloud Source Repository to store the source code, Artifact Registry to store the Docker images, and GKE to deploy the images to clusters. Then to start the GKE I created a Terraform script, By running the script from GCP Cloud Shell It will launch the GKE cluster. It will perform the same tasks as Containerization with the Docker project.

### Flow diagram for the system:

![Picture1](https://github.com/akshitpatel3189/cloudProject/assets/65401508/076fbcfe-45f1-45a6-898d-5e615bd66e7c)
