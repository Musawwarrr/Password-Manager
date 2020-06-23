# Password-Manager
 
I always had the problem of remembering my passwords for all the sites I signed up for and most of them were different than each other. And also being a college student and not wanting to pay for services like LastPass and others, I decided to create my own Password Generator that would only be accessible from my laptop. 

My Password Manager encrypts using Fernet with SHA256 as Hash,salt generated from a random hardware instance and with 100000 iterations. 

My program asks for a master password in the beginning that is used as a key for the encryption algorithm, and if that is forgotten, there is no way to retrieve the passwords. 

Upcoming features:
- Searching through passwords
- Changing passwords, including master
- GUI 
