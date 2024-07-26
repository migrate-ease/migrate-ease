#include <iostream>
#include <thread>
#include <cassert>

typedef volatile int64_t easy_atomic_t; 
#define YIELD_PROCESSOR __asm__ __volatile__("yield")

#define easy_atomic_cmp_set(lock, cmp, set)     __sync_bool_compare_and_swap(lock, cmp, set)
#define easy_unlock(lock)   {__asm__ ("" ::: "memory"); *(lock) = 0;}
#define easy_spin_unlock easy_unlock

static __inline__ void easy_spin_lock(easy_atomic_t *lock)
{
    int                     i, n;

    for ( ; ; ) {
        if (*lock == 0 && easy_atomic_cmp_set(lock, 0, 1)) {
            return;
        }

        for (n = 1; n < 1024; n <<= 1) {

            for (i = 0; i < n; i++) {
                YIELD_PROCESSOR;
            }

            if (*lock == 0 && easy_atomic_cmp_set(lock, 0, 1)) {
                return;
            }
        }

        sched_yield();
    }
}

static int64_t N = 1000000;
// prevent modified data are in the same cache line
static int64_t count[23] = {0};
static int64_t count1 = 0;
static int64_t count2 = 0;
static int64_t count3 = 0;
static int64_t count4 = 0;
easy_atomic_t lock;

void func() {
    int64_t c = N;
    while (c--) {
	easy_spin_lock(&lock);
	count1++;
	count[22]++;
	// unlock maybe reordered at run time in aarch64
	easy_spin_unlock(&lock);
    }
}

int main() {
  while (true) {
    count1 = 0;
    count2 = 0;
    count3 = 0;
    count4 = 0;
    std::thread c1(func);
    std::thread c2(func);
    std::thread c3(func);
    std::thread c4(func);
    std::thread c5(func);
    c1.join();
    c2.join();
    c3.join();
    c4.join();
    c5.join();
   assert(count1 == 5*N);
   assert(count[22] == 5*N);
  }
}

/*
 * ref: https://topic.atatech.org/articles/146494
 * */
/*
case: case.cc: int main(): Assertion `count1 == 5*N' failed.
Aborted 
*/

/*
Architecture:          aarch64
Byte Order:            Little Endian
CPU(s):                128
On-line CPU(s) list:   0-127
Thread(s) per core:    1
Core(s) per socket:    64
Socket(s):             2
NUMA node(s):          4
Model:                 0
CPU max MHz:           2600.0000
CPU min MHz:           200.0000
BogoMIPS:              200.00
L1d cache:             64K
L1i cache:             64K
L2 cache:              512K
L3 cache:              65536K
NUMA node0 CPU(s):     0-31
NUMA node1 CPU(s):     32-63
NUMA node2 CPU(s):     64-95
NUMA node3 CPU(s):     96-127
Flags:                 fp asimd evtstrm aes pmull sha1 sha2 crc32 atomics fphp asimdhp cpuid asimdrdm jscvt fcma dcpop asimddp asimdfhm
*/
