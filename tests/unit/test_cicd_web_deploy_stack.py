import aws_cdk as core
import aws_cdk.assertions as assertions

from cicd_web_deploy.cicd_web_deploy_stack import CicdWebDeployStack

# example tests. To run these tests, uncomment this file along with the example
# resource in cicd_web_deploy/cicd_web_deploy_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = CicdWebDeployStack(app, "cicd-web-deploy")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
