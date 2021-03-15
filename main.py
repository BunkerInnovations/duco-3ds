import socket, hashlib
# Global variables
soc = socket.socket()
username = "user"  # Edit this to your username, mind the quotes
pool_address = "51.15.127.80"
pool_port = 2811

print("Starting 3DS Miner, you probably won't get any output") 

while True:
    soc.connect((str(pool_address), int(pool_port)))  # Connect to the server
    server_version = soc.recv(3).decode()  # Get server version
    print("Server is on version", server_version)
    # Mining section
    while True:
        soc.send(bytes("JOB," + str(username) + ",LOW", encoding="utf8"))  # Send job request
        
        # Don't mind the "LOW" for now since it is in an early state
        
        job = soc.recv(1024).decode()  # Get work from pool
        job = job.split(",")  # Split received data to job (job and difficulty)
        difficulty = job[2]
        for result in range(
            100 * int(difficulty) + 1
        ):  # Calculate hash with difficulty
            ducos1 = hashlib.sha1(
                str(job[0] + str(result)).encode("utf-8")
            ).hexdigest()  # Generate hash
            if job[1] == ducos1:  # If result is even with job
                soc.send(
                    bytes(str(result) + "," + ",3DS Miner unstable)", encoding="utf8")
                )  # Send result of hashing algorithm to pool
                feedback = soc.recv(1024).decode()  # Get feedback about the result
                print(feedback)
