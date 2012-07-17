import shutil
import os
import time
import datetime
import math
import urllib.request
from array import array
from random import random

def getUrl(keepGoing, http):
    if(keepGoing == True):
        formattedWrong = True
    else:
        formattedWrong = False
    while(formattedWrong):
            http = str(input('Please Enter A Valid Url :'))
            if( 'http://' in http):
                formattedWrong = False
    
    x = 'http://www.asrs.org/extranet/MeetingScheduler/ExportOvation/0'
    y = 'http://www.asrs.org/extranet/MeetingScheduler/ExportPosters/0'
    z = 'http://www.asrs.org/extranet/MeetingScheduler/ExportFilms/0'
    print('processing files')
    onlineScrape = urllib.request.urlopen(http);
    myfile = onlineScrape.readlines()
    onlineScrape.close()
    
    directory = os.getcwd()+'\\'+((http.split('/')[-1]))
    if not os.path.exists(directory):
        os.makedirs(directory)
    httplogfile = directory +'\\'+((http.split('/')[-1])+'.txt')
    
    file = open( httplogfile ,'w');
    for line in myfile:
        try:
            line = line.decode('utf-8')
            if('src=\"' in line):
                for i in range(4,len(line)-1):
                    if((str(line[i-4]+line[i-3]+line[i-2]+line[i-1]+line[i]) == 'src=\"')or(str(line[i-4]+line[i-3]+line[i-2]+line[i-1]+line[i]) == 'SRC=\"')):
                        for j in range(i+1, len(line)-1):
                            if((line[j] == '\'')or(line[j] == '"')):
                                file.write(str(line[i+1:j])+'\n')
                                break
        except UnicodeDecodeError:
            pass
    for line in myfile:
        try:
            line = line.decode('utf-8')
            if(('src=\'' in line)or('SRC=\'' in line)):
                for i in range(4,len(line)-1):
                    if((str(line[i-4]+line[i-3]+line[i-2]+line[i-1]+line[i]) == 'src=\'')or(str(line[i-4]+line[i-3]+line[i-2]+line[i-1]+line[i]) == 'SRC=\'')):
                        for j in range(i+1, len(line)-1):
                            if((line[j] == '\'')or(line[j] == '"')):
                                file.write(str(line[i+1:j])+'\n')
                                break
        except:
            pass
    for line in myfile:
        try:
            line = line.decode('utf-8')
            if(('href\"' in line)or(('HREF\"' in line))):
                for i in range(5,len(line)-1):
                    if((str(line[i-5]+line[i-4]+line[i-3]+line[i-2]+line[i-1]+line[i]) == 'href\"')or(str(line[i-5]+line[i-4]+line[i-3]+line[i-2]+line[i-1]+line[i]) == 'HREF=\"')):
                        for j in range(i+1, len(line)-1):
                            if((line[j] == '\'')or(line[j] == '"')):
                                file.write(str(line[i+1:j])+'\n')
                                break
        except:
            pass
    for line in myfile:
        try:
            line = line.decode('utf-8')
            if(('href=\'' in line)or('HREF=\'' in line)):
                for i in range(5,len(line)-1):
                    if((str(line[i-5]+line[i-4]+line[i-3]+line[i-2]+line[i-1]+line[i]) == 'href\'')or(str(line[i-5]+line[i-4]+line[i-3]+line[i-2]+line[i-1]+line[i]) == 'HREF=\'')):
                        for j in range(i+1, len(line)-1):
                            if((line[j] == '\'')or(line[j] == '"')):
                                file.write(str(line[i+1:j])+'\n')
                                break
        except:
            pass
    for line in myfile:
        try:
            line = line.decode('utf-8')
            if('href' in line):
                #print('href in line')
                for i in range(3,len(line)-1):
                    if(line[i-3]+line[i-2]+line[i-1]+line[i] == 'href'):
                        for j in range(i+3, len(line)-1):
                            if((line[j] == ('"'))or(line[j] == ('?'))or(line[j] == ('#'))or(line[j] == ('\''))):
                                file.write(line[i+3:j]+'\n')
                                break;
        except:
            pass
    file.close()
    if(keepGoing == True):
        download(httplogfile,directory, http)

