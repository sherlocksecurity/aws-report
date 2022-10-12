<p align="center">
  <h3 align="center">AWS Report</h3>
  <p align="center">AWS Report is a tool for analyzing amazon resources.</p>

  
  </p>
</p>

<hr>

[![asciicast](https://asciinema.org/a/H2kIjGRo4GvvdRXDZ41DoFXRn.svg)](https://asciinema.org/a/H2kIjGRo4GvvdRXDZ41DoFXRn)

### Features

* Search iam users based on creation date
* Search buckets public
* Search security group with inbound rule for 0.0.0.0/0
* Search elastic ip dissociated
* Search volumes available
* Search AMIs with permission public
* Search internet gateways detached

### Install requirements
```
pip3 install -U -r requirements.txt
```

### Enviroment variables

```
IAM_MAX_ACCESS_KEY_AGE default is 60 days.
```

### Usage

```
Usage: aws_report.py [OPTIONS]

Options:
  --s3          Search buckets public in s3
  --iam         Search iam users based on creation date
  --sg          Search security groups with inbound rule 0.0.0.0
  --elasticip   Search elastic IP not associated
  --volumes     Search volumes available
  --ami         Search AMIs with permission public
  --owner TEXT  Defines the owner of the resources to be found
  --igw         Search internet gateways detached
  --help        Show this message and exit.
```

### Examples

```
python3 aws_report.py --s3
python3 aws_report.py --iam
python3 aws_report.py --owner 296193067842 --ami
```

### Running in Docker

```
docker run -it -e AWS_ACCESS_KEY_ID=you-access-key -e AWS_SECRET_ACCESS_KEY=you-secret-key gmdutra/aws-report --s3
```

