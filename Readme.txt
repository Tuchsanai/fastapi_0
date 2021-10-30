######################################
# Run only first time

#Window  run
python -m venv env
.\env\Scripts\activate
pip install -r -q requirements.txt

# On Unix or MacOS, run:
python -m venv env
source env/bin/activate
pip install -r requirements.txt

# On vscode
#On Unix or MacOS, run: 
virtualenv env
source env/bin/activate
pip install -r requirements.txt
#Windows :  
virtualenv env
.\env\Scripts\activate
pip install -r requirements.txt

######################################
# Run when Install new Library
pip freeze > requirements.txt

######################################
# Activate Environment
.\env\Scripts\activate

# On Unix or MacOS, run:
source env/bin/activate

######################################
# Run fast api 
uvicorn main:app --reload

######################################
# Build Docker
# AWS Access key ID: AKIATSGWRBLJMPMVJGWD
# AWS Secret access key: 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
# Add AWS Key ID and Secret key
pip install awscli
aws configure
    aws_access_key_id=AKIATSGWRBLJMPMVJGWD
    aws_secret_access_key=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
    default_region_name = ap-southeast-1

1. Move File to Docker work Directory
python deployment.py;cd dockerdeployment

2. Build Docker Image
docker build -t elderbackend .

3. Login to ECR
aws ecr get-login-password --region ap-southeast-1 | docker login --username AWS --password-stdin 245263043282.dkr.ecr.ap-southeast-1.amazonaws.com

4. Tag the version
docker tag elderbackend:latest 245263043282.dkr.ecr.ap-southeast-1.amazonaws.com/elderbackend:latest

5. Upload
docker push 245263043282.dkr.ecr.ap-southeast-1.amazonaws.com/elderbackend:latest

######################################
# Create API Server on EC2

# Amazon Linux 2 AMI (HVM), SSD Volume Type - ami-0f511ead81ccde020 (64-bit x86)
# Attach Role: ecr-role 

# Userdata For AMI
##################

#!/bin/bash
sudo yum install docker -y
sudo service docker start
sudo chmod 666 /var/run/docker.sock
aws ecr get-login-password --region ap-southeast-1 | docker login --username AWS --password-stdin 245263043282.dkr.ecr.ap-southeast-1.amazonaws.com
docker pull 245263043282.dkr.ecr.ap-southeast-1.amazonaws.com/elderbackend:latest
docker run -dp 80:8000 245263043282.dkr.ecr.ap-southeast-1.amazonaws.com/elderbackend:latest

##################

# Select SecurityGroup: HTTPSecurityGroup

# Run EC2 instance then wait to see result at http://<public ip address>