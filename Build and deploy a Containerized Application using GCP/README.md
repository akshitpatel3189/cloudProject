# Build and deploy a Containerized Application using GCP

This docker project gives a basic understanding of how to build and deploy Docker containers using GCP.
# Technology

**Database:** Google Cloud Firestore
**Programming language:** Python
**IDE:** VS code
**Cloud services:** Google Cloud Run, Artifact registry/ Container Registry, Firestore

# Discription

There are 2 collections in the database.

**“Reg”** to  contain **registration data** (Name, Password, Email, Location).

**“state”** to contain **user state** (online, offline, timestamp, etc.) information.
<br />
<br />
<br />


There are 3 containers.

**Container 1** is responsible for accepting registration details from the frontend and storing it in the backend database.

**Container 2** is responsible for validating the Login information (checking with the database values).

**Container 3** is responsible for extracting state information from the database. E.g.which user is online.

Once the docker images are built, you need to push those 3 container images to  
the artifact registry repository or container repository. Once it is done, you need to  
deploy those in Cloud Run.

## Flow Diagram:
