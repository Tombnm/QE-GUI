#include <iostream>
#include <stdio.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <stdlib.h>
#include <arpa/inet.h>
#include <unistd.h>
#include <string.h>
#include <string>

#define		BUFLEN		4096
#define		IP		"10.193.255.27"
#define		PORT		"10000"

int main(int argc,char *argv[]){

int n;
FILE *QEfd = NULL;
int sd,bindsd,listensd,filesd;
char clientFile[BUFLEN];
sockaddr_in serverAddr,clientAddr;
socklen_t clientAddr_len;

serverAddr.sin_family = AF_INET;
serverAddr.sin_port = htons(atoi(PORT));
inet_pton(AF_INET,IP,&serverAddr.sin_addr);



sd = socket(AF_INET,SOCK_STREAM,0);
if(sd < 0){
	perror("socket()");
	exit(1);}

bindsd = bind(sd,(sockaddr*)&serverAddr,sizeof(serverAddr));
if(bindsd < 0){
	perror("bind()");
	exit(1);}

listensd = listen(sd,1);
if(listensd < 0){
	perror("listen()");
	exit(1);}

filesd = accept(sd,(sockaddr*)&clientAddr,&clientAddr_len);
if(filesd < 0){
	perror("accept()");
	exit(1);}

QEfd = fopen("QEFILE.txt","w");
while(1){
	n = recv(filesd,clientFile,BUFLEN,0);
	if(n == 0){
		break;}
	fprintf(QEfd,clientFile);

}

fclose(QEfd);
close(filesd);
close(sd);

FILE *QEFILEfd = NULL;
FILE *QEfilefd = NULL;

QEFILEfd = fopen("QEFILE.txt","r");
QEfilefd = fopen("bfgs.in","w");
char fin[512];
char fout[512];







exit(0);
}
