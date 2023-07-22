import os
import subprocess
from prettytable import PrettyTable
from tqdm import tqdm
from crontab import CronTab
from crontab import CronSlices


def check_for_existing_cron_job():
    cron = CronTab(user=True)
    for job in cron:
        if job.comment == "delete_temporary_files":
            return True
    return False


def main():
    while 1:
        cron = CronTab(user=True)
        hometable = PrettyTable()
        hometable.field_names = ["", "What do you desire?"]
        hometable.add_row(
            ["1.", "Schedule basic cleanup of temporary files"], divider=True)
        hometable.add_row(["2.", "Schedule cleanup (advance)"], divider=True)
        hometable.add_row(
            ["3.", "See all currently scheduled jobs"], divider=True)
        hometable.add_row(["4.", "Exit"], divider=True)
        print(hometable)
        log_dir = os.path.join(os.path.expanduser("~"), "logs")
        log_file = os.path.join(log_dir, "cron_logs.log")
        if os.path.exists(log_dir) != True:
            print("creating log directory and file at ", log_file)
            os.mkdir(log_dir)
            with open(log_dir, '/myfile.txt', 'w') as fp:
                pass

        xin = ""
        x = 0
        a = 0
        try:
            xin = input("\nEnter Your Choice: \n")
            x = int(xin)
        except:
            print(
                "Unkown Input Detected, please Stick to the above number range, and try again!\n")
            continue
        print(f"\n{'*'*100}\n")

        if x == 1:
            print("Scheduling basic temporary files cleanup:\n\n")
            flag = 1
            while flag:
                schedule = input(
                    "Enter the schedule in comma separated format (1, hourly for repeating job every hour): ")
                password = input("Enter your password: ")
                delete_temporary_cmd = f'echo {password} | sudo find /tmp -type f \( ! -user root \) -atime +3 -delete; echo search for temporary files ran at $(date) >> {log_file}'
                # delete_temporary_cmd=f"echo {password} >> /home/manav/logs/cron_logs.log"
                job = cron.new(command=delete_temporary_cmd)
                schedule = schedule.split(",")
                for i in range(len(schedule)):
                    schedule[i] = schedule[i].strip()
                if schedule[1] == "minute":
                    job.minute.every(schedule[0])
                elif schedule[1] == "hourly":
                    job.hour.every(schedule[0])
                elif schedule[1] == "daily":
                    job.day.every(schedule[0])
                elif schedule[1] == "weekly":
                    job.weekly.every(schedule[0])
                elif schedule[1] == "monthly":
                    job.month.every(schedule[0])
                elif schedule[1] == "yearly":
                    job.year.every(schedule[0])
                else:
                    print("Invalid schedule")
                    continue
                job.enable()
                job.run()
                cron.write()
                print("Job scheduled successfully")
                print("You can see log file at ", log_file, "for more details")
                while 1:
                    a = int(input("\nEnter 1 to redo and 2 to exit to Home\n"))
                    if a == 1 or a == 2:
                        break
                print(f"\n{'*'*100}\n")
                if a == 1:
                    continue
                else:
                    flag = 0
                    break

        elif x == 2:
            print("Scheduling advanced temporary files cleanup:\n\n")
            str = """*    *    *    *    *
│   │     │    │     │
│   │     │    │     │
│   |     │    │     |_________   Day of Week (0 – 6) (0 is Sunday, or use names)
│   │     │    |____________ Month (1 – 12),* means every month
│   │     |______________  Day of Month (1 – 31),* means every day
│   |________________  Hour (0 – 23),* means every hour
|___________________ Minute (0 – 59), * means every minute"""
            print(str, "\n\n")
            flag = 1
            while flag:
                unused_num_days = input(
                    "Please specify the number of days for which the temporary file remain unused that you want to get (enter -1 for all files otherwise enter like +3 for 3 days): ")
                unused_num_days = int(unused_num_days)
                get_root_files = input(
                    "Do you also want to check for all temp files created which are even created by root user/services? (y/n):")
                if get_root_files == "y" or get_root_files == "Y":
                    bool_get_root = True
                else:
                    bool_get_root = False

                schedule = input(
                    "Enter the schedule in cron format (1 * * * * for repeating job every hour): ")
                password = input("Enter your password: ")

                if bool_get_root:
                    delete_temporary_cmd = f'{schedule} echo {password} | sudo find /tmp -atime {unused_num_days} -delete; echo search for temporary files ran at $(date) >> {log_file}'
                else:
                    delete_temporary_cmd = f'{schedule} echo {password} | sudo find /tmp \( ! -user root \) -atime {unused_num_days} -delete; echo search for temporary files ran at $(date) >> {log_file}'

                job = cron.new(command=delete_temporary_cmd)
                schedule_is_valid = CronSlices.is_valid(schedule)
                if schedule_is_valid:
                    job.setall(schedule)
                    job.enable()
                    job.run()
                    cron.write()
                    print("Job scheduled successfully")
                    print("You can see log file at ", os.path.join(
                        log_dir, "cron_logs.log"), "for more details")
                else:
                    print("Invalid schedule")
                    continue
                while 1:
                    a = int(input("\nEnter 1 to redo and 2 to exit to Home\n"))
                    if a == 1 or a == 2:
                        break
                print(f"\n{'*'*100}\n")
                if a == 1:
                    continue
                else:
                    flag = 0
                    break

        elif x == 3:
            print("Scheduled jobs:\n")
            for job in cron:
                print(job)
            while 1:
                a = int(input("\nEnter 1 to redo and 2 to exit to Home\n"))
                if a == 1 or a == 2:
                    break
            print(f"\n{'*'*100}\n")
            if a == 1:
                continue
            else:
                break

        elif x == 4:
            break
        else:
            print(
                "Unkown Input Detected, Please Stick to the above number range, and lets try again ,shall we?\n"
            )


if __name__ == "__main__":
    main()
