# Build and deploy a Containerized Application using GCP

This docker project gives a basic understanding of how to build and deploy Docker containers using GCP.<br />
# Technology<br />

**Database:** Google Cloud Firestore<br />
**Programming language:** Python<br />
**IDE:** VS code<br />
**Cloud services:** Google Cloud Run, Artifact registry/ Container Registry, Firestore<br />

# Discription

There are 2 collections in the database.<br />
<br />
**“Reg”** to  contain **registration data** (Name, Password, Email, Location).<br />
**“state”** to contain **user state** (online, offline, timestamp, etc.) information.<br />
<br />
<br />
<br />
There are 3 containers.<br />
<br />
**Container 1** is responsible for accepting registration details from the frontend and storing it in the backend database.<br />
**Container 2** is responsible for validating the Login information (checking with the database values).<br />
**Container 3** is responsible for extracting state information from the database. E.g.which user is online.<br />
<br />
Once the docker images are built, you need to push those 3 container images to  
the artifact registry repository or container repository. Once it is done, you need to  
deploy those in Cloud Run.<br />
<br />
## Flow Diagram:<br />
![flow_diagram](https://github.com/akshitpatel3189/cloudProject/assets/65401508/af9d8698-5432-4070-8025-9c696f2f50fa)
