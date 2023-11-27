import argparse
import subprocess

# Define the command-line parser
parser = argparse.ArgumentParser(description="Rescueme - A diagnostic tool")

# Add the '-prediagnostics' flag
parser.add_argument("-prediagnostics", action="store_true", help="Run pre-diagnostics")
parser.add_argument("-diagnostics", action="store_true", help="Run diagnostics")

# Parse the command-line arguments
args = parser.parse_args()

# Define and implement the functionality for the -prediagnostics subcommand
def prediagnostics():
                    try:
                        subprocess.run(["python", "Modules/prediagnostics.py"])
                    except Exception as e:
                        print(f"Error calling script.py: {str(e)}")
print("Running pre-diagnostics...")

def diagnostics():
    try:
        subprocess.run(["python", "Modules/top.py"])
    except Exception as e:
        print(f"Error calling script.py: {str(e)}")
    
# Add your pre-diagnostics code here


def main():
    if args.prediagnostics:
        prediagnostics()
    elif args.diagnostics:
        diagnostics()
    else:
        print("Diagnostic cann't Run")

if __name__ == "__main__":
    main()