import tkinter as tk 
import pandas as pd 
import matplotlib.pyplot as plt  
from tkinter import filedialog, messagebox 
from PIL import Image, ImageTk
from abc import ABC, abstractmethod 

# Abstract class defining the structure of survey objects
# The AbstractSurvey and StudentSurvey classes represent the concept of surveys in the code. 
# AbstractSurvey is an abstract class, and StudentSurvey is its concrete implementation.
class AbstractSurvey(ABC):  # Class (Abstract class)
    @abstractmethod
    def analyze_data(self):  # Abstract method
        pass

# Concrete implementation of the survey class
# StudentSurvey inherits from AbstractSurvey, demonstrating inheritance.
# The AbstractSurvey class contains an abstract method analyze_data, which must be implemented by its subclasses.
class StudentSurvey(AbstractSurvey):  # Class (Inheritance)
    def __init__(self, dataset_path):
        self.dataset_path = dataset_path
        # Load survey data from a CSV file
        self.data = self.load_data()  # Object

    # Method to load survey data from a CSV file
    def load_data(self): 
        try:
            # Read CSV file into a DataFrame
            data = pd.read_csv(self.dataset_path)  
            return data
        except FileNotFoundError:
            print(f"Error: File '{self.dataset_path}' not found.")
            return None

    # Method to analyze the survey data and generate visualizations
    # The analyze_data method is polymorphic, as its behavior varies depending on the specific implementation in StudentSurvey.
    def analyze_data(self):  
        if self.data is None:
            return

        # Print basic statistics about the survey data
        print("Basic Statistics:")

        # Create subplots for visualization
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(5, 8))

        # Plot count of students for each existing brand
        existing_brand_count = self.data['Exst_brand'].value_counts()
        print("\nExisting Brand:")
        print(existing_brand_count)
        existing_brand_count.plot(kind='bar', ax=ax1)
        ax1.set_title('Existing Brand')
        ax1.set_xlabel('Brand')
        ax1.set_ylabel('Count')
        ax1.tick_params(axis='x', labelrotation=0)  

        # Plot count of students for each preferred brand
        prefer_brand_count = self.data['Prefer_brand'].value_counts()
        print("\nPreferred Brand:")
        print(prefer_brand_count)
        prefer_brand_count.plot(kind='bar', ax=ax2)
        ax2.set_title('Preferred Brand')
        ax2.set_xlabel('Brand')
        ax2.set_ylabel('Count')
        ax2.tick_params(axis='x', labelrotation=0)

        # Adjust layout to prevent overlap
        plt.tight_layout()

        # Save plots as image files
        self.save_plot(ax2, 'brand_count_plot.png')

        # Show the plots
        plt.show()

    # Method to save a plot as an image file
    def save_plot(self, ax, filename): 
        fig = ax.get_figure()
        fig.savefig(filename)

    # Method to generate a report and save it as a text file
    def generate_report(self):
        if self.data is None:
            return

        # Generate a report and save it as a text file
        report_text_filename = "survey_report.txt"
        with open(report_text_filename, 'w') as report_file:
            report_file.write("Survey Report\n\n")

            report_file.write("Basic Statistics:\n")
            report_file.write(str(self.data.describe().round(3)) + '\n\n')

            report_file.write("Count of Students for Each Existing Brand:\n")
            existing_brand_count = self.data['Exst_brand'].value_counts()
            report_file.write(str(existing_brand_count.reset_index(drop=True)) + '\n\n')

            report_file.write("Count of Students for Each Preferred Brand:\n")
            prefer_brand_count = self.data['Prefer_brand'].value_counts()
            report_file.write(str(prefer_brand_count.reset_index(drop=True)) + '\n\n')

            report_file.write("Plot of Preferred Brand Count saved as 'brand_count_plot.png'\n")

        print(f"Report generated. Text saved as '{report_text_filename}'.")

# Function to browse and upload a CSV file for analysis
# Objects of the StudentSurvey class are created in the browse_file function.
def browse_file():
    file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    if file_path:
        survey = StudentSurvey(file_path)  # Object
        survey.analyze_data()
        survey.generate_report()

# Function to exit the program
def ext_program():  # The ext_program function encapsulates the functionality of exiting the program.
    return exit()

# Main function to create the GUI window and handle user interaction
def main():
    width, height = 450, 250
    root_window = tk.Tk()
    root_window.title("Mobile Market Analysis for Student") 
    root_window.minsize(width, height)
    root_window.configure(bg='white')  # Set the background color of the window to white

    # Load image
    image = Image.open("background.jpg")  
    image = image.resize((width, height), Image.LANCZOS)
    bg_image = ImageTk.PhotoImage(image)

    # Create a canvas that fills the window
    canvas = tk.Canvas(root_window, width=width, height=height)
    canvas.pack(fill="both", expand=True)
    # Add the image to the canvas
    canvas.create_image(0, 0, image=bg_image, anchor="nw")

    # Frame to position widgets within the image
    main_windows = tk.Frame(canvas, bg='#091E33', width=10, height=10)  
    main_windows.place(relx=0.3, rely=0.3, anchor='n')  # Adjust positioning as needed

    # Welcome message (placed within the frame)
    label = tk.Label(main_windows, text="Mobile Student Survey Analysis", font=("Arial", 10, "bold"), bg='#091E33', fg='white')
    label.pack(pady=10)
    # Button styling
    button_style = {'font': ("Arial", 9,"bold"), 'bg': '#e0e0e0', 'activebackground': '#cccccc'}
    # Upload CSV File button
    upload_button = tk.Button(main_windows, text="Upload CSV File", command=browse_file, width=20, **button_style)
    upload_button.pack(pady=10)
    # Exit button
    ext_button = tk.Button(main_windows, text="Exit", command=ext_program, width=20, **button_style)
    ext_button.pack(pady=10)

    root_window.mainloop()

if __name__ == "__main__":
    print("Noted:")
    print("CSV Format: Name, Age, Gender, Exst_brand, Exst_model, Prefer_brand, Prefer_model")
    messagebox.showinfo("NOTE!", "CSV Format: \n\nName, Age, Gender, Exst_brand, Exst_model, Prefer_brand, Prefer_model")
    main()


# Concrete implementation of the survey class
class StudentSurvey(AbstractSurvey):  # Class (Inheritance)
    def __init__(self, dataset_path):
        # Implementation details...
