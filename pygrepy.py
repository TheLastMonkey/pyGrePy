def pygrepy(ops, rex, the_path):
    import subprocess
    grep_command = "grep {} {} {}".format(ops, rex, the_path)
    proc = subprocess.Popen([grep_command], stdout=subprocess.PIPE, shell=True)

    (out, err) = proc.communicate()
    out = out.decode("utf-8").split("\n")
    return out
