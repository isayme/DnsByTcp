# Background #
As you know, China is a "magical" country! The govenment made a firewall named by Great Firewall(**GFW**), the purpose of the GFW is to block some website such as twitter.com, facebook.com and so on.  

One of the method of GFW is DNS poisoning, while this project is to avoid the DNS poisoning. 
 
# About #
This project use python script, but I just have a little skill with python, so the main script is based on [henices/Tcp-DNS-proxy](https://github.com/henices/Tcp-DNS-proxy "henices/Tcp-DNS-proxy").

If you are not a pythoner, maybe you can try my another project [isayme/fuck_dns](https://github.com/isayme/fuck_dns "isayme/fuck_dns") which is also associated with DNS poisoning.

# How To Use #
## Linux User ##
1. change your dns server to 127.0.0.1   
$ vi /etc/resolve.conf  
nameserver 127.0.0.1
2. restart the network $ sudo /etc/init.d/networking restart
3. run the script $ sudo python DnsByTcp.py

## Windows User ##
1. change your dns server to 127.0.0.1, you can use my bat script([cdns.bat](https://github.com/isayme/DnsByTcp/blob/master/README.md "cdns.bat")) and follow its prompt message to change your dns server fastly.
2. run the script $ sudo python DnsByTcp.py