% s = serial('COM7','BaudRate',9600,'DataBits',8);
% out = instrfind;
% fclose(s);
% fopen(s);
% voltage=fscanf(s)
% fclose(s);
% 
% function [s,flag]=setupSerial(comPort)
% flag=1;
% s=serial(comPort);
% set(s,"DataBits",8);
% set(s,"StopBits",1);
% set(s,"BaudRate",9600);
% set(s,"parity","none");
% fopen(s);
% a="b";
% while (a~="a")
%     a=fread(s,1,"uchar");
% end
% if(a=="a")
%     disp("serial read");
% end
%     fprintf(s,"%c","a");
%     mbox=msgbox("serial communication setup.");uiwait(mbox);
%     fscanf(s,"%u");
% end
%      



























