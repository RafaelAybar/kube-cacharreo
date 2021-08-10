terraform {
  required_version = ">= 0.12"
    required_providers {
            google = {
                source = "hashicorp/google"
                version = "3.75.0"
            }
    }
}

provider "google" {
  credentials = file("cambialaruta/application_default_credentials.json")
  project = "idproyecto"
  region = "europe-west4"
  zone = "europe-west4-c"
}

resource "google_compute_instance" "cks_master" {
  name         = "cks-master"
  machine_type = "e2-medium"
  tags = ["cksmaster"]

  boot_disk {
    initialize_params {
      image = "ubuntu-os-cloud/ubuntu-1804-lts"
      size = 50
    }
  }
   network_interface {
    network = "default"
    access_config {}
   }

    metadata = {
        ssh-keys = "user:${file("~/.ssh/id_rsa.pub")}"
        }


}

resource "google_compute_instance" "cks_worker" {
  name         = "cks-worker"
  machine_type = "e2-medium"
  tags = ["cksworker"]
  boot_disk {
    initialize_params {
      image = "ubuntu-os-cloud/ubuntu-1804-lts"
      size = 50
      }
  }
    metadata = {
      ssh-keys = "user:${file("~/.ssh/id_rsa.pub")}"
    }

  network_interface {
        # A default network is created for all GCP projects
        network = "default"
        access_config {}
    }
}

resource "google_compute_firewall" "web-rule" {
  name = "http"
  network = "default"
  target_tags = ["cksmaster","cksworker"]
  allow {
    protocol = "tcp"
    ports = ["80","443"]
  }

  source_ranges = ["0.0.0.0/0"]
}