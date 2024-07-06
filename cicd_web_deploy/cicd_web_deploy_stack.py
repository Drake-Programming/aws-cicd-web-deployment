from aws_cdk import (
    Stack,
    aws_s3 as s3,
    aws_s3_deployment as s3_deployment,
    aws_cloudfront as cloudfront,
    aws_cloudfront_origins as cloudfront_origins,
    CfnOutput,
)
from constructs import Construct
import os


class CicdWebDeployStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        deployment_bucket = s3.Bucket(self, "WebDeplBucket")

        ui_dir = os.path.join(os.path.dirname(__file__), "..", "web_app")
        if not os.path.exists(ui_dir):
            print("Ui dir not found: " + ui_dir)
            return

        origin_identity = cloudfront.OriginAccessIdentity(self, "OriginAccessIdentity")
        deployment_bucket.grant_read(origin_identity)

        distribution = cloudfront.Distribution(
            self,
            "WebDeploymentDistribution",
            default_root_object="index.html",
            default_behavior=cloudfront.BehaviorOptions(
                origin=cloudfront_origins.S3Origin(
                    deployment_bucket, origin_access_identity=origin_identity
                )
            ),
        )

        s3_deployment.BucketDeployment(
            self,
            "WebDeployment",
            destination_bucket=deployment_bucket,
            sources=[s3_deployment.Source.asset(ui_dir)],
            distribution=distribution,
        )

        CfnOutput(self, "AppUrl", value=distribution.distribution_domain_name)
