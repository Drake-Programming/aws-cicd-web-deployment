#!/usr/bin/env python3
import os

import aws_cdk as cdk

from cicd_web_deploy.cicd_web_deploy_stack import CicdWebDeployStack


app = cdk.App()
CicdWebDeployStack(app, "CicdWebDeployStack")

app.synth()
