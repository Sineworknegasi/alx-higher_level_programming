#!/bin/bash
#this bash script sends a DELETE request to the URL passed as the first argumentt and display the body of the response
curl -sX DELETE "$1"
