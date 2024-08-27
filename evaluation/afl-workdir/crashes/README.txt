Command line used to find this crash:

/home/tenebris/Disk/Documents/RootCauseAnalysisPruning/evaluation/afl-fuzz/afl-fuzz -C -d -m none -i /home/tenebris/Disk/Documents/RootCauseAnalysisPruning/evaluation/seed/libxml2_seed -o /home/tenebris/Disk/Documents/RootCauseAnalysisPruning/evaluation/afl-workdir -- /home/tenebris/Disk/Documents/RootCauseAnalysisPruning/evaluation/test_bin/libxml2/xmllint_fuzz --recover @@

If you can't reproduce a bug outside of afl-fuzz, be sure to set the same
memory limit. The limit used for this fuzzing session was 0 B.

Need a tool to minimize test cases before investigating the crashes or sending
them to a vendor? Check out the afl-tmin that comes with the fuzzer!

Found any cool bugs in open-source tools using afl-fuzz? If yes, please drop
me a mail at <lcamtuf@coredump.cx> once the issues are fixed - I'd love to
add your finds to the gallery at:

  http://lcamtuf.coredump.cx/afl/

Thanks :-)
