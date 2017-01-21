import json

# read waveform data
fname_in  = '/Users/jayurbain/Dropbox/Scalable Machine Learning/IPTD/Data_For_MSOE/CMFACT/Scaled_J5_Main_Output (2).csv'
fname_out = '/Users/jayurbain/Dropbox/Scalable Machine Learning/IPTD/Data_For_MSOE/CMFACT/Scaled_J5_Main_Output (2).json'
fin = open(fname_in, 'r')
fout = open(fname_out, 'w')

header = {}
X = []
Y = []
data = {}
inHeader=True
jsonHeader = ""
firstWf = True
for line in fin:
    # strip whitespace characters at the end of each line
    line = line.strip()
    # print(line)
    if inHeader is True:
        if line != 'X,Y':
            l = line.split(':,')
            if len(l) == 2:
                header[ l[0] ] = l[1]
        else:
            print( header )
            inHeader = False
            data["Title"] = header["Name"]
            data["TesterID"] = header["Source ID"]
            data["ProductID"] = header["Source ID"]
            data["TestCode"] = header["Source ID"]
            data["SourceCode"] = header["Source ID"]
            data["SerialNumber"] = header["Source ID"]
            # data["TestIDs"]:["CMFACT", "TILT"],  # optional test id
            data["TimeStamp"] = header["TimeStamp"]
            # data["YAxisName"]: "voltage out",  # optional
            # data["XAxisName"]: "time",  # optional
            # data["DigitalStates"]:  {"bit1": "voltage", "bit2": "unit on", …},
            data["N"] = header["Points"]
            # data["ScaleFactor"]=header["TimeStamp"]
            # data["Offset"]=header["TimeStamp"]
            data["CalFactor"] = header["Cal Factor"]
            data["CalOffset"] = header["Cal Offset"]
            # data["SampleRate"]=header["TimeStamp"]
            # data["XZero"]=header["TimeStamp"]
            # data["Info"]=header["TimeStamp"]
            # data["AccuracyInfo"]=header["TimeStamp"]
            # data["UserInfo"]=header["TimeStamp"]
            # data["WaveformType"]=header["TimeStamp"]
            # data["DecimationType"]=header["TimeStamp"]
            # data["DecimationRate"]=header["TimeStamp"]
            # data["FixedInterval"]=header["TimeStamp"]
            fout.write("{header:{\n");
            print( json.dumps( data ))
            fout.write(json.dumps(data))
            fout.write(",\n")
            fout.write("{[\n")
    else:
        if firstWf == True:
            firstWf = False;
        else:
            fout.write(',\n')
        l = [float(e) for e in line.split(',')]
        fout.write( str(l) )
fout.write("]}")
fout.write("}")
fin .close()
fout.close()


