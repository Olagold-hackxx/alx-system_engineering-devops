# Attack is the Best Defense :computer:

In this project, I ran two different cyber attacks - Packet sniffing with Wireshark/Tcpdump and Bruteforcing with wordlists using Hydra

## Tasks :page_with_curl:

* **0. ARP spoofing and sniffing unencrypted traffic**
 Your mission is to execute user_authenticating_into_server locally on your machine and, using tcpdump, sniff the network to find my password. Once you find it, paste the password in your answer file. This script will not work on a Docker container or Mac OS, use your Ubuntu vagrant machine or any other Linux machine.
* **1. Dictionary attack**
  Password-based authentication systems can be easily broken by using a dictionary attack (you’ll have to find your own password dictionary). Let’s try it on an SSH account.

    * Install Docker on your machine Ubuntu
    * Pull and run the Docker image sylvainkalache/264-1 with the command docker run -p 2222:22 -d -ti sylvainkalache/264-1
    * Find a password dictionary (you might need multiple of them)
    * Install and use hydra to try to brute force the account sylvain via SSH on the Docker container
    * Because the Docker container is running locally, hydra should access the SSH account via IP 127.0.0.1 and port 2222
    * Hint: the password is 11 characters long
Once you found the password, share it in your answer file..


## Authors :black_nib:
**Abdulqoyyum Aileru** [Github] (github.com/olagold-hackxx)