terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "4.69.1"
    }
  }
}

provider "google" {
  credentials = file("/home/akshitpatel042/credentials.json")
  project = "a3kubernetes-390219"
  region  = "us-central1"
}

resource "google_container_cluster" "my_cluster" {
  name               = "a3-cluster"
  location           = "us-central1"
  initial_node_count = 1

  node_config {
    machine_type = "e2-micro"
    disk_size_gb = 10
  }
}