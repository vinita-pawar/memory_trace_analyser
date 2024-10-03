# memory_trace_analyser
Analyse memory access pattern from memory trace derived from maphea analyser.

Input is a .csv file with traces.

Example of trace :
```
dbtest,231156.772509,"mem-loads,ldlat=4",4503567599274575.0,L1 or,482,ffff88afa0a4f138,9,SNP None,TLB L1 or L2 hit,LCK No

Important fields (starting from 0):
0: executable file name (dbtest)
1: timestamp (231156.772509)
4: Memory hierarchy where the load / store occurred (L1, L2, L3, DRAM) (L1 or)
5: Number of samples (482)
6: Memory virtual address (ffff88afa0a4f138)
7: Latency (9)
```

In the above example, there are 482 load instructions from L1 cache at address 0xffff88afa0a4f138, which were sampled at timestamp of: 231156.772509 from dbtest.
