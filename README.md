# test-api-for-k8s

### App
The application is a very simple Python API, which was made to be deployed into K8s cluster for learning & testing purposes.

### GitHub actions
This repository has a pipeline that automatically builds and pushes the Docker image with the application into DockerHub.
The pipeline is defined in `.github/workflows` directory.
To use it, you need to submit a PR request from a non-protected branch into `main` after editing the application and `.env` files

#### To-Do's:
* automatic image version increment
