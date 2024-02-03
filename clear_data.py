#!/usr/bin/env python
import subprocess
import shutil
from datetime import datetime
import calendar
################################################################################
get_current_year = int(datetime.now().strftime("%Y"))
def Alarm_free_space():
    process_pic_folder = subprocess.run(["sudo","du", "-sh", "/home/admin1/Pictures/nvdws"],
                        stdout=subprocess.PIPE).stdout.decode("utf-8")
    process_log_folder = subprocess.run(["sudo","du", "-sh", "/var/log"],
                        stdout=subprocess.PIPE).stdout.decode("utf-8")
    disk_usage = subprocess.run(['df','/dev/sda3'],stdout=subprocess.PIPE).\
        stdout.decode(encoding='utf-8').split('\n')[1].split(' ')
    while True:
        try:
            disk_usage.remove('')
        except:
            break
    disk_usage_vol = 'Free_disk_usage:' + str(int((int(disk_usage[3]))/1000000)) \
        + 'Gb '+ ' - Used_%:' + disk_usage[4]
    print("Size of Pictures folder: "+ process_pic_folder)
    print("Size of Log folder: " + process_log_folder)
    print(disk_usage_vol)
    print('')
    print("Which folder do you want to delete? 1-Log_folder   2-Pictures_foler   3-Both")
    print('')
    del_obj = input("Please input the option: ")
    if(del_obj=='1'):
        handle_dir_Log()
    elif(del_obj=='2'):
        handle_dir_Pic()
    elif(del_obj=='3'):
        handle_dir_Log()
        handle_dir_Pic()

def remove_dir(data):
    try:
        directory = "/home/admin1/Pictures/nvdws/"+data
        print(directory)
        shutil.rmtree(directory)
    except:
        pass

def handle_dir_Pic():
    global get_current_year
    current_month = datetime.today().month
    current_day = datetime.today().day
    if current_day < 14:
        if (current_month) > 1:
            remove_dir(str(get_current_year - 1))
            last_month = current_month - 1
            last_day_of_last_month = calendar.monthrange(get_current_year, last_month)[1]
            leave_day_in_last_month = last_day_of_last_month + current_day - 14
            for x in range(1, last_month):
                data = str(x)
                try:
                    if (x < 10):
                        data = str(f"{x:02d}")
                    remove_dir(str(get_current_year)+'/'+data)
                except:
                    pass
            for y in range(1, leave_day_in_last_month):
                data_1 = str(last_month)
                data_2 = str(y)
                try:
                    if (last_month < 10):
                        data_1 = str(f"{last_month:02d}")
                    if (y < 10):
                        data_2 = str(f"{y:02d}")
                    remove_dir(str(get_current_year)+'/'+data_1 + "/" + data_2)
                except:
                    pass
        else:
            remove_dir(str(get_current_year - 1))
            last_year = get_current_year - 1
            leave_day_in_last_month = 17 + current_day
            for x in range(1, 12):
                data = str(x)
                try:
                    if (x < 10):
                        data = str(f"{x:02d}")
                    remove_dir(str(last_year)+'/'+data)
                except:
                    pass
            for y in range(1, leave_day_in_last_month):
                data_2 = str(y)
                try:
                    if (y < 10):
                        data_2 = str(f"{y:02d}")
                    remove_dir(str(last_year)+'/12' + "/" + data_2)
                except:
                    pass
    else:
        remove_dir(str(get_current_year - 1))
        for x in range(1, current_month):
            data = str(x)
            try:
                if (x < 10):
                    data = str(f"{x:02d}")
                remove_dir(str(get_current_year)+'/'+data)
            except:
                pass
        if (current_day == 14):
            leave_day_in_current_month = current_day - 13
        else:
            leave_day_in_current_month = current_day - 14
        for x in range(1, leave_day_in_current_month + 1):
            data_1 = str(current_month)
            data_2 = str(x)
            try:
                if (current_month < 10):
                    data_1 = str(f"{current_month:02d}")
                if (x < 10):
                    data_2 = str(f"{x:02d}")
                remove_dir(str(get_current_year)+'/'+data_1+ "/" +data_2)
            except:
                pass

def handle_dir_Log():
    for x in range(1,31):
        try:
            directory_1 = "/var/log/nvdws.log."+str(x)+".gz"
            subprocess.call(["sudo","rm", directory_1])
            directory_2 = "/var/log/nvdws.log."+str(x)
            subprocess.call(["sudo","rm", directory_2])
        except:
            pass
    try:
        subprocess.call(["sudo","rm", "/var/log/nvdws.log"])
    except:
        pass

Alarm_free_space()