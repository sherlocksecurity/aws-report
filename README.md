<p align="center">
  <h3 align="center">AWS Report</h3>
  <p align="center">AWS report is a tool to perform security preemptive analysis.</p>

  <p align="center">
    <a href="https://twitter.com/gmdutrax">
      <img src="https://img.shields.io/badge/twitter-@gmdutrax-blue.svg">
    </a>
    <a href="https://travis-ci.org/gmdutra/aws-report">
      <img src="https://travis-ci.org/gmdutra/aws-report.svg?branch=master">
    </a>
    <a href="https://www.gnu.org/licenses/gpl-3.0">
      <img src="https://img.shields.io/badge/License-GPLv3-blue.svg">
    </a>
  </p>
</p>

<hr>

[![asciicast](https://asciinema.org/a/SviEsPkf4Oxr4HkGFAV3Vkjh9.svg)](https://asciinema.org/a/SviEsPkf4Oxr4HkGFAV3Vkjh9)

### Features

* Search iam users based on creation date
* Search buckets public
* Search security group with inbound rule for 0.0.0.0/0
* Search elastic ip dissociated
* Search volumes available

### Install requirements
```
pip3 install -U -r requirements.txt
```

### Enviroment variables

```
IAM_MAX_ACCESS_KEY_AGE default is 60 days.
```

### Examples

```
python3 aws_report.py --s3
python3 aws_report.py --iam
```

### Running in Docker

```
docker run -it -e AWS_ACCESS_KEY_ID=you-access-key -e AWS_SECRET_ACCESS_KEY=you-secret-key gmdutra/aws-report --s3
```

### Contact

```
[+]Email     gmdutra.eu@gmail.com
[+]Linkedin  linkedin.com/in/gmdutra
[+]Twitter   twitter.com/gmdutrax
```
