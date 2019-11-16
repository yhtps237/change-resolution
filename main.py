#!/usr/bin/python3
import subprocess as sb

main_command = 'xrandr'
command1 = 'cvt 1920 1080 60'
command2 = 'xrandr --newmode'
command3 = 'xrandr --addmode'
command4 = 'xrandr --output'

data = sb.check_output(main_command, shell=True).decode()
device_name = data.split('connected')[0].split()[-1]

data = sb.check_output(command1, shell=True).decode()
cvt_data = data.split('Modeline ')[1].split(r'\n')[0]
resolution = cvt_data.split()[0]

command2 = command2 + ' ' + cvt_data 
data = sb.call(command2, shell=True)

command3 = command3 + ' ' + device_name + ' ' + resolution
sb.call(command3, shell=True)

command4 = command4 + ' ' + device_name + ' --mode ' + resolution.replace('"','')
sb.call(command4, shell=True)
