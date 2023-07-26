import calendar
import tkinter as tk

def generate_calendar_string(year, month, workdays):
    cal = calendar.TextCalendar()
    month_days = [day.day if day in workdays else None for day in cal.itermonthdates(year, month)]
    month_name = cal.formatmonthname(year, month, width=0)
    
    cal_string = f"\n{month_name}\nMo Tu We Th Fr Sa Su\n"
    for week in cal.monthdayscalendar(year, month):
        week_str = " ".join(f"{day:2}" if day is not None else "  " for day in week)
        cal_string += week_str + "\n"
    
    return cal_string

def show_calendar():
    output_label.delete(1.0, tk.END)  # Clear previous output
    input_data = input_text.get("1.0", tk.END)
    input_lines = input_data.strip().split("\n")
    
    for line in input_lines:
        try:
            year, months = line.split()
            year = int(year)
            month_range = list(map(int, months.split('-')))
            start_month, end_month = month_range[0], month_range[1] + 1
            
            for month in range(start_month, end_month):
                workdays = []
                cal = calendar.Calendar()
                for day in cal.itermonthdates(year, month):
                    if day.weekday() < 5:  # Monday is 0, Friday is 4 (0 to 4 are workdays)
                        workdays.append(day)
                
                cal_string = generate_calendar_string(year, month, workdays)
                output_label.insert(tk.END, cal_string + "\n")
        except (ValueError, IndexError):
            output_label.insert(tk.END, f"Invalid input: {line}\n")

def reset():
    input_text.delete(1.0, tk.END)   # Clear the input text
    output_label.delete(1.0, tk.END) # Clear the output text

# Create the main window
window = tk.Tk()
window.title("Workdays Calendar")

# Text widget for multiple months and years input
input_label = tk.Label(window, text="Enter the year and month range (e.g., '2023 1-12' or '2022 1-4'):")
input_label.pack(padx=10, pady=5)
input_text = tk.Text(window, height=5, width=30)
input_text.pack(padx=10, pady=5)

# Button to show the calendar
show_button = tk.Button(window, text="Show Calendar", command=show_calendar)
show_button.pack(padx=10, pady=5)

# Label to display the calendar output
output_label = tk.Text(window, height=15, width=40, wrap=tk.WORD, font=("Courier", 12))
output_label.pack(padx=10, pady=10)

# Create a menu
my_menu = tk.Menu(window)
window.config(menu=my_menu)

# Options Menu
options_menu = tk.Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Options", menu=options_menu)
options_menu.add_command(label="Reset", command=reset)

window.mainloop()
