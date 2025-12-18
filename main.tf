resource "aws_s3_bucket" "bad_bucket" {
  bucket = "my-public-bucket-demo"
  acl    = "public-read"
}
