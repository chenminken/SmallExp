#coding: utf-8
#author:陈闽
#date:2017/7/17
#Useage:type the name and telphone number separate by space in file simple.txt
def savetovcf():
    #define a string to read from file 'simple.txt' which in the same path
    string = open('simple.txt','r')
    #define a string array lines
    lines = string.readlines()
    string.close()
    oneline = open('01.vcf','a')
#for each line in lines, process the item in vcf file and save to the file.
    for line in lines:
        name=line.split(' ')[0]
        tel=line.split(' ')[1]
        oneline.write('BEGIN:VCARD\n')
        oneline.write('VERSION:3.0\n')
        FNLog = 'FN:'+name+'\n'
        oneline.write(FNLog)
        TelLog = 'TEL;TYPE=CELL:' + tel
        oneline.write(TelLog)
        oneline.write('END:VCARD\n')
    oneline.close()
#run the function savetovcf
savetovcf()
