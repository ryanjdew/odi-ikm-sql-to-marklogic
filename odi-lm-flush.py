print >> log, "Flushing batch queue and waiting..."
writer.flushAndWait();
manager.stopJob(job);
print >> log, "DONE"