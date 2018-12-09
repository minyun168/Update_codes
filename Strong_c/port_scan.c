#include<stdio.h>
#include<sys/types.h>
#include<sys/socket.h>
#include<netinet/in.h>
#include<errno.h>
#include<netdb.h>
#include<signal.h>

int main(int argc,char * *argv)
{
	int probeport =0;
	struct hostent *host;
	in err, i, net;
	int startport,endport;
	struct sockaddr_in sa;
	   
	startport = endport = atoi(argv[2]);
	

}
