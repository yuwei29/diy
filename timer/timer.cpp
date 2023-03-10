#include<stdio.h>
#include<stdlib.h>
#include<time.h>
#include<unistd.h>
#include<windows.h> 
#include<mmsystem.h>
using namespace std;
int main(int argc,char** argv){
	//time_t t1 = time(NULL);
	int duration = 0;
	for(int i=1;i<argc;i++){
		//printf("%d\n",atoi(argv[i]));
		duration = duration*60+atoi(argv[i]);
	}
	sleep(duration);
	//time_t t2 = time(NULL);
	//system("start TrueForceCut.mp3");
	mciSendString("open d:/apps/diy/timer/TrueForceCut.mp3 alias music", NULL, 0, NULL);
    mciSendString("play music wait", NULL, 0, NULL);
    time_t t;   // not a primitive datatype
    time(&t);

    printf("%s", ctime(&t));
	//printf("%ds\n",t2-t1);
}

