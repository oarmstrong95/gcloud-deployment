import subprocess

def run_command(command):
    """
    Executes a shell command and prints the output.

    Args:
        command (str): The shell command to be executed.

    Raises:
        CalledProcessError: If the command execution fails.

    Returns:
        None
    """
    result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print(result.stdout.decode())
    if result.stderr:
        print(result.stderr.decode())

# Define your variables
project_id = 'gcloud-deployment-435313'
image_name = 'gclouddeployment'
region = 'europe-west2'
artifact_registry = f'europe-west2-docker.pkg.dev/{project_id}/gcloud-deployment/{image_name}'

# Build the Docker image
build_command = f'docker build -t {artifact_registry}:latest .'
run_command(build_command)

# Push the Docker image to Artifact Registry
push_command = f'docker push {artifact_registry}:latest'
run_command(push_command)

# Deploy the Docker image to Cloud Run
deploy_command = f'gcloud run deploy {image_name} --image {artifact_registry}:latest --platform managed --region {region} --allow-unauthenticated'
run_command(deploy_command)
