import sys
import subprocess

#remove previous results
if os.path.exists('AMIRIS.FameResult.pb'):
  os.remove('AMIRIS.FameResult.pb')


# Create command arguments
args = ['java'] + sys.argv[1:]
       
print(f"Executing command '{' '.join(args)}'")
subprocess.run(args, check=True)   
