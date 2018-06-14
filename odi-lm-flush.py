# Add our last document to the batch
if output != "": addToBatch(output)

print >> log, "Flushing batch queue and waiting..."
writer.flushAndWait();
manager.stopJob(job);
print >> log, "DONE"