
(checkpoint_restart)=
# Checkpoint files and restarts

Checkpoint files are dumps of all the information needed to restart a
computation at the time of the checkpoint.

Some reasons you might want to do this:
- For long simulations that take a lot of computer time, 
  it's good to write out checkpoint files periodically in case the run dies
  at some point (e.g. if you are running on a supercomputer with a time
  limit and you run out of time).
- A checkpoint file written at the end of the simulation can be used to run
  out farther in time if you decide you need to.
- You might want to restart the simulation at some intermediate time and
  specify more frequent outputs, if you something interesting happened that
  wasn't captured in your original output times.

See [Checkpointing and restarting](https://www.clawpack.org/restart.html)
in the Clawpack documentation for details on how to specify checkpoint
intervals and how to restart from a checkpoint file.

