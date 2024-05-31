# Hugging_Face_Model_assignment

## Requirement
Create a Docker container that periodically generates reports by fetching data from the Hugging Face model hub, compiling a list of the top 10 downloaded models, and then stopping the container. Ensure the container is easily downloadable and runnable on a Linux machine.

Replace YOUR_HUGGINGFACE_TOKEN with your actual Hugging Face access token.  This will allow the container to access the Hugging Face API and fetch model data. We can get one for free by signing up on their website https://huggingface.co/. Due to securuty concerns I am not adding my personal token here.

## Build the Docker image:

docker build -t huggingface_report .

## Run the container:

docker run -d huggingface_report

This will create a Docker container that runs a cron job every day at midnight. The cron job fetches data from the Hugging Face model hub API, generates a report with the top 10 downloaded models, and saves it to the report.txt file within the container.

