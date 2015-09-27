#!/bin/bash
sudo docker stop marketplace_instance
sudo docker rm marketplace_instance
sudo docker run --name marketplace_instance -d -p 5000:5000 -i -t marketplace_img
