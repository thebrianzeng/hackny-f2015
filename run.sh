#!/bin/bash
sudo docker rm marketplace_instance
sudo docker run --name marketplace_instance -p 5000:5000 -i -t marketplace_img
