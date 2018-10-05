# 概论作业3 (Sep/25/2018) #

### Q : 详述通用的高速缓存存储器结构及工作原理
* 高速缓存存储器，即Cache，分为L1 Cache（CPU内）与L2 Cache（在L1 Cache和内存间）。Cache分为**direct-mapped、set-associative、fully-associative**多种组成方式。简单地说，Cache在逻辑结构上包括**data（数据）、tag（地址信息）以及valid（有效位）**。物理结构上，它包括*TCAM与SRAM*两部分，分别存储**tag array与data array**的数据内容。
* Cache主要是为了调和高速昂贵的存储器（*SRAM*） 与低速廉价的存储器（*DRAM*）之间的效率矛盾。当CPU发出寻址信息时，先先索引cache中的index，然后用tag部分相比较，得出是否缓存命中的结论。如果命中，则直接读取data，从而提高了数据传输速率；如果未命中，则需要从后备存储中访问更昂贵的数据。未命中时，采取**替换策略**，移除一些先前存在的高速缓存条目以便为新检索的数据腾出空间。优良的缓存算法能够进一步提高Cache命中率，从而提升效率。
***
###### <p align="right">Friedrich Foo *from CCME* </p>
###### <p align="right">2018/10/5 </p>

