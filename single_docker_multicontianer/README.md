# Build the Docker image
docker build -t print_service:latest .

# First container, port 9090 mapped to the host's port 9090 with a custom message
docker run -d -p 9090:9090 -e PRINT_MESSAGE="Hello from Container 1" print_service:latest

# Second container, port 9091 mapped to the host's port 9091 with another custom message
docker run -d -p 9091:9090 -e PRINT_MESSAGE="Greetings from Container 2" print_service:latest

# Third container, port 9092 mapped to the host's port 9092 with a different custom message
docker run -d -p 9092:9090 -e PRINT_MESSAGE="Welcome from Container 3" print_service:latest


curl -OJ "http://localhost:9090/print"