def download(fileName, wd, ext):
    myFile = open(str(fileName),'r')
    readFile = myFile.readlines()
    myFile.close()
    errorLog = open(wd+'\\errorLog.txt','w')
    for line in readFile:
        if(line[0] == '/'):
            line = ext[1:] + line
        if((line[0] != 'h')and(line != '')and (line != '\n')):
            line = 'h' + line
        if('javascript:' in line):
            line = ''
        if('?' in line):
            x = line.index('?')
            line = line[:x]
        if(line[-3:-1] == '/\n'):
            getUrl(False,line[:-2])
        tryPath = ''
        try:
            if('.jpg' in line):
                tryPath += wd+'\\JPG'
            elif('.JPG' in line):
                tryPath += wd+'\\JPG'
            elif('.jpeg' in line):
                tryPath += wd+'\\JPG'
            elif('.png' in line):
                tryPath += wd+'\\PNG'
            elif('.PNG' in line):
                tryPath += wd+'\\PNG'
            elif('.mp4' in line):
                tryPath += wd+'\\MP4'
            elif('.MP4' in line):
                tryPath += wd+'\\MP4'
            elif('.gif' in line):
                tryPath += str(wd)+'\\GIF'
            elif('.GIF' in line):
                tryPath += str(wd)+'\\GIF'
            elif('.aspx' in line):
                tryPath += str(wd)+'\\ASPX'
            elif('.ASPX' in line):
                tryPath += str(wd)+'\\ASPX'
            elif('.asp' in line):
                tryPath += str(wd)+'\\ASP'
            elif('.ASP' in line):
                tryPath += str(wd)+'\\ASP'
            elif('.Png' in line):
                tryPath += str(wd)+'\\PNG'
            elif('.js' in line):
                tryPath += str(wd)+'\\JS'
            elif('.JS' in line):
                tryPath += str(wd)+'\\JS'
            elif('.ico' in line):
                tryPath += str(wd)+'\\ICO'
            elif('.ICO' in line):
                tryPath += str(wd)+'\\ICO'
            elif('.css' in line):
                tryPath += str(wd)+'\\CSS'
            elif('.CSS' in line):
                tryPath += str(wd)+'\\CSS'
            elif('.htm' in line):
                tryPath += str(wd)+'\\HTML'
            elif('.html' in line):
                tryPath += str(wd)+'\\HTML'
            elif('.HTM' in line):
                tryPath += str(wd)+'\\HTML'
            elif('.HTML' in line):
                tryPath += str(wd)+'\\HTML'
            elif('.php' in line):
                tryPath += str(wd)+'\\PHP'
            elif('.PHP' in line):
                tryPath += str(wd)+'\\PHP'
            elif('.flv' in line):
                tryPath += str(wd)+'\\FLV'
            elif('.FLV' in line):
                tryPath += str(wd)+'\\FLV'
            elif('.pdf' in line):
                tryPath += str(wd)+'\\PDF'
            elif('.PDF' in line):
                tryPath += str(wd)+'\\PDF'
            elif('.com' in line):
                tryPath += str(wd)+'\\EXE'
            else:
                tryPath += str(wd) +'\\MISC'
            if not os.path.exists(tryPath):
                os.makedirs(tryPath)
            urllib.request.urlretrieve(line, tryPath + '\\' + line.split('/')[-1].replace('\n',''))
        except ValueError:
            print('\nValue Error Accepting Href '+ line+'\n Log Record made in errorLog.txt')
            errorLog.write(line)
            pass
        except IOError:
            print('\nIOError Accepting Href '+ line+'\n Log Record made in errorLog.txt')
            errorLog.write(line)
        except TypeError:
            print('\nTypeError Accepting Href '+ line+'\n Log Record made in errorLog.txt')
            errorLog.write(line)
    errorLog.close()
    
getUrl(True,'')
