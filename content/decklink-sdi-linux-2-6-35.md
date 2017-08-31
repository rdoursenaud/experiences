Title: Decklink SDI Linux 2.6.35
Date: 2010-09-01 09:07
Category: Blog
Tags: GNU/Linux, Blackmagic Design, Decklink
Slug: decklink-sdi-linux-2-6-35
Status: draft

Here's a patch allowing the
[blackmagic](http://www.blackmagic-design.com/) kernel module to  
  
build against 2.6.35 linux kernel.

    diff -Nurp DeckLink-7.6.3/blackmagic_lib.c DeckLink-7.6.3-2.6.35//blackmagic_lib.c
    --- DeckLink-7.6.3/blackmagic_lib.c 2010-04-19 05:30:38.000000000 +0200
    +++ DeckLink-7.6.3-2.6.35//blackmagic_lib.c 2010-07-05 23:52:12.498000012 +0200
    @@ -726,7 +726,9 @@ dl_kernel_fpu_begin()
            #define FX_SAVE_INSTR   "fxsave %0; fnclex"
     #endif
     
    -#if LINUX_VERSION_CODE >= KERNEL_VERSION(2, 6, 26)
    +#if LINUX_VERSION_CODE >= KERNEL_VERSION(2, 6, 35)
    +                asm volatile(FX_SAVE_INSTR : "=m" (thread->task->thread.fpu.state->fxsave));
    +#elif LINUX_VERSION_CODE >= KERNEL_VERSION(2, 6, 26)
            asm volatile(FX_SAVE_INSTR : "=m" (thread->task->thread.xstate->fxsave));
     #else
            asm volatile(FX_SAVE_INSTR : "=m" (thread->task->thread.i387.fxsave));
