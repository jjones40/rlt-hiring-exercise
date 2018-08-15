Infrastructure Coding Test
==========================

# Goal

Script the creation of a web server and your choice of database server, and a script to check the server is up.

# Infrastructure Description

For this exercise terraform will be used to build infrastructure: one ec2 instance hosting nginx and mysql instances. Nginx will be configured to host a version.txt file containing one version number, using 1.0.6 from the example below. A checker script written in python is provided to meet the requirements listed below, including running it as a cron job.

# STEPS

0. Choose and cd to a project directory.
   Choose a driectory outside this for keyfiles (in this case directory is one level above project):
   	Secret Key, Secret Access Key, and Host access key.

1. Checkout fork of git project.
	> git clone https://github.com/rootleveltech/rlt-hiring-exercise.git

2. In project directory, initialize for terraform.
	> terraform init

3. Create *.tf file to generate infrastructure. Terraform looks for .tf files in directory.
	create-infrastructure.tf

4. Run plan, referencing keyfile, outside project directory
	> terraform plan -var-file='../rlt-hiring-exercise-keyfiles/terraform.tfvars'
	
5. Apply plan
	> terraform apply -auto-approve -var-file='../rlt-hiring-exercise-keyfiles/terraform.tfvars'

6. Run check script checker.py. Tail log file to verify site up and serving correct version information.
   	> checkey.py
   	> tail -f checker.log

6.1 Checker script can be configured to search for other version numbers by a config file:
	checker.conf

7. Finally clear infrastructure using destroy:
	> terraform destroy -auto-approve -var-file='../rlt-hiring-exercise-keyfiles/terraform.tfvars'

8. An AWS VPC read only account has been setup, and credentials will be provided.

# Prerequisites

You will need an AWS account. Create one if you don't own one already. You can use free-tier resources for this test.

# The Task

You are required to set up a new server in AWS. It must:

* Be publicly accessible.
* Run Nginx.
* Run MySQL, Postgresql, MariaDB, MongoDB
* Serve a `/version.txt` file, containing only static text representing a version number, for example:

```
1.0.6
```

# Mandatory Work

Fork this repository.

* Provide instructions on how to create the server.
* Provide a script that can be run periodically (and externally) to check if the server is up and serving the expected version number. Use your scripting language of choice.
* Alter the README to contain the steps required to:
  * Create the server.
  * Run the checker script.
* Provide us IAM credentials to login to the AWS account. If you have other resources in it make sure we can only access what is related to this test.

Send us an email when you’re done with the repo zipped up. Feel free to ask questions if anything is unclear, confusing, or just plain missing.

# Extra Credit

We know time is precious, we won't mark you down for not doing the extra credits, but if you want to give them a go...

* Use a terraform to set up the server.
* Use a configuration management tool (such as Puppet, Chef or Ansible) to bootstrap the server.
* Put the server behind a load balancer.
* Run run inside docker
* Make the checker script SSH into the instance, check if services are running and start it if it isn't.

# Questions

#### What scripting languages can I use?

Anyone you like. You’ll have to justify your decision. We use Bash, Python and JavaScript internally. Please pick something you're familiar with, as you'll need to be able to discuss it.

#### Will I have to pay for the AWS charges?

No. You are expected to use free-tier resources only and not generate any charges. Please remember to delete your resources once the review process is over so you are not charged by AWS.

#### What will you be grading me on?

Scripting skills, elegance, understanding of the technologies you use, security, documentation.

#### Will I have a chance to explain my choices?

Feel free to comment your code, or put explanations in a pull request within the repo.
If we proceed to a phone interview, we’ll be asking questions about why you made the choices you made.

#### Why doesn't the test include X?

Good question. Feel free to tell us how to make the test better. Or, you know, fork it and improve it!
