variable "region" {
  default = "eu-north-1"
}

variable "cluster_name" {
  default = "my-circleci-cluster"
}

variable "subnet_ids" {
  type = list(string)
}
