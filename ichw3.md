# 概论作业3 (Sep/25/2018) #

### Q : 详述通用的高速缓存存储器结构及工作原理
* 高速缓存存储器，即Cache，分为L1 Cache（CPU内）与L2 Cache（在L1 Cache和内存间）。Cache分为**direct-mapped、set-associative、fully-associative**多种组成方式。简单地说，Cache在逻辑结构上包括**data（数据）、tag（地址信息）以及valid（有效位）**。物理结构上，它包括*TCAM与SRAM*两部分，分别存储**tag array与data array**的数据内容。
* * Cache主要是为了调和高速昂贵的存储器（*SRAM*） 与低速廉价的存储器（*DRAM*）之间的效率矛盾。当CPU发出寻址信息时，先索引cache中的index，然后用tag部分相比较，得出是否缓存命中的结论。如果命中，则直接读取data，从而提高了数据传输速率；如果未命中，则需要从后备存储中访问更昂贵的数据。未命中时，采取**替换策略**，移除一些先前存在的高速缓存条目以便为新检索的数据腾出空间。优良的缓存算法能够进一步提高Cache命中率，从而提升效率。

  * 处理器微架构访问Cache的方法与访问主存储器有类似之处。主存储器使用地址编码方式，微架构可以地址寻址方式访问这些存储器。Cache也使用了类似的地址编码方式，微架构也是使用这些地址操纵着各级Cache，可以将数据写入Cache，也可以从Cache中读出内容。 

  * Cache的存在使得CPU Core的存储器读写操作略微显得复杂。CPU Core在进行存储器方式时，首先使用EPN(Effective Page Number)进行虚实地址转换，并同时使用CLN(Cache Line Number)查找合适的Cache Block。这两个步骤可以同时进行。在使用Virtual Cache时，还可以使用虚拟地址对Cache进行寻址。为简化起见，我们并不考虑Virtual Cache的实现细节。
   
   * EPN经过转换后得到VPN，之后在TLB中查找并得到最终的RPN(Real Page Number)。如果期间发生了TLB Miss，将带来一系列的严重的系统惩罚，我们只讨论TLB Hit的情况，此时将很快获得合适的RPN，并依此得到PA(Physical Address)。


   * 在多数处理器微架构中，Cache由多行多列组成，使用CLN进行索引最终可以得到一个完整的Cache Block。但是在这个Cache Block中的数据并不一定是CPU Core所需要的。因此有必要进行一些检查，将Cache Block中存放的Address与通过虚实地址转换得到的PA进行地址比较(Compare Address)。如果结果相同而且状态位匹配，则表明Cache Hit。此时微架构再经过Byte Select and Align部件最终获得所需要的数据。如果发生Cache Miss，CPU需要使用PA进一步索引主存储器获得最终的数据。

![image](http://s9.sinaimg.cn/large/6472c4ccgae0b93f864a8&690)

***
###### <p align="right">Friedrich Foo *from CCME* </p>
###### <p align="right">2018/10/5 </p>

