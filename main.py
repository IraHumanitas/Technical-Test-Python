import re

def get_user_input(prompt):
    return input(prompt).strip()

def tasks_display():
    tasks = {
        'LG': 'Login',
        'RG': 'Register',
        'US': 'User',
        'EMP': 'Employee',
        'TS': 'Timesheet',
    }
    print("Choose your task:")
    for key, value in tasks.items():
        print(f"{key} - {value}")
    return tasks


def validate_task_input(task_input, tasks):
    pattern = re.compile(r'^[A-Z]{2,}')
    return pattern.match(task_input) and task_input in tasks

def get_time_input():
    while True:
        try:
            time_input = float(input("Masukkan waktu "))
            return time_input
        except ValueError:
            print("Input tidak valid. coba lagi")


def main():
    user_name = get_user_input("Masukkan Nama Anda: ")
    while True:
        try:
            loops = int(get_user_input("Masukkan jumlah task yang akan dikerjakan: "))
            break
        except ValueError:
            print("Input tidak valid. coba lagi")

    tasks = tasks_display()

    total_time = 0

    for i in range(loops):
        print(f"Pengisian task ke-{i+1}:")
        while True:
            task_input = get_user_input("Pilih task dari daftar diatas.Silakan pilih singkatannya: ")
            if validate_task_input(task_input, tasks):
                break
            else:
                print("Tidak valid. Coba lagi")

        time_input = get_time_input()
        total_time += time_input
        print(f"Task '{tasks[task_input]}' dengan waktu {time_input} jam telah ditambahkan.")

    total_days = total_time / 24

    print("\nTotal Working Hours: ")
    print(f"Nama: {user_name}")
    print(f"Total waktu: {total_time} jam atau {total_days: .2f} hari ")

if __name__ == "__main__":
    main()



