How to run this repo using docker:

Using any CLI, run these commands: 
1. docker build -t html-server-image:v1 .
2. docker run -d -p 80:80 html-server-image:v1
3. curl localhost:80 // (to check if it properly runs)