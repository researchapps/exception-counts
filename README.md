# Exception Counts

This is a small exercise to look at exceptions for a little over 200 artifacts
in the spack build sandbox. There is a lot of redundancy, but it's better than
nothing! The script [has_exceptions.py](has_exceptions.py) was run within
the Smeagle container:

```bash
$ docker run -it -v $PWD:/code smeagle bash
```
with appropriate credentials exported, Smeagle added to the path,
and ipython and boto3 installed (see script header for details).
This generated [exception-counts.json](exception-counts.json). For results
without a count, we can assume that Dyninst didn't find any count.
We can then run the organize/parsing script to generate [exception-counts-processed.json](exception-counts-processed.json)
and print to the terminal:


```bash
$ python organize_results.py
boost-1.50.0-lnnxdnv3w25ghoe2jqyhjhnf7x6nzb7b libboost_unit_test_framework-mt.so has 1353 exceptions
boost-1.50.0-lnnxdnv3w25ghoe2jqyhjhnf7x6nzb7b libboost_graph-mt.so has 770 exceptions
boost-1.50.0-lnnxdnv3w25ghoe2jqyhjhnf7x6nzb7b libboost_math_tr1.so has 328 exceptions
boost-1.50.0-lnnxdnv3w25ghoe2jqyhjhnf7x6nzb7b libboost_locale.so has 2078 exceptions
boost-1.50.0-lnnxdnv3w25ghoe2jqyhjhnf7x6nzb7b libboost_unit_test_framework.so has 1353 exceptions
boost-1.50.0-lnnxdnv3w25ghoe2jqyhjhnf7x6nzb7b libboost_thread.so has 513 exceptions
boost-1.50.0-lnnxdnv3w25ghoe2jqyhjhnf7x6nzb7b libboost_math_c99l-mt.so has 316 exceptions
boost-1.50.0-lnnxdnv3w25ghoe2jqyhjhnf7x6nzb7b libboost_math_c99-mt.so has 316 exceptions
boost-1.50.0-lnnxdnv3w25ghoe2jqyhjhnf7x6nzb7b libboost_timer-mt.so has 19 exceptions
boost-1.50.0-lnnxdnv3w25ghoe2jqyhjhnf7x6nzb7b libboost_iostreams.so has 343 exceptions
boost-1.50.0-lnnxdnv3w25ghoe2jqyhjhnf7x6nzb7b libboost_thread-mt.so has 513 exceptions
boost-1.50.0-lnnxdnv3w25ghoe2jqyhjhnf7x6nzb7b libboost_signals-mt.so has 307 exceptions
boost-1.50.0-lnnxdnv3w25ghoe2jqyhjhnf7x6nzb7b libboost_graph.so has 770 exceptions
boost-1.50.0-lnnxdnv3w25ghoe2jqyhjhnf7x6nzb7b libboost_math_c99.so has 316 exceptions
boost-1.50.0-lnnxdnv3w25ghoe2jqyhjhnf7x6nzb7b libboost_random-mt.so has 23 exceptions
boost-1.50.0-lnnxdnv3w25ghoe2jqyhjhnf7x6nzb7b libboost_wave-mt.so has 1784 exceptions
boost-1.50.0-lnnxdnv3w25ghoe2jqyhjhnf7x6nzb7b libboost_serialization-mt.so has 752 exceptions
boost-1.50.0-lnnxdnv3w25ghoe2jqyhjhnf7x6nzb7b libboost_math_tr1-mt.so has 328 exceptions
boost-1.50.0-lnnxdnv3w25ghoe2jqyhjhnf7x6nzb7b libboost_chrono-mt.so has 4 exceptions
boost-1.50.0-lnnxdnv3w25ghoe2jqyhjhnf7x6nzb7b libboost_regex.so has 1718 exceptions
boost-1.50.0-lnnxdnv3w25ghoe2jqyhjhnf7x6nzb7b libboost_filesystem-mt.so has 330 exceptions
boost-1.50.0-lnnxdnv3w25ghoe2jqyhjhnf7x6nzb7b libboost_math_c99f-mt.so has 320 exceptions
boost-1.50.0-lnnxdnv3w25ghoe2jqyhjhnf7x6nzb7b libboost_iostreams-mt.so has 343 exceptions
boost-1.50.0-lnnxdnv3w25ghoe2jqyhjhnf7x6nzb7b libboost_prg_exec_monitor.so has 138 exceptions
boost-1.50.0-lnnxdnv3w25ghoe2jqyhjhnf7x6nzb7b libboost_math_c99f.so has 320 exceptions
boost-1.50.0-lnnxdnv3w25ghoe2jqyhjhnf7x6nzb7b libboost_program_options-mt.so has 1760 exceptions
boost-1.50.0-lnnxdnv3w25ghoe2jqyhjhnf7x6nzb7b libboost_chrono.so has 4 exceptions
boost-1.50.0-lnnxdnv3w25ghoe2jqyhjhnf7x6nzb7b libboost_date_time-mt.so has 111 exceptions
boost-1.50.0-lnnxdnv3w25ghoe2jqyhjhnf7x6nzb7b libboost_wserialization-mt.so has 544 exceptions
boost-1.50.0-lnnxdnv3w25ghoe2jqyhjhnf7x6nzb7b libboost_program_options.so has 1760 exceptions
boost-1.50.0-lnnxdnv3w25ghoe2jqyhjhnf7x6nzb7b libboost_math_tr1f-mt.so has 355 exceptions
boost-1.50.0-lnnxdnv3w25ghoe2jqyhjhnf7x6nzb7b libboost_signals.so has 307 exceptions
boost-1.50.0-lnnxdnv3w25ghoe2jqyhjhnf7x6nzb7b libboost_filesystem.so has 330 exceptions
boost-1.50.0-lnnxdnv3w25ghoe2jqyhjhnf7x6nzb7b libboost_random.so has 23 exceptions
boost-1.50.0-lnnxdnv3w25ghoe2jqyhjhnf7x6nzb7b libboost_math_c99l.so has 316 exceptions
boost-1.50.0-lnnxdnv3w25ghoe2jqyhjhnf7x6nzb7b libboost_date_time.so has 111 exceptions
boost-1.50.0-lnnxdnv3w25ghoe2jqyhjhnf7x6nzb7b libboost_math_tr1l-mt.so has 324 exceptions
boost-1.50.0-lnnxdnv3w25ghoe2jqyhjhnf7x6nzb7b libboost_math_tr1f.so has 355 exceptions
boost-1.50.0-lnnxdnv3w25ghoe2jqyhjhnf7x6nzb7b libboost_regex-mt.so has 1718 exceptions
boost-1.50.0-lnnxdnv3w25ghoe2jqyhjhnf7x6nzb7b libboost_locale-mt.so has 2078 exceptions
boost-1.50.0-lnnxdnv3w25ghoe2jqyhjhnf7x6nzb7b libboost_prg_exec_monitor-mt.so has 138 exceptions
boost-1.50.0-lnnxdnv3w25ghoe2jqyhjhnf7x6nzb7b libboost_wserialization.so has 544 exceptions
boost-1.50.0-lnnxdnv3w25ghoe2jqyhjhnf7x6nzb7b libboost_math_tr1l.so has 324 exceptions
boost-1.50.0-lnnxdnv3w25ghoe2jqyhjhnf7x6nzb7b libboost_serialization.so has 752 exceptions
boost-1.50.0-lnnxdnv3w25ghoe2jqyhjhnf7x6nzb7b libboost_wave.so has 1784 exceptions
boost-1.50.0-lnnxdnv3w25ghoe2jqyhjhnf7x6nzb7b libboost_timer.so has 19 exceptions
boost-1.55.0-7zjcspxxurinexwp35byw5boif4fe3xx libboost_log_setup.so has 4078 exceptions
boost-1.55.0-7zjcspxxurinexwp35byw5boif4fe3xx libboost_log.so has 2283 exceptions
boost-1.55.0-7zjcspxxurinexwp35byw5boif4fe3xx libboost_log_setup-mt.so has 4078 exceptions
boost-1.55.0-7zjcspxxurinexwp35byw5boif4fe3xx libboost_log-mt.so has 2283 exceptions
ncurses-6.0-ojquuwk3yazi2v4sq4iipmrcurdrwnbj libncurses++w.so has 52 exceptions
ncurses-6.0-ojquuwk3yazi2v4sq4iipmrcurdrwnbj libncurses++.so has 52 exceptions
openmpi-1.10.0-vqg5ps34oj35v5fbcrgvzalwjph4jo7o vtf90 has 341 exceptions
openmpi-1.10.0-vqg5ps34oj35v5fbcrgvzalwjph4jo7o vtfiltergen has 249 exceptions
openmpi-1.10.0-vqg5ps34oj35v5fbcrgvzalwjph4jo7o vtc++ has 341 exceptions
openmpi-1.10.0-vqg5ps34oj35v5fbcrgvzalwjph4jo7o vtunify-mpi has 387 exceptions
openmpi-1.10.0-vqg5ps34oj35v5fbcrgvzalwjph4jo7o vtfilter-mpi has 258 exceptions
openmpi-1.10.0-vqg5ps34oj35v5fbcrgvzalwjph4jo7o vtfiltergen-mpi has 258 exceptions
openmpi-1.10.0-vqg5ps34oj35v5fbcrgvzalwjph4jo7o vtcc has 341 exceptions
openmpi-1.10.0-vqg5ps34oj35v5fbcrgvzalwjph4jo7o vtcxx has 341 exceptions
openmpi-1.10.0-vqg5ps34oj35v5fbcrgvzalwjph4jo7o otfaux has 24 exceptions
openmpi-1.10.0-vqg5ps34oj35v5fbcrgvzalwjph4jo7o otfprofile has 517 exceptions
openmpi-1.10.0-vqg5ps34oj35v5fbcrgvzalwjph4jo7o vtfilter has 249 exceptions
openmpi-1.10.0-vqg5ps34oj35v5fbcrgvzalwjph4jo7o vtwrapper has 341 exceptions
openmpi-1.10.0-vqg5ps34oj35v5fbcrgvzalwjph4jo7o otfprint has 1 exceptions
openmpi-1.10.0-vqg5ps34oj35v5fbcrgvzalwjph4jo7o vtunify has 384 exceptions
openmpi-1.10.0-vqg5ps34oj35v5fbcrgvzalwjph4jo7o vtfort has 341 exceptions
openmpi-1.10.0-vqg5ps34oj35v5fbcrgvzalwjph4jo7o vtf77 has 341 exceptions
openmpi-1.10.0-vqg5ps34oj35v5fbcrgvzalwjph4jo7o vtCC has 341 exceptions
openmpi-1.10.0-vqg5ps34oj35v5fbcrgvzalwjph4jo7o opari has 226 exceptions
openmpi-1.10.0-vqg5ps34oj35v5fbcrgvzalwjph4jo7o otfshrink has 66 exceptions
openmpi-1.10.0-vqg5ps34oj35v5fbcrgvzalwjph4jo7o otfprofile-mpi has 547 exceptions
openmpi-1.10.0-vqg5ps34oj35v5fbcrgvzalwjph4jo7o libvt-mpi-unify.so has 389 exceptions
openmpi-1.3.1-lnz2vlqknrpdjgwhrky53yqwsqn7jw6k otfdump has 2 exceptions
```
