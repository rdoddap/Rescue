import run_command


def linux_top():
  return run_command.run_command("top -b -n 1")


def linux_ipconfig():
  return run_command.run_command("ipconfig -a")


linux_top()
linux_ipconfig()