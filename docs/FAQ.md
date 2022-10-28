1. if you get into "could not connect to server: Cannot assign requested address Is the server running on host "localhost" (::1) and accepting TCP/IP connections on port 5432?"

docker ps
docker exec -it CONTAINER_ID bash
lsof -i -P -n | grep LISTEN